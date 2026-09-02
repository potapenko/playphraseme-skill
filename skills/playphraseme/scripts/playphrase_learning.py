#!/usr/bin/env python3
"""Bounded zero-dependency client for the public PlayPhrase.me Learning API."""

from __future__ import annotations

import argparse
import ipaddress
import json
import socket
import sys
from dataclasses import dataclass
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urljoin, urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener


PRODUCTION_BASE = "https://www.playphrase.me/api/v1/learning"
LEARNING_PREFIX = "/api/v1/learning"
PATHS = {
    "suggestions": "/common-phrases/suggestions",
    "phrases": "/common-phrases",
    "words": "/common-words",
}
LEVELS = ("A1", "A2", "B1", "B2", "C1", "C2")
SORTS = {"usefulness", "travel-utility", "daily-utility", "business-utility"}
EMOTIONS = {
    "angry", "anxious", "assertive", "concerned", "confident", "confused",
    "determined", "embarrassed", "empathetic", "excited", "fearful",
    "friendly", "frustrated", "happy", "hopeful", "nervous", "neutral",
    "nostalgic", "other", "romantic", "sad", "sarcastic", "scared",
    "serious", "skeptical", "supportive", "surprised", "urgent", "worried",
}
POLARITIES = {"negative", "neutral", "positive"}
TOPICS = {
    "art", "business", "daily-life", "decision-making", "education",
    "emergency", "entertainment", "family", "government", "health",
    "healthcare", "history", "language", "law", "legal", "life",
    "literature", "medical", "personal development", "personal-development",
    "personal-reflection", "philosophy", "politics", "problem-solving",
    "relationship", "relationships", "religion", "sports", "transportation",
    "travel", "work", "other",
}
MAX_BODY_BYTES = 1024 * 1024
MAX_TIMEOUT_SECONDS = 10.0


class LearningClientError(RuntimeError):
    exit_code = 10


class InputError(LearningClientError):
    exit_code = 2


class TimeoutFailure(LearningClientError):
    exit_code = 3


class BadRequestFailure(LearningClientError):
    exit_code = 4


class RateLimitFailure(LearningClientError):
    exit_code = 5

    def __init__(self, message: str, retry_after: str | None = None):
        super().__init__(message)
        self.retry_after = retry_after


class HTTPFailure(LearningClientError):
    exit_code = 6


class RedirectPolicyFailure(LearningClientError):
    exit_code = 7


class ResponseTooLargeFailure(LearningClientError):
    exit_code = 8


class InvalidJSONFailure(LearningClientError):
    exit_code = 9


@dataclass(frozen=True)
class ValidatedBase:
    url: str
    origin: tuple[str, str, int | None]


def _is_loopback(hostname: str | None) -> bool:
    if not hostname:
        return False
    if hostname.lower() == "localhost":
        return True
    try:
        return ipaddress.ip_address(hostname).is_loopback
    except ValueError:
        return False


def _origin(parts: Any) -> tuple[str, str, int | None]:
    return (parts.scheme.lower(), (parts.hostname or "").lower(), parts.port)


def validate_base_url(base_url: str) -> ValidatedBase:
    parts = urlsplit(base_url)
    if parts.scheme not in {"http", "https"} or not parts.netloc:
        raise InputError("base URL must be an http(s) URL")
    if parts.username or parts.password or parts.query or parts.fragment:
        raise InputError("base URL must not contain credentials, query, or fragment")
    if parts.path.rstrip("/") != LEARNING_PREFIX:
        raise InputError(f"base URL path must be exactly {LEARNING_PREFIX}")
    normalized = f"{parts.scheme}://{parts.netloc}{LEARNING_PREFIX}"
    if normalized != PRODUCTION_BASE and not _is_loopback(parts.hostname):
        raise InputError("--base-url override is restricted to loopback hosts")
    return ValidatedBase(normalized, _origin(parts))


def _bounded_int(value: Any, *, default: int, minimum: int, maximum: int, field: str) -> int:
    if value is None:
        return default
    try:
        parsed = int(value)
    except (TypeError, ValueError) as exc:
        raise InputError(f"{field} must be an integer") from exc
    return max(minimum, min(maximum, parsed))


def _text(value: Any, field: str, *, required: bool = False) -> str | None:
    if value is None:
        if required:
            raise InputError(f"{field} is required")
        return None
    text = str(value).strip()
    if not text:
        if required:
            raise InputError(f"{field} must not be blank")
        return None
    return text


def _language(value: Any, field: str = "language") -> str:
    text = _text(value, field, required=True) or ""
    if len(text) > 32 or any(character.isspace() for character in text):
        raise InputError(f"{field} is invalid")
    return text


def _levels(level_from: str, level_to: str) -> tuple[str, str]:
    level_from = level_from.upper()
    level_to = level_to.upper()
    if level_from not in LEVELS or level_to not in LEVELS:
        raise InputError("language levels must be CEFR A1-C2")
    if LEVELS.index(level_from) > LEVELS.index(level_to):
        raise InputError("language-level-from must not exceed language-level-to")
    return level_from, level_to


def build_request(command: str, options: dict[str, Any], base_url: str = PRODUCTION_BASE) -> tuple[str, ValidatedBase]:
    if command not in PATHS:
        raise InputError("unsupported Learning API command")
    validated = validate_base_url(base_url)
    language = _language(options.get("language", "en"))
    translate_to = options.get("translate_to")
    if translate_to is not None:
        translate_to = _language(translate_to, "translate-to")
    limit = _bounded_int(options.get("limit"), default=10, minimum=1, maximum=20, field="limit")
    params: list[tuple[str, Any]] = [("language", language)]
    if translate_to:
        params.append(("translate-to", translate_to))

    if command == "suggestions":
        query = _text(options.get("query"), "query", required=True) or ""
        if len(query) > 200:
            raise InputError("query must be at most 200 characters")
        params = [("q", query), *params, ("limit", limit)]
    else:
        skip = _bounded_int(options.get("skip"), default=0, minimum=0, maximum=1000, field="skip")
        level_from, level_to = _levels(
            str(options.get("language_level_from", "A1")),
            str(options.get("language_level_to", "C2")),
        )
        params.extend([
            ("skip", skip),
            ("limit", limit),
            ("language-level-from", level_from),
            ("language-level-to", level_to),
        ])
        if command == "phrases":
            if options.get("idiom"):
                params.append(("idiom", "true"))
            if options.get("is_question"):
                params.append(("is-question", "true"))
            for option_key, api_key in (
                ("emotion", "emotion"),
                ("polarity", "polarity"),
                ("topic", "topic"),
            ):
                value = _text(options.get(option_key), api_key)
                if value:
                    allowed_values = {
                        "emotion": EMOTIONS,
                        "polarity": POLARITIES,
                        "topic": TOPICS,
                    }[option_key]
                    if value not in allowed_values:
                        raise InputError(f"unsupported {api_key}")
                    params.append((api_key, value))
        else:
            for option_key, api_key in (
                ("domain", "domain"),
                ("part_of_speech", "part-of-speech"),
            ):
                value = _text(options.get(option_key), api_key)
                if value:
                    params.append((api_key, value))
            if options.get("is_slang"):
                params.append(("is-slang", "true"))
            sort_by = str(options.get("sort_by", "usefulness"))
            if sort_by not in SORTS:
                raise InputError("unsupported sort-by")
            params.append(("sort-by", sort_by))

    endpoint = validated.url + PATHS[command]
    return endpoint + "?" + urlencode(params), validated


class _SafeRedirectHandler(HTTPRedirectHandler):
    def __init__(self, validated_base: ValidatedBase):
        super().__init__()
        self.validated_base = validated_base
        self.redirect_count = 0

    def redirect_request(self, req: Request, fp: Any, code: int, msg: str, headers: Any, newurl: str) -> Request | None:
        self.redirect_count += 1
        if self.redirect_count > 1:
            raise RedirectPolicyFailure("more than one redirect is not allowed")
        target = urlsplit(urljoin(req.full_url, newurl))
        if _origin(target) != self.validated_base.origin:
            raise RedirectPolicyFailure("cross-origin redirect was rejected")
        if not (target.path == LEARNING_PREFIX or target.path.startswith(LEARNING_PREFIX + "/")):
            raise RedirectPolicyFailure("redirect outside the Learning API prefix was rejected")
        if target.username or target.password or target.fragment:
            raise RedirectPolicyFailure("redirect contains forbidden URL components")
        return super().redirect_request(req, fp, code, msg, headers, target.geturl())


def fetch_json(url: str, validated_base: ValidatedBase, *, timeout: float = MAX_TIMEOUT_SECONDS) -> dict[str, Any]:
    try:
        timeout = float(timeout)
    except (TypeError, ValueError) as exc:
        raise InputError("timeout must be a number") from exc
    if timeout <= 0 or timeout > MAX_TIMEOUT_SECONDS:
        raise InputError("timeout must be greater than 0 and no more than 10 seconds")
    handler = _SafeRedirectHandler(validated_base)
    opener = build_opener(handler)
    request = Request(
        url,
        method="GET",
        headers={"Accept": "application/json", "User-Agent": "playphraseme-skill/1.0"},
    )
    try:
        with opener.open(request, timeout=timeout) as response:
            content_length = response.headers.get("Content-Length")
            if content_length:
                try:
                    if int(content_length) > MAX_BODY_BYTES:
                        raise ResponseTooLargeFailure("response body exceeds 1 MiB")
                except ValueError:
                    pass
            body = response.read(MAX_BODY_BYTES + 1)
            if len(body) > MAX_BODY_BYTES:
                raise ResponseTooLargeFailure("response body exceeds 1 MiB")
    except HTTPError as exc:
        if exc.code == 400:
            exc.close()
            raise BadRequestFailure("Learning API returned 400 Bad Request") from exc
        if exc.code == 429:
            retry_after = exc.headers.get("Retry-After")
            exc.close()
            raise RateLimitFailure(
                "Learning API rate limit reached",
                retry_after=retry_after,
            ) from exc
        code = exc.code
        exc.close()
        raise HTTPFailure(f"Learning API returned HTTP {code}") from exc
    except (TimeoutError, socket.timeout) as exc:
        raise TimeoutFailure("Learning API request timed out") from exc
    except RedirectPolicyFailure:
        raise
    except URLError as exc:
        if isinstance(exc.reason, (TimeoutError, socket.timeout)):
            raise TimeoutFailure("Learning API request timed out") from exc
        raise HTTPFailure(f"Learning API request failed: {exc.reason}") from exc

    try:
        payload = json.loads(body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise InvalidJSONFailure("Learning API response is not valid UTF-8 JSON") from exc
    if not isinstance(payload, dict):
        raise InvalidJSONFailure("Learning API response must be a JSON object")
    return payload


def _extract_global_options(argv: list[str]) -> tuple[list[str], str, float]:
    cleaned: list[str] = []
    base_url = PRODUCTION_BASE
    timeout = MAX_TIMEOUT_SECONDS
    index = 0
    while index < len(argv):
        item = argv[index]
        if item in {"--base-url", "--timeout"}:
            if index + 1 >= len(argv):
                raise InputError(f"{item} requires a value")
            value = argv[index + 1]
            if item == "--base-url":
                base_url = value
            else:
                try:
                    timeout = float(value)
                except ValueError as exc:
                    raise InputError("timeout must be a number") from exc
            index += 2
        elif item.startswith("--base-url="):
            base_url = item.split("=", 1)[1]
            index += 1
        elif item.startswith("--timeout="):
            try:
                timeout = float(item.split("=", 1)[1])
            except ValueError as exc:
                raise InputError("timeout must be a number") from exc
            index += 1
        else:
            cleaned.append(item)
            index += 1
    return cleaned, base_url, timeout


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    suggestions = subparsers.add_parser("suggestions")
    suggestions.add_argument("--query", required=True)
    suggestions.add_argument("--language", default="en")
    suggestions.add_argument("--translate-to")
    suggestions.add_argument("--limit", default=10)

    for name in ("phrases", "words"):
        command = subparsers.add_parser(name)
        command.add_argument("--language", default="en")
        command.add_argument("--translate-to")
        command.add_argument("--skip", default=0)
        command.add_argument("--limit", default=10)
        command.add_argument("--language-level-from", default="A1")
        command.add_argument("--language-level-to", default="C2")
        if name == "phrases":
            command.add_argument("--idiom", action="store_true")
            command.add_argument("--is-question", "--question", dest="is_question", action="store_true")
            command.add_argument("--emotion")
            command.add_argument("--polarity")
            command.add_argument("--topic")
        else:
            command.add_argument("--domain")
            command.add_argument("--part-of-speech")
            command.add_argument("--is-slang", "--slang", dest="is_slang", action="store_true")
            command.add_argument("--sort-by", choices=sorted(SORTS), default="usefulness")
    return parser


def main(argv: list[str] | None = None) -> int:
    try:
        cleaned, base_url, timeout = _extract_global_options(list(argv or sys.argv[1:]))
        args = _parser().parse_args(cleaned)
        options = vars(args).copy()
        command = options.pop("command")
        url, validated = build_request(command, options, base_url)
        payload = fetch_json(url, validated, timeout=timeout)
        print(json.dumps(payload, ensure_ascii=False, separators=(",", ":")))
        return 0
    except RateLimitFailure as exc:
        suffix = f"; Retry-After={exc.retry_after}" if exc.retry_after else ""
        print(f"error: {exc}{suffix}", file=sys.stderr)
        return exc.exit_code
    except LearningClientError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return exc.exit_code


if __name__ == "__main__":
    raise SystemExit(main())

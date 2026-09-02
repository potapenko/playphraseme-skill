#!/usr/bin/env python3
"""Build, decode, and validate public learner-facing PlayPhrase.me URLs."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections.abc import Iterable, Mapping
from typing import Any
from urllib.parse import parse_qsl, quote, unquote, urlencode, urlsplit


PRODUCTION_ORIGIN = "https://www.playphrase.me"
LEVELS = ("A1", "A2", "B1", "B2", "C1", "C2")
EMOTIONS = {
    "angry", "anxious", "assertive", "concerned", "confident", "confused",
    "determined", "embarrassed", "empathetic", "excited", "fearful",
    "friendly", "frustrated", "happy", "hopeful", "nervous", "neutral",
    "nostalgic", "other", "romantic", "sad", "sarcastic", "scared",
    "serious", "skeptical", "supportive", "surprised", "urgent", "worried",
}
TOPICS = {
    "art", "business", "daily-life", "decision-making", "education",
    "emergency", "entertainment", "family", "government", "health",
    "healthcare", "history", "language", "law", "legal", "life",
    "literature", "medical", "personal development", "personal-development",
    "personal-reflection", "philosophy", "politics", "problem-solving",
    "relationship", "relationships", "religion", "sports", "transportation",
    "travel", "work", "other",
}
POLARITIES = {"negative", "neutral", "positive"}
PARTS_OF_SPEECH = {"verb", "noun", "adjective", "adverb"}
WORD_SORTS = {
    "usefulness", "travel-utility", "daily-utility", "business-utility",
}
SOURCE_KINDS = {"movie", "episode", "tv-special"}
REELS_SOURCES = {"common-phrases", "common-words", "favorites", "custom-search"}
CUSTOM_TYPES = {"phrases", "words", "favorites"}
COMMON_PHRASE_DEFAULTS: dict[str, Any] = {
    "idiom": False,
    "is-question": False,
    "language-level-from": "A1",
    "language-level-to": "C2",
    "emotion": None,
    "polarity": None,
    "topic": None,
}
COMMON_WORD_DEFAULTS: dict[str, Any] = {
    "language-level-from": "A1",
    "language-level-to": "C2",
    "domain": None,
    "part-of-speech": None,
    "is-slang": False,
    "offensive-filter": "exclude",
    "sort-by": "usefulness",
}
CLIP_ARRAY_FIELDS = {"genre", "cast-actor", "voice-detection", "director"}
CLIP_SINGLE_FIELDS = {"source-kind", "movie-id", "imdb", "serie-imdb"}
CLIP_ALIASES = {"actor": "cast-actor", "year-range": "year"}
EXACT_SOURCE_FIELDS = {"movie-id", "imdb"}
GENERIC_SOURCE_FIELDS = {
    "year", "source-kind", "genre", "cast-actor", "voice-detection", "director",
}


class URLContractError(ValueError):
    """Raised when a requested URL cannot be represented by the public contract."""


def _clean_text(value: Any, field: str, *, required: bool = False) -> str | None:
    if value is None:
        if required:
            raise URLContractError(f"{field} is required")
        return None
    text = str(value).strip()
    if not text:
        if required:
            raise URLContractError(f"{field} must not be empty")
        return None
    return text


def _parse_bool(value: Any, field: str) -> bool:
    if isinstance(value, bool):
        return value
    text = str(value).strip().lower()
    if text in {"true", "1", "yes", "on"}:
        return True
    if text in {"false", "0", "no", "off"}:
        return False
    raise URLContractError(f"{field} must be true or false")


def _parse_nonnegative_int(value: Any, field: str) -> int:
    try:
        parsed = int(value)
    except (TypeError, ValueError) as exc:
        raise URLContractError(f"{field} must be an integer") from exc
    if parsed < 0:
        raise URLContractError(f"{field} must be non-negative")
    return parsed


def _parse_year(value: Any) -> int | dict[str, int]:
    if isinstance(value, Mapping):
        raw_min, raw_max = value.get("min"), value.get("max")
    elif isinstance(value, int):
        return value
    else:
        text = str(value).strip()
        if not text:
            raise URLContractError("year must not be empty")
        if text.startswith("{"):
            try:
                decoded = json.loads(text)
            except json.JSONDecodeError as exc:
                raise URLContractError("year JSON is invalid") from exc
            if not isinstance(decoded, Mapping):
                raise URLContractError("year JSON must be an object")
            raw_min, raw_max = decoded.get("min"), decoded.get("max")
        else:
            match = re.fullmatch(r"(\d{4})\s*(?:\.\.|-|:)\s*(\d{4})", text)
            if match:
                raw_min, raw_max = match.groups()
            elif re.fullmatch(r"\d{4}", text):
                return int(text)
            else:
                raise URLContractError("year must be YYYY or YYYY..YYYY")
    try:
        year_min, year_max = int(raw_min), int(raw_max)
    except (TypeError, ValueError) as exc:
        raise URLContractError("year range requires integer min and max") from exc
    if year_min > year_max:
        raise URLContractError("year range min must not exceed max")
    return {"min": year_min, "max": year_max}


def _origin(base_url: str) -> str:
    parts = urlsplit(base_url)
    if parts.scheme not in {"http", "https"} or not parts.netloc:
        raise URLContractError("base URL must be an http(s) origin")
    if parts.username or parts.password or parts.query or parts.fragment:
        raise URLContractError("base URL must not contain credentials, query, or fragment")
    if parts.path not in {"", "/"}:
        raise URLContractError("base URL must not contain a path")
    return f"{parts.scheme}://{parts.netloc}".rstrip("/")


def _compact_json(value: Mapping[str, Any]) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _app_url(base_url: str, route: str, params: Iterable[tuple[str, Any]]) -> str:
    origin = _origin(base_url)
    pairs = [(key, str(value)) for key, value in params if value is not None and value != ""]
    query = urlencode(pairs, doseq=False)
    return f"{origin}/#/{route}" + (f"?{query}" if query else "")


def _result(url: str, mode: str, state: Mapping[str, Any], warnings: list[str] | None = None) -> dict[str, Any]:
    return {
        "url": url,
        "mode": mode,
        "state": dict(state),
        "warnings": list(warnings or []),
    }


def build_search(
    query: str,
    *,
    language: str = "en",
    exact: bool = False,
    grammar: bool = False,
    pos: int = 0,
    base_url: str = PRODUCTION_ORIGIN,
) -> dict[str, Any]:
    query = _clean_text(query, "query", required=True) or ""
    language = _clean_text(language, "language", required=True) or "en"
    pos = _parse_nonnegative_int(pos, "pos")
    if grammar:
        if language != "en":
            raise URLContractError("grammar mode is supported only for the English corpus")
        query = re.sub(r"^(?:gr:\s*)+", "", query, flags=re.IGNORECASE).strip()
        query = f"gr: {query}"
    if grammar and exact:
        raise URLContractError("exact and grammar modes cannot be combined")
    if exact:
        if not (len(query) >= 2 and query.startswith('"') and query.endswith('"')):
            query = f'"{query}"'
    state: dict[str, Any] = {"language": language, "q": query}
    params: list[tuple[str, Any]] = [("language", language), ("q", query)]
    if pos:
        state["pos"] = pos
        params.append(("pos", pos))
    return _result(_app_url(base_url, "search", params), "search", state)


def _parse_filter_assignments(assignments: Iterable[str]) -> list[tuple[str, str]]:
    result: list[tuple[str, str]] = []
    for assignment in assignments:
        if "=" not in assignment:
            raise URLContractError(f"filter must use KEY=VALUE: {assignment}")
        key, value = assignment.split("=", 1)
        key = key.strip()
        if not key:
            raise URLContractError("filter key must not be empty")
        result.append((key, value.strip()))
    return result


def normalize_catalog_filters(source: str, raw: Mapping[str, Any]) -> dict[str, Any]:
    if source == "common-phrases":
        allowed = set(COMMON_PHRASE_DEFAULTS)
        defaults = COMMON_PHRASE_DEFAULTS
    elif source == "common-words":
        allowed = set(COMMON_WORD_DEFAULTS)
        defaults = COMMON_WORD_DEFAULTS
    else:
        raise URLContractError("catalog source must be common-phrases or common-words")
    unknown = sorted(set(raw) - allowed)
    if unknown:
        raise URLContractError(f"unsupported {source} filter(s): {', '.join(unknown)}")

    normalized: dict[str, Any] = {}
    for key, value in raw.items():
        if value is None or value == "":
            continue
        if key in {"idiom", "is-question", "is-slang"}:
            parsed: Any = _parse_bool(value, key)
        elif key in {"language-level-from", "language-level-to"}:
            parsed = str(value).upper()
            if parsed not in LEVELS:
                raise URLContractError(f"{key} must be a CEFR level A1-C2")
        elif key == "emotion":
            parsed = str(value)
            if parsed not in EMOTIONS:
                raise URLContractError("unsupported emotion")
        elif key == "polarity":
            parsed = str(value)
            if parsed not in POLARITIES:
                raise URLContractError("unsupported polarity")
        elif key == "topic":
            parsed = str(value)
            if parsed not in TOPICS:
                raise URLContractError("unsupported topic")
        elif key == "part-of-speech":
            parsed = str(value)
            if parsed not in PARTS_OF_SPEECH:
                raise URLContractError("unsupported part-of-speech")
        elif key == "offensive-filter":
            parsed = str(value)
            if parsed not in {"exclude", "include", "only"}:
                raise URLContractError("unsupported offensive-filter")
        elif key == "sort-by":
            parsed = str(value)
            if parsed not in WORD_SORTS:
                raise URLContractError("unsupported sort-by")
        else:
            parsed = _clean_text(value, key)
        if parsed != defaults[key] and parsed is not None:
            normalized[key] = parsed

    level_from = normalized.get("language-level-from", defaults["language-level-from"])
    level_to = normalized.get("language-level-to", defaults["language-level-to"])
    if LEVELS.index(level_from) > LEVELS.index(level_to):
        raise URLContractError("language-level-from must not exceed language-level-to")
    return dict(sorted(normalized.items()))


def build_catalog(
    source: str,
    *,
    language: str = "en",
    offset: int = 0,
    filters: Mapping[str, Any] | None = None,
    base_url: str = PRODUCTION_ORIGIN,
) -> dict[str, Any]:
    language = _clean_text(language, "language", required=True) or "en"
    offset = _parse_nonnegative_int(offset, "offset")
    normalized = normalize_catalog_filters(source, filters or {})
    state: dict[str, Any] = {"language": language, "source": source, "filters": normalized}
    params: list[tuple[str, Any]] = [("language", language), ("source", source)]
    if normalized:
        params.append(("filters", _compact_json(normalized)))
    if offset:
        state["offset"] = offset
        params.append(("offset", offset))
    return _result(_app_url(base_url, "search", params), "catalog", state)


def _coerce_array(value: Any, field: str) -> list[str]:
    values = value if isinstance(value, list) else [value]
    result: list[str] = []
    for item in values:
        text = _clean_text(item, field)
        if text and text not in result:
            result.append(text)
    return result


def normalize_clip_filters(raw: Mapping[str, Any], language: str) -> tuple[dict[str, Any], list[str]]:
    merged: dict[str, Any] = {}
    warnings: list[str] = []
    for incoming_key, value in raw.items():
        key = CLIP_ALIASES.get(incoming_key, incoming_key)
        if key == "year":
            merged[key] = _parse_year(value)
        elif key in CLIP_ARRAY_FIELDS:
            values = _coerce_array(value, key)
            if values:
                existing = merged.get(key, [])
                merged[key] = _coerce_array([*existing, *values], key)
        elif key in CLIP_SINGLE_FIELDS:
            text = _clean_text(value, key)
            if text:
                merged[key] = text
        else:
            raise URLContractError(f"unsupported Clip Search filter: {incoming_key}")

    if "source-kind" in merged and merged["source-kind"] not in SOURCE_KINDS:
        raise URLContractError("unsupported source-kind")
    if len(merged.get("voice-detection", [])) > 1:
        raise URLContractError("voice-detection accepts at most one value")
    if language != "en" and "voice-detection" in merged:
        del merged["voice-detection"]
        warnings.append("voice-detection was removed because it is supported only for English")
    exact = sorted(EXACT_SOURCE_FIELDS.intersection(merged))
    generic = sorted(GENERIC_SOURCE_FIELDS.intersection(merged))
    if exact and generic:
        warnings.append(
            f"exact source filter {exact[0]} makes generic metadata filters ineffective: "
            + ", ".join(generic)
        )
    return dict(sorted(merged.items())), warnings


def build_clip_search(
    *,
    query: str | None = None,
    language: str = "en",
    filters: Mapping[str, Any] | None = None,
    base_url: str = PRODUCTION_ORIGIN,
) -> dict[str, Any]:
    language = _clean_text(language, "language", required=True) or "en"
    query = _clean_text(query, "query")
    normalized, warnings = normalize_clip_filters(filters or {}, language)
    state: dict[str, Any] = {"language": language, "filters": normalized}
    params: list[tuple[str, Any]] = [("language", language)]
    if query:
        state["q"] = query
        params.append(("q", query))
    if normalized:
        params.append(("filters", _compact_json(normalized)))
    return _result(_app_url(base_url, "clip-search", params), "clip-search", state, warnings)


def build_reels(
    *,
    source: str | None = None,
    query: str | None = None,
    language: str = "en",
    translate_direction: str | None = None,
    offset: int = 0,
    filters: Mapping[str, Any] | None = None,
    collection_id: str | None = None,
    shuffle_seed: str | None = None,
    custom_type: str | None = None,
    base_url: str = PRODUCTION_ORIGIN,
) -> dict[str, Any]:
    language = _clean_text(language, "language", required=True) or "en"
    source = _clean_text(source, "source")
    if source and source not in REELS_SOURCES:
        raise URLContractError("unsupported Reels source")
    query = _clean_text(query, "query")
    translate_direction = _clean_text(translate_direction, "translate-direction")
    collection_id = _clean_text(collection_id, "collection-id")
    shuffle_seed = _clean_text(shuffle_seed, "shuffle-seed")
    custom_type = _clean_text(custom_type, "ct")
    if custom_type and custom_type not in CUSTOM_TYPES:
        raise URLContractError("unsupported custom-search collection type")
    offset = _parse_nonnegative_int(offset, "offset")
    warnings: list[str] = []
    if filters:
        if source not in {"common-phrases", "common-words"}:
            raise URLContractError("Reels filters are supported only for catalog sources")
        normalized_filters = normalize_catalog_filters(source, filters)
    else:
        normalized_filters = {}
    if translate_direction == language:
        translate_direction = None
        warnings.append("same-language translate-direction was removed")
    if collection_id and source != "favorites":
        raise URLContractError("collection-id requires source=favorites")
    if shuffle_seed and source != "favorites":
        raise URLContractError("shuffle-seed requires source=favorites")
    if custom_type and source != "custom-search":
        raise URLContractError("ct requires source=custom-search")

    state: dict[str, Any] = {"language": language}
    params: list[tuple[str, Any]] = []
    for key, value in (("source", source), ("q", query)):
        if value:
            state[key] = value
            params.append((key, value))
    if normalized_filters:
        state["filters"] = normalized_filters
        params.append(("filters", _compact_json(normalized_filters)))
    for key, value in (
        ("offset", offset if offset else None),
        ("collection-id", collection_id),
        ("shuffle-seed", shuffle_seed),
        ("ct", custom_type),
        ("translate-direction", translate_direction),
    ):
        if value is not None:
            state[key] = value
            params.append((key, value))
    return _result(_app_url(base_url, f"reels/{quote(language, safe='')}", params), "reels", state, warnings)


def build_actor(
    actor_id: str,
    *,
    pos: int = 0,
    base_url: str = PRODUCTION_ORIGIN,
) -> dict[str, Any]:
    actor_id = _clean_text(actor_id, "actor-id", required=True) or ""
    if "/" in actor_id:
        raise URLContractError("actor-id must be a single path segment")
    pos = _parse_nonnegative_int(pos, "pos")
    origin = _origin(base_url)
    url = f"{origin}/actor/{quote(actor_id, safe='')}" + (f"/{pos}" if pos else "")
    state: dict[str, Any] = {"actor-id": actor_id}
    if pos:
        state["pos"] = pos
    return _result(url, "actor", state)


def _load_filters(value: str | None) -> dict[str, Any]:
    if not value:
        return {}
    try:
        decoded = json.loads(value)
    except json.JSONDecodeError as exc:
        raise URLContractError("filters must be valid JSON") from exc
    if not isinstance(decoded, dict):
        raise URLContractError("filters must be a JSON object")
    return decoded


def _unknown_params(pairs: list[tuple[str, str]], allowed: set[str]) -> list[str]:
    return sorted({key for key, _ in pairs if key not in allowed})


def _record_removed_parameters(
    result: dict[str, Any], names: Iterable[str], warnings: list[str] | None = None
) -> dict[str, Any]:
    removed = sorted(set(names))
    combined_warnings = [*(warnings or []), *result.get("warnings", [])]
    if removed:
        result["unknown"] = sorted(set(result.get("unknown", [])) | set(removed))
        combined_warnings.insert(
            0, "removed unknown or internal parameter(s): " + ", ".join(removed)
        )
    result["warnings"] = combined_warnings
    return result


def decode_url(url: str, *, base_url: str = PRODUCTION_ORIGIN) -> dict[str, Any]:
    expected_origin = _origin(base_url)
    parts = urlsplit(url)
    actual_origin = f"{parts.scheme}://{parts.netloc}"
    if actual_origin != expected_origin:
        raise URLContractError(f"URL origin must be {expected_origin}")
    warnings: list[str] = []

    actor_match = re.fullmatch(r"/actor/([^/]+)(?:/(\d+))?/?", parts.path)
    if actor_match and not parts.fragment:
        result = build_actor(unquote(actor_match.group(1)), pos=int(actor_match.group(2) or 0), base_url=base_url)
        return _record_removed_parameters(
            result, (key for key, _ in parse_qsl(parts.query, keep_blank_values=True))
        )

    public_reels = re.fullmatch(r"/reels/([^/]+)/(?:(?:([^/]+)/)?([^/]+))/?", parts.path)
    if public_reels and not parts.fragment:
        language, maybe_translation, search_text = public_reels.groups()
        result = build_reels(
            source="custom-search",
            query=unquote(search_text),
            language=unquote(language),
            translate_direction=unquote(maybe_translation) if maybe_translation else None,
            base_url=base_url,
        )
        return _record_removed_parameters(
            result, (key for key, _ in parse_qsl(parts.query, keep_blank_values=True))
        )

    fragment = parts.fragment
    if not fragment.startswith("/"):
        raise URLContractError("unsupported PlayPhrase.me route")
    route, separator, raw_query = fragment[1:].partition("?")
    pairs = parse_qsl(raw_query if separator else "", keep_blank_values=True)
    values = dict(pairs)

    if route == "search":
        source = values.get("source")
        if source in {"common-phrases", "common-words"}:
            allowed = {"language", "source", "filters", "offset"}
            unknown = _unknown_params(pairs, allowed)
            result = build_catalog(
                source,
                language=values.get("language", "en"),
                offset=values.get("offset", 0),
                filters=_load_filters(values.get("filters")),
                base_url=base_url,
            )
        else:
            allowed = {"language", "q", "pos"}
            unknown = _unknown_params(pairs, allowed)
            result = build_search(
                values.get("q", ""),
                language=values.get("language", "en"),
                pos=values.get("pos", 0),
                base_url=base_url,
            )
    elif route == "clip-search":
        allowed = {"language", "q", "filters"}
        unknown = _unknown_params(pairs, allowed)
        result = build_clip_search(
            query=values.get("q"),
            language=values.get("language", "en"),
            filters=_load_filters(values.get("filters")),
            base_url=base_url,
        )
    elif route == "reels" or route.startswith("reels/"):
        language = route.split("/", 1)[1] if "/" in route else "en"
        if route == "reels":
            warnings.append("legacy Reels route was normalized to /#/reels/en")
        source = values.get("source")
        allowed = {
            "source", "q", "filters", "offset", "collection-id", "shuffle-seed",
            "ct", "translate-direction",
        }
        unknown = _unknown_params(pairs, allowed)
        result = build_reels(
            source=source,
            query=values.get("q"),
            language=language,
            translate_direction=values.get("translate-direction"),
            offset=values.get("offset", 0),
            filters=_load_filters(values.get("filters")),
            collection_id=values.get("collection-id"),
            shuffle_seed=values.get("shuffle-seed"),
            custom_type=values.get("ct"),
            base_url=base_url,
        )
    else:
        raise URLContractError("unsupported PlayPhrase.me route")

    outer_unknown = [key for key, _ in parse_qsl(parts.query, keep_blank_values=True)]
    return _record_removed_parameters(result, [*unknown, *outer_unknown], warnings)


def validate_url(url: str, *, base_url: str = PRODUCTION_ORIGIN) -> dict[str, Any]:
    result = decode_url(url, base_url=base_url)
    if result.get("unknown"):
        raise URLContractError(
            "URL contains unknown or internal parameter(s): " + ", ".join(result["unknown"])
        )
    return result


def _merge_cli_filters(filters_json: str | None, assignments: Iterable[str]) -> dict[str, Any]:
    result = _load_filters(filters_json)
    for key, value in _parse_filter_assignments(assignments):
        canonical = CLIP_ALIASES.get(key, key)
        if canonical in CLIP_ARRAY_FIELDS and canonical in result:
            existing = result[canonical]
            result[canonical] = [*(existing if isinstance(existing, list) else [existing]), value]
        else:
            result[canonical] = value
    return result


def _extract_global_options(argv: list[str]) -> tuple[list[str], str, str]:
    cleaned: list[str] = []
    base_url = PRODUCTION_ORIGIN
    output_format = "url"
    index = 0
    while index < len(argv):
        item = argv[index]
        if item in {"--base-url", "--format"}:
            if index + 1 >= len(argv):
                raise URLContractError(f"{item} requires a value")
            value = argv[index + 1]
            if item == "--base-url":
                base_url = value
            else:
                output_format = value
            index += 2
        elif item.startswith("--base-url="):
            base_url = item.split("=", 1)[1]
            index += 1
        elif item.startswith("--format="):
            output_format = item.split("=", 1)[1]
            index += 1
        else:
            cleaned.append(item)
            index += 1
    if output_format not in {"url", "json"}:
        raise URLContractError("--format must be url or json")
    return cleaned, base_url, output_format


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    search = subparsers.add_parser("search")
    search.add_argument("--query", required=True)
    search.add_argument("--language", default="en")
    search.add_argument("--exact", action="store_true")
    search.add_argument("--grammar", action="store_true")
    search.add_argument("--pos", default=0)

    catalog = subparsers.add_parser("catalog")
    catalog.add_argument("--source", choices=("common-phrases", "common-words"), required=True)
    catalog.add_argument("--language", default="en")
    catalog.add_argument("--offset", default=0)
    catalog.add_argument("--filter", action="append", default=[])

    clip = subparsers.add_parser("clip-search")
    clip.add_argument("--query")
    clip.add_argument("--language", default="en")
    clip.add_argument("--filter", action="append", default=[])
    clip.add_argument("--filters-json")

    reels = subparsers.add_parser("reels")
    reels.add_argument("--source", choices=sorted(REELS_SOURCES))
    reels.add_argument("--query")
    reels.add_argument("--language", default="en")
    reels.add_argument("--translate-direction")
    reels.add_argument("--offset", default=0)
    reels.add_argument("--filter", action="append", default=[])
    reels.add_argument("--filters-json")
    reels.add_argument("--collection-id")
    reels.add_argument("--shuffle-seed")
    reels.add_argument("--custom-type", choices=sorted(CUSTOM_TYPES))

    actor = subparsers.add_parser("actor")
    actor.add_argument("--actor-id", required=True)
    actor.add_argument("--pos", default=0)

    decode = subparsers.add_parser("decode")
    decode.add_argument("url")
    validate = subparsers.add_parser("validate")
    validate.add_argument("url")
    return parser


def _run(args: argparse.Namespace, base_url: str) -> dict[str, Any]:
    if args.command == "search":
        return build_search(
            args.query,
            language=args.language,
            exact=args.exact,
            grammar=args.grammar,
            pos=args.pos,
            base_url=base_url,
        )
    if args.command == "catalog":
        filters = dict(_parse_filter_assignments(args.filter))
        return build_catalog(
            args.source,
            language=args.language,
            offset=args.offset,
            filters=filters,
            base_url=base_url,
        )
    if args.command == "clip-search":
        return build_clip_search(
            query=args.query,
            language=args.language,
            filters=_merge_cli_filters(args.filters_json, args.filter),
            base_url=base_url,
        )
    if args.command == "reels":
        return build_reels(
            source=args.source,
            query=args.query,
            language=args.language,
            translate_direction=args.translate_direction,
            offset=args.offset,
            filters=_merge_cli_filters(args.filters_json, args.filter),
            collection_id=args.collection_id,
            shuffle_seed=args.shuffle_seed,
            custom_type=args.custom_type,
            base_url=base_url,
        )
    if args.command == "decode":
        return decode_url(args.url, base_url=base_url)
    if args.command == "validate":
        return validate_url(args.url, base_url=base_url)
    if args.command == "actor":
        return build_actor(args.actor_id, pos=args.pos, base_url=base_url)
    raise URLContractError("unknown command")


def main(argv: list[str] | None = None) -> int:
    try:
        cleaned, base_url, output_format = _extract_global_options(list(argv or sys.argv[1:]))
        args = _parser().parse_args(cleaned)
        result = _run(args, base_url)
        for warning in result.get("warnings", []):
            print(f"warning: {warning}", file=sys.stderr)
        if output_format == "json" or args.command == "decode":
            print(json.dumps(result, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
        else:
            print(result["url"])
        return 0
    except URLContractError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

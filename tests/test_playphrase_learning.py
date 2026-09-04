from __future__ import annotations

import importlib.util
import json
import socket
import sys
import threading
import time
import unittest
from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from unittest.mock import patch
from urllib.error import URLError
from urllib.parse import parse_qs, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/playphraseme/scripts/playphrase_learning.py"
SPEC = importlib.util.spec_from_file_location("playphrase_learning", SCRIPT)
assert SPEC and SPEC.loader
client = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = client
SPEC.loader.exec_module(client)


class StubHandler(BaseHTTPRequestHandler):
    mode = "json"
    requests: list[str] = []

    def log_message(self, *_args: object) -> None:
        return

    def do_GET(self) -> None:
        type(self).requests.append(self.path)
        mode = type(self).mode
        if mode == "redirect-same" and "redirected=1" not in self.path:
            self.send_response(302)
            self.send_header("Location", "/api/v1/learning/common-phrases?redirected=1")
            self.end_headers()
            return
        if mode == "redirect-cross":
            self.send_response(302)
            self.send_header("Location", "https://example.com/api/v1/learning/common-phrases")
            self.end_headers()
            return
        if mode == "bad-request":
            self.send_response(400)
            self.end_headers()
            return
        if mode == "rate-limit":
            self.send_response(429)
            self.send_header("Retry-After", "37")
            self.end_headers()
            return
        if mode == "invalid-json":
            body = b"not-json"
            self.send_response(200)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        if mode == "oversized":
            self.send_response(200)
            self.send_header("Content-Length", str(client.MAX_BODY_BYTES + 1))
            self.end_headers()
            return
        if mode == "timeout":
            time.sleep(0.2)
            try:
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"{}")
            except (BrokenPipeError, ConnectionResetError):
                pass
            return
        body = json.dumps({"items": [{"text": "ok"}], "path": self.path}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


@contextmanager
def stub_server(mode: str = "json"):
    StubHandler.mode = mode
    StubHandler.requests = []
    server = ThreadingHTTPServer(("127.0.0.1", 0), StubHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}/api/v1/learning"
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=1)


class LearningClientTests(unittest.TestCase):
    def test_suggestions_encodes_unicode_apostrophe_and_clamps_limit(self) -> None:
        url, _ = client.build_request(
            "suggestions",
            {"query": "l'été 日本語", "language": "fr", "limit": 999},
        )
        query = parse_qs(urlsplit(url).query)
        self.assertEqual(["l'été 日本語"], query["q"])
        self.assertEqual(["20"], query["limit"])

    def test_phrases_filters_and_exactly_one_request(self) -> None:
        with stub_server() as base_url:
            url, validated = client.build_request(
                "phrases",
                {
                    "language": "en",
                    "idiom": True,
                    "language_level_from": "B1",
                    "language_level_to": "C1",
                    "limit": 3,
                },
                base_url,
            )
            payload = client.fetch_json(url, validated)
            self.assertEqual("ok", payload["items"][0]["text"])
            self.assertEqual(1, len(StubHandler.requests))
            query = parse_qs(urlsplit(StubHandler.requests[0]).query)
            self.assertEqual(["true"], query["idiom"])
            self.assertEqual(["B1"], query["language-level-from"])
            self.assertEqual(["C1"], query["language-level-to"])

    def test_words_domain_and_part_of_speech(self) -> None:
        url, _ = client.build_request(
            "words",
            {
                "language": "en",
                "domain": "American-English",
                "part_of_speech": "verb",
            },
        )
        query = parse_qs(urlsplit(url).query)
        self.assertEqual(["American-English"], query["domain"])
        self.assertEqual(["verb"], query["part-of-speech"])

    def test_rejects_arbitrary_origin_path_and_credentials(self) -> None:
        invalid = [
            "https://example.com/api/v1/learning",
            "http://localhost:3000/api/v1/phrases",
            "http://user:pass@localhost:3000/api/v1/learning",
            "http://localhost:3000/api/v1/learning?token=secret",
        ]
        for value in invalid:
            with self.subTest(value=value), self.assertRaises(client.InputError):
                client.validate_base_url(value)

    def test_cross_origin_redirect_is_rejected_without_following(self) -> None:
        with stub_server("redirect-cross") as base_url:
            url, validated = client.build_request("phrases", {}, base_url)
            with self.assertRaises(client.RedirectPolicyFailure):
                client.fetch_json(url, validated)
            self.assertEqual(1, len(StubHandler.requests))

    def test_one_same_origin_redirect_is_allowed_and_bounded(self) -> None:
        with stub_server("redirect-same") as base_url:
            url, validated = client.build_request("phrases", {}, base_url)
            payload = client.fetch_json(url, validated)
            self.assertEqual("ok", payload["items"][0]["text"])
            self.assertEqual(2, len(StubHandler.requests))

    def test_bad_request_has_distinct_failure(self) -> None:
        with stub_server("bad-request") as base_url:
            url, validated = client.build_request("phrases", {}, base_url)
            with self.assertRaises(client.BadRequestFailure):
                client.fetch_json(url, validated)

    def test_rate_limit_preserves_retry_after_and_does_not_retry(self) -> None:
        with stub_server("rate-limit") as base_url:
            url, validated = client.build_request("phrases", {}, base_url)
            with self.assertRaises(client.RateLimitFailure) as caught:
                client.fetch_json(url, validated)
            self.assertEqual("37", caught.exception.retry_after)
            self.assertEqual(1, len(StubHandler.requests))

    def test_timeout_is_distinct(self) -> None:
        with stub_server("timeout") as base_url:
            url, validated = client.build_request("phrases", {}, base_url)
            with self.assertRaises(client.TimeoutFailure):
                client.fetch_json(url, validated, timeout=0.05)

    def test_dns_resolution_failure_has_clear_diagnostic(self) -> None:
        class FailingOpener:
            def open(self, *_args: object, **_kwargs: object) -> None:
                raise URLError(socket.gaierror(-3, "Temporary failure in name resolution"))

        url, validated = client.build_request("phrases", {})
        with patch.object(client, "build_opener", return_value=FailingOpener()):
            with self.assertRaises(client.HTTPFailure) as caught:
                client.fetch_json(url, validated)
        self.assertEqual(
            "DNS resolution failed in the execution environment",
            str(caught.exception),
        )
        self.assertEqual(6, caught.exception.exit_code)

    def test_oversized_body_is_rejected(self) -> None:
        with stub_server("oversized") as base_url:
            url, validated = client.build_request("phrases", {}, base_url)
            with self.assertRaises(client.ResponseTooLargeFailure):
                client.fetch_json(url, validated)

    def test_invalid_json_is_rejected(self) -> None:
        with stub_server("invalid-json") as base_url:
            url, validated = client.build_request("phrases", {}, base_url)
            with self.assertRaises(client.InvalidJSONFailure):
                client.fetch_json(url, validated)

    def test_query_over_200_characters_is_rejected(self) -> None:
        with self.assertRaises(client.InputError):
            client.build_request("suggestions", {"query": "x" * 201})

    def test_failure_exit_codes_are_distinct(self) -> None:
        failures = [
            client.InputError,
            client.TimeoutFailure,
            client.BadRequestFailure,
            client.RateLimitFailure,
            client.HTTPFailure,
            client.RedirectPolicyFailure,
            client.ResponseTooLargeFailure,
            client.InvalidJSONFailure,
        ]
        self.assertEqual(len(failures), len({failure.exit_code for failure in failures}))

    def test_api_item_becomes_url_by_text_not_id(self) -> None:
        item = {"id": "word-record-id", "word": "break"}
        url_script_spec = importlib.util.spec_from_file_location(
            "playphrase_url_for_learning_test",
            ROOT / "skills/playphraseme/scripts/playphrase_url.py",
        )
        assert url_script_spec and url_script_spec.loader
        url_module = importlib.util.module_from_spec(url_script_spec)
        sys.modules[url_script_spec.name] = url_module
        url_script_spec.loader.exec_module(url_module)
        result = url_module.build_search(item["word"])
        self.assertIn("q=break", result["url"])
        self.assertNotIn(item["id"], result["url"])


if __name__ == "__main__":
    unittest.main()

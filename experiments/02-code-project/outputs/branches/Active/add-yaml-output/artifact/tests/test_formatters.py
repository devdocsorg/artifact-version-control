"""Tests for the formatters module."""

import json
import yaml

from csvjson.formatters import format_output


SAMPLE_RECORDS = [
    {"name": "Alice", "age": 30, "active": True},
    {"name": "Bob", "age": 25, "active": False},
]


class TestFormatJson:
    def test_basic_json(self):
        result = format_output(SAMPLE_RECORDS, fmt="json")
        parsed = json.loads(result)
        assert len(parsed) == 2
        assert parsed[0]["name"] == "Alice"

    def test_pretty_json(self):
        result = format_output(SAMPLE_RECORDS, fmt="json", pretty=True)
        assert "\n" in result
        assert "  " in result


class TestFormatJsonl:
    def test_basic_jsonl(self):
        result = format_output(SAMPLE_RECORDS, fmt="jsonl")
        lines = result.strip().split("\n")
        assert len(lines) == 2
        assert json.loads(lines[0])["name"] == "Alice"


class TestFormatYaml:
    def test_basic_yaml(self):
        result = format_output(SAMPLE_RECORDS, fmt="yaml")
        parsed = yaml.safe_load(result)
        assert len(parsed) == 2
        assert parsed[0]["name"] == "Alice"
        assert parsed[0]["age"] == 30

    def test_yaml_is_readable(self):
        result = format_output(SAMPLE_RECORDS, fmt="yaml")
        # YAML should be human-readable, not a single-line dump
        assert "\n" in result
        assert "name: Alice" in result

    def test_yaml_preserves_types(self):
        result = format_output(SAMPLE_RECORDS, fmt="yaml")
        parsed = yaml.safe_load(result)
        assert parsed[1]["active"] is False
        assert isinstance(parsed[0]["age"], int)


class TestFormatInvalid:
    def test_unknown_format_raises(self):
        try:
            format_output(SAMPLE_RECORDS, fmt="xml")
            assert False, "Should have raised ValueError"
        except ValueError as e:
            assert "Unknown format" in str(e)

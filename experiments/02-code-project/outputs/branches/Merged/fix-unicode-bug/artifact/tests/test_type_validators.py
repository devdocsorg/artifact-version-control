"""Tests for the type_validators module."""

from csvjson.type_validators import validate_output_format, validate_delimiter


class TestValidateOutputFormat:
    def test_valid_json(self):
        assert validate_output_format("json") == []

    def test_valid_jsonl(self):
        assert validate_output_format("jsonl") == []

    def test_valid_yaml(self):
        assert validate_output_format("yaml") == []

    def test_invalid_format(self):
        errors = validate_output_format("xml")
        assert "unsupported" in errors[0].lower()


class TestValidateDelimiter:
    def test_comma(self):
        assert validate_delimiter(",") == []

    def test_semicolon(self):
        assert validate_delimiter(";") == []

    def test_tab(self):
        assert validate_delimiter("\t") == []

    def test_pipe(self):
        assert validate_delimiter("|") == []

    def test_unusual_warns(self):
        errors = validate_delimiter("^")
        assert any("unusual" in e.lower() for e in errors)

    def test_multi_char_rejects(self):
        errors = validate_delimiter(",,")
        assert any("single character" in e.lower() for e in errors)

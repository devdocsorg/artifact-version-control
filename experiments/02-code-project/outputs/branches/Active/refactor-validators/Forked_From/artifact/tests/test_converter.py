"""Tests for the converter module."""

import os
import tempfile
import pytest

from csvjson.converter import convert_csv_to_json, _coerce_type


class TestCoerceType:
    def test_integer(self):
        assert _coerce_type("42") == 42

    def test_float(self):
        assert _coerce_type("3.14") == 3.14

    def test_boolean_true(self):
        assert _coerce_type("true") is True
        assert _coerce_type("yes") is True

    def test_boolean_false(self):
        assert _coerce_type("false") is False
        assert _coerce_type("no") is False

    def test_string(self):
        assert _coerce_type("hello") == "hello"

    def test_empty_string(self):
        assert _coerce_type("") is None

    def test_none(self):
        assert _coerce_type(None) is None


class TestConvertCsvToJson:
    def _write_csv(self, content: str) -> str:
        """Write content to a temp CSV file and return the path."""
        fd, path = tempfile.mkstemp(suffix=".csv")
        with os.fdopen(fd, "w") as f:
            f.write(content)
        return path

    def test_basic_conversion(self):
        path = self._write_csv("name,age,active\nAlice,30,true\nBob,25,false\n")
        try:
            result = convert_csv_to_json(path)
            assert len(result) == 2
            assert result[0] == {"name": "Alice", "age": 30, "active": True}
            assert result[1] == {"name": "Bob", "age": 25, "active": False}
        finally:
            os.unlink(path)

    def test_custom_delimiter(self):
        path = self._write_csv("name;age\nAlice;30\n")
        try:
            result = convert_csv_to_json(path, delimiter=";")
            assert result[0] == {"name": "Alice", "age": 30}
        finally:
            os.unlink(path)

    def test_empty_file_raises(self):
        path = self._write_csv("")
        try:
            with pytest.raises(ValueError, match="appears to be empty"):
                convert_csv_to_json(path)
        finally:
            os.unlink(path)

    def test_headers_only_raises(self):
        path = self._write_csv("name,age\n")
        try:
            with pytest.raises(ValueError, match="has headers but no data"):
                convert_csv_to_json(path)
        finally:
            os.unlink(path)

    def test_file_not_found(self):
        with pytest.raises(FileNotFoundError):
            convert_csv_to_json("/nonexistent/file.csv")

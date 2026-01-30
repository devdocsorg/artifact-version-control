"""Tests for the validators module."""

import os
import tempfile

from csvjson.validators import validate_file_path, validate_output_format


class TestValidateFilePath:
    def test_valid_csv_file(self):
        fd, path = tempfile.mkstemp(suffix=".csv")
        os.close(fd)
        try:
            errors = validate_file_path(path)
            assert errors == []
        finally:
            os.unlink(path)

    def test_empty_path(self):
        errors = validate_file_path("")
        assert len(errors) == 1
        assert "cannot be empty" in errors[0]

    def test_nonexistent_file(self):
        errors = validate_file_path("/no/such/file.csv")
        assert len(errors) == 1
        assert "not found" in errors[0].lower()

    def test_directory_not_file(self):
        errors = validate_file_path(tempfile.gettempdir())
        assert any("not a file" in e.lower() for e in errors)

    def test_wrong_extension(self):
        fd, path = tempfile.mkstemp(suffix=".txt")
        os.close(fd)
        try:
            errors = validate_file_path(path)
            assert any(".csv" in e for e in errors)
        finally:
            os.unlink(path)


class TestValidateOutputFormat:
    def test_valid_json(self):
        assert validate_output_format("json") == []

    def test_valid_jsonl(self):
        assert validate_output_format("jsonl") == []

    def test_valid_yaml(self):
        assert validate_output_format("yaml") == []

    def test_invalid_format(self):
        errors = validate_output_format("xml")
        assert len(errors) == 1
        assert "unsupported" in errors[0].lower()

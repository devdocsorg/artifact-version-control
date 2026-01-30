"""Tests for the schema_validators module."""

import os
import tempfile

from csvjson.schema_validators import validate_file_path, validate_csv_structure


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


class TestValidateCsvStructure:
    def test_valid_csv(self):
        fd, path = tempfile.mkstemp(suffix=".csv")
        with os.fdopen(fd, "w") as f:
            f.write("name,age\nAlice,30\n")
        try:
            errors = validate_csv_structure(path)
            assert errors == []
        finally:
            os.unlink(path)

    def test_empty_csv(self):
        fd, path = tempfile.mkstemp(suffix=".csv")
        os.close(fd)
        try:
            errors = validate_csv_structure(path)
            assert len(errors) == 1
            assert "empty" in errors[0].lower()
        finally:
            os.unlink(path)

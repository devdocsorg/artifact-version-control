"""Tests for backward-compatibility of the validators shim."""

from csvjson.validators import (
    validate_file_path,
    validate_output_format,
    validate_csv_structure,
    validate_delimiter,
    SUPPORTED_FORMATS,
)


class TestBackwardCompat:
    def test_file_path_importable(self):
        assert callable(validate_file_path)

    def test_output_format_importable(self):
        assert callable(validate_output_format)

    def test_csv_structure_importable(self):
        assert callable(validate_csv_structure)

    def test_delimiter_importable(self):
        assert callable(validate_delimiter)

    def test_supported_formats(self):
        assert "json" in SUPPORTED_FORMATS
        assert "yaml" in SUPPORTED_FORMATS

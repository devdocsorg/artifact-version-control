"""Input validation for csvjson."""

import os
from typing import List


SUPPORTED_FORMATS = ["json", "jsonl", "yaml"]


def validate_file_path(filepath: str) -> List[str]:
    """
    Validate that the input file exists and is readable.

    Returns:
        List of error messages (empty if valid).
    """
    errors = []

    if not filepath:
        errors.append("File path cannot be empty")
        return errors

    if not os.path.exists(filepath):
        errors.append(f"File not found: {filepath}")
        return errors

    if not os.path.isfile(filepath):
        errors.append(f"Not a file: {filepath}")
        return errors

    if not filepath.lower().endswith(".csv"):
        errors.append(f"File does not have .csv extension: {filepath}")

    return errors


def validate_output_format(fmt: str) -> List[str]:
    """
    Validate the output format string.

    Returns:
        List of error messages (empty if valid).
    """
    errors = []

    if fmt not in SUPPORTED_FORMATS:
        errors.append(
            f"Unsupported format '{fmt}'. Supported: {', '.join(SUPPORTED_FORMATS)}"
        )

    return errors

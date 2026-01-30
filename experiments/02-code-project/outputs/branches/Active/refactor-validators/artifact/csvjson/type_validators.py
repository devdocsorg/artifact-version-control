"""Type and format validation for csvjson.

Validates output formats, delimiter characters, and type coercion rules.
"""

from typing import List


SUPPORTED_FORMATS = ["json", "jsonl", "yaml"]

VALID_DELIMITERS = [",", ";", "\t", "|"]


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


def validate_delimiter(delimiter: str) -> List[str]:
    """
    Validate the delimiter character.

    Returns:
        List of error messages (empty if valid).
    """
    errors = []

    if len(delimiter) != 1:
        errors.append(f"Delimiter must be a single character, got: '{delimiter}'")

    if delimiter not in VALID_DELIMITERS:
        errors.append(
            f"Unusual delimiter '{delimiter}'. Common delimiters: {', '.join(repr(d) for d in VALID_DELIMITERS)}"
        )

    return errors

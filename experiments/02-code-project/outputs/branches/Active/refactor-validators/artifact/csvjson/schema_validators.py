"""Schema-level validation for csvjson inputs.

Validates file paths, extensions, and structural requirements.
"""

import os
from typing import List


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


def validate_csv_structure(filepath: str) -> List[str]:
    """
    Validate that a CSV file has basic structural integrity.

    Checks:
    - File is not empty
    - Has at least a header row

    Returns:
        List of error messages (empty if valid).
    """
    errors = []

    try:
        with open(filepath, "r") as f:
            first_line = f.readline().strip()
            if not first_line:
                errors.append(f"CSV file is empty: {filepath}")
    except (IOError, OSError) as e:
        errors.append(f"Cannot read file: {e}")

    return errors

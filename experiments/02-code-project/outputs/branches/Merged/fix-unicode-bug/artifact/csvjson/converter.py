"""Core CSV-to-JSON conversion logic."""

import csv
from typing import List, Dict, Any


def convert_csv_to_json(
    filepath: str,
    delimiter: str = ",",
    encoding: str = "utf-8-sig",
) -> List[Dict[str, Any]]:
    """
    Read a CSV file and return a list of dictionaries.

    Args:
        filepath: Path to the CSV file.
        delimiter: Column delimiter character.
        encoding: File encoding. Default is 'utf-8-sig' which handles
                  BOM (byte order mark) transparently.

    Returns:
        List of dictionaries, one per row.

    Raises:
        FileNotFoundError: If the file doesn't exist.
        ValueError: If the file is empty or malformed.
    """
    records = []

    with open(filepath, "r", encoding=encoding, newline="") as f:
        reader = csv.DictReader(f, delimiter=delimiter)

        if reader.fieldnames is None:
            raise ValueError(f"CSV file '{filepath}' appears to be empty")

        for row_num, row in enumerate(reader, start=2):
            # Convert numeric strings to numbers where possible
            cleaned = {}
            for key, value in row.items():
                cleaned[key] = _coerce_type(value)
            records.append(cleaned)

    if not records:
        raise ValueError(f"CSV file '{filepath}' has headers but no data rows")

    return records


def _coerce_type(value: str) -> Any:
    """Attempt to coerce a string value to int, float, or bool."""
    if value is None or value == "":
        return None

    # Try integer
    try:
        return int(value)
    except ValueError:
        pass

    # Try float
    try:
        return float(value)
    except ValueError:
        pass

    # Try boolean
    if value.lower() in ("true", "yes"):
        return True
    if value.lower() in ("false", "no"):
        return False

    return value

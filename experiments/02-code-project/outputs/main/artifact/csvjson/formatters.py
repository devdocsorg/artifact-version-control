"""Output formatting options for csvjson."""

import json
from typing import List, Dict, Any


def format_output(
    records: List[Dict[str, Any]],
    fmt: str = "json",
    pretty: bool = False,
) -> str:
    """
    Format records for output.

    Args:
        records: List of record dictionaries.
        fmt: Output format ('json' or 'jsonl').
        pretty: Pretty-print JSON (only applies to 'json' format).

    Returns:
        Formatted string.
    """
    if fmt == "json":
        return _format_json(records, pretty=pretty)
    elif fmt == "jsonl":
        return _format_jsonl(records)
    else:
        raise ValueError(f"Unknown format: {fmt}")


def _format_json(records: List[Dict[str, Any]], pretty: bool = False) -> str:
    """Format as a JSON array."""
    if pretty:
        return json.dumps(records, indent=2, ensure_ascii=False)
    return json.dumps(records, ensure_ascii=False)


def _format_jsonl(records: List[Dict[str, Any]]) -> str:
    """Format as JSON Lines (one JSON object per line)."""
    lines = []
    for record in records:
        lines.append(json.dumps(record, ensure_ascii=False))
    return "\n".join(lines)

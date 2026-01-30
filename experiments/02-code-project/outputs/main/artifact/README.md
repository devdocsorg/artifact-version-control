# csvjson

A simple CLI tool to convert CSV files to JSON.

## Installation

```bash
pip install -e .
```

## Usage

```bash
# Basic conversion (outputs to stdout)
csvjson data.csv

# Pretty-printed JSON
csvjson data.csv --pretty

# JSON Lines format
csvjson data.csv --format jsonl

# Custom delimiter
csvjson data.csv --delimiter ";"

# Output to file
csvjson data.csv -o output.json
```

## Output Formats

| Format | Description |
|--------|-------------|
| `json`  | Standard JSON array (default) |
| `jsonl` | JSON Lines — one JSON object per line |

## Features

- Automatic type coercion (integers, floats, booleans)
- Custom delimiter support
- Pretty-printing option
- Input validation

## Development

```bash
pip install -e ".[dev]"
pytest tests/
```

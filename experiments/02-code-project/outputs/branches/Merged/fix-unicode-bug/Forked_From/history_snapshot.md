# Main History — csvjson

## v1.2.0 — 2025-02-01 (merged from refactor-validators)
- Split validators.py into schema_validators.py + type_validators.py
- validators.py kept as backward-compat shim
- Added validate_csv_structure() and validate_delimiter()
- Updated cli.py imports
- 41 tests passing

## v1.1.0 — 2025-01-31 (merged from add-yaml-output)
- Added YAML as output format (--format yaml)
- Added PyYAML dependency (pyyaml>=6.0)
- Graceful ImportError if PyYAML not installed
- 28 tests passing

## v1.0.0 — 2025-01-31
- Initial release: CSV-to-JSON converter
- Type coercion, argparse CLI, json/jsonl output
- Input validation, 20 tests passing

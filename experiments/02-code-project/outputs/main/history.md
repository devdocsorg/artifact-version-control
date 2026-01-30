# Main History — csvjson

## v1.1.0 — 2025-01-31 (merged from add-yaml-output)
- Added YAML as output format (--format yaml)
- Added PyYAML dependency (pyyaml>=6.0)
- Graceful ImportError if PyYAML not installed
- Updated CLI, validators, setup.py, README
- Added test_formatters.py (7 tests), updated test_validators.py (+1)
- 28 tests passing

## v1.0.0 — 2025-01-31
- Initial release
- CSV-to-JSON converter with DictReader-based parsing
- Automatic type coercion (int, float, bool)
- CLI with argparse: input, output, format, delimiter, pretty-print
- Output formats: json, jsonl
- Input validation: file existence, extension, format
- Test suite: 20 tests (converter + validators)
- All tests passing

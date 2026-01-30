# Main History — csvjson

## v1.1.0 — 2025-01-31 (merged from add-yaml-output)
- Added YAML as an output format option (--format yaml)
- Added PyYAML dependency
- Graceful ImportError handling if PyYAML missing
- Updated CLI, validators, setup.py, README
- Added test_formatters.py (7 tests) and updated test_validators.py
- 28 tests passing

## v1.0.0 — 2025-01-31
- Initial release
- CSV-to-JSON converter with DictReader-based parsing
- Automatic type coercion (int, float, bool)
- CLI with argparse: input file, output file, format, delimiter, pretty-print
- Output formats: json, jsonl
- Input validation: file existence, extension check, format validation
- Test suite: 20 tests covering converter and validators
- All tests passing

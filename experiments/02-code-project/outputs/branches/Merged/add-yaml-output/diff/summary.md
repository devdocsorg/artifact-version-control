# Diff Summary

## Files Changed
| File | Status | Description |
|------|--------|-------------|
| `csvjson/formatters.py` | Modified | Added YAML output formatter with PyYAML import and graceful error handling |
| `csvjson/cli.py` | Modified | Added "yaml" to --format choices |
| `csvjson/validators.py` | Modified | Added "yaml" to SUPPORTED_FORMATS list |
| `setup.py` | Modified | Added pyyaml>=6.0 to install_requires |
| `README.md` | Modified | Added YAML usage example and format table entry |
| `tests/test_formatters.py` | Added | New test file with 7 tests for all output formats |
| `tests/test_validators.py` | Modified | Added test_valid_yaml test case |
| `csvjson/__init__.py` | Unchanged | — |
| `csvjson/converter.py` | Unchanged | — |
| `tests/__init__.py` | Unchanged | — |
| `tests/test_converter.py` | Unchanged | — |

## Detailed Changes
See individual diff files for specifics.
- `formatters.py.diff` — Main logic change (new YAML formatter)
- `cli.py.diff` — Argument parser update
- `validators.py.diff` — Format list update
- `setup.py.diff` — Dependency addition
- `README.md.diff` — Documentation update
- `test_validators.py.diff` — New test case
- `test_formatters.py.diff` — Entire new file

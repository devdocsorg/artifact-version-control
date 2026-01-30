# Branch History: add-yaml-output

## 2025-01-31 — Branch Created
- Forked from main at v1.0.0
- Goal: Add YAML as an output format option

## 2025-01-31 — Changes Implemented
- Added `_format_yaml()` function to formatters.py with PyYAML dependency
- Added graceful ImportError handling when PyYAML not installed
- Updated cli.py to accept `--format yaml` choice
- Updated validators.py SUPPORTED_FORMATS to include "yaml"
- Added pyyaml>=6.0 to setup.py install_requires
- Added YAML documentation to README.md (usage + formats table)
- Created test_formatters.py with 7 new tests (3 YAML, 2 JSON, 1 JSONL, 1 error)
- Updated test_validators.py with yaml format validation test
- All 28 tests passing (20 existing + 8 new)

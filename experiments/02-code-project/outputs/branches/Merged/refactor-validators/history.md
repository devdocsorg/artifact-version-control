# Branch History: refactor-validators

## 2025-02-01 — Branch Created
- Forked from main at v1.1.0 (post add-yaml-output)
- Goal: Split validators.py into schema_validators.py + type_validators.py

## 2025-02-01 — Changes Implemented
- Created schema_validators.py with validate_file_path() (moved) + validate_csv_structure() (new)
- Created type_validators.py with validate_output_format() (moved) + validate_delimiter() (new)
- Rewrote validators.py as backward-compat re-export shim
- Updated cli.py imports to new module paths
- Created test_schema_validators.py (7 tests), test_type_validators.py (10 tests)
- Rewrote test_validators.py as 5 backward-compat tests
- 41 tests passing

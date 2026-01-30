# Diff Summary

## Files Changed
| File | Status | Description |
|------|--------|-------------|
| `csvjson/schema_validators.py` | Added | File path validation + new CSV structure validator |
| `csvjson/type_validators.py` | Added | Output format validation + new delimiter validator |
| `csvjson/validators.py` | Modified | Rewritten as backward-compat re-export shim (was full implementation) |
| `csvjson/cli.py` | Modified | Import paths changed to new modules |
| `tests/test_schema_validators.py` | Added | 7 tests for schema validation |
| `tests/test_type_validators.py` | Added | 10 tests for type/format validation |
| `tests/test_validators.py` | Modified | Rewritten as backward compatibility tests (was direct tests) |
| `csvjson/__init__.py` | Unchanged | — |
| `csvjson/converter.py` | Unchanged | — |
| `csvjson/formatters.py` | Unchanged | — |
| `setup.py` | Unchanged | — |
| `README.md` | Unchanged | — |
| `tests/__init__.py` | Unchanged | — |
| `tests/test_converter.py` | Unchanged | — |
| `tests/test_formatters.py` | Unchanged | — |

## Refactoring Map
This is a structural refactor. The key insight:

```
BEFORE:                         AFTER:
validators.py                   schema_validators.py  (file-level checks)
  ├─ validate_file_path()       type_validators.py    (format/type checks)
  ├─ validate_output_format()   validators.py         (re-export shim)
  └─ SUPPORTED_FORMATS
```

**Code movement:**
- `validate_file_path()` → `schema_validators.py` (unchanged logic)
- `validate_output_format()` → `type_validators.py` (unchanged logic)
- `SUPPORTED_FORMATS` → `type_validators.py` (unchanged value)

**New code:**
- `validate_csv_structure()` in `schema_validators.py`
- `validate_delimiter()` in `type_validators.py`
- `VALID_DELIMITERS` in `type_validators.py`

## Detailed Changes
See individual diff files.

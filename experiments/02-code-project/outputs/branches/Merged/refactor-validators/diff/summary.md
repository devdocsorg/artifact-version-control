# Diff Summary

## Files Changed
| File | Status | Description |
|------|--------|-------------|
| `csvjson/schema_validators.py` | Added | File path + CSV structure validation (extracted from validators.py) |
| `csvjson/type_validators.py` | Added | Output format + delimiter validation (extracted from validators.py) |
| `csvjson/validators.py` | Modified | Rewritten as backward-compat re-export shim |
| `csvjson/cli.py` | Modified | Import paths updated to new modules |
| `tests/test_schema_validators.py` | Added | 7 tests for schema validation |
| `tests/test_type_validators.py` | Added | 10 tests for type/format validation |
| `tests/test_validators.py` | Modified | Rewritten as 5 backward-compat import tests |
| `csvjson/__init__.py` | Unchanged | — |
| `csvjson/converter.py` | Unchanged | — |
| `csvjson/formatters.py` | Unchanged | — |
| `setup.py` | Unchanged | — |
| `README.md` | Unchanged | — |
| `tests/__init__.py` | Unchanged | — |
| `tests/test_converter.py` | Unchanged | — |
| `tests/test_formatters.py` | Unchanged | — |

## Refactoring Map

```
BEFORE:                           AFTER:
validators.py                     schema_validators.py  (file/structure checks)
  ├─ validate_file_path()     →     ├─ validate_file_path()      [MOVED, unchanged]
  ├─ validate_output_format() │     └─ validate_csv_structure()  [NEW]
  └─ SUPPORTED_FORMATS        │   type_validators.py             (format/type checks)
                               →     ├─ validate_output_format() [MOVED, unchanged]
                               │     ├─ validate_delimiter()     [NEW]
                               │     ├─ SUPPORTED_FORMATS        [MOVED, unchanged]
                               │     └─ VALID_DELIMITERS         [NEW]
                               │   validators.py                 (shim)
                               →     └─ re-exports all of the above
```

**Key distinction git diff CANNOT make:** `validate_file_path()` and `validate_output_format()` moved with zero logic changes. Git shows them as deleted from one file and added to another. This map tells you nothing changed except location.

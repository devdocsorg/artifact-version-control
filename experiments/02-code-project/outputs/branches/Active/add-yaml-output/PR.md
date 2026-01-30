# PR: add-yaml-output

## Original Request
Add YAML as an output format option for the csvjson tool, alongside existing JSON and JSONL formats.

## Summary of Changes
- **formatters.py**: New `_format_yaml()` function using PyYAML; graceful ImportError if PyYAML missing
- **cli.py**: Added "yaml" to --format choices
- **validators.py**: Added "yaml" to SUPPORTED_FORMATS list
- **setup.py**: Added pyyaml>=6.0 dependency
- **README.md**: Updated usage examples and format table
- **tests/test_formatters.py**: NEW — 7 tests covering JSON, JSONL, YAML output, and error handling
- **tests/test_validators.py**: Added test_valid_yaml test

## Files to Review
1. `csvjson/formatters.py` — main logic change
2. `tests/test_formatters.py` — new test file
3. `setup.py` — new dependency

## Decisions Made
- Used `yaml.dump()` with `default_flow_style=False` for human-readable output
- Made PyYAML a hard dependency (in install_requires) rather than optional
- Added graceful import error message suggesting `pip install pyyaml`

## Status
- [x] Branch created
- [x] Changes implemented
- [x] Unit testing complete
- [x] Integration testing complete
- [x] Diff generated
- [x] Ready for review
- [ ] Feedback addressed
- [ ] Approved for merge
- [ ] Merged to main

# Test Checklist for Python Code (csvjson)

## Unit Tests (per changed section)
- [ ] Changed module passes `pytest` in isolation
- [ ] New functions have corresponding test cases
- [ ] Type coercion handles edge cases (None, empty string, mixed types)
- [ ] Validators return correct error messages for invalid inputs
- [ ] No import errors in changed modules

## Integration Tests (whole artifact)
- [ ] Full test suite passes: `python3 -m pytest tests/ -v`
- [ ] CLI runs end-to-end: `csvjson sample.csv --pretty`
- [ ] All cross-module imports resolve correctly

## Custom Checks
- [ ] Code follows existing patterns (error returns as lists, docstrings on public functions)
- [ ] README reflects current functionality

---
Last updated: 2025-01-31

# PR: fix-unicode-bug

## Original Request
Fix handling of Unicode BOM (byte order mark) in CSV files. Excel-exported CSVs 
often include a UTF-8 BOM prefix (`\xef\xbb\xbf`), causing the first column name 
to become `\ufeffname` instead of `name`.

## Summary of Changes
- **csvjson/converter.py**: Changed default encoding from `utf-8` to `utf-8-sig` (1 line)
- **tests/test_converter.py**: Added 2 test cases (unicode chars + BOM handling)

## Files to Review
1. `csvjson/converter.py` — encoding parameter change + docstring update

## Decisions
- Used Python stdlib `utf-8-sig` codec (strips BOM if present, identity otherwise)
- No new dependencies needed

## Status
- [x] Branch created
- [x] Changes implemented
- [x] Unit testing complete (43 tests passing)
- [x] Integration testing complete
- [x] Diff generated
- [x] Ready for review

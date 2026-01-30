# Experiment 04: Spreadsheet/CSV

## Goal
Test the Artifact Branch Workflow with tabular data — a format where row/column diffs matter more than line diffs.

## Why This Matters
- CSV is technically text but line-by-line diffs are terrible for understanding data changes
- Need semantic diffs: "Added 5 rows", "Changed column D values for Q3", "Removed duplicates"
- Formula/calculation changes need special handling
- Data validation is a natural integration test

## Test Plan
1. Create a sample dataset (quarterly sales data, 50+ rows, 8+ columns)
2. Feature branch: add Q4 data (new rows)
3. Feature branch: fix calculation errors in existing data
4. Feature branch: restructure columns (rename, reorder)
5. Evaluate: does the diff tell a human what changed in the DATA, not just the text?

## Artifact
A quarterly sales report CSV with summary rows, formulas (in a companion .py or .md showing calculations).

## Success Criteria
- Diffs describe data changes semantically ("Added 12 rows for Q4 2025")
- Row-level changes show before/after values
- Column restructuring is clearly described
- Data validation catches introduced errors

# Branch History: restructure-docs

## Branch Created
- **Date:** 2025-01-31
- **Forked from:** main @ v1.0 (Initial Commit)
- **Purpose:** Restructure docs: reorder endpoint sections, inline error codes, delete errors.md

## Commit 1: Full restructure
- **Date:** 2025-01-31
- **Changes:**
  - endpoints.md: Reordered sections — Projects now comes before Users
  - endpoints.md: Added inline error tables for each endpoint (moved from errors.md)
  - endpoints.md: Added "Common Errors" section at bottom for 429/500
  - errors.md: DELETED — content moved inline to endpoints.md
  - README.md: Removed errors.md from Quick Start and Table of Contents
  - README.md: Updated endpoints description to mention inline error codes

---
id: src-string-manipulation-routines
type: source
title: 'Source Summary: String manipulation routines'
aliases:
- String manipulation routines
- string_manipulation_routines.md
tags:
- sprite programming
- assembly
- basic
- memory management
sources:
- path: data/docs/codebase_c64_org/base/string_manipulation_routines.md
  sha256: 9228160fbea3c8f503d719b8196eaf4e0100eaf6b038a0333c2bffca34825b3f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: String manipulation routines

**Raw Source File**: `data/docs/codebase_c64_org/base/string_manipulation_routines.md`
**SHA256**: `9228160fbea3c8f503d719b8196eaf4e0100eaf6b038a0333c2bffca34825b3f`

## Summary




# String manipulation routines

# String manipulation routines

Here is a set of routines to handle null-terminated character strings. Included is a small demonstration as to how they should be used. You will find routines to count the length of a string, copy a whole string, copy a string up to a predetermined offset, concatenate two strings and print a string. Take care to notice which pointer each routine utilizes.

The zero page locations used fall within the floating point accumulators o...

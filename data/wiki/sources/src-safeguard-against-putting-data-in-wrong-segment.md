---
id: src-safeguard-against-putting-data-in-wrong-segment
type: source
title: 'Source Summary: base:safeguard_against_putting_data_in_wrong_segment [Codebase64
  wiki]'
aliases:
- base:safeguard_against_putting_data_in_wrong_segment [Codebase64 wiki]
- safeguard_against_putting_data_in_wrong_segment.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/safeguard_against_putting_data_in_wrong_segment.md
  sha256: 72892e983820a112c2acd7313f5f1796fa850742c6ef1b7a7c304307401a2f7c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:safeguard_against_putting_data_in_wrong_segment [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/safeguard_against_putting_data_in_wrong_segment.md`
**SHA256**: `72892e983820a112c2acd7313f5f1796fa850742c6ef1b7a7c304307401a2f7c`

## Summary



# base:safeguard_against_putting_data_in_wrong_segment [Codebase64 wiki]

base:safeguard_against_putting_data_in_wrong_segment

                Especially in macros, you often want to put data into a specific segments. After that is done, afaik, there's no way to go back to “previous segment” automatically. The next best thing would be to make current segment “undefined”, which isn't possible either.

One good safeguard for this is to create an empty segment.

Add to your config file:

```
MEM...

---
id: src-multiplication-and-division
type: source
title: 'Source Summary: Multiplication'
aliases:
- Multiplication
- multiplication_and_division.md
tags:
- assembly
- basic
- memory management
sources:
- path: data/docs/codebase_c64_org/base/multiplication_and_division.md
  sha256: fcd4773fee758afff9b3e5d01d2c8d7289a75b90256b42dedeb301fbbca8f4a2
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Multiplication

**Raw Source File**: `data/docs/codebase_c64_org/base/multiplication_and_division.md`
**SHA256**: `fcd4773fee758afff9b3e5d01d2c8d7289a75b90256b42dedeb301fbbca8f4a2`

## Summary



# Multiplication

### Table of Contents

# Multiplication

The multiplication of two numbers can be done in various forms. The most common methods are “adding in a loop”, bit-shifting, table-based routines and using the floatingpoint-routines in the c64-kernal. Which one is the best depends on your needs (of course), but in general only bit-shifting and table-based routines are used (at least when you deal with integer-values). The examples given in this document are writen to multiply two uns...

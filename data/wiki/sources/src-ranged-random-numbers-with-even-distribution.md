---
id: src-ranged-random-numbers-with-even-distribution
type: source
title: 'Source Summary: Ranged Random Numbers with Even Distribution'
aliases:
- Ranged Random Numbers with Even Distribution
- ranged_random_numbers_with_even_distribution.md
tags:
- assembly
- graphics
- memory management
sources:
- path: data/docs/codebase_c64_org/base/ranged_random_numbers_with_even_distribution.md
  sha256: 5247a2a67fc97c90ddff9b855b237825db2d16f074346a7ef7f4c575dccd5708
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Ranged Random Numbers with Even Distribution

**Raw Source File**: `data/docs/codebase_c64_org/base/ranged_random_numbers_with_even_distribution.md`
**SHA256**: `5247a2a67fc97c90ddff9b855b237825db2d16f074346a7ef7f4c575dccd5708`

## Summary



# Ranged Random Numbers with Even Distribution

### Table of Contents

# Ranged Random Numbers with Even Distribution

(Well, “amortized” even distribution, but keep reading…)

Normally with a random number generator you get an 8-bit value
<sup>[1)](https://codebase.c64.org#fn__1)</sup>.
This gives you a random number with a range of 256 possible values,
from 0 to 255.  But what if you want a smaller range?

For ranges that are a power of two (2, 4, 8, 16, 32, 64, 128) this is easy. You can tr...

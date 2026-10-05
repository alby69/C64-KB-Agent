---
id: src-8bit-logarithm-table-generator-routine
type: source
title: 'Source Summary: 8bit log table generator'
aliases:
- 8bit log table generator
- 8bit_logarithm_table_generator_routine.md
tags:
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/8bit_logarithm_table_generator_routine.md
  sha256: 795d6722bb4562677d1488f741280d5304d3dc461ab8ccc9318129c911abab36
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: 8bit log table generator

**Raw Source File**: `data/docs/codebase_c64_org/base/8bit_logarithm_table_generator_routine.md`
**SHA256**: `795d6722bb4562677d1488f741280d5304d3dc461ab8ccc9318129c911abab36`

## Summary



# 8bit log table generator

# 8bit log table generator

Logarithm tables are often used in C64 and for much the same reason they were originally invented, that is exploiting the same identities your old slide rule uses for transforming multiplication and division into addition and subtraction:

lg(x*y) = lg(x) + lg(y)
lg(x/y) = lg(x) - lg(y)

Typically they'd be used together with an exponentiation table (to get the approximate result), with the exponent built-in to another table (such as in m...

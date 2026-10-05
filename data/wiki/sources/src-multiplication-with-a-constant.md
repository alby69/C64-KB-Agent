---
id: src-multiplication-with-a-constant
type: source
title: 'Source Summary: Multiplication with a constant'
aliases:
- Multiplication with a constant
- multiplication_with_a_constant.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/multiplication_with_a_constant.md
  sha256: 5103fe3feba19d98f6a89cfef81b37a2a8207a866faf65dabda1259fd43485d2
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Multiplication with a constant

**Raw Source File**: `data/docs/codebase_c64_org/base/multiplication_with_a_constant.md`
**SHA256**: `5103fe3feba19d98f6a89cfef81b37a2a8207a866faf65dabda1259fd43485d2`

## Summary



# Multiplication with a constant

# Multiplication with a constant

Multiplication by a specific constant can be a lot simpler and faster than a general-purpose routine to multiply two given numbers together.

For multiplying by a power of two, you can use ASL multiple times on a number.

For multiplying by other things, you can use two copies of the number, ASL both copies different amounts, and then add the results together. For example, here's some code for multiplying the accumulator by te...

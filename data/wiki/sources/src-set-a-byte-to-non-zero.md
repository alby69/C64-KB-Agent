---
id: src-set-a-byte-to-non-zero
type: source
title: 'Source Summary: Set a byte to non-zero'
aliases:
- Set a byte to non-zero
- set_a_byte_to_non-zero.md
tags:
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/set_a_byte_to_non-zero.md
  sha256: d30bc0e602aab965eb285c50f76d47e8b1b2c4cc03fb5552573a2e100265061a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Set a byte to non-zero

**Raw Source File**: `data/docs/codebase_c64_org/base/set_a_byte_to_non-zero.md`
**SHA256**: `d30bc0e602aab965eb285c50f76d47e8b1b2c4cc03fb5552573a2e100265061a`

## Summary



# Set a byte to non-zero

### Table of Contents

# Set a byte to non-zero

*by White Flame*

Consider a flag in memory that is initialized to zero, but should become non-zero based on some check. The byte will later be polled to invoke some behavior and reset to zero. Sometimes small/fast programs need to get clever with this very simple operation depending on how the registers are constrained.

In this page, the “MNZ” operation means “Make Non-Zero”.

### Using Register Values

If a register ...

---
id: src-ax-tinyrand8
type: source
title: 'Source Summary: AX+ Tinyrand8 - a fast 8-bit random generator with internal
  16bit state'
aliases:
- AX+ Tinyrand8 - a fast 8-bit random generator with internal 16bit state
- ax_tinyrand8.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/ax_tinyrand8.md
  sha256: 4dc4741a868840a42522fc1c13be230fa60f88d7e5cb6b8ed5637477b63e2d5b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: AX+ Tinyrand8 - a fast 8-bit random generator with internal 16bit state

**Raw Source File**: `data/docs/codebase_c64_org/base/ax_tinyrand8.md`
**SHA256**: `4dc4741a868840a42522fc1c13be230fa60f88d7e5cb6b8ed5637477b63e2d5b`

## Summary



# AX+ Tinyrand8 - a fast 8-bit random generator with internal 16bit state

# AX+ Tinyrand8 - a fast 8-bit random generator with internal 16bit state

This algorithm produces eventually all numbers between 0 and 255, but the sequence does not repeat until 59748 values. The routine has a 16bit state, but yields an 8 bit value. The randomization is a combination of an ASL, EOR and ADC command. The name AX+ is derived from comes from the ASL, XOR and addition operation. I have tested several other...

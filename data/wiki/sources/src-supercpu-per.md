---
id: src-supercpu-per
type: source
title: 'Source Summary: PER'
aliases:
- PER
- supercpu_per.md
tags:
- sprite programming
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/supercpu_per.md
  sha256: 56ad93119fbca9cd00db973c2d51408845cc3fc32e88e83f8cc05bf80612538d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: PER

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_per.md`
**SHA256**: `56ad93119fbca9cd00db973c2d51408845cc3fc32e88e83f8cc05bf80612538d`

## Summary



# PER

base:supercpu_per

                # PER

```
    /*-------------------------------------------------------------------------
    OP CODE: PER (Push Effective PC Relative indirect address)
    ==========================================================
    
    Addressing Modes:
        Stack (PC Relative Long)         ($62 - 3 bytes, 6 cycles)
    Flags Affected:
        N/A
    Description:
        Add the current value of the program counter to the sixteen-bit signed
        displacem...

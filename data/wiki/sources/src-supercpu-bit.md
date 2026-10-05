---
id: src-supercpu-bit
type: source
title: 'Source Summary: BIT'
aliases:
- BIT
- supercpu_bit.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/supercpu_bit.md
  sha256: 0a4a718e3be55ad60ec3467fe49bc1286cd96a5d106130adaa77831b917ab1d6
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: BIT

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_bit.md`
**SHA256**: `0a4a718e3be55ad60ec3467fe49bc1286cd96a5d106130adaa77831b917ab1d6`

## Summary



# BIT

base:supercpu_bit

                # BIT

```
    //---------------------------------------------------------------------------------------------
    // PseudoCommand-OPC: BIT16 (test memory BITs against accumulator)
    //
    // Addressing Modes:
    //   Immediate                               ($89 - 2 bytes*, 2 cycles¹)
    //   Absolute                                ($2c - 3 bytes, 4 cycles¹)
    //   Direct Page (DP)                        ($24 - 2 bytes, 3 cycles¹²)
    //   Abs...

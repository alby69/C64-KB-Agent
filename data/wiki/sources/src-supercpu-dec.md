---
id: src-supercpu-dec
type: source
title: 'Source Summary: DEC'
aliases:
- DEC
- supercpu_dec.md
tags:
- general
sources:
- path: data/docs/codebase_c64_org/base/supercpu_dec.md
  sha256: ec10a81787315bb0bd90936327141d97d1edda379d78093f736c299039e3b6f0
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: DEC

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_dec.md`
**SHA256**: `ec10a81787315bb0bd90936327141d97d1edda379d78093f736c299039e3b6f0`

## Summary



# DEC

base:supercpu_dec

                # DEC

```
    //---------------------------------------------------------------------------------------------
    // PseudoCommand-OPC: DEC16 (DECrement)
    //
    // Addressing Modes:
    //   Accumulator                        ($3a - 1 bytes, 2 cycles)
    //   Absolute                        ($ce - 3 bytes, 6 cycles¹)
    //   Direct Page (Also DP)            ($c6 - 2 bytes, 5 cycles¹²)
    //   Absolute Indexed,X                ($de - 3 bytes, 7 ...

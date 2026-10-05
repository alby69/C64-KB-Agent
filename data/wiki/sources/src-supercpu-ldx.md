---
id: src-supercpu-ldx
type: source
title: 'Source Summary: LDX'
aliases:
- LDX
- supercpu_ldx.md
tags:
- general
sources:
- path: data/docs/codebase_c64_org/base/supercpu_ldx.md
  sha256: 554dbfb3197efbe2bfef9426ea7b4056579f7df65687fef5185ce47a1f8385cb
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: LDX

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_ldx.md`
**SHA256**: `554dbfb3197efbe2bfef9426ea7b4056579f7df65687fef5185ce47a1f8385cb`

## Summary



# LDX

base:supercpu_ldx

                # LDX

```
    /*-------------------------------------------------------------------------
    OP CODE: LDY (LoaD index register Y from memory)
    ================================================
    Addressing Modes:
        Immediate                        ($a0 - 2 bytes*, 2 cycles¹)
        Absolute                         ($ac - 3 bytes, 4 cycles¹)
        Direct Page (also DP)            ($a4 - 2 bytes, 3 cycles¹²)
        Absolute Indexed, X    ...

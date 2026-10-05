---
id: src-supercpu-ldy
type: source
title: 'Source Summary: LDY'
aliases:
- LDY
- supercpu_ldy.md
tags:
- general
sources:
- path: data/docs/codebase_c64_org/base/supercpu_ldy.md
  sha256: 19a0ad9e14c297434d0215ae34322b6e629b40a606609f3b39c84638a91cb58b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: LDY

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_ldy.md`
**SHA256**: `19a0ad9e14c297434d0215ae34322b6e629b40a606609f3b39c84638a91cb58b`

## Summary



# LDY

base:supercpu_ldy

                # LDY

```
    /*-------------------------------------------------------------------------
    OP CODE: LDX (LoaD index register X from memory)
    ================================================
    
    Addressing Modes:
        Immediate                        ($a2 - 2 bytes*, 2 cycles¹)
        Absolute                         ($ae - 3 bytes, 4 cycles¹)
        Direct Page (also DP)            ($a6 - 2 bytes, 3 cycles¹²)
        Absolute Indexed, ...

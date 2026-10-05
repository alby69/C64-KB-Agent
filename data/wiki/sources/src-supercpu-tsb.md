---
id: src-supercpu-tsb
type: source
title: 'Source Summary: TSB'
aliases:
- TSB
- supercpu_tsb.md
tags:
- general
sources:
- path: data/docs/codebase_c64_org/base/supercpu_tsb.md
  sha256: db08c614b8c303d038b6091471ab6bfeccb5cf5c1d6005846f9623c191d8806e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: TSB

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_tsb.md`
**SHA256**: `db08c614b8c303d038b6091471ab6bfeccb5cf5c1d6005846f9623c191d8806e`

## Summary



# TSB

base:supercpu_tsb

                # TSB

```
    /*-------------------------------------------------------------------------
    OP CODE: TSB (Test and Set memory Bits against accumulator)
    ===========================================================
    
    Addressing Modes:
        Absolute                        ($0c - 3 bytes, 6 cycles¹)
        Direct Page                     ($04 - 2 bytes, 5 cycles¹²)
    Flags Affected:
        z - Set if memory value AND’ed with accumulator...

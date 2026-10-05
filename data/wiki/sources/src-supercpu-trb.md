---
id: src-supercpu-trb
type: source
title: 'Source Summary: TRB'
aliases:
- TRB
- supercpu_trb.md
tags:
- general
sources:
- path: data/docs/codebase_c64_org/base/supercpu_trb.md
  sha256: ac11329550069944ab8556bac3e0f4ffa30666d6953423e3103560056cb97b68
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: TRB

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_trb.md`
**SHA256**: `ac11329550069944ab8556bac3e0f4ffa30666d6953423e3103560056cb97b68`

## Summary



# TRB

base:supercpu_trb

                # TRB

```
    /*-------------------------------------------------------------------------
    OP CODE: TRB (Test and Reset memory Bits against accumulator)
    =============================================================
    
    Addressing Modes:
        Absolute                        ($1c - 3 bytes, 6 cycles¹)
        Direct Page                     ($14 - 2 bytes, 5 cycles¹²)
        ¹ - Add 2 cycles if m = 0 (16-bit memory/accumulator)
        ²...

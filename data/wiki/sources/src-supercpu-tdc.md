---
id: src-supercpu-tdc
type: source
title: 'Source Summary: TCD'
aliases:
- TCD
- supercpu_tdc.md
tags:
- general
sources:
- path: data/docs/codebase_c64_org/base/supercpu_tdc.md
  sha256: ec13d46127712e6bb7d8c4ef04c8d3960e010f042a189dc22f0f8a47220c4161
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: TCD

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_tdc.md`
**SHA256**: `ec13d46127712e6bb7d8c4ef04c8d3960e010f042a189dc22f0f8a47220c4161`

## Summary



# TCD

base:supercpu_tdc

                # TCD

```
    /*-------------------------------------------------------------------------
    OP CODE: TDC (Transfer Direct page register to 16-Bit aCcumulator)
    ==================================================================
    
    Addressing Modes:
        Implied                            ($7b - 1 byte, 2 cycles)
    Flags Affected:
        n - Set if most significant bit of transferred value is set; else
            cleared.
        z - S...

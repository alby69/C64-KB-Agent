---
id: src-scpu-rasterirq-leadout
type: source
title: 'Source Summary: RasterIRQLeadOut'
aliases:
- RasterIRQLeadOut
- scpu_rasterirq_leadout.md
tags:
- raster interrupts
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/scpu_rasterirq_leadout.md
  sha256: 4737b4d8005697be5e6ad070981ae80aa63e21099bb9a677b39544edbb4eacb0
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: RasterIRQLeadOut

**Raw Source File**: `data/docs/codebase_c64_org/base/scpu_rasterirq_leadout.md`
**SHA256**: `4737b4d8005697be5e6ad070981ae80aa63e21099bb9a677b39544edbb4eacb0`

## Summary



# RasterIRQLeadOut

base:scpu_rasterirq_leadout

                # RasterIRQLeadOut

Exits IRQ interrupt code. Restores registers and sets next IRQ vector

| SYNTAX: | :RasterIRQLeadOut RasterCompareValue : VectorIRQ |  |  | 
| EXAMPLE: | :RasterIRQ 52 : #NextIRQ |  |  | 
| PARAMETERS: | Type | Minimum | Maximum | 
| RasterCompareValue | U9 | 0 | 312 | 
| VectorIRQ | Label | N/A | N/A | 

```
    .pseudocommand RasterIRQLeadOut RasterCompareValue : IRQVector {
        lda #IRQVector.getValue()...

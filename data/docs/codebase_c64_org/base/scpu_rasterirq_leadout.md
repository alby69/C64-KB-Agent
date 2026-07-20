---
title: RasterIRQLeadOut
source_url: https://codebase.c64.org/doku.php?id=base%3Ascpu_rasterirq_leadout
category: reference
topics:
- raster interrupts
- assembly
- basic
difficulty: advanced
language: assembly
hardware:
- CPU
- VIC-II
related:
- vic-ii-registers
- raster-interrupts
- sprite-programming
scraped_at: '2026-07-20'
---

# RasterIRQLeadOut

base:scpu_rasterirq_leadout

                # RasterIRQLeadOut

Exits IRQ interrupt code. Restores registers and sets next IRQ vector

| SYNTAX: | :RasterIRQLeadOut RasterCompareValue : VectorIRQ | ||
| EXAMPLE: | :RasterIRQ 52 : #NextIRQ | ||
| PARAMETERS: | Type | Minimum | Maximum | 
| RasterCompareValue | U9 | 0 | 312 | 
| VectorIRQ | Label | N/A | N/A | 

```
    .pseudocommand RasterIRQLeadOut RasterCompareValue : IRQVector {
        lda #IRQVector.getValue()
        sta $ffee
        RasterCompare RasterCompareValue.getValue()
        lda $d019
        sta $d019
        ply
        plx
        pla
        rti
    }
```
base/scpu_rasterirq_leadout.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
.pseudocommand RasterIRQLeadOut RasterCompareValue : IRQVector {
        lda #IRQVector.getValue()
        sta $ffee
        RasterCompare RasterCompareValue.getValue()
        lda $d019
        sta $d019
        ply
        plx
        pla
        rti
    }
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Ascpu_rasterirq_leadout](https://codebase.c64.org/doku.php?id=base%3Ascpu_rasterirq_leadout)*

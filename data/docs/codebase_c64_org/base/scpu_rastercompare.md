---
title: RasterCompare
source_url: https://codebase.c64.org/doku.php?id=base%3Ascpu_rastercompare
category: reference
topics:
- raster interrupts
- assembly
- memory management
- basic
difficulty: advanced
language: assembly
hardware:
- VIC-II
related:
- vic-ii-registers
- raster-interrupts
- sprite-programming
scraped_at: '2026-07-20'
---


# RasterCompare

base:scpu_rastercompare

                # RasterCompare

Sets $d011:$d012 to 9 bit value passed to the pseudocommand. Assumes 16 bit Acc.

| SYNTAX: | RasterCompare RasterCompareValue | ||
| EXAMPLE: | RasterCompare 52 | ||
| PARAMETERS: | Type | Minimum | Maximum | 
| RasterCompareValue | U9 | 0 | 312 | 

```
    .pseudocommand RasterCompare val {
        // Sets Both $d012 & $d011 (for Y adresses > 256)
        lda $d011
        and #%0000000001111111
        ora #[[val.getValue() & %0000000100000000] >> 1] | [[val.getValue() & %0000000011111111]<<8]
        sta $d011
    }
```
base/scpu_rastercompare.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
.pseudocommand RasterCompare val {
        // Sets Both $d012 & $d011 (for Y adresses > 256)
        lda $d011
        and #%0000000001111111
        ora #[[val.getValue() & %0000000100000000] >> 1] | [[val.getValue() & %0000000011111111]<<8]
        sta $d011
    }
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Ascpu_rastercompare](https://codebase.c64.org/doku.php?id=base%3Ascpu_rastercompare)*


### Collegamenti e Riferimenti Hardware
- **$D011 (VIC Control Register 1)**: Associato al chip VIC-II. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#d011).
- **$D012 (Raster Counter)**: Associato al chip VIC-II. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#d012).

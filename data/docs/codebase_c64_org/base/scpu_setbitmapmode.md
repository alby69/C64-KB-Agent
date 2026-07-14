---
title: SetBitmapMode
source_url: https://codebase.c64.org/doku.php?id=base%3Ascpu_setbitmapmode
category: reference
topics:
- graphics
- basic
- assembly
difficulty: intermediate
language: assembly
hardware: []
related: []
scraped_at: '2026-07-14'
---


# SetBitmapMode

base:scpu_setbitmapmode

                # SetBitmapMode

Set Bitmap Mode (set bit #5 of $d011).

| SYNTAX: | :SetBitmapMode | 
| EXAMPLE: | :SetBitmapMode | 
| PARAMETERS: | N/A | 

```
    .pseudocommand SetBitmapMode {
        lda #%0010000000000000
        tsb $d010
    }
```
base/scpu_setbitmapmode.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
.pseudocommand SetBitmapMode {
        lda #%0010000000000000
        tsb $d010
    }
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Ascpu_setbitmapmode](https://codebase.c64.org/doku.php?id=base%3Ascpu_setbitmapmode)*


### Collegamenti e Riferimenti Hardware
- **$D011 (VIC Control Register 1)**: Associato al chip VIC-II. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#d011).

---
title: SetCharMode
source_url: https://codebase.c64.org/doku.php?id=base%3Ascpu_setchermode
category: reference
topics:
- basic
- assembly
difficulty: intermediate
language: assembly
hardware: []
related: []
scraped_at: '2026-07-14'
---


# SetCharMode

base:scpu_setchermode

                # SetCharMode

Set Character Set Mode (reset bit #5 of $d011).

| SYNTAX: | :SetCharMode | 
| EXAMPLE: | :SetCharMode | 
| PARAMETERS: | N/A | 

```
    .pseudocommand SetChar {
        lda #%0010000000000000
        trb $d010
    }
```
base/scpu_setchermode.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
.pseudocommand SetChar {
        lda #%0010000000000000
        trb $d010
    }
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Ascpu_setchermode](https://codebase.c64.org/doku.php?id=base%3Ascpu_setchermode)*


### Collegamenti e Riferimenti Hardware
- **$D011 (VIC Control Register 1)**: Associato al chip VIC-II. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#d011).

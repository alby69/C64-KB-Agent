---
title: PSEUDOCOMMAND
source_url: https://codebase.c64.org/doku.php?id=base%3Ascpu_setscrncol
category: tool
topics:
- basic
- assembly
difficulty: intermediate
language: assembly
hardware:
- VIC-II
related:
- sprite-programming
- raster-interrupts
- vic-ii-registers
scraped_at: '2026-07-14'
---


# PSEUDOCOMMAND

base:scpu_setscrncol

                # PSEUDOCOMMAND

Sets $d020 and $d021 to value passed to pseudocommand. Lowbyte of val sets $d020 and highbyte sets $d021

| SYNTAX: | :ScreenColor val | ||
| EXAMPLE: | :ScreenColor #$0201 | ||
| PARAMETERS: | Type | Minimum | Maximum | 
| U16 | #$0000 | #$ffff | |

Can with good advantage be improved to take advantage of the nativly defined color constants in Kickassembler allowing :ScreenColor BLUE : RED

```
    .pseudocommand ScreenColor val {
        .if (val.getType()==AT_IMMEDIATE) {
            lda #val.getValue()
            sta $d020
        }
    }
```
base/scpu_setscrncol.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
.pseudocommand ScreenColor val {
        .if (val.getType()==AT_IMMEDIATE) {
            lda #val.getValue()
            sta $d020
        }
    }
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Ascpu_setscrncol](https://codebase.c64.org/doku.php?id=base%3Ascpu_setscrncol)*


### Collegamenti e Riferimenti Hardware
- **$D020 (Border Color)**: Associato al chip VIC-II. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#d020).
- **$D021 (Background Color)**: Associato al chip VIC-II. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#d021).

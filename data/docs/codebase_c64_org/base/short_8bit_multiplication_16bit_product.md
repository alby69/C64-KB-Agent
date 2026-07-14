---
title: Short 8bit * 8bit = 16bit multiply
source_url: https://codebase.c64.org/doku.php?id=base%3Ashort_8bit_multiplication_16bit_product
category: reference
topics:
- assembly
difficulty: intermediate
language: assembly
hardware: []
related: []
scraped_at: '2026-07-14'
---

# Short 8bit * 8bit = 16bit multiply

base:short_8bit_multiplication_16bit_product

                # Short 8bit * 8bit = 16bit multiply

A small multiplication routine using the ancient egyptian multiplication algorithm. Factors should be stored in the FAC1 and FAC2 variables, the product can be found in Akku (high byte) and the X-Register (low byte). FAC1 will be destroyed. No tables required.

```
FAC1     = $58
FAC2     = $59
        ; A*256 + X = FAC1 * FAC2
MUL8
        lda #$00
        ldx #$08
        clc
m0      bcc m1
        clc
        adc FAC2
m1      ror
        ror FAC1
        dex
        bpl m0
        ldx FAC1
        rts
```
base/short_8bit_multiplication_16bit_product.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`m0`** (unknown): A*256 + X = FAC1 * FAC2
- **`m1`** (unknown): No description available

```assembly
FAC1     = $58
FAC2     = $59

        ; A*256 + X = FAC1 * FAC2
MUL8
        lda #$00
        ldx #$08
        clc
m0      bcc m1
        clc
        adc FAC2
m1      ror
        ror FAC1
        dex
        bpl m0
        ldx FAC1
        rts
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Ashort_8bit_multiplication_16bit_product](https://codebase.c64.org/doku.php?id=base%3Ashort_8bit_multiplication_16bit_product)*

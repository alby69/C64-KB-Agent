---
title: 16 bit Pseudo Random Generator
source_url: https://codebase.c64.org/doku.php?id=base%3A16bit_pseudo_random_generator
category: reference
topics:
- assembly
difficulty: intermediate
language: assembly
hardware: []
related: []
scraped_at: '2026-07-20'
---

# 16 bit Pseudo Random Generator

base:16bit_pseudo_random_generator

                # 16 bit Pseudo Random Generator

The original creator of this routine is unknown.

```
;---------------------------------------------------------------------------
;pseudo-random routine, value in random+1 (akku also) and random
;---------------------------------------------------------------------------
getrandom:
         lda random+1
         sta temp1
         lda random
         asl a
         rol temp1
         asl a
         rol temp1
         clc
         adc random
         pha
         lda temp1
         adc random+1
         sta random+1
         pla
         adc #$11
         sta random
         lda random+1
         adc #$36
         sta random+1
         rts
temp1:   .byte $5a
random:  .byte %10011101,%01011011
```
base/16bit_pseudo_random_generator.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`getrandom`** (unknown): --------------------------------------------------------------------------- pseudo-random routine, value in random+1 (akku also) and random ---------------------------------------------------------------------------
- **`temp1`** (unknown): No description available
- **`random`** (unknown): No description available

```assembly
;---------------------------------------------------------------------------
;pseudo-random routine, value in random+1 (akku also) and random
;---------------------------------------------------------------------------
getrandom:

         lda random+1
         sta temp1
         lda random
         asl a
         rol temp1
         asl a
         rol temp1
         clc
         adc random
         pha
         lda temp1
         adc random+1
         sta random+1
         pla
         adc #$11
         sta random
         lda random+1
         adc #$36
         sta random+1

         rts

temp1:   .byte $5a
random:  .byte %10011101,%01011011
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3A16bit_pseudo_random_generator](https://codebase.c64.org/doku.php?id=base%3A16bit_pseudo_random_generator)*

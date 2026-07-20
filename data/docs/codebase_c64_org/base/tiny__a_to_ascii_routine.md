---
title: Tiny .A to ASCII routine
source_url: https://codebase.c64.org/doku.php?id=base%3Atiny_.a_to_ascii_routine
category: reference
topics:
- basic
- assembly
difficulty: intermediate
language: mixed
hardware:
- KERNAL
related:
- memory-map
- kernal-routines
scraped_at: '2026-07-20'
---

# Tiny .A to ASCII routine

base:tiny_.a_to_ascii_routine

                # Tiny .A to ASCII routine

From somebody in comp.sys.cbm, don't remember who nor if I tweaked it further to get this version. The thread was probably “Converting An 8-bit Number Into A String”, but I couldn't find it in Google.

Converts .A to 3 ASCII/PETSCII digits: .Y = hundreds, .X = tens, .A = ones

ldy #$2f ldx #$3a sec - iny sbc #100 bcs - - dex adc #10 bmi - adc #$2f rts

Converts .A to 2 ASCII/PETSCII digits: .X = tens, .A = ones

ldx #$3a sec sbc #$64 - dex adc #$0a bmi - adc #$2f rts

base/tiny_.a_to_ascii_routine.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
ldy #$2f
  ldx #$3a
  sec
- iny
  sbc #100
  bcs -
- dex
  adc #10
  bmi -
  adc #$2f
  rts
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
ldx #$3a
  sec
  sbc #$64
- dex
  adc #$0a
  bmi -
  adc #$2f
  rts
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Atiny_.a_to_ascii_routine](https://codebase.c64.org/doku.php?id=base%3Atiny_.a_to_ascii_routine)*

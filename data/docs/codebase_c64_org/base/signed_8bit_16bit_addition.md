---
title: base:signed_8bit_16bit_addition [Codebase64 wiki]
source_url: https://codebase.c64.org/doku.php?id=base%3Asigned_8bit_16bit_addition
category: reference
topics:
- assembly
difficulty: intermediate
language: mixed
hardware:
- CPU
related: []
scraped_at: '2026-07-20'
---

# base:signed_8bit_16bit_addition [Codebase64 wiki]

base:signed_8bit_16bit_addition

                To add a signed 8-bit delta to a 16-bit value, we need to sign-extend the delta to a full 16 bits. The low byte can be added as normal, but the upper byte needs to be $00 or $ff based on the sign of the low byte.

; Precalculate the sign-extended high byte in .X ldx #$00 lda delta bpl :+ dex ; decrement high byte to $ff for a negative delta : ; Normal 16-bit addition clc adc value ; .A still holds delta sta value txa ; .X is the high byte adc value+1 sta value+1

The following version uses only the accumulator, adding 2 bytes and 1 cycle:

; Standard low byte addition clc lda delta adc value sta value ; Sign extend the high byte lda delta and #$80 ; Extract the sign bit beq :+ ; If zero, add #$00 (+ carry) lda #$ff ; Else, add $ff (+ carry) :adc value+1 sta value+1

White Flame

base/signed_8bit_16bit_addition.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
; Precalculate the sign-extended high byte in .X
 ldx #$00
 lda delta
 bpl :+
  dex        ; decrement high byte to $ff for a negative delta
:
 
 ; Normal 16-bit addition
 clc
 adc value   ; .A still holds delta
 sta value
 txa         ; .X is the high byte
 adc value+1
 sta value+1
```

### Snippet Codice (BASIC)

```basic
; Standard low byte addition
 clc
 lda delta
 adc value
 sta value
 
 ; Sign extend the high byte
 lda delta
 and #$80    ; Extract the sign bit
 beq :+      ; If zero, add #$00 (+ carry)
  lda #$ff   ; Else, add $ff (+ carry)
:adc value+1
 sta value+1
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Asigned_8bit_16bit_addition](https://codebase.c64.org/doku.php?id=base%3Asigned_8bit_16bit_addition)*

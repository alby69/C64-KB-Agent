---
title: 32 bit hexadecimal to decimal conversion
source_url: https://codebase.c64.org/doku.php?id=base%3A32_bit_hexadecimal_to_decimal_conversion
category: reference
topics:
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


# 32 bit hexadecimal to decimal conversion

base:32_bit_hexadecimal_to_decimal_conversion

                # 32 bit hexadecimal to decimal conversion

By Graham.

In cases you need to print decimal values, you can use this routine to convert any unsigned 32 bit value to decimal. It doesn't use the BCD mode. The conversion is done by repeatedly dividing the 32 bit value by 10 and storing the remainder of each division as decimal digits.

```
        ; prints a 32 bit value to the screen
printdec
        jsr hex2dec
        ldx #9
l1      lda result,x
        bne l2
        dex             ; skip leading zeros
        bne l1
l2      lda result,x
        ora #$30
        jsr $ffd2
        dex
        bpl l2
        rts
        ; converts 10 digits (32 bit values have max. 10 decimal digits)
hex2dec
        ldx #0
l3      jsr div10
        sta result,x
        inx
        cpx #10
        bne l3
        rts
        ; divides a 32 bit value by 10
        ; remainder is returned in akku
div10
        ldy #32         ; 32 bits
        lda #0
        clc
l4      rol
        cmp #10
        bcc skip
        sbc #10
skip    rol value
        rol value+1
        rol value+2
        rol value+3
        dey
        bpl l4
        rts
value   .byte $ff,$ff,$ff,$ff
result  .byte 0,0,0,0,0,0,0,0,0,0
```
16-bit version with tightened up loops and routine structure:

```
    // Converts 16 bit values to 5 decimal digits.
    ldx #-5
!Loop:
    ldy #16                    // Divides a 16 bit value by 10 (Remainder in A)
    lda #0
    clc
!:  rol
    cmp #10
    bcc !+
        sbc #10
!:  rol value
    rol value+1
    dey
    bpl !--
    sta result-[255-4],x
    inx
    bne !Loop-
    // Print result, skip leading zeros
    ldx #4
!:  lda result,x
    beq !Skip+
    ora #$30
    jsr $ffd2
!Skip:
    dex
    bpl !-
    rts
value:  .word 65535
result: .byte 0,0,0,0,0
```
NB! If you're only looking to convert, not print; Replace jsr $ffd2 with sta result,x.

NB!! If you want to maintain digit positioning, replacing proceeding zero's with #$20.

NB!!! If you wish to extend to 24, 32 or whatever size, adjust the following values:

```
    ldx #-5               // How many digits as a negative number
    ldy #16               // How many bits as a positive number
    sta result-[255-4],x  // Change the "-4" to the negative quantity of digits-1 (i.e. 24 bit => [255-23]
    ldx #4                // How many digits-1 as a positive number
value:  .word 65535       // Adjust to quantity of bits needed
result: .byte 0,0,0,0,0   // Adjust to quantity of digits needed
Finally adjust the quantity of "rol value+n" to: roundup(bits/8)
```
base/32_bit_hexadecimal_to_decimal_conversion.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`l1`** (unknown): prints a 32 bit value to the screen
- **`l2`** (unknown): No description available
- **`l3`** (unknown): converts 10 digits (32 bit values have max. 10 decimal digits)
- **`l4`** (unknown): remainder is returned in akku
- **`skip`** (unknown): No description available

```assembly
; prints a 32 bit value to the screen
printdec
        jsr hex2dec

        ldx #9
l1      lda result,x
        bne l2
        dex             ; skip leading zeros
        bne l1

l2      lda result,x
        ora #$30
        jsr $ffd2
        dex
        bpl l2
        rts

        ; converts 10 digits (32 bit values have max. 10 decimal digits)
hex2dec
        ldx #0
l3      jsr div10
        sta result,x
        inx
        cpx #10
        bne l3
        rts

        ; divides a 32 bit value by 10
        ; remainder is returned in akku
div10
        ldy #32         ; 32 bits
        lda #0
        clc
l4      rol
        cmp #10
        bcc skip
        sbc #10
skip    rol value
        rol value+1
        rol value+2
        rol value+3
        dey
        bpl l4
        rts

value   .byte $ff,$ff,$ff,$ff

result  .byte 0,0,0,0,0,0,0,0,0,0
```

### Snippet Codice (BASIC)

```basic
// Converts 16 bit values to 5 decimal digits.
    ldx #-5
!Loop:
    ldy #16                    // Divides a 16 bit value by 10 (Remainder in A)
    lda #0
    clc
!:  rol
    cmp #10
    bcc !+
        sbc #10
!:  rol value
    rol value+1
    dey
    bpl !--
    sta result-[255-4],x
    inx
    bne !Loop-
    // Print result, skip leading zeros
    ldx #4
!:  lda result,x
    beq !Skip+
    ora #$30
    jsr $ffd2
!Skip:
    dex
    bpl !-
    rts

value:  .word 65535
result: .byte 0,0,0,0,0
```

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`value`** (unknown): No description available
- **`result`** (unknown): No description available

```assembly
ldx #-5               // How many digits as a negative number
    ldy #16               // How many bits as a positive number
    sta result-[255-4],x  // Change the "-4" to the negative quantity of digits-1 (i.e. 24 bit => [255-23]
    ldx #4                // How many digits-1 as a positive number
value:  .word 65535       // Adjust to quantity of bits needed
result: .byte 0,0,0,0,0   // Adjust to quantity of digits needed
Finally adjust the quantity of "rol value+n" to: roundup(bits/8)
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3A32_bit_hexadecimal_to_decimal_conversion](https://codebase.c64.org/doku.php?id=base%3A32_bit_hexadecimal_to_decimal_conversion)*


### Collegamenti e Riferimenti Hardware
- **$FFD2 (CHROUT (Output Character))**: Associato al chip KERNAL. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#ffd2).

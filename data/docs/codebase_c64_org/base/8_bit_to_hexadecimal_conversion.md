---
title: base:8_bit_to_hexadecimal_conversion [Codebase64 wiki]
source_url: https://codebase.c64.org/doku.php?id=base%3A8_bit_to_hexadecimal_conversion
category: reference
topics:
- basic
- assembly
difficulty: intermediate
language: assembly
hardware:
- KERNAL
related:
- memory-map
- kernal-routines
scraped_at: '2026-07-14'
---


# base:8_bit_to_hexadecimal_conversion [Codebase64 wiki]

base:8_bit_to_hexadecimal_conversion

                ## 8 bit to hexadecimal conversion

by ABujok

This is another way to print a 8 bit integer value as a HEX value on a C64 Screen. The given integer must be loaded into the accu before calling the routine.

```
; Example:
	lda #$3F        ; load accu immediate with $3f or 63      
        jsr OUTHEX      ; print $3F
        rts             ; bye
```
; Syntax for DASM BSOUT = $ffd2 ; Print character in accu ;************************** ; print Akku hex value ;************************** OUTHEX tax ; save value for low nibble and #$f0 ; High nibble clc ; clear carry ror ; rotate one bit right ror ; rotate one bit right ror ; rotate one bit right ror ; rotate one bit right jsr NIB2HEX ; print nibble txa ; restore value and #$0f ; Low nibble jsr NIB2HEX ; print nibble rts ;********************* ;* Akku low Nibble to Hex ;********************* NIB2HEX cmp #$0a ; Accu >= 10? bcs HEX ; Yes DIGIT clc ; Accu < 10 adc #$30 ; Accu + $30 jmp OUT ; print HEX clc ; adc #$37 ; Accu + $37 OUT jmp BSOUT ; Print Accu (HEX nibble) and bye

Slight optimization:

```
;**************************
; print Akku hex value
;**************************
OUTHEX	tax		; save value for low nibble
        lsr             ; ignore CARRY and shift hi nybble to lonybble pos.
	lsr		; 
	lsr		; 
	lsr		; 
	jsr NIB2HEX	; print nibble
	txa		; restore value
	and #$0f	; Low nibble
	jsr NIB2HEX	; print nibble
	rts
;*********************
;* Akku low Nibble to Hex
;*********************
NIB2HEX cmp #$0a	; Accu >= 10?
	bcs HEX		; Yes
        adc #$30	; Accu < 10
	jmp BSOUT       ; Print #$30 - #39
HEX	adc #$36	; Accu >= 10, subtract #$09 to get "A" to "F" (CARRY always set here)
	jmp BSOUT	; Print Accu (HEX nibble) and bye
```
Version not using KERNAL:

```
    // Dest.          = YREG:XREG
    // Value to utput = ACC
OUTHEX:
    sty $fb
    stx $fc
    ldy #$00
    pha
    lsr
    lsr
    lsr
    lsr
    tax
    lda tab,x
    sta ($fb),y
    iny
    pla
    and #$0f
    tax
    lda tab,x
    sta ($fb),y
    rts
tab:
    .text "0123456789abcdef"
```
base/8_bit_to_hexadecimal_conversion.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
; Example:

	lda #$3F        ; load accu immediate with $3f or 63      
        jsr OUTHEX      ; print $3F
        rts             ; bye
```

### Snippet Codice (BASIC)

```basic
; Syntax for DASM

BSOUT  = $ffd2	; Print character in accu

;**************************
; print Akku hex value
;**************************
OUTHEX	tax		; save value for low nibble
	and #$f0	; High nibble
	clc		; clear carry
	ror		; rotate one bit right
	ror		; rotate one bit right
	ror		; rotate one bit right
	ror		; rotate one bit right
	jsr NIB2HEX	; print nibble
	txa		; restore value
	and #$0f	; Low nibble
	jsr NIB2HEX	; print nibble
	rts


;*********************
;* Akku low Nibble to Hex
;*********************
NIB2HEX cmp #$0a	; Accu >= 10?
	bcs HEX		; Yes
DIGIT	clc		; Accu < 10
	adc #$30	; Accu + $30
	jmp OUT		; print
HEX	clc		;
	adc #$37	; Accu + $37
OUT	jmp BSOUT	; Print Accu (HEX nibble) and bye
```

### Snippet Codice (BASIC)

```basic
;**************************
; print Akku hex value
;**************************
OUTHEX	tax		; save value for low nibble
        lsr             ; ignore CARRY and shift hi nybble to lonybble pos.
	lsr		; 
	lsr		; 
	lsr		; 
	jsr NIB2HEX	; print nibble
	txa		; restore value
	and #$0f	; Low nibble
	jsr NIB2HEX	; print nibble
	rts

;*********************
;* Akku low Nibble to Hex
;*********************
NIB2HEX cmp #$0a	; Accu >= 10?
	bcs HEX		; Yes
        adc #$30	; Accu < 10
	jmp BSOUT       ; Print #$30 - #39
HEX	adc #$36	; Accu >= 10, subtract #$09 to get "A" to "F" (CARRY always set here)
	jmp BSOUT	; Print Accu (HEX nibble) and bye
```

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`OUTHEX`** (unknown): Dest.          = YREG:XREG Value to utput = ACC
- **`tab`** (unknown): No description available

```assembly
// Dest.          = YREG:XREG
    // Value to utput = ACC
OUTHEX:
    sty $fb
    stx $fc
    ldy #$00
    pha
    lsr
    lsr
    lsr
    lsr
    tax
    lda tab,x
    sta ($fb),y
    iny
    pla
    and #$0f
    tax
    lda tab,x
    sta ($fb),y
    rts

tab:
    .text "0123456789abcdef"
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3A8_bit_to_hexadecimal_conversion](https://codebase.c64.org/doku.php?id=base%3A8_bit_to_hexadecimal_conversion)*


### Collegamenti e Riferimenti Hardware
- **$FFD2 (CHROUT (Output Character))**: Associato al chip KERNAL. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#ffd2).

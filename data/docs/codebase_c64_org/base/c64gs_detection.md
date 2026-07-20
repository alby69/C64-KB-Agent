---
title: base:c64gs_detection [Codebase64 wiki]
source_url: https://codebase.c64.org/doku.php?id=base%3Ac64gs_detection
category: reference
topics:
- basic
- assembly
difficulty: intermediate
language: mixed
hardware:
- KERNAL
- CIA
related:
- keyboard-handling
- memory-map
- joystick-reading
- kernal-routines
- cia-registers
scraped_at: '2026-07-20'
---

# base:c64gs_detection [Codebase64 wiki]

base:c64gs_detection

                ## C64 Game System (C64GS) detection

If you're developing a cartridge-based game and want to setup the controls differently on C64GS (since it doesn't have any physical keyboard), here is how to detect it.

```
check_c64gs			; returns 1 in x-register if true, otherwise 0.
                lda $01		; save $01 temporarily
                pha
		lda #$36	; kernal will now be visible at $e000
		sta $01
		ldx #$00
		lda #$43	; check bytes from kernal
		cmp $fc00	; equals 'C' from 'COPYRIGHT 1990' in C64GS ROM
		bne cc_break
		cmp $fc0f	; equals 'C' from 'COMMODORE'
		bne cc_break
		cmp $fc1c	; equals first 'C' from 'ELECTRONICS'
		bne cc_break
		inx
cc_break	pla		; load old $01-value again
		sta $01
		rts
```
How to use: Call the routine with 'jsr check_c64gs' and check the x-register afterwards.

base/c64gs_detection.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
check_c64gs			; returns 1 in x-register if true, otherwise 0.

                lda $01		; save $01 temporarily
                pha

		lda #$36	; kernal will now be visible at $e000
		sta $01

		ldx #$00

		lda #$43	; check bytes from kernal
		cmp $fc00	; equals 'C' from 'COPYRIGHT 1990' in C64GS ROM
		bne cc_break
		cmp $fc0f	; equals 'C' from 'COMMODORE'
		bne cc_break
		cmp $fc1c	; equals first 'C' from 'ELECTRONICS'
		bne cc_break

		inx

cc_break	pla		; load old $01-value again
		sta $01

		rts
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Ac64gs_detection](https://codebase.c64.org/doku.php?id=base%3Ac64gs_detection)*

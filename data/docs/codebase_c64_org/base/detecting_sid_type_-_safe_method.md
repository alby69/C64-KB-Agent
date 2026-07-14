---
title: Detecting Sid Type - safe method
source_url: https://codebase.c64.org/doku.php?id=base%3Adetecting_sid_type_-_safe_method
category: reference
topics:
- raster interrupts
- assembly
- sound generation
difficulty: advanced
language: assembly
hardware:
- SID
- KERNAL
related:
- sprite-programming
- sound-programming
- memory-map
- raster-interrupts
- sid-registers
- music-player
- kernal-routines
- vic-ii-registers
scraped_at: '2026-07-14'
---


# Detecting Sid Type - safe method

base:detecting_sid_type_-_safe_method

                # Detecting Sid Type - safe method

This SID detection routine is based on the fact that there is a one cycle delay in the oscillator on 8580 compared to 6581 when turned on.

;SID DETECTION ROUTINE ;By SounDemon - Based on a tip from Dag Lem. ;Put together by FTC after SounDemons instructions ;...and tested by Rambones and Jeff. ; - Don't run this routine on a badline sei ;No disturbing interrupts lda #$ff cmp $d012 ;Don't run it on a badline. bne *-3 ;Detection itself starts here lda #$ff ;Set frequency in voice 3 to $ffff sta $d412 ;...and set testbit (other bits don't matter) in VCREG3 ($d412) to disable oscillator sta $d40e sta $d40f lda #$20 ;Sawtooth wave and gatebit OFF to start oscillator again. sta $d412 lda $d41b ;Accu now has different value depending on sid model (6581=3/8580=2) lsr ;...that is: Carry flag is set for 6581, and clear for 8580. bcc model_8580 model_6581: [...] model_8580: [...]

base/detecting_sid_type_-_safe_method.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
;SID DETECTION ROUTINE
	
	;By SounDemon - Based on a tip from Dag Lem.
	;Put together by FTC after SounDemons instructions
	;...and tested by Rambones and Jeff.
	
	; - Don't run this routine on a badline
	
	sei		;No disturbing interrupts
	lda #$ff
	cmp $d012	;Don't run it on a badline.
	bne *-3
	
	;Detection itself starts here	
	lda #$ff	;Set frequency in voice 3 to $ffff 
	sta $d412	;...and set testbit (other bits don't matter) in VCREG3 ($d412) to disable oscillator
	sta $d40e
	sta $d40f
	lda #$20	;Sawtooth wave and gatebit OFF to start oscillator again.
	sta $d412
	lda $d41b	;Accu now has different value depending on sid model (6581=3/8580=2)
	lsr		;...that is: Carry flag is set for 6581, and clear for 8580.
	bcc model_8580
model_6581:
	[...]

model_8580:
	[...]
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Adetecting_sid_type_-_safe_method](https://codebase.c64.org/doku.php?id=base%3Adetecting_sid_type_-_safe_method)*


### Collegamenti e Riferimenti Hardware
- **$D012 (Raster Counter)**: Associato al chip VIC-II. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#d012).

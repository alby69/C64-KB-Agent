---
title: Method used in "Mathematica" by Reflex
source_url: https://codebase.c64.org/doku.php?id=base%3Adetecting_sid_type
category: reference
topics:
- assembly
- sprite programming
difficulty: intermediate
language: assembly
hardware:
- KERNAL
- CPU
- SID
related:
- sid-registers
- memory-map
- music-player
- sprite-programming
- sound-programming
- kernal-routines
- vic-ii-registers
- raster-interrupts
scraped_at: '2026-07-20'
---

# Method used in "Mathematica" by Reflex

base:detecting_sid_type

                # Method used in "Mathematica" by Reflex

```
;;;;;
;;;;  detecting sid type (disassembled from Mathematica by Reflex)
;;;
;;    commented and labelled by Raf/Vulture Design
;
	; subroutine filling SID's registers with $00
        LDX #24
        LDA #0
loop    STA $D400,x
        DEX
        BPL loop
	; main routine
        LDA #$02
	STA $D40F
	LDA #$30
	STA $D412
	LDY #$00
	LDX #$00
sl3	LDA $D41B
	BMI sl2
	DEX
	BNE sl3
	DEY
	BNE sl3
	BEQ sl4
sl2	LDX #$01 	; 1 = 8580
sl4			; 0 = 6581
	bne d8580
; we have 6581 found
;	lda #<t6581 ; pointer to text about 6581
;	ldy #>t6581
;	jsr $ab1e
	jmp _end
; we have 8580 found
d8580 	
;       lda #<t8580 ; pointer to text about 8580
;	ldy #>t8580
;	jsr $ab1e
	
_end
```
base/detecting_sid_type.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`loop`** (unknown): subroutine filling SID's registers with $00
- **`sl3`** (unknown): No description available
- **`sl2`** (unknown): No description available

```assembly
;;;;;
;;;;  detecting sid type (disassembled from Mathematica by Reflex)
;;;
;;    commented and labelled by Raf/Vulture Design
;
	; subroutine filling SID's registers with $00

        LDX #24
        LDA #0
loop    STA $D400,x
        DEX
        BPL loop

	; main routine
        LDA #$02
	STA $D40F
	LDA #$30
	STA $D412
	LDY #$00
	LDX #$00
sl3	LDA $D41B
	BMI sl2
	DEX
	BNE sl3
	DEY
	BNE sl3
	BEQ sl4
sl2	LDX #$01 	; 1 = 8580
sl4			; 0 = 6581
	bne d8580

; we have 6581 found
;	lda #<t6581 ; pointer to text about 6581
;	ldy #>t6581
;	jsr $ab1e

	jmp _end

; we have 8580 found
d8580 	
;       lda #<t8580 ; pointer to text about 8580
;	ldy #>t8580
;	jsr $ab1e
	
_end
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Adetecting_sid_type](https://codebase.c64.org/doku.php?id=base%3Adetecting_sid_type)*

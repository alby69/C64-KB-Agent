---
title: DTV detect
source_url: https://codebase.c64.org/doku.php?id=base%3Adtv_detect
category: reference
topics:
- raster interrupts
- assembly
difficulty: intermediate
language: assembly
hardware: []
related:
- vic-ii-registers
- raster-interrupts
- sprite-programming
scraped_at: '2026-07-20'
---


# DTV detect

base:dtv_detect

                # DTV detect

Also detects C64 vs C128, and PAL vs NTSC.

```
;----------------------------------------------------------
; DTV detect v1.0 by TLR (disassembly by groepaz)
;
; returns:
;
; a=$7f c64
;   $ff c128
;   $7d dtv1 (ntsc dtv)
;   $75 dtv2 (early pal dtv)
;   $74 dtv3 (recent pal dtv, hummer game)
;
; x=0 ntsc
;   1 pal
;----------------------------------------------------------
dtvdetect:
        PHP
        SEI
        LDA #$00
        STA $FB
        STA $FC
        LDX #$FE
        CPX $D030
        ROL $FB
        STA $D03F
        JSR ic03e
        LDA #$01
        STA $D03F
        JSR ic03e
        LDA $FB
        CMP #$3A
        BNE skp1
        JSR ic067
skp1:
        ROL $FB
        LDA #$00
        STA $D03F
        ; test pal/ntsc
        JSR palntsc
        ROL $FC
        PLP
        LDA $FB
        LDX $FC
        RTS
;----------------------------------------------------------
	!scr "TLR'06"	; signature, not used
;----------------------------------------------------------
ic03e:
        LDY #$D0
        LDX #$40
        JSR ic04e
        LDX #$80
        JSR ic04e
        LDY #$D3
        LDX #$00
ic04e:		
        STY cmphi
        LDA #$55
lp1:
        STA $D000
cmphi=*+2
        CMP $D300,X
        BNE skp2
		
        EOR #$FF
        CMP #$55
        BNE lp1
ic061:	
        ROL $FB
        RTS
skp2:
        CLC
        BCC ic061
;----------------------------------------------------------
ic067:
        LDX #$1F
        STX $FF
lp2:
        LDA ic086,X
        STA $D320,X
        DEX
        BPL lp2
        LDA #$0F
        STA $D33A
lp3:
        LDA $D33F
        LSR A
        BCS lp3
        LDA $FF
        BEQ skp3
        RTS
skp3:
        SEC
        RTS
ic086:
	!byte $89,$c0,0,0, 0,0,0,0
	!byte 0,0,0,0, 0,0,0,0
	!byte $ff,0,0,0, 0,0,0,0
	!byte 1,0,0,5, 0,0,0,0
;----------------------------------------------------------
palntsc:
		
lp4:
        LDA $D011
        BMI lp4
lp5:
        LDA $D011
        BPL lp5
lp6:
        LDA $D012
        CMP #$20
        BEQ skp4
		
        LDA $D011
        BMI lp6
        CLC 		; C=0 - ntsc
skp4:
        RTS
;----------------------------------------------------------
```
base/dtv_detect.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: ACME)

#### Routine Identificate:
- **`dtvdetect`** (unknown): $74 dtv3 (recent pal dtv, hummer game)  x=0 ntsc 1 pal ----------------------------------------------------------
- **`skp1`** (unknown): No description available
- **`ic03e`** (unknown): ---------------------------------------------------------- ----------------------------------------------------------
- **`ic04e`** (unknown): No description available
- **`lp1`** (unknown): No description available
- **`ic061`** (unknown): No description available
- **`skp2`** (unknown): No description available
- **`ic067`** (unknown): ----------------------------------------------------------
- **`lp2`** (unknown): ----------------------------------------------------------
- **`lp3`** (unknown): No description available
- **`skp3`** (unknown): No description available
- **`ic086`** (unknown): No description available
- **`palntsc`** (unknown): ----------------------------------------------------------
- **`lp4`** (unknown): ----------------------------------------------------------
- **`lp5`** (unknown): No description available
- **`lp6`** (unknown): No description available
- **`skp4`** (unknown): No description available

```assembly
;----------------------------------------------------------
; DTV detect v1.0 by TLR (disassembly by groepaz)
;
; returns:
;
; a=$7f c64
;   $ff c128
;   $7d dtv1 (ntsc dtv)
;   $75 dtv2 (early pal dtv)
;   $74 dtv3 (recent pal dtv, hummer game)
;
; x=0 ntsc
;   1 pal
;----------------------------------------------------------
dtvdetect:

        PHP
        SEI

        LDA #$00
        STA $FB
        STA $FC

        LDX #$FE
        CPX $D030
        ROL $FB
        STA $D03F
        JSR ic03e

        LDA #$01
        STA $D03F
        JSR ic03e

        LDA $FB
        CMP #$3A
        BNE skp1
        JSR ic067
skp1:
        ROL $FB
        LDA #$00
        STA $D03F

        ; test pal/ntsc
        JSR palntsc
        ROL $FC

        PLP
        LDA $FB
        LDX $FC
        RTS

;----------------------------------------------------------
	!scr "TLR'06"	; signature, not used
;----------------------------------------------------------

ic03e:
        LDY #$D0
        LDX #$40
        JSR ic04e
        LDX #$80
        JSR ic04e
        LDY #$D3
        LDX #$00
ic04e:		
        STY cmphi
        LDA #$55
lp1:
        STA $D000
cmphi=*+2
        CMP $D300,X
        BNE skp2
		
        EOR #$FF
        CMP #$55
        BNE lp1
ic061:	
        ROL $FB
        RTS
skp2:
        CLC
        BCC ic061
;----------------------------------------------------------
ic067:
        LDX #$1F
        STX $FF
lp2:
        LDA ic086,X
        STA $D320,X
        DEX
        BPL lp2

        LDA #$0F
        STA $D33A
lp3:
        LDA $D33F
        LSR A
        BCS lp3

        LDA $FF
        BEQ skp3
        RTS
skp3:
        SEC
        RTS

ic086:
	!byte $89,$c0,0,0, 0,0,0,0
	!byte 0,0,0,0, 0,0,0,0
	!byte $ff,0,0,0, 0,0,0,0
	!byte 1,0,0,5, 0,0,0,0
;----------------------------------------------------------
palntsc:
		
lp4:
        LDA $D011
        BMI lp4
lp5:
        LDA $D011
        BPL lp5
lp6:
        LDA $D012
        CMP #$20
        BEQ skp4
		
        LDA $D011
        BMI lp6
        CLC 		; C=0 - ntsc
skp4:
        RTS
;----------------------------------------------------------
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Adtv_detect](https://codebase.c64.org/doku.php?id=base%3Adtv_detect)*


### Collegamenti e Riferimenti Hardware
- **$D011 (VIC Control Register 1)**: Associato al chip VIC-II. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#d011).
- **$D012 (Raster Counter)**: Associato al chip VIC-II. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#d012).

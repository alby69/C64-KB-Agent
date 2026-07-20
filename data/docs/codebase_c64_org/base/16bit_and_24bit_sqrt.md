---
title: base:16bit_and_24bit_sqrt [Codebase64 wiki]
source_url: https://codebase.c64.org/doku.php?id=base%3A16bit_and_24bit_sqrt
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

# base:16bit_and_24bit_sqrt [Codebase64 wiki]

base:16bit_and_24bit_sqrt

                
this one is from: [http://www.geocities.com/oneelkruns/asm1step.html](http://www.geocities.com/oneelkruns/asm1step.html) (defunct page)

Returns the 8-bit square root in $20 of the 16-bit number in $20 (low) and $21 (high). The remainder is in location $21.

sqrt16 LDY #$01 ; lsby of first odd number = 1 STY $22 DEY STY $23 ; msby of first odd number (sqrt = 0) again SEC LDA $20 ; save remainder in X register TAX ; subtract odd lo from integer lo SBC $22 STA $20 LDA $21 ; subtract odd hi from integer hi SBC $23 STA $21 ; is subtract result negative? BCC nomore ; no. increment square root INY LDA $22 ; calculate next odd number ADC #$01 STA $22 BCC again INC $23 JMP again nomore STY $20 ; all done, store square root STX $21 ; and remainder RTS


And here a version for a 24bit input number: (use page zero locations for best performance; anyway is a bit slow!)

;----------------------------------- ; Square Root of a 24bit number ;----------------------------------- ; by Verz - Jul2019 ;----------------------------------- ; ; load the 24bit input in square ; 16bit result in sqrt & remainder ;----------------------------------- square byte 0,0,0 ; input number storage byte 0,0,0 ; temporary data sqrt byte 0,0 ; result remainder byte 0,0 ; result remainder sqrt24 LDY #$01 ; lsby of first odd number = 1 STY storage DEY STY storage+1 ; msby of first odd number (sqrt = 0) sty storage+2 sty sqrt sty sqrt+1 again SEC LDA square ; save remainder sta remainder SBC storage ; subtract odd lo from integer lo STA square LDA square+1 sta remainder+1 SBC storage+1 ; subtract odd mid from integer mid STA square+1 lda square+2 sbc storage+2 ; subtract odd hi from integer hi sta square+2 BCC nomore ; is subtract result negative? INC sqrt ; no. increment square root bne sqnxt inc sqrt+1 sqnxt LDA storage ; calculate next odd number ADC #$01 ; +1+C(=1) STA storage BCC again lda storage+1 adc #$00 sta storage+1 bcc again INC storage+2 JMP again nomore RTS

base/16bit_and_24bit_sqrt.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
sqrt16
	LDY #$01 ; lsby of first odd number = 1
	STY $22
	DEY
	STY $23 ; msby of first odd number (sqrt = 0)
again
	SEC
	LDA $20 ; save remainder in X register
	TAX ; subtract odd lo from integer lo
	SBC $22
	STA $20
	LDA $21 ; subtract odd hi from integer hi
	SBC $23
	STA $21 ; is subtract result negative?
	BCC nomore ; no. increment square root
	INY
	LDA $22 ; calculate next odd number
	ADC #$01
	STA $22
	BCC again
	INC $23
	JMP again
nomore
	STY $20 ; all done, store square root
	STX $21 ; and remainder
	RTS
```

### Snippet Codice (BASIC)

```basic
;-----------------------------------
;   Square Root of a 24bit number
;-----------------------------------
; by Verz - Jul2019
;-----------------------------------
;
;  load the 24bit input in square
;  16bit result in  sqrt & remainder
;-----------------------------------
 
square    byte 0,0,0     ; input number
storage   byte 0,0,0     ; temporary data
sqrt      byte 0,0       ; result
remainder byte 0,0       ; result remainder
 
sqrt24
        LDY #$01        ; lsby of first odd number = 1
        STY storage
        DEY
        STY storage+1   ; msby of first odd number (sqrt = 0)
        sty storage+2
        sty sqrt
        sty sqrt+1
again
        SEC
        LDA square     ; save remainder
        sta remainder             
        SBC storage    ; subtract odd lo from integer lo
        STA square
        LDA square+1
        sta remainder+1
        SBC storage+1   ; subtract odd mid from integer mid
        STA square+1
        lda square+2
        sbc storage+2   ; subtract odd hi from integer hi
        sta square+2
        BCC nomore    ; is subtract result negative?
        INC sqrt      ; no. increment square root
        bne sqnxt
        inc sqrt+1
sqnxt   LDA storage     ; calculate next odd number
        ADC #$01        ; +1+C(=1)        
        STA storage
        BCC again
        lda storage+1
        adc #$00
        sta storage+1
        bcc again
        INC storage+2
        JMP again
nomore
        RTS
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3A16bit_and_24bit_sqrt](https://codebase.c64.org/doku.php?id=base%3A16bit_and_24bit_sqrt)*

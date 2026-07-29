---
title: start of the kernal ROM
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- e000-continuation-of-exp-function
- e043-ya1xa2x3a3x5
- e059-ya0a1xa2x2a3x3
- eor
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  address: $E000
  address_end: $E08C
  symbol: start-of-the-kernal-rom
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E000**: save FAC2 rounding byte'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $E000 — start of the kernal ROM

## Disassemblatura
```assembly
.E000  85 56    STA $56   ; save FAC2 rounding byte
.E002  20 0F BC JSR $BC0F   ; copy FAC1 to FAC2
.E005  A5 61    LDA $61   ; get FAC1 exponent
.E007  C9 88    CMP #$88   ; compare with EXP limit (256d)
.E009  90 03    BCC $E00E   ; branch if less
.E00B  20 D4 BA JSR $BAD4   ; handle overflow and underflow
.E00E  20 CC BC JSR $BCCC   ; perform INT()
.E011  A5 07    LDA $07   ; get mantissa 4 from INT()
.E013  18       CLC   ; clear carry for add
.E014  69 81    ADC #$81   ; normalise +1
.E016  F0 F3    BEQ $E00B   ; if $00 result has overflowed so go handle it
.E018  38       SEC   ; set carry for subtract
.E019  E9 01    SBC #$01   ; exponent now correct
.E01B  48       PHA   ; save FAC2 exponent swap FAC1 and FAC2
.E01C  A2 05    LDX #$05   ; 4 bytes to do
.E01E  B5 69    LDA $69,X   ; get FAC2,X
.E020  B4 61    LDY $61,X   ; get FAC1,X
.E022  95 61    STA $61,X   ; save FAC1,X
.E024  94 69    STY $69,X   ; save FAC2,X
.E026  CA       DEX   ; decrement count/index
.E027  10 F5    BPL $E01E   ; loop if not all done
.E029  A5 56    LDA $56   ; get FAC2 rounding byte
.E02B  85 70    STA $70   ; save as FAC1 rounding byte
.E02D  20 53 B8 JSR $B853   ; perform subtraction, FAC2 from FAC1
.E030  20 B4 BF JSR $BFB4   ; do - FAC1
.E033  A9 C4    LDA #$C4   ; set counter pointer low byte
.E035  A0 BF    LDY #$BF   ; set counter pointer high byte
.E037  20 59 E0 JSR $E059   ; go do series evaluation
.E03A  A9 00    LDA #$00   ; clear A
.E03C  85 6F    STA $6F   ; clear sign compare (FAC1 EOR FAC2)
.E03E  68       PLA   ; get saved FAC2 exponent
.E03F  20 B9 BA JSR $BAB9   ; test and adjust accumulators
.E042  60       RTS   ; ^2 then series evaluation
.E043  85 71    STA $71   ; save count pointer low byte
.E045  84 72    STY $72   ; save count pointer high byte
.E047  20 CA BB JSR $BBCA   ; pack FAC1 into $57
.E04A  A9 57    LDA #$57   ; set pointer low byte (Y already $00)
.E04C  20 28 BA JSR $BA28   ; do convert AY, FCA1*(AY)
.E04F  20 5D E0 JSR $E05D   ; go do series evaluation
.E052  A9 57    LDA #$57   ; pointer to original # low byte
.E054  A0 00    LDY #$00   ; pointer to original # high byte
.E056  4C 28 BA JMP $BA28   ; do convert AY, FCA1*(AY) do series evaluation
.E059  85 71    STA $71   ; save count pointer low byte
.E05B  84 72    STY $72   ; save count pointer high byte do series evaluation
.E05D  20 C7 BB JSR $BBC7   ; pack FAC1 into $5C
.E060  B1 71    LDA ($71),Y   ; get constants count
.E062  85 67    STA $67   ; save constants count
.E064  A4 71    LDY $71   ; get count pointer low byte
.E066  C8       INY   ; increment it (now constants pointer)
.E067  98       TYA   ; copy it
.E068  D0 02    BNE $E06C   ; skip next if no overflow
.E06A  E6 72    INC $72   ; else increment high byte
.E06C  85 71    STA $71   ; save low byte
.E06E  A4 72    LDY $72   ; get high byte
.E070  20 28 BA JSR $BA28   ; do convert AY, FCA1*(AY)
.E073  A5 71    LDA $71   ; get constants pointer low byte
.E075  A4 72    LDY $72   ; get constants pointer high byte
.E077  18       CLC   ; clear carry for add
.E078  69 05    ADC #$05   ; +5 to low pointer (5 bytes per constant)
.E07A  90 01    BCC $E07D   ; skip next if no overflow
.E07C  C8       INY   ; increment high byte
.E07D  85 71    STA $71   ; save pointer low byte
.E07F  84 72    STY $72   ; save pointer high byte
.E081  20 67 B8 JSR $B867   ; add (AY) to FAC1
.E084  A9 5C    LDA #$5C   ; set pointer low byte to partial
.E086  A0 00    LDY #$00   ; set pointer high byte to partial
.E088  C6 67    DEC $67   ; decrement constants count
.E08A  D0 E4    BNE $E070   ; loop until all done
.E08C  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E000**: save FAC2 rounding byte
- **$E002**: copy FAC1 to FAC2
- **$E005**: get FAC1 exponent
- **$E007**: compare with EXP limit (256d)
- **$E009**: branch if less
- **$E00B**: handle overflow and underflow
- **$E00E**: perform INT()
- **$E011**: get mantissa 4 from INT()
- **$E013**: clear carry for add
- **$E014**: normalise +1
- **$E016**: if $00 result has overflowed so go handle it
- **$E018**: set carry for subtract
- **$E019**: exponent now correct
- **$E01B**: save FAC2 exponent swap FAC1 and FAC2
- **$E01C**: 4 bytes to do
- **$E01E**: get FAC2,X
- **$E020**: get FAC1,X
- **$E022**: save FAC1,X
- **$E024**: save FAC2,X
- **$E026**: decrement count/index
- **$E027**: loop if not all done
- **$E029**: get FAC2 rounding byte
- **$E02B**: save as FAC1 rounding byte
- **$E02D**: perform subtraction, FAC2 from FAC1
- **$E030**: do - FAC1
- **$E033**: set counter pointer low byte
- **$E035**: set counter pointer high byte
- **$E037**: go do series evaluation
- **$E03A**: clear A
- **$E03C**: clear sign compare (FAC1 EOR FAC2)
- **$E03E**: get saved FAC2 exponent
- **$E03F**: test and adjust accumulators
- **$E042**: ^2 then series evaluation
- **$E043**: save count pointer low byte
- **$E045**: save count pointer high byte
- **$E047**: pack FAC1 into $57
- **$E04A**: set pointer low byte (Y already $00)
- **$E04C**: do convert AY, FCA1*(AY)
- **$E04F**: go do series evaluation
- **$E052**: pointer to original # low byte
- **$E054**: pointer to original # high byte
- **$E056**: do convert AY, FCA1*(AY) do series evaluation
- **$E059**: save count pointer low byte
- **$E05B**: save count pointer high byte do series evaluation
- **$E05D**: pack FAC1 into $5C
- **$E060**: get constants count
- **$E062**: save constants count
- **$E064**: get count pointer low byte
- **$E066**: increment it (now constants pointer)
- **$E067**: copy it
- **$E068**: skip next if no overflow
- **$E06A**: else increment high byte
- **$E06C**: save low byte
- **$E06E**: get high byte
- **$E070**: do convert AY, FCA1*(AY)
- **$E073**: get constants pointer low byte
- **$E075**: get constants pointer high byte
- **$E077**: clear carry for add
- **$E078**: +5 to low pointer (5 bytes per constant)
- **$E07A**: skip next if no overflow
- **$E07C**: increment high byte
- **$E07D**: save pointer low byte
- **$E07F**: save pointer high byte
- **$E081**: add (AY) to FAC1
- **$E084**: set pointer low byte to partial
- **$E086**: set pointer high byte to partial
- **$E088**: decrement constants count
- **$E08A**: loop until all done

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
---
title: '"STR$" FUNCTION ENTERS HERE, WITH (Y)=0'
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/bob_sander-cederlof.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- 00d3-pntr
- aa2c-string
- bc5b-fac
- bc9b-integer
- bde7-str-function-enters-here-with-y0
- f5ed-save
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  address: $BDE7
  address_end: $BE09
  symbol: str-function-enters-here-with-y0
  sources:
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$BDE7**: EMIT "-"'
---

# $BDE7 — "STR$" FUNCTION ENTERS HERE, WITH (Y)=0

## Disassemblatura
```assembly
.BDE7  99 FF 00 STA $00FF,Y   ; EMIT "-"
.BDEA  85 66    STA $66   ; MAKE FAC.SIGN POSITIVE ($2D)
.BDEC  84 71    STY $71   ; SAVE STRING PNTR
.BDEE  C8       INY
.BDEF  A9 30    LDA #$30   ; IN CASE (FAC)=0
.BDF1  A6 61    LDX $61   ; NUMBER=0?
.BDF3  D0 03    BNE $BDF8   ; NO, (FAC) NOT ZERO
.BDF5  4C 04 BF JMP $BF04   ; YES, FINISHED
.BDF8  A9 00    LDA #$00   ; STARTING VALUE FOR TMPEXP
.BDFA  E0 80    CPX #$80   ; ANY INTEGER PART?
.BDFC  F0 02    BEQ $BE00   ; NO, BTWN .5 AND .999999999
.BDFE  B0 09    BCS $BE09   ; YES
.BE00  A9 BD    LDA #$BD   ; MULTIPLY BY 1E9
.BE02  A0 BD    LDY #$BD   ; TO GIVE ADJUSTMENT A HEAD START
.BE04  20 28 BA JSR $BA28
.BE07  A9 F7    LDA #$F7   ; EXPONENT ADJUSTMENT
.BE09  85 5D    STA $5D   ; 0 OR -9
```


## Commenti

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BDE7**: EMIT "-"
- **$BDEA**: MAKE FAC.SIGN POSITIVE ($2D)
- **$BDEC**: SAVE STRING PNTR
- **$BDEF**: IN CASE (FAC)=0
- **$BDF1**: NUMBER=0?
- **$BDF3**: NO, (FAC) NOT ZERO
- **$BDF5**: YES, FINISHED
- **$BDF8**: STARTING VALUE FOR TMPEXP
- **$BDFA**: ANY INTEGER PART?
- **$BDFC**: NO, BTWN .5 AND .999999999
- **$BDFE**: YES
- **$BE00**: MULTIPLY BY 1E9
- **$BE02**: TO GIVE ADJUSTMENT A HEAD START
- **$BE07**: EXPONENT ADJUSTMENT
- **$BE09**: 0 OR -9

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
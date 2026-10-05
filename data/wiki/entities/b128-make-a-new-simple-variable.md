---
id: b128-make-a-new-simple-variable
type: entity
title: MAKE A NEW SIMPLE VARIABLE
aliases:
- MAKE A NEW SIMPLE VARIABLE
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b128-make-a-new-simple-variable.md
  sha256: 81cfeafc7cfaf7d48f6c7cb150dbd03e2065381b77147aa6ed97a42d75d8dd6a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-b128-make-a-new-simple-variable
---

# MAKE A NEW SIMPLE VARIABLE



# $B128 — MAKE A NEW SIMPLE VARIABLE

## Disassemblatura
```assembly
.B128  A5 45    LDA $45
.B12A  A4 46    LDY $46
.B12C  C9 54    CMP #$54
.B12E  D0 0B    BNE $B13B
.B130  C0 C9    CPY #$C9
.B132  F0 EF    BEQ $B123
.B134  C0 49    CPY #$49
.B136  D0 03    BNE $B13B
.B138  4C 08 AF JMP $AF08
.B13B  C9 53    CMP #$53
.B13D  D0 04    BNE $B143
.B13F  C0 54    CPY #$54
.B141  F0 F5    BEQ $B138
.B143  A5 2F    LDA $2F   ; SET UP CALL TO BLTU TO
.B145  A4 30    LDY $30   ; TO MOVE FROM ARYTAB THRU STREND-1
.B147  85 5F    STA $5F   ; 7 BYTES HIGHER
.B149  84 60    STY $60
.B14B  A5 31    LDA $31
.B14D  A4 32    LDY $32
.B14F  85 5A    STA $5A
.B151  84 5B    STY $5B
.B153  18       CLC
.B154  69 07    ADC #$07
.B156  90 01    BCC $B159
.B158  C8       INY
.B159  85 58    STA $58
.B15B  84 59    STY $59
.B15D  20 B8 A3 JSR $A3B8   ; MOVE ARRAY BLOCK UP
.B160  A5 58    LDA $58   ; STORE NEW START OF ARRAYS
.B162  A4 59    LDY $59
.B164  C8       INY
.B165  85 2F    STA $2F
.B167  84 30    STY $30
.B169  A0 00    LDY #$00
.B16B  A5 45    LDA $45   ; FIRST CHAR OF NAME
.B16D  91 5F    STA ($5F),Y
.B16F  C8       INY
.B170  A5 46    LDA $46   ; SECOND CHAR OF NAME
.B172  91 5F    STA ($5F),Y
.B174  A9 00    LDA #$00   ; SET FIVE-BYTE VALUE TO 0
.B176  C8       INY
.B177  91 5F    STA ($5F),Y
.B179  C8       INY
.B17A  91 5F    STA ($5F),Y
.B17C  C8       INY
.B17D  91 5F    STA ($5F),Y
.B17F  C8       INY
.B180  91 5F    STA ($5F),Y
.B182  C8       INY
.B183  91 5F    STA ($5F),Y
```


## Commenti

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B143**: SET UP CALL TO BLTU TO
- **$B145**: TO MOVE FROM ARYTAB THRU STREND-1
- **$B147**: 7 BYTES HIGHER
- **$B15D**: MOVE ARRAY BLOCK UP
- **$B160**: STORE NEW START OF ARRAYS
- **$B16B**: FIRST CHAR OF NAME
- **$B170**: SECOND CHAR OF NAME
- **$B174**: SET FIVE-BYTE VALUE TO 0

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-b128-make-a-new-simple-variable]]

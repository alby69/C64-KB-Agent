---
title: shift FCAtemp << A+8 times
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
- asl
- b983-registers
- b999-main-entry-to-right-shift-subroutine
- b9b0-enter-here-for-short-shifts-with-no-sign-extension
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $B983
  address_end: $B9BB
  symbol: shift-fcatemp-a8-times
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B983**: set the offset to FACtemp'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B983**: Offset-Zeiger auf Register'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B983**: SHIFT RESULT RIGHT'
---

# $B983 — shift FCAtemp << A+8 times

## Disassemblatura
```assembly
.B983  A2 25    LDX #$25   ; set the offset to FACtemp
.B985  B4 04    LDY $04,X   ; get FACX mantissa 4
.B987  84 70    STY $70   ; save as FAC1 rounding byte
.B989  B4 03    LDY $03,X   ; get FACX mantissa 3
.B98B  94 04    STY $04,X   ; save FACX mantissa 4
.B98D  B4 02    LDY $02,X   ; get FACX mantissa 2
.B98F  94 03    STY $03,X   ; save FACX mantissa 3
.B991  B4 01    LDY $01,X   ; get FACX mantissa 1
.B993  94 02    STY $02,X   ; save FACX mantissa 2
.B995  A4 68    LDY $68   ; get FAC1 overflow byte
.B997  94 01    STY $01,X   ; save FACX mantissa 1 shift FACX -A times right (> 8 shifts)
.B999  69 08    ADC #$08   ; add 8 to shift count
.B99B  30 E8    BMI $B985   ; go do 8 shift if still -ve
.B99D  F0 E6    BEQ $B985   ; go do 8 shift if zero
.B99F  E9 08    SBC #$08   ; else subtract 8 again
.B9A1  A8       TAY   ; save count to Y
.B9A2  A5 70    LDA $70   ; get FAC1 rounding byte
.B9A4  B0 14    BCS $B9BA
.B9A6  16 01    ASL $01,X   ; shift FACX mantissa 1
.B9A8  90 02    BCC $B9AC   ; branch if +ve
.B9AA  F6 01    INC $01,X   ; this sets b7 eventually
.B9AC  76 01    ROR $01,X   ; shift FACX mantissa 1 (correct for ASL)
.B9AE  76 01    ROR $01,X   ; shift FACX mantissa 1 (put carry in b7) shift FACX Y times right
.B9B0  76 02    ROR $02,X   ; shift FACX mantissa 2
.B9B2  76 03    ROR $03,X   ; shift FACX mantissa 3
.B9B4  76 04    ROR $04,X   ; shift FACX mantissa 4
.B9B6  6A       ROR   ; shift FACX rounding byte
.B9B7  C8       INY   ; increment exponent diff
.B9B8  D0 EC    BNE $B9A6   ; branch if range adjust not complete
.B9BA  18       CLC   ; just clear it
.B9BB  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$B983**: set the offset to FACtemp
- **$B985**: get FACX mantissa 4
- **$B987**: save as FAC1 rounding byte
- **$B989**: get FACX mantissa 3
- **$B98B**: save FACX mantissa 4
- **$B98D**: get FACX mantissa 2
- **$B98F**: save FACX mantissa 3
- **$B991**: get FACX mantissa 1
- **$B993**: save FACX mantissa 2
- **$B995**: get FAC1 overflow byte
- **$B997**: save FACX mantissa 1 shift FACX -A times right (> 8 shifts)
- **$B999**: add 8 to shift count
- **$B99B**: go do 8 shift if still -ve
- **$B99D**: go do 8 shift if zero
- **$B99F**: else subtract 8 again
- **$B9A1**: save count to Y
- **$B9A2**: get FAC1 rounding byte
- **$B9A6**: shift FACX mantissa 1
- **$B9A8**: branch if +ve
- **$B9AA**: this sets b7 eventually
- **$B9AC**: shift FACX mantissa 1 (correct for ASL)
- **$B9AE**: shift FACX mantissa 1 (put carry in b7) shift FACX Y times right
- **$B9B0**: shift FACX mantissa 2
- **$B9B2**: shift FACX mantissa 3
- **$B9B4**: shift FACX mantissa 4
- **$B9B6**: shift FACX rounding byte
- **$B9B7**: increment exponent diff
- **$B9B8**: branch if range adjust not complete
- **$B9BA**: just clear it

### Commodore-64-intern-Buch (Commodore)
- **$B983**: Offset-Zeiger auf Register
- **$B985**: FAC-
- **$B987**: Rundungsbyte
- **$B989**: 1 mal
- **$B98B**: verschieben
- **$B98D**: 2 mal
- **$B98F**: verschieben
- **$B991**: 3 mal
- **$B993**: verschieben
- **$B995**: FAC-
- **$B997**: Rundungsbyte
- **$B999**: Zähler um 8 erhöhen
- **$B99B**: größer als 0?
- **$B99D**: wenn nicht, dann weiter verschieben
- **$B99F**: Zähler um 8 vermindern
- **$B9A1**: Zähler sichern
- **$B9A2**: FAC-Rundungsbyte laden
- **$B9A4**: wenn Null, dann CLC, RTS
- **$B9A6**: höchstwertiges Bit =1?,
- **$B9A8**: wenn nicht, dann zu $B9AC
- **$B9AA**: höchste Mantissenstelle erhöhen
- **$B9AC**: sämtliche
- **$B9AE**: Stellen
- **$B9B0**: um ein
- **$B9B2**: Bit nach
- **$B9B4**: rechts
- **$B9B6**: verschieben
- **$B9B7**: Zähler um eins erhöhen
- **$B9B8**: verschieben bis Zähler =0
- **$B9BA**: Carry löschen
- **$B9BB**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B983**: SHIFT RESULT RIGHT
- **$B985**: SHIFT 8 BITS RIGHT
- **$B995**: $00 IF +, $FF IF -

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
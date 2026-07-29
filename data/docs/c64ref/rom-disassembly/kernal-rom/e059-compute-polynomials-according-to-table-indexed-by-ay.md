---
title: compute polynomials according to table indexed by AY
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/bob_sander-cederlof.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related: []
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - commodore-64-intern-buch.txt
  address: $E059
  address_end: $E08C
  symbol: compute-polynomials-according-to-table-indexed-by-ay
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E059**: Zeiger auf'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$E059**: POINTER TO COEFFICIENT TABLE'
---

# $E059 — compute polynomials according to table indexed by AY

## Disassemblatura
```assembly
.E059  85 71    STA $71
.E05B  84 72    STY $72
.E05D  20 C7 BB JSR $BBC7
.E060  B1 71    LDA ($71),Y
.E062  85 67    STA $67
.E064  A4 71    LDY $71
.E066  C8       INY
.E067  98       TYA
.E068  D0 02    BNE $E06C
.E06A  E6 72    INC $72
.E06C  85 71    STA $71
.E06E  A4 72    LDY $72
.E070  20 28 BA JSR $BA28
.E073  A5 71    LDA $71
.E075  A4 72    LDY $72
.E077  18       CLC
.E078  69 05    ADC #$05
.E07A  90 01    BCC $E07D
.E07C  C8       INY
.E07D  85 71    STA $71
.E07F  84 72    STY $72
.E081  20 67 B8 JSR $B867
.E084  A9 5C    LDA #$5C
.E086  A0 00    LDY #$00
.E088  C6 67    DEC $67
.E08A  D0 E4    BNE $E070
.E08C  60       RTS
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$E059**: Zeiger auf
- **$E05B**: Polynomgrad
- **$E05D**: FAC nach Akku #4 bringen
- **$E060**: Polynomgrad
- **$E062**: als Zähler
- **$E064**: Zeiger für Polynomauswertung
- **$E066**: Zeiger erhöhen,
- **$E067**: zeigt dann
- **$E068**: auf ersten Koeffizienten
- **$E06A**: Zeiger
- **$E06C**: für
- **$E06E**: Polynomauswertung
- **$E070**: FAC = FAC * Konstante
- **$E073**: Zeiger in
- **$E075**: (A/Y)
- **$E077**: Zeiger
- **$E078**: um 5 erhöhen - nächste Zahl
- **$E07A**: wenn kleiner, dann zu $E07D
- **$E07C**: ansonsten erhöhen
- **$E07D**: Zeiger für
- **$E07F**: Polynomauswertung speichern
- **$E081**: FAC = FAC + Konstante
- **$E084**: Zeiger auf
- **$E086**: Akku #4
- **$E088**: Zähler erniedrigen
- **$E08A**: schon alle, nein, dann zu $E070
- **$E08C**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$E059**: POINTER TO COEFFICIENT TABLE
- **$E060**: GET N
- **$E062**: SAVE N
- **$E064**: BUMP PNTR TO HIGHEST COEFFICIENT
- **$E066**: AND GET PNTR INTO Y,A
- **$E070**: ACCUMULATE SERIES TERMS
- **$E073**: BUMP PNTR TO NEXT COEFFICIENT
- **$E081**: ADD NEXT COEFFICIENT
- **$E084**: POINT AT X AGAIN
- **$E088**: IF SERIES NOT FINISHED,
- **$E08A**: THEN ADD ANOTHER TERM
- **$E08C**: FINISHED
- **$E08D**: RND 1
- **$E092**: RND 2

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
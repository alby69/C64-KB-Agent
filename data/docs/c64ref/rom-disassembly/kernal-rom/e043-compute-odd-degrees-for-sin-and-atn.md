---
title: compute odd degrees for SIN and ATN
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
  address: $E043
  address_end: $E056
  symbol: compute-odd-degrees-for-sin-and-atn
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E043**: Zeiger auf'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$E043**: SAVE ADDRESS OF COEFFICIENT TABLE'
---

# $E043 — compute odd degrees for SIN and ATN

## Disassemblatura
```assembly
.E043  85 71    STA $71
.E045  84 72    STY $72
.E047  20 CA BB JSR $BBCA
.E04A  A9 57    LDA #$57
.E04C  20 28 BA JSR $BA28
.E04F  20 5D E0 JSR $E05D
.E052  A9 57    LDA #$57
.E054  A0 00    LDY #$00
.E056  4C 28 BA JMP $BA28
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$E043**: Zeiger auf
- **$E045**: Polynomkoeffizienten
- **$E047**: FAC nach Akku #3 bringen
- **$E04A**: Zeiger auf Akku #3
- **$E04C**: FAC * Akku #3 (quadrieren)
- **$E04F**: Polynomberechnung
- **$E052**: Zeiger auf
- **$E054**: Akku #3
- **$E056**: FAC = FAC * Akku #3

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$E043**: SAVE ADDRESS OF COEFFICIENT TABLE
- **$E04A**: Y=0 ALREADY, SO Y,A POINTS AT TEMP1
- **$E04C**: FORM X^2
- **$E04F**: DO SERIES IN X^2
- **$E052**: GET X AGAIN
- **$E056**: MULTIPLY X BY P(X^2) AND EXIT

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
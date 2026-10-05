---
id: e043-compute-odd-degrees-for-sin-and-atn
type: entity
title: compute odd degrees for SIN and ATN
aliases:
- compute odd degrees for SIN and ATN
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e043-compute-odd-degrees-for-sin-and-atn.md
  sha256: ecd499d22f6ead937b447c6f02d2377dbd1e539536935dff0d7761ada796a2a2
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-e043-compute-odd-degrees-for-sin-and-atn
---

# compute odd degrees for SIN and ATN



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

## References
- Source: [[src-e043-compute-odd-degrees-for-sin-and-atn]]

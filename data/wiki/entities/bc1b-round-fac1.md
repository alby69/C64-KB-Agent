---
id: bc1b-round-fac1
type: entity
title: round FAC1
aliases:
- round FAC1
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bc1b-round-fac1.md
  sha256: 4afa27678efa016fb6ea99de5866a9f9adaf99c528c70e9bbf4d290fd8431cb3
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-bc1b-round-fac1
---

# round FAC1



# $BC1B — round FAC1

## Disassemblatura
```assembly
.BC1B  A5 61    LDA $61   ; get FAC1 exponent
.BC1D  F0 FB    BEQ $BC1A   ; exit if zero
.BC1F  06 70    ASL $70   ; shift FAC1 rounding byte
.BC21  90 F7    BCC $BC1A   ; exit if no overflow round FAC1 (no check)
.BC23  20 6F B9 JSR $B96F   ; increment FAC1 mantissa
.BC26  D0 F2    BNE $BC1A   ; branch if no overflow
.BC28  4C 38 B9 JMP $B938   ; normalise FAC1 for C=1 and return
```


## Commenti

### Original Disassembly (—)
- **$BC1B**: get FAC1 exponent
- **$BC1D**: exit if zero
- **$BC1F**: shift FAC1 rounding byte
- **$BC21**: exit if no overflow round FAC1 (no check)
- **$BC23**: increment FAC1 mantissa
- **$BC26**: branch if no overflow
- **$BC28**: normalise FAC1 for C=1 and return

### Commodore-64-intern-Buch (Commodore)
- **$BC1B**: Exponent null ?,
- **$BC1D**: dann fertig
- **$BC1F**: Rundungsstelle größer $7F ?
- **$BC21**: nein, dann fertig
- **$BC23**: Mantisse um eins erhöhen
- **$BC26**: jetzt null ?
- **$BC28**: nach rechts verschieben, Exponent erhöhen

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BC1D**: FAC = 0, RETURN
- **$BC1F**: IS FAC.EXTENSION >= 128?
- **$BC21**: NO, FINISHED

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-bc1b-round-fac1]]

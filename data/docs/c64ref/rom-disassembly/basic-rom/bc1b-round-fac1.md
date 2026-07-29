---
title: round FAC1
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
- bc1b-fac-runden
- bc23-increment-mantissa-and-re-normalize-if-carry
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $BC1B
  address_end: $BC28
  symbol: round-fac1
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$BC1B**: get FAC1 exponent'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$BC1B**: Exponent null ?,'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$BC1D**: FAC = 0, RETURN'
---

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
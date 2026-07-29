---
title: check value according to C flag
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/bob_sander-cederlof.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
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
  address: $AD90
  address_end: $AD9B
  symbol: check-value-according-to-c-flag
  sources:
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$AD90**: $00 IF NUMERIC, $FF IF STRING'
---

# $AD90 — check value according to C flag

## Disassemblatura
```assembly
.AD90  24 0D    BIT $0D
.AD92  30 03    BMI $AD97
.AD94  B0 03    BCS $AD99
.AD96  60       RTS
.AD97  B0 FD    BCS $AD96
.AD99  A2 16    LDX #$16
.AD9B  4C 37 A4 JMP $A437
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$AD90**: $00 IF NUMERIC, $FF IF STRING
- **$AD92**: TYPE IS STRING
- **$AD94**: NOT STRING, BUT WE NEED STRING
- **$AD96**: TYPE IS CORRECT
- **$AD97**: IS STRING AND WE WANTED STRING
- **$AD99**: TYPE MISMATCH

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
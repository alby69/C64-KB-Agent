---
title: assign to integer
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
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
  - marko_mäkelä.txt
  - commodore-64-intern-buch.txt
  address: $A9C4
  address_end: $A9D5
  symbol: assign-to-integer
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A9C4**: FAC runden'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $A9C4 — assign to integer

## Disassemblatura
```assembly
.A9C4  20 1B BC JSR $BC1B
.A9C7  20 BF B1 JSR $B1BF
.A9CA  A0 00    LDY #$00
.A9CC  A5 64    LDA $64
.A9CE  91 49    STA ($49),Y
.A9D0  C8       INY
.A9D1  A5 65    LDA $65
.A9D3  91 49    STA ($49),Y
.A9D5  60       RTS
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$A9C4**: FAC runden
- **$A9C7**: und nach INTEGER wandlen
- **$A9CA**: Zeiger setzen
- **$A9CC**: HIGH-Byte holen und
- **$A9CE**: Wert in Variable bringen
- **$A9D0**: Zeiger erhöhen
- **$A9D1**: LOW-Byte holen und
- **$A9D3**: Wert in Variable bringen
- **$A9D5**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
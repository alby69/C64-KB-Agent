---
title: check descriptor stack
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
  address: $B6DB
  address_end: $B6EB
  symbol: check-descriptor-stack
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B6DB**: Zeiger auf Stringdescriptor'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $B6DB — check descriptor stack

## Disassemblatura
```assembly
.B6DB  C4 18    CPY $18
.B6DD  D0 0C    BNE $B6EB
.B6DF  C5 17    CMP $17
.B6E1  D0 08    BNE $B6EB
.B6E3  85 16    STA $16
.B6E5  E9 03    SBC #$03
.B6E7  85 17    STA $17
.B6E9  A0 00    LDY #$00
.B6EB  60       RTS
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$B6DB**: Zeiger auf Stringdescriptor
- **$B6DD**: identisch mit $18, nicht? RTS
- **$B6DF**: identisch mit 17
- **$B6E1**: wenn nicht, dann RTS
- **$B6E3**: Zeiger nach $16 speichern
- **$B6E5**: Von Adresse $17
- **$B6E7**: 3 abziehen
- **$B6E9**: Zähler auf Null
- **$B6EB**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
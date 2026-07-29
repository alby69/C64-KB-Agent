---
title: shift + commodore key check
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
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
  - marko_mäkelä.txt
  address: $EC5E
  address_end: $EC75
  symbol: shift-commodore-key-check
  sources:
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $EC5E — shift + commodore key check

## Disassemblatura
```assembly
.EC5E  C9 08    CMP #$08
.EC60  D0 07    BNE $EC69
.EC62  A9 80    LDA #$80
.EC64  0D 91 02 ORA $0291
.EC67  30 09    BMI $EC72
.EC69  C9 09    CMP #$09
.EC6B  D0 EE    BNE $EC5B
.EC6D  A9 7F    LDA #$7F
.EC6F  2D 91 02 AND $0291
.EC72  8D 91 02 STA $0291
.EC75  4C A8 E6 JMP $E6A8
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
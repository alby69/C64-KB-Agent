---
title: select keyboard table
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
  address: $EB64
  address_end: $EB76
  symbol: select-keyboard-table
  sources:
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $EB64 — select keyboard table

## Disassemblatura
```assembly
.EB64  0A       ASL
.EB65  C9 08    CMP #$08
.EB67  90 02    BCC $EB6B
.EB69  A9 06    LDA #$06
.EB6B  AA       TAX
.EB6C  BD 79 EB LDA $EB79,X
.EB6F  85 F5    STA $F5
.EB71  BD 7A EB LDA $EB7A,X
.EB74  85 F6    STA $F6
.EB76  4C E0 EA JMP $EAE0
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
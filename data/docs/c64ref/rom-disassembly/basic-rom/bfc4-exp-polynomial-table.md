---
title: EXP polynomial table
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- bfc4-exp-polynomial-table
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  address: $BFC4
  address_end: $BFE8
  symbol: exp-polynomial-table
  sources:
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$BFC4**: degree 8'
---

# $BFC4 — EXP polynomial table

## Disassemblatura
```assembly
.BFC4  07   ; degree 8
.BFC5  71 34 58 3E 56
.BFCA  74 16 7E B3 1B
.BFCF  77 2F EE E3 85
.BFD4  7A 1D 84 1C 2A
.BFD9  7C 63 59 58 0A
.BFDE  7E 75 FD E7 C6
.BFE3  80 31 72 18 10
.BFE8  81 00 00 00 00
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
- **$BFC4**: degree 8

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
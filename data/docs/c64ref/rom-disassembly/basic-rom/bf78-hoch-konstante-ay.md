---
title: hoch Konstante (A/Y)
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/commodore-64-intern-buch.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- bc5b-fac
- bf78-hoch-konstante-ay
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - commodore-64-intern-buch.txt
  address: $BF78
  address_end: $BF78
  symbol: hoch-konstante-ay
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$BF78**: Konstante nach FAC'
---

# $BF78 — hoch Konstante (A/Y)

## Disassemblatura
```assembly
.BF78  20 A2 BB JSR $BBA2   ; Konstante nach FAC
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$BF78**: Konstante nach FAC

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
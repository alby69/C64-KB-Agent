---
title: LOG polynomial table
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
- b9c1-log-polynomial-table
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  address: $B9C1
  address_end: $B9D1
  symbol: log-polynomial-table
  sources:
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$B9C1**: degree 4'
---

# $B9C1 — LOG polynomial table

## Disassemblatura
```assembly
.B9C1  03   ; degree 4
.B9C2  7F 5E 56 CB 79
.B9C7  80 13 9B 0B 64
.B9CC  80 76 38 93 16
.B9D1  82 38 AA 3B 20
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
- **$B9C1**: degree 4

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
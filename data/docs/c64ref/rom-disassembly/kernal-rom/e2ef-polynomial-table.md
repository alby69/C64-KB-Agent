---
title: polynomial table
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- e2ef-polynomial-table
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  address: $E2EF
  address_end: $E309
  symbol: polynomial-table
  sources:
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$E2EF**: degree 6'
---

# $E2EF — polynomial table

## Disassemblatura
```assembly
.E2EF  05   ; degree 6
.E2F0  84 E6 1A 2D 1B
.E2F5  86 28 07 FB F8
.E2FA  87 99 68 89 01
.E2FF  87 23 35 DF E1
.E304  86 A5 5D E7 28
.E309  83 49 0F DA A2
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
- **$E2EF**: degree 6

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
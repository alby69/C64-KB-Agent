---
title: limits for scientific mode
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
- bdb3-nach-ascii
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $BDB3
  address_end: $BDBD
  symbol: limits-for-scientific-mode
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$BDB3**: 99999999.90625, maximum value with at least one decimal'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$BDB3**: 99999999.9'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $BDB3 — limits for scientific mode

## Disassemblatura
```assembly
.BDB3  9B 3E BC 1F FD   ; 99999999.90625, maximum value with at least one decimal
.BDB8  9E 6E 6B 27 FD   ; 999999999.25, maximum value before scientific notation
.BDBD  9E 6E 6B 28 00   ; 1000000000
```


## Commenti

### Original Disassembly (—)
- **$BDB3**: 99999999.90625, maximum value with at least one decimal
- **$BDB8**: 999999999.25, maximum value before scientific notation
- **$BDBD**: 1000000000

### Commodore-64-intern-Buch (Commodore)
- **$BDB3**: 99999999.9
- **$BDB8**: 999999999
- **$BDBD**: 1E9

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
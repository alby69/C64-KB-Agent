---
title: RND values
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
- e08d-konstanten-fr-rnd
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $E08D
  address_end: $E092
  symbol: rnd-values
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E08D**: 11879546            multiplier'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E08D**: 11879546'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $E08D — RND values

## Disassemblatura
```assembly
.E08D  98 35 44 7A 00   ; 11879546            multiplier
.E092  68 28 B1 46 00   ; 3.927677739E-8      offset
```


## Commenti

### Original Disassembly (—)
- **$E08D**: 11879546            multiplier
- **$E092**: 3.927677739E-8      offset

### Commodore-64-intern-Buch (Commodore)
- **$E08D**: 11879546
- **$E092**: 3.92767774E-4

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
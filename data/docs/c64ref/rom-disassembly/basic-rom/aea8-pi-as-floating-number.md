---
title: PI as floating number
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
- aea8-float-value-of-pi
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  address: $AEA8
  address_end: $AEA8
  symbol: pi-as-floating-number
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$AEA8**: 3.141592653'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$AEAD**: decimal point'
---

# $AEA8 — PI as floating number

## Disassemblatura
```assembly
.AEA8  82 49 0F DA A1   ; 3.141592653
```


## Commenti

### Original Disassembly (—)
- **$AEA8**: 3.141592653

### Marko Mäkelä (Marko Mäkelä)
- **$AEAD**: decimal point
- **$AEB1**: plus code
- **$AEB5**: times code
- **$AEB9**: quote mark
- **$AECC**: NOT code

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
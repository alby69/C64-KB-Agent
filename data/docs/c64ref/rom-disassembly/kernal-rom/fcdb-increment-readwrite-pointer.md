---
title: increment read/write pointer
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
- fcdb-increment-acad
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  address: $FCDB
  address_end: $FCE1
  symbol: increment-readwrite-pointer
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FCDB**: increment buffer address low byte'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $FCDB — increment read/write pointer

## Disassemblatura
```assembly
.FCDB  E6 AC    INC $AC   ; increment buffer address low byte
.FCDD  D0 02    BNE $FCE1   ; branch if no overflow
.FCDF  E6 AD    INC $AD   ; increment buffer address low byte
.FCE1  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$FCDB**: increment buffer address low byte
- **$FCDD**: branch if no overflow
- **$FCDF**: increment buffer address low byte

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
---
title: control keyboard table
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
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $EC78
  address_end: $ECB8
  symbol: control-keyboard-table
  sources:
  - name: Original Disassembly
    author: —
    description: Nessun commento disponibile.
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Nessun commento disponibile.
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$ECB8**: free byte'
---

# $EC78 — control keyboard table

## Disassemblatura
```assembly
.EC78  FF FF FF FF FF FF FF FF
.EC80  1C 17 01 9F 1A 13 05 FF
.EC88  9C 12 04 1E 03 06 14 18
.EC90  1F 19 07 9E 02 08 15 16
.EC98  12 09 0A 92 0D 0B 0F 0E
.ECA0  FF 10 0C FF FF 1B 00 FF
.ECA8  1C FF 1D FF FF 1F 1E FF
.ECB0  90 06 FF 05 FF FF 11 FF
.ECB8  FF
```


## Commenti

### Original Disassembly (—)
Nessun commento disponibile.

### Commodore-64-intern-Buch (Commodore)
Nessun commento disponibile.

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$ECB8**: free byte

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
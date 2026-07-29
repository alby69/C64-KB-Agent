---
title: standard keyboard table
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
  address: $EB81
  address_end: $EBC1
  symbol: standard-keyboard-table
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
    description: '- **$EBC1**: free byte'
---

# $EB81 — standard keyboard table

## Disassemblatura
```assembly
.EB81  14 0D 1D 88 85 86 87 11
.EB89  33 57 41 34 5A 53 45 01
.EB91  35 52 44 36 43 46 54 58
.EB99  37 59 47 38 42 48 55 56
.EBA1  39 49 4A 30 4D 4B 4F 4E
.EBA9  2B 50 4C 2D 2E 3A 40 2C
.EBB1  5C 2A 3B 13 01 3D 5E 2F
.EBB9  31 5F 04 32 20 02 51 03
.EBC1  FF
```


## Commenti

### Original Disassembly (—)
Nessun commento disponibile.

### Commodore-64-intern-Buch (Commodore)
Nessun commento disponibile.

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$EBC1**: free byte

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
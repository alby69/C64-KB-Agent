---
title: CBM key keyboard table
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
  address: $EC03
  address_end: $EC43
  symbol: cbm-key-keyboard-table
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
    description: '- **$EC43**: free byte'
---

# $EC03 — CBM key keyboard table

## Disassemblatura
```assembly
.EC03  94 8D 9D 8C 89 8A 8B 91
.EC0B  96 B3 B0 97 AD AE B1 01
.EC13  98 B2 AC 99 BC BB A3 BD
.EC1B  9A B7 A5 9B BF B4 B8 BE
.EC23  29 A2 B5 30 A7 A1 B9 AA
.EC2B  A6 AF B6 DC 3E 5B A4 3C
.EC33  A8 DF 5D 93 01 3D DE 3F
.EC3B  81 5F 04 95 A0 02 AB 83
.EC43  FF
```


## Commenti

### Original Disassembly (—)
Nessun commento disponibile.

### Commodore-64-intern-Buch (Commodore)
Nessun commento disponibile.

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$EC43**: free byte

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
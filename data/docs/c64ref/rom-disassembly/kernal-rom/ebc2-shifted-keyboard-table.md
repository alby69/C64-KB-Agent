---
title: shifted keyboard table
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
  address: $EBC2
  address_end: $EC02
  symbol: shifted-keyboard-table
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
    description: '- **$EC02**: free byte'
---

# $EBC2 — shifted keyboard table

## Disassemblatura
```assembly
.EBC2  94 8D 9D 8C 89 8A 8B 91
.EBCA  23 D7 C1 24 DA D3 C5 01
.EBD2  25 D2 C4 26 C3 C6 D4 D8
.EBDA  27 D9 C7 28 C2 C8 D5 D6
.EBE2  29 C9 CA 30 CD CB CF CE
.EBEA  DB D0 CC DD 3E 5B BA 3C
.EBF2  A9 C0 5D 93 01 3D DE 3F
.EBFA  21 5F 04 22 A0 02 D1 83
.EC02  FF
```


## Commenti

### Original Disassembly (—)
Nessun commento disponibile.

### Commodore-64-intern-Buch (Commodore)
Nessun commento disponibile.

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$EC02**: free byte

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
---
title: table addresses
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
- eb79-dekodiertabellen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $EB79
  address_end: $EB7F
  symbol: table-addresses
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$EB79**: standard'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Nessun commento disponibile.
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$EB79**: standard'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$EB79**: vector to unshifted keyboard, $eb81'
---

# $EB79 — table addresses

## Disassemblatura
```assembly
.EB79  81 EB   ; standard
.EB7B  C2 EB   ; shift
.EB7D  03 EC   ; commodore
.EB7F  78 EC   ; control
```


## Commenti

### Original Disassembly (—)
- **$EB79**: standard
- **$EB7B**: shift
- **$EB7D**: commodore
- **$EB7F**: control

### Commodore-64-intern-Buch (Commodore)
Nessun commento disponibile.

### Marko Mäkelä (Marko Mäkelä)
- **$EB79**: standard
- **$EB7B**: shift
- **$EB7D**: commodore key
- **$EB7F**: control

### Magnus Nyman (Magnus Nyman)
- **$EB79**: vector to unshifted keyboard, $eb81
- **$EB7B**: vector to shifted keyboard, $ebc2
- **$EB7D**: vector to cbm keyboard, $ec03
- **$EB7F**: vector to ctrl keyboard, $ec78

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
---
title: hardware vectors
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/original_disassembly.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- fce2-reset
- fffa-hardware-vektoren
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $FFFA
  address_end: $FFFE
  symbol: hardware-vectors
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FFFA**: NMI Vector'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$FFFA**: NMI Vektor'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: Nessun commento disponibile.
---

# $FFFA — hardware vectors

## Disassemblatura
```assembly
.FFFA  43 FE   ; NMI Vector
.FFFC  E2 FC   ; RESET Vector
.FFFE  48 FF   ; IRQ Vector
```


## Commenti

### Original Disassembly (—)
- **$FFFA**: NMI Vector
- **$FFFC**: RESET Vector
- **$FFFE**: IRQ Vector

### Commodore-64-intern-Buch (Commodore)
- **$FFFA**: NMI Vektor
- **$FFFC**: RESET Vektor
- **$FFFE**: IRQ Vektor

### Magnus Nyman (Magnus Nyman)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
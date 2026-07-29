---
title: set timeout on serial bus
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
- fe21-timeout-flag-fr-iec-setzen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $FE21
  address_end: $FE24
  symbol: set-timeout-on-serial-bus
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FE21**: save serial bus timeout flag'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$FE21**: Timeout-disable'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$FE21**: store in TIMOUT'
---

# $FE21 — set timeout on serial bus

## Disassemblatura
```assembly
.FE21  8D 85 02 STA $0285   ; save serial bus timeout flag
.FE24  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$FE21**: save serial bus timeout flag

### Commodore-64-intern-Buch (Commodore)
- **$FE21**: Timeout-disable
- **$FE24**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$FE21**: store in TIMOUT

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
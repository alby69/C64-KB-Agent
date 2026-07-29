---
title: set logical, first and second addresses
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
- fe00-file-setzen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $FE00
  address_end: $FE06
  symbol: set-logical-first-and-second-addresses
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FE00**: save the logical file'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$FE00**: logische Filenummer'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$FE00**: store logical filenumber in LA'
---

# $FE00 — set logical, first and second addresses

## Disassemblatura
```assembly
.FE00  85 B8    STA $B8   ; save the logical file
.FE02  86 BA    STX $BA   ; save the device number
.FE04  84 B9    STY $B9   ; save the secondary address
.FE06  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$FE00**: save the logical file
- **$FE02**: save the device number
- **$FE04**: save the secondary address

### Commodore-64-intern-Buch (Commodore)
- **$FE00**: logische Filenummer
- **$FE02**: Geräteadresse
- **$FE04**: Sekundäradresse
- **$FE06**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$FE00**: store logical filenumber in LA
- **$FE02**: store devicenumber in FA
- **$FE04**: store secondary address in SA

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
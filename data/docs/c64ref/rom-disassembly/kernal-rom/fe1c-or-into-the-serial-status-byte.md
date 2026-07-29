---
title: OR into the serial status byte
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
- fe1c-status-setzen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $FE1C
  address_end: $FE20
  symbol: or-into-the-serial-status-byte
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FE1C**: OR with the serial status byte'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$FE1C**: Statusflag testen und'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $FE1C — OR into the serial status byte

## Disassemblatura
```assembly
.FE1C  05 90    ORA $90   ; OR with the serial status byte
.FE1E  85 90    STA $90   ; save the serial status byte
.FE20  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$FE1C**: OR with the serial status byte
- **$FE1E**: save the serial status byte

### Commodore-64-intern-Buch (Commodore)
- **$FE1C**: Statusflag testen und
- **$FE1E**: wieder abspeichern
- **$FE20**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
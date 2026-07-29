---
title: control kernal messages
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
- fe18-meldungen-setzen
- fe1a-read-st
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $FE18
  address_end: $FE1A
  symbol: control-kernal-messages
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FE18**: set message mode flag'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$FE18**: Ausgabeflag (Direktmodus)'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$FE18**: store MSGFLG'
---

# $FE18 — control kernal messages

## Disassemblatura
```assembly
.FE18  85 9D    STA $9D   ; set message mode flag
.FE1A  A5 90    LDA $90   ; read the serial status byte
```


## Commenti

### Original Disassembly (—)
- **$FE18**: set message mode flag
- **$FE1A**: read the serial status byte

### Commodore-64-intern-Buch (Commodore)
- **$FE18**: Ausgabeflag (Direktmodus)
- **$FE1A**: Statusflag holen

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$FE18**: store MSGFLG
- **$FE1A**: read STATUS

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
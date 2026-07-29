---
title: fetch a screen address
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
- e9f0-zeile-x
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E9F0
  address_end: $E9FE
  symbol: fetch-a-screen-address
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E9F0**: get the start of line low byte from the ROM table'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E9F0**: LOW-Byte'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E9F0**: table of screen line to bytes'
---

# $E9F0 — fetch a screen address

## Disassemblatura
```assembly
.E9F0  BD F0 EC LDA $ECF0,X   ; get the start of line low byte from the ROM table
.E9F3  85 D1    STA $D1   ; set the current screen line pointer low byte
.E9F5  B5 D9    LDA $D9,X   ; get the start of line high byte from the RAM table
.E9F7  29 03    AND #$03   ; mask 0000 00xx, line memory page
.E9F9  0D 88 02 ORA $0288   ; OR with the screen memory page
.E9FC  85 D2    STA $D2   ; save the current screen line pointer high byte
.E9FE  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E9F0**: get the start of line low byte from the ROM table
- **$E9F3**: set the current screen line pointer low byte
- **$E9F5**: get the start of line high byte from the RAM table
- **$E9F7**: mask 0000 00xx, line memory page
- **$E9F9**: OR with the screen memory page
- **$E9FC**: save the current screen line pointer high byte

### Commodore-64-intern-Buch (Commodore)
- **$E9F0**: LOW-Byte
- **$E9F3**: holen
- **$E9F5**: HIGH-Byte
- **$E9F7**: des
- **$E9F9**: Video-
- **$E9FC**: RAM
- **$E9FE**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E9F0**: table of screen line to bytes
- **$E9F3**: <PNT, current screen line address
- **$E9F5**: LDTB1, screen line link table
- **$E9F9**: HIBASE, page of top screen
- **$E9FC**: >PNT

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
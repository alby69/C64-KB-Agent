---
title: save the character and colour to the screen @ the cursor
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
- ea1c-bildschirm-setzen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $EA1C
  address_end: $EA23
  symbol: save-the-character-and-colour-to-the-screen-the-cursor
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$EA1C**: get the cursor column'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$EA1C**: Spaltenposition'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $EA1C — save the character and colour to the screen @ the cursor

## Disassemblatura
```assembly
.EA1C  A4 D3    LDY $D3   ; get the cursor column
.EA1E  91 D1    STA ($D1),Y   ; save the character from current screen line
.EA20  8A       TXA   ; copy the colour to A
.EA21  91 F3    STA ($F3),Y   ; save to colour RAM
.EA23  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$EA1C**: get the cursor column
- **$EA1E**: save the character from current screen line
- **$EA20**: copy the colour to A
- **$EA21**: save to colour RAM

### Commodore-64-intern-Buch (Commodore)
- **$EA1C**: Spaltenposition
- **$EA1E**: Zeichen in Akku auf Bildschirm
- **$EA20**: Farb-Code von x in Akku
- **$EA21**: in Farb-RAM schreiben
- **$EA23**: Rücksprung zum Hauptprogramm

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
---
title: Background Color 0
source_url: https://github.com/mist64/c64ref/blob/main/src/c64io/mapping_the_commodore_64.txt
category: reference
topics:
- io-map
- vic-ii-registers
difficulty: intermediate
language: assembly
hardware:
- VIC-II
related: []
scraped_at: '2026-07-29'
c64ref:
  module: c64io
  source_files:
  - mapping_the_commodore_64.txt
  - c64_programmer's_reference_guide.txt
  address: $D021
  symbol: BGCOL0
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Background Color 0
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This register sets the background color for all text modes, sprite
---

# BGCOL0 — Background Color 0 ($D021)

## Panoramica
Il registro o area di memoria BGCOL0 è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$D021` (`53281` decimale)
- **Range**: `$D021`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
Background Color 0

### Mapping the Commodore 64 (Sheldon Leemon)
This register sets the background color for all text modes, sprite
     graphics, and multicolor bitmap graphics.  The default color value is
     6 (blue).

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
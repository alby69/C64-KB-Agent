---
title: Background Color 3
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
  address: $D024
  symbol: BGCOL3
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Background Color 3
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This register sets the background color for characters having screen
---

# BGCOL3 — Background Color 3 ($D024)

## Panoramica
Il registro o area di memoria BGCOL3 è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$D024` (`53284` decimale)
- **Range**: `$D024`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
Background Color 3

### Mapping the Commodore 64 (Sheldon Leemon)
This register sets the background color for characters having screen
     codes between 192 and 255 in extended background color text mode.  The
     default color value is 3 (cyan).

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
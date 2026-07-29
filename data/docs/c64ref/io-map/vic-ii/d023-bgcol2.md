---
title: Background Color 2
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
  address: $D023
  symbol: BGCOL2
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Background Color 2
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This register sets the color for the 10 bit-pair of multicolor
---

# BGCOL2 — Background Color 2 ($D023)

## Panoramica
Il registro o area di memoria BGCOL2 è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$D023` (`53283` decimale)
- **Range**: `$D023`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
Background Color 2

### Mapping the Commodore 64 (Sheldon Leemon)
This register sets the color for the 10 bit-pair of multicolor
     character graphics, and the background color for characters having
     screen codes 128-191 in extended background color text mode.  The
     default color value is 2 (red).

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
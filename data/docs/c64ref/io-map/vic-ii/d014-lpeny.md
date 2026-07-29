---
title: Light Pen Vertical Position
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
  address: $D014
  symbol: LPENY
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Light-Pen Latch Y Pos
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This location holds the vertical position of the light pen.  Since
---

# LPENY — Light Pen Vertical Position ($D014)

## Panoramica
Il registro o area di memoria LPENY è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$D014` (`53268` decimale)
- **Range**: `$D014`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
Light-Pen Latch Y Pos

### Mapping the Commodore 64 (Sheldon Leemon)
This location holds the vertical position of the light pen.  Since
     there are only 200 visible scan lines on the screen, the value in this
     register corresponds exactly to the current raster scan line.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
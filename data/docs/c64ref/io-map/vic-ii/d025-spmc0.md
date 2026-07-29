---
title: Sprite Multicolor Register 0
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
  address: $D025
  symbol: SPMC0
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Sprite Multi-Color Register 0
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This register sets the color that is displayed by the 01 bit-pair
      in
---

# SPMC0 — Sprite Multicolor Register 0 ($D025)

## Panoramica
Il registro o area di memoria SPMC0 è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$D025` (`53285` decimale)
- **Range**: `$D025`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
Sprite Multi-Color Register 0

### Mapping the Commodore 64 (Sheldon Leemon)
This register sets the color that is displayed by the 01 bit-pair in
     multicolor sprite graphics.  The default color value is 4 (purple).

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
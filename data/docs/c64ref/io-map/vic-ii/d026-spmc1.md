---
title: Sprite Multicolor Register 1
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
  address: $D026
  symbol: SPMC1
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Sprite Multi-Color Register 1
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This register sets the color that is displayed by the 11 bit-pair
      in
---

# SPMC1 — Sprite Multicolor Register 1 ($D026)

## Panoramica
Il registro o area di memoria SPMC1 è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$D026` (`53286` decimale)
- **Range**: `$D026`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
Sprite Multi-Color Register 1

### Mapping the Commodore 64 (Sheldon Leemon)
This register sets the color that is displayed by the 11 bit-pair in
     multicolor sprite graphics.  The default color value is 0 (black).

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
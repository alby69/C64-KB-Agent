---
title: Read Game Paddle 2 (or 4) Position
source_url: https://github.com/mist64/c64ref/blob/main/src/c64io/mapping_the_commodore_64.txt
category: reference
topics:
- io-map
- sid-registers
difficulty: intermediate
language: assembly
hardware:
- SID
related: []
scraped_at: '2026-07-29'
c64ref:
  module: c64io
  source_files:
  - mapping_the_commodore_64.txt
  - c64_programmer's_reference_guide.txt
  address: $D41A
  symbol: POTY
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Analog/Digital Converter: Game Paddle 2 (0-255)'
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: Read Game Paddle 2 (or 4) Position
---

# POTY — Read Game Paddle 2 (or 4) Position ($D41A)

## Panoramica
Il registro o area di memoria POTY è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$D41A` (`54298` decimale)
- **Range**: `$D41A`
- **Dimensione**: `1 byte`
- **Permessi**: `R`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
Analog/Digital Converter: Game Paddle 2 (0-255)

### Mapping the Commodore 64 (Sheldon Leemon)
Read Game Paddle 2 (or 4) Position

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
---
title: Most Significant Bits of Sprites 0-7 Horizontal Position
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
  address: $D010
  symbol: MSIGX
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Sprites 0-7 X Pos (msb of X coord.)
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: 0    Most significant bit of Sprite 0 horizontal position
---

# MSIGX — Most Significant Bits of Sprites 0-7 Horizontal Position ($D010)

## Panoramica
Il registro o area di memoria MSIGX è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$D010` (`53264` decimale)
- **Range**: `$D010`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
Sprites 0-7 X Pos (msb of X coord.)

### Mapping the Commodore 64 (Sheldon Leemon)
0    Most significant bit of Sprite 0 horizontal position
1    Most significant bit of Sprite 1 horizontal position
2    Most significant bit of Sprite 2 horizontal position
3    Most significant bit of Sprite 3 horizontal position
4    Most significant bit of Sprite 4 horizontal position
5    Most significant bit of Sprite 5 horizontal position
6    Most significant bit of Sprite 6 horizontal position
7    Most significant bit of Sprite 7 horizontal position

     Setting one of these bites to 1 adds 256 to the horizontal position of
     the corresponding sprite.  Resetting one of these bits to 0 restricts
     the horizontal position of the corresponding sprite to a value of 255
     or less

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
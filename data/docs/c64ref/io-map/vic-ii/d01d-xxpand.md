---
title: Sprite Horizontal Expansion Register
source_url: https://github.com/mist64/c64ref/blob/main/src/c64io/mapping_the_commodore_64.txt
category: reference
topics:
- io-map
- vic-ii-registers
difficulty: intermediate
language: assembly
hardware:
- VIC-II
related:
- d017
scraped_at: '2026-07-29'
c64ref:
  module: c64io
  source_files:
  - mapping_the_commodore_64.txt
  - c64_programmer's_reference_guide.txt
  address: $D01D
  symbol: XXPAND
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Sprites 0-7 Expand 2x Horizontal (X)
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: 0    Expand Sprite 0 horizontally (1=double-width sprite, 0=normal
      width)
---

# XXPAND — Sprite Horizontal Expansion Register ($D01D)

## Panoramica
Il registro o area di memoria XXPAND è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$D01D` (`53277` decimale)
- **Range**: `$D01D`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
Sprites 0-7 Expand 2x Horizontal (X)

### Mapping the Commodore 64 (Sheldon Leemon)
0    Expand Sprite 0 horizontally (1=double-width sprite, 0=normal width)
1    Expand Sprite 1 horizontally (1=double-width sprite, 0=normal width)
2    Expand Sprite 2 horizontally (1=double-width sprite, 0=normal width)
3    Expand Sprite 3 horizontally (1=double-width sprite, 0=normal width)
4    Expand Sprite 4 horizontally (1=double-width sprite, 0=normal width)
5    Expand Sprite 5 horizontally (1=double-width sprite, 0=normal width)
6    Expand Sprite 6 horizontally (1=double-width sprite, 0=normal width)
7    Expand Sprite 7 horizontally (1=double-width sprite, 0=normal width)

     This register can be used to double the width of any sprite.  Setting
     any bit of this register to 1 will cause each dot of the corresponding
     sprite shape to be displayed twice as wide as normal, so that without
     changing its horizontal resolution, the sprite takes up twice as much
     space.  The horizontal expansion feature can be used alone, or in
     combination with the vertical expansion register at 53271 ($D017).

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
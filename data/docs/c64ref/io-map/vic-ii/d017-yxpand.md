---
title: Sprite Vertical Expansion Register
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
  address: $D017
  symbol: YXPAND
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Sprites 0-7 Expand 2x Vertical (Y)
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: 0    Expand Sprite 0 vertically (1=double height, 0=normal height)
---

# YXPAND — Sprite Vertical Expansion Register ($D017)

## Panoramica
Il registro o area di memoria YXPAND è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$D017` (`53271` decimale)
- **Range**: `$D017`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
Sprites 0-7 Expand 2x Vertical (Y)

### Mapping the Commodore 64 (Sheldon Leemon)
0    Expand Sprite 0 vertically (1=double height, 0=normal height)
1    Expand Sprite 1 vertically (1=double height, 0=normal height)
2    Expand Sprite 2 vertically (1=double height, 0=normal height)
3    Expand Sprite 3 vertically (1=double height, 0=normal height)
4    Expand Sprite 4 vertically (1=double height, 0=normal height)
5    Expand Sprite 5 vertically (1=double height, 0=normal height)
6    Expand Sprite 6 vertically (1=double height, 0=normal height)
7    Expand Sprite 7 vertically (1=double height, 0=normal height)

     This register can be used to double the height of any sprite.  When
     the bit in this register that corresponds to a particular sprite is
     set to 1, each dot of the 24 by 21 sprite dot matrix will become two
     raster scan lines high instead of one.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
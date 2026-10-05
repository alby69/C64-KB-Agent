---
id: d01d-xxpand
type: entity
title: Sprite Horizontal Expansion Register
aliases:
- Sprite Horizontal Expansion Register
tags:
- io-map
- vic-ii-registers
sources:
- path: data/docs/c64ref/io-map/vic-ii/d01d-xxpand.md
  sha256: 11c23111e369d39160df0502b0a26f94a0061ac5463c01620cf48e732e43c65a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-d01d-xxpand
---

# Sprite Horizontal Expansion Register



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

## References
- Source: [[src-d01d-xxpand]]

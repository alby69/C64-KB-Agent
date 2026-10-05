---
id: d010-msigx
type: entity
title: Most Significant Bits of Sprites 0-7 Horizontal Position
aliases:
- Most Significant Bits of Sprites 0-7 Horizontal Position
tags:
- io-map
- vic-ii-registers
sources:
- path: data/docs/c64ref/io-map/vic-ii/d010-msigx.md
  sha256: 7f90de132087968b662bd3a112d89878b4367114371408809af434dd14833ba6
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-d010-msigx
---

# Most Significant Bits of Sprites 0-7 Horizontal Position



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

## References
- Source: [[src-d010-msigx]]

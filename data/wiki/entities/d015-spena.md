---
id: d015-spena
type: entity
title: Sprite Enable Register
aliases:
- Sprite Enable Register
tags:
- io-map
- vic-ii-registers
sources:
- path: data/docs/c64ref/io-map/vic-ii/d015-spena.md
  sha256: 058c7424ac6bf8156ef538f5d385ac03d85f27182c55032a0acde422093d130b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-d015-spena
---

# Sprite Enable Register



# SPENA — Sprite Enable Register ($D015)

## Panoramica
Il registro o area di memoria SPENA è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$D015` (`53269` decimale)
- **Range**: `$D015`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
Sprite display Enable: 1 = Enable

### Mapping the Commodore 64 (Sheldon Leemon)
0    Enable Sprite 0 (1=sprite is on, 0=sprite is off)
1    Enable Sprite 1 (1=sprite is on, 0=sprite is off)
2    Enable Sprite 2 (1=sprite is on, 0=sprite is off)
3    Enable Sprite 3 (1=sprite is on, 0=sprite is off)
4    Enable Sprite 4 (1=sprite is on, 0=sprite is off)
5    Enable Sprite 5 (1=sprite is on, 0=sprite is off)
6    Enable Sprite 6 (1=sprite is on, 0=sprite is off)
7    Enable Sprite 7 (1=sprite is on, 0=sprite is off)

     In order for any sprite to be displayed, the corresponding bit in this
     register must be set to 1 (the default for this location is 0).  Of
     course, just setting this bit along will not guarantee that a sprite
     will be shown on the screen.  The Sprite Data Pointer must indicate a
     data area that holds some values other than 0.  The Sprite Color
     Register must also contain a value other than that of the background
     color.  In addition, the Sprite Horizontal and Vertical Position
     Registers must be set for positions that lie within the visible screen
     range in order for a sprite to appear on screen.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-d015-spena]]

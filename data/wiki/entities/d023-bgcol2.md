---
id: d023-bgcol2
type: entity
title: Background Color 2
aliases:
- Background Color 2
tags:
- io-map
- vic-ii-registers
sources:
- path: data/docs/c64ref/io-map/vic-ii/d023-bgcol2.md
  sha256: e7c291839c8a1bb72da9e0e185e10f688f3881c764caef60ab7771a8b62242ee
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-d023-bgcol2
---

# Background Color 2



# BGCOL2 — Background Color 2 ($D023)

## Panoramica
Il registro o area di memoria BGCOL2 è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$D023` (`53283` decimale)
- **Range**: `$D023`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
Background Color 2

### Mapping the Commodore 64 (Sheldon Leemon)
This register sets the color for the 10 bit-pair of multicolor
     character graphics, and the background color for characters having
     screen codes 128-191 in extended background color text mode.  The
     default color value is 2 (red).

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-d023-bgcol2]]

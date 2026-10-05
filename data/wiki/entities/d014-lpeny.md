---
id: d014-lpeny
type: entity
title: Light Pen Vertical Position
aliases:
- Light Pen Vertical Position
tags:
- io-map
- vic-ii-registers
sources:
- path: data/docs/c64ref/io-map/vic-ii/d014-lpeny.md
  sha256: 606d70bcdc83df3331080bad1dd12eacfdb8bf56740aa07055a6ede98bd433af
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-d014-lpeny
---

# Light Pen Vertical Position



# LPENY — Light Pen Vertical Position ($D014)

## Panoramica
Il registro o area di memoria LPENY è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$D014` (`53268` decimale)
- **Range**: `$D014`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
Light-Pen Latch Y Pos

### Mapping the Commodore 64 (Sheldon Leemon)
This location holds the vertical position of the light pen.  Since
     there are only 200 visible scan lines on the screen, the value in this
     register corresponds exactly to the current raster scan line.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-d014-lpeny]]

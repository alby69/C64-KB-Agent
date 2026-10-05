---
id: d025-spmc0
type: entity
title: Sprite Multicolor Register 0
aliases:
- Sprite Multicolor Register 0
tags:
- io-map
- vic-ii-registers
sources:
- path: data/docs/c64ref/io-map/vic-ii/d025-spmc0.md
  sha256: 4de8e1d0392c499f092a4760438bab2087a36ba165bf65bb84e336f8166b5da7
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-d025-spmc0
---

# Sprite Multicolor Register 0



# SPMC0 — Sprite Multicolor Register 0 ($D025)

## Panoramica
Il registro o area di memoria SPMC0 è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$D025` (`53285` decimale)
- **Range**: `$D025`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
Sprite Multi-Color Register 0

### Mapping the Commodore 64 (Sheldon Leemon)
This register sets the color that is displayed by the 01 bit-pair in
     multicolor sprite graphics.  The default color value is 4 (purple).

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-d025-spmc0]]

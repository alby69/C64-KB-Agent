---
id: d026-spmc1
type: entity
title: Sprite Multicolor Register 1
aliases:
- Sprite Multicolor Register 1
tags:
- io-map
- vic-ii-registers
sources:
- path: data/docs/c64ref/io-map/vic-ii/d026-spmc1.md
  sha256: c853502e88f8f871715491158a708ca8e9027640e74357b7da9a16a4075106b1
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-d026-spmc1
---

# Sprite Multicolor Register 1



# SPMC1 — Sprite Multicolor Register 1 ($D026)

## Panoramica
Il registro o area di memoria SPMC1 è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$D026` (`53286` decimale)
- **Range**: `$D026`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
Sprite Multi-Color Register 1

### Mapping the Commodore 64 (Sheldon Leemon)
This register sets the color that is displayed by the 11 bit-pair in
     multicolor sprite graphics.  The default color value is 0 (black).

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-d026-spmc1]]

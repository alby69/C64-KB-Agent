---
id: d01f-spbgcl
type: entity
title: Sprite to Foreground Collision Register
aliases:
- Sprite to Foreground Collision Register
tags:
- io-map
- vic-ii-registers
sources:
- path: data/docs/c64ref/io-map/vic-ii/d01f-spbgcl.md
  sha256: e18b5421d462bf0de5430917a248a97ff739fc114d2ba41082116c0bedd514af
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-d01f-spbgcl
---

# Sprite to Foreground Collision Register



# SPBGCL — Sprite to Foreground Collision Register ($D01F)

## Panoramica
Il registro o area di memoria SPBGCL è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$D01F` (`53279` decimale)
- **Range**: `$D01F`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
Sprite to Background Collision Detect

### Mapping the Commodore 64 (Sheldon Leemon)
0    Did Sprite 0 collide with the foreground display?  (1=yes)
1    Did Sprite 1 collide with the foreground display?  (1=yes)
2    Did Sprite 2 collide with the foreground display?  (1=yes)
3    Did Sprite 3 collide with the foreground display?  (1=yes)
4    Did Sprite 4 collide with the foreground display?  (1=yes)
5    Did Sprite 5 collide with the foreground display?  (1=yes)
6    Did Sprite 6 collide with the foreground display?  (1=yes)
7    Did Sprite 7 collide with the foreground display?  (1=yes)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-d01f-spbgcl]]

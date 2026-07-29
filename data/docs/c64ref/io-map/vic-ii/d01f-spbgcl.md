---
title: Sprite to Foreground Collision Register
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
  address: $D01F
  symbol: SPBGCL
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Sprite to Background Collision Detect
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: 0    Did Sprite 0 collide with the foreground display?  (1=yes)
---

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
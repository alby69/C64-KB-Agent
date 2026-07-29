---
title: Sprite Enable Register
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
  address: $D015
  symbol: SPENA
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Sprite display Enable: 1 = Enable'
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: 0    Enable Sprite 0 (1=sprite is on, 0=sprite is off)
---

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
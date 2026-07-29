---
title: Sprite to Foreground Display Priority Register
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
  address: $D01B
  symbol: SPBGPR
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Sprite to Background Display Priority: 1 = Sprite'
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: 0    Select display priority of Sprite 0 to foreground (0=sprite
---

# SPBGPR — Sprite to Foreground Display Priority Register ($D01B)

## Panoramica
Il registro o area di memoria SPBGPR è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$D01B` (`53275` decimale)
- **Range**: `$D01B`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
Sprite to Background Display Priority: 1 = Sprite

### Mapping the Commodore 64 (Sheldon Leemon)
0    Select display priority of Sprite 0 to foreground (0=sprite
       appears in front of foreground)
1    Select display priority of Sprite 1 to foreground (0=sprite
       appears in front of foreground)
2    Select display priority of Sprite 2 to foreground (0=sprite
       appears in front of foreground)
3    Select display priority of Sprite 3 to foreground (0=sprite
       appears in front of foreground)
4    Select display priority of Sprite 4 to foreground (0=sprite
       appears in front of foreground)
5    Select display priority of Sprite 5 to foreground (0=sprite
       appears in front of foreground)
6    Select display priority of Sprite 6 to foreground (0=sprite
       appears in front of foreground)
7    Select display priority of Sprite 7 to foreground (0=sprite
       appears in front of foreground)

     If a sprite is positioned to appear at a spot on the screen that is
     already occupied by text or bitmap graphics, a conflict arises.  The
     contents of this register determines which one will be displayed in
     such a situation.  If the bit that corresponds to a particular sprite
     is set to 0, the sprite will be displayed in front of the foreground
     graphics data.  If that bit is set to 1, the foreground data will be
     displayed in front of the sprite.  The default value that this
     register is set to at power-on is 0, so all sprites start out with
     priority over foreground graphics.

     Note that for the purpose of priority, the 01 bit-pair of multicolor
     graphics modes is considered to display a background color, and
     therefore will be shown behind sprite graphics even if the foreground
     graphics data takes priority.  Also, between the sprites themselves
     there is a fixed priority.  Each sprite has priority over all
     higher-number sprites, so that Sprite 0 is displayed in front of all
     the others.

     The use of priority can aid in creating three-dimensional effects, by
     allowing some objects on the screen to pass in front of or behind
     other objects.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
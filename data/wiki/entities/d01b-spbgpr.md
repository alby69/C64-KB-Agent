---
id: d01b-spbgpr
type: entity
title: Sprite to Foreground Display Priority Register
aliases:
- Sprite to Foreground Display Priority Register
tags:
- io-map
- vic-ii-registers
sources:
- path: data/docs/c64ref/io-map/vic-ii/d01b-spbgpr.md
  sha256: 0df14c49820b792788996edeb69020d1e5fa8d672ab2c9b504eb08347df87ff5
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-d01b-spbgpr
---

# Sprite to Foreground Display Priority Register



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

## References
- Source: [[src-d01b-spbgpr]]

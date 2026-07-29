---
title: Sprite Multicolor Registers
source_url: https://github.com/mist64/c64ref/blob/main/src/c64io/mapping_the_commodore_64.txt
category: reference
topics:
- io-map
- vic-ii-registers
difficulty: intermediate
language: assembly
hardware:
- VIC-II
related:
- d016
- d025
- d026
- d027
scraped_at: '2026-07-29'
c64ref:
  module: c64io
  source_files:
  - mapping_the_commodore_64.txt
  - c64_programmer's_reference_guide.txt
  address: $D01C
  symbol: SPMC
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Sprites 0-7 Multi-Color Mode Select: 1 = M.C.M'
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: 0    Select multicolor mode for Sprite 0 (1=multicolor, 0=hi-res)
---

# SPMC — Sprite Multicolor Registers ($D01C)

## Panoramica
Il registro o area di memoria SPMC è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$D01C` (`53276` decimale)
- **Range**: `$D01C`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
Sprites 0-7 Multi-Color Mode Select: 1 = M.C.M

### Mapping the Commodore 64 (Sheldon Leemon)
0    Select multicolor mode for Sprite 0 (1=multicolor, 0=hi-res)
1    Select multicolor mode for Sprite 1 (1=multicolor, 0=hi-res)
2    Select multicolor mode for Sprite 2 (1=multicolor, 0=hi-res)
3    Select multicolor mode for Sprite 3 (1=multicolor, 0=hi-res)
4    Select multicolor mode for Sprite 4 (1=multicolor, 0=hi-res)
5    Select multicolor mode for Sprite 5 (1=multicolor, 0=hi-res)
6    Select multicolor mode for Sprite 6 (1=multicolor, 0=hi-res)
7    Select multicolor mode for Sprite 7 (1=multicolor, 0=hi-res)

     Sprite multicolor mode is very similar to text and bitmap multicolor
     modes (see Bit 4 of 53270, $D016).  Normally, the color of each dot of
     the sprite is controlled by a single bit of sprite shape data.  When
     the mode is enabled for a sprite, by setting the corresponding bit of
     this register to 1, the bits of sprite shape data are grouped together
     in pairs, with each pair of bits controlling a double-wide dot of the
     sprite display.  By sacrificing some of the horizontal resolution (the
     sprite, although the same size, is now only 12 dots wide), you gain
     the use of two additional colors.  The four possible combinations of
     these bit-pairs display dot colors from the following sources:

     | 00 | Background Color Register 0 (transparent)   |
     | 01 | Sprite Multicolor Register 0 (53285, $D025) |
     | 10 | Sprite Color Registers (53287-94, $D027-E)  |
     | 11 | Sprite Multicolor Register 1 (53286, $D026) |

     Like multicolor text characters, multicolor sprites all share two
     color registers.  While each sprite can display three foreground
     colors, only one of these colors in unique to that sprite.  The number
     of unique colors may be increased by combining more than one sprite
     into a single character.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
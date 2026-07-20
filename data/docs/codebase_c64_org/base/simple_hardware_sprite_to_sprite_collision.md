---
title: base:simple_hardware_sprite_to_sprite_collision [Codebase64 wiki]
source_url: https://codebase.c64.org/doku.php?id=base%3Asimple_hardware_sprite_to_sprite_collision
category: reference
topics:
- basic
- assembly
- sprite programming
difficulty: beginner
language: mixed
hardware:
- VIC-II
related:
- vic-ii-registers
- raster-interrupts
- sprite-programming
scraped_at: '2026-07-20'
---


# base:simple_hardware_sprite_to_sprite_collision [Codebase64 wiki]

base:simple_hardware_sprite_to_sprite_collision

                ### Sprite/Sprite hardware collision

One of the most easiest methods to make the player sprite collide into sprite 2 or higher is by using a simple hardware collision. This is triggered by using $D01E. Unfortunately with most games these days, $D01E is very useless, therefore a software collision is used. Anyway, if you wish to use a sprite/sprite collision using hardware pokes, then here is how it works.

```
  
          LDA $D01E ;Read hardware sprite/sprite collision
          LSR       ; (LSR A for TASM users) Collision for sprite 1
          BCC HIT
          RTS       ;No collision
HIT       INC $D020
          JMP HIT
```
This source above shows that if the very first sprite hits any other sprite, the border will flash

If you want the next sprite to read hardware collision to other sprites just add another LSR, etc.

base/simple_hardware_sprite_to_sprite_collision.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
LDA $D01E ;Read hardware sprite/sprite collision
          LSR       ; (LSR A for TASM users) Collision for sprite 1
          BCC HIT
          RTS       ;No collision
HIT       INC $D020
          JMP HIT
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Asimple_hardware_sprite_to_sprite_collision](https://codebase.c64.org/doku.php?id=base%3Asimple_hardware_sprite_to_sprite_collision)*


### Collegamenti e Riferimenti Hardware
- **$D020 (Border Color)**: Associato al chip VIC-II. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#d020).

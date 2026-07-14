---
title: base:simple_hardware_sprite_to_background_collision [Codebase64 wiki]
source_url: https://codebase.c64.org/doku.php?id=base%3Asimple_hardware_sprite_to_background_collision
category: reference
topics:
- sprite programming
- assembly
difficulty: beginner
language: assembly
hardware:
- VIC-II
related:
- sprite-programming
- raster-interrupts
- vic-ii-registers
scraped_at: '2026-07-14'
---

# base:simple_hardware_sprite_to_background_collision [Codebase64 wiki]

base:simple_hardware_sprite_to_background_collision

                #### Simple Hardware Sprite to Background collision

Using $D01E causes a simple hardware sprite/sprite collision detection, but some games I wrote i.e. Bomb Chase, Balloonacy and Balloonacy 2 all used hardware sprite/sprite collision, which uses $D01F only for the player's sprite. Here is how the code worked.

```
       lda $d01f
       lsr a ;Sprite 0 crash into background
       bcs dead
       rts
dead   jmp kill_sprite
```
However, if you want this to work on the next sprite, just add another 'lsr' command, etc.

base/simple_hardware_sprite_to_background_collision.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`dead`** (unknown): No description available

```assembly
lda $d01f
       lsr a ;Sprite 0 crash into background
       bcs dead
       rts
dead   jmp kill_sprite
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Asimple_hardware_sprite_to_background_collision](https://codebase.c64.org/doku.php?id=base%3Asimple_hardware_sprite_to_background_collision)*

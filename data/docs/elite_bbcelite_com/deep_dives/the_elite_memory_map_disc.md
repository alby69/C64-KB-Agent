---
title: BBC Micro disc Elite memory map
source_url: https://elite.bbcelite.com/deep_dives/the_elite_memory_map_disc.html
category: deep-dive
topics:
- memory management
- basic
- raster interrupts
- assembly
difficulty: intermediate
language: mixed
hardware:
- CPU
- BASIC ROM
- KERNAL
- CIA
related:
- keyboard-handling
- joystick-reading
- raster-interrupts
- memory-map
- sprite-programming
- vic-ii-registers
- kernal-routines
- cia-registers
scraped_at: '2026-07-14'
---

# BBC Micro disc Elite memory map

## Memory usage in the enhanced disc version of Elite

Although it isn't quite as impressive as the cassette version when it comes to memory usage, the disc version of BBC Micro Elite is no slouch when it comes to squeezing every last byte out of the BBC Micro. For a start, the code spills out onto the disc, with a separate code file for flight, 16 individual files containing ship blueprints, and a further code file for when we are docked. That's why launching and docking are accompanied by so much disc activity; unlike the cassette version, the code for the disc version of Elite most definitely does not fit into a BBC Micro, at least not all at the same time.

But even with the luxury of being able to swap out the main code block when launching and docking, the disc version takes up almost every spare inch of the BBC Micro, particularly with the flight code, which is such a tight squeeze that it needs to take over the print buffer in order to fit.

The game starts with us being docked at a station, so let's take a look at the memory map for when the docked code is loaded.

## Docked memory map (T.CODE)

													 --------------------------

						This is the initial memory map for when the game starts, or when we dock and the docked code has loaded. The memory map changes slightly when we launch from the space station, as detailed in the next section, but most of the following is consistent throughout the game.

+-----------------------------------+ &FFFF | | | Machine Operating System (MOS) | | | +-----------------------------------+ &C000 | | | Paged ROMs | | | +-----------------------------------+ &8000 | | | Missile blueprint (MISSILE.bin) | | | +-----------------------------------+ &7F00 =[SHIP_MISSILE](https://elite.bbcelite.com/disc/missile_ship_blueprint/variable/ship_missile.html)| | | Memory for the split-screen mode | | | +-----------------------------------+ &6000 | | | &5F55-&5FFF unused when docked | | | +-----------------------------------+ &5F55 | | | Main game code (T.CODE) | | | +-----------------------------------+ &11E2 =[S%](https://elite.bbcelite.com/disc/docked/workspace/s_per_cent.html)| | | Break handler for flight code | | | +-----------------------------------+ &11D5 =[BRBR1](https://elite.bbcelite.com/disc/loader_3/subroutine/brbr1.html)| | | Last saved commander file | | | +-----------------------------------+ &117C =[S1%](https://elite.bbcelite.com/disc/loader_3/variable/s1_per_cent.html)| | | IRQ1 handler, mode 1 palette data | | | +-----------------------------------+ &1100 =[TVT1](https://elite.bbcelite.com/disc/loader_3/variable/tvt1.html)| | | DFS general workspace | | | +-----------------------------------+ &1000 | | | WP workspace or disc catalogue | | | +-----------------------------------+ &0E00 =[WP](https://elite.bbcelite.com/disc/docked/workspace/wp.html)| | | DFS general workspace | | | +-----------------------------------+ &0D9D | | | CATD routine in DFS NMI workspace | | | +-----------------------------------+ &0D7A =[CATD](https://elite.bbcelite.com/disc/loader_3/subroutine/catd.html)| | | DFS general workspace | | | +-----------------------------------+ &0D00 = LS% | | | Ship line heap descends from LS% | | | +-----------------------------------+ SLSP | | . . . . . . . . . . | | +-----------------------------------+ &0ABB when all ship slots are used | | | Ship data blocks ascend from K% | | | +-----------------------------------+ &0900 =[K%](https://elite.bbcelite.com/disc/docked/workspace/k_per_cent.html)| | | MOS sound/printer workspace | | | +-----------------------------------+ &0800 | | | Sine, cosine and arctan tables | | | +-----------------------------------+ &07C0 =[SNE](https://elite.bbcelite.com/disc/text_tokens/variable/sne.html)| | | Recursive text tokens (WORDS.bin) | | | +-----------------------------------+ &0400 =[QQ18](https://elite.bbcelite.com/disc/text_tokens/variable/qq18.html)| | | MOS keyboard input buffer | | | +-----------------------------------+ &03E0 | | | &03D0-&03DF unused | | | +-----------------------------------+ &03D0 | | | UP workspace | | | +-----------------------------------+ &0300 =[UP](https://elite.bbcelite.com/disc/docked/workspace/up.html)| | | MOS general workspace | | | +-----------------------------------+ &0200 | | | 6502 stack descends from &01FF | | | +-----------------------------------+ &0194 | | | Heap space ascends from XX3 | | | +-----------------------------------+ &0100 =[XX3](https://elite.bbcelite.com/disc/docked/workspace/xx3.html)| | | Zero page workspace | | | +-----------------------------------+ &0000 =[ZP](https://elite.bbcelite.com/disc/docked/workspace/zp.html)


Note that the [WP workspace](https://elite.bbcelite.com/disc/docked/workspace/wp.html) at &0E00-&0FD2 uses the same memory as the DFS disc catalogue. The game contains a routine at &0D7A called [CATD](https://elite.bbcelite.com/disc/loader_3/subroutine/catd.html) that manages this memory to ensure that the DFS and game don't clash. See the deep dive on [swapping between the docked and flight code](https://elite.bbcelite.com/docked_and_flight_code.html) for details on how this works.

## Flight memory map (D.CODE)

													 --------------------------

						The memory map for flight is, with two exceptions, the same as for when we are docked. The main difference is that instead of loading a single code file (T.CODE) as we do when we dock, we instead load two files when we launch. First, the flight code file (D.CODE) gets loaded at &11E2 and called, and then the first thing this code does is load one of the ship blueprint files (D.MOA to D.MOP) straight after the end of D.CODE at location &5600. Together, the main flight code and chosen ship blueprint file take up the same part of the memory map as the main docked code (i.e. &11E2-&5FFF), like this:

. . . . . . | | +-----------------------------------+ &6000 | | | Ship blueprints file (D.MOA-MOP) | | | +-----------------------------------+ &5600 =[XX21](https://elite.bbcelite.com/disc/ship_blueprints_a/variable/xx21.html)| | | Main game code (D.CODE) | | | +-----------------------------------+ &11E2 =[S%](https://elite.bbcelite.com/disc/docked/workspace/s_per_cent.html)| | . . . . . .

The other difference is that the main flight code binary in D.CODE doesn't contain the two-letter token table at [QQ16](https://elite.bbcelite.com/disc/docked/variable/qq16.html). Instead, the docked code moves its own copy of this 64-byte token table to location &0880, so the flight code can use it there. See the deep dive on [swapping between the docked and flight code](https://elite.bbcelite.com/docked_and_flight_code.html) for more details on this process.

The memory block from &0880 to &08BF is normally used by the MOS print buffer, but as we don't use the printer in this version of Elite, this is a safe location. During flight, then, this part of the memory map looks like this:

. . . . . . | | +-----------------------------------+ &0900 =[K%](https://elite.bbcelite.com/disc/docked/workspace/k_per_cent.html)| | | MOS sound workspace | | | +-----------------------------------+ &08C0 | | | Two-letter token lookup table | | | +-----------------------------------+ &0880 = QQ16_FLIGHT | | | MOS sound workspace | | | +-----------------------------------+ &0800 | | . . . . . .

Apart from these two differences, the docked and flight code share the same memory map.

## Elite code as an image

													 ----------------------

						To see just how big BBC Micro disc Elite is, we can convert the main game binary into an image, with one byte per pixel, and a greyscale showing each byte's value, with 0 being shown as black, 255 being shown as white, and interim values as greyscale pixels. The result is a 295-pixel square, like this (shown here at double size, so you can see the pixels more clearly):

![The game binary for BBC Micro disc Elite as an image](https://elite.bbcelite.com/images/disc/code.png) 

						This image contains the entire main game, including all ship data files and both the docked and flight code. Because of the duplication of code between the various files, it's actually one of the larger versions of Elite, in terms of code size.

## Codice Estratto

### Snippet Codice (BASIC)

```basic
+-----------------------------------+   &FFFF
  |                                   |
  | Machine Operating System (MOS)    |
  |                                   |
  +-----------------------------------+   &C000
  |                                   |
  | Paged ROMs                        |
  |                                   |
  +-----------------------------------+   &8000
  |                                   |
  | Missile blueprint (MISSILE.bin)   |
  |                                   |
  +-----------------------------------+   &7F00 = SHIP_MISSILE
  |                                   |
  | Memory for the split-screen mode  |
  |                                   |
  +-----------------------------------+   &6000
  |                                   |
  | &5F55-&5FFF unused when docked    |
  |                                   |
  +-----------------------------------+   &5F55
  |                                   |
  | Main game code (T.CODE)           |
  |                                   |
  +-----------------------------------+   &11E2 = S%
  |                                   |
  | Break handler for flight code     |
  |                                   |
  +-----------------------------------+   &11D5 = BRBR1
  |                                   |
  | Last saved commander file         |
  |                                   |
  +-----------------------------------+   &117C = S1%
  |                                   |
  | IRQ1 handler, mode 1 palette data |
  |                                   |
  +-----------------------------------+   &1100 = TVT1
  |                                   |
  | DFS general workspace             |
  |                                   |
  +-----------------------------------+   &1000
  |                                   |
  | WP workspace or disc catalogue    |
  |                                   |
  +-----------------------------------+   &0E00 = WP
  |                                   |
  | DFS general workspace             |
  |                                   |
  +-----------------------------------+   &0D9D
  |                                   |
  | CATD routine in DFS NMI workspace |
  |                                   |
  +-----------------------------------+   &0D7A = CATD
  |                                   |
  | DFS general workspace             |
  |                                   |
  +-----------------------------------+   &0D00 = LS%
  |                                   |
  | Ship line heap descends from LS%  |
  |                                   |
  +-----------------------------------+   SLSP
  |                                   |
  .                                   .
  .                                   .
  .                                   .
  .                                   .
  .                                   .
  |                                   |
  +-----------------------------------+   &0ABB when all ship slots are used
  |                                   |
  | Ship data blocks ascend from K%   |
  |                                   |
  +-----------------------------------+   &0900 = K%
  |                                   |
  | MOS sound/printer workspace       |
  |                                   |
  +-----------------------------------+   &0800
  |                                   |
  | Sine, cosine and arctan tables    |
  |                                   |
  +-----------------------------------+   &07C0 = SNE
  |                                   |
  | Recursive text tokens (WORDS.bin) |
  |                                   |
  +-----------------------------------+   &0400 = QQ18
  |                                   |
  | MOS keyboard input buffer         |
  |                                   |
  +-----------------------------------+   &03E0
  |                                   |
  | &03D0-&03DF unused                |
  |                                   |
  +-----------------------------------+   &03D0
  |                                   |
  | UP workspace                      |
  |                                   |
  +-----------------------------------+   &0300 = UP
  |                                   |
  | MOS general workspace             |
  |                                   |
  +-----------------------------------+   &0200
  |                                   |
  | 6502 stack descends from &01FF    |
  |                                   |
  +-----------------------------------+   &0194
  |                                   |
  | Heap space ascends from XX3       |
  |                                   |
  +-----------------------------------+   &0100 = XX3
  |                                   |
  | Zero page workspace               |
  |                                   |
  +-----------------------------------+   &0000 = ZP
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
.                                   .
  .                                   .
  .                                   .
  |                                   |
  +-----------------------------------+   &6000
  |                                   |
  | Ship blueprints file (D.MOA-MOP)  |
  |                                   |
  +-----------------------------------+   &5600 = XX21
  |                                   |
  | Main game code (D.CODE)           |
  |                                   |
  +-----------------------------------+   &11E2 = S%
  |                                   |
  .                                   .
  .                                   .
  .                                   .
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
.                                   .
  .                                   .
  .                                   .
  |                                   |
  +-----------------------------------+   &0900 = K%
  |                                   |
  | MOS sound workspace               |
  |                                   |
  +-----------------------------------+   &08C0
  |                                   |
  | Two-letter token lookup table     |
  |                                   |
  +-----------------------------------+   &0880 = QQ16_FLIGHT
  |                                   |
  | MOS sound workspace               |
  |                                   |
  +-----------------------------------+   &0800
  |                                   |
  .                                   .
  .                                   .
  .                                   .
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/the_elite_memory_map_disc.html](https://elite.bbcelite.com/deep_dives/the_elite_memory_map_disc.html)*

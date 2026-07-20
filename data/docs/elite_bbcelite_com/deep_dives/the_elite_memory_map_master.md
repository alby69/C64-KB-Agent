---
title: BBC Master Elite memory map
source_url: https://elite.bbcelite.com/deep_dives/the_elite_memory_map_master.html
category: source-code
topics:
- memory management
- assembly
- graphics
- basic
difficulty: intermediate
language: mixed
hardware:
- KERNAL
- SID
- CPU
- BASIC ROM
related:
- sid-registers
- sound-programming
- memory-map
- kernal-routines
- music-player
scraped_at: '2026-07-20'
---

# BBC Master Elite memory map

## Memory usage in the smoothest version of Elite

The main advantage of the BBC Master compared to the standard BBC Micro is extra memory, and given how tightly packed things are in standard Elite, it's a very welcome addition. The main benefit is that it allows the Master version to use the same mode 1/2 split screen as the 6502 Second Processor version, thus giving four colours in the space view and eight colours in the dashboard.

What the Master doesn't do, perhaps surprisingly, is use this extra memory to implement [flicker-free ship drawing](https://elite.bbcelite.com/flicker-free_ship_drawing.html). The Master certainly has much smoother ship animation, but there aren't any clever memory techniques in use here - the lack of flicker is down to an improvement in the ship-drawing algorithm rather than any shenanigans with bank-switching or swapping screen memory; even in a Master, there still isn't enough free memory to maintain two copies of the screen.

Let's take a quick look at the memory map first, and then we'll talk about how the Master can use its extra memory, and how it all fits into the memory map.

## BBC Master memory map

													 ---------------------

						The following setup gives us a generous memory footprint when compared to the BBC Micro, though the Master version of Elite still manages to fill most of it up. Here's the memory map of Elite on the BBC Master.

+-----------------------------------+ &FFFF | | | Machine Operating System (MOS) | | | +-----------------------------------+ &C000 | | | &B200-&BFFF unused | | | +-----------------------------------+ &B200 | | | Text tokens, sin/cos tables | | | +-----------------------------------+ &A000 =[QQ18](https://elite.bbcelite.com/master/game_data/variable/qq18.html)| | | &9D95-&9FFF unused | | | +-----------------------------------+ &9D95 | | | Ship blueprints (SHIPS.bin) | | | Shadow RAM +-----------------------------------+-- &8000 =[XX21](https://elite.bbcelite.com/master/game_data/variable/xx21.html)-------------------+ | | | | &7F48-&7FFF unused | | | | | +--------------------- &7F48 =[F%](https://elite.bbcelite.com/master/main/variable/f_per_cent.html)--+ &7E00-&7FFF unused | | | | | | | | | | | +-- &7E00 --------------------------+ | | | | | Screen memory | | | | | Main game code (BCODE.bin) +-- &4000 --------------------------+ | | | | | Zero page swap space | | | | | +-- &3000 --------------------------+ | | | | | | +-----------------------------------+ &1300 =[TVT3](https://elite.bbcelite.com/master/main/variable/tvt3.html)| | | &12AA-&12FF unused | | | +-----------------------------------+ &12AA | | | WP workspace | | | +-----------------------------------+ &0E41 =[WP](https://elite.bbcelite.com/master/main/workspace/wp.html)| | | &0E00-&0E40 unused | | | +-----------------------------------+ &0E00 | | | Sideways ROM and NMI workspace | | | +-----------------------------------+ &0D00 | | | Hangar ship line heap | | | +-----------------------------------+ &0B00 | | | &0900-&0AFF unused | | | +-----------------------------------+ &0900 | | | MOS sound/printer workspace | | | +-----------------------------------+ &0800 = LS% | | | Ship line heap descends from LS% | | | +-----------------------------------+ SLSP | | . . . . . . . . . . | | +-----------------------------------+ &05BB when all ship slots are used | | | Ship data blocks ascend from K% | | | +-----------------------------------+ &0400 =[K%](https://elite.bbcelite.com/master/main/workspace/k_per_cent.html)| | | MOS VDU and tape workspace | | | +-----------------------------------+ &0300 | | | MOS general workspace | | | +-----------------------------------+ &0200 | | | 6502 stack descends from &01FF | | | +-----------------------------------+ &0194 | | | Heap space ascends from XX3 | | | +-----------------------------------+ &0100 =[XX3](https://elite.bbcelite.com/master/main/workspace/xx3.html)| | | Zero page workspace | | | +-----------------------------------+ &0000 =[ZP](https://elite.bbcelite.com/master/main/workspace/zp.html)

On the left is the game code in main memory, while on the right are the various blocks of extra memory in the Master, so let's look at those in more detail.

## The Master's extra memory

													 -------------------------

						The Master's extra memory comes in three main chunks, and Elite uses all of them.

- First of all, sideways RAM bank 6 is switched into main memory at &8000 to &BFFF. In the BBC Micro, this address range always contains one of the paged ROMs (such as BASIC), but in the Master it's available as user RAM, so we can use it for storing the ship blueprints, text tokens and so on.
- Next up is shadow RAM, also known as LYNNE, which sits alongside the main memory. We can switch the memory block from &3000 to &7FFF between main memory and shadow RAM, and we can also set up LYNNE to host the screen memory, from &4000 to &7DFF. In this way screen memory doesn't steal RAM from the main memory, and we can just switch to shadow RAM to poke our graphics directly to the screen.
- Finally, the Master also supports an area of memory called HAZEL from &C000 to &DFFF, which can be used for the current filing system workspace. Filing system memory requirements are a real pain in the standard BBC Micro, where, for example, the disc filing system pushes the start of user memory (PAGE) from &0E00 to &1900. HAZEL fixes this problem and takes the extra load, leaving PAGE alone and freeing up a lot of extra memory for Elite.

Throughout the source code, you will see memory access being switched between shadow and main RAM. This is done by updating bits 1 and 2 of the Access Control Register at SHEILA &34. This switching aside, the rest of the extra memory just maps into the main memory space, and we can use it as normal.

## Zero page swap space

													 --------------------

						The main game code on the left of the memory map is fairly straightforward, but it's worth mentioning the zero page swap space in shadow RAM at &3000. This setup was inherited from the Commodore 64 and Apple II versions of Elite, on which the BBC Master version is based (see the [Commodore 64 Elite memory map](https://elite.bbcelite.com/the_elite_memory_map_commodore_64.html) for more details).

Whenever the game does any filing system work, such as cataloguing discs or saving commander files, it first swaps out the top part of zero page (&0090 to &00EF) with a copy that's been stored at the start of LYNNE. This part of zero page is used by the MOS to store various filing system variables, so this process effectively stores a "filing system-compatible" version of zero page in LYNNE, and swaps it in whenever we do any filing work. This enables the game to share this part of zero page with the operating system, but without corrupting the filing system.

## Elite code as an image

													 ----------------------

						To see just how big BBC Master Elite is, we can convert the main game binary into an image, with one byte per pixel, and a greyscale showing each byte's value, with 0 being shown as black, 255 being shown as white, and interim values as greyscale pixels. The result is a 213-pixel square, like this (shown here at double size, so you can see the pixels more clearly):

![The game binary for BBC Master Elite as an image](https://elite.bbcelite.com/images/master/code.png) 

						This image contains the entire main game, including all the game data.

## Codice Estratto

### Snippet Codice (BASIC)

```basic
+-----------------------------------+   &FFFF
  |                                   |
  | Machine Operating System (MOS)    |
  |                                   |
  +-----------------------------------+   &C000
  |                                   |
  | &B200-&BFFF unused                |
  |                                   |
  +-----------------------------------+   &B200
  |                                   |
  | Text tokens, sin/cos tables       |
  |                                   |
  +-----------------------------------+   &A000 = QQ18
  |                                   |
  | &9D95-&9FFF unused                |
  |                                   |
  +-----------------------------------+   &9D95
  |                                   |
  | Ship blueprints (SHIPS.bin)       |
  |                                   |                         Shadow RAM
  +-----------------------------------+-- &8000 = XX21 -------------------+
  |                                   |                                   |
  | &7F48-&7FFF unused                |                                   |
  |                                   |                                   |
  +--------------------- &7F48 = F% --+                &7E00-&7FFF unused |
  |                                   |                                   |
  |                                   |                                   |
  |                                   |                                   |
  |                                   +-- &7E00 --------------------------+
  |                                   |                                   |
  |                                   |                     Screen memory |
  |                                   |                                   |
  | Main game code (BCODE.bin)        +-- &4000 --------------------------+
  |                                   |                                   |
  |                                   |              Zero page swap space |
  |                                   |                                   |
  |                                   +-- &3000 --------------------------+
  |                                   |
  |                                   |
  |                                   |
  +-----------------------------------+   &1300 = TVT3
  |                                   |
  | &12AA-&12FF unused                |
  |                                   |
  +-----------------------------------+   &12AA
  |                                   |
  | WP workspace                      |
  |                                   |
  +-----------------------------------+   &0E41 = WP
  |                                   |
  | &0E00-&0E40 unused                |
  |                                   |
  +-----------------------------------+   &0E00
  |                                   |
  | Sideways ROM and NMI workspace    |
  |                                   |
  +-----------------------------------+   &0D00
  |                                   |
  | Hangar ship line heap             |
  |                                   |
  +-----------------------------------+   &0B00
  |                                   |
  | &0900-&0AFF unused                |
  |                                   |
  +-----------------------------------+   &0900
  |                                   |
  | MOS sound/printer workspace       |
  |                                   |
  +-----------------------------------+   &0800 = LS%
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
  +-----------------------------------+   &05BB when all ship slots are used
  |                                   |
  | Ship data blocks ascend from K%   |
  |                                   |
  +-----------------------------------+   &0400 = K%
  |                                   |
  | MOS VDU and tape workspace        |
  |                                   |
  +-----------------------------------+   &0300
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



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/the_elite_memory_map_master.html](https://elite.bbcelite.com/deep_dives/the_elite_memory_map_master.html)*

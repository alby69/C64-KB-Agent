---
title: Acorn Electron Elite memory map
source_url: https://elite.bbcelite.com/deep_dives/the_elite_memory_map_electron.html
category: deep-dive
topics:
- memory management
- assembly
- graphics
- basic
difficulty: intermediate
language: mixed
hardware:
- KERNAL
- CPU
- BASIC ROM
related:
- memory-map
- kernal-routines
scraped_at: '2026-07-20'
---

# Acorn Electron Elite memory map

## Memory usage in the smallest and most basic version of Elite

Memory might be tight in the [BBC Micro cassette version of Elite](https://elite.bbcelite.com/the_elite_memory_map.html), but things get really problematic in the Electron version. The Electron has the same 32K of user RAM as the BBC, but it's missing one vital feature that the BBC versions use to reduce screen memory, and which can't be implemented on the Electron.

The BBC versions reprogram the 6845 CRTC chip to create a [square screen mode](https://elite.bbcelite.com/drawing_monochrome_pixels_in_mode_4.html). This new mode is based on mode 4 (in the disc and cassette versions) or mode 1 (in the colour versions), but with a reduced width and height - it has 32 character columns and 31 character rows, compared to 40 columns and 32 rows in the standard mode 4/mode 1 screen. This custom screen mode is not only much easier to work with, as it's exactly 256 pixels wide, but is also takes up less memory than the standard mode 4: 2,304 bytes fewer, to be exact.
						

Unfortunately, the Electron doesn't contain a 6845 CRTC chip. Instead there is one huge custom ULA that controls the whole system - including the screen - and we can't reprogram this in the same way. This means we have to stick to standard mode 4 instead of the BBC's smaller screen mode, and somehow absorb the loss of 2,304 bytes compared to the already cramped [memory map of the BBC cassette version](https://elite.bbcelite.com/the_elite_memory_map.html).

## Electron memory map

													 -------------------

						This is why Electron Elite doesn't support suns, planet meridians or craters, Thargoids, Thargons or witchspace - the authors had to drop functionality to squeeze everything in. 2,304 bytes is around 10% of the game code, and even without these features, it's an incredibly tight fit.

Here's the memory map for Electron Elite.

+-----------------------------------+ &FFFF | | | Machine Operating System (MOS) | | | +-----------------------------------+ &C000 | | | Paged ROMs | | | +-----------------------------------+ &8000 | | | Memory for the mode 4 screen | | | +-----------------------------------+ &5800 | | | Ship blueprints (SHIPS.bin) | | | +-----------------------------------+ &4ED4 =[XX21](https://elite.bbcelite.com/electron/main/variable/xx21.html)| | | Main game code (ELITECO.bin) | | | +-----------------------------------+ &0D00 =[S%](https://elite.bbcelite.com/electron/main/workspace/s_per_cent_part_1_of_2.html)| | | &0CF3-&0CFF unused | | | +-----------------------------------+ &0CF3 | | | WP workspace | | | +-----------------------------------+ &0BE0 =[WP](https://elite.bbcelite.com/electron/main/workspace/wp.html)| | | Ship line heap descends from WP | | | +-----------------------------------+ SLSP | | . . . . . . . . . . | | +-----------------------------------+ &0AB0 when all ship slots are used | | | Ship data blocks ascend from K% | | | +-----------------------------------+ &0900 =[K%](https://elite.bbcelite.com/electron/main/workspace/k_per_cent.html)| | | MOS sound/printer workspace | | | +-----------------------------------+ &0800 | | | Recursive tokens (WORDS9.bin) | | | +-----------------------------------+ &0400 =[QQ18](https://elite.bbcelite.com/electron/main/variable/qq18.html)| | | MOS tape filing system workspace | | | +-----------------------------------+ &0380 | | | &036C-&037F unused | | | +-----------------------------------+ &036C | | | T% workspace | | | +-----------------------------------+ &0300 =[T%](https://elite.bbcelite.com/electron/main/workspace/t_per_cent.html)| | | MOS general workspace | | | +-----------------------------------+ &0200 | | | 6502 stack descends from &01FF | | | +-----------------------------------+ &0170 | | | Heap space ascends from XX3 | | | +-----------------------------------+ &0100 =[XX3](https://elite.bbcelite.com/electron/main/workspace/xx3.html)| | | Zero page workspace | | | +-----------------------------------+ &0000 =[ZP](https://elite.bbcelite.com/electron/main/workspace/zp.html)

Apart from the 13 unused bytes from &0CF3 to &0CFF, every location is used. That said, the Electron version does still contain the same unused multiplication routines as the BBC Micro (a duplicate of MULTU and the unused MUT3 routine), so there are at least 28 unused bytes that could be reused... and on top of that, the authors left the ARCTAN routine (70 bytes) and ACT table (32 bytes) intact, even though they are only ever used to draw meridians and equators on planets, a feature that isn't present in the Electron version. In terms of the game binary that was released, though, it's even more of a squeeze than in the BBC version. In this version, more than any other, every byte counts.

## Elite code as an image

													 ----------------------

						To see just how small the Acorn Electron version of Elite is, we can convert the main game binary into an image, with one byte per pixel, and a greyscale showing each byte's value, with 0 being shown as black, 255 being shown as white, and interim values as greyscale pixels. The result is a 156-pixel square, like this (shown here at double size, so you can see the pixels more clearly):

![The game binary for Acorn Electron Elite as an image](https://elite.bbcelite.com/images/electron/code.png) 

						This image contains the entire main game. This is the smallest Elite of them all - it doesn't get more compact than this.

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
  | Memory for the mode 4 screen      |
  |                                   |
  +-----------------------------------+   &5800
  |                                   |
  | Ship blueprints (SHIPS.bin)       |
  |                                   |
  +-----------------------------------+   &4ED4 = XX21
  |                                   |
  | Main game code (ELITECO.bin)      |
  |                                   |
  +-----------------------------------+   &0D00 = S%
  |                                   |
  | &0CF3-&0CFF unused                |
  |                                   |
  +-----------------------------------+   &0CF3
  |                                   |
  | WP workspace                      |
  |                                   |
  +-----------------------------------+   &0BE0 = WP
  |                                   |
  | Ship line heap descends from WP   |
  |                                   |
  +-----------------------------------+   SLSP
  |                                   |
  .                                   .
  .                                   .
  .                                   .
  .                                   .
  .                                   .
  |                                   |
  +-----------------------------------+   &0AB0 when all ship slots are used
  |                                   |
  | Ship data blocks ascend from K%   |
  |                                   |
  +-----------------------------------+   &0900 = K%
  |                                   |
  | MOS sound/printer workspace       |
  |                                   |
  +-----------------------------------+   &0800
  |                                   |
  | Recursive tokens (WORDS9.bin)     |
  |                                   |
  +-----------------------------------+   &0400 = QQ18
  |                                   |
  | MOS tape filing system workspace  |
  |                                   |
  +-----------------------------------+   &0380
  |                                   |
  | &036C-&037F unused                |
  |                                   |
  +-----------------------------------+   &036C
  |                                   |
  | T% workspace                      |
  |                                   |
  +-----------------------------------+   &0300 = T%
  |                                   |
  | MOS general workspace             |
  |                                   |
  +-----------------------------------+   &0200
  |                                   |
  | 6502 stack descends from &01FF    |
  |                                   |
  +-----------------------------------+   &0170
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
*Fonte originale: [https://elite.bbcelite.com/deep_dives/the_elite_memory_map_electron.html](https://elite.bbcelite.com/deep_dives/the_elite_memory_map_electron.html)*

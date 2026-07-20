---
title: Apple II Elite memory map
source_url: https://elite.bbcelite.com/deep_dives/the_elite_memory_map_apple_ii.html
category: deep-dive
topics:
- memory management
- basic
- graphics
- assembly
- sprite programming
difficulty: intermediate
language: mixed
hardware:
- CIA
- SID
- CPU
- VIC-II
- KERNAL
- BASIC ROM
related:
- sid-registers
- sound-programming
- vic-ii-registers
- joystick-reading
- keyboard-handling
- kernal-routines
- memory-map
- music-player
- sprite-programming
- raster-interrupts
- cia-registers
scraped_at: '2026-07-20'
---

# Apple II Elite memory map

## Memory usage in the Apple II version of Elite

On its launch in 1977, the most powerful version of the Apple II came with a whopping 48K of RAM, and Elite needs almost all of it. Once the game is loaded, there are only 422 spare bytes in the entire machine, spread out between four small pockets of free space.

This is not that surprising, as the Apple version is a development of the Commodore 64 version, which itself takes up most of that machine's generous 64K of RAM. Gone are the music and sprites of the Commodore version, and the Trumbles mission and Cougar ship blueprint are also axed, but those features aside, Apple Elite manages to pack everything into memory at once.

Let's see how it does it.

## Apple II memory map

													 -------------------

						Here's the memory map of a 48K Apple II when Elite is loaded and running:

+-----------------------------------+ $FFFF | | | Standard system monitor ROM space | | | +-----------------------------------+ $F800 | | | Applesoft ROM space | | | +-----------------------------------+ $D000 | | | Peripheral and firmware ROM space | | | +-----------------------------------+ $C100 | | | I/O memory | | | +-----------------------------------+ $C000 | | | $BF8E-$BFFF unused | | | +-----------------------------------+ $BF8E | | | Ship blueprints (SHIPS.bin) | | | +-----------------------------------+ $A300 =[XX21](https://elite.bbcelite.com/apple/game_data/variable/xx21.html)| | | $A2FB-$A2FF unused | | | +-----------------------------------+ $A2FB =[F%](https://elite.bbcelite.com/apple/main/variable/f_per_cent.html)| | | Main game code | | | +-----------------------------------+ $4000 =[ENTRY](https://elite.bbcelite.com/apple/main/subroutine/entry.html)| | | High-resolution screen (page 1) | | | +-----------------------------------+ $2000 =[SCBASE](https://elite.bbcelite.com/apple/all/workspaces.html#scbase)| | | $1FA0-$1FFF unused | | | +-----------------------------------+ $1FA0 | | | Text tokens, sin/cos tables | | | +-----------------------------------+ $0B60 =[QQ18](https://elite.bbcelite.com/apple/game_data/variable/qq18.html)| | | Ship line heap descends from LS% | | | +-----------------------------------+ SLSP | | . . . . . . . . . +-- $0A6D --------------------------+ . | | . | Disk routine variables | . | | . +-- $0A5E =[track](https://elite.bbcelite.com/apple/main/workspace/disk_operations_workspace.html#track)------------------+ . | | . | | | | Disk 6-bit nibble buffer | +-------------------------- $0927 --+ | | | | | +-- $0900 =[buffr2](https://elite.bbcelite.com/apple/main/workspace/disk_operations_workspace.html#buffr2)-----------------+ | Ship data blocks ascend from K% | | | | Disk sector buffer | | | | +-----------------------------[K%](https://elite.bbcelite.com/master/main/workspace/k_per_cent.html)--+-- $0800 =[buffer](https://elite.bbcelite.com/apple/main/workspace/disk_operations_workspace.html#buffer)-----------------+ | | | | | | | Text screen (page 1) +-- $0716 --------------------------+ | | | | | WP workspace | | | | +-----------------------------------+-- $0400 =[WP](https://elite.bbcelite.com/apple/main/workspace/wp.html)---------------------+ | | | Applesoft and DOS vectors | | | +-----------------------------------+ $03D0 | | | $0301-$03CF unused | | | +-----------------------------------+ $0301 | | | UP workspace | | | +-----------------------------------+ $0200 =[UP](https://elite.bbcelite.com/apple/main/workspace/up.html)| | | 6502 stack descends from $01FF | | | +-----------------------------------+ &0194 | | | Heap space ascends from XX3 | | | +-----------------------------------+ $0100 =[XX3](https://elite.bbcelite.com/apple/main/workspace/xx3.html)| | | Zero page workspace | | | +-----------------------------------+ $0000 =[ZP](https://elite.bbcelite.com/apple/main/workspace/zp.html)

One of the most interesting aspects of the Apple II version of Elite is that it includes its own low-level disk access routines. To enable the game to load and save commander files without giving away all the memory required by the official version of Apple DOS, the game includes its own copy of the RWTS (Read Write Track Sector) routines, taken from Apple DOS 3.3 and modified to include only the features that are required. These routines use the same memory as the ship heap at K% for the disk buffers, which works because we don't need to access the disk while flying.

Similarly, the WP workspace is designed so it only contains graphics-related variables, such as the stardust coordinates, the ball line heap and the sun line heap. This means it can share memory with the text screen memory, as we are either showing the text screen or the graphics screen, but never both at the same time.

## Elite code as an image

													 ----------------------

						To see just how big Appple II Elite is, we can convert the main game binary into an image, with one byte per pixel, and a greyscale showing each byte's value, with 0 being shown as black, 255 being shown as white, and interim values as greyscale pixels. The result is a 196-pixel square, like this (shown here at double size, so you can see the pixels more clearly):

![The game binary for Apple II Elite as an image](https://elite.bbcelite.com/images/apple/code.png) 

						This image contains the entire main game.

## Codice Estratto

### Snippet Codice (BASIC)

```basic
+-----------------------------------+   $FFFF
  |                                   |
  | Standard system monitor ROM space |
  |                                   |
  +-----------------------------------+   $F800
  |                                   |
  | Applesoft ROM space               |
  |                                   |
  +-----------------------------------+   $D000
  |                                   |
  | Peripheral and firmware ROM space |
  |                                   |
  +-----------------------------------+   $C100
  |                                   |
  | I/O memory                        |
  |                                   |
  +-----------------------------------+   $C000
  |                                   |
  | $BF8E-$BFFF unused                |
  |                                   |
  +-----------------------------------+   $BF8E
  |                                   |
  | Ship blueprints (SHIPS.bin)       |
  |                                   |
  +-----------------------------------+   $A300 = XX21
  |                                   |
  | $A2FB-$A2FF unused                | 
  |                                   |
  +-----------------------------------+   $A2FB = F%
  |                                   |
  | Main game code                    |
  |                                   |
  +-----------------------------------+   $4000 = ENTRY
  |                                   |
  | High-resolution screen (page 1)   |
  |                                   |
  +-----------------------------------+   $2000 = SCBASE
  |                                   |
  | $1FA0-$1FFF unused                | 
  |                                   |
  +-----------------------------------+   $1FA0
  |                                   |
  | Text tokens, sin/cos tables       |
  |                                   |
  +-----------------------------------+   $0B60 = QQ18
  |                                   |
  | Ship line heap descends from LS%  |
  |                                   |
  +-----------------------------------+   SLSP
  |                                   |
  .                                   .
  .                                   .
  .                                   .
  .                                   .
  .                                   +-- $0A6D --------------------------+
  .                                   |                                   |
  .                                   |            Disk routine variables |
  .                                   |                                   |
  .                                   +-- $0A5E = track ------------------+
  .                                   |                                   |
  .                                   |                                   |
  |                                   |          Disk 6-bit nibble buffer |
  +-------------------------- $0927 --+                                   |
  |                                   |                                   |
  |                                   +-- $0900 = buffr2 -----------------+
  | Ship data blocks ascend from K%   |                                   |
  |                                   |                Disk sector buffer |
  |                                   |                                   |
  +----------------------------- K% --+-- $0800 = buffer -----------------+
  |                                   |
  |                                   |
  |                                   |
  | Text screen (page 1)              +-- $0716 --------------------------+
  |                                   |                                   |
  |                                   |                      WP workspace |
  |                                   |                                   |
  +-----------------------------------+-- $0400 = WP ---------------------+
  |                                   |
  | Applesoft and DOS vectors         |
  |                                   |
  +-----------------------------------+   $03D0
  |                                   |
  | $0301-$03CF unused                |
  |                                   |
  +-----------------------------------+   $0301
  |                                   |
  | UP workspace                      |
  |                                   |
  +-----------------------------------+   $0200 = UP
  |                                   |
  | 6502 stack descends from $01FF    |
  |                                   |
  +-----------------------------------+   &0194
  |                                   |
  | Heap space ascends from XX3       |
  |                                   |
  +-----------------------------------+   $0100 = XX3
  |                                   |
  | Zero page workspace               |
  |                                   |
  +-----------------------------------+   $0000 = ZP
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/the_elite_memory_map_apple_ii.html](https://elite.bbcelite.com/deep_dives/the_elite_memory_map_apple_ii.html)*

---
title: Commodore 64 Elite memory map
source_url: https://elite.bbcelite.com/deep_dives/the_elite_memory_map_commodore_64.html
category: deep-dive
topics:
- sprite programming
- basic
- raster interrupts
- assembly
- graphics
- memory management
- input handling
difficulty: advanced
language: mixed
hardware:
- BASIC ROM
- VIC-II
- CIA
- SID
- CPU
- KERNAL
related:
- cia-registers
- keyboard-handling
- sound-programming
- music-player
- raster-interrupts
- joystick-reading
- memory-map
- sprite-programming
- vic-ii-registers
- kernal-routines
- sid-registers
scraped_at: '2026-07-14'
---


# Commodore 64 Elite memory map

## Memory usage in the musical version of Elite

For those of us more used to the unexpanded BBC Micro, the Commodore 64 comes as a bit of a shock. That "64" in the name? Turns out it ain't kidding.

Both the 6502 CPU in the BBC Micro and the almost-identical 6510 CPU in the Commodore 64 can address a maximum of 64K of memory. When Elite is loaded into the BBC Micro, just over half of that 64K is taken up by the operating system ROM, the language ROM and various essential OS workspaces. The main game code, workspaces and screen memory are squished into the remainder, which comes to a modest 31.3K; see the [BBC Micro cassette Elite memory map](https://elite.bbcelite.com/the_elite_memory_map.html) for details.

The Commodore 64 is a very different beast, and Elite unbuckles its belt and lets it all hang out, taking advantage of pretty much all the extra memory in Commodore's behemoth. Let's take a look at how Elite manages to fill even the Commodore 64, practically to the brim.

## Commodore 64 memory map

													 -----------------------

						Here's the memory map of Elite when it is loaded and running on the Commodore 64. On the left is the 64K of main memory RAM, while on the right are the Kernal ROM and I/O memory, which can be paged into the memory map when needed (see below for more on this).

+-----------------------------------+-- $FFFF --------------------------+ | | | | 6510 interrupt and reset vectors | | | | | +-------------------- $FFC0 = LS% --+ | | | | | Ship line heap descends from LS% | | | | | +--------------------------- SLSP --+ | | | | . . | . . | . . | . . | . . | +-------------------------- $FA72 --+ | | | | | Ship data blocks ascend from K% | | | | | +--------------------- $F900 =[K%](https://elite.bbcelite.com/c64/main/workspace/k_per_cent.html)--+ Kernal ROM | | | | | $F850-$F8FF unused | | | | | +-------------------------- $F850 --+ | | | | | Copy of dashboard bitmap | | | | | +---------------- $EF90 =[DSTORE%](https://elite.bbcelite.com/c64/all/workspaces.html#dstore-per-cent)--+ | | | | | $EF8D-$EF8F unused | | | | | +-------------------------- $EF8D --+ | | | | | | | | | | | | | | | | | | | | | | | +-- $E000 --------------------------+ | | | | Ship blueprints (SHIPS.bin) | I/O memory | | | | | | VIC-II $D000-$D02E | | | SID $D400-$D41C | | | Colour RAM $D800-$DBE7 | | | CIA1 $DC00-$DC0F | | | CIA2 $DD00-$DD0F | | | I/O 1 $DE00-$DEFF | | | I/O 2 $DF00-$DFFF | | | | +------------------- $D000 =[XX21](https://elite.bbcelite.com/c64/game_data/variable/xx21.html)--+-- $D000 --------------------------+ | | | Commander file staging area | | | +-----------------------------------+ $CF00 =[TAP%](https://elite.bbcelite.com/c64/all/workspaces.html#tap-per-cent)| | | Zero page swap space | | | +-----------------------------------+ $CE00 | | | $CCD7-$CDFF unused | | | +-----------------------------------+ $CCD7 =[F%](https://elite.bbcelite.com/c64/main/variable/f_per_cent.html)| | | Title music (C.THEME.bin) | | | +-----------------------------------+ $C164 =[THEME](https://elite.bbcelite.com/c64/main/variable/comudat.html#theme)| | | Blue Danube music (C.COMUDAT.bin) | | | +-----------------------------------+ $B72D =[COMUDAT](https://elite.bbcelite.com/c64/main/variable/comudat.html)| | | Main game code 2/2 (HICODE.bin) | | | +-----------------------------------+ $6A00 =[tnpr1](https://elite.bbcelite.com/c64/main/subroutine/tnpr1.html)| | | Sprite definitions (8 x 64 bytes) | | | +-----------------------------------+ $6800 =[SPRITELOC%](https://elite.bbcelite.com/c64/all/workspaces.html#dstore-per-cent)| | | Screen RAM for space view (1K) | | | +-----------------------------------+ $6400 | | | Screen RAM for text view (1K) | | | +-----------------------------------+ $6000 | | | Screen bitmap (8K) | | | +-----------------------------------+ $4000 =[SCBASE](https://elite.bbcelite.com/c64/all/workspaces.html#scbase)| | | $3ED2-$3FFF unused | | | +-----------------------------------+ $3ED2 =[R%](https://elite.bbcelite.com/c64/main/variable/r_per_cent.html)| | | Main game code 1/2 (LOCODE.bin) | | | +-----------------------------------+ $1D00 =[Option variables](https://elite.bbcelite.com/c64/main/workspace/option_variables.html)| | | $1CCC-$1CFF unused | | | +-----------------------------------+ $1CCC | | | Extended text tokens | | | +-----------------------------------+ $0E00 =[TKN1](https://elite.bbcelite.com/c64/game_data/variable/tkn1.html)| | | Game font | | | +-----------------------------------+ $0B00 =[FONT](https://elite.bbcelite.com/c64/all/workspaces.html#font)| | | Text tokens, sin/cos/tan tables | | | +-----------------------------------+ $0700 =[QQ18](https://elite.bbcelite.com/c64/game_data/variable/qq18.html)| | | $06FC-$06FF unused | | | +-----------------------------------+ $06FC | | | WP workspace | | | +-----------------------------------+ $0580 =[WP](https://elite.bbcelite.com/c64/main/workspace/wp.html)| | | $0541-$057F unused | | | +-----------------------------------+ $0541 | | | UP workspace | | | +-----------------------------------+ $0400 =[UP](https://elite.bbcelite.com/c64/main/workspace/up.html)| | | Kernal workspace | | | +-----------------------------------+ $0200 | | | 6502 stack descends from $01FF | | | +-----------------------------------+ &0194 | | | Heap space ascends from XX3 | | | +-----------------------------------+ $0100 =[XX3](https://elite.bbcelite.com/c64/main/workspace/xx3.html)| | | Zero page workspace | | | +-----------------------------------+ $0002 =[RAND](https://elite.bbcelite.com/c64/main/workspace/zp.html#rand)| | | 6510 port registers | | | +-----------------------------------+ $0000 =[ZP](https://elite.bbcelite.com/c64/main/workspace/zp.html)

So the game code lives in the 64K of main RAM, where it takes up almost all of the available memory. There are a few gaps, but they aren't very big; if you add up all the areas marked as "unused" in the above map, then the spare memory comes to just 897 bytes, or 1.4% of the total 64K of RAM, leaving a full 98.6% of memory in use.

Elite can do this because the Commodore 64's 6510 CPU lets you configure the memory layout in a way that simply isn't possible on the standard BBC Micro, and if you want to, you can page out pretty much everything that isn't RAM, from the BASIC ROM to the Kernal, leaving almost all of the 64K of memory for your own programs.

The Kernal operating system reserves 512 bytes from $0200 to $03FF and a number of locations in zero page; there are the two port registers at $0000 and $0001 that let you reconfigure memory; and the 6510 keeps its reset and interrupt vectors at $FFFA-$FFFF, just like the 6502... and that's about it. The rest of the 64K memory space can be mapped to RAM that is available to the user.

The memory layout can be changed by writing to the 6510 port register in location $0001. The bottom three bits of this register control three settings known as LORAM, HIRAM and CHAREN, and the combination of these three bits lets us pick from a whole range of memory layouts, as described in the Programmer's Reference Guide from pages 260 to 267.

Out of all of the possible configurations, Elite only uses three memory layouts:

- Set the entire 64K memory map to RAM:
								- LORAM = 0
- HIRAM = 0
- CHAREN = 1
 
- Map in both I/O memory and the Kernal ROM:
								- LORAM = 0
- HIRAM = 1
- CHAREN = 1
 [KERNALSETUP](https://elite.bbcelite.com/c64/main/subroutine/kernalsetup.html)routine, which is called when we need to use the operating system's Kernal functions to load or save commander files.
- Map in I/O memory:
								- LORAM = 1
- HIRAM = 0
- CHAREN = 1
 

In the main game code, memory reconfiguration is done by calling the [SETL1](https://elite.bbcelite.com/c64/main/subroutine/setl1.html) routine, though the loaders and [main interrupt routine](https://elite.bbcelite.com/c64/main/subroutine/comirq1.html) poke $0001 directly.

## Zero page swap space

													 --------------------

						The main game code on the left of the memory map is fairly straightforward, but it's worth mentioning the zero page swap space at $CE00. Whenever the game does any filing system work, such as saving commander files, it first swaps out zero page ($0002 to $00FF) with a copy at $CE00.

This swapping process effectively stores a "Kernal function-compatible" version of zero page at $CE00, which is set up by the disk loader via the [CopyZeroPage](https://elite.bbcelite.com/c64/disk_loader_2/subroutine/copyzeropage.html) routine. The game then swaps in this copy of zero page whenever it needs to do any file operations with the Kernal functions; this is done by calling the [SWAPPZERO](https://elite.bbcelite.com/c64/main/subroutine/swappzero.html) routine before and after each filing system-related Kernal function call.

This enables the game to share zero page with the Kernal, but without clashing and corrupting either the game's zero page variables or the Kernal's zero page variables. The same approach is used in the Apple II and BBC Master versions, but the Commodore 64 version was the first to use it.

## Elite code as an image

													 ----------------------

						To see just how big Commodore 64 Elite is, we can convert the main game binary into an image, with one byte per pixel, and a greyscale showing each byte's value, with 0 being shown as black, 255 being shown as white, and interim values as greyscale pixels. The result is a 229-pixel square, like this (shown here at double size, so you can see the pixels more clearly):

![The game binary for Commodore 64 Elite as an image](https://elite.bbcelite.com/images/c64/code.png) 

						This image contains the entire main game, including all the music and sprites.

## Codice Estratto

### Snippet Codice (BASIC)

```basic
+-----------------------------------+-- $FFFF --------------------------+
  |                                   |                                   |
  | 6510 interrupt and reset vectors  |                                   |
  |                                   |                                   |
  +-------------------- $FFC0 = LS% --+                                   |
  |                                   |                                   |
  | Ship line heap descends from LS%  |                                   |
  |                                   |                                   |
  +--------------------------- SLSP --+                                   |
  |                                   |                                   |
  .                                   .                                   |
  .                                   .                                   |
  .                                   .                                   |
  .                                   .                                   |
  .                                   .                                   |
  +-------------------------- $FA72 --+                                   |
  |                                   |                                   |
  | Ship data blocks ascend from K%   |                                   |
  |                                   |                                   |
  +--------------------- $F900 = K% --+                        Kernal ROM |
  |                                   |                                   |
  | $F850-$F8FF unused                |                                   |
  |                                   |                                   |
  +-------------------------- $F850 --+                                   |
  |                                   |                                   |
  | Copy of dashboard bitmap          |                                   |
  |                                   |                                   |
  +---------------- $EF90 = DSTORE% --+                                   |
  |                                   |                                   |
  | $EF8D-$EF8F unused                |                                   |
  |                                   |                                   |
  +-------------------------- $EF8D --+                                   |
  |                                   |                                   |
  |                                   |                                   |
  |                                   |                                   |
  |                                   |                                   |
  |                                   |                                   |
  |                                   |                                   |
  |                                   |                                   |
  |                                   +-- $E000 --------------------------+
  |                                   |                                   |
  | Ship blueprints (SHIPS.bin)       |                        I/O memory |
  |                                   |                                   |
  |                                   |                VIC-II $D000-$D02E |
  |                                   |                   SID $D400-$D41C |
  |                                   |            Colour RAM $D800-$DBE7 |
  |                                   |                  CIA1 $DC00-$DC0F |
  |                                   |                  CIA2 $DD00-$DD0F |
  |                                   |                 I/O 1 $DE00-$DEFF |
  |                                   |                 I/O 2 $DF00-$DFFF |
  |                                   |                                   |
  +------------------- $D000 = XX21 --+-- $D000 --------------------------+
  |                                   |
  | Commander file staging area       |
  |                                   |
  +-----------------------------------+   $CF00 = TAP%
  |                                   |
  | Zero page swap space              |
  |                                   |
  +-----------------------------------+   $CE00
  |                                   |
  | $CCD7-$CDFF unused                |
  |                                   |
  +-----------------------------------+   $CCD7 = F%
  |                                   |
  | Title music (C.THEME.bin)         |
  |                                   |
  +-----------------------------------+   $C164 = THEME
  |                                   |
  | Blue Danube music (C.COMUDAT.bin) |
  |                                   |
  +-----------------------------------+   $B72D = COMUDAT
  |                                   |
  | Main game code 2/2 (HICODE.bin)   |
  |                                   |
  +-----------------------------------+   $6A00 = tnpr1
  |                                   |
  | Sprite definitions (8 x 64 bytes) |
  |                                   |
  +-----------------------------------+   $6800 = SPRITELOC%
  |                                   |
  | Screen RAM for space view (1K)    |
  |                                   |
  +-----------------------------------+   $6400
  |                                   |
  | Screen RAM for text view (1K)     |
  |                                   |
  +-----------------------------------+   $6000
  |                                   |
  | Screen bitmap (8K)                |
  |                                   |
  +-----------------------------------+   $4000 = SCBASE
  |                                   |
  | $3ED2-$3FFF unused                |
  |                                   |
  +-----------------------------------+   $3ED2 = R%
  |                                   |
  | Main game code 1/2 (LOCODE.bin)   |
  |                                   |
  +-----------------------------------+   $1D00 = Option variables
  |                                   |
  | $1CCC-$1CFF unused                |
  |                                   |
  +-----------------------------------+   $1CCC
  |                                   |
  | Extended text tokens              |
  |                                   |
  +-----------------------------------+   $0E00 = TKN1
  |                                   |
  | Game font                         |
  |                                   |
  +-----------------------------------+   $0B00 = FONT
  |                                   |
  | Text tokens, sin/cos/tan tables   |
  |                                   |
  +-----------------------------------+   $0700 = QQ18
  |                                   |
  | $06FC-$06FF unused                |
  |                                   |
  +-----------------------------------+   $06FC
  |                                   |
  | WP workspace                      |
  |                                   |
  +-----------------------------------+   $0580 = WP
  |                                   |
  | $0541-$057F unused                |
  |                                   |
  +-----------------------------------+   $0541
  |                                   |
  | UP workspace                      |
  |                                   |
  +-----------------------------------+   $0400 = UP
  |                                   |
  | Kernal workspace                  |
  |                                   |
  +-----------------------------------+   $0200
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
  +-----------------------------------+   $0002 = RAND
  |                                   |
  | 6510 port registers               |
  |                                   |
  +-----------------------------------+   $0000 = ZP
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/the_elite_memory_map_commodore_64.html](https://elite.bbcelite.com/deep_dives/the_elite_memory_map_commodore_64.html)*


### Collegamenti e Riferimenti Hardware
- **$DC00 (CIA 1 Port A (Joystick 2, Keyboard))**: Associato al chip CIA. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#dc00).

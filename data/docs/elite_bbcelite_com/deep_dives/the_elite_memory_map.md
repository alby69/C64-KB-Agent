---
title: BBC Micro cassette Elite memory map
source_url: https://elite.bbcelite.com/deep_dives/the_elite_memory_map.html
category: source-code
topics:
- sound generation
- basic
- assembly
- memory management
- graphics
difficulty: intermediate
language: mixed
hardware:
- BASIC ROM
- CIA
- SID
- CPU
- KERNAL
related:
- keyboard-handling
- music-player
- sound-programming
- joystick-reading
- memory-map
- kernal-routines
- sid-registers
- cia-registers
scraped_at: '2026-07-14'
---

# BBC Micro cassette Elite memory map

## Memory usage in the classic version of Elite, where space is really tight

The cassette version of BBC Micro Elite uses almost every nook and cranny of the BBC Micro Model B, which isn't surprising when you consider just how much the authors managed to squeeze into this 32K micro. Sure, the BBC Micro disc version of the game has more features, but that's because the main game code is split into two different programs, one that's loaded when you're docked and another that's loaded for spaceflight. The cassette version that's documented here doesn't have the luxury of fast loading - quite the opposite, in fact - so it has to cram the whole game into memory, all at once. It's an absolute marvel of efficiency.

When the cassette version of Elite is loaded, this is how the memory map of the BBC Micro Model B looks.

+-----------------------------------+ &FFFF | | | Machine Operating System (MOS) | | | +-----------------------------------+ &C000 | | | Paged ROMs | | | +-----------------------------------+ &8000 | | | Python blueprint (PYTHON.bin) | | | +-----------------------------------+ &7F00 =[SHIP_PYTHON](https://elite.bbcelite.com/cassette/main/variable/ship_python.html)| | | Memory for the split-screen mode | | | +-----------------------------------+ &6000 | | | Ship blueprints (SHIPS.bin) | | | +-----------------------------------+ &563A =[XX21](https://elite.bbcelite.com/cassette/main/variable/xx21.html)| | | Main game code (ELTcode.bin) | | | +-----------------------------------+ &0F40 =[S%](https://elite.bbcelite.com/cassette/main/workspace/s_per_cent.html)| | | &0F34-&0F3F unused | | | +-----------------------------------+ &0F34 | | | WP workspace | | | +-----------------------------------+ &0D40 =[WP](https://elite.bbcelite.com/cassette/main/workspace/wp.html)| | | Ship line heap descends from WP | | | +-----------------------------------+ SLSP | | . . . . . . . . . . | | +-----------------------------------+ &0AB0 when all ship slots are used | | | Ship data blocks ascend from K% | | | +-----------------------------------+ &0900 =[K%](https://elite.bbcelite.com/cassette/main/workspace/k_per_cent.html)| | | MOS sound envelope buffer | | | +-----------------------------------+ &08C0 | | | MOS printer buffer | | | +-----------------------------------+ &0880 | | | MOS sound workspace and buffer | | | +-----------------------------------+ &0800 | | | Recursive tokens (WORDS9.bin) | | | +-----------------------------------+ &0400 =[QQ18](https://elite.bbcelite.com/cassette/main/variable/qq18.html)| | | MOS tape filing system workspace | | | +-----------------------------------+ &0380 | | | &0372-&037F unused | | | +-----------------------------------+ &0372 | | | T% workspace | | | +-----------------------------------+ &0300 =[T%](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html)| | | MOS general workspace | | | +-----------------------------------+ &0200 | | | 6502 stack descends from &01FF | | | +-----------------------------------+ &0170 | | | Heap space ascends from XX3 | | | +-----------------------------------+ &0100 =[XX3](https://elite.bbcelite.com/cassette/main/workspace/xx3.html)| | | Zero page workspace | | | +-----------------------------------+ &0000 =[ZP](https://elite.bbcelite.com/cassette/main/workspace/zp.html)

This memory map shows the full 64K of addressable memory that's supported by the BBC's 6502 processor, but only the bottom 32K is writable RAM, and hence usable by Elite. The top 16K is mapped to the MOS (Machine Operating System) ROM, and the next 16K is mapped to the currently selected paged ROM, which might be anything from BBC BASIC to the VIEW word processor.

This 32K of RAM includes both screen memory and the various operating system workspaces, which can leave a pretty small amount for programs (especially in high resolution screen modes). Let's take a look at how the authors managed to shoehorn their game into such a small amount of memory.

## Memory usage

													 ------------

						Here's a full breakdown of memory usage in bytes, once the cassette version of Elite is loaded and running. The figures show the number of available bytes in each section and how many of those are unused:

| Memory contents (ROMs) | Address range | Bytes | Unused | 
|---|---|---|---|
| Paged ROMs | &8000 to &BFFF | 16,384 | - | 
| Machine operating system (MOS) ROM | &C000 to &FFFF | 16,384 | - | 
| Total ROM memory | 32,768 | - | 

| Memory contents (MOS workspace) | Address range | Bytes | Unused | 
|---|---|---|---|
| MOS zero page filing system workspace | &00B0 to &00CF | 32 | - | 
| MOS zero page VDU status byte | &00D0 | 1 | - | 
| MOS zero page tape filing system workspace | &00E2 to &00E3 | 2 | - | 
| MOS zero page general workspace | &00E4 to &00FF | 28 | - | 
| MOS general workspace | &0200 to &02FF | 256 | - | 
| MOS tape filing system workspace | &0380 to &03DF | 96 | - | 
| MOS keyboard buffer | &03E0 to &03FF | 32 | - | 
| MOS sound workspace and buffer | &0800 to &087F | 128 | - | 
| MOS printer buffer | &0880 to &08BF | 64 | 64 | 
| MOS envelope buffer | &08C0 to &08FF | 64 | - | 
| Total MOS workspace memory | 703 | 64 | 

| Memory contents (shared memory) | Address range | Bytes | Unused | 
|---|---|---|---|
| 6502 stack | &0170 to &01FF | 144 | - | 
| Memory for the custom screen mode | &6000 to &7EFF | 7,936 | - | 
| Total shared memory | 8,080 | - | 

| Memory contents (game code) | Address range | Bytes | Unused | 
|---|---|---|---|
| Main game code | &0F40 to &5639 | 18,170 | 34 | 
| Ship blueprints (except Python) | &563A to &5FFF | 2,502 | - | 
| QQ18 (game text) | &0400 to &07FF | 1,024 | 1 | 
| Python ship blueprint, SVN, VEC | &7F00 to &7FFF | 256 | 11 | 
| Total game code memory | 21,952 | 46 | 

| Memory contents (workspaces) | Address range | Bytes | Unused | 
|---|---|---|---|
| Zero page workspace 1 | &0000 to &00AF | 176 | 1 | 
| Zero page workspace 2 | &00D1 to &00E1 | 17 | - | 
| XX3 (temporary heap) | &0100 to &016F | 112 | - | 
| K% (ship data blocks, line heaps) | &0900 to &0D3F | 1,088 | - | 
| WP (ship slots, variables) | &0D40 to &0F33 | 500 | 1 | 
| Unused space after WP | &0F34 to &0F3F | 12 | 12 | 
| T% (commander data, stardust data) | &0300 to &0371 | 114 | 6 | 
| Unused space after T% | &0372 to &037F | 14 | 14 | 
| Total workspace memory | 2,033 | 34 | 

| Summary | Bytes | Unused | |
|---|---|---|---|
| Total ROM memory | 32,768 | - | |
| Total MOS workspace memory | 703 | 64 | |
| Total shared memory | 8,080 | - | |
| Total game code memory | 21,952 | 46 | |
| Total workspace memory | 2,033 | 34 | |
| Totals | 65,536 | 144 | 

As you can see - and contrary to popular legend - Elite does not use every single last byte of the BBC Micro's usable memory. There are actually quite a few unused bytes in the cassette version, as noted in the "Unused" column above; 144 of them, to be precise. Here are the details, in the order in which they appear above:

- There are 64 unused bytes in the MOS printer buffer from &0880 to &08BF (as the game does not need a printer).
- There are 34 unused bytes in the main game code:
								- There are six unused bytes in the last saved commander data at NA%. Two of them are between LASER and CRGO, just after the four laser powers; they were originally used for up and down lasers, but those views were dropped and the space never reclaimed. There are four more unused bytes between the escape pod at ESCP and the cargo bay capacity at CRGO, which might have been for additional equipment that didn't get implemented... who knows?
- There's an unused and unlabelled duplicate of the multiplication routine MULTU sandwiched between FMLTU and MLTU2 that takes up 24 bytes.
- The MUT3 routine is never called and would be identical to MUT2 even if it were, so that's another four bytes that aren't used.
 
- There is one unused byte at &07FF in the recursive text token table at QQ18, right at the end of the table.
- There are 11 unused bytes in the Python workspace, between the end of the Python ship blueprint and the SVN and VEC variables, right at the top of user memory.
- In the zero page workspace, the one-byte variable XX14 is never used.
- There are 13 unused bytes in and after the WP workspace:
								- The one-byte variable XX24 is never used.
- There are 12 bytes after the end of the WP workspace, from &0F34 to &0F40, which aren't used.
 
- There are 20 unused bytes in and after the T% workspace:
								- There are six unused bytes in the current commander data block at T%, which correspond with the unused bytes in the last saved commander data block at NA% (see above).
- There are 14 bytes after the end of the T% workspace, from &0372 to &037F, which aren't used.
 

On top of this, there are quite a few instructions in the main game code that have no effect and could have been culled without impact; I've identified 22 of them, but there are no doubt more of them to find (search the comments for "no effect" to find the ones I've spotted).

But this is splitting hairs, as Elite swells the BBC Micro to near bursting point while being both incredibly clever and incredibly efficient, and for that, very serious respect is due to the authors.

## The XX3 heap

													 ------------

						The XX3 heap shares page 1 with the 6502 stack, with XX3 growing up from &0100 and the stack growing down from &01FF. XX3 is used to store temporary values, and the biggest collection of values is stored when drawing ships, when the projected screen coordinates of the ship's visible vertices are stored in the heap. (XX3 is also used to store a copy of the INWK workspace, but at 36 bytes, this is much smaller than the vertex heap.)

In this context, "visible" just means that the vertex is close enough to be seen, irrespective of whether the corresponding face is hidden, so the heap is at its fullest when the ship with the largest number of vertices is close enough for them all to be deemed visible.

In the standard versions of Elite (i.e. the cassette version of BBC Micro Elite and the Acorn Electron version), the Cobra Mk III has the largest number of vertices at 28, There are four bytes stored per vertex, so this means the largest heap size is 28 * 4 = 112 bytes, in which case XX3 takes up memory from &0100 to &016F.

In the enhanced versions of Elite, the Transporter has the largest number of vertices at 37, so the largest heap size is 37 * 4 = 148 bytes, and XX3 takes up memory from &0100 to &0193.

## Shared locations

													 ----------------

						Some locations have two names in the source code. This is partly because some of the code was developed on an Acorn Atom, which restricts the names you can use for labels to two letters followed by one or more numbers. Presumably when this code was merged with the code that was developed on a BBC Micro, where label naming is more flexible, it was easier just to share label names than refactor the Atom code.

The following label names point to the same locations in memory, and are therefore interchangeable:

LOIN = LL30 INWK = XX1 INWK(34 33) = XX19(1 0) X1 = XX15 Y1 = XX15+1 X2 = XX15+2 Y2 = XX15+3 K5 = XX18 = QQ17 K3 = XX2 LSO = LSX CABTMP = MANY

The last one is slightly different, in that the first byte of the MANY table is unused, so CABTMP simply makes the most of the otherwise unused location.

## Elite code as an image

													 ----------------------

						To see just how small the cassette version of Elite is, we can convert the main game binary into an image, with one byte per pixel, and a greyscale showing each byte's value, with 0 being shown as black, 255 being shown as white, and interim values as greyscale pixels. The result is a 162-pixel square, like this (shown here at double size, so you can see the pixels more clearly):

![The game binary for BBC Micro cassette Elite as an image](https://elite.bbcelite.com/images/cassette/code.png) 

						This image contains the entire main game. That's some nice, bloat-free code!

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
  | Python blueprint (PYTHON.bin)     |
  |                                   |
  +-----------------------------------+   &7F00 = SHIP_PYTHON
  |                                   |
  | Memory for the split-screen mode  |
  |                                   |
  +-----------------------------------+   &6000
  |                                   |
  | Ship blueprints (SHIPS.bin)       |
  |                                   |
  +-----------------------------------+   &563A = XX21
  |                                   |
  | Main game code (ELTcode.bin)      |
  |                                   |
  +-----------------------------------+   &0F40 = S%
  |                                   |
  | &0F34-&0F3F unused                |
  |                                   |
  +-----------------------------------+   &0F34
  |                                   |
  | WP workspace                      |
  |                                   |
  +-----------------------------------+   &0D40 = WP
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
  | MOS sound envelope buffer         |
  |                                   |
  +-----------------------------------+   &08C0
  |                                   |
  | MOS printer buffer                |
  |                                   |
  +-----------------------------------+   &0880
  |                                   |
  | MOS sound workspace and buffer    |
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
  | &0372-&037F unused                |
  |                                   |
  +-----------------------------------+   &0372
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

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
LOIN        = LL30
  INWK        = XX1
  INWK(34 33) = XX19(1 0)
  X1          = XX15
  Y1          = XX15+1
  X2          = XX15+2
  Y2          = XX15+3
  K5          = XX18         = QQ17
  K3          = XX2
  LSO         = LSX
  CABTMP      = MANY
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/the_elite_memory_map.html](https://elite.bbcelite.com/deep_dives/the_elite_memory_map.html)*

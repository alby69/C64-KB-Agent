---
title: NES Elite memory map
source_url: https://elite.bbcelite.com/deep_dives/the_elite_memory_map_nes.html
category: deep-dive
topics:
- sprite programming
- basic
- assembly
- memory management
- graphics
difficulty: intermediate
language: mixed
hardware:
- CPU
- SID
- KERNAL
- VIC-II
related:
- sound-programming
- music-player
- raster-interrupts
- memory-map
- sprite-programming
- vic-ii-registers
- kernal-routines
- sid-registers
scraped_at: '2026-07-14'
---

# NES Elite memory map

## Memory usage in the only console-based version of Elite

When it comes to memory layout, the NES is quite different to the BBC Micro, Acorn Electron, Commodore 64 and Apple II, despite sharing the same 6502-based CPU architecture.

In the computer versions of Elite, the game is loaded into RAM, which gets shared between the code, variable storage and screen memory. This means the game structure can be a mixture of instructions and variables, all of which can be updated (so code can be modified as well as variables, though Elite tends not to do this, unlike a lot of other games of this era).

The memory map of the NES console is a lot more regimented. The game code lives in read-only ROM, which is plugged into the system as part of the game cartridge. Alongside the ROM, there are three separate blocks of writeable RAM: there's 2K of work RAM (WRAM) that's built into the console, there's 8K of battery-backed WRAM that's built into the Elite cartridge, and there's another 10K of video RAM (VRAM) that's used by the Picture Processing Unit (PPU), of which 2K of VRAM is on-board and 8K of VRAM is provided by the Elite cartridge. The line between ROM and RAM is absolute, and that dictates the shape of the memory map.

The VRAM is managed by the PPU and isn't directly accessible from the game code. Instead it can only be accessed via the PPU registers, and it has its own separate structure that is independent from the main game's memory map, so we won't cover it here. For details of how the VRAM is laid out, see the deep dive on [understanding the NES for Elite](https://elite.bbcelite.com/understanding_the_nes_for_elite.html) instead.

That leaves the game code in ROM, and the two banks of WRAM that the game can access directly. The ROM is mapped into memory from $8000 to $FFFF, the 8K of battery-backed cartridge RAM is from $6000 to $7FFF, and the 2K of built-in RAM is from $0000 to $07FF. They are laid out in memory as follows, with the top three blocks being ROM, and the rest being WRAM:

+-----------------------------------+ $FFFF | | | Vectors (in ROM bank 7) | | | +-----------------------------------+ $FFFA =[Vectors_b7](https://elite.bbcelite.com/nes/bank_7/variable/vectors_b7.html)| | | ROM bank 7 | | | +-----------------------------------+ $C000 =[ResetMMC1_b7](https://elite.bbcelite.com/nes/bank_7/variable/resetmmc1_b7.html)| | | Currently paged ROM bank (0 to 6) | | | +-----------------------------------+ $8000 =[ResetMMC1_b0](https://elite.bbcelite.com/nes/bank_0/subroutine/resetmmc1_b0.html)| | | $7FD8-$7FFF unused | | | +-----------------------------------+ $7FD8 | | | Saved commander slots | | | +-----------------------------------+ $7800 | | | Attribute buffer 1 | | | +-----------------------------------+ $77C0 | | | Nametable buffer 1 | | | +-----------------------------------+ $7400 | | | Attribute buffer 0 | | | +-----------------------------------+ $73C0 | | | Nametable buffer 0 | | | +-----------------------------------+ $7000 | | | Pattern buffer 1 | | | +-----------------------------------+ $6800 | | | Pattern buffer 0 | | | +-----------------------------------+ $6000 =[Cartridge WRAM](https://elite.bbcelite.com/nes/common/workspace/cartridge_wram.html)| | . . . . . . . . . . | | +-----------------------------------+ $0750 when all ship slots are used | | | Ship data blocks ascend from K% | | | +-----------------------------------+ $0600 =[K%](https://elite.bbcelite.com/nes/common/workspace/k_per_cent.html)| | | WP workspace | | | +-----------------------------------+ $0300 =[WP](https://elite.bbcelite.com/nes/common/workspace/wp.html)| | | Sprite buffer | | | +-----------------------------------+ $0200 =[ySprite0](https://elite.bbcelite.com/nes/common/workspace/sprite_buffer.html)| | | 6502 stack descends from $01FF | | | +-----------------------------------+ &0194 | | | Heap space ascends from XX3 | | | +-----------------------------------+ $0100 =[XX3](https://elite.bbcelite.com/nes/common/workspace/xx3.html)| | | Zero page workspace | | | +-----------------------------------+ $0000 =[ZP](https://elite.bbcelite.com/nes/common/workspace/zp.html)

The game code is split into eight different ROM banks, with bank 7 permanently mapped into the top of memory from $C000 to $FFFF. Routines in bank 7 can page the other ROM banks into memory at $8000, enabling the game binary to be 128K in size, with only 32K of this being paged into memory at any one time (16K for bank 7 and 16K for one of banks 0 to 6). This process is controlled by the MMC1 mapper, and is described in the deep dive on [splitting NES Elite across multiple ROM banks](https://elite.bbcelite.com/splitting_nes_elite_across_multiple_rom_banks.html).

You'll notice there is a large gap in the memory map between $0800 and $5FFF. The main use for this memory range is to access the console's Audio Processing Unit (APU) and Picture Processing Unit (PPU), whose registers are mapped to addresses in this range - essentially, we can make sounds and draw to the screen by reading and writing specific locations within this block. See the deep dive on [understanding the NES for Elite](https://elite.bbcelite.com/understanding_the_nes_for_elite.html) for details about this process.

In terms of free memory, there are some reasonable chunks of unused memory at the end of each ROM bank. Specifically, each ROM bank is padded out with $FF bytes between the end of the code and the vectors in the last six bytes of each bank. These unused blocks are as follows:

- ROM bank 0 is unused from $BFF5 to $BFF9 = 5 free bytes
- ROM bank 1 is unused from $BC51 to $BFF9 = 936 free bytes
- ROM bank 2 is unused from $B934 to $BFF9 = 1734 free bytes
- ROM bank 3 is unused from $BB4B to $BFF9 = 1199 free bytes
- ROM bank 4 is unused from $BA98 to $BFF9 = 1378 free bytes
- ROM bank 5 is unused from $BF6C to $BFF9 = 142 free bytes
- ROM bank 6 is unused from $BF08 to $BFF9 = 242 free bytes
- ROM bank 7 is unused from $FFD8 to $FFF9 = 34 free bytes

That's a total of 5670 free bytes of ROM. There are also 40 bytes of unused RAM from $7FD8 to $7FFF, and there are other unused bytes dotted throughout the code and variable space. Altogether there is more than enough free space to add at least one extra feature to NES Elite... though it [probably doesn't need any](https://elite.bbcelite.com/comparing_nes_elite_with_the_other_versions.html).

## Elite code as an image

													 ----------------------

						To see just how big NES Elite is, we can convert the main game binary into an image, with one byte per pixel, and a greyscale showing each byte's value, with 0 being shown as black, 255 being shown as white, and interim values as greyscale pixels. The result is a 363-pixel square, like this:

![The game binary for NES Elite as an image](https://elite.bbcelite.com/images/nes/code.png) 

						This is easily the biggest version of Elite on the 6502, and you can clearly see the division into the eight ROM banks.

## Codice Estratto

### Snippet Codice (BASIC)

```basic
+-----------------------------------+   $FFFF
  |                                   |
  | Vectors (in ROM bank 7)           |
  |                                   |
  +-----------------------------------+   $FFFA = Vectors_b7
  |                                   |
  | ROM bank 7                        |
  |                                   |
  +-----------------------------------+   $C000 = ResetMMC1_b7
  |                                   |
  | Currently paged ROM bank (0 to 6) |
  |                                   |
  +-----------------------------------+   $8000 = ResetMMC1_b0
  |                                   |
  | $7FD8-$7FFF unused                |
  |                                   |
  +-----------------------------------+   $7FD8
  |                                   |
  | Saved commander slots             |
  |                                   |
  +-----------------------------------+   $7800
  |                                   |
  | Attribute buffer 1                |
  |                                   |
  +-----------------------------------+   $77C0
  |                                   |
  | Nametable buffer 1                |
  |                                   |
  +-----------------------------------+   $7400
  |                                   |
  | Attribute buffer 0                |
  |                                   |
  +-----------------------------------+   $73C0
  |                                   |
  | Nametable buffer 0                |
  |                                   |
  +-----------------------------------+   $7000
  |                                   |
  | Pattern buffer 1                  |
  |                                   |
  +-----------------------------------+   $6800
  |                                   |
  | Pattern buffer 0                  |
  |                                   |
  +-----------------------------------+   $6000 = Cartridge WRAM
  |                                   |
  .                                   .
  .                                   .
  .                                   .
  .                                   .
  .                                   .
  |                                   |
  +-----------------------------------+   $0750 when all ship slots are used
  |                                   |
  | Ship data blocks ascend from K%   |
  |                                   |
  +-----------------------------------+   $0600 = K%
  |                                   |
  | WP workspace                      |
  |                                   |
  +-----------------------------------+   $0300 = WP
  |                                   |
  | Sprite buffer                     |
  |                                   |
  +-----------------------------------+   $0200 = ySprite0
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
*Fonte originale: [https://elite.bbcelite.com/deep_dives/the_elite_memory_map_nes.html](https://elite.bbcelite.com/deep_dives/the_elite_memory_map_nes.html)*

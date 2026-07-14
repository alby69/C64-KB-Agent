---
title: 6502 Second Processor Elite memory map
source_url: https://elite.bbcelite.com/deep_dives/the_elite_memory_map_6502sp.html
category: deep-dive
topics:
- memory management
- basic
- assembly
- graphics
difficulty: intermediate
language: mixed
hardware:
- CPU
- SID
- BASIC ROM
- KERNAL
related:
- music-player
- sound-programming
- memory-map
- kernal-routines
- sid-registers
scraped_at: '2026-07-14'
---

# 6502 Second Processor Elite memory map

## Memory usage in the Tube-based version of Elite

Unlike the cassette and disc versions of BBC Micro Elite, the 6502 Second Processor version is positively swimming in memory. But even with 32K in the BBC Micro and a whopping 64K in the Second Processor, Elite still manages to take up almost all of the available memory, as everything in the game is loaded at once - all the ship blueprints, all the docked and flight code, and all the features that are unique to this version, like the scrolling text demo, the screenshot system, printer support and the system for [communicating across the Tube](https://elite.bbcelite.com/6502sp_tube_communication.html). Even the BBC Master version isn't quite this large; if the cassette version is a paragon of youthful efficiency, the 6502 Second Processor version is more like a middle-aged spread.

Not surprisingly, the memory map for 6502 Second Processor Elite is split in two, with the majority of the game code running in the parasite (the Second Processor), and a much smaller set of code running in the I/O processor (the BBC Micro), where most of the space is taken up by the screen memory. Let's look at the two memory maps in turn, starting with the motherlode in the parasite.

## Parasite memory map

													 -------------------

						In a 6502 Second Processor that isn't running a language ROM such as BASIC - which is the case when running machine code programs such as Elite - the available user RAM extends from &0400 to &F7FF, plus all of zero page except for 18 bytes, which are reserved for the Second Processor OS. Compared to the standard BBC Micro, this is an amazing amount of memory - out of the 64K of memory in the Second Processor, 2K is required for the Second Processor OS itself, 530 bytes are used as OS workspace (that's &0200-&03FF plus those 18 zero-page bytes), and the 65C02 reserves the 256 bytes of page 1 for the stack (though as with the other versions of Elite, it still uses the opposite end of the stack's page for its own heap storage).

That's a total of just 2,834 bytes for the OS and stack, leaving 62,702 bytes free for user programs, or 61.2K. Elite manages to use almost all of that memory, leaving just 3,263 bytes, or 3.2K unused:

+-----------------------------------+ &FFFF | | | Second Processor OS | | | +-----------------------------------+ &F800 | | | &F102-&F7FF unused | | | +-----------------------------------+ &F102 | | | Ship blueprints | | | +-----------------------------------+ &D000 =[XX21](https://elite.bbcelite.com/6502sp/main/variable/xx21.html)| | | Ship line heap descends from LS% | | | +-----------------------------------+ SLSP | | . . . . . . . . . . | | +-----------------------------------+ &9200 | | | LP workspace (shared with ships) | | | +-----------------------------------+ &8600 =[LP](https://elite.bbcelite.com/6502sp/main/workspace/lp.html)| | . . . . . . . . . . | | +-----------------------------------+ &84E4 when all ship slots are used | | | Ship data blocks ascend from K% | | | +-----------------------------------+ &8200 =[K%](https://elite.bbcelite.com/6502sp/main/workspace/k_per_cent.html)| | | &818F-&81FF unused | | | +-----------------------------------+ &818F = F% | | | Main parasite code (P.CODE) | | | +-----------------------------------+ &1000 =[Parasite variables](https://elite.bbcelite.com/6502sp/main/workspace/parasite_variables.html)| | | &0E3C-&0FFF unused | | | +-----------------------------------+ &0E3C | | | WP workspace | | | +-----------------------------------+ &0D00 =[WP](https://elite.bbcelite.com/6502sp/main/workspace/wp.html)| | | Hangar ship line heap, file space | | | +-----------------------------------+ &0B00 | | | &0975-&0AFF unused | | | +-----------------------------------+ &0975 | | | UP workspace | | | +-----------------------------------+ &0800 =[UP](https://elite.bbcelite.com/6502sp/main/workspace/up.html)| | | Sine, cosine and arctan tables | | | +-----------------------------------+ &07C0 =[SNE](https://elite.bbcelite.com/6502sp/main/variable/sne.html)| | | Recursive text tokens (WORDS.bin) | | | +-----------------------------------+ &0400 =[QQ18](https://elite.bbcelite.com/6502sp/main/variable/qq18.html)| | | Second Processor OS workspace | | | +-----------------------------------+ &0200 | | | 6502 stack descends from &01FF | | | +-----------------------------------+ &0194 | | | Heap space ascends from XX3 | | | +-----------------------------------+ &0100 =[XX3](https://elite.bbcelite.com/6502sp/main/workspace/xx3.html)| | | MOS workspace | | | +-----------------------------------+ &00EE | | | Zero page workspace | | | +-----------------------------------+ &0000 =[ZP](https://elite.bbcelite.com/6502sp/main/workspace/zp.html)

## I/O processor memory map

													 ------------------------

						Compared to the luxurious 61.2K of user memory available in the parasite, the BBC Micro's memory is a lot more cramped when it acts as the I/O processor. The main reason is that the 6502 Second Processor version of Elite devotes a large chunk of memory to the mode 1/mode 2 split-screen mode - 15.5K, to be precise - and all of that memory is in the BBC Micro.

On top of that, the Disc Filing System (DFS) takes up a considerable amount of room, pushing PAGE (the start of user memory) to &1900, and then there's the Tube host code that looks after communication with the Second Processor, which gets copied into pages 4 to 7 on start-up, taking over the language ROM workspace that is normally available to machine code programs. We even lose access to a large chunk of zero page, as the Tube host code also uses locations below &80.

Incidentally, the Tube also grabs another 6 pages of memory by default, this time to support a user-definable (or "exploded") character set. This would push PAGE up to &1F00, but this feature can be disabled to "implode" the character set and reclaim this memory. Elite does this as it doesn't use the OS printing routines, but you can see that demands on the BBC Micro's memory are many and varied, even though the parasite is supposed to be the one doing all the work.

Let's see how Elite uses up most of the available memory in the I/O processor, leaving just 3,787 bytes, or 3.7K unused.

+-----------------------------------+ &FFFF | | | Machine Operating System (MOS) | | | +-----------------------------------+ &C000 | | | Paged ROMs | | | +-----------------------------------+ &8000 | | | &7E00-&7FFF unused | | | +-----------------------------------+ &7E00 | | | Memory for the split-screen mode | | | +-----------------------------------+ &4000 | | | &3D36-&3FFF unused | | | +-----------------------------------+ &3D36 | | | Main I/O code (I.CODE) | | | +-----------------------------------+ &2300 =[TABLE](https://elite.bbcelite.com/6502sp/i_o_processor/variable/table.html)| | | &1900-&22FF unused | | | +-----------------------------------+ &1900 | | | MOS workspace | | | +-----------------------------------+ &0800 | | | Tube host code | | | +-----------------------------------+ &0400 | | | MOS workspace | | | +-----------------------------------+ &0200 | | | 6502 stack descends from &01FF | | | +-----------------------------------+ &0100 | | | Zero page workspace | | | +-----------------------------------+ &0080 =[ZP](https://elite.bbcelite.com/6502sp/main/workspace/zp.html)| | | Tube host code | | | +-----------------------------------+ &0000

Overall, the 6502 Second Processor version of Elite leaves a paltry 7,039 bytes unused, or just 6.9K out of the 96K of RAM in the two-system host-parasite setup. It's a far cry from the cut-down cassette version, that's for sure.

## Elite code as an image

													 ----------------------

						To see just how big 6502 Second Processor Elite is, we can convert the main game binary into an image, with one byte per pixel, and a greyscale showing each byte's value, with 0 being shown as black, 255 being shown as white, and interim values as greyscale pixels. The result is a 228-pixel square, like this (shown here at double size, so you can see the pixels more clearly):

![The game binary for 6502 Second Processor Elite as an image](https://elite.bbcelite.com/images/6502sp/code.png) 

						This image contains the entire main game, including all the game data.

## Codice Estratto

### Snippet Codice (BASIC)

```basic
+-----------------------------------+   &FFFF
  |                                   |
  | Second Processor OS               |
  |                                   |
  +-----------------------------------+   &F800
  |                                   |
  | &F102-&F7FF unused                |
  |                                   |
  +-----------------------------------+   &F102
  |                                   |
  | Ship blueprints                   |
  |                                   |
  +-----------------------------------+   &D000 = XX21
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
  +-----------------------------------+   &9200
  |                                   |
  | LP workspace (shared with ships)  |
  |                                   |
  +-----------------------------------+   &8600 = LP
  |                                   |
  .                                   .
  .                                   .
  .                                   .
  .                                   .
  .                                   .
  |                                   |
  +-----------------------------------+   &84E4 when all ship slots are used
  |                                   |
  | Ship data blocks ascend from K%   |
  |                                   |
  +-----------------------------------+   &8200 = K%
  |                                   |
  | &818F-&81FF unused                |
  |                                   |
  +-----------------------------------+   &818F = F%
  |                                   |
  | Main parasite code (P.CODE)       |
  |                                   |
  +-----------------------------------+   &1000 = Parasite variables
  |                                   |
  | &0E3C-&0FFF unused                |
  |                                   |
  +-----------------------------------+   &0E3C
  |                                   |
  | WP workspace                      |
  |                                   |
  +-----------------------------------+   &0D00 = WP
  |                                   |
  | Hangar ship line heap, file space |
  |                                   |
  +-----------------------------------+   &0B00
  |                                   |
  | &0975-&0AFF unused                |
  |                                   |
  +-----------------------------------+   &0975
  |                                   |
  | UP workspace                      |
  |                                   |
  +-----------------------------------+   &0800 = UP
  |                                   |
  | Sine, cosine and arctan tables    |
  |                                   |
  +-----------------------------------+   &07C0 = SNE
  |                                   |
  | Recursive text tokens (WORDS.bin) |
  |                                   |
  +-----------------------------------+   &0400 = QQ18
  |                                   |
  | Second Processor OS workspace     |
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
  | MOS workspace                     |
  |                                   |
  +-----------------------------------+   &00EE
  |                                   |
  | Zero page workspace               |
  |                                   |
  +-----------------------------------+   &0000 = ZP
```

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
  | &7E00-&7FFF unused                |
  |                                   |
  +-----------------------------------+   &7E00
  |                                   |
  | Memory for the split-screen mode  |
  |                                   |
  +-----------------------------------+   &4000
  |                                   |
  | &3D36-&3FFF unused                |
  |                                   |
  +-----------------------------------+   &3D36
  |                                   |
  | Main I/O code (I.CODE)            |
  |                                   |
  +-----------------------------------+   &2300 = TABLE
  |                                   |
  | &1900-&22FF unused                |
  |                                   |
  +-----------------------------------+   &1900
  |                                   |
  | MOS workspace                     |
  |                                   |
  +-----------------------------------+   &0800
  |                                   |
  | Tube host code                    |
  |                                   |
  +-----------------------------------+   &0400
  |                                   |
  | MOS workspace                     |
  |                                   |
  +-----------------------------------+   &0200
  |                                   |
  | 6502 stack descends from &01FF    |
  |                                   |
  +-----------------------------------+   &0100
  |                                   |
  | Zero page workspace               |
  |                                   |
  +-----------------------------------+   &0080 = ZP
  |                                   |
  | Tube host code                    |
  |                                   |
  +-----------------------------------+   &0000
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/the_elite_memory_map_6502sp.html](https://elite.bbcelite.com/deep_dives/the_elite_memory_map_6502sp.html)*

---
title: Technical information for the Elite Universe Editor
source_url: https://elite.bbcelite.com/hacks/elite_universe_editor_technical_information.html
category: source-code
topics:
- basic
- assembly
- sprite programming
difficulty: beginner
language: mixed
hardware:
- SID
- CPU
- VIC-II
- KERNAL
- BASIC ROM
related:
- sid-registers
- sound-programming
- vic-ii-registers
- memory-map
- kernal-routines
- music-player
- sprite-programming
- raster-interrupts
scraped_at: '2026-07-20'
---

# Technical information for the Elite Universe Editor

## Details of how the Elite Universe Editor works under the bonnet

This page contains various bits of technical information about the Elite Universe Editor. Click on any of the following to jump down to the relevant section:

- [Exploring the Universe Editor source code](https://elite.bbcelite.com#source)
- [The universe file format](https://elite.bbcelite.com#file)
- [Creating universes for the Master and Commodore 64 versions](https://elite.bbcelite.com#master)
- [Squeezing the Universe Editor into BBC Elite](https://elite.bbcelite.com#bbc_map)
- [Squeezing the Universe Editor into Commodore 64 Elite](https://elite.bbcelite.com#commodore64_map)

When reading this section, it is pretty useful to have the source code to hand, so let's start with that.


													 -----------------------------------------

						The source code for the Universe Editor is available for you to explore. It is fully documented and fully buildable on modern computers, and the source includes labelled modifications within the main game code so you can see exactly how the mod gets hooked in.

The core Universe Editor code lives in this library repository, which contains the code for all three platforms:

This gets included as a GitHub submodule in each of the three versions of the Universe Editor, each of which has its own repository:

- [BBC Master Elite Universe Editor](https://github.com/markmoxon/elite-universe-editor-bbc-master)
- [6502 Second Processor Elite Universe Editor](https://github.com/markmoxon/elite-universe-editor-6502-second-processor)
- [Commodore 64 Elite Universe Editor](https://github.com/markmoxon/elite-universe-editor-commodore-64)

For the BBC versions, these repositories are downstream from the main code repositories at [elite-source-code-bbc-master](https://github.com/markmoxon/elite-source-code-bbc-master) and [elite-source-code-6502-second-processor](https://github.com/markmoxon/elite-source-code-6502-second-processor), so it's easy to keep the modified codebase for the Universe Editor in sync with the original source.

Finally, the [elite-universe-editor repository](https://github.com/markmoxon/elite-universe-editor) pulls together all the above repositories as submodules, and builds the final disc images for the Universe Editor and the Elite Compendium.


													 ------------------------

						The universe file format is essentially a concatenated memory dump of the relevant parts of the workspace from the 6502 Second Processor version. When loaded into the BBC Master or Commodore 64, the file is converted to address any differences in the memory map, but the file format is the same across all platforms.

The file length is &0321 bytes and consists of the following (the links will take you to those variables in the 6502 Second Processor source code):

| Offset | Size | Contents | 
|---|---|---|
| &000 to &001 | 2 bytes | &F900 (Commodore 64 PRG, see below) | 
| &002 to &2E5 | &2E4 (740) bytes | [K%](https://elite.bbcelite.com/6502sp/main/workspace/k_per_cent.html)block (20 ships, 37 bytes each) | 
| &2E6 to &2FA | &15 (21) bytes | [FRIN](https://elite.bbcelite.com/6502sp/main/workspace/up.html#frin)block | 
| &2FB to &31D | &23 (35) bytes | [MANY](https://elite.bbcelite.com/6502sp/main/workspace/up.html#many)block | 
| &31E | 1 byte | [JUNK](https://elite.bbcelite.com/6502sp/main/workspace/up.html#junk)byte | 
| &31F to &320 | 2 bytes | [SLSP(1 0)](https://elite.bbcelite.com/6502sp/main/workspace/up.html#slsp)address | 

The file format supports up to 20 ships in the bubble, as per the 6502 Second Processor version, with 37 bytes of ship data per slot. When a file is loaded into a BBC Master, only the first 12 ship slots are used, and the rest are ignored; when loaded into a Commodore 64, only the first 10 ship slots are used. Ship heap memory addresses in INWK(34 33) are updated to work on the Master and Commodore 64, but if the bottom of the ship heap at SLSP is at a lower address than the top of the K% ship data blocks, then the ship data and the ship heap will overlap, and the file will crash. See the [BBC Master memory map](https://elite.bbcelite.com/deep_dives/the_elite_memory_map_master.html) for a diagram that shows this.

The first two bytes are only used by the Commodore 64. On the Commodore 64, file load addresses are stored in the first two bytes of the file (for PRG files), so they are always set to &F900 (0 in the first byte, &F9 in the second byte). The original Elite saves commander files as PRG files, so the Universe Editor does the same. You can load the same files into both the BBC and Commodore versions of the Universe Editor, and the BBC versions simply ignore the first two bytes.

Note that the first release of the Universe Editor on the BBC Micro and BBC Master (build number 2022-10-27 14:49:14) did not include these two bytes in their universe files; they were added in the second release to support cross-platform loading. As a result, files saved from the first release will not load on later releases, and vice versa. To load these original files into the latest version of the Universe Editor, two new bytes need to be appended to the start of the file, after which they can successfully be loaded on all three platforms. There is a BASIC program called B.CONVERT on the BBC disc image that you can run to update files, or you can do it yourself by using a hex editor to prepend &00 and &F9 to the start of the file.


													 -----------------------------------------------------------

						If you want to generate universe files that are guaranteed to work on all versions of the Universe Editor, and in particular the BBC Master and Commodore 64 versions, then I recommend you build them on the Master or the Commodore 64. The 6502 Second Processor version supports more ship slots and more types of ship, and although the editor tries to convert these larger files when they are loaded into a BBC Master or Commodore 64, they can cause problems (in particular, the line-drawing routine can go haywire - it's pretty obvious when things don't work!).

The SHIPID6 file that's included with the BBC version of the Universe Editor is a good example - it works on the 6502 Second Processor, but crashes when loaded into a Master, as it contains more ships than there are slots in the Master version. A quick fix for this kind of issue is to load the file into the 6502 Second Processor version and delete the extra ships, so the smaller file will load into the Master properly. The SHIPID file takes this approach; it contains the same universe as SHIPID6 but with fewer ships, and it works fine on all three versions of the Universe Editor.

Note that if a universe includes the Elite logo, which is only supported in the 6502 Second Processor version, then if you want to be able to load the same file on a Master or Commodore 64, you should put the logo in the last used slot. When a file containing the logo is loaded into a Master or Commodore 64, the logo is deleted along with any other ships after it. This approach is used in the included BOXART1 file, which loads on all three machines, but only displays the logo on the 6502 Second Processor.

In summary, if you create files on the 6502 Second Processor version that you want to load into the Master or Commodore 64, keep the number and complexity of ships lower to increase your chances of it working, and only include the Elite logo in the last slot.


													 --------------------------------------------

						Elite is famous for using every spare byte in the BBC Micro, and while this is [pretty much the case](https://elite.bbcelite.com/deep_dives/the_elite_memory_map.html) in the standard BBC Micro versions, the enhanced versions on the 6502 Second Processor and BBC Master do have some spare memory. It turns out this is just enough free space to squeeze in a Universe Editor.

If you look at the memory maps for the [6502 Second Processor](https://elite.bbcelite.com/deep_dives/the_elite_memory_map_6502sp.html) and [BBC Master](https://elite.bbcelite.com/deep_dives/the_elite_memory_map_master.html) versions, there are various unused blocks that are perfect for hosting new functionality, leaving the original game untouched save for a quick key-press check on the title screen and the addition of a "Universe Editor" subtitle.

That said, although the full game is present in the Universe Editor, I did have to remove the rolling demo from the 6502 Second Processor version, and the music from the Commodore 64 version. Also missing (from all versions) is pause option X, which shows the authors' names on the title screen, as that's been replaced by the subtitle. But apart from the removal of these two Easter eggs, the original game is present and correct.

In order for me to slot what is essentially the same Universe Editor code into both platforms, I had to split it up into five blocks, which I then packed into the different pockets of free space in each version. The source files for these blocks are called elite-universe-editor-1.asm through elite-universe-editor-4.asm, plus elite-universe-editor-z.asm, and you can see them in the GitHub repository.

You can see how these various files get slotted into the game code in the memory maps below. Note that the 6502 Second Processor code is split between the I/O Processor and the Parasite - the "z" suffix in elite-universe-editor-z.asm denotes the code that goes in the I/O Processor, as the name of the original game's I/O Processor source file is elite-z.asm.

First, let's look at the 6502 Second Processor version, starting with the Parasite memory map (which you might like to compare with the [memory map for the unmodified version](https://elite.bbcelite.com/deep_dives/the_elite_memory_map_6502sp.html)):

+-----------------------------------+ &FFFF | | | Second Processor OS | | | +-----------------------------------+ &F800 | | | elite-universe-editor-4.asm | | | +-----------------------------------+ &F10C | | | Ship blueprints | | | +-----------------------------------+ &D000 =[XX21](https://elite.bbcelite.com/6502sp/main/variable/xx21.html)| | . . . . . . | | +-----------------------------------+ | | | Ship data blocks ascend from K% | | | +-----------------------------------+ &8200 =[K%](https://elite.bbcelite.com/6502sp/main/workspace/k_per_cent.html)| | | elite-universe-editor-3.asm | | | +-----------------------------------+ &8191 | | | Main parasite code (P.CODE) | | | +-----------------------------------+ &738D | | | elite-universe-editor-2.asm | Replaces the demo, DEMON to SPEECH | | +-----------------------------------+ &6E42 | | | Main parasite code (P.CODE) | | | +-----------------------------------+ &1000 =[Parasite variables](https://elite.bbcelite.com/6502sp/main/workspace/parasite_variables.html)| | | elite-universe-editor-1.asm | | | +-----------------------------------+ &0E3C | | | WP workspace | | | +-----------------------------------+ &0D00 =[WP](https://elite.bbcelite.com/6502sp/main/workspace/wp.html). . . . . .

Here's the I/O Processor memory map (and for comparison, here's the [memory map for the unmodified version](https://elite.bbcelite.com/deep_dives/the_elite_memory_map_6502sp.html)):

. . . . . . | | +-----------------------------------+ &7E00 | | | Memory for the split-screen mode | | | +-----------------------------------+ &4000 | | | elite-universe-editor-z.asm | | | +-----------------------------------+ &3D36 | | | Main I/O code (I.CODE) | | | +-----------------------------------+ &2300 =[TABLE](https://elite.bbcelite.com/6502sp/i_o_processor/variable/table.html)| | . . . . . .

Finally, here's the BBC Master memory map (which you might like to compare with the [memory map for the unmodified version](https://elite.bbcelite.com/deep_dives/the_elite_memory_map_master.html)):

+-----------------------------------+ &FFFF | | | Machine Operating System (MOS) | | | +-----------------------------------+ &C000 | | | elite-universe-editor-1, 2, 4.asm | | | +-----------------------------------+ &B200 | | | Text tokens, sin/cos tables | | | +-----------------------------------+ &A000 =[QQ18](https://elite.bbcelite.com/master/game_data/variable/qq18.html)| | | elite-universe-editor-z.asm | | | +-----------------------------------+ &9D94 | | | Ship blueprints (SHIPS.bin) | | | +-----------------------------------+ &8000 =[XX21](https://elite.bbcelite.com/master/game_data/variable/xx21.html)| | | elite-universe-editor-3.asm | | | +-----------------------------------+ &7F48 | | | Main game code (BCODE.bin) | | | +-----------------------------------+ &1300 =[TVT3](https://elite.bbcelite.com/master/main/variable/tvt3.html)| | . . . . . .

In the Master version, I had to make sure all the disc access code was in main memory, as otherwise it would crash on finding a disc error. The only bit of code in main memory is elite-universe-editor-3.asm, so that's where all the saving and loading code appears.

To see where the Universe Editor source code is added to the game, search the source code for "INCLUDE" to see where BeebAsm adds the files, and to see the modifications to the original code that hook in the new code, search for "Mod:".

To demonstrate what a squeeze it is to shoehorn the Universe Editor into Elite, here's a summary of the amount of code that sits within each of the blocks across both versions. Let's start with the 6502 Second Processor version, which is the tighter of the two as there is very little free space in the parasite. These are the addresses of the code within each of the blocks:

```
  1 = CheckShiftCtrl to endUniverseEditor1 = &0E3C to &0FD9 = &019E =  414
  2 = UniverseEditor to endUniverseEditor2 = &6E42 to &7383 = &0542 = 1346
  3 = SaveLoadFile   to endUniverseEditor3 = &8191 to &81EF = &005F =   95
      prgAddress                           = &81FE to &81FF = &0002 =    2
  4 = UpdateChecksum to endUniverseEditor4 = &F102 to &F7E5 = &06E4 = 1764
  z = rowOffsets     to endUniverseEditorZ = &3D36 to &3E87 = &0152 =  338
                                            Total code size = &0F77 = 3959
```
						These are the constraints on the block sizes, as per the memory maps above, showing any free memory at the end of each block:

Block end address Maximum value Actual value Free space ----------------- ------------- ------------ ---------- endUniverseEditor1 &1000 &0FD9 38 bytes endUniverseEditor2 &738D &7383 9 bytes endUniverseEditor3 &81FE &81EF 14 bytes endUniverseEditor4 &F800 &F7E5 26 bytes endUniverseEditorZ &4000 &3E87 376 bytes

Now for the BBC Master version. Here are the addresses of the code within each of the blocks:

```
  1 = CheckShiftCtrl to endUniverseEditor1 = &B200 to &B3CE = &01CF =  463
  2 = UniverseEditor to endUniverseEditor2 = &B3CF to &B8F1 = &0523 = 1315
  3 = SaveLoadFile   to endUniverseEditor3 = &7F4F to &7FFF = &00B1 =  177
  4 = UpdateChecksum to endUniverseEditor4 = &B8F2 to &BFF4 = &0703 = 1795
  z = rowOffsets     to endUniverseEditorZ = &9D95 to &9F1A = &0186 =  390
                                            Total code size = &102C = 4140
```
						and these are the constraints on the block sizes, as per the memory map:

Block end address Maximum value Actual value Free space ----------------- ------------- ------------ ---------- endUniverseEditor3 &8000 &7FFF 0 bytes endUniverseEditor4 &C000 &BFF4 11 bytes endUniverseEditorZ &9FFF &9F1A 228 bytes

Note that in the Master version, the block that ends at endUniverseEditor4 consists of blocks 1, 2 and 4, one after the other in memory.

To summarize, the 6502 Second Processor version of the Universe Editor is 3959 bytes of code, while the BBC Master version is 4140 bytes; the extra code is mainly devoted to converting the file format to work with a Master.

The 6502 Second Processor's parasite has just 87 bytes free, spread across four blocks, while the Master version has 239 bytes free. However, as the codebase is shared between the two platforms, we can't add any more shared functionality, as it would have to go into elite-universe-editor-z.asm (as there are only 11 bytes free in blocks 1-4 on the Master). However, in the 6502 Second Processor version, elite-universe-editor-z.asm runs in the I/O Processor, so any extra shared code we add would have to work in the I/O Processor, which isn't that useful for adding functionality to the main codebase across both systems. It could probably be wrapped in an API call, but sometimes you have to know when to stop...

To put it another way, if we want to maintain a shared codebase, we have only got 11 bytes free, which is an even tighter squeeze than in the [original BBC Micro version](https://elite.bbcelite.com/deep_dives/the_elite_memory_map.html).


													 -----------------------------------------------------

						The Commodore 64 comes with twice the memory of the standard BBC machines (64K vs 32K), so you would assume that there would be lots of free space available for the Universe Editor add-on. However, the additional sprites and music in the Commodore version are pretty memory-hungry, so in the end I had to sacrifice the music in order to fit the Universe Editor routines into memory.

The music data for the Commodore 64 version lives between addresses $B72D and $CFFF (though there are some spare bytes at the end of this block). If we disable the music, then this gives us $18D3 (6355) bytes of space, which is more than enough for the Universe Editor. The routine that actually plays the music is at address $920D, so we can reclaim all the memory used by the music data by simply injecting an RTS instruction into $920D. This makes the music routines return without doing anything, leaving the music data at $B72D unused.

This injection process is implemented in the elite-modify.py script, which extracts the game binaries, decrypts them, modifies them with the Universe Editor code, and re-encrypts them. Disabling the music is done as part of this process; see the project's [GitHub repository](https://github.com/markmoxon/elite-universe-editor) for details.

The music data is actually in two parts: the title music is from $B72D to $C163, while the docking music runs from $C164 to $CCD5. Unfortunately, removing just one tune doesn't free up enough memory for the Universe Editor, so sadly they both have to go.

For more details of the memory layout of the Commodore 64 version, check out the [Commodore 64 Elite memory map](https://elite.bbcelite.com/deep_dives/the_elite_memory_map_commodore_64.html).

## Codice Estratto

### Snippet Codice (BASIC)

```basic
+-----------------------------------+   &FFFF
  |                                   |
  | Second Processor OS               |
  |                                   |
  +-----------------------------------+   &F800
  |                                   |
  | elite-universe-editor-4.asm       |
  |                                   |
  +-----------------------------------+   &F10C
  |                                   |
  | Ship blueprints                   |
  |                                   |
  +-----------------------------------+   &D000 = XX21
  |                                   |
  .                                   .
  .                                   .
  .                                   .
  |                                   |
  +-----------------------------------+
  |                                   |
  | Ship data blocks ascend from K%   |
  |                                   |
  +-----------------------------------+   &8200 = K%
  |                                   |
  | elite-universe-editor-3.asm       |
  |                                   |
  +-----------------------------------+   &8191
  |                                   |
  | Main parasite code (P.CODE)       |
  |                                   |
  +-----------------------------------+   &738D
  |                                   |
  | elite-universe-editor-2.asm       |   Replaces the demo, DEMON to SPEECH  
  |                                   |
  +-----------------------------------+   &6E42
  |                                   |
  | Main parasite code (P.CODE)       |
  |                                   |
  +-----------------------------------+   &1000 = Parasite variables
  |                                   |
  | elite-universe-editor-1.asm       |
  |                                   |
  +-----------------------------------+   &0E3C
  |                                   |
  | WP workspace                      |
  |                                   |
  +-----------------------------------+   &0D00 = WP
  .                                   .
  .                                   .
  .                                   .
```

### Snippet Codice (BASIC)

```basic
.                                   .
  .                                   .
  .                                   .
  |                                   |
  +-----------------------------------+   &7E00
  |                                   |
  | Memory for the split-screen mode  |
  |                                   |
  +-----------------------------------+   &4000
  |                                   |
  | elite-universe-editor-z.asm       |
  |                                   |
  +-----------------------------------+   &3D36
  |                                   |
  | Main I/O code (I.CODE)            |
  |                                   |
  +-----------------------------------+   &2300 = TABLE
  |                                   |
  .                                   .
  .                                   .
  .                                   .
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
+-----------------------------------+   &FFFF
  |                                   |
  | Machine Operating System (MOS)    |
  |                                   |
  +-----------------------------------+   &C000
  |                                   |
  | elite-universe-editor-1, 2, 4.asm |
  |                                   |
  +-----------------------------------+   &B200
  |                                   |
  | Text tokens, sin/cos tables       |
  |                                   |
  +-----------------------------------+   &A000 = QQ18
  |                                   |
  | elite-universe-editor-z.asm       |
  |                                   |
  +-----------------------------------+   &9D94
  |                                   |
  | Ship blueprints (SHIPS.bin)       |
  |                                   |
  +-----------------------------------+   &8000 = XX21
  |                                   |
  | elite-universe-editor-3.asm       |
  |                                   |
  +-----------------------------------+   &7F48
  |                                   |
  | Main game code (BCODE.bin)        |
  |                                   |
  +-----------------------------------+   &1300 = TVT3
  |                                   |
  .                                   .
  .                                   .
  .                                   .
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
1 = CheckShiftCtrl to endUniverseEditor1 = &0E3C to &0FD9 = &019E =  414
  2 = UniverseEditor to endUniverseEditor2 = &6E42 to &7383 = &0542 = 1346
  3 = SaveLoadFile   to endUniverseEditor3 = &8191 to &81EF = &005F =   95
      prgAddress                           = &81FE to &81FF = &0002 =    2
  4 = UpdateChecksum to endUniverseEditor4 = &F102 to &F7E5 = &06E4 = 1764
  z = rowOffsets     to endUniverseEditorZ = &3D36 to &3E87 = &0152 =  338

                                            Total code size = &0F77 = 3959
```

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`Block`** (unknown): No description available

```assembly
Block end address    Maximum value   Actual value    Free space
  -----------------    -------------   ------------    ----------
  endUniverseEditor1       &1000           &0FD9         38 bytes
  endUniverseEditor2       &738D           &7383          9 bytes
  endUniverseEditor3       &81FE           &81EF         14 bytes
  endUniverseEditor4       &F800           &F7E5         26 bytes
  endUniverseEditorZ       &4000           &3E87        376 bytes
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
1 = CheckShiftCtrl to endUniverseEditor1 = &B200 to &B3CE = &01CF =  463
  2 = UniverseEditor to endUniverseEditor2 = &B3CF to &B8F1 = &0523 = 1315
  3 = SaveLoadFile   to endUniverseEditor3 = &7F4F to &7FFF = &00B1 =  177
  4 = UpdateChecksum to endUniverseEditor4 = &B8F2 to &BFF4 = &0703 = 1795
  z = rowOffsets     to endUniverseEditorZ = &9D95 to &9F1A = &0186 =  390

                                            Total code size = &102C = 4140
```

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`Block`** (unknown): No description available

```assembly
Block end address    Maximum value   Actual value    Free space
  -----------------    -------------   ------------    ----------
  endUniverseEditor3       &8000           &7FFF          0 bytes
  endUniverseEditor4       &C000           &BFF4         11 bytes
  endUniverseEditorZ       &9FFF           &9F1A        228 bytes
```



---
*Fonte originale: [https://elite.bbcelite.com/hacks/elite_universe_editor_technical_information.html](https://elite.bbcelite.com/hacks/elite_universe_editor_technical_information.html)*

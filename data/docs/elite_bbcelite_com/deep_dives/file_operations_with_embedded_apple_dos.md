---
title: File operations with embedded Apple DOS
source_url: https://elite.bbcelite.com/deep_dives/file_operations_with_embedded_apple_dos.html
category: source-code
topics:
- basic
- assembly
difficulty: beginner
language: mixed
hardware:
- CPU
- SID
- KERNAL
- CIA
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

# File operations with embedded Apple DOS

## Saving and loading commander files with a customised version of DOS 3.3

Just like all the other versions of Elite on the 6502, the Apple II version of Elite was written by Ian Bell and David Braben... and just like all the other non-Acorn versions that they wrote, they didn't do it entirely alone. Tucked away inside the cover of the Apple version's Space Trader's Flight Training Manual is this credit:

Technical Assistance by Rob Northan


They may have spelled his name incorrectly, but this is the same Rob Northen who was responsible for the devious copy protection system in the original BBC Micro version of Elite. So what did he contribute to Apple II Elite?

Luckily there's a pretty big clue in the source code, at the top of the [A.ELITEJ](https://github.com/markmoxon/elite-source-code-apple-ii/blob/main/1-source-files/original-sources/A.ELITEJ.TXT) source file:

30REM ELITE <J> AP / Apple DOS 1.00 from Rob Northen

This source file contains the code to load and save commander files... and there is an awful lot of it, too. So let's take a look at this contribution, because it turns out that Rob Northen wasn't working alone either.

## Apple DOS

													 ---------

						Putting the Apple II version to one side for a minute, Elite on the 6502 typically contains pretty terse file-related code.

For example, the Acorn versions all use the operating system's built-in OSFILE routine to load and save files, which involves little more than setting up a small data block containing the file details and passing the address of this block to OSFILE. The operating system takes care of everything else, and the resulting code is nice and simple: for example, the [LOD](https://elite.bbcelite.com/cassette/main/subroutine/lod.html) and [QUS1](https://elite.bbcelite.com/cassette/main/subroutine/qus1.html) routines in the BBC Micro cassette version load a commander file and move it to the correct location in memory, all in a few instructions, and the same approach works for the disc-based versions too.

The Commodore 64 code is similarly snappy, and it uses the Kernal's SETLFS, SETNAM, LOAD and SAVE functions in a comparable fashion. And the NES version doesn't even bother with saving or loading - it just copies the commander file into battery-backed RAM in the cartridge, and that's it.

The Apple II does things a little differently, to put it mildly. At launch, the Apple II only supported cassettes for loading and saving files; this was 1977, and floppy disks were a prohibitively expensive technology. This led to one of the most impressive developments in the early history of computing, when Steve Wozniak created the Disk II Interface card.

Designed with just eight simple chips, this groundbreaking board changed the rules by shifting the complexity of contemporary disk interfaces from hardware into software. The interface itself was brilliantly simple and worked with a disk drive with all the control electronics removed, so the hardware cost was tiny compared to the other disk systems on the market. This was because all the heavy lifting had been moved into the supporting software that ran on the Apple II - software called Apple DOS.

To be honest, I can't do this story justice, so if you want to bask in the brilliance of Woz's design and why it was so astonishing, I recommend you read this [excellent article from Big Mess o' Wires](https://www.bigmessowires.com/2021/11/12/the-amazing-disk-ii-controller-card/). Just be warned - this is a rabbit hole that it's difficult to emerge from!

Apple DOS itself is an epic bit of coding. At its heart is a set of low-level routines called the "read/write track-sector" routines, or RWTS for short; and sitting on top of these routines is a user interface that lets you enter disk commands such as BSAVE or CATALOG. The RWTS routines were written by Steve Wozniak and Randy Wigginton during the Christmas holidays in 1977, and they formed the basis for the first demos in early 1978; Paul Laughton then wrote what would become Apple DOS on top of these low-level routines. If you want to know more, the Computer History Museum has [released the sources for everyone to play with](https://computerhistory.org/blog/apple-ii-dos-source-code/), along with a great summary of the development history of DOS.

Apple DOS is very much a disk-based product, and every DOS disk contains a copy of the Apple DOS routines. The Disk II Interface contains a tiny 251-byte program that loads the first bit of DOS from disk, and then this in turn loads the rest of DOS into memory. It's an involved process that's nicely described in the [Big Mess o' Wires article](https://www.bigmessowires.com/2021/11/12/the-amazing-disk-ii-controller-card/), but if you're really interested in how this works, I can highly recommend the go-to reference on the subject, in the form of the [Beneath Apple DOS](https://archive.org/details/beneath-apple-dos-2020/) book.

This approach of loading DOS from disk differs considerably from the BBC Micro and Commodore 64. On the BBC Micro, the disc interface contains a powerful 8271 or 1770 controller chip and the Disc Filing System (DFS) lives in a separate ROM, while the 1541 disk drive for the Commodore 64 plugs into the machine's IEEE-488 serial port and is powered by the drive's own dedicated 6502 CPU, which has its own on-board disk controller and disk operating system. In both cases that's a lot more hardware than with the Apple II, so there's no need to load DOS into memory, as it's already present in ROM.

Let's see what Apple DOS means for Elite.

## Embedded Apple DOS

													 ------------------

						When a floppy disk that has been formatted and initialised is put into an Apple II disk drive, the first thing that happens is that DOS gets loaded into memory. When it's fully loaded, DOS consumes quite a bit of space. According to the memory map in chapter 5 of Beneath Apple DOS, it grabs the whole block from $9600 to $BFFF, inserting itself just below I/O memory at $C000.

This is what it looks like once everything is loaded:

: : : : +-----------------------------------+ $C100 | | | I/O memory | | | +-----------------------------------+ $C000 | | | RWTS | | | +-----------------------------------+ $B600 | | | File manager | | | +-----------------------------------+ $AAC9 | | | Main DOS routines | | | +-----------------------------------+ $9D00 | | | DOS file buffers | | | +-----------------------------------+ $9600 : : : :

This is quite a big memory footprint: it's 10.5K of RAM, to be exact, which is a significant chunk of memory in a 48K machine. Elite uses almost all of that 48K when it's loaded, so there's no way that Elite and DOS can co-exist in the same machine - see the [Apple II Elite memory map](https://elite.bbcelite.com/the_elite_memory_map_apple_ii.html) for details. Something has to give, and it isn't going to be Elite.
						

The solution is to ignore this 10.5K version of DOS once it has loaded the game loader from disk. If we don't call any more DOS routines or use any more DOS commands after this point, then the DOS code will never be run and we can use the memory from $9600 to $BFFF for Elite.

But if we decide to ignore DOS, how does the game loader load the game binaries, and how do we then load and save commander files when the game is running? The answer is to embed a cut-down version of DOS within both the game loader and the main game binary, and this is the "Apple DOS 1.0" that Rob Northen wrote for the game. You can see his code in the [game loader source](https://elite.bbcelite.com/apple/all/loader.html) and the [Elite J source](https://elite.bbcelite.com/apple/all/elite_j.html), so let's look at what's involved.

The disk routines in Apple II Elite fall into two categories. First, there's a set of routines by Rob Northen that let us examine the disk catalog and free space map to work out how to save and load commander files; and second, there's a copy of the RWTS routines from Apple DOS 3.3, with only minor changes from the official release of DOS, that do the low-level disk access. Rob Northen's code calls the relevant RWTS routines when it needs to read or write a disk sector, and because the RWTS code in Elite is self-contained and only contains the essentials, it looks after the DOS aspects and we can simply ignore the DOS code that loaded the original game and can overwrite it with game code.

The result takes up a lot less memory than the 10.5K of standard DOS. Indeed, the combined memory footprint of Rob Northen's code and the RWTS routines comes to just under 1.5K, and Elite saves even more memory by storing the DOS file buffers at K%, sharing space with the ship data blocks. We can do this because we only ever do disk operations when saving or loading commander files, and we only do that when we're docked, at which point there are no ships in the local bubble that need data blocks. It's all very efficient, and it enables Elite to enjoy the required functionality from Apple DOS but without taking a huge memory hit.

It also means that Apple II Elite contains a whole chunk of code that was written by Steve Wozniak and Randy Wigginton, right there in the game binary. It's in the second part of the main game, which is on the final game disk in the form of the ELA file. So the ELA file in Firebird Elite contains code by Ian Bell, David Braben, Steve Wozniak, Randy Wigginton and Rob Northen, all in the same file. I mean, just how many coding heroes can you fit into one place? It's giddy stuff.

## The disk routines

													 -----------------

						Here are the details of all the major disk routines and lookup variables in Apple II Elite.

The first table below shows all the low-level RWTS routines that have been included from Apple DOS 3.3, in the order in which they appear in the Elite source. The table also shows the equivalent routine name in DOS, and if you click the Elite routine name to see the commented code, you'll see I've included the original source code from Apple DOS 3.3 alongside the version in the Elite source code. This includes all the original Wozniak/Wigginton commentary, so you can see exactly how the two versions match up.

For reference, you can also see the original DOS routines in the [Apple II DOS 3.3 C Source Code Listing](https://elite.bbcelite.com/pdfs/apple2_SRC_DOS33C_1983.pdf) PDF. Note that the rtable variable in Elite maps to an unlabelled table in DOS at address $3A96, which can be found on page 99 of the source listing PDF, just after the PD2 label.

| Routine | Description | DOS routine | 
|---|---|---|
| [wtable](https://elite.bbcelite.com/apple/main/variable/wtable.html) | 6-bit to 7-bit nibble conversion table | NIBL | 
| [rwts](https://elite.bbcelite.com/apple/main/subroutine/rwts.html) | Read or write a specific sector | RWTS | 
| [trytrk](https://elite.bbcelite.com/apple/main/subroutine/trytrk.html) | Try finding a specific track on the disk | TRYTRK | 
| [rdrght](https://elite.bbcelite.com/apple/main/subroutine/rdrght.html) | Check that this is the correct track | RDRIGHT | 
| [read](https://elite.bbcelite.com/apple/main/subroutine/read.html) | Read a sector's worth of data into the buffr2 buffer | READ16 | 
| [write](https://elite.bbcelite.com/apple/main/subroutine/write.html) | Write a sector's worth of data from the buffr2 buffer to the current track and sector | WRITE16 | 
| [rdaddr](https://elite.bbcelite.com/apple/main/subroutine/rdaddr.html) | Read a track address field | RDADR16 | 
| [seek](https://elite.bbcelite.com/apple/main/subroutine/seek.html) | Fast seek routine | SEEK | 
| [armwat](https://elite.bbcelite.com/apple/main/subroutine/armwat.html) | Implement the arm move delay | MSWAIT | 
| [armtab](https://elite.bbcelite.com/apple/main/variable/armtab.html) | Phase-on time table in 100-usec intervals | ONTABLE | 
| [armtb2](https://elite.bbcelite.com/apple/main/variable/armtb2.html) | Phase-off time table in 100-usec intervals | OFFTABLE | 
| [prenib](https://elite.bbcelite.com/apple/main/subroutine/prenib.html) | Convert 256 8-bit bytes in buffer into 342 6-bit nibbles in buffr2 | PRENIB16 | 
| [pstnib](https://elite.bbcelite.com/apple/main/subroutine/pstnib.html) | Convert 342 6-bit nibbles in buffr2 into 256 8-bit bytes in buffer | POSTNB16 | 
| [wbyte](https://elite.bbcelite.com/apple/main/subroutine/wbyte.html) | Write one byte to disk | WNIBL9 | 
| [scttab](https://elite.bbcelite.com/apple/main/variable/scttab.html) | Lookup table to translate logical (requested) sector number to physical sector number | INTRLEAV | 
| [rtable](https://elite.bbcelite.com/apple/main/variable/rtable.html) | 64 disk nibbles of "6-and-2" Read Translate Table | $3A96 | 

The second table below shows the high-level routines by Rob Northen, again in the order in which they appear in the Elite source.

These routines mainly deal with the structure of data on the disk, and specifically the Virtual Table of Contents (VTOC), the catalog sector, file entries and the track/sector lists. These routines implement tasks like searching the disk for free space or finding existing files in the catalog. They call the RWTS routines above when they need to access the disk itself.

| Routine | Description | 
|---|---|
| [diskerror](https://elite.bbcelite.com/apple/main/subroutine/diskerror.html) | Print a disk error, make a beep and wait for a key press | 
| [rfile](https://elite.bbcelite.com/apple/main/subroutine/rfile.html) | Read a commander file from a DOS disk into the buffer | 
| [wfile](https://elite.bbcelite.com/apple/main/subroutine/wfile.html) | Write a commander file from the buffer to a DOS disk | 
| [findf](https://elite.bbcelite.com/apple/main/subroutine/findf.html) | Search the disk catalog for an existing file | 
| [finde](https://elite.bbcelite.com/apple/main/subroutine/finde.html) | Search the disk catalog for an empty file entry | 
| [rentry](https://elite.bbcelite.com/apple/main/subroutine/rentry.html) | Search the disk catalog for an existing file or an empty file entry | 
| [getsct](https://elite.bbcelite.com/apple/main/subroutine/getsct.html) | Analyse the VTOC sector to allocate one free sector | 
| [isfull](https://elite.bbcelite.com/apple/main/subroutine/isfull.html) | Check the disk to ensure there are least two free sectors, one for the file's track/sector list and one for the file's contents | 
| [gettsl](https://elite.bbcelite.com/apple/main/subroutine/gettsl.html) | Read a file's track/sector list | 
| [rvtoc](https://elite.bbcelite.com/apple/main/subroutine/rvtoc.html) | Read the VTOC sector into the buffer | 
| [rsect](https://elite.bbcelite.com/apple/main/subroutine/rsect.html) | Read a specific sector from disk into the buffer | 
| [wsect](https://elite.bbcelite.com/apple/main/subroutine/wsect.html) | Write a specific sector from the buffer to disk | 
| [prterr](https://elite.bbcelite.com/apple/main/subroutine/prterr.html) | Return from the RWTS code with a "Disk write protected" error | 
| [rttrk](https://elite.bbcelite.com/apple/main/subroutine/rttrk.html) | Read or write a sector on the current track | 
| [drverr](https://elite.bbcelite.com/apple/main/subroutine/drverr.html) | Return from the RWTS code with a "Disk I/O error" | 
| [rttrk3](https://elite.bbcelite.com/apple/main/subroutine/rttrk3.html) | Successfully return from the RWTS code with no error reported | 

Together, these routines form the save and load system in Apple II Elite. Compared to the simple operating system calls in the other versions of Elite, they are really quite involved, but that's the Apple II for you; more than any other system that runs Elite, you have to get really involved in programming the low-level hardware.

It's an absolute delight, and analysing this code lets us rub shoulders with the giants of the 1970s home computer revolution... even if it's a bit closer to the bare metal than most of us are used to.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
30REM ELITE <J>  AP   /  Apple DOS 1.00 from Rob Northen
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
:                                   :
  :                                   :
  +-----------------------------------+   $C100
  |                                   |
  | I/O memory                        |
  |                                   |
  +-----------------------------------+   $C000
  |                                   |
  | RWTS                              |
  |                                   |
  +-----------------------------------+   $B600
  |                                   |
  | File manager                      |
  |                                   |
  +-----------------------------------+   $AAC9
  |                                   |
  | Main DOS routines                 |
  |                                   |
  +-----------------------------------+   $9D00
  |                                   |
  | DOS file buffers                  |
  |                                   |
  +-----------------------------------+   $9600
  :                                   :
  :                                   :
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/file_operations_with_embedded_apple_dos.html](https://elite.bbcelite.com/deep_dives/file_operations_with_embedded_apple_dos.html)*

---
title: Music in Commodore 64 Elite
source_url: https://elite.bbcelite.com/deep_dives/music_in_commodore_64_elite.html
category: source-code
topics:
- basic
- sound generation
- raster interrupts
- assembly
difficulty: advanced
language: mixed
hardware:
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

# Music in Commodore 64 Elite

## The music driver behind the iconic Blue Danube and the catchy Elite Theme

There is one aspect of Commodore 64 Elite that people seem to remember more fondly than anything else. It's The Blue Danube, which plays when you engage your docking computer in Commodore 64 Elite.

![A screenshot of the docking computer in Commodore 64 Elite](https://elite.bbcelite.com/images/c64/docking_computer.png) 

						This feature alone makes the Commodore 64 conversion a really special update of the original; it's a sublime merging of 2001: A Space Odyssey and 1980s home computing, all wrapped up in the unique tones of the amazing SID sound synthesiser chip that makes the sound of the Commodore 64 so uniquely lush.

Let's take a look at how The Blue Danube - and the Elite Theme, which was added in a later release - work in Elite.

## Multiple developers

													 -------------------

						The source files for Commodore 64 Elite aren't exactly awash with comments, but the music driver does have some interesting information tucked into the start of the [BDirqhere](https://elite.bbcelite.com/c64/main/subroutine/bdirqhere.html) routine:

Music driver by Dave Dunn. BBC source code converted from Commodore disassembly extremely badly Jez. 13/4/85. Music system (c)1985 D.Dunn. Modified by IB,DB

The music system is one of the few parts of Commodore 64 Elite that wasn't written by Ian Bell or David Braben. The comments tell us that it's actually a modified version of a Commodore 64 music driver by Julie Dunn (née David), which was converted into BBC Micro-compatible assembly by Jez (Jez San) in April 1985, and modified by IB (Ian Bell) and DB (David Braben).

Julie Dunn composed and arranged a lot of computer music on the Commodore 64 in the mid-1980s. For a full list, here's a biography that includes a [list of games on which she worked](https://www.vgmpf.com/Wiki/index.php?title=Julie_Dunn).

Jez San was the main Commodore consultant on the conversion project, and he helped Bell and Braben get their heads around this non-Acorn system that they weren't familiar with. He was also part of the team behind the Programmer's Development System, which enabled the authors to develop the game on a BBC Micro rather than a Commodore 64 (see the deep dive on [developing Commodore 64 Elite on a BBC Micro](https://elite.bbcelite.com/developing_commodore_64_elite_on_a_bbc_micro.html) for details).

Most routines and variables in the converted driver code have names with the prefix "BD", which stands for Blue Danube. In the first Firebird release of Elite, only The Blue Danube was present; the ridiculously catchy Elite Theme that plays on the title screen was a later addition. Composed by Ian Bell's brother Aidan Bell and arranged by Julie Dunn, the Elite Theme uses the same file format and driver as The Blue Danube, but the "BD" prefix lives on in the source.

## Julie Dunn's music driver

													 -------------------------

						The driver itself is a relatively straightforward affair. We can start playing music by calling the [startbd](https://elite.bbcelite.com/c64/main/subroutine/startbd.html) routine, which first checks the music-related option variables to make sure everything is enabled and that we aren't already playing something. If nothing is playing and music is enabled, then the MUPLA variable gets set to $FF to indicate that we should now be playing music, and we call the [BDENTRY](https://elite.bbcelite.com/c64/main/subroutine/bdentry.html) routine to reset a few music-related variables and configure the SID chip.

The magic happens in the interrupt handler at [COMIRQ1](https://elite.bbcelite.com/c64/main/subroutine/comirq1.html). This routine is called twice during each screen refresh, as part of the split-screen implementation; specifically, it gets called when the raster reaches the top of the space view and again when it reaches the top of the dashboard (see the deep dive on [the split-screen mode in Commodore 64 Elite](https://elite.bbcelite.com/the_split-screen_mode_commodore_64.html) for details). If bit 7 of MUPLA is set, to indicate that music is playing, then on every other call, COMIRQ1 calls the music driver routine at [BDirqhere](https://elite.bbcelite.com/c64/main/subroutine/bdirqhere.html); this means the music driver is called once for each screen refresh, so that's 50 times a second on PAL systems and 60 times a second on NTSC systems.

Each call to the music driver routine sends the correct batch of music data to the SID chip for that clock tick. These batches are stored sequentially in two large blocks of music data, one for The Blue Danube and another for the Elite Theme. The interrupt routine keeps sending these batches of data to the SID, working through the music data as regular as clockwork, and the result is the background music that makes the Commodore 64 version of Elite so compelling.

Let's take a look at the format of these blocks of music data.

## The music data format

													 ---------------------

						So each tune is made up of sequential blocks of music data, with one block of data being sent to the SID chip by the interrupt routine on each screen refresh.

Each block of music data consists of a series of commands that get processed sequentially by the [BDirqhere](https://elite.bbcelite.com/c64/main/subroutine/bdirqhere.html) routine. Each command starts with a command number between #0 and #15, and most (but not all) commands take arguments. The music data is simply a sequence of these commands, where each command is stored as the command number followed by any arguments that command requires.

The commands are implemented using the jump tables in [BDJMPTBH](https://elite.bbcelite.com/c64/main/variable/bdjmptbh.html) and [BDJMPTBL](https://elite.bbcelite.com/c64/main/variable/bdjmptbl.html), which between them contain the addresses of the routines that correspond to each command. These routines send the appropriate data to the SID chip, as required, and are shown in the table below.

The commands are as follows:

| Command | Description | Routine | 
|---|---|---|
| <#0> | Do nothing and move on to the next command | n/a | 
| <#1 fh1 fl1> | Set the frequency for voice 1 to (fh1 fl1) and the control register for voice 1 to value1 | [BDRO1](https://elite.bbcelite.com/c64/main/subroutine/bdro1.html) | 
| <#2 fh2 fl2> | Set the frequency for voice 2 to (fh2 fl2) and the control register for voice 2 to value2 | [BDRO2](https://elite.bbcelite.com/c64/main/subroutine/bdro2.html) | 
| <#3 fh3 fl3> | Set the frequency for voice 3 to (fh3 fl3) and the control register for voice 3 to value3 | [BDRO3](https://elite.bbcelite.com/c64/main/subroutine/bdro3.html) | 
| <#4 fh1 fl1 fh2 fl2> | Set the frequencies and voice control registers for voices 1 and 2 | [BDRO4](https://elite.bbcelite.com/c64/main/subroutine/bdro4.html) | 
| <#4 fh1 fl1 fh2 fl2 fh3 fl3> | Set the frequencies and voice control registers for voices 1, 2 and 3 | [BDRO5](https://elite.bbcelite.com/c64/main/subroutine/bdro5.html) | 
| <#6> | Increment value0 and move on to the next command | [BDRO6](https://elite.bbcelite.com/c64/main/subroutine/bdro6.html) | 
| <#7 ad1 ad2 ad3 sr1 sr2 sr3> | Set the attack and decay length, sustain volume and release length for all three voices | [BDRO7](https://elite.bbcelite.com/c64/main/subroutine/bdro7.html) | 
| <#8> | Rest for value4 interrupts (i.e. return from the interrupt routine and play nothing for n/50 or n/60 of a second) | [BDRO8](https://elite.bbcelite.com/c64/main/subroutine/bdro8.html) | 
| <#9> | Restart the current tune | [BDRO9](https://elite.bbcelite.com/c64/main/subroutine/bdro9.html) | 
| <#10 h1 l1 h2 l2 h3 l3> | Set voice 1 pulse width to (h1 l1), voice 2 pulse width to (h2 l2), and voice 3 pulse width to (h3 l3) | [BDRO10](https://elite.bbcelite.com/c64/main/subroutine/bdro10.html) | 
| <#11> | Do command <#9> to restart the current tune | [BDRO11](https://elite.bbcelite.com/c64/main/subroutine/bdro11.html) | 
| <#12 n> | Set value4 = n, which sets the rest length for commands #8 and #15 | [BDRO12](https://elite.bbcelite.com/c64/main/subroutine/bdro12.html) | 
| <#13 v1 v2 v3> | Set value1, value2 and value3 to v1, v2 and v3, to use as the voice control register values in commands <#1>, <#2> and <#3> | [BDRO13](https://elite.bbcelite.com/c64/main/subroutine/bdro13.html) | 
| <#14 vf fc cf> | Set the volume and filter modes, filter control and filter cut-off frequency | [BDRO14](https://elite.bbcelite.com/c64/main/subroutine/bdro14.html) | 
| <#15> | Rest for 2 * value4 interrupts (i.e. return from the interrupt routine and play nothing for 2n/50 or 2n/60 of a second) | [BDRO15](https://elite.bbcelite.com/c64/main/subroutine/bdro15.html) | 

There are four variables associated with the music data, called value1 to value4, which can be set by commands #12 and #13. These values can then be used by other commands to set things like the rest length and voice control. There is also a variable value0 that can be incremented by command #6, but this variable is never set and is never read, so this command is effectively disabled in Elite.

There is one more important aspect of the music data: the command numbers are packed to take up less space. As command numbers are in the range 0 to 15, they can be stored as nibbles (i.e. four bits), so we can fit two commands into a single byte. Given a byte containing two command numbers, the command in the low nibble is processed first, followed by the command in the high nibble. Note that command arguments are always bytes, it's only the command numbers that are packed into nibbles.

## An example from The Blue Danube

													 -------------------------------

						This compression can make the music data a bit tricky to follow, so let's look at an example. The Blue Danube music data lives in the binary file C.COMUDAT on the source disk, which is included in the game binary using an INCBIN directive in the [COMUDAT](https://elite.bbcelite.com/c64/main/variable/comudat.html) variable.

If we look at the first few bytes of this file in a hex editor, it looks like this:

A7 26 26 48 29 29 AA 00 06 00 05 00 06 ED 21 21 41 1F F4 70 ...

We start with the first byte, $A7. Taking the low nibble first, i.e. $7, this means command #7, which is of the form <#7 ad1 ad2 ad3 sr1 sr2 sr3>. The arguments follow the command byte, so the first command is this:

<#7 26 26 48 29 29 AA>

This sets the attack and decay length, sustain volume and release length for all three voices; see the [BDRO7](https://elite.bbcelite.com/c64/main/subroutine/bdro7.html) routine for details on how the arguments correspond to the SID registers.

We then move on to the command in the high nibble of the first byte, i.e. $A. This means command #10, which is of the form <#10 h1 l1 h2 l2 h3 l3>, and we get the arguments from just after the arguments for the previous command, giving this command:

<#10 00 06 00 05 00 06>

This sets the pulse width for all three voices; see the [BDRO10](https://elite.bbcelite.com/c64/main/subroutine/bdro10.html) routine for details of how these values are sent to the SID chip.

We then move on to the next byte of music data, which follows the arguments for the last command (as we have now processed both nibbles in the first byte). The next byte is $ED, so again we pick the low nibble first, $D, to give command #13. This is of the form <#13 v1 v2 v3>, so we fetch the next three bytes to give this:

<#13 21 21 41>

This sets the value1, value2 and value3 variables to $21, $21 and $41 respectively, by calling the [BDRO13](https://elite.bbcelite.com/c64/main/subroutine/bdro13.html) routine.

Then we do the high nibble command, $E, which is <#14 vf fc cf>, so this gives us:

<#14 1F F4 70>

which sets the volume and filter modes, filter control and filter cut-off frequency, calling the [BDRO14](https://elite.bbcelite.com/c64/main/subroutine/bdro10.html) routine to send the data to the SID chip.

And then we move on to the next command byte, where we process the low nibble command and then the high nibble command, and this process continues until we reach either command #8 or command #15, at which point control is handed back to the interrupt handler (assuming there is a non-zero value in the value4 variable by this point). These commands set the rest counter to either value4 or 2 * value4, so if value4 is non-zero, this hands control back to the game and prevents any more commands being processed until the specified number of screen refreshes have passed.

At which point we start again with the next byte of music data, until the music is stopped by calling the [stopbd](https://elite.bbcelite.com/c64/main/subroutine/stopbd.html) routine, which zeroes MUPLA to stop the interrupt routine from processing any more data.

## PAL vs NTSC

													 -----------

						One final point to note is that the music plays at different speeds on PAL and NTSC machines. PAL machines refresh the screen at 50Hz (50 times a second), while NTSC machines refresh the screen at 60Hz (60 times a second). As we process music data in batches on every screen refresh, this means that NTSC machines work through the music data about 20% faster than the PAL machines, which means that The Blue Danube on NTSC machines plays about 20% faster than music on PAL machines.

Note that the pitch of the music is unchanged, so this isn't the same as running a tape at a higher speed - it's only the tempo that is faster, while all the notes and frequencies remain the same.

For an explanation of all the difference between the PAL and NTSC versions of the Commodore 64, check out this [excellent summary](http://unusedino.de/ec64/technical/misc/vic656x/pal-ntsc.html).

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
Music driver by Dave Dunn.

  BBC source code converted from Commodore disassembly extremely badly
  Jez. 13/4/85.

  Music system (c)1985 D.Dunn.
  Modified by IB,DB
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
A7 26 26 48 29 29 AA 00 06 00 05 00 06 ED 21 21 41 1F F4 70 ...
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
<#7 26 26 48 29 29 AA>
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
<#10 00 06 00 05 00 06>
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
<#13 21 21 41>
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
<#14 1F F4 70>
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/music_in_commodore_64_elite.html](https://elite.bbcelite.com/deep_dives/music_in_commodore_64_elite.html)*

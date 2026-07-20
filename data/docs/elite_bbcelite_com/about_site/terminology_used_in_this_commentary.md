---
title: Terminology used in this commentary
source_url: https://elite.bbcelite.com/about_site/terminology_used_in_this_commentary.html
category: source-code
topics:
- basic
- assembly
- sprite programming
- input handling
difficulty: beginner
language: mixed
hardware:
- KERNAL
- SID
- CPU
- CIA
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

# Terminology used in this commentary

There's a lot to explain in Elite, and some of it is pretty challenging stuff. Before getting stuck in, it's probably wise to take a brief look at some of the terminology I've used in this commentary.

Let's start with some general terms.

- Given a number X, ~X is the number with all the bits inverted.
- Given a number A, |A| is the absolute of that number - i.e. the number with no sign, or just the magnitude of the number.
- Given a multi-byte number, (S R) say, the absolute would be written |S R| (see below for more on multi-byte numbers and terminology).
- Coordinates are shown as (x, y) for screen coordinates and (x, y, z) for 3D coordinates in the outside world, so the centre of the space view is at screen coordinate (128, 96), while our trusty Cobra Mk III is at space coordinates (0, 0, 0).
- Vectors and matrices are enclosed in square brackets, like this:
[ 1 0 0 ] [ x ] [ 0 1 0 ] or [ y ] [ 0 0 -1 ] [ z ] We might sometimes write a column vector as [x y z] instead, just to save space, but it means the same thing as the vertical version.
- As Elite started out on the BBC Micro and Acorn Electron, the original source code uses Acorn's BBC BASIC syntax, so hexadecimal values are shown using ampersands (such as &FE05) and comments start with the '\' backslash character. When talking specifically about other platforms, such as the NES, Apple II or Commodore 64, hexadecimal values are shown using dollars (such as $FE05), and comments start with the ';' semicolon character.

We also need some terminology for multi-byte numbers, but that needs its own section, particularly as Elite has quite a few variations on this theme.

## Multi-byte numbers

						                             ------------------

						Not surprisingly, Elite deals with some pretty big numbers. For example, the cash reserves are stored as big-endian 32-bit numbers, space coordinates are stored as 24-bit sign-magnitude little-endian numbers, and the joystick gives us two's complement signed 16-bit numbers. When you only have the 8-bit bytes of 6502 assembly language to play with, things can get confusing, and quickly.

First, let's recap some basic definitions, so we're all on the same page.

- Big-endian numbers store their most significant bytes first, then the least significant bytes. This is how humans tend to write numbers.
- Little-endian numbers store the least significant bytes first then the most significant ones. The 6502 stores its addresses in little-endian format, as do the EQUD and EQUW operatives, for example.
- Sign-magnitude numbers store their sign in their highest bit, and the rest of the number contains the magnitude of the number (i.e. the number without the sign). You can change the sign of a sign-magnitude number by simply flipping the highest bit (bit 7 in an 8-bit sign-magnitude number, bit 15 in a 16-bit sign-magnitude number, and so on). See below for more on sign-magnitude numbers.
- Two's complement numbers, meanwhile, are the mainstay of 6502 assembly language, and instructions like ADC and SBC are designed to work with both negative and positive two's complement numbers without us having to worry about a thing. They also have a sign bit in the highest bit, but negative numbers have their bits flipped compared to positive numbers. To flip the sign of a number in two's complement, you flip all the bits and add 1.

Elite uses a smorgasbord of all these types, and it can get pretty confusing. Given this, let's agree on some terminology to make it easier to talk about multi-byte numbers and how they are stored in memory.

If we have three bytes called x_sign, x_hi and x_lo, which contain a 24-bit sign-magnitude number, with the highest byte in x_sign and the lowest in x_lo, then we can refer to their 24-bit number like this:

(x_sign x_hi x_lo)

To take this one further, if we have four bytes called xCoordTop, xCoordHi, xCoordLo and xCoordBot which between them contain a 32-bit number with the highest byte in xCoordTop and the lowest in xCoordBot, then we can refer to the 32-bit number like this:

(xCoordTop xCoordHi xCoordLo xCoordBot)

or we can shorten it even more, like this:

xCoord(Top Hi Lo Bot)

In this terminology, the most significant byte is always written first, irrespective of how the bytes are stored in memory. So, we can talk about 16-bit numbers made up of registers:

(X Y)

So here X is the high byte and Y the low byte. Or here's a 24-bit number made up of a mix of registers and memory locations:

(A S S+1)

Again, the most significant byte is on the left, so that's the accumulator A, then the next most significant is in memory location S, and the least significant byte is in S+1.

Or we can even talk about numbers made up of registers, memory locations and constants, like this 24-bit number:

(A P 0)

or this constant, which stores 590 in a 32-bit number:

(2 78)

Just remember that in every case, the high byte is on the left, and the low byte is on the right.

When talking about numbers in sequential memory locations, we can use another shorthand. Consider this little-endian number:

(K+3 K+2 K+1 K)

where a 32-bit little-endian number is stored in memory locations K (low byte) through to K+3 (high byte). We can also refer to this number like this:

K(3 2 1 0)

Or a big-endian number stored in XX15 through XX15+3 would be:

XX15(0 1 2 3)

where XX15 is the most significant byte and XX15+3 the least significant. We could also refer to the little-endian 16-bit number stored in the X-th byte of the block at XX3 with:

XX3+X(1 0)

To take this even further, if we want to add another significant byte to the 32-bit number K(3 2 1 0) to make a five-byte, 40-bit number - an overflow byte in a memory location called S, say - then we might talk about:

K(S 3 2 1 0)

or even something like this:

XX15(4 0 1 2 3)

which is a five-byte number stored with the highest byte in XX15+4, then the next most significant in XX15, then XX15+1 and XX15+2, through to the lowest byte in XX15+3. And yes, Elite does store one of its numbers like this - see the [BPRNT](https://elite.bbcelite.com/cassette/main/subroutine/bprnt.html) routine for the gory details.

With this terminology, it might help to think of the digits listed in the brackets as being written down in the same order that we would write them down as humans. The point of this terminology is to make it easier for people to read, after all.

## Sign-magnitude numbers

						                             ----------------------

						Many (but not all) of Elite's multi-byte numbers are stored as sign-magnitude numbers.

For example the x, y and z coordinates in bytes #0-8 of the ship data block in INWK and K% (which contain a ship's coordinates in space) are stored as 24-bit sign-magnitude numbers, where the sign of the number is stored in bit 7 of the sign byte, and the other 23 bits contain the magnitude of the number without any sign (i.e. the absolute value, |x|, |y| or |z|). So an x value of &123456 would be stored like this:

```
     x_sign          x_hi          x_lo
  +     &12           &34           &56
  0 0010010      00110100      01010110
```
						while -&123456 is identical, just with bit 7 of the x_sign byte set:

```
     x_sign          x_hi          x_lo
  -     &12           &34           &56
  1 0010010      00110100      01010110
```
						There are also sign-magnitude numbers where the sign byte is only ever used for storing the sign bit, and bits 0-6 are ignored, and there are others where we only ever care about the top byte (a planet's distance, for example, is determined by the value of x_sign, y_sign and z_sign, for example). But they all work in exactly the same way.

## Label names in the Acornsoft and Firebird versions

						                             --------------------------------------------------

						For those versions of Elite where the original source code is available, I have used the same label names in the code on this site. This applies to the BBC Micro cassette, 6502 Second Processor, Commodore 64 and Apple II versions, for which Ian Bell has released the source code on his website.

There are only three exceptions: LABEL_1, LABEL_2 and LABEL_3, which respectively appear in the original source code as `_ (a backtick followed by an underscore), ` (a backtick), and `` (two backticks). Backticks don't compile in BeebAsm and are pretty cryptic, so I've used the LABEL_n terminology from the cassette version instead.

Also, the original code redefines a handful of labels so they appear twice, which is legal in the BBC BASIC assembler. However BeebAsm does not allow labels to be redefined, so I have appended a 'K' to one of the labels to prevent errors. The new labels are [MUL6K](https://elite.bbcelite.com/disc/docked/subroutine/unused_duplicate_of_multu.html#mul6k) (BBC cassette, BBC disc, Electron, 6502SP), [PDL1K](https://elite.bbcelite.com/6502sp/main/subroutine/pdesc.html#pdl1k) (all enhanced versions) and [TT223K](https://elite.bbcelite.com/6502sp/main/subroutine/tt219.html#tt223k) (6502SP, Master, Commodore 64, Apple II).

For those versions where the original source code is not available, we don't know the original label names for code that doesn't already appear in any of the known sources. In these cases I have either invented my own labels, or I've reused labels from pre-existing disassemblies. Here are the details:

- For the BBC Master Compact version, these are the labels I've added: [CTRLmc](https://elite.bbcelite.com/master/main/subroutine/ctrlmc.html),[DFIRE](https://elite.bbcelite.com/master/main/subroutine/rdfire.html#dfire),[DIG1](https://elite.bbcelite.com/master/main/subroutine/rdjoy.html#dig1),[DIG2](https://elite.bbcelite.com/master/main/subroutine/rdjoy.html#dig2),[DIGITAL](https://elite.bbcelite.com/master/main/subroutine/rdjoy.html#digital),[DIRI](https://elite.bbcelite.com/master/main/variable/diri.html),[DIRL](https://elite.bbcelite.com/master/main/subroutine/gtdir.html#dirl),[DJOY](https://elite.bbcelite.com/master/main/subroutine/djoy.html),[DKS4mc](https://elite.bbcelite.com/master/main/subroutine/dks4mc.html),[GTDIR](https://elite.bbcelite.com/master/main/subroutine/gtdir.html),[MOS](https://elite.bbcelite.com/master/main/workspace/zp.html#mos),[NMI](https://elite.bbcelite.com/master/main/workspace/wp.html#nmi),[NMICLAIM](https://elite.bbcelite.com/master/main/subroutine/nmiclaim.html),[NMIRELEASE](https://elite.bbcelite.com/master/main/subroutine/nmirelease.html),[noshift](https://elite.bbcelite.com/master/main/subroutine/mt26.html#noshift),[RDFIRE](https://elite.bbcelite.com/master/main/subroutine/rdfire.html),[RDJOY](https://elite.bbcelite.com/master/main/subroutine/rdjoy.html),[RETURN](https://elite.bbcelite.com/master/main/subroutine/return.html),[RRNEW](https://elite.bbcelite.com/master/main/subroutine/chpr.html#rrnew),[SHIFT](https://elite.bbcelite.com/master/main/subroutine/shift.html),[TT171](https://elite.bbcelite.com/master/main/subroutine/tt17x.html#tt171)and[TT17X](https://elite.bbcelite.com/master/main/subroutine/tt17x.html).
- For the BBC Master version, these are the labels I've added: [DELL1K](https://elite.bbcelite.com/master/main/subroutine/wscan.html#dell1k)(for the duplicated DELL1 label),[EE3K](https://elite.bbcelite.com/master/main/subroutine/clyns.html#ee3k)(for the duplicated EE3 label),[OUTK](https://elite.bbcelite.com/master/main/subroutine/outk.html)and[TT67K](https://elite.bbcelite.com/master/main/subroutine/tt67k.html)(for the duplicated TT67 routine). Also, I have retained the[GVL](https://elite.bbcelite.com/master/main/subroutine/gvl.html)label from the cassette version for clarity, even though it is omitted in the original Master source.
- For the Acorn Electron version, these are the labels I've added: [BORDER](https://elite.bbcelite.com/electron/main/subroutine/ttx66.html#border),[CAPSL](https://elite.bbcelite.com/electron/main/subroutine/dks4.html#capsl),[DELY1](https://elite.bbcelite.com/electron/main/subroutine/delay.html#dely1),[DELY2](https://elite.bbcelite.com/electron/main/subroutine/delay.html#dely2),[DELY3](https://elite.bbcelite.com/electron/main/subroutine/delay.html#dely3),[KEY1](https://elite.bbcelite.com/electron/main/subroutine/key1.html),[KEYB](https://elite.bbcelite.com/electron/main/workspace/s_per_cent_part_1_of_2.html#keyb),[KSCAN](https://elite.bbcelite.com/electron/main/subroutine/dks4.html#kscan),[LOOKL](https://elite.bbcelite.com/electron/main/subroutine/tt102.html#lookl),[MDIALS](https://elite.bbcelite.com/electron/main/variable/mdials.html),[NEXTR](https://elite.bbcelite.com/electron/main/subroutine/nextr.html),[SFX2](https://elite.bbcelite.com/electron/main/variable/sfx.html#sfx2),[SFXDU](https://elite.bbcelite.com/electron/main/workspace/wp.html#sfxdu),[SFXL](https://elite.bbcelite.com/electron/main/subroutine/main_flight_loop_part_1_of_16.html#sfxl),[SFXPR](https://elite.bbcelite.com/electron/main/workspace/wp.html#sfxpr)and[VKEYS](https://elite.bbcelite.com/electron/main/subroutine/tt102.html#vkeys).
- For the BBC Micro disc version, these are the labels I've added (most of which are the same as in Paul Brink's disassembly): [CPIR](https://elite.bbcelite.com/disc/flight/workspace/wp.html#cpir),[DK9](https://elite.bbcelite.com/disc/docked/subroutine/dk4.html#dk9),[DOBEGIN](https://elite.bbcelite.com/disc/docked/subroutine/dobegin.html),[eny1](https://elite.bbcelite.com/disc/docked/subroutine/tt110.html#eny1),[GTNMES](https://elite.bbcelite.com/disc/docked/subroutine/gtnmes.html),[hloop](https://elite.bbcelite.com/disc/docked/subroutine/has1.html#hloop),[INBAY](https://elite.bbcelite.com/disc/flight/subroutine/inbay.html),[LTLI](https://elite.bbcelite.com/disc/flight/variable/ltli.html),[modify](https://elite.bbcelite.com/disc/docked/subroutine/res2.html#modify),[more](https://elite.bbcelite.com/disc/flight/subroutine/main_game_loop_part_4_of_6.html#more),[nroll](https://elite.bbcelite.com/disc/flight/subroutine/tactics_part_7_of_7.html#nroll),[nroll2](https://elite.bbcelite.com/disc/flight/subroutine/tactics_part_7_of_7.html#nroll2),[PROT4](https://elite.bbcelite.com/disc/loader_3/subroutine/prot4.html),[RRNEW](https://elite.bbcelite.com/disc/docked/subroutine/chpr.html#rrnew),[RSHIPS](https://elite.bbcelite.com/disc/flight/subroutine/rships.html),[SCANCOL](https://elite.bbcelite.com/disc/flight/subroutine/scancol.html),[SCRAM](https://elite.bbcelite.com/disc/docked/subroutine/scram.html),[SHIPI](https://elite.bbcelite.com/disc/flight/variable/shipi.html),[SHIPinA](https://elite.bbcelite.com/disc/flight/subroutine/lomod.html#shipina),[tiwe](https://elite.bbcelite.com/disc/docked/subroutine/title.html#tiwe),[TJe](https://elite.bbcelite.com/disc/docked/subroutine/tt17.html#tje)and[TPnot8](https://elite.bbcelite.com/disc/flight/subroutine/lomod.html#tpnot8).
- For the Commodore 64 version, these are the labels I've added (for the code that was added to the Firebird versions): [THEME](https://elite.bbcelite.com/c64/main/variable/comudat.html#theme)and[MUDOCK](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#mudock). I have also used P2 to T2 for the P to T variables in the line-drawing code, as the original source redefines those labels, and this isn't possible in BeebAsm. For the firebird and gma1-3 disk loaders and the send utility, all the labels have been added by me, as the source code for these is not available.
- For the Apple II version, I have added this label (for the code that was added to the Firebird version): [fireButtonMask](https://elite.bbcelite.com/apple/main/workspace/option_variables.html#firebuttonmask). For the loaders in the Firebird and Ian Bell game disk variants, all the labels have been added by me, as the source code for these is not available.
- For the sideways RAM variant of the BBC Micro disc version, all the labels in the [sideways RAM loader](https://elite.bbcelite.com/disc/all/loader_sideways_ram.html)have been added by me, apart from the entry point names which I've taken from the MENU program.
- For all versions, I have added labels to the ship blueprints, along the lines of [SHIP_SIDEWINDER](https://elite.bbcelite.com/cassette/main/variable/ship_sidewinder.html)and[SHIP_COBRA_MK_3_EDGES](https://elite.bbcelite.com/cassette/main/variable/ship_cobra_mk_3.html#ship_cobra_mk_3_edges). The original source doesn't use labels for the ship data, so I had to add my own.

All other labels should be the same as in the original sources.

## Label names in the NES version

						                             ------------------------------

						As the original source for NES Elite wasn't released until after I had done my commentary, I had to make up my own labels for the code that didn't already appear in the BBC Master version (and there's a lot of new code in the NES version!). My label names follow a number of rules:

- Subroutine names are in camel case with an initial capital letter, such as SubroutineLabel.
- Variable names are in camel case with an initial lower case letter, such as variableLabel (with the exception of temporary variables such as P and PP).
- Variables that refer to coordinates tend to start with the axis, such as xScreenCoord.
- Variables that refer to multi-byte values tend to end in Hi or Lo, such as xCoordLo.
- Multi-byte variables can be written as (xCoordTop xCoordHi xCoordLo xCoordBot) or xCoord(Top Hi Lo Bot).
- Minor labels within subroutines are four lower-case letters and a number, such as main34.
- Subroutines that exist as jump points tend to end in a capital S (a terminology taken from the original version of Elite), so BigRoutineS will typically jump through to BigRoutine, for example.
- Constant are in all caps, such as PPU_CTRL.
- Bank 7 contains a "switchyard" that enables routines to be called, even when they are in another ROM bank (bank 7 is always present in the top ROM bank, so it can host the switchyard). Routines in the switchyard have names that end in _bn, where n is the destination bank, so for example calling PauseGame_b6 will switch bank 6 into memory, call the PauseGame routine in bank 6, and then switch back to the previous bank when the routine returns.
- Some routines are duplicated across ROM banks, such as BRIS, which appears in both bank 0 and bank 2. As there is only one namespace for the project, I have added _bn to the end of one of them (so the copy of BRIS in bank 0 is called BRIS_b0, for example).

Routine names tend to be in the form "VerbNoun", so they describe an action, e.g. DrawIconBar or SendPalettesToPPU. Hopefully this makes things easier to follow...

Wherever code in the NES version is based on the original BBC Micro code (which is around 30% of the NES game binary), I have kept the original labels from the 1984 source. It is therefore pretty easy to work out whether code is original or new, as the original code uses old-school routine names like LL9, DOEXP, TT24, BEGIN and so on, while the new code has routine names like DrawBoxEdges, SendScreenToPPU and MoveIconBarPointer.

## Variant conditionals

						                             --------------------

						The source code is designed to build multiple variants of the game. This is done using BeebAsm variables whose names start with underscores, and the source code contains IF ... ENDIF statement blocks to control which code is assembled during the build, according to which variant is being built.

This means you can search the source code for the likes of _PAL, _SNG45 and _COMPACT to see exactly how the variants differ. For a list of the source code variables used, see the variant page for each version (such as the page on [different variants of the BBC Master version](https://elite.bbcelite.com/master/releases.html), for example).

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
[ 1   0   0 ]        [ x ]
  [ 0   1   0 ]   or   [ y ]
  [ 0   0  -1 ]        [ z ]
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
(x_sign x_hi x_lo)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
(xCoordTop xCoordHi xCoordLo xCoordBot)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
xCoord(Top Hi Lo Bot)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
(X Y)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
(A S S+1)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
(A P 0)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
(2 78)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
(K+3 K+2 K+1 K)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
K(3 2 1 0)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
XX15(0 1 2 3)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
XX3+X(1 0)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
K(S 3 2 1 0)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
XX15(4 0 1 2 3)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
x_sign          x_hi          x_lo
  +     &12           &34           &56
  0 0010010      00110100      01010110
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
x_sign          x_hi          x_lo
  -     &12           &34           &56
  1 0010010      00110100      01010110
```



---
*Fonte originale: [https://elite.bbcelite.com/about_site/terminology_used_in_this_commentary.html](https://elite.bbcelite.com/about_site/terminology_used_in_this_commentary.html)*

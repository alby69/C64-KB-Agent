---
title: Building Commodore 64 Elite from the source disk
source_url: https://elite.bbcelite.com/deep_dives/building_commodore_64_elite_from_the_source_disk.html
category: source-code
topics:
- basic
- assembly
- sprite programming
- graphics
difficulty: beginner
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

# Building Commodore 64 Elite from the source disk

## How to build Commodore 64 Elite from the original BBC Micro source disk

To celebrate the 40th anniversary of Elite on the BBC Micro, Ian Bell [released a number of interesting disk images](http://www.elitehomepage.org/fourty/index.htm) on his personal website. One of these was the original 1985 source disk for the Commodore 64 version of Elite, which is particularly intriguing as it was the first non-Acorn version of the game.

Let's take a look at the source disk and see what's involved in building Commodore 64 Elite from the source.

## What's on the disk?

													 -------------------

						The source disk comes as a zip file, which you can [download](http://www.elitehomepage.org/archive/a/a5050010.zip) from the [archive](http://www.elitehomepage.org/archive/index.htm) on Ian Bell's site. Inside the zip is a DSD file, which is a BBC Micro double-sided DFS disk image that consists of two sides, drive 0 and drive 2.

This is the catalogue of drive 0:

![A catalogue of drive 0 of the Commodore 64 source disk](https://elite.bbcelite.com/images/c64/source_drive_0.png) 

						And this is drive 2:

![A catalogue of drive 2 of the Commodore 64 source disk](https://elite.bbcelite.com/images/c64/source_drive_2.png) 

						The disk contents can be viewed on any BBC Micro with DFS, but to actually run the build it needs to be loaded into a BBC Micro with a 6502 Second Processor. It will also work on emulators: my personal favourite is Tom Seddon's [b2 emulator](https://github.com/tom-seddon/b2), but any emulator with support for a second processor will do, even the browser-based JSBeeb (which you can use to run the build by following the links below).

That said, if you try to run the build process using Ian Bell's disk image, then you quickly run out of disk space. To make it easier to run the build yourself, I have produced a stripped-down version of the disk that only contains the source files that the build needs, so there's enough room to run the whole end-to-end process.

For ultimate convenience, you can [open JSBeeb with the stripped-down source disk already loaded](https://bbc.xania.org/?coProcessor=true&autoboot&disc=https://elite.bbcelite.com/versions/sources/A5050010-stripped-to-sources.dsd). Then you can follow the process below to build Commodore 64 Elite yourself, all within your browser. If you want to follow along with your own setup, you can download the [stripped-down image as a DSD file](https://elite.bbcelite.com/versions/sources/A5050010-stripped-to-sources.dsd) that you can load directly into your emulator. 

Note that the build process needs a copy of Acorn's HIBASIC on drive 2. This is essential because it frees up more memory than standard BASIC, and we need that extra space for the build process. HIBASIC is not included in the disks from Ian Bell's site, but I have included it on the stripped-down source disk images so they are ready to go.

Also note that this build process is pretty slow. If you are in a standalone emulator you may be able to run things at a faster speed, but if you're on real hardware or JSBeeb, prepare for some long waits. It's a lot of work for an 8-bit machine to handle, and it makes you appreciate just how complicated Elite really is.

If you would like to look at the source files but don't want to be messing about with disk images from a bygone era, I have converted all the BASIC programs into text and uploaded them to the accompanying repository, where [you can browse them at your convenience](https://github.com/markmoxon/elite-source-code-commodore-64/tree/main/1-source-files/original-sources).

## What the programs do

													 --------------------

						Before we run through the build process itself, here's a quick summary of what the core source files do, in the order that they appear in the build pipeline. These are all BBC BASIC programs, with most of them including inline assembly language. All of them produce files as output, with some of them taking other files as input.

There is one part of the source pipeline that's missing from the source disk: the $.ELITE file from the first step. This file should contain an uncompressed source for the Elite Theme music, which the S.THEMES program converts into the C.THEME file, but $.ELITE is missing; luckily the compressed C.THEMES file is present, so we can simply skip the first step.

There are also four prerequisite files that are required by the build process: C.SHIPS, $.DIALS53, C.MUSDAT and C.FONT. These are described in the section below on running the build.

| Program | Input | Output | 
|---|---|---|
| S.THEMES | $.ELITE (missing) | C.THEME | 
| S.CSHIPS | Ship source disk ( [download](http://www.elitehomepage.org/archive/a/a4100082.zip)) | C.SHIPS | 
| S.MUCOMPR | C.MUSDAT | C.COMUDAT | 
| S.GENWORD | - | P.WORDS | 
| S.IANTOKS | - | A.IANTOK | 
| S.LODATAS | P.WORDS C.FONT C.IANTOK | $.LODATA | 
| S.SPRITES | - | C.SPRITE | 
| S.CDATE4S | - | C.DATE4 | 
| $.MO5-COM | $.DIALS53 | C.CODIALS | 
| C.ELITEA | C.ELITEB C.ELITEC C.ELITED C.ELITEE C.ELITEF C.ELITEG C.ELITEH C.ELITEI C.ELITEJ C.ELITEK C.COMUDAT | $.ELTA $.ELTB $.ELTC $.ELTD $.ELTE $.ELTF $.ELTG $.ELTH $.ELTI $.ELTJ $.ELTK | 
| S.BCODES | $.ELTA $.ELTB $.ELTC $.ELTD $.ELTE $.ELTF $.ELTG $.ELTH $.ELTI $.ELTJ $.ELTK | $.LOCODE $.HICODE | 
| S.COMLODS | C.LODATA C.SHIPS C.CODIALS C.SPRITE C.DATE4 | C.COMLOD | 

The following programs are also on the source disk:

- S.HICODES is like S.BCODES but only produces HICODES.
- $.SCRNOP5 is an image editor.
- $.SEND sends a file to a Commodore 64.
- $.UNPACK analyses competition codes.

Now let's take a look at the build process itself.

## The end result

													 --------------

						At the outset it's worth noting that the source disk doesn't build a fully functioning Commodore 64 game. Instead, it produces binary files that are suitable for transmitting from a BBC Micro to a Commodore 64 via the user port, using the *SEND utility and the Programmer's Development System (see the deep dive on [developing Commodore 64 Elite on a BBC Micro](https://elite.bbcelite.com/developing_commodore_64_elite_on_a_bbc_micro.html) for more information). The binaries produced by the build process contain the game itself, but there is no disk loader, so the game can't be easily run in this format.

Specifically, the build process creates three binary files:

- COMLOD, which contains the game loader
- LOCODE, which contains the first part of the main game binary
- HICODE, which contains the second part of the main game binary

These binaries are themselves composed of lots of smaller binaries that are produced during the build. This is how the finished product is composed:

- LODATA = P.WORDS + C.FONT + C.IANTOK
- COMLOD = LODATA + C.SHIPS + COMLODS + C.CODIALS + C.SPRITE + C.DATE4
- LOCODE = ELTA + ELTB + ELTC
- HICODE = ELTD + ELTE + ELTF + ELTG + ELTH + ELTI + ELTJ + ELTK

Comparing these files to the Firebird GMA release, which is the version that's built by the [accompanying repository](https://github.com/markmoxon/elite-source-code-commodore-64), we have the following mapping:

- gma4 = COMLOD
- gma5 = LOCODE
- gma6 = HICODE + C.THEME

Firebird then added three disk loader programs - firebird, gma1 and gma3 - to produce the final game disk.

## Running the build process

													 -------------------------

						In order to run the build process, we need all the source files, plus the four prerequisite files mentioned above. These latter four files are produced outside of the build process, as follows:

- C.SHIPS contains the ship data. There is a separate source disk for creating ship data, which [can be found on Ian Bell's site](http://www.elitehomepage.org/archive/a/a4100082.zip). The sources on this separate disk create individual ship files called MISSILE, COBRA and so on, which the S.CSHIPS program on the Commodore 64 source disk combines to form the C.SHIPS file. The Commodore 64 source disk contains a pre-compiled C.SHIPS file, so we can just use that.
- C.MUSDAT is the uncompressed music file for The Blue Danube, which would have been delivered to Bell and Braben by Julie Dunn. See the deep dive on [music in Commodore 64 Elite](https://elite.bbcelite.com/music_in_commodore_64_elite.html)for more information.
- C.FONT is the game font, and it is identical to the P.FONT font file on the 6502 Second Processor version source disk. This is a direct extract of the font from the BBC Micro's operating system ROM.
- $.DIALS53 contains the dashboard bitmap image, as a BBC Micro mode 5 screen image.

These four files are already included in the source disk from Ian Bell's site, so now let's look at the actual build process. The following assumes you are using the [stripped-down disk image](https://elite.bbcelite.com/versions/sources/A5050010-stripped-to-sources.dsd) that frees up enough space to run the build.

First, load up your emulator and change the machine type to a BBC Micro with a 6502 Second Processor (or if you are running this on a real BBC Micro, make sure your co-processor is turned on).

Put the disk image in drive 0 and press SHIFT-CTRL-BREAK. This will run a set of commands that will appear on the screen. If you are using JSBeeb, then you can simply [fire it up with this link](https://bbc.xania.org/?coProcessor=true&autoboot&disc=https://elite.bbcelite.com/versions/sources/A5050010-stripped-to-sources.dsd) to complete this step.

Now type the following and press RETURN:

CHAIN ":2.S.MUCOMPR"

This will compress the C.MUSDAT music data file and will save it as C.COMUDAT on drive 2. It takes a while.

Now type the following and press RETURN after each line:

*DRIVE 2 CHAIN "S.GENWORD"

This will generate the P.WORDS text token file on drive 2.

Now type the following and press RETURN:

CHAIN "S.IANTOKS"

This will generate the C.IANTOK extended text token file on drive 2. It takes a while.

Now type the following and press RETURN, and then press RETURN again at the "insert destination disk" prompt:

CHAIN "S.LODATAS"

This takes P.WORDS, C.FONT and C.IANTOK and produces the C.LODATA file on drive 2.

Now type the following and press RETURN:

CHAIN "S.SPRITES"

This will generate the C.SPRITE sprite definitions file on drive 2. It takes a while.

Now type the following and press RETURN:

CHAIN "S.CDATE4S"

This will generate the C.DATE4 date image on drive 2.

Now type the following and press RETURN after each line:

*DIR $ CHAIN "$.MO5-COM"

This converts the $.DIALS53 dashboard image into a Commodore 64 format image in C.CODIALS on drive 2. It takes a while.

Next, press SHIFT-CTRL-BREAK to reboot the disk.

Now tap f0 (or f10 if you are in JSBeeb) and press RETURN, which will enter the following for you:

CHAIN "ELITEA"

Be careful not to hold f0 down too long, otherwise it might insert multiple copies of the CHAIN command - just tap it quickly. If it does insert too much text, you can delete it with the DELETE key and try again.

Press RETURN at the USA% prompt, and Elite will start to build. This part takes a very long time, as it runs C.ELITEA through C.ELITEK to produce C.ELTA through C.ELTK, ingesting C.COMUDAT in the process. The process is then repeated to implement a two-pass assembly, and it takes a particularly long time around the second stage "f" - patience is the key here.

When it's finished, tap f4 and then RETURN, which will enter the following for you:

CHAIN ":2.S.BCODES"

Again, press RETURN at the "insert destination disk" prompt. This will ingest C.ELTA through C.ELTK to produce the LOCODE and HICODE files on drive 2.

Now type the following and press RETURN after each line:

HIMEM=&B800 CHAIN ":2.S.COMLODS"

This will ingest C.LODATA, C.SHIPS, C.CODIALS, C.SPRITE and C.DATE4 to produce the C.COMLOD file on drive 0.

And that's it! We now have the three files we want: COMLOD on drive 0, and LOCODE and HICODE on drive 2. These will be identical to the binaries produced by the modern build process when the variant build parameter is set to source-disk-build - see the [repository for details](https://github.com/markmoxon/elite-source-code-commodore-64#building-the-source-disk-build-variant).

If you don't want to run through the above process but want to see the final result, you can download [a disk image of the build result](https://elite.bbcelite.com/versions/sources/A5050010-results-of-build.dsd).

In the original development environment, the authors could then send the results to a connected Commodore 64, using the SEND utility, before running the transmitted code directly on the Commodore 64 (see the deep dive on [developing Commodore 64 Elite on a BBC Micro](https://elite.bbcelite.com/developing_commodore_64_elite_on_a_bbc_micro.html) for more details). To see how this works from the BBC Micro side, you can run the SEND utility like this:

*DIR $ *SEND

You can enter a filename if you like (try C.COMLOD, for example), but it will just hang, as it waits for a response from the Commodore 64 that you probably don't have hooked up to your machine. But this is how they did the original development, so it's still interesting to see what the process would have looked like, even if it doesn't work.

And that is how you build Commodore 64 Elite on a BBC Micro, just like Bell and Braben did back in 1985...

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
CHAIN ":2.S.MUCOMPR"
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
*DRIVE 2
  CHAIN "S.GENWORD"
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
CHAIN "S.IANTOKS"
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
CHAIN "S.LODATAS"
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
CHAIN "S.SPRITES"
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
CHAIN "S.CDATE4S"
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
*DIR $
  CHAIN "$.MO5-COM"
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
CHAIN "ELITEA"
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
CHAIN ":2.S.BCODES"
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
HIMEM=&B800
  CHAIN ":2.S.COMLODS"
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
*DIR $
  *SEND
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/building_commodore_64_elite_from_the_source_disk.html](https://elite.bbcelite.com/deep_dives/building_commodore_64_elite_from_the_source_disk.html)*

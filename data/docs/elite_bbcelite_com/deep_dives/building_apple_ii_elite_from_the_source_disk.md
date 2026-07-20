---
title: Building Apple II Elite from the source disk
source_url: https://elite.bbcelite.com/deep_dives/building_apple_ii_elite_from_the_source_disk.html
category: source-code
topics:
- basic
- assembly
- graphics
difficulty: intermediate
language: mixed
hardware:
- CIA
- SID
- CPU
- KERNAL
- BASIC ROM
related:
- sid-registers
- sound-programming
- joystick-reading
- keyboard-handling
- kernal-routines
- memory-map
- music-player
- cia-registers
scraped_at: '2026-07-20'
---

# Building Apple II Elite from the source disk

## How to build Apple II Elite from the original BBC Micro source disk

To celebrate the 40th anniversary of Elite on the BBC Micro, Ian Bell [released a number of interesting disk images](http://www.elitehomepage.org/fourty/index.htm) on his personal website. One of these was the original source disk for the 1986 Apple II version of Elite, which was the second non-Acorn version to be built from the 6502 sources, following the release of the 1985 Commodore 64 version.

Let's take a look at the source disk and see what's involved in building Apple II Elite from the source.

## What's on the disk?

													 -------------------

						The source disk comes as a zip file, which you can [download](http://www.elitehomepage.org/archive/a/a6010080.zip) from the [archive](http://www.elitehomepage.org/archive/index.htm) on Ian Bell's site. Inside the zip is a DSD file, which is a BBC Micro double-sided DFS disk image that consists of two sides, drive 0 and drive 2.

This is the catalogue of drive 0:

![A catalogue of drive 0 of the Apple II source disk](https://elite.bbcelite.com/images/apple/source_drive_0.png) 

						And this is drive 2:

![A catalogue of drive 2 of the Apple II source disk](https://elite.bbcelite.com/images/apple/source_drive_2.png) 

						The disk contents can be viewed on any BBC Micro with DFS, but to actually run the build it needs to be loaded into a BBC Micro with a 6502 Second Processor. It will also work on emulators: my personal favourite is Tom Seddon's [b2 emulator](https://github.com/tom-seddon/b2), but any emulator with support for a second processor will do, even the browser-based JSBeeb (which you can use to run the build by following the links below).

That said, if you try to run the build process using Ian Bell's disk image, then you quickly run out of disk space, and you also get various "Bad command" errors. To make it easier to run the build yourself, I have produced a stripped-down version of the disk that only contains the source files that the build needs, so there's enough room to run the whole end-to-end process. This disk image also includes the fixes that allow us to run the build without giving any errors about missing transmission utilities (see the next section for details).

For ultimate convenience, you can [open JSBeeb with the stripped-down source disk already loaded](https://bbc.xania.org/?coProcessor=true&autoboot&disc=https://elite.bbcelite.com/versions/sources/A6010080-stripped-to-sources.dsd). Then you can follow the process below to build Apple II Elite yourself, all within your browser. If you want to follow along with your own setup, you can download the [stripped-down image as a DSD file](https://elite.bbcelite.com/versions/sources/A6010080-stripped-to-sources.dsd) that you can load directly into your emulator. 

Note that the build process needs a copy of Acorn's HIBASIC on drive 2. This is essential because it frees up more memory than standard BASIC, and we need that extra space for the build process. HIBASIC is not included in the disks from Ian Bell's site, but I have included it on the stripped-down source disk images so they are ready to go.

Also note that this build process is pretty slow. If you are in a standalone emulator you may be able to run things at a faster speed, but if you're on real hardware or JSBeeb, prepare for some long waits. It's a lot of work for an 8-bit machine to handle, and it makes you appreciate just how complicated Elite really is.

If you would like to look at the source files but don't want to be messing about with disk images from a bygone era, I have converted all the BASIC programs into text and uploaded them to the accompanying repository, where [you can browse them at your convenience](https://github.com/markmoxon/elite-source-code-apple-ii/tree/main/1-source-files/original-sources).

## Fixing the build process

													 ------------------------

						The Apple II Elite build process was designed to produce game binaries that could be transmitted to an Apple II, that was connected to the development BBC Micro machine via a cable. Two utilities were used for this transmission: MSEND and APPLE (which could be run using *MSEND and *APPLE, or by using the OSCLI command in BASIC). Unfortunately these utilities are missing from the source disk, so when the build process tries to run either of these commands, we get a "Bad command" error.

I have fixed this in the stripped-down build process, by changing the build programs to print out what the commands would be, rather than trying to run them. This does not affect the build itself, it just skips the steps that will no longer work.

I have also copied the game font file onto the disk, which would normally be loaded from a separate disk (which isn't included in Ian Bell's archive).

These are all the changes I have made to the original build files:

- Copy A.FLOWY to drive 2 (A.FLOWY contains the game font, extracted from the released game)
- In S.DATAS, change the load command so that instead of loading it from drive 1:
`250OSCLI("L.:1.A.FLOWY "+STR$~(FONT+CODE-DL%))`it loads it from drive 2:`250OSCLI("L.:2.A.FLOWY "+STR$~(FONT+CODE-DL%))`
- In S.SCREEN2, disable the *MSEND command:
`3200OSCLI("MSEND "+STR$~SP +" +2000 2000")`by changing it to a PRINT statement:`3200PRINT("*MSEND "+STR$~SP +" +2000 2000")`
- In S.APMAKES, disable the *MSEND and *APPLE commands:
160 OSCLI"MSEND "+STR$~CODE%+" +"+STR$~(&C000-&9000+&3600)+" A00" ... 180 VDU7,7:*APPLE ... 200 OSCLI"MSEND "+STR$~CODE%+" +"+STR$~(&9000-C%)+" "+STR$~C% ... 220 VDU7,7:*APPLE by changing them to PRINT statements:160 PRINT"*MSEND "+STR$~CODE%+" +"+STR$~(&C000-&9000+&3600)+" A00" ... 180 VDU7,7:PRINT"*APPLE" ... 200 PRINT"*MSEND "+STR$~CODE%+" +"+STR$~(&9000-C%)+" "+STR$~C% ... 220 VDU7,7:PRINT"*APPLE" 
- Also in S.APMAKES, add two save commands to save the ELA and ELB binaries to the disk, rather than trying to transmit them:
185 OSCLI"SAVE :2.ELA "+STR$~CODE%+"+"+STR$~(&C000-&9000+&3600) ... 215 OSCLI"SAVE :2.ELB "+STR$~CODE%+"+"+STR$~(&9000-C%) 

This updates the build process to save the ELA and ELB binaries to the source disk, rather than trying (and failing) to run the missing utilities that would transmit the binaries to an attached Apple II.

## What the programs do

													 --------------------

						Before we run through the build process itself, here's a quick summary of what the core source files do, in the order that they appear in the build pipeline. These are all BBC BASIC programs, with most of them including inline assembly language. All of them produce files as output, with some of them taking other files as input.

There are also three prerequisite files that are required by the build process: A.SHIPS, $.DIALS25 and :1.A.FLOWY. These are described in the section below on running the build.

| Program | Input | Output | 
|---|---|---|
| S.ASHIPS | Ship source disk ( [download](http://www.elitehomepage.org/archive/a/a4100082.zip)) | A.SHIPS | 
| S.GENWORD | - | A.WORDS | 
| S.IANTOKS | - | A.IANTOK | 
| S.DATAS | A.WORDS :1.A.FLOWY A.IANTOK | A.DATA | 
| S.SCREEN2 | $.DIALS25 | A.SCREEN | 
| A.ELITEA | A.ELITEB A.ELITEC A.ELITED A.ELITEE A.ELITEF A.ELITEG A.ELITEH A.ELITEI A.ELITEJ A.ELITEK A.COMUDAT | $.ELTA $.ELTB $.ELTC $.ELTD $.ELTE $.ELTF $.ELTG $.ELTH $.ELTI $.ELTJ $.ELTK | 
| S.SCODES | $.ELTA $.ELTB $.ELTC $.ELTD $.ELTE $.ELTF $.ELTG $.ELTH $.ELTI $.ELTJ $.ELTK A.SHIPS | $.CODE1 $.CODE2 | 
| S.APMAKES | $.DATA $.SCREEN $.CODE2 $.CODE1 | $.ELA $.ELB | 

The following programs are also on the source disk:

- A.APLINE, A.APLINE2 and A.APTES are test programs that contain iterations of the line-drawing code.
- $.DIALS2, $.DIALS23, $.DIALS24, $.DIALS5 and E.DIALS4 are variations of the dashboard image.
- S.FONTS converts the font from Commodore 64 Elite into an Apple-compatible format. It looks for :3.C.FONT, so it expects the Commodore 64 Elite source disk in drive 1. It produces the A.FONT file on the source disk, though this file is not used in the build process.
- $.RAMCTST checks whether there is a RAM card fitted to the Apple II that's attached to the BBC Micro.
- S.SCREEN is like S.SCREEN2 but it converts $.DIALS5 into Apple format rather than $.DIALS25.
- $.SCRNOP5 is an image editor.
- A.SLIDE loads the dashboard in E.DIALS4 and draws vertical edges in the space view, possibly as part of creating the loading screen.
- A.TESTER is like S.APMAKES but replaces the *APPLE commands with *CALL commands.
- A.RECIEVE seems to take byte input from the keyboard to send to an Apple II (depending on what *APPLE command actually does).
- V.APDOC is a VIEW word processor document that contains information about the Apple II version.

Now let's take a look at the build process itself.

## The end result

													 --------------

						At the outset it's worth noting that the source disk doesn't build a fully functioning Apple II game. Instead, it produces binary files that are suitable for transmitting from a BBC Micro to an Apple II via the user port, using the MSEND and APPLE utilities and the Programmer's Development System (see the deep dive on [developing Apple II Elite on a BBC Micro](https://elite.bbcelite.com/developing_commodore_64_elite_on_a_bbc_micro.html) for more information). The binaries produced by the build process contain the game itself, but there is no game loader, so the game can't be easily run in this format.

Specifically, the build process creates two binary files:

- ELA, which contains the second part of the main game binary (CODE2), plus the game data and loading screen, and a routine that copies the CODE2 binary into bank-switched RAM as part of the development process
- ELB, which contains the first part of the main game binary

These binaries are themselves composed of lots of smaller binaries that are produced during the build. This is how the finished product is composed:

- DATA = A.WORDS + A.IANTOK + :1.A.FLOWY
- CODE = ELTA + ELTB + ELTC + ELTD + ELTE + ELTF + ELTG + ELTH + ELTI + ELTJ + ELTK + A.SHIPS
- CODE1 = first $5000 bytes of CODE
- CODE2 = rest of CODE
- ELA = copy routine + DATA + A.SCREEN + CODE2
- ELB = CODE1

In the released version of the game, the ELA and ELB files are on the disk as ELA and ELB1. Firebird then added three loader programs: the game loader in SEC3, a BASIC bootstrap in ELITE and the first part of A.SCREEN in SCRN (which is used to repair the damage caused by loading the game into screen memory).

## Running the build process

													 -------------------------

						In order to run the build process, we need all the source files, plus the three prerequisite files mentioned above. These latter three files are produced outside of the build process, as follows:

- A.SHIPS contains the ship data. There is a separate source disk for creating ship data, which [can be found on Ian Bell's site](http://www.elitehomepage.org/archive/a/a4100082.zip). The sources on this separate disk create individual ship files called MISSILE, COBRA and so on, which the S.ASHIPS program on the Apple II source disk combines to form the A.SHIPS file. The Apple II source disk contains a pre-compiled A.SHIPS file, so we can just use that.
- :1.A.FLOWY contains the game font, which is unique to the Apple version of Elite. It's a more flowing font that in the other versions, hence the name.
- $.DIALS25 contains the dashboard bitmap image, as a BBC Micro mode 2 screen image.

The first two prerequisite files are already included in the source disk from Ian Bell's site, but the FLOWY file is missing (as it comes from a different disk that we are supposed to put into drive 1). To enable us to run the build, I have extracted the font from the released game and added it to the stripped-down source disk image, as the A.FLOWY file on drive 2.

Now let's look at the actual build process. The following assumes you are using the [stripped-down disk image](https://elite.bbcelite.com/versions/sources/A6010080-stripped-to-sources.dsd) that frees up enough space to run the build and disables the commands that try to send the results to the Apple II.

First, load up your emulator and change the machine type to a BBC Micro with a 6502 Second Processor (or if you are running this on a real BBC Micro, make sure your co-processor is turned on).

Put the disk image in drive 0 and press SHIFT-CTRL-BREAK. This will run a set of commands that will appear on the screen. If you are using JSBeeb, then you can simply [fire it up with this link](https://bbc.xania.org/?coProcessor=true&autoboot&disc=https://elite.bbcelite.com/versions/sources/A6010080-stripped-to-sources.dsd) to complete this step.

Now type the following and press RETURN:

CHAIN ":2.S.GENWORD"

This will generate the A.WORDS text token file on drive 2.

Now type the following and press RETURN:

CHAIN ":2.S.IANTOKS"

This will generate the A.IANTOK extended text token file on drive 2. It takes a while.

Now type the following and press RETURN, and then press RETURN again at the "insert destination disk" prompt:

CHAIN ":2.S.DATAS"

This takes A.WORDS, A.FLOWY and A.IANTOK and produces the A.DATA file on drive 2.

Now type the following and press RETURN:

CHAIN ":2.S.SCREEN2"

This converts the $.DIALS25 dashboard image into an Apple II format loading screen image in A.SCREEN on drive 2. It takes a while. It ends by sending the screen to a connected Apple II, but I have modified the source to print out the MSEND command rather than executing it, as we no longer have a copy of the MSEND utility.

Next, press SHIFT-CTRL-BREAK to reboot the disk.

Now tap f0 (or f10 if you are in JSBeeb) and press RETURN, which will enter the following for you:

CHAIN "ELITEA"

Be careful not to hold f0 down too long, otherwise it might insert multiple copies of the CHAIN command - just tap it quickly. If it does insert too much text, you can delete it with the DELETE key and try again.

Elite will now start to build. This part takes a very long time, as it runs A.ELITEA through A.ELITEK to produce A.ELTA through A.ELTK. The process is then repeated to implement a two-pass assembly - patience is the key here.

When it's finished, tap f4 and then RETURN, which will enter the following for you:

CHAIN ":2.S.CODES"

This will ingest A.ELTA through A.ELTK to produce the CODE1 and CODE2 files on drive 2.

Now type the following and press RETURN after each line:

HIMEM=&B800 CHAIN ":2.S.APMAKES"

This will ingest A.DATA, A.SCREEN and CODE2 to produce the ELA file on drive 0, and it will ingest CODE1 to produce the ELB file on drive 0. It ends by sending the files to a connected Apple II, but I have modified the source to print out the MSEND and APPLE commands rather than executing them, as we no longer have a copy of the MSEND utility.

And that's it! We now have the two files we want: ELA and ELB on drive 2. These will be identical to the binaries produced by the modern build process when the variant build parameter is set to source-disk-build - see the [repository for details](https://github.com/markmoxon/elite-source-code-apple-ii#building-the-source-disk-build-variant).

If you don't want to run through the above process but want to see the final result, you can download [a disk image of the build result](https://elite.bbcelite.com/versions/sources/A6010080-results-of-build.dsd).

In the original development environment, the APMAKES program would also send the ELA and ELB binaries to a connected Apple II, using the MSEND and APPLE utilities, before running the transmitted code directly on the Apple II (see the deep dive on [developing Apple II Elite on a BBC Micro](https://elite.bbcelite.com/developing_apple_ii_elite_on_a_bbc_micro.html) for more details). Unfortunately neither of these utilities are included on the source disk, so that's where the process ends for us.

And that is how you build Apple II Elite on a BBC Micro, just like Bell and Braben did back in 1985/6...

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
250OSCLI("L.:1.A.FLOWY "+STR$~(FONT+CODE-DL%))
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
250OSCLI("L.:2.A.FLOWY "+STR$~(FONT+CODE-DL%))
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
3200OSCLI("MSEND "+STR$~SP +" +2000 2000")
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
3200PRINT("*MSEND "+STR$~SP +" +2000 2000")
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
160 OSCLI"MSEND "+STR$~CODE%+" +"+STR$~(&C000-&9000+&3600)+" A00"
  ...
  180 VDU7,7:*APPLE
  ...
  200 OSCLI"MSEND "+STR$~CODE%+" +"+STR$~(&9000-C%)+" "+STR$~C%
  ...
  220 VDU7,7:*APPLE
```

### Snippet Codice (BASIC)

```basic
160 PRINT"*MSEND "+STR$~CODE%+" +"+STR$~(&C000-&9000+&3600)+" A00"
  ...
  180 VDU7,7:PRINT"*APPLE"
  ...
  200 PRINT"*MSEND "+STR$~CODE%+" +"+STR$~(&9000-C%)+" "+STR$~C%
  ...
  220 VDU7,7:PRINT"*APPLE"
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
185 OSCLI"SAVE :2.ELA "+STR$~CODE%+"+"+STR$~(&C000-&9000+&3600)
  ...
  215 OSCLI"SAVE :2.ELB "+STR$~CODE%+"+"+STR$~(&9000-C%)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
CHAIN ":2.S.GENWORD"
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
CHAIN ":2.S.IANTOKS"
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
CHAIN ":2.S.DATAS"
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
CHAIN ":2.S.SCREEN2"
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
CHAIN "ELITEA"
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
CHAIN ":2.S.CODES"
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
HIMEM=&B800
  CHAIN ":2.S.APMAKES"
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/building_apple_ii_elite_from_the_source_disk.html](https://elite.bbcelite.com/deep_dives/building_apple_ii_elite_from_the_source_disk.html)*

---
title: Developing Apple II Elite on a BBC Micro
source_url: https://elite.bbcelite.com/deep_dives/developing_apple_ii_elite_on_a_bbc_micro.html
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

# Developing Apple II Elite on a BBC Micro

## Clues about the remote development of the Apple II version of Elite

One of the more intriguing aspects of the 6502 versions of Elite is how the Commodore 64 and Apple II versions were developed on a BBC Micro. Indeed, the only 6502-based version not to be developed in this way was the NES version, and even then the BBC Micro-based source code was used as a starting point (see [the Elite source code family tree](https://elite.bbcelite.com/the_elite_source_code_family_tree.html) for more details on how the different sources are related).

The Commodore 64 version was built using the Programmer's Development System (PDS). This clever bit of hardware let the authors connect a Commodore 64 to the BBC Micro development system, so they could develop the game on the BBC before transmitting the assembled binaries to the attached Commodore for testing. This system was available for a number of systems, and the same PDS setup was used to develop Elite for the NES (though this time the development machine was an Apricot PC). See the deep dive on [developing Commodore 64 Elite on a BBC Micro](https://elite.bbcelite.com/developing_commodore_64_elite_on_a_bbc_micro.html) for details.

The Apple II version was also developed using a connected BBC Micro, but there's a catch: there doesn't seem to be any record of a PDS system being available for the Apple II. Of course, this doesn't mean that it didn't exist, but it does mean we can't scour the internet for clues about the development environment.

So let's see if we can work it out from the clues on the original source disk for Apple II Elite, which Ian Bell released to celebrate the 40th anniversary of the original BBC Micro version.

## Clues on the Apple source disk

													 ------------------------------

						The build process for the Apple II version of Elite is described in detail in the deep dive on [building Apple II Elite from the source disk](https://elite.bbcelite.com/building_apple_ii_elite_from_the_source_disk.html), so check that out for a detailed overview of what's involved. In that build process, I had to disable the commands that would transmit the game binaries to an attached Apple II, as otherwise those commands just give "Bad command" errors. For this article, these are the exact parts that we're interested in.

There are four clues dotted throughout the build process that point towards a remotely connected Apple II:

- The *MSEND command is used in a number of utilities on the source disk, in particular the [S.APMAKES](https://github.com/markmoxon/elite-source-code-apple-ii/blob/main/1-source-files/original-sources/S.APMAKES.txt)program, which builds the ELA and ELB binaries (and which forms the basis of the[transfer program](https://elite.bbcelite.com/apple/all/transfer_program.html)).
- The *APPLE command is also used in a number of utilities, including [S.APMAKES](https://github.com/markmoxon/elite-source-code-apple-ii/blob/main/1-source-files/original-sources/S.APMAKES.txt).
- The *CALL command appears in various utilities as well, such as [A.TESTER](https://github.com/markmoxon/elite-source-code-apple-ii/blob/main/1-source-files/original-sources/A.TESTER.txt),[A.APLINE](https://github.com/markmoxon/elite-source-code-apple-ii/blob/main/1-source-files/original-sources/A.APLINE.txt)and[$.RAMCTST](https://github.com/markmoxon/elite-source-code-apple-ii/blob/main/1-source-files/original-sources/%24.RAMCTST.txt).
- The assembled game binary contains code that copies part of the game into bank-switched RAM and relocates it when the game is run; you can see it in the [ENTRY](https://elite.bbcelite.com/apple/transfer_program/subroutine/entry.html)routine in the transfer program. Bank-switched RAM came as standard with the 64K Apple IIe, and it maps to addresses $D000-$FFFF.

The first three clues refer to star-commands that do not exist in the standard BBC Micro, so they must either have been utilities on the source disk, or commands from a sideways ROM; in either case, we don't have the utilities anymore, so we can only guess what they do.

The last one is really interesting in that it is clearly development-specific code that still runs in the finished, released game.

Let's take a look at all of these, starting with the star-commands.

## The *MSEND command

													 ------------------

						We might not have the three missing utilities anymore, but we do have examples of their usage, so let's see if we can work out what they do.

First up is *MSEND. This one seems reasonably obvious, as it appears to send a block of memory from the BBC Micro to the connected Apple II. Let's look at an example from the S.APMAKES program, which builds the ELA and ELB binaries in memory and then transmits them to the Apple. I'm going to be analysing the last few lines of the program, which look like this:

130 OSCLI"LOAD :2.DATA "+STR$~(CODE%+&160) 140 OSCLI"LOAD :2.SCREEN "+STR$~(CODE%+&1600) 150 OSCLI"LOAD :2.CODE2 "+STR$~(CODE%+&3600) 160 OSCLI"MSEND "+STR$~CODE%+" +"+STR$~(&C000-&9000+&3600)+" A00" 170 PRINT"BSAVE ELA,A$A00,L$"+STR$~(&C000-&9000+&3600) 180 VDU7,7:*APPLE 190 OSCLI"LOAD :2.CODE1 "+STR$~CODE% 200 OSCLI"MSEND "+STR$~CODE%+" +"+STR$~(&9000-C%)+" "+STR$~C% 210 PRINT"BSAVE ELB,A$"+STR$~C%+",L$"+STR$~(&9000-C%) 220 VDU7,7:*APPLE

Before we examine this code in detail, let's quickly run through the pertinent parts of the build process.

When the game is loaded and running in memory, the main game binary lives at address $4000 (see the [Apple II Elite memory map](https://elite.bbcelite.com/the_elite_memory_map_apple_ii.html) for details). The build process sets the C% variable to this address, so C% is $4000.

The game binary isn't loaded in one go, though. Instead, it is split into two parts: CODE1 and CODE2. CODE1 contains the first $5000 bytes of the main binary, from $4000 to $8FFF, while CODE2 contains the rest of the binary, from $9000 to $BFFF. The size of the CODE1 binary is therefore $9000 - $4000 bytes, or $9000 - C% bytes, and the size of the CODE2 binary is $C000 - $9000 bytes (so CODE1 is $5000 bytes while CODE2 is only $3000 bytes). The S.APMAKES program that we're looking at here takes CODE1 and CODE2 and transmits them to the connected Apple; CODE1 is transmitted on its own, but CODE2 is bundled up with the game data and a relocation routine that we'll talk about below.

Let's start by looking at the part of S.APMAKES that transmits the CODE1 file, as it's the simpler of the two. This is actually the second of the two transmissions, and it is done in lines 190 to 220 (we'll look at the more complicated first transmission in a minute). By this point CODE1 has been assembled and saved to drive 2, and BASIC has reserved a large block of memory at address CODE% using the DIM command. S.APMAKES then runs the following four lines:

190 OSCLI"LOAD :2.CODE1 "+STR$~CODE% 200 OSCLI"MSEND "+STR$~CODE%+" +"+STR$~(&9000-C%)+" "+STR$~C% 210 PRINT"BSAVE ELB,A$"+STR$~C%+",L$"+STR$~(&9000-C%) 220 VDU7,7:*APPLE

Note that the BBC Micro uses ampersands to indicate hexadecimal numbers, so &9000 is the same as the more common $9000 notation. Also, the BASIC OSCLI command lets you compose operating system star-commands as strings, so the OSCLI "MSEND" statement in BASIC does the same thing as entering *MSEND from the command line.

The first line loads the CODE1 binary from drive 2 into the reserved block of memory at CODE%. The second line then does a *MSEND command, which seems to be in this format:

*MSEND <source_addr> +<source_length> <destination_addr>

This command appears to transmit a block of memory of length <source_length> from <source_addr> in the BBC Micro, storing it in the Apple II at address <destination_addr>. So in this particular example, we have the following command:

*MSEND CODE% +(&9000-C%) C%

This transmits a block of memory of length $9000 - C% bytes, from address CODE% in the BBC Micro to address C% (i.e. $4000) in the Apple II. As discussed above, we know that CODE1 is loaded at address CODE% and that it is $9000 - C% bytes in size, so this command transmits the whole CODE1 binary to address $4000 in the Apple II, which is the address at which it runs when the game is loaded.

That's the simpler of the two transmissions in S.APMAKES, so now let's look at the more complicated transmission of CODE2 (which actually happens first). The code is along similar lines, but it's a bit more involved and looks like this:

130 OSCLI"LOAD :2.DATA "+STR$~(CODE%+&160) 140 OSCLI"LOAD :2.SCREEN "+STR$~(CODE%+&1600) 150 OSCLI"LOAD :2.CODE2 "+STR$~(CODE%+&3600) 160 OSCLI"MSEND "+STR$~CODE%+" +"+STR$~(&C000-&9000+&3600)+" A00" 170 PRINT"BSAVE ELA,A$A00,L$"+STR$~(&C000-&9000+&3600) 180 VDU7,7:*APPLE

Before we reach this code, S.APMAKES has already assembled the relocation routine at the start of CODE%, so the first line loads the game data after the relocation code at offset $160 in the CODE% block, then the second line loads the loading screen at offset $1600, and finally the third line loads CODE2 at offset $3600. We then reach another *MSEND command, which looks like this:

*MSEND CODE% +(&C000-&9000+&3600) A00

This transmits a block of memory from CODE% in the BBC Micro into the Apple II at address $A00, with a length of $C000 - $9000 + $3600. We noted above that CODE2 is $C000 - $9000 bytes long, and the extra $3600 covers the relocation code, the DATA file and the SCREEN file, which together take up the first $3600 bytes of the CODE% block.

The result of this transmission, which is the first to be performed, is a memory layout in the connected Apple II that looks like this:

+-----------------------------------+ $7000 | | | :2.CODE2 | | | +-----------------------------------+ $4000 | | | :2.SCREEN | | | +-----------------------------------+ $2000 | | | :2.DATA | | | +-----------------------------------+ $0B60 | | | Relocation code | | | +-----------------------------------+ $0A00

The second transmission that we looked at above then sends CODE1 into address $4000-$8FFF in the Apple II... but this overwrites CODE2. Can that be right? What is going on here?

Well, you may have noticed that there is more to the S.APMAKES program - for each of the transmissions, it also prints a BSEND command on the screen, and issues a *APPLE command after making a couple of beeps using the ASCII 7 character. So let's look at those bits next.

## The *APPLE command

													 ------------------

						The *MSEND command in the above code transmits the game into memory on the Apple II, but we also have the following lines after the first transmission:

170 PRINT"BSAVE ELA,A$A00,L$"+STR$~(&C000-&9000+&3600) 180 VDU7,7:*APPLE

and these lines after the second transmission:

210 PRINT"BSAVE ELB,A$"+STR$~C%+",L$"+STR$~(&9000-C%) 220 VDU7,7:*APPLE

The PRINT statements print a BSAVE command to the screen. BSAVE is an Apple II BASIC command that saves a block of memory, using this syntax:

BSAVE <filename>,A$<start_addr>,L$<end_addr>

So in each case, S.APMAKES prints the Apple II command that would save the transmitted data to disk on the Apple II - the first BSAVE would save a file called ELA that contains the contents of memory from $A00 to the end of CODE2 (as the BSAVE is printed before we transmit CODE1 to overwrite CODE2), while the second BSAVE would save a file called ELB after we have transmitted CODE1 over the top of CODE2, so ELB would therefore contain CODE1. All we would have to do is type these commands into the Apple II at the right moments, and they would save the ELA and ELB files to disk; essentially we transmit the content for ELA to the Apple II and then save ELA to disk, and then we transmit the content for ELB to the Apple II (overwriting some of the content on ELA) and then save ELB to disk.

This, I think, is where the *APPLE command comes in. After making two beeps with a VDU7,7 statement, S.APMAKES runs a *APPLE command, and I think this enables us to type something on the BBC Micro and have it echo through to the Apple II as if we were typing it there. I think S.SPMAKES prints the MSEND command on the screen so we can use the BBC Micro's cursor keys and COPY key to easily "type" that command on the BBC Micro, and because *APPLE has been run, it will also be "typed" on the Apple II, thus saving the ELA and ELB binaries to the Apple's disk at the correct moment for each file.

This is an educated guess, though. The only other use of the *APPLE command is in the [A.RECIEVE](https://github.com/markmoxon/elite-source-code-apple-ii/blob/main/1-source-files/original-sources/A.RECIEVE.txt) (sic) program, which looks like this:

```
    5 *APPLE
   10 DIM L% &1000
   20 FOR I%=L% TO L%+&2FF
   30 INPUT ?I%
   40 NEXT
```
						This seems to be a way of populating a block of memory by typing in the contents byte by byte, and the *APPLE at the start might ensure that the data is also "typed" on the connected Apple II. It isn't totally clear, though, so the exact functionality of the *APPLE command is debatable.

But it does appear that S.APMAKES is a method of transmitting the game into the Apple II, in two parts, from where it can be saved to an Apple disk as two files, ELA and ELB. It doesn't matter that the second transmission overwrites part of the first one, as all we want to do is transmit and send; we aren't trying to run the game, we're just trying to get it onto an Apple disk.

So can a similar method be used to transmit the game to an Apple II and run it there, for testing purposes? Let's look at that next.

## The *CALL command and bank-switched RAM

													 ---------------------------------------

						The A.TESTER program on the source disk is identical to the S.APMAKES program, except the VDU7,7:*APPLE commands in lines 180 and 220 have been replaced:

130 OSCLI"LOAD :2.DATA "+STR$~(CODE%+&160) 140 OSCLI"LOAD :2.SCREEN "+STR$~(CODE%+&1600) 150 OSCLI"LOAD :2.CODE2 "+STR$~(CODE%+&3600) 160 OSCLI"MSEND "+STR$~CODE%+" +"+STR$~(&C000-&9000+&3600)+" A00" 170 PRINT"BSAVE ELA,A$A00,L$"+STR$~(&C000-&9000+&3600) 180 OSCLI"CALL A00" 190 OSCLI"LOAD :2.CODE1 "+STR$~CODE% 200 OSCLI"MSEND "+STR$~CODE%+" +"+STR$~(&9000-C%)+" "+STR$~C% 210 PRINT"BSAVE ELB,A$"+STR$~C%+",L$"+STR$~(&9000-C%) 220 OSCLI"CALL "+STR$~S%

These are the only lines that are different between S.APMAKES and A.TESTER, and the *APPLE commands have been replaced by *CALL commands. So what does *CALL do, and what difference does this make?

The first *CALL command is run after the relocation code, game data, loading screen and CODE2 have been transmitted into the Apple II, so the memory map of the Apple II looks like this:

+-----------------------------------+ $7000 | | | :2.CODE2 | | | +-----------------------------------+ $4000 | | | :2.SCREEN | | | +-----------------------------------+ $2000 | | | :2.DATA | | | +-----------------------------------+ $0B60 | | | Relocation code | | | +-----------------------------------+ $0A00

This first transmission puts the relocation code from [ENTRY](https://elite.bbcelite.com/apple/transfer_program/subroutine/entry.html) into location $A00 on the Apple, and it puts CODE2 into address $4000. Then it runs a *CALL A00 command, which I'm pretty sure tells the Apple to run the code at address $A00 - in other words, it tells the Apple to run the relocation code.

The relocation code copies CODE2 into bank-switched RAM at $D000, so when the *CALL command is finished, we have an Apple memory map that looks like this:

+-----------------------------------+ $FFFF | | | :2.CODE2 in bank-switched RAM | | | +-----------------------------------+ $D000 : : : : : : : : +-----------------------------------+ $7000 | | | :2.CODE2 | | | +-----------------------------------+ $4000 | | | :2.SCREEN | | | +-----------------------------------+ $2000 | | | :2.DATA | | | +-----------------------------------+ $0B60 | | | Relocation code | | | +-----------------------------------+ $0A00

We then perform the second transmission, which sends CODE1 to address $4000, so we get this:

+-----------------------------------+ $FFFF | | | :2.CODE2 in bank-switched RAM | | | +-----------------------------------+ $D000 : : : : : : : : +-----------------------------------+ $9000 | | | :2.CODE1 | | | +-----------------------------------+ $4000 | | | :2.SCREEN | | | +-----------------------------------+ $2000 | | | :2.DATA | | | +-----------------------------------+ $0B60 | | | Relocation code | | | +-----------------------------------+ $0A00

And then we perform another *CALL command, this time with an argument of S%. S% is the address of the [entry point for the main game code](https://elite.bbcelite.com/apple/main/subroutine/s_per_cent.html), and in the source disk build of the game, the first thing it does is to copy a $3000-byte block of memory from address $D000 in bank-switched RAM to $9000. So this produces the following memory map in the Apple II:

+-----------------------------------+ $C000 | | | :2.CODE2 | | | +-----------------------------------+ $9000 | | | :2.CODE1 | | | +-----------------------------------+ $4000 | | | :2.SCREEN | | | +-----------------------------------+ $2000 | | | :2.DATA | | | +-----------------------------------+ $0B60 | | | Relocation code | | | +-----------------------------------+ $0A00

This layout matches the [Apple II Elite memory map](https://elite.bbcelite.com/the_elite_memory_map_apple_ii.html) for when the game is running, and the S% routine continues on to start the game proper.

So S.APMAKES transmits the game to an Apple II for saving to disk, while A.TESTER transmits the game to an Apple II and runs it.

Interestingly, the relocation code at $A00 is still present in the released version of the game, and it is still run when ELA is loaded by the [game loader](https://elite.bbcelite.com/apple/all/loader.html), so the released game also tries to copy CODE2 into bank-switched RAM when it loads. The only difference is that the copied code is ignored, as the code to copy it back into main RAM in S% has been replaced by a routine to repair the loading screen, which gets corrupted by the loading process in the game loader.


In other words, the official version of Firebird Elite on the Apple II contains traces of the original two-machine development system, and it gets run every time you load the game. So while there might not have been an official version of the Programmer's Development System for the Apple platform, the code that it inspired was still released, in a sense... and it is still run today, every time anyone straps themselves into their Apple II and fires up the thrusters on their Cobra Mk III.

## Codice Estratto

### Snippet Codice (BASIC)

```basic
130 OSCLI"LOAD :2.DATA "+STR$~(CODE%+&160)
  140 OSCLI"LOAD :2.SCREEN "+STR$~(CODE%+&1600)
  150 OSCLI"LOAD :2.CODE2 "+STR$~(CODE%+&3600)
  160 OSCLI"MSEND "+STR$~CODE%+" +"+STR$~(&C000-&9000+&3600)+" A00"
  170 PRINT"BSAVE ELA,A$A00,L$"+STR$~(&C000-&9000+&3600)
  180 VDU7,7:*APPLE

  190 OSCLI"LOAD :2.CODE1 "+STR$~CODE%
  200 OSCLI"MSEND "+STR$~CODE%+" +"+STR$~(&9000-C%)+" "+STR$~C%
  210 PRINT"BSAVE ELB,A$"+STR$~C%+",L$"+STR$~(&9000-C%)
  220 VDU7,7:*APPLE
```

### Snippet Codice (BASIC)

```basic
190 OSCLI"LOAD :2.CODE1 "+STR$~CODE%
  200 OSCLI"MSEND "+STR$~CODE%+" +"+STR$~(&9000-C%)+" "+STR$~C%
  210 PRINT"BSAVE ELB,A$"+STR$~C%+",L$"+STR$~(&9000-C%)
  220 VDU7,7:*APPLE
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
*MSEND <source_addr> +<source_length> <destination_addr>
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
*MSEND CODE% +(&9000-C%) C%
```

### Snippet Codice (BASIC)

```basic
130 OSCLI"LOAD :2.DATA "+STR$~(CODE%+&160)
  140 OSCLI"LOAD :2.SCREEN "+STR$~(CODE%+&1600)
  150 OSCLI"LOAD :2.CODE2 "+STR$~(CODE%+&3600)
  160 OSCLI"MSEND "+STR$~CODE%+" +"+STR$~(&C000-&9000+&3600)+" A00"
  170 PRINT"BSAVE ELA,A$A00,L$"+STR$~(&C000-&9000+&3600)
  180 VDU7,7:*APPLE
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
*MSEND CODE% +(&C000-&9000+&3600) A00
```

### Snippet Codice (BASIC)

```basic
+-----------------------------------+   $7000
  |                                   |
  | :2.CODE2                          |
  |                                   |
  +-----------------------------------+   $4000
  |                                   |
  | :2.SCREEN                         |
  |                                   |
  +-----------------------------------+   $2000
  |                                   |
  | :2.DATA                           |
  |                                   |
  +-----------------------------------+   $0B60
  |                                   |
  | Relocation code                   |
  |                                   |
  +-----------------------------------+   $0A00
```

### Snippet Codice (BASIC)

```basic
170 PRINT"BSAVE ELA,A$A00,L$"+STR$~(&C000-&9000+&3600)
  180 VDU7,7:*APPLE
```

### Snippet Codice (BASIC)

```basic
210 PRINT"BSAVE ELB,A$"+STR$~C%+",L$"+STR$~(&9000-C%)
  220 VDU7,7:*APPLE
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
BSAVE <filename>,A$<start_addr>,L$<end_addr>
```

### Snippet Codice (BASIC)

```basic
5 *APPLE
   10 DIM L% &1000
   20 FOR I%=L% TO L%+&2FF
   30 INPUT ?I%
   40 NEXT
```

### Snippet Codice (BASIC)

```basic
130 OSCLI"LOAD :2.DATA "+STR$~(CODE%+&160)
  140 OSCLI"LOAD :2.SCREEN "+STR$~(CODE%+&1600)
  150 OSCLI"LOAD :2.CODE2 "+STR$~(CODE%+&3600)
  160 OSCLI"MSEND "+STR$~CODE%+" +"+STR$~(&C000-&9000+&3600)+" A00"
  170 PRINT"BSAVE ELA,A$A00,L$"+STR$~(&C000-&9000+&3600)
  180 OSCLI"CALL A00"

  190 OSCLI"LOAD :2.CODE1 "+STR$~CODE%
  200 OSCLI"MSEND "+STR$~CODE%+" +"+STR$~(&9000-C%)+" "+STR$~C%
  210 PRINT"BSAVE ELB,A$"+STR$~C%+",L$"+STR$~(&9000-C%)
  220 OSCLI"CALL "+STR$~S%
```

### Snippet Codice (BASIC)

```basic
+-----------------------------------+   $7000
  |                                   |
  | :2.CODE2                          |
  |                                   |
  +-----------------------------------+   $4000
  |                                   |
  | :2.SCREEN                         |
  |                                   |
  +-----------------------------------+   $2000
  |                                   |
  | :2.DATA                           |
  |                                   |
  +-----------------------------------+   $0B60
  |                                   |
  | Relocation code                   |
  |                                   |
  +-----------------------------------+   $0A00
```

### Snippet Codice (BASIC)

```basic
+-----------------------------------+   $FFFF
  |                                   |
  | :2.CODE2 in bank-switched RAM     |
  |                                   |
  +-----------------------------------+   $D000
  :                                   :
  :                                   :

  :                                   :
  :                                   :
  +-----------------------------------+   $7000
  |                                   |
  | :2.CODE2                          |
  |                                   |
  +-----------------------------------+   $4000
  |                                   |
  | :2.SCREEN                         |
  |                                   |
  +-----------------------------------+   $2000
  |                                   |
  | :2.DATA                           |
  |                                   |
  +-----------------------------------+   $0B60
  |                                   |
  | Relocation code                   |
  |                                   |
  +-----------------------------------+   $0A00
```

### Snippet Codice (BASIC)

```basic
+-----------------------------------+   $FFFF
  |                                   |
  | :2.CODE2 in bank-switched RAM     |
  |                                   |
  +-----------------------------------+   $D000
  :                                   :
  :                                   :

  :                                   :
  :                                   :
  +-----------------------------------+   $9000
  |                                   |
  | :2.CODE1                          |
  |                                   |
  +-----------------------------------+   $4000
  |                                   |
  | :2.SCREEN                         |
  |                                   |
  +-----------------------------------+   $2000
  |                                   |
  | :2.DATA                           |
  |                                   |
  +-----------------------------------+   $0B60
  |                                   |
  | Relocation code                   |
  |                                   |
  +-----------------------------------+   $0A00
```

### Snippet Codice (BASIC)

```basic
+-----------------------------------+   $C000
  |                                   |
  | :2.CODE2                          |
  |                                   |
  +-----------------------------------+   $9000
  |                                   |
  | :2.CODE1                          |
  |                                   |
  +-----------------------------------+   $4000
  |                                   |
  | :2.SCREEN                         |
  |                                   |
  +-----------------------------------+   $2000
  |                                   |
  | :2.DATA                           |
  |                                   |
  +-----------------------------------+   $0B60
  |                                   |
  | Relocation code                   |
  |                                   |
  +-----------------------------------+   $0A00
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/developing_apple_ii_elite_on_a_bbc_micro.html](https://elite.bbcelite.com/deep_dives/developing_apple_ii_elite_on_a_bbc_micro.html)*

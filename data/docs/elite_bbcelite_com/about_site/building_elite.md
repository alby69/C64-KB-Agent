---
title: Building Elite from the source
source_url: https://elite.bbcelite.com/about_site/building_elite.html
category: source-code
topics:
- basic
- assembly
difficulty: beginner
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

# Building Elite from the source

If you would like to build a fully working version of Elite on a modern computer, from the exact same source code as on this site, then you will find everything you need in the [accompanying GitHub repositories](https://elite.bbcelite.com#repositories), including full instructions. These repositories replicate the original build process as closely as possible; here we take a look at how the source files are structured and how the build process works.

To keep things simple, let's concentrate on the build process for the BBC Micro cassette Na Acorn Electron versions, which work in the same way. The BBC Micro disc, 6502 Second Processor, Commodore 64, Apple II, BBC Master and Elite-A versions have more files and produce more binaries, but the basic pipeline is essentially the same, while the NES version has its own unique pipeline (as it produces a cartridge rather than a disc).

(I am indebted to Kieran Connell for the following, who designed the modern build pipeline and wrote the original versions of the checksum and verify scripts as part of his epic [elite-beebasm](https://github.com/kieranhj/elite-beebasm) project. Without his original project, none of this would have ever happened...)

## The Elite build pipeline

						                             ------------------------

						The modern build process uses a multi-stage pipeline. This pipeline is based on the original build process from the source disc, but it uses the BeebAsm assembler and Python instead of BBC BASIC.

There are five main folders in each repository, which reflect the progress of the build process (the links will take you to the relevant folders on GitHub for the cassette version):

- [1-source-files](https://github.com/markmoxon/elite-source-code-bbc-micro-cassette/tree/main/1-source-files)contains all the different source files, such as the main assembler source files, image binaries, fonts, boot files and so on.
- [2-build-files](https://github.com/markmoxon/elite-source-code-bbc-micro-cassette/tree/main/2-build-files)contains build-related scripts, such as the checksum, encryption and crc32 verification scripts.
- [3-assembled-output](https://github.com/markmoxon/elite-source-code-bbc-micro-cassette/tree/main/3-assembled-output)contains the output from the assembly process, when the source files are assembled and the results processed by the build files.
- [4-reference-binaries](https://github.com/markmoxon/elite-source-code-bbc-micro-cassette/tree/main/4-reference-binaries)contains the correct binaries for each variant, so we can verify that our assembled output matches the reference.
- [5-compiled-game-discs](https://github.com/markmoxon/elite-source-code-bbc-micro-cassette/tree/main/5-compiled-game-discs)contains the final output of the build process: an SSD disc image that contains the compiled game and which can be run on real hardware or in an emulator.

These folders are used in the multi-stage build process in the following manner: the 1-source-files are assembled, then encrypted and checksummed by the 2-build-files to create the 3-assembled-output, which is optionally verified against the 4-reference-binaries before being compiled into the final 5-compiled-game-discs.

This build process is configured via the project's [Makefile](https://github.com/markmoxon/elite-source-code-bbc-micro-cassette/blob/main/Makefile). Each version is subtly different, but the steps are the same in each case. For the cassette version, the specific build steps are as follows (the links will take you to the relevant source files on GitHub):

- Assemble the main game with [elite-source.asm](https://github.com/markmoxon/elite-source-code-bbc-micro-cassette/blob/main/1-source-files/main-sources/elite-source.asm)
- Concatenate the game code and assemble the header with [elite-bcfs.asm](https://github.com/markmoxon/elite-source-code-bbc-micro-cassette/blob/main/1-source-files/main-sources/elite-bcfs.asm)
- Assemble the loader with [elite-loader.asm](https://github.com/markmoxon/elite-source-code-bbc-micro-cassette/blob/main/1-source-files/main-sources/elite-loader.asm)
- Calculate checksums and add encryption with [elite-checksum.py](https://github.com/markmoxon/elite-source-code-bbc-micro-cassette/blob/main/2-build-files/elite-checksum.py)
- Verify the assembled output with [crc32.py](https://github.com/markmoxon/elite-source-code-bbc-micro-cassette/blob/main/2-build-files/crc32.py)
- Assemble a bootable disc image with [elite-disc.asm](https://github.com/markmoxon/elite-source-code-bbc-micro-cassette/blob/main/1-source-files/main-sources/elite-disc.asm)

This process broadly mirrors the build system on the original source discs. The original source code is split across a number of separate BBC BASIC files, each of which assembles and saves a binary file (the game itself isn't written in BASIC - the source code just uses BBC BASIC's built-in assembler to produce the game). In the cassette version there are ten BASIC source files in all: one for the text tokens, another for the ship blueprints, seven for the main game (A-G), and one for the game's loader.

(For comparison, the 6502 Second Processor version has two separate loader files, the main parasite code is made up of Elite A through Elite J, and there's an additional I/O processor source that runs on the BBC Micro side of the Tube. The BBC Micro disc version, meanwhile, has three loaders, two main code files and 16 ship blueprint files; the BBC Master version has one loader and just two main files, one for the main game code and another for data; and Elite-A has one loader, three main code files, two Tube code files, and 23 ship blueprint files. The Commodore 64 and Apple II versions are variations on this theme, while NES Elite has no loader or blueprint files at all, but has eight ROM banks instead.)

The binary files produced by the BASIC sources are then concatenated and encrypted to give the finished game binaries. This is done by another BBC BASIC program - the "Big Code File" source - and the results are copied to the final game disc. Note that in the modern build process, only the cassette and 6502 Second Processor versions incorporate this BCFS approach, as those are the only two versions for which the original source discs exist. The other versions assemble each source file in one go, as this is trivial on modern machines, and adding the complexity of the BCFS approach seemed a bit pointless.

The modern version of this build process uses BeebAsm instead of BBC BASIC, the encryption is done in Python, and the final product is an SSD disc image, but otherwise the approach is just like the original process. This disc image contains a fully playable version of Elite that you can load into an emulator like JSBeeb or BeebEm, or into a real BBC Micro or Acorn Electron using a device like a Gotek. The code produced is identical to the released version of the game.

Let's take a look at each of the pipeline stages in more detail.

## 1. Assemble the main game with elite-source.asm

						                             -----------------------------------------------

						BeebAsm loads elite-source.asm and creates the following files:

- ELTA.bin
- ELTB.bin
- ELTC.bin
- ELTD.bin
- ELTE.bin
- ELTF.bin
- ELTG.bin
- PYTHON.bin
- SHIPS.bin
- WORDS9.bin

elite-source.asm contains the main source code for Elite. It is based on the original BASIC source files, converted to BeebAsm assembler syntax. In the original build, this is what happens:

- ELITEA produces the ELTA binary
- ELITEB produces the ELTB binary
- ELITEC produces the ELTC binary
- ELITED produces the ELTD binary
- ELITEE produces the ELTE binary
- ELITEF produces the ELTF binary
- ELITEG produces the ELTG binary
- DIALSHP contains the PYTHON binary
- SHPPRTE produces the SHIPS binary
- GENTOK produces the WORDS9 binary

So the BeebAsm process mirrors the original compilation steps pretty closely.

## 2. Concatenate the game code and compile the header with elite-bcfs.asm

						                             -----------------------------------------------------------------------

						BeebAsm then loads elite-bcfs.asm, which reads the following files:

- ELTA.bin
- ELTB.bin
- ELTC.bin
- ELTD.bin
- ELTE.bin
- ELTF.bin
- ELTG.bin
- SHIPS.bin

and creates the following:

- ELTcode.unprot.bin
- ELThead.bin

elite-bcfs.asm is the BeebAsm version of the BASIC source file S.BCFS, which is responsible for creating the "Big Code File" - i.e. concatenating the ELTA to ELTG binaries plus the SHIPS data into a single executable called ELTcode.

There is also a simple checksum test added to the start of the ELTcode file, but at this stage the compiled code is not encrypted, which is why it has "unprot" in the name. The original BASIC files contain encryption code that can't be replicated in BeebAsm, so we do this using Python in step 4 below.

## 3. Assemble the loader with elite-loader.asm

						                             --------------------------------------------

						Next, BeebAsm loads elite-loader.asm, which reads the following files:

- images/P.DIALS.bin
- images/P.ELITE.bin
- images/P.A-SOFT.bin
- images/P.(C)ASFT.bin
- WORDS9.bin
- PYTHON.bin

and creates the following:

- ELITE.unprot.bin

This is the BeebAsm version of the BASIC source file ELITES, which creates the executable Elite loader ELITE. This is responsible for displaying the title screen and planet, loading the dashboard image, setting up interrupt routines, configuring a number of operating system settings, relocating code to lower memory (below PAGE), and finally loading and running the main game.

The loader incorporates four image binaries from the images folder that, together with the code to draw the Saturn backdrop, make up the loading screen. It also incorporates the WORDS9 and PYTHON data files that contain the game's text and the Python ship blueprint.

There are also a number of checksum and protection routines that EOR the code and data with other parts of memory in an attempt to obfuscate and protect the game from tampering. This can't be done in BeebAsm, so we do this using Python in the next step.

## 4. Calculate checksums and add encryption with elite-checksum.py

						                             ----------------------------------------------------------------

						Next, the pipeline runs the Python script elite-checksum.py, which reads the following files:

- ELTA.bin
- ELTB.bin
- ELTC.bin
- ELTD.bin
- ELTE.bin
- ELTF.bin
- ELTG.bin
- ELThead.bin
- SHIPS.bin
- ELITE.unprot.bin

and creates the following:

- ELTcode.bin
- ELITE.bin

There are a number of checksum and simple EOR encryption routines that form part of the cassette version's build process. These were trivial to interleave with the assembly process in the original BASIC source files, but they've been converted into Python so they can run on modern machines (as not too many modern computers support BBC BASIC out of the box). Kieran Connell is the genius behind all this Python magic, so many thanks to him for cracking the code for the cassette version (which inspired me to do the same for the other versions).

The cassette version's Python script has two parts. The first part generates an encrypted version of the ELTcode binary, based on the code in the original BASIC source program S.BCFS, as follows:

- Concatenate all the compiled binaries
- Compute the checksum for the commander data
- Poke the checksum value into the binary
- Compute the checksum for all the game code except the header
- Poke the checksum value into the binary
- Encrypt all the game code except the header using a cycling EOR value (0-255)
- Compute the final checksum for the game code
- Output the encrypted ELTcode binary

The second part implements the checksum and encryption functions from the original BASIC source program ELITES, to generate an encrypted ELITE binary as follows:

- Reverse the bytes for a block of code that is placed on the stack
- Compute the checksum for MAINSUM
- Poke the checksum value into the binary
- Compute the checksum for CHECKbyt
- Poke the checksum value into the binary
- Encrypt a block of code by EOR'ing with the code to be placed on the stack
- Encrypt the code destined for lower RAM by EOR'ing with the loader boot code
- Encrypt binary data (dashboard etc.) by EOR'ing with the loader boot code
- Output the encrypted ELITE binary

At the end of all this we have two encrypted binaries, one for the loader and another for the main game.

## 5. Verify the assembled output with crc32.py

						                             --------------------------------------------

						By default the crc32.py script is run on the results, which compares the assembled output with the binaries from the original build process. This enables us to confirm that our output is correct.

The verification output for the cassette version is as follows:

[--originals--] [---output----] Checksum Size Checksum Size Match Filename ----------------------------------------------------------- a88ca82b 5426 a88ca82b 5426 Yes ELITE.bin f40816ec 5426 f40816ec 5426 Yes ELITE.unprot.bin 0f1ad255 2228 0f1ad255 2228 Yes ELTA.bin e725760a 2600 e725760a 2600 Yes ELTB.bin 97e338e8 2735 97e338e8 2735 Yes ELTC.bin 322b174c 2882 322b174c 2882 Yes ELTD.bin 29f7b8cb 2663 29f7b8cb 2663 Yes ELTE.bin 8a4cecc2 2721 8a4cecc2 2721 Yes ELTF.bin 7a6a5d1a 2340 7a6a5d1a 2340 Yes ELTG.bin 01a00dce 20712 01a00dce 20712 Yes ELTcode.bin 1e4466ec 20712 1e4466ec 20712 Yes ELTcode.unprot.bin 00d5bb7a 40 00d5bb7a 40 Yes ELThead.bin 99529ca8 256 99529ca8 256 Yes PYTHON.bin 49ee043c 2502 49ee043c 2502 Yes SHIPS.bin c4547e5e 1023 c4547e5e 1023 Yes WORDS9.bin

In this case all the assembled binaries match the original binaries, so our build process has worked.

## 6. Assemble a bootable disc image with elite-disc.asm

						                             -----------------------------------------------------

						Finally, BeebAsm loads elite-disc.asm, which reads the following files:

- boot-files/$.!BOOT.bin
- basic-programs/$.ELITE.bin
- ELITE.bin
- ELTcode.bin

and creates the following:

- elite-cassette-from-source-disc.ssd

This script builds the final disc image, to match the released version of the game (albeit on a disc rather than a cassette). Note that the name of the disc image depends on the variant that's being built - the name shown above is the default build, which builds the version from the original source discs for the cassette version.

The names of the files in the released version of cassette Elite are slightly different to those produced by the build process from the source disc, because the released disc also contains Acornsoft's iconic mode 7 loading screen in a BASIC program called ELITE. As a result, the ELITE binary that the build process generates for the Elite loader in step 4 gets renamed to ELTdata. The final disc image therefore contains the following files:

- !BOOT - a boot file that is *EXECuted on a Shift-Break and simply CHAINs the ELITE program
- ELITE - displays the mode 7 Acornsoft loading screen for Elite, and then *RUNs the Elite loader in ELTdata
- ELTdata - the Elite loader with its Saturn loading screen, renamed from the original ELITE file that's produced by the build process
- ELTcode - the main game code

Note that by default, the build process produces a version of the cassette game that can be loaded from disc, so the above names are designed to fit into the seven-character limit of DFS. You can build a genuine cassette version by setting the DISC configuration variable to FALSE, in which case the filenames will be ELITEdata and ELITEcode.

The disc image can be loaded into an emulator, or into a real BBC Micro using a device like a Gotek.


						                             ------------------------------------

						For more details on how to run this process on a modern computer, and for all the sources and build files you need to run this on your PC, Mac or Linux box, see the accompanying GitHub repositories:

- [Fully buildable source for the BBC Micro cassette version](https://github.com/markmoxon/elite-source-code-bbc-micro-cassette)
- [Fully buildable source for the BBC Micro disc version](https://github.com/markmoxon/elite-source-code-bbc-micro-disc)
- [Fully buildable source for the Elite Demonstration Disc](https://github.com/markmoxon/elite-demo-source-code-bbc-micro)
- [Fully buildable source for the Acorn Electron version](https://github.com/markmoxon/elite-source-code-acorn-electron)
- [Fully buildable source for the 6502 Second Processor version](https://github.com/markmoxon/elite-source-code-6502-second-processor)
- [Fully buildable source for the Commodore 64 version](https://github.com/markmoxon/elite-source-code-commodore-64)
- [Fully buildable source for the Apple II version](https://github.com/markmoxon/elite-source-code-apple-ii)
- [Fully buildable source for the BBC Master version](https://github.com/markmoxon/elite-source-code-bbc-master)
- [Fully buildable source for the NES version](https://github.com/markmoxon/elite-source-code-nes)
- [Fully buildable source for Elite-A](https://github.com/markmoxon/elite-a-source-code-bbc-micro)

In each case the source code on GitHub is identical to the code on this site (in fact, this website is generated from the GitHub repositories, so they are guaranteed to be identical).

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
[--originals--]  [---output----]
  Checksum   Size  Checksum   Size  Match  Filename
  -----------------------------------------------------------
  a88ca82b   5426  a88ca82b   5426   Yes   ELITE.bin
  f40816ec   5426  f40816ec   5426   Yes   ELITE.unprot.bin
  0f1ad255   2228  0f1ad255   2228   Yes   ELTA.bin
  e725760a   2600  e725760a   2600   Yes   ELTB.bin
  97e338e8   2735  97e338e8   2735   Yes   ELTC.bin
  322b174c   2882  322b174c   2882   Yes   ELTD.bin
  29f7b8cb   2663  29f7b8cb   2663   Yes   ELTE.bin
  8a4cecc2   2721  8a4cecc2   2721   Yes   ELTF.bin
  7a6a5d1a   2340  7a6a5d1a   2340   Yes   ELTG.bin
  01a00dce  20712  01a00dce  20712   Yes   ELTcode.bin
  1e4466ec  20712  1e4466ec  20712   Yes   ELTcode.unprot.bin
  00d5bb7a     40  00d5bb7a     40   Yes   ELThead.bin
  99529ca8    256  99529ca8    256   Yes   PYTHON.bin
  49ee043c   2502  49ee043c   2502   Yes   SHIPS.bin
  c4547e5e   1023  c4547e5e   1023   Yes   WORDS9.bin
```



---
*Fonte originale: [https://elite.bbcelite.com/about_site/building_elite.html](https://elite.bbcelite.com/about_site/building_elite.html)*

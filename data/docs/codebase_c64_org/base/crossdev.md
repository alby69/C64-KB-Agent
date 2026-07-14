---
title: Cross Development
source_url: https://codebase.c64.org/doku.php?id=base%3Acrossdev
category: tutorial
topics:
- basic
- sprite programming
- assembly
difficulty: beginner
language: mixed
hardware:
- VIC-II
- CPU
- KERNAL
related:
- sprite-programming
- memory-map
- raster-interrupts
- kernal-routines
- vic-ii-registers
scraped_at: '2026-07-14'
---

# Cross Development

### Table of Contents

# Cross Development

Use that PC for something good!

## Setting up a cross development environment

- [Tools for putting files into a .d64 image](https://codebase.c64.org/doku.php?id=crossdev:tools_for_putting_files_into_a_.d64_image)- by Frantic
- [Makefile to use with ca65 & VICE](https://codebase.c64.org/doku.php?id=base:makefile_to_use_with_ca65_vice)- by Jupp3
- [Cross Development using Makefile](https://codebase.c64.org/doku.php?id=base:cross_development_using_makefile)- A Tutorial explaining automated building of your c64 projects. - by Burglar

## Debugging

- [Using the VICE monitor](https://codebase.c64.org/doku.php?id=base:using_the_vice_monitor)- by radiantx
- [Using a running VICE session for development](https://codebase.c64.org/doku.php?id=base:using_a_running_vice_session_for_development)- by Compyx

## Crunching

- [Exomizer Level Compression/Decompression for beginners](https://codebase.c64.org/doku.php?id=crossdev:exomizer_level_compress_decompression_for_beginners)- by Richard / TND
- [Exomizer making custom oldschool decrunch effects](https://codebase.c64.org/doku.php?id=base:exomizer_making_custom_oldschool_decrunch_effects)- by StatMat and Richard/TND
- [Exomizer adding decrunch splash screens during sfx decrunch](https://codebase.c64.org/doku.php?id=base:exomizer_adding_decrunch_splash_screens_during_sfx_decrunch)= by Richard / TND

## Graphics conversion

- [Sprite Converter](https://codebase.c64.org/doku.php?id=base:sprite_converter)- a simple tool (Python script) to convert images to fields of sprites
- [Sprite data and KickAssembler](https://codebase.c64.org/doku.php?id=base:sprite_data_and_kickassembler)- How to use KickAss to directly include sprites in .gif format

## Assemblers and Cross-dev systems

This section contains information relating to specific assemblers of cross-dev systems.

Also check the [syntax highlighting section](https://codebase.c64.org/doku.php?id=base:crossdev#syntax_highlighting) below which contains syntax highlighting files for various assemblers for various text editors.

Also have a look at the [source code conversion](https://codebase.c64.org/doku.php?id=source_conversion) page if you want to know how to convert your sources from turbo assembler (petscii) to ascii, and how to (re)indent code that is messy. Also note that there is a list of commonly used assemblers on the [Most used tools](https://codebase.c64.org/doku.php?id=tools:start) page.

### ACME

- [Small Tutorial on how to use Macros in ACME](https://codebase.c64.org/doku.php?id=base:acme-macro-tut)- by St0fF/Neoplasia^theObsessedManiacs

- [ACME win32 binary](https://codebase.c64.org/lib/exe/fetch.php?media=sourcecode:acme093exe2.zip)and- [ACME source](https://codebase.c64.org/lib/exe/fetch.php?media=sourcecode:acme093src2.zip)includes some tweaks I made from the base ACME 0.93 tree to add some development helpers when using the Microsoft Visual Studio IDE:- Compiler fixes for Microsoft Visual Studio 6.0
- Added –msvc to output warnings/erros in the MS IDE format. Pressing F4 in the IDE will jump to the next warning/error.
- Added –vicelabeldump and the PO !svl to save referenced global labels in VICE monitor format. When loaded in the monitor these labels are displayed in the disassembly.
- Added the PO !sal to cause !sl and !svl to save all referenced labels including local labels. This is useful if separate zones have labels you want to know while debugging.
 

### ca65

ca65 is an assembler which is part of the cc65 suite of tools.

- [Create labels on the fly using macros](https://codebase.c64.org/doku.php?id=base:create_labels_on_the_fly_using_macros)- by RadiantX (taken from CSDb)

### DreamAss

DreamAss is perhaps the most turbo-assembler-alike assembler, expanded with macros.

### Kick Assembler

- [Kick Assembler macros](https://codebase.c64.org/doku.php?id=base:kick_assembler_macros)- by Various
- [C64 Kickass IDE](http://back2theretro.blogspot.com.au/)- Full IDE includes many tools
- Kick Assembler development with[Sublime Text 3](http://www.sublimetext.com/3):- Sublime Package (Package control):[Kick Assembler (C64)](https://sublime.wbond.net/packages/Kick%20Assembler%20(C64))
- [Page](https://goatpower.org/projects-releases/sublime-package-kick-assembler-c64/)with details on installation, features and tips
 

### PDS (Programmers Development System)

- [PDS](https://codebase.c64.org/doku.php?id=base:pds)- Info and resources related to PDS

### CBM .prg Studio

- [CBM .prg Studio](http://www.ajordison.co.uk/index.html)- ML and BASIC dev environment targetting most 8 bit machines (64/128/VIC20/16/Plus4/PET). Integrated assembler/debugger & sprite/char/screen designer (Windows)

### C64 Studio

- [C64 Studio](http://www.georg-rottensteiner.de/index.html)- Assembler and BASIC development tailored to game development. Contains sprite/char/graphic/screen/map editors, media managers, supports remote debugging via VICE.
- Supports CPU types 6502, 6510, 65C02, R65C02, W65C02, 65CE02, 4502, M65 (Mega65)
- Supports several assembler syntaxes (ACME foremost, DASM, PDS)
- Open Source (MIT license)[https://github.com/GeorgRottensteiner/C64Studio](https://github.com/GeorgRottensteiner/C64Studio)

### xa65

- [The xa65 cross assembler](http://www.floodgap.com/retrotech/xa/)is a small and simple cross assembler for Unix/Linux systems. It is available under GPLv2.

## Syntax Highlighting

This section is for 6502/6510 assembler syntax highlighting files.

- [64tass, Crimson Editor, windows](https://codebase.c64.org/lib/exe/fetch.php?media=base:6510-asm-crimson.zip)- by Hein

- [ACME, EMACS, multi-platform](https://codebase.c64.org/lib/exe/fetch.php?media=base:acme-mode.el.zip)- By Abaddon/Fairlight (more info- [here](http://noname.c64.org/csdb/release/?id=93353&show=summary#summary))
- [ACME, UltraEdit, windows](https://codebase.c64.org/lib/exe/fetch.php?media=base:ultraedit_acme_wordfile.zip)- by Fredrik Ramsberg
- [ACME, VIM, multi-platform](https://codebase.c64.org/lib/exe/fetch.php?media=base:acme_vim.tar.gz)- by Bitbreaker/Nuance^Metalvotze
- [ACME, Katepart (any KDE Text-Editor, like Kate, KDevelop, KWrite can use this](https://codebase.c64.org/lib/exe/fetch.php?media=tools:acme.xml.tar.gz)- by St0fF/Neoplasia^theObsessedManiacs
- [ACME Assembler, Sublime Text 3, multi-platform](http://www.csdb.dk/release/?id=126930)- by Fix/Onslaught
- [base:acme_notepadplusplus_syntax](https://codebase.c64.org/doku.php?id=base:acme_notepadplusplus_syntax)— by Strykker

- [ca65, 6502 bundle for TextMate, mac](https://codebase.c64.org/lib/exe/fetch.php?media=base:6502_assembler.tmbundle.zip)- by MagerValp

- [DreamAss 6502 highlighting file for "Kate" (from KDE), Linux](https://codebase.c64.org/lib/exe/fetch.php?media=base:dreamass.xml.zip)- by DocBacardi and Count Zero
- [DreamAss 6502 highlighting config for "Sublime Text 2 and 3", Linux only](https://codebase.c64.org/lib/exe/fetch.php?media=base:dreamass_sublime_2_3_highlightlings_2014-01-21.zip)with Makefile project - by Count Zero

- [KickAssembler, UltraEdit, windows](https://codebase.c64.org/lib/exe/fetch.php?media=sourcecode:kickass_6502.zip)- by PMC
- [Visual Studio 6502 Language Extension, windows](http://noname.c64.org/csdb/release/?id=90437)- by Pantaloon/FLT
- [Language definition for 6502 asm (k2asm), gedit](http://k2.untergrund.net/k2asm/k2src.lang)- by yago/K2
- [KickAssembler, Notepad++, Windows](https://codebase.c64.org/lib/exe/fetch.php?media=tools:kickassembler.xml.zip)- by Skid Row
- [KickAssembler, Vim, multi-platform](http://www.vim.org/scripts/script.php?script_id=4121)- by gryf/Elysium
- [Kick Assembler, Sublime Text 3, multi-platform](https://goatpower.org/projects-releases/sublime-package-kick-assembler-c64/)- by Swoffa/Noice
- [Kick Assembler, Atom, multi-platform](https://github.com/ProbablyNotArtyom/language-6502-kickass)- by NotArtyom

## Ways to transfer your code to C64

- [Final replay and Codenet](http://www.oxyron.de/html/freplay.html)- by Graham/Oxyron. Requires a cartridge with RR-net.
- [RR.exe](http://hitmen.c02.at/html/tools_rr.html)- by Groepaz/Hitmen. Requires a Retro Replay cartdrige with SilverSurfer.
- [http://commodoreserver.com](http://commodoreserver.com)– Allows accessing .d64 images (you can upload to the site) from a real C64 via virtual drive software. Currently supports Comet64 internet modem, but RR-net/64nic versions are being developted.
- [64net NG](http://noname.c64.org/csdb/release/?id=100099)- by Bitbreaker/Nuance^Metalvotze

---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Acrossdev](https://codebase.c64.org/doku.php?id=base%3Acrossdev)*

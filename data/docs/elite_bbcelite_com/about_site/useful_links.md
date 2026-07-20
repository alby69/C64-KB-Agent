---
title: Useful links
source_url: https://elite.bbcelite.com/about_site/useful_links.html
category: tutorial
topics:
- memory management
- assembly
- input handling
- basic
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

# Useful links

Here's a collection of links that I've found useful or interesting when working on this project.

## General

						                             -------

						- [Ian Bell's Elite site](http://www.elitehomepage.org/)- The most important source for 8-bit Elite fans, quite literally, as without the original source discs released here, none of this would be possible; thank you for the wonderful gift, Ian!
- [Ian Bell's handwritten dev docs](http://www.elitehomepage.org/design/)- Fascinating relics from the actual development process of Elite
- [Frontier Astro](https://www.frontierastro.co.uk/)- If, like me, you don't own all the physical Elite versions but would love to, this is a wonderful resource
- [Elite wiki classic articles](http://wiki.alioth.net/index.php/Category:Classic)- The Elite wiki gave me a head start on a number of topics and is a highly recommended read
- [The alt.fan.elite FAQ](http://bbc.nvg.org/doc/games/EliteFAQ.htm)- I've read this FAQ many times over the years, and although it contains a few errors, it's still a great read from the Usenet era
- [Elite-A](http://knackered.org/angus/beeb/elite.html)- Angus Duggan's Elite-A page, where you can find instructions and download links for his extended version of Elite

## BBC Micro and Acorn Electron user guides

						                             ----------------------------------------

						- [The BBC Microcomputer User Guide](https://stardot.org.uk/forums/viewtopic.php?t=14024)- The original guide that came with the BBC Micro, giving an excellent introduction to the machine
- [The Advanced User Guide for the BBC Micro](https://stardot.org.uk/forums/viewtopic.php?t=17242)- My most-thumbed book, which permanently lies by the side of my trusty Beeb, open at the assembly mnemonics section
- [The Electron User Guide](https://www.retro-kit.co.uk/user/custom/Acorn/8bit/Electron/manuals/Acorn_ElectronUG.pdf)- The guide that came with the Acorn Electron, which contains a pretty good section on assembly language
- [The Acorn Electron Advanced User Guide](https://stardot.org.uk/forums/viewtopic.php?t=23193)- The most in-depth reference book for the Acorn Electron, remastered for modern PDF readers

## BBC Micro information and tools

						                             -------------------------------

						- [BBC ASCII character set](http://beebwiki.mdfs.net/ASCII)- I can't tell you how many times I've had to refer to this table when disassembling Elite; I probably should have just printed it out!
- [BBC MOS disassembly](https://tobylobster.github.io/mos/index.html)- I found this particularly useful when trying to decipher keyboard translation tables and OS calls
- [Acorn MOS disassembly](https://github.com/tom-seddon/acorn_mos_disassembly)- A brilliant collection of MOS disassemblies for the BBC Master
- [Electron OS disassembly](https://github.com/tom-seddon/electron_os_disassembly)- A very useful disassembly of the Electron operating system
- [BBC memory map](http://8bs.com/mag/32/bbcmemmap1.txt)- When every single byte counts, as it does in Elite, a map is an essential part of the toolkit
- [Hex and binary converter](https://www.mathsisfun.com/binary-decimal-hexadecimal-converter.html)- Probably the web tool I used the most during this project, especially when converting numbers into binary
- [The 76489 sound chip](https://mansfield-devine.com/speculatrix/2019/11/fun-with-chips-2-sn76489-sound-generator-ic/)- I'm not sure I fully understand the sound chip in the Beeb, but this article really helps explain things
- [Teletext page editor](https://zxnet.co.uk/teletext/editor/)- A really useful tool for designing BBC Micro teletext screens, which I used to create the dashboard in Teletext Elite

## BBC Micro and Electron emulators

						                             --------------------------------

						- [b2](https://github.com/tom-seddon/b2)- A Beeb emulator with brilliant debugging capabilities that happily works on the Mac, and which is now my go-to emulator for complex disassembly projects like this
- [JSBeeb (BBC Micro)](https://bbc.xania.org/)- An absolute tour-de-force from Matt Godbolt, this browser-based emulator is brilliant for testing Elite builds in all the variations of the BBC Micro and Master
- [Using the JSBeeb debugger](https://github.com/mattgodbolt/jsbeeb/wiki/Debugger)- A very useful tool when trying to work out what all those zero-page locations actually do
- [BeebEm](https://github.com/stardot/beebem-windows)- An oldie but a goldie, and particularly useful for screenshots
- [beebjit](https://github.com/scarybeasts/beebjit)- The best BBC emulator for playing with disc protection on the original discs
- [B-em](https://github.com/stardot/b-em)- You can never have too many BBC Micro emulators, right?
- [Electroniq](https://0xc0de6502.github.io/electroniq/)- A brilliant browser-based emulator from the incomparable 0xC0DE
- [Elkulator](https://www.elkulator.acornelectron.co.uk/)- The original Electron emulator is still the best option for emulating ADFS, joysticks and sideways RAM

## BBC Micro and Electron assemblers and disassemblers

						                             ---------------------------------------------------

						- [BeebAsm](https://github.com/stardot/beebasm)- The wonderful 6502 assembler that powers the versions that are documented on this site
- [py8dis](https://github.com/ZornsLemma/py8dis)- An absolutely fantastic tool for disassembling original game binaries
- [BeebDis](https://github.com/prime6809/BeebDis)- I found this really useful for disassembling the disc, Master and Electron versions, for which the source discs are lost in time
- [VSCode, max65 and the Electroniq debugger extension](https://github.com/0xC0DE6502/electroniq-debugger-extension)- This fully featured Electron development environment from 0xC0DE is an absolute game-changer for Electron development

## 6502 Second Processor information

						                             ---------------------------------

						- [6502 Second Processor programming](http://ffe3.com/tom/tube.html)- A brilliant article about how the Tube works from the incomparable Tom Seddon
- [Acorn's Tube application notes (PDF)](https://elite.bbcelite.com/pdfs/Tube_Application_Note_004.pdf)- The best source of official Tube information, crammed full of details about the 6502 Second Processor
- [The 6502 Second Processor boxed version](https://stardot.org.uk/forums/viewtopic.php?t=19917)- Rare as hen's teeth and very kindly archived by the owner, what a prize!
- [Getting the 6502 Second Processor sources to compile](https://stardot.org.uk/forums/viewtopic.php?t=14607)- If you want to build 6502SP Elite from the original discs, you'll need to read this first

## Universe in a bottle

						                             --------------------

						- [Market prices in Acornsoft Elite](http://typethinker.blogspot.com/2014/10/market-prices-in-acornsoft-elite.html)- A really interesting blog post about trade prices in Elite
- [Random number generator](http://wiki.alioth.net/index.php/Random_number_generator)- A great article on the Elite wiki about the generation and use of the galaxy and system seeds
- [Random number generation](https://www.christianpinder.com/articles/pseudo-random-number-generation/)- This doesn't describe the algorithm in Elite, but it's still a great introduction to the topic
- [Matt Godbolt on text tokens](https://xania.org/201406/elites-crazy-string-format)- I wish I'd read this before tackling the text token system, as it's a great read

## Ships, planets and suns

						                             -----------------------

						- [Classic Elite ships wireframe](http://wiki.alioth.net/index.php/Classic_Elite_ships_wireframe)- A detailed introduction to ship data blocks and what all those bytes actually mean
- [Yaw and pitch matrices](http://msl.cs.uiuc.edu/planning/node102.html)- The heart of Elite's rotation mechanism, explained in matrix format
- [Ian Bell's scribbled yaw/pitch calculations](http://www.elitehomepage.org/design/index.htm)- The original matrix calculations from the handwritten cache of dev documents
- [The small angle approximation](https://en.wikipedia.org/wiki/Small-angle_approximation)- This hack is absolutely fundamental to squeezing the above maths into 8 bits
- [Wikipedia entrry on trigonometric identities](https://en.wikipedia.org/wiki/List_of_trigonometric_identities)- A handy list of equivalents and expansions for trigonometric functions
- [Loading screen Saturn of Elite](https://wendigo.online-siesta.com/elite/saturn.html)- A JavaScript version of the Saturn from the loading screen
- [Sun of Elite](https://wendigo.online-siesta.com/elite/sun.html)- A JavaScript version of the shimmering sun

## 6502 assembly code

						                             ------------------

						- [Online 6502 disassembler](https://www.masswerk.at/6502/disassembler.html)- A super-handy web-based disassembler that takes hex bytes and returns 6502 assembly code
- [6502 optimisations](https://www.nesdev.org/wiki/6502_assembly_optimisations)- Not all of these optimisations are used in Elite, but quite a few of them are
- [Compare and branch logic](http://6502.org/tutorials/compare_instructions.html)- If, like me, you can never remember whether it should be a BCC or a BCS after a CMP, this will put you straight
- [Multiply and divide in 6502](https://llx.com/Neil/a2/mult.html)- A really good explanation of the kind of bit manipulation that Elite implements in its maths routines
- [BIT hopping with EQUB &2C](http://forum.6502.org/viewtopic.php?t=1614)- An interesting thread on a technique that Elite uses quite a lot

## Commodore 64 information

						                             ------------------------

						- [Commodore 64 Programmer's Reference Guide](https://pickledlight.blogspot.com/p/commodore-64-guides.html)- The official guide to the Commodore 64, published by Commodore and remastered for easy reading on modern machines
- [Commodore documentations](https://sta.c64.org/cbmdocs.html)- The best quick-reference site for everything C64, from Kernal functions to memory maps
- [Commodore 64 memory map](https://sta.c64.org/cbm64mem.html)- Essential information for anyone working with the Commodore 64 at machine level
- [The 6510 processor port](https://www.c64os.com/post/6510procport)- An excellent explanation of the different memory configurations on the Commodore 64
- [C64 Kernal API](https://www.pagetable.com/c64ref/kernal/)- The ultimate reference for the Commodore 64's kernal calls
- [How the keyboard works](https://c64os.com/post/howthekeyboardworks)- Lots of detail about the Commodore 64 keyboard and how it works
- [PAL vs NTSC](http://unusedino.de/ec64/technical/misc/vic656x/pal-ntsc.html)- Information on the difference between the PAL and NTSC models of the Commodore 64
- [Elite Harmless](https://github.com/Kroc/elite-harmless)- A project to disassemble and improve Commodore 64 Elite; a useful companion when exploring the Commodore 64 version

## Apple II information

						                             --------------------

						- [Apple II graphics: More than you wanted to know](https://nicole.express/2024/phasing-in-and-out-of-existence.html)- An excellent look at the hardware behind the high-resolution screen mode
- [HIRES Graphics on Apple II](https://www.xtof.info/hires-graphics-apple-ii.html)- A good summary of the Apple II's high-resolution screen mode
- [Understanding the Apple II](https://archive.org/details/understanding_the_apple_ii/)- If you weant to know exactly how the Apple II hardware works, Jim Sather's book is a must-read
- [The Amazing Disk II Controller Card](https://www.bigmessowires.com/2021/11/12/the-amazing-disk-ii-controller-card/)- A brilliant article about Steve Wozniak's epic disk interface card
- [Beneath Apple DOS](https://archive.org/details/beneath-apple-dos-2020/)- The best reference book for Apple DOS, which explains all the concepts used in the RWTS routines in Elite
- [Apple II DOS Source Code](https://computerhistory.org/blog/apple-ii-dos-source-code/)- The Computer History Museum's release of the original DOS 3.1 source code
- [Apple II DOS 3.3 C Source Code Listing](https://elite.bbcelite.com/pdfs/apple2_SRC_DOS33C_1983.pdf)- The annotated Apple DOS 3.3 source code that I've quoted in this commentary
- [Apple IIjs](https://www.scullinsteel.com/apple2/)- A fully functional Apple II emulator in a browser

## Nintendo Entertainment System (NES) information

						                             -----------------------------------------------

						- [An Overview of NES Rendering](https://austinmorlan.com/posts/nes_rendering_overview/)- A great introduction to how the NES builds screens out of tiles
- [Nintendo Entertainment System (NES) Architecture](https://www.copetti.org/writings/consoles/nes/)- A very approachable summary of the NES architecture
- [Nerdy Nights](https://nerdy-nights.nes.science)- An excellent collection of tutorials on programming the NES
- [NESdev wiki](https://www.nesdev.org/wiki)- An absolute goldmine for NES developers
- [Mesen 2](https://github.com/SourMesen/Mesen2)- My preferred NES emulator for debugging and analysing code
- [The Ian Bell Interview](http://www.elitehomepage.org/archive/b5081501.htm)- Ian Bell's thoughts on NES Elite being his favourite published conversion
- [Elite FAQ (answers from David Braben)](http://www.elitehomepage.org/archive/c2031200.htm)- David Braben's thoughts on the best versions of Elite
- [Elite music](http://www.vgmpf.com/Wiki/index.php?title=Elite_(NES)#Music)- Details of the various tunes used in NES Elite
- [NES (Famicom) Development Kit Hardware](https://www.retroreversing.com/famicom-nes-development-kit/#programmers-development-system-pds)- Information about the Programmers Development System (PDS) used to write NES Elite

## Archimedes Elite

						                             ----------------

						- [Archimedes Elite on Ian Bell's site](http://www.elitehomepage.org/arc/index.htm)- A downloadable version of one of the best conversions of Elite
- [Cracking RISC OS Elite](https://tautology.org.uk/blog/2023/10/09/cracking-risc-os-elite/)- A neat introduction to hacking Archimedes Elite via relocatable module

## The history of Elite

						                             --------------------

						- [GDC classic game post-mortem](https://www.gdcvault.com/play/1014628/Classic-Game-Postmortem)- A fascinating romp through the development of Elite with co-author David Braben
- [Right on Commander!](https://rightoncmdr.wordpress.com/the-elite-story/)- Probably my favourite article about the history of Elite, originally from Retro Gamer
- [Elite (or, The Universe on 32K Per Day)](https://www.filfre.net/2013/12/elite/)- The Digital Antiquarian's excellent and very detailed article about the history of Elite
- [Masters of their universe](https://www.theguardian.com/books/2003/oct/18/features.weekend)- A great article in The Guardian containing the bulk of the Elite section from Backroom Boys
- [Elite on Wikipedia](https://en.m.wikipedia.org/wiki/Elite_(video_game))- A handy summary of what happened and when
- [David Braben - A Life in Pixels](https://www.youtube.com/watch?v=PJlxHeUZ_bQ)- An interesting BAFTA interview with David Braben, in which he plays the original Elite
- [Q&A: David Braben - from Elite to today](https://www.gamespot.com/articles/qanda-david-braben-from-elite-to-today/1100-6162140/)- Another David Braben interview
- [Rob Northen interview](http://zakalwe.fi/~shd/amiga-cracking/rob_northen_interview.txt)- A chat with the man behind the copy protection used in the original Elite
- [The Platform and the Player: exploring the (hi)stories of Elite](http://gamestudies.org/1302/articles/agazzard)- An interesting academic paper about Elite
- [The History of Elite: Space, the Endless Frontier](https://www.gamedeveloper.com/design/the-history-of-elite-space-the-endless-frontier)- A cracking read, full of detail about how Elite fits into gaming history
- [The Life of Pi](https://www.newstatesman.com/science-tech/technology/2017/02/life-pi-0)- There's some interesting stuff about Elite in this interview with David Braben about the Raspberry Pi
- [Interview about Elite Z80 conversions](https://www.ricardopinto.com/2022/09/19/interview-about-elite-z80-conversions/)- A fascinating chat with Ricrado Pinto of Torus about the ZX Spectrum conversion of Elite

## Anaglyph 3D

						                             -----------

						- [Calculating Stereo Pairs](https://paulbourke.net/stereographics/stereorender/)- A handy introduction to anaglyph 3D and parallax (though note that red and blue are a different way around to most anaglyph glasses)
- [3D in 3D: Rendering anaglyph stereographics in real time](https://ubm-twvideo01.s3.amazonaws.com/o1/vault/gdc07/slides/S3729i1.pdf)- A slideshow from the 2007 Game Developers Conference that explains eye spacing and skew
- [Anaglyph 3D games on Moby Games](https://www.mobygames.com/group/1937/anaglyph-3-d-support-3-d-glasses/)- A list of all the anaglyph 3D games in the Moby Games database (it isn't very long!)

## Other Elite projects

						                             --------------------

						- [Elite for BeebAsm](https://github.com/kieranhj/elite-beebasm)- Kieran Connell's original BeebAsm port, without which this project would never have cleared the first hurdle
- [Original Stardot thread about Elite for BeebAsm](https://stardot.org.uk/forums/viewtopic.php?t=15375)- This is the thread I stumbled across during lockdown that started the whole thing
- [Elite for VIC 20](https://vic20elite.wordpress.com/)- Aleksi Eeben's astonishing version of Elite, backported from the Commodore 64 to the VIC 20
- [Elite Harmless](https://github.com/Kroc/elite-harmless)- A knockout project from Kroc Camen that's taking the Commodore 64 version and making it even better
- [1337 (Elite for the Oric)](https://defenceforce.itch.io/1337)- A brilliant version of Elite for the Oric by DefenceForce, and a worthy winner of the 2010 Oldschool Gaming Game Of The Year award
- [Elite: The New Kind source](https://github.com/fesh0r/newkind)- For those of us disassembling Elite, Christian Pinder is a complete legend, and this is the reason why
- [Apple Elite disassembly](https://6502disassembly.com/a2-elite/Elite.html)- Brilliant work from Andy McFadden on the Apple II version, particularly in his analysis of the ship-drawing code
- [Atomic Elite](https://stardot.org.uk/forums/viewtopic.php?p=55890)- Elite on the Acorn Atom, from Atomic legend Kees
- [Second Processor Elite for the Electron](https://stardot.org.uk/forums/viewtopic.php?p=295000)- 6502 Second Processor Elite on the Acorn Electron from Stardot user jms2
- [Wrathchild's Atari 8-bit disc Elite](https://forums.atariage.com/topic/149925-just-for-fun/page/3/#comment-5753669)- An epic and full-featured conversion of BBC Micro disc Elite to the Atari 8-bit platform by Mark Keates (also discussed- [here](https://forums.atariage.com/topic/293865-why-no-atari-8-bit-elite-homebrew/))
- [reifsnyderb's Atari 8-bit disc Elite demo](https://forums.atariage.com/topic/149925-just-for-fun/page/3/#comment-5753669)- Currently in demo form, this conversion of BBC Micro disc Elite to the Atari is actively in development and looking pretty great
- [Rensoupp's Atari 8-bit cassette Elite beta](https://www.atarimania.com/game-atari-400-800-xl-xe-elite_44548.html)- An early beta of the BBC Micro cassette version, converted to the Atari 8-bit range
- [Elite-B](https://bb.oolite.space/viewtopic.php?t=16899)- An enhanced version of BBC Micro Elite in the vein of Elite-A

---
*Fonte originale: [https://elite.bbcelite.com/about_site/useful_links.html](https://elite.bbcelite.com/about_site/useful_links.html)*

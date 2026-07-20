---
title: ''
source_url: https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-8-if-the-sid-doesnt-fit-use-a-bigger-hammer
category: tutorial
topics:
- sprite programming
- basic
- assembly
- graphics
difficulty: advanced
language: mixed
hardware:
- CIA
- SID
- VIC-II
- KERNAL
related:
- sound-programming
- music-player
- raster-interrupts
- vic-ii-registers
- sprite-programming
- sid-registers
- keyboard-handling
- kernal-routines
- joystick-reading
- cia-registers
- memory-map
scraped_at: '2026-07-20'
---

# 

# Episode 3-8: If the SID doesn't fit, use a bigger Hammer

**Synopsis:** Sometimes you want to use a SID file which is set up for a special memory address which is not aligned with you own memory strategy. I introduce a great tool to fix this. 

**Download via  dust:** $ dust tutorials (select 'spritro') 

**Github Repository:**

[Spritro Source Code on Github](https://github.com/actraiser/dust-tutorial-c64-spritro)

- [Episode 3-1: Spritro - An Intro with a Sprite](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-1-spritro-an-intro-with-a-sprite)
- [Episode 3-2: Creating the Shapes - Hello SpritePad](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-2-creating-the-shapes-hello-spritepad)
- [Episode 3-3: Loading Shapes and grasping Symbols](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-3-loading-shapes-and-grasping-symbols)
- [Episode 3-4: Flying the Space Ship off Course](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-4-flying-the-space-ship-off-course)
- [Episode 3-5: Taking Command of the Ship Controls](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-5-taking-command-of-the-ship-controls)
- [Episode 3-6: Custom Character Sets - Hello CharPad](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-6-custom-character-sets-hello-charpad)
- [Episode 3-7: Creating Pseudo Timers for Color Cycle](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-7-creating-pseudo-timers-for-color-cycle)
- **Episode 3-8: If the SID doesn't fit, use a bigger Hammer**
- [Episode 3-9: Greetings, Acknowledgments and Links](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-9-greetings-acknowledgments-and-links)

### The nature of playing back a SID file

A SID file is more than just some music data. A SID comes with everything you need to play back the music too. So there is Replay Routine, the actual Music Information and some SID header. No matter which Replay Routine is used, whether it be custom or something standardized due some popular Music Editor the procedure to play a SID file is always the same after loaded into memory:

- Initialize the Playback routine once by jumping to the SIDs init address
- Trigger the Play Routine Address with every screen refresh

When there are subtunes you also may want to actually select beforehand which tune to play back. The common convention is to set the X-Register to the desired subtune number before initializing the SID.

It also turned out to be pretty standard to store the SID file starting at memory location $1000 and program the replay routines accordingly. The main reason is that $1000 - $1fff are overshadowed with the Character Generator ROM so this place is not really usable to the VIC-II which can not access for example graphics you store in the RAM under ROM in that area. It is important to understand that the SID actually defines itself where it wants to be located. If you put a SID file that is intended to be put at $1000 into a different memory location it just might now work anymore.

There are SIDs which require other locations than $1000 though and when you want to use those in your "standard" intro you may run into problems. The good news is that this can usually be very easily fixed with a tool released in 2013 actually - SidReloc.  SidReloc is actually installed when you use DUST. If you use your own environment you have to download the [SidReloc](http://www.linusakesson.net/software/sidreloc/) source code and compile it yourself.

Let's look for a SID tune which is not using the standard location to demonstrate SidReloc magic.

### Selecting a guinea pig

Empty (512 Bytes) by 4-Mat is a brillant SID - short yet powerful. I can listen to it like forever. It also sets a good mood for the Spritro. To find out it's init and play address on Mac we can open it in [SidPlay](http://www.sidmusic.org/sidplay/mac/) and check the Info Window. Let's look at the original SID file!

Load Address is $0801 which is actually the start of BASIC in the C64 memory, than Init Address is $09ed and last but not least, the Play Routine resides at $0804.

This does not go along well with our requirements to have it start somewhere at $1000. 


Let's open the terminal and run SidReloc against that SID file. By default it will try to relocate the SID to $1000 but you can also specify any other location as long as it is the beginning of a page in memory. For clarification, a page is an expression for 256 Bytes of Memory. The Commodore C64 therefor has 256 Pages as 256 Bytes times 256 equals 65536 Bytes. Even easier is to remember that the ZeroPage ranges from $0000 to $00FF, Page 1 from $0100 to $01FF and so forth. Since we want to use the area starting at address $1000, we don't need to specify anything but for the sake of completeness I put down the full command in the terminal screenshot below:

**sidreloc --page 10 empty_512.bytes.sid empty_1000.sid**

Looks good so far! SidReloc analyzed the SID and created a new output file empty_1000.sid. Let's load that new file in Sidplay and check again the Info Window. 

Et Voila - the SID file has been relocated!

The Load Address is not exactly at $1000 since it must consider the relative Load, Init and Play Address of the original file but it's good enough to utilize the otherwise useless area around our desired memory location. 



We finally load the SID file in **config_resources.asm** and setup the two symbols **init_sid** and **play_sid** in in **config_symbols.asm** so we don't have to remember the addresses.  In our Interrupt Setup routine in **main.asm** we initialize the SID with** jsr init_sid** and from there we just call **jsr ****play_sid** within our custom interrupt 50 times a second. Everything works just fine! 

SidReloc is a really a nice little utility.

-act

---
*Fonte originale: [https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-8-if-the-sid-doesnt-fit-use-a-bigger-hammer](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-8-if-the-sid-doesnt-fit-use-a-bigger-hammer)*

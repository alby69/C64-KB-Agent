---
title: ''
source_url: https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-6-custom-character-sets-hello-charpad
category: tutorial
topics:
- assembly
- sprite programming
- graphics
difficulty: beginner
language: assembly
hardware:
- CIA
- SID
- KERNAL
- VIC-II
related:
- kernal-routines
- keyboard-handling
- sprite-programming
- sound-programming
- joystick-reading
- raster-interrupts
- sid-registers
- cia-registers
- music-player
- memory-map
- vic-ii-registers
scraped_at: '2026-07-14'
---


# 

# Episode 3-6: Custom Character Sets - Hello CharPad

**Synopsis:** Using the Standard C64 Character Set is not really cool, so we will acquire a modfied set taken a C64 game and edit it in another Windows tool which can also run on Mac. 

**Download via  dust:** $ dust tutorials (select 'spritro') 

**Github Repository:**

[Spritro Source Code on Github](https://github.com/actraiser/dust-tutorial-c64-spritro)

- [Episode 3-1: Spritro - An Intro with a Sprite](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-1-spritro-an-intro-with-a-sprite)
- [Episode 3-2: Creating the Shapes - Hello SpritePad](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-2-creating-the-shapes-hello-spritepad)
- [Episode 3-3: Loading Shapes and grasping Symbols](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-3-loading-shapes-and-grasping-symbols)
- [Episode 3-4: Flying the Space Ship off Course](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-4-flying-the-space-ship-off-course)
- [Episode 3-5: Taking Command of the Ship Controls](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-5-taking-command-of-the-ship-controls)
- **Episode 3-6: Custom Character Sets - Hello CharPad**
- [Episode 3-7: Creating Pseudo Timers for Color Cycle](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-7-creating-pseudo-timers-for-color-cycle)
- [Episode 3-8: If the SID doesn't fit, use a bigger Hammer](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-8-if-the-sid-doesnt-fit-use-a-bigger-hammer)
- [Episode 3-9: Greetings, Acknowledgments and Links](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-9-greetings-acknowledgments-and-links)

### Characters the nice way

We used the Standard Commodore Character Set to display some text in our first tutorial but this is kinda lame and you rather want to use custom characters for your on-screen text and scrollers.

Again Mac Users are stuck as there are no good tools to work with Characters for the C64 on this platform. Again we are lucky that the Windows Program CharPad will just run fine using Wine. For this chapter we use [CharPad 1.8.3](http://csdb.dk/release/?id=101863) which was the latest version at the time of writing.  If you have not installed WineBottler yet, you should do it now to run the program.

### A brief look on CharPad

CharPad was coded by the same author who did SpritePad so the overall look and feel is similar yet CharPad is the much more complex program as Characters are not only used to build some Letters but in fact for entire tiled-based background graphics. For this intro we will just modify an existing 1x1 Character Set and will look into the many other options within CharPad at another appropriate time. You can check the example directory which has some great Character Sets including lots of tiled-based graphics.

Start up CharPad and load the rambo_font.ctm which came with the source code of Spritro. Since I already prepared that Character Set there is not really anything to do for the actual Spritro, however, feel free to change letters to your liking and work a bit with the program. At a later point you want to create your own characters.

### Loading Characters and setting Pointers

The Commodore Character Set has a Standard Size of 2 Kbyte which can hold 256 different items. We don't need that many items as we only work with the letters A-Z and some punctuation letters as well as a Heart Symbol which I put at the position of the "]"-letter. It is of course important that the order of the letters match the standard order of the C64 Character Sets so that the screen codes resulting from our text in the sources is adequately converted to the C64 screen.

In **data_text.asm **you will find the three lines of text that are displayed on the screen. Notice how I use the "]" character which will be later shown as a heart character. 

Before we load our Character Set into the project we we need to identify some acceptable space in memory and as with the Sprite Data make sure that the VIC-II can actually see the data its selected Bank. In Standard Bank 3 of the VIC-II there are not too many options and we decide to load our small set starting at $3800.

This is done in **config_resources.asm **and again we need to consider that CharPad exports files with a header with lots of information. Since we only use the raw data without the need to consider anything special we skip all the header information spanning over 24 Bytes and just load the 384 Bytes of the following Character Data into memory. That translates to 48 single Characters each having a size of 8 Bytes or 8x8 Pixels. Lots of them are empty though because I did not bother to clean the Charset up thoughtfully.   

Once the Character Set is loaded into memory we need to tell the VIC-II where it needs to fetch the data from because it is still pointing to the standard Character Generator ROM and we need to bend that pointer in question to our location at $3800.  We do this in the routine we execute only once to write all characters to the screen located in the file **sub_write_text.asm**.

The register we need to store our Character Location at is $d018. As the Standard Character Set is 2Kb large, we have in theory 8 possible location in a 16Kb Bank. So similar as with the Sprite Pointers we need to make sure that the Character Set is put into a location that can be divided by 2048. Unfortunately the options in Bank 3 are limited as a few areas are overshadowed with ROM and the VIC-II can not read RAM information underneath. Location $3800 works for us though.

Now to store 8 different values of possible Character Set locations we actually only need 3 Bits that can represent the values 0-7.  This job is done by **Bit#1 to Bit#3 of $d018**. Setting the Bits to $00 will configure the Character Pointer to $0000, using #$02 will point to $0800  and ongoing until the last possible spot which requires the value #$0e to finally point to $3800. This is the last spot because $3800 + $800 (=2048 Bytes) marks the end of the 16Kb of Bank 3 and the VIC-II expects 2Kb of Data for a Character Set.. 

**Here is the code to set the character pointer and draw text to the screen:**


The output to the screen is the same as in the first tutorial, it's a simple loop over each of the characters in the **data_text.asm**. We don't set color information at this point as the color cycling effect is being taken care of in **sub_color_cycle.asm**.

-act

---
*Fonte originale: [https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-6-custom-character-sets-hello-charpad](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-6-custom-character-sets-hello-charpad)*


### Collegamenti e Riferimenti Hardware
- **$D018 (Memory Setup Register)**: Associato al chip VIC-II. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#d018).

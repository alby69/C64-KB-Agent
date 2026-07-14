---
title: ''
source_url: https://dustlayer.com/c64-coding-tutorials/2013/4/8/episode-2-2-writing-to-the-c64-screen
category: tutorial
topics:
- assembly
- basic
difficulty: beginner
language: mixed
hardware:
- SID
- KERNAL
- CPU
- VIC-II
- CIA
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

# Episode 2-2: Writing to the C64 Screen

**Topics:** Now that we saw the working intro, we want to understand how it works. Let's start with the text written to the C64 screen.  

**Download via  dust:** $ dust tutorials (select 'first intro') 

**Github Repository:**

[First Intro on Github](https://github.com/actraiser/dust-tutorial-c64-first-intro)

- [Episode 2-1: Let's compile and run C64 code](http://dustlayer.com/c64-coding-tutorials/2013/2/17/a-simple-c64-intro)
- **Episode 2-2: Writing to the C64 Screen**
- [Episode 2-3: Did I interrupt you?](http://dustlayer.com/c64-coding-tutorials/2013/4/8/episode-2-3-did-i-interrupt-you)
- [Episode 2-4: Effects using a table of data](http://dustlayer.com/c64-coding-tutorials/2013/4/8/episode-2-4-reading-from-a-data-table)
- [Episode 2-5: Understanding and including music](http://dustlayer.com/c64-coding-tutorials/2013/4/8/episode-2-5-understanding-and-including-music)

### The Memory Map

Before we write to the C64 screen we need to cover some basics about how memory is organized in the C64. If you are not fluent in this topic just take a look at the  [RAM under ROM](https://dustlayer.com/c64-architecture/2013/4/13/ram-under-rom) article in the knowledge base. 

### Let's put text on the screen

So everything in the C64 is addressable using memory locations. The 40 columns x 25 rows of screen you see when turning on the C64 is simply a 1000 Bytes (40x25) large area of the memory called Screen RAM located at address 1024-2023 ($0400-$07F7). Whatever you write into any of those 1000 locations, it will show up in some way on the screen. To put something there which makes sense you have to look up Screen Codes which are associated which each of the C64 characters available when you turn on the computer. Luckily you don't have to bother with Screen Code tables as ACME already provides features to make this easy - I will explain below.

Anyways, for example the Screen Code 1 put into location 1024 ($0400) will print the letter "A" on the top left corner of the screen.

n addition to Screen RAM, there is Color RAM from 55296-56295 ($D800-$DBE7). It also spans over 1000 Bytes and maps the Screen RAM locations 1:1. The lower 4 Bits of the Color RAM are used to set foreground color for the appropriate Screen RAM location. You only need the 4 Bits - also called a Nibble which means "one half of a byte" - as there are only 16 colors available on the C64, so 4 Bits are sufficient to store any of the 16 combinations. If you put a zero into memory location 55296, the previously printed A turns black.

**Type in the BASIC POKE commands on your emulator or real hardware to verify:**

*POKE 1024,1**POKE 55296,0*

So how does this work with machine language? Let's look at the intro code.

### Black out

Our Intro can not start with the standard blue background and C64 welcome text, let's put out the lights. There in fact is a single system routine we could execute but we want to do it the hard but faster way. 

**Open code/init_clear_screen.asm**

The first thing we want to do is to set the border and background color to black. There are two memory locations we just need to set to $00 to achieve this $d020 and $d021.

Then we learned that the actual screen is just an area in memory spanning over 1000 bytes. If we put a space bar in each of those locations and turn the foreground color to black we should achieve a completely black screen without any text. And that is what we will do!

We load the Accumulator with the screen code for the <blank> character which is $20 (decimal 32). Since 1000 locations need to be filled but only 256 iterations can be done with a single byte counter we just start at four positions on the screen at once with the filling. With this method we will be able to turn the entire screen black with just 256 iterations. That's why all we need to do is to check if our X-Index-Register has turned to Zero with the *bne* branch command. Unless this is the case we increment X and hop back to the *clear* label.  

Of course we also need to set the color to black in Color Ram for each of the locations. We do this along the way by loading the Accumulator with $00 and store it in the appropriate memory location starting at $d800.

By the way - with this information you should now be able to do the "inc $d020" effect I ranted about in Episode 2-1. All you need is an infinite loop and increment the memory location of the border color.

### Writing Text to the middle of the screen

**Open the file code/data_static_text.asm**

Now meet one of many conveniences using a cross-development environment. As we use the assembler syntax of the ACME cross assembler we have some very helpful pseudo opcodes which ACME will process for us during compilation. All ACME pseudo opcodes are prefixed with an exclamation mark.

What "!scr" does is to translate the following string to individual C64 screen codes and puts each in the next processed memory location. Which location that might be is not of a big concern to us for this first simple example.  By prefixing each of the rows with a label (*line1, line2*) we can easily reference the memory location later, e.g. when we need to loop over this data to actually display the text. Again, we do not need to know where in memory the text is stored which is very convenient. 

So here comes the next challenge. Now that we have some text defined, how do we print it to the screen using 6502 machine language?

**Open code/init_static_text.asm**

What we want to do is to put the two strings stored in data_static_text.asm into the middle of the C64 screen. We know that the screen ram starts in memory at $0400 so we estimate the middle of the screen near $0590 for the first line of text and $05E0 for the second line.

We now need to loop over the previously defined string data byte by byte and copy what we read into the memory locations of the Screen Ram. As pointed out above, we do not need to know where the text is located in memory but just use the label specified before.

e add another label for the code to loop over the text (init_text), then we initialize our X-Index-Register with zero and start with loading the first byte stored at label line1 into the accumulator. The content of the accumulator is then stored at the location near the middle of the screen plus the content of the X-Index-Register which is 0 at the beginning.

The content of *line1,x *s the first byte in the first string, actually the Screen Code for a space character. We store the code from the accumulator to the appropriate position in Screen RAM at $0590 plus the value of the X-Index-Register which is still zero. 

We repeat the process with line2 but this time we start storing the screen code at $05E0 which is two lines below the previous Screen RAM we wrote to earlier.


The first byte of each line of text has been written to Screen RAM - excellent! Now we want to do the same with the second character of the string. For that all we need to do is to increment the X-Index-Register and continue looping.

*inx *oes exactly that - it increments the content of the X-Index-Register. The next thing before we continue the loop is to check whether we already finished iterating over the complete line. As one row of the C64 screen can not hold more than 40 characters we simply compare the X-Index-Register using the *cmp* command to the number 40 which is $28 in hex. the branch command *bne* will jump back to our label *loop_text* if the comparison is not true. With this we can work through 40 bytes of data for each line. Once the comparison to $28 is true the next command after *bne executed. * This is an *rts *hich means *return from subroutine*.

**And that's it! **on't worry that we skipped some details yet but you should have been able to get what we did to write some text to the C64 screen. We will soon do another iteration example when it comes to the color washer effect but before that, we talk about interrupts.

-act

---
*Fonte originale: [https://dustlayer.com/c64-coding-tutorials/2013/4/8/episode-2-2-writing-to-the-c64-screen](https://dustlayer.com/c64-coding-tutorials/2013/4/8/episode-2-2-writing-to-the-c64-screen)*


### Collegamenti e Riferimenti Hardware
- **$D020 (Border Color)**: Associato al chip VIC-II. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#d020).
- **$D021 (Background Color)**: Associato al chip VIC-II. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#d021).

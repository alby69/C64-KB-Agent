---
title: ''
source_url: https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-3-loading-shapes-and-grasping-symbols
category: tutorial
topics:
- assembly
- basic
- sprite programming
- graphics
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

# Episode 3-3: Loading Shapes and grasping Symbols

**Synopsis:** We will finally load our Sprite into memory and discuss the usage of Symbols along the way.

**Download via  dust:** $ dust tutorials (select 'spritro') 

**Github Repository:**

[Spritro Source Code on Github](https://github.com/actraiser/dust-tutorial-c64-spritro)

- [Episode 3-1: Spritro - An Intro with a Sprite](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-1-spritro-an-intro-with-a-sprite)
- [Episode 3-2: Creating the Shapes - Hello SpritePad](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-2-creating-the-shapes-hello-spritepad)
- **Episode 3-3: Loading Shapes and grasping Symbols**
- [Episode 3-4: Flying the Space Ship off Course](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-4-flying-the-space-ship-off-course)
- [Episode 3-5: Taking Command of the Ship Controls](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-5-taking-command-of-the-ship-controls)
- [Episode 3-6: Custom Character Sets - Hello CharPad](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-6-custom-character-sets-hello-charpad)
- [Episode 3-7: Creating Pseudo Timers for Color Cycle](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-7-creating-pseudo-timers-for-color-cycle)
- [Episode 3-8: If the SID doesn't fit, use a bigger Hammer](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-8-if-the-sid-doesnt-fit-use-a-bigger-hammer)
- [Episode 3-9: Greetings, Acknowledgments and Links](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-9-greetings-acknowledgments-and-links)

### There is the Sprite - now what?

We have stored our 16 Sprite Shapes that make up the Space Ship Animation into a file in SpritePad-format. We have to load it into C64 memory then we want to setup the appropriate VIC-II registers to actually display the Sprite and last but not least we want to run the animation and move the space ship over the screen - smoothly. As a bonus, we want to open the top and bottom borders by exploiting a VIC-II bug and let the Space Ship fly freely in that area.

The source codes in the Spritro project are split up so responsibilities in each file are more or less clear by looking at the file name. Working with the Sprite spans over four different files, each having a very specific set of tasks.

- **config_resources.asm**loads the spritesheet file exported from SpritePad into memory
- **config_sprites.asm**does all sort of setups to display the Sprite on the screen
- **main.asm**sets up our custom interrupt which calls the the subroutine to move and animate the ship. It also uses a trick to open the top and bottom borders.
- **update_ship.asm**includes the subroutines that take care of the animation and movement of the space ship

Looks like a lot at first glance but actually we are talking about less than 100 lines of code all together for everything Sprite related. 

### Choosing appropriate Space in Memory

Our Sprite has 16 individual frames or Shapes, each 64 Bytes long as they consist of 12 double-wide horizontal pixels * 21 vertical pixels plus an extra byte to pad them to the convenient number 64. This last Byte is used by SpritePad to store whether the Sprite Shape is in MultiColor or Standard Mode plus it holds the individual Sprite Color. Each of the 8 Hardware Sprites can have one of 16 individual colors that it does not share with other Sprites as opposed to the Background Color, MultiColor 1 and MultiColor 2 in the appropriate Mode.

The 16*64 Bytes or 1 Kbyte of Sprite Data needs to be stored in an area the VIC-II is able to see. As we don't change the Bank the VIC-II looks at on C64 boot time the range we can theoretically use are the 16 Kbytes from $0000 to $3FFF. Before we decide on the location there is one more thing to take into account. The address where the Sprite is stored must be dividable by 64. That is important for the Sprite Pointers I will elaborate about in a bit. I will use $2000 for no special reason. I don't have anything lying around $2000 so this location seems fine. All of our shapes take up 1 Kbyte all together so we are going to occupy the C64 memory from $2000 to $23FF.

### Loading Data in Order

Sometimes it can be tricky to get the order right when loading multiple files into C64 memory. The Index file which is also the file you later compile with your favorite cross assembler or using DUST is already structured in a way that should always work fine.

That **index.asm **has three responsibilities it takes care in a specific order: 

- load external resources (graphics, music, charsets) by including **config_resources.asm**at the top.
- set up BASIC loader so we do not have to write SYS 41952 to run the Intro after loading the compiled .prg on the C64
- include all remaining source files with the actual 6502 code starting at a dedicated memory address 

We define the memory starting locations for external binary files using some meaningful symbols within the **config_resources.asm **file and then load each resource by defining the starting zone with *** = <our_defined_symbol> **along with the ACME pseudo operator **!bin **to actually read the data from disk into the specified location. 

Regarding the Spritesheet we know that the first three bytes of SpritePad 1.8.1-formated files contain a header with color Information for all shared colors but we actually do not really need that information as we can remember the three colors and just skip an extra step of parsing them from the actual file. The !bin command is modified to load 1024 bytes but skipping the first three bytes of the file before loading the data starting at memory address $2000. Similar procedure applies to the SID and Character Set import which will be discussed later. Then inclusion flow is returned to the next statements in **index.asm **where the BASIC Loader is set up starting at $0801 before all the actual 6502 code is written into memory starting from $c000. 

### A brief Detour about Symbols and Labels

When I started getting into 6502 coding the thing which was a source of regular confusion at start was the whole issue with using addressing modes in conjunction with symbols. When I define a symbol, Is it a value, a vector or is it a memory address I refer to? During my first steps into 6502 coding It seemed to be totally random when later used with keywords like LDA or STA. But then my eyes opened one day - **it is what you would like it to be!  Just understand the 6502 addressing modes!**

If you are unfamiliar and confused, just read the [knowledge base article on 6510 Addressing Modes](https://dustlayer.com/cpu-6510-articles/2013/5/24/whatever-you-like-coming-to-addressing-modes) to get clarity.

Let's quickly talk about Symbols as such. **Symbols** are not really the same as variables you know from other programming languages. **Labels** are not variables either but mark a starting point within the program code. During assembling those labels and all instructions pointing to the label will point to the corresponding memory address instead - or rather the offset when using branch commands. It is good to know what actually happens during assembling. 

An assembler passes over a source file and needs to collect the symbols and also labels for resolving future references and doing the actual assembly. The difficult part is to resolve future label references and assemble all code in only one assembler pass. That's why most assemblers are doing* two passes*. In the first pass the assembler looks for all label and symbol definitions and puts them in an internal table. In the second pass, after the table is set up, it does the actual assembly by translating the operations and replaces labels with the calculated memory locations and also replace all values originating from using Symbols.

For example, in our custom interrupt routine in **main.asm** we jump to the subroutine **color_cycle** which is actually label in the file **sub_color_cycle.asm** . After the first pass the assembler knows the actual memory location of where the subroutine starts. In the second pass it replaces the **jsr color_cycle **instruction with **jsr $c17e** . If we look into memory after starting the intro we can see that $c17e is in fact the place where our color_cycle subroutine starts.

### Enlightening the VIC-II

We know that our sprites are loaded at $2000 but the VIC-II does not yet. The VIC-II actually knows nothing about our intentions to use Sprites in the first place so let's address this in **code/config_sprites.asm. **

The **config_sprites.asm** file is basically split in three parts. We define some memory locations and values using symbols we need for later use. We then start initializing the locations and some VIC-II sprite registers to get the word out to the street that we want to show our space ship. 

First of all I have to pick two memory locations I know are not occupied by something important in the C64 while the intro is running. I will use $fb and $fc.

- $fb will be used to store the currently shown sprite shape within our 16 frames animation.
- $fc will be used as a flipping Byte which we use to change between two colors in the side borders. 

The next symbol is a placeholder for the Integer 16 which represents the overall number of used frames/sprite shapes in our animation.

The **sprinter_pointer_ship **symbol may at first look awkward. We divide what we defined in the symbol **address_sprites** in the **config_resources.asm** by the value $40. That would be $2000 / $40 or 8192 / 64 which translates to $80 respectively 128.  $80 is the value that we need to put into the Sprite Pointer for Sprite#0 which is stored at the end of Screen RAM.  

**What is a Sprite Pointer?** Each of the last 8 Bytes of Screen RAM define the location of our Sprite Shape currently appointed to the respective Hardware Sprite, hence the name Sprite Pointer. As explained in the [VIC-II knowledge base article on Sprites](https://dustlayer.com/vic-ii/2013/4/28/vic-ii-for-beginners-part-5-bringing-sprites-in-shape) one Byte is all we need to address any possible Sprite location in the part of the C64 memory the VIC-II looks at. The reason is that the VIC-II can only see data within a portion of 16 Kbyte of Ram and** 16340 Bytes / 255 possible Byte Values** **translates to 64 Bytes** - the size of a single Shape actually. So in theory a Sprite Shape can be put anywhere in the active VIC-II Bank area by putting the Sprites memory location divided by 64 into the appropriate Sprite Pointer Register. $80 is therefor pointing to our first Sprite Shape out of 16 as $80 (128) * $40 (64) results in $2000, the address we loaded our Spritesheet into. 

**What about animation?** We will get to this topic in a later chapter.

Next we assign a few values to symbols reflecting the shared colors for theoretically all hardware sprites but we just use Sprite#0. The color information is taken from the SpritePad program - it's not so hard to remember three colors after all so we did not parse the header of the* sprites.spr* file for this. Likewise the individual ship color is also stored in a symbol.

Now we have our symbols set up and can use them to initialize our registers and as a side effect have a much better readability in the process by using all those symbols. 

I already pointed out that a symbol just references to a value whose purpose is then determined by the way you use it in your code, in plain terms, it all comes down what addressing mode you use.  The following LDA/STA pairs do simply load some value from a memory location or take an absolute value and store them in a specific register. Again the symbols help us to keep readability but in your mindset you can just replace them for the referenced value and consider any addressing mode syntax in the process.

Let's look at the place where we store the location of the Sprite Shape for Sprite#0 into the Sprite Pointer. As already elaborated  the location to store the value is the very first of 8 Bytes at the end of Screen RAM. I have defined a symbol called *screen_ram* in **config_symbols.asm**  so using **sta screen ram + $3f8** will indeed store the previous calculated value $80 into the first Sprite Pointer Byte since $0400 which is start of Screen RAM plus $03f8 results in $07f8 - the first of the last 8 Bytes. Why use this complex construct and not just **sta $07f8** instead? If you move Screen RAM for any reason, e.g. you may want to use a different VIC-II bank, you would not need to recalculate the locations of the Sprite Pointer Registers. 

At the very end we define the starting X/Y coordinates for Sprite#0. Since we set Bit#0 in $d010 high you can basically consider it to be a set 9th Bit for the X-Coordinate or in other words add 256 to whatever is written to $d000. In our case we put $a0 into $d000 so this translates to Decimal 160 plus the 9th Bit which values to 256 and that results in X-Coordinate 416. That is a location outside the visible area which is of course desired so the ship can fly into the scenery. 

For the Y-Coord we chose a value which is  actually hidden by the bottom border of the Commodore C64 but since we remove this border later, our Sprite will happily fly along that part of the screen and be visible. 

Speaking of flying - at the moment the Sprite does not go anywhere - we don't even see it because it's hidden below the right bottom corner. The next chapter will deal with the Ship Animation and Movement.

-act

---
*Fonte originale: [https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-3-loading-shapes-and-grasping-symbols](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-3-loading-shapes-and-grasping-symbols)*

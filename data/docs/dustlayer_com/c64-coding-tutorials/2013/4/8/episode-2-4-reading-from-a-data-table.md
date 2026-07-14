---
title: ''
source_url: https://dustlayer.com/c64-coding-tutorials/2013/4/8/episode-2-4-reading-from-a-data-table
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
related:
- kernal-routines
- sound-programming
- sid-registers
- music-player
- memory-map
scraped_at: '2026-07-14'
---

# 

# Episode 2-4: Effects using a table of data

**Topics:** We will understand the first demo effect which is cycling a color pattern on some text. To achieve this we must know how to iterate over table data.  

**Download via  dust:** $ dust tutorials (select 'first intro') 

**Github Repository:**

[First Intro on Github](https://github.com/actraiser/dust-tutorial-c64-first-intro)

- [Episode 2-1: Let's compile and run C64 code](http://dustlayer.com/c64-coding-tutorials/2013/2/17/a-simple-c64-intro)
- [Episode 2-2: Writing to the C64 Screen](http://dustlayer.com/c64-coding-tutorials/2013/4/8/episode-2-2-writing-to-the-c64-screen)
- [Episode 2-3: Getting into interrupts](http://dustlayer.com/c64-coding-tutorials/2013/4/8/episode-2-3-getting-into-interrupts)
- **Episode 2-4: Effects using a table of data**
- [Episode 2-5: Understanding and including music](http://dustlayer.com/c64-coding-tutorials/2013/4/8/episode-2-5-understanding-and-including-music)

### The Color Washer effect

We have put some text on the screen and now we want a nice effect to happen. A good starter is an effect which is sometimes referred as color cycle or color wash effect. In our intro it's about changing the foreground text color for each letter in a pattern so it does look like the color *washes* from one end to the other. 

**There are two extra challenges:**

- We need to change the foreground colors of all letters with every screen refresh.
- We want that the color moves from right to left in the upper line of text and r*eturn*from left to right in the second line of text. With this we achieve a little optical illusion of a rotating color cycle across both lines.

We need to define what colors we want to use for the effect and put it in a table we can iterate over. The tricky part is to write down a pattern auf color codes that actually look good in our pseudo motion. You can experiment by changing color information in the data tables. 

**Open code/sub_colorwash.asm**

There is the first mystery -  we want to load some information from somewhere labeled *color+$00 *ut there is no such label in that file. I actually like to organize code in as many chunks as possible and that is why you find the table data with the color information in a different file. So additionally  open** code/data_colorwash.asm. **

Now we have everything we need to understand the code. First of all, why would we use two tables? or simplicity actually - with some more thoughts put into a good routine one table is probably sufficient. But this is something you do on C64 all the time - looking for optimizations. In this example we use two tables so it's easier to follow what is going on.

The two tables in *data_colorwash.asm* are labeled with *color* and *color2*. ACMEs pseudo opcode !byte wrote al the values consecutively into memory. A subroutine can now retrieve the data by referencing to the labels *color* and *color2 *- this is what we do in *sub_colorwash.asm*.   The way the tables are formatted is not of importance, I used an 8x5 matrix because it looked fine for 40 values.  We use 40 values because we are manipulating 40 positions per row.  The values are numbers ranging form 1 to 15 ($00 - $0F) as there are 16 colors available on the Commodore C64 to work with.  

If you would stop the effect while running the intro you get a visualization of the color pattern. You need to experiment a bit with different colors to generate for example some kind of shining effect like this one.

Let's look at the actual sub routine in *sub_colorwash.asm* which manipulates the first line of text. Every time we execute the routine  - which is on every screen refresh - we change the foreground color of all characters in both rows starting at $0590 for the first row and $05E0 for the second row on the screen. In the places where no text is printed we won't see any side effect as there is no character where a foreground color would change anything. So if there is a space character, it will remain black to the viewer's eye though we actually do change the memory location in the process.   

### The principle of the effect

At first glance the code might confuse because we seem to work on the color table itself and not on the characters in Screen Ram - *but* this is in fact what we do.

Take a moment to grasp the principle: The foreground color of each of the two rows of text can be manipulated in Color RAM. There is no need to care about the Screen RAM as the actual character codes will not change. To achieve a color cycle effect we need to change foreground color of all our characters in Color RAM with every screen refresh. And for that we basically rotate the values in the color tables and write the updated color information into Color Ram.

**Still confused? Let's go through the code.**

As you can see, there are two main blocks of code. *colwash* and *cycle1* for manipulating the first row of text where we want the colors to "wash" from right to left and then there is *colwash2* and *cylce2* with the reverse effect for the second line of text. 

There is one not obvious complexity in the code that is due to how I designed the data table for the colors.  The two tables are adjacent, that is there are 40 bytes in the first table named *color* and right after another 40 bytes in the table named color2. The problem with this was pointed out in the blog comments below for an earlier version of this subroutine where I accidentally operated one byte outside the tables. 

You may want to read through the blog comments to get the whole picture but the important thing is that we need a temporary location to store one color value while iterating in the process. You will understand in a bit.

**Let's focus again and continue to step through the code with the just said in mind. **

I will dissect exactly what happens in the first iteration of the loop. We start by initializing the x-register with the number of iterations we need to do. Then, for our first line of text, we load the last color of the first color table, that is the 40th byte - that is position $27/#39 when you count from zero.

Now the actual loop starts. We grab the next color from the end of the color table which is at this point at position #38 and temporarily store it into the y-register. The table location we read that color from is then overwritten with the color that is still stored in our accumulator from the initialization process at start. That would be the color formerly known as color number #40. It is written into Color Ram for the character in column position $27/#39 of the row that starts at Color Ram location $d990. That memory address $d990 maps exactly the color information for our characters in the Screen Ram location starting at $0590.  If you *check init_static_text.asm*, you see that this is exactly the row we use for our first line of text. 

So what we did here in the first iteration is to move the color from the formerly 40th position of the color table to the 39th position **and** **before that **kept a note of the color that was previously stored at position 39 for later use. That information is now restored using the implicit *tya* operator which transfers the content of y to accumulator.  We can now decrement x and check if we already did 39 iterations. If we did, we only need to write our final 40th color to beginning of our  Color Ram of the first line of text at $d990. Thanks to the y-register that final value has been remembered and moved to the accumulator in the last iteration. 

That was a bit of heavy stuff, mainly because of the temporary storage strategy. Maybe it clicks when we do the reverse approach for the second line of text. This time we wash our colors from left to right to achieve those sort of rotor-effect in the intro. This requires some minor changes but the principle remains exactly the same.

We don't start at the end but in the beginning of the table, so x-register is initialized with #$00. Accumulator is again initialized wit the last color,  this time from the *color2* table..  Again we grab the next color and store it temporary in y plus write it into the color2 table overwriting the memory address we just remembered the previous value of. This in turn is again transferred to the accumulator and written into Color Ram, this time two rows lower as our second line of text is located in Screen ram row starting at position $05e0 which has it's Color Ram position starting at $d9e0.  In our 39th iteration (starting at 0 that would be $26/#38), we put our final color into the last position in Color Ram. Again this is only possible because we remembered it in the y-register before and moved it to the accumulator in the last iteration step. 

**We now did the whole round trip for both lines of text!**

As a beginner you will need to read the code over and over again probably because it's a bit hard to grasp at first but it will eventually make sense after some time looking at the code and the output.

### perfect color cycle example

Using color cycling is a very interesting technique. You can do very simple effects like the one in our intro but also create astonishing visualizations. For some inspiration, please check this awesome color cycle effect implemented by Joseph Huckaby.  There are more incredible screens available on [this page](http://www.effectgames.com/demos/canvascycle/) at Effect Games.

In the last episode of this tutorial I briefly talk about including external resources, namely music. 

-act

---
*Fonte originale: [https://dustlayer.com/c64-coding-tutorials/2013/4/8/episode-2-4-reading-from-a-data-table](https://dustlayer.com/c64-coding-tutorials/2013/4/8/episode-2-4-reading-from-a-data-table)*

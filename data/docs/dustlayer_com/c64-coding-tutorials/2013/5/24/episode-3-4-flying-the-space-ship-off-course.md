---
title: ''
source_url: https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-4-flying-the-space-ship-off-course
category: tutorial
topics:
- sprite programming
- assembly
- raster interrupts
difficulty: beginner
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

# Episode 3-4: Flying the Space Ship off Course

**Synopsis:** Moving an animated Sprite is cool, but moving it across borders of the C64 results in +1 in Street Credibility.  

**Download via  dust:** $ dust tutorials (select 'spritro') 

**Github Repository:**

[Spritro Source Code on Github](https://github.com/actraiser/dust-tutorial-c64-spritro)

- [Episode 3-1: Spritro - An Intro with a Sprite](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-1-spritro-an-intro-with-a-sprite)
- [Episode 3-2: Creating the Shapes - Hello SpritePad](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-2-creating-the-shapes-hello-spritepad)
- [Episode 3-3: Loading Shapes and grasping Symbols](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-3-loading-shapes-and-grasping-symbols)
- **Episode 3-4: Flying the Space Ship off Course**
- [Episode 3-5: Taking Command of the Ship Controls](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-5-taking-command-of-the-ship-controls)
- [Episode 3-6: Custom Character Sets - Hello CharPad](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-6-custom-character-sets-hello-charpad)
- [Episode 3-7: Creating Pseudo Timers for Color Cycle](https://dustlayer.com/c64-coding-tutorials/2013/5/24/epsiode-3-7-creating-pseudo-timers-for-color-cycle)
- [Episode 3-8: If the SID doesn't fit, use a bigger Hammer](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-8-if-the-sid-doesnt-fit-use-a-bigger-hammer)
- [Episode 3-9: Greetings, Acknowledgments and Links](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-9-greetings-acknowledgments-and-links)

### Setting Sail to unknown Territories

It's about time to to move the Sprite and update it's animations so we have a nice rotating Space Ship flying from right to left. This challenge will actually turn out to be easily achievable. All we need to do is to update the X-Coordinate with every screen refresh and accordingly set our Sprite Pointer to the next shape in the timeline of consecutive Sprite Shapes.

But first we want to check** main.asm** because this is where we call our subroutines for the move and animate action plus we open the top and bottom borders!

I have removed some of the Custom Interrupt Setup Code as it is identical with the one from the ["First Intro" Tutorial](http://dustlayer.com/c64-coding-tutorials/2013/4/8/episode-2-3-did-i-interrupt-you). 

Not surprisingly our main routine has only two responsibilities

- run any subroutine which needs to be executed once at the beginning of the intro
- install a custom interrupt and run any routines which needs to be executed repeatedly on each screen refresh

What is different compared to the last tutorial is that the custom interrupt also executes some code after it processed our subroutines. That extra code exploits a VIC-II bug that opens the top and bottom border of the Commodore C64. I will explain this easy but very cool exploit before we continue with the actual trivial Sprite animations and movement. 

### How to trick the VIC-II in not drawing the border

Before we go through the code let's examine what the VIC-II actually does during a screen refresh in respect to borders. We look only at the top and bottom border at this point though the side boarders can be opened in a similar fashion but that requires some additional considerations which are out of the scope for this episode. 

The C64 can switch between two different screen heights and screen widths. You can select the standard height of 25 visible rows or shrink to 24 rows. Horizontally you are allowed to choose between the default 40 visible columns versus a smaller area with only 38 columns.

To shrink the rows horizontally one needs to set Bit#3 in the control register $d011 low. By default this Bit is set high so 25 rows are visible which together with the 40 default columns corresponds to the standard 1000 screen locations in a 25 x 40 grid each cell being 8x8 Bits in size.

**Why are there modes which shrink the screen in the first place you may ask?** 

You know that 8x8 Bit Characters can be put on any of the 1000 locations via Screen RAM. This also applies when we use either of the alternative modes for screen height and width. This makes it possible to draw something below not visible area - imagine for example the beginning of a text which soft scrolls from right to left. Without hiding the first scrolling character of your text behind some invisible area the character would just suddenly appear on the screen - which does not look great. By limiting horizontal width by one column to the left and to the right you can not only smoothly scroll in a text from below the extended border into the users focus, you can also equally get them off screen on the opposite side of the screen.

Vertically for whatever reason only one row which in fact is split can be added to the screen so effectively you have four lines extending the top and and 4 lines extending the bottom border area. I did not find a satisfying answer why you can shrink by two full columns horizontally but only by one row vertically yet . Different theories came up in #c-64, e.g. that the designers might have though that limiting the already small height of 24 rows even further would not be acceptable while shrinking 40 to 38 columns is barely notable. Or that they simply wanted to avoid more costs by saving a few transistors in the chip design It seems to still be mystery after 30 years.

Whether you scroll something from right to left or from bottom to top it does not really matter. Even four pixels vertically on each side of the screen is fine to gently let something appear into the screen.

Anyways, we can exploit this mode switching feature to actually make the borders disappear completely. It will come with some constraints like that you can still not put characters in the area where the borders were originally located - you are still restricted to the 1000 Bytes in Screen RAM after all - but Sprites for instance can be freely in that then visible area. 

**So how does the trick work? **

The VIC-II internally holds an ON and OFF state for both, the top/bottom and the side borders. When it starts drawing the top border for instance the state for top/bottom is set to ON. After it finished drawing - which happens at Raster Line 50 in default 25 rows mode - it will switch the state to OFF to continue with rendering the visible area of the the screen. After the VIC-II has finished drawing the last possible character to that visible area - that is the 1000th location in the 25x40 grid - it will turn the Border State to ON again to draw the bottom border. That happens at Raster Line 250.

In 24 Row Mode the state switching Border Drawing ON and OFF happens in Raster Line 54 and in Raster Line 246 accordingly.  Understood the procedure? **Good, because here comes the actual exploit!** 

Let's assume we are in 25 rows mode. We start drawing the first Lines of the Top border, that is the Border State is set to ON. The VIC-II turns OFF border at Raster Line 50 as expected. We know that the next time the VIC-II will turn border state ON is at line 250. What we do is to let the VIC-II draw the screen until it reaches Raster Line 249 that is the 25th Row, hence the last visible row on the screen. We wait until it finished drawing that last line in this final row **AND THEN **we clear the Bit#3 of $d011 to instantly switch to 24 rows mode. **There we fooled the VIC-II! **

What, you ask? What did we do? We switched to 24 Rows Mode **while we already passed the 24th Row**, in fact we are at Row 25. But in 24 Row Mode the VIC-II is supposed to turns Border State ON in Raster Line 246 - a line we already passed. And since  we already passed this Raster Line, the VIC-II does not turn ON the border state - it will remain OFF, no Border is drawn.  

To make this exploit work properly we have to set Bit#3 of $d011 high again before the next screen refresh. We do this on the last line of the screen.

The exploit comes with a constraint. Since there is no Screen RAM available behind the borders - remember we still work in a 25x40 grid for Characters no matter what - you are not able to write text using standard character into the new visible areas. Sprites are fine though as they can move freely across the screen so coders for example started to build Character Sets from Sprite Data and used that in the opened border areas.

We also confused the VIC-II a bit along the way. Since it does not draw any border it just draws SOMETHING into the new uncharted territory. It simply uses whatever is written in the last Byte of the selected Bank. For the default Bank 3 that would be the content of $3fff. We want to to clear that Byte to not have any potential garbage on our screen.

The actual exploit is really short and straight forward, let's quickly check the portion of code that achieves this result. It is part of our custom interrupt routine which is executed with every screen refresh. 

As just pointed out we clear $3fff to not see any garbage in the border area.  Then we wait until Raster Line 249 is reached. This is done by just checking $d012 and loop with **bne *-3** which means to branch back three bytes as long as we have not reached the Raster Line in question.  Then we set Bit#3 in $d011 to low to achieve 24 Rows Mode and wait until we reached the end of the screen to set Bit#3 of $d011 high again - that is, switch back to 25 rows mode. This last step is required to make the trick work - in fact the border will not show up anymore. 

### Moving and Animating the Space Ship

Now that we have opened the borders we want to move the ship from right to left in all its glory. For that we want to execute the **update_ship** subroutine 50 times a second. Let's look into the code residing in **sub_****update_ship.asm**. 

Since both Moving the Ship and Cycling through the different Shapes is done in this routine we need to delay the latter within the subroutine because otherwise the playback of the animation is simply too fast.

Coming from our Custom Interrupt Routine in **main.as****m ** we jump to the label **update_ship **in** sub_update_ship.asm**.

We decrease the X-Coordinate register for Sprite#0 at $d000 and check if it it has become #$00 yet. When this happens we need to branch to the label **ship_x_high** and flip the 9th Bit for Sprite#0 accordingly and start over.  This will make sure that our Sprite will not reappear in the middle of the screen when reaching the left side of the screen but in fact is set back to the outer right below the side border. 

The next thing we check is the **delay_animation_pointer **- we did set up this Byte in **config_sprites.asm** before to flip between two states. This is achieved with **eor #$01** which will flip the corresponding Bit#0 between high and low. Whenever the Bit is low we want to delay the animation and just take a short cut and return from the subroutine to wait for the next refresh. 

If Bit#0 in the **delay_animation_pointer** is set high on the other hand, we want to go forward one step in our animation - that is exchange the current Sprite Shape with the next one. We branch to the **dec_ship_frame **label where increase the Sprite Pointer for Sprite#0 by 1. If there was the value #$80 written in the Sprite Pointer register it now becomes #$81, and in fact, this works fine because #$81 determines the next Sprite Shape location which is residing at $2040. So #$81  is pointing to the next block of 64 Bytes after the first Sprite Shape. 

With this pattern we can just go forward step by step in our 16 shapes by manipulating the Sprite Pointer at the end of Screen RAM by counting up the value.

We additionally need to decrease the current frame counter in the process as we need to keep track somewhere whether we have played back all 16 Shapes yet. 

Once this is the case we will reset all pointers back to the beginning. We branch to the label** reset_ship_frames** and simply load the **sprite_ship_current_frame w****ith the total numbers of frames, that is 16. That is how we initialized it in the first place in ****config_sprites.asm**. Then we load the original value for the Sprite#0 pointer into the respective Pointer Register at $07f7 and everything is ready for restart. 

That's it - not much magic here, the most challenging part is to keep track of Bit#9 for the X-Coord. 

-act

---
*Fonte originale: [https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-4-flying-the-space-ship-off-course](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-4-flying-the-space-ship-off-course)*


### Collegamenti e Riferimenti Hardware
- **$D011 (VIC Control Register 1)**: Associato al chip VIC-II. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#d011).
- **$D012 (Raster Counter)**: Associato al chip VIC-II. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#d012).

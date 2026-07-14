---
title: ''
source_url: https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-7-creating-pseudo-timers-for-color-cycle
category: tutorial
topics:
- assembly
- sprite programming
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

# Epsiode 3-7 - Creating Pseudo Timers for Color Cycle

**Synopsis:** For our two color cycle effects we experiment with different ideas where to source timing information from.

**Download via  dust:** $ dust tutorials (select 'spritro') 

**Github Repository:**

[Spritro Source Code on Github](https://github.com/actraiser/dust-tutorial-c64-spritro)

- [Episode 3-1: Spritro - An Intro with a Sprite](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-1-spritro-an-intro-with-a-sprite)
- [Episode 3-2: Creating the Shapes - Hello SpritePad](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-2-creating-the-shapes-hello-spritepad)
- [Episode 3-3: Loading Shapes and grasping Symbols](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-3-loading-shapes-and-grasping-symbols)
- [Episode 3-4: Flying the Space Ship off Course](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-4-flying-the-space-ship-off-course)
- [Episode 3-5: Taking Command of the Ship Controls](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-5-taking-command-of-the-ship-controls)
- [Episode 3-6: Custom Character Sets - Hello CharPad](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-6-custom-character-sets-hello-charpad)
- **Episode 3-7: Creating Pseudo Timers for Color Cycle**
- [Episode 3-8: If the SID doesn't fit, use a bigger Hammer](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-8-if-the-sid-doesnt-fit-use-a-bigger-hammer)
- [Episode 3-9: Greetings, Acknowledgments and Links](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-9-greetings-acknowledgments-and-links)

### A different Color Cycle Effect

In the first tutorial we used a table with values to generate a nice color washing effect. This time we will use a different source to cycle through color information across all our characters. Along the way we will also flip colors in the side borders. 

### Two ways of Timing the uncommon Way

Programming the C64 is really about trying things - sometimes not the standard way, sometimes not even the smart way. The approach I took is probably even stupid but it fulfilled its purpose. Coding the C64 is really not about the greatest algorithm but quite the contrary you sometimes need to be sloppy to save cycles or achieve a certain effect in the given number of CPU cycles.

For the color cycle effect on the letters in Spritro I wanted to cycle 16 colors from right to left, actually 15 because I want to skip a black foreground color. To have a good looking cycle speed the cycle should proceed every second screen refresh at most. Instead of wasting another memory location to keep progress of the colors I thought why not use the ship animation pointer. It has 16 Frames after all and is updated every two screen refreshes already - that seemed to fit nicely with the 16 color values I want to cycle through.

In the same subroutine I also let the side borders flip between to color states - dark blue and light blue. This again should be executed significantly slower. I thought with a bit of trial and error I could sync it to the lead instrument of the SID tune. We know how to flip some state already with a simple EOR instruction on some reserved Byte. But we also need to delay the switching.

Let's check the code in **sub_color_cycle.asm** on how I approached this. This sub routine is executed in the custom interrupt routine 50 times per second on a PAL machine so I need to take delay actions within the sub routine.

We start by initializing the X-Register with #$00. The X-Register's purpose is to check our column position when writing to the screen. Then we load the** sprite_ship_current_frame** symbol which holds the current shape number displayed within the space ship animation. We cmp against #$0f, the last of the 16 color codes of the C64. If the value is indeed #$0f we skip the next instruction which is incrementing that value.  

We store the current value into Color RAM locations for the three rows of text and then subtract 1 from it. So if the value was for example #$06, it became #$05. We compare if the value is #$00 yet because if this is the case we want to skip the next step - we are not interested in using a Black foreground color. If it is not we increase our X register to step forward in our text. Then we check if we reached the end of the row already by comparing X against #$28 (= Column 40). As long as we have not reached the end of the row we will keep branching back to the **color_inc **label. It will colorize the next character with the current value in the Accumulator and so forth. With this, every character in all three lines of texts are changing color every two screen refreshes. 

Now how did we sync the border flipping color with the SID (kinda...). As already mentioned it is simple trial and error. For the switching logic I used a free memory location and attached the symbol **delay_counter** to it. Every time we completed to colorize all three lines of text I load the delay pointer into the accumulator and compare it against #$34. If this comparison turns out true I flip the border color by simply loading the current color from $d021 and EOR'ing it against the value #$08. This wil flip dark blue for light blue and vice-versa every time this is executed. If you put in another EOR value it will flip against another color. After that the **delay_counter** is reseted to #$00. 

If we have not reached #$34 yet in the** delay_counter**, it is simply incremented and we return from the subroutine. This approach will delay the flipping to about ever three seconds which is at least for the first few chords in sync with the music. It is far from perfect though after a few chords the music and color flipping will be out of sync. It's fine for a first impression though.

### ConclusionI

Again this was actually not really smart nor anything near timing perfect. But It just shows that you can do what you want in that machine. If you see an opportunity to create something no matter how strange it might feel - don't hesitate. You don't have always to copy and paste stuff you find on the net. The Commodore C64 gave you an All Access Pass to do whatever you want to do.

-act

---
*Fonte originale: [https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-7-creating-pseudo-timers-for-color-cycle](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-7-creating-pseudo-timers-for-color-cycle)*


### Collegamenti e Riferimenti Hardware
- **$D021 (Background Color)**: Associato al chip VIC-II. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#d021).

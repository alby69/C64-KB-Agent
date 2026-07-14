---
title: ''
source_url: https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-5-taking-command-of-the-ship-controls
category: tutorial
topics:
- assembly
- basic
- input handling
- sprite programming
difficulty: advanced
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

# Episode 3-5: Taking Command of the Ship Controls

**Synopsis:** We implement some basic steering controls for our Space Ship using the C64 keyboard.  

**Download via  dust:** $ dust tutorials (select 'spritro') 

**Github Repository:**

[Spritro Source Code on Github](https://github.com/actraiser/dust-tutorial-c64-spritro)

- [Episode 3-1: Spritro - An Intro with a Sprite](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-1-spritro-an-intro-with-a-sprite)
- [Episode 3-2: Creating the Shapes - Hello SpritePad](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-2-creating-the-shapes-hello-spritepad)
- [Episode 3-3: Loading Shapes and grasping Symbols](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-3-loading-shapes-and-grasping-symbols)
- [Episode 3-4: Flying the Space Ship off Course](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-4-flying-the-space-ship-off-course)
- **Episode 3-5: Taking Command of the Ship Controls**
- [Episode 3-6: Custom Character Sets - Hello CharPad](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-6-custom-character-sets-hello-charpad)
- [Episode 3-7: Creating Pseudo Timers for Color Cycle](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-7-creating-pseudo-timers-for-color-cycle)
- [Episode 3-8: If the SID doesn't fit, use a bigger Hammer](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-8-if-the-sid-doesnt-fit-use-a-bigger-hammer)
- [Episode 3-9: Greetings, Acknowledgments and Links](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-9-greetings-acknowledgments-and-links)

### Steering the Ship

The Intro comes with some basic keyboard controls. You can hit the key D to steer the ship downwards to the bottom border area or U to fly upwards to the top. If we would use Kernel routines this would be a no-brainer as all you need to know about what key is currently pressed is stored by the Kernel in a specific memory locations. However, as usual, this is slow compared to accessing the hardware directly. 

Once you understand how the different Keys are stored in memory and addressed using the CIAs the resulting routine is actually very small.

**Querying the Keyboard Matrix**

Your C64 has 66 Keys where SHIFT-LOCK and RESTORE being not part of the internal Keyboard Matrix. RESTORE is connected to the NMI, thus it triggers an non-maskable interrupt when pressed. SHIFT-LOCK is actually a switch and not a key per se so it is like-wise not detectable within the Keyboard Matrix.

All other 64 keys can be easily addressed and checked using the SCNKEY Kernal routine. However, as already pointed out we want to work without the Kernal, so we need to go one layer deeper into the hardware.

The Keyboard Matrix System can be imagined as 8x8 Grid where Rows and Columns can be individually accessed by the CIA-1 which is one of two Complex Interface Adapters (CIA 6526) in the Commodore C64. 

The approach to check for an individual pressed key is actually not very hard. You first need to set up two so-called Data Direction Registers. Then you look at the Keyboard Matrix below and identify the row with your key in question. The value of that Row from that Table needs to be put into the Port Register A at $dc00. When this is done we just need to load the Port Register B $dc01 and test it against a Bit pattern to check if the appropriate key was pressed.

What needs to be considered is that the Bits in $dc00 and $dc01 are low-active, so if a key is pressed, a Bit is 0, if it is not pressed the Bit is set high.

**Let's do an example! **

Below is the matrix as organized between the two Port Register A and Port Register B. Next to each key the Screen Code is shown for the sake of completeness but it is not required for the following scan. The testing for keys without supplied Screen Code need some additional checking in other registers which we will not discuss at this point.

So let's check if the "x" key is currently pressed because we may want to exit a program in that case. If we follow the approach outlined above we need to set the Data Direction Registers first so reading is actually possible. Then we write the Bit Pattern of the third row into Port Register A and can afterwards query if Bit#7 of Port Register B to check if it is NOT set. When this is the case the 'x' key is pressed down.

**Now for the code:**

When you have the table - it is really not hard to follow.

With this knowledge we can easily test for three different keys, the 'u'-key, the 'd'-key and the 'Space'-key and act accordingly, that is move the ship one Y-Coordinate up or down or exit the program. Additionally we want to add a boundary in the top and bottom of the screen so the ship can not vanish.

As you can see, it is not very hard to check for a specific key press and take actions accordingly. We check for three keys consecutively before we either return with rts or if we identified one of the keys take some action before returning.

-act

---
*Fonte originale: [https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-5-taking-command-of-the-ship-controls](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-5-taking-command-of-the-ship-controls)*


### Collegamenti e Riferimenti Hardware
- **$DC00 (CIA 1 Port A (Joystick 2, Keyboard))**: Associato al chip CIA. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#dc00).
- **$DC01 (CIA 1 Port B (Joystick 1, Keyboard))**: Associato al chip CIA. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#dc01).

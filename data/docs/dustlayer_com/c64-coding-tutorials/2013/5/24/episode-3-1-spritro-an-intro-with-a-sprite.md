---
title: ''
source_url: https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-1-spritro-an-intro-with-a-sprite
category: tutorial
topics:
- assembly
- basic
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

# Episode 3-1: Spritro - an Intro with a Sprite

**Synopsis:** In this huge Episode we will analyze an intro with an animated Sprite controlled via Keyboard. To spice up the action we add a new color cycle effect and open the top and bottom borders where our sprite can freely move into. Finally we fix a SID file which is not locating it's data at our desired memory location. 

**Download via  dust:** $ dust tutorials (select 'spritro') 

**Github Repository:**

[Spritro Source Code on Github](https://github.com/actraiser/dust-tutorial-c64-spritro)

- **Episode 3-1: Spritro - An Intro with a Sprite**
- [Episode 3-2: Creating the Shapes - Hello SpritePad](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-2-creating-the-shapes-hello-spritepad)
- [Episode 3-3: Loading Shapes and grasping Symbols](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-3-loading-shapes-and-grasping-symbols)
- [Episode 3-4: Flying the Space Ship off Course](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-4-flying-the-space-ship-off-course)
- [Episode 3-5: Taking Command of the Ship Controls](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-5-taking-command-of-the-ship-controls)
- [Episode 3-6: Custom Character Sets - Hello CharPad](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-6-custom-character-sets-hello-charpad)
- [Episode 3-7: Creating Pseudo Timers for Color Cycle](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-7-creating-pseudo-timers-for-color-cycle)
- [Episode 3-8: If the SID doesn't fit, use a bigger Hammer](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-8-if-the-sid-doesnt-fit-use-a-bigger-hammer)
- [Episode 3-9: Greetings, Acknowledgments and Links](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-9-greetings-acknowledgments-and-links)

### Spritro - a simple intro with a Sprite

Welcome to a new multi-part tutorial on C64 programming on dustlayer.com! It's been a month since the last coding tutorial but I did not waste a lot of time in-between but filled the site with a few in-depth knowledge base articles.

If you have not read the Knowledge Base Series [VIC-II for Beginners](https://dustlayer.squarespace.com/vic-ii/2013/4/22/when-visibility-matters), [Math Basics](https://dustlayer.squarespace.com/cpu-6510-articles/2013/4/18/math-basics-number-systems) and [Hardware Basics](https://dustlayer.squarespace.com/c64-architecture/2013/5/7/hardware-basics-part-1-tick-tock-know-your-clock) yet - I encourage to do so. 

I improved a bit on my coding style and changed things around in how I structure new projects. This first chapter is an overview of the actual outcome of this tutorial and how everything is organized.

**But first **- download the Spritro via DUST or clone it from the Github repository linked above, then build it. If you are too lazy to do this now, you can also watch the following video.

### Some obvious and not so obvious features

This little intro comes with an **animated Sprite **- of course you know it's the famous [Manta Class Ship from Uridium](http://www.lemon64.com/?game_id=2766). It **moves smoothly** from right to left - but did you notice something?! Is this ship not a bit low on the screen? Shouldn't there be a border?! 

It should! But by exploiting a VIC-II bug the** top and bottem borders have been removed **and the Sprite can freely move across 312 PAL Rasterlines on the screen. You also have some **control by hitting the U or D key** to move the ship up and down. 

Additionally as opposed to the [First Intro Tutorial](https://dustlayer.com/c64-coding-tutorials/2013/2/17/a-simple-c64-intro) we use a **custom font** to display some text on the screen - actually it is a very popular character set from the game [Rambo First Blood Part II](http://www.lemon64.com/?game_id=2084) - used in dozens of other games and intros before. 

The different **color cycle effect** on the text is this time not based on a table of values but kinda syncs with the 16 frames of the Ship animation. If you don't understand at this moment - don't worry, I will explain it along the way. There is also a periodic switching of colors in the side borders to **demo how to delay timing** of effects while on the interrupt.   

Last but not least an **awesome SID tune** is playing - this time *"Empty (512 Bytes)"* by 4-Mat. The original SID file places it's play routine and data in a memory location not suitable for our intro so we** learn how to relocate SIDs** in memory. This is a task  which was rather tedious to do not so long ago but with a recently released tool it has become incredibly easy. 

That's it! We have a lot of ground to cover but first, I want to explain what you find where in the project.

### Project Structure

As with the last tutorial we stick to three directories and an index files.

The** index.asm** file is basically something like a header file which includes all the other source code files from the project plus it sets up a BASIC loader so we do not have to type *SYS 49152* ourselves after loading the .prg. It is the file you compile against to build your .prg output file.

If the **/ build-directory** does not exist, it is created automatically when you compile the intro for the first time. It contains the finished 

*executable .prg file*and - if you use DUST - a list of

*labels and their memory addresses*are dumped here into a file and on the screen as well. If the labels are not generated you need to update DUST with the command 'dust setup' and select option 1 ("install all").

****The*  /resources-directory* includes  all our binaries we like to load into the intro, namely a SID file, our custom character set and of course the Sprite Data. 

Finally the * /code-directory *includes all the routines and other code. The prefixes on each file indicate their role. 

* config-files *set up something, e.g. place a loaded sprite at the desired memory location, initialize registers at start, setup symbols, define how to actually load a binary. 

* data-files* are strings or tables with information to iterate over. For Spritro it's just three lines of static text. 

* sub-files* are subroutines. I use one file per subroutine usually and the name of the file minus the prefix corresponds to the label in the code you would jump to. 

Finally, the * main.asm* file is the basis of our custom interrupt routine and executes all the other subroutines either one-time or periodically during the interrupt.

### Ready, Set, Go!

Now go to the next chapter which will deal with the Sprite creation process. Enjoy this new Episode and don't hesitate to send comments or like my [Facebook page](http://www.facebook.com/dustlayer.c64.coding) or follow me on [Twitter](https://twitter.com/actraiser).

-act

---
*Fonte originale: [https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-1-spritro-an-intro-with-a-sprite](https://dustlayer.com/c64-coding-tutorials/2013/5/24/episode-3-1-spritro-an-intro-with-a-sprite)*

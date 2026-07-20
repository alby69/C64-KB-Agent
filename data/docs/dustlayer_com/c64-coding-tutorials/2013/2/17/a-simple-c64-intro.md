---
title: ''
source_url: https://dustlayer.com/c64-coding-tutorials/2013/2/17/a-simple-c64-intro
category: tutorial
topics:
- basic
- assembly
difficulty: beginner
language: assembly
hardware:
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
- kernal-routines
- memory-map
scraped_at: '2026-07-20'
---


# 

# Episode 2-1: Let's compile and run C64 code

**Topics:** In this first tutorial I want to cover some basics like loading code, writing text to screen, adding effects and include music. No indepth explanations yet, let's get an initial feeling for C64 coding.  

**Download via  dust:** $ dust tutorials (select 'first intro')

**Github Repository:**

[First Intro on Github](https://github.com/actraiser/dust-tutorial-c64-first-intro)

- **Episode 2-1: Let's compile and run C64 code**
- [Episode 2-2: Writing to the C64 Screen](http://dustlayer.com/c64-coding-tutorials/2013/4/8/episode-2-2-writing-to-the-c64-screen)
- [Episode 2-3: Did I interrupt you?](http://dustlayer.com/c64-coding-tutorials/2013/4/8/episode-2-3-did-i-interrupt-you)
- [Episode 2-4: Effects using a table of data](http://dustlayer.com/c64-coding-tutorials/2013/4/8/episode-2-4-reading-from-a-data-table)
- [Episode 2-5: Understanding and including music](http://dustlayer.com/c64-coding-tutorials/2013/4/8/episode-2-5-understanding-and-including-music)

### We start simple but not too simple

**Is there something more boring then the "inc $d020" tutorials seen on most C64 beginner tutorials?** I think people who start coding the C64 want to do the cool stuff they did not understand in the past. And new people to C64 coding must get an immediate understanding with how little effort you can achieve cool stuff. I think if you want to get people excited about C64 development one must provide a breath of retro demo coding. On the other hand I understand that a lot of simplification is required to not frustrate people on their first steps. Anyways, if you wonder what that standard introduction into C64 coding looks like, here is a screenshot.

### A real C64 intro explained

As opposed to the boring screenshot above the little intro that we will inspect during this tutorial is simple but as a kid in the 80s I would have thought it is  looking cool. Basically something I wanted to achieve myself one day after I understand how to code C64 - I  just did not expect to wait for over 25 years. The intro is not much more complex than let's say [the famous Dynamic Duo intro](http://www.youtube.com/watch?v=nLaVqPULd7I) and how much did I admire those guys and felt good whenever I saw the intro.


All our little intro does is to display two lines of text with a rotor-like colorcycle effect and it plays some background music.

When the code has been downloaded, just change into the directory and run "dust compile". Vice should open and the compiled intro will be loaded in the emulator. If you don't use DUST there is some advice in the [second chapter](http://dustlayer.com/c64-coding-tutorials/2013/4/8/working-without-dust-environment) of this tutorial.

**Here is a video of the actual program.**

Wow! So simple but it somewhat catches the beginner with the nice sid music and the color cycling, does it not?

So what we do here is putting two lines of text using the standard C64 font in the middle of the screen, do twice the color cycle effect in two different directions for each line and last but not least make sure the music is played while all this crazy stuff happens.

### The basics you will get introduced to

In the next chapters I will describe in details everything that is required to understand what is going on in the intro. We will touch programming of the interrupt, you will also soon understand how memory, and in particular the screen, is organized on the C64. I will explain how to iterate over tables of data, e.g. to change color information or to display a line of text. Finally we will include the music into the intro and look how initialization and playback work.

---
*Fonte originale: [https://dustlayer.com/c64-coding-tutorials/2013/2/17/a-simple-c64-intro](https://dustlayer.com/c64-coding-tutorials/2013/2/17/a-simple-c64-intro)*


### Collegamenti e Riferimenti Hardware
- **$D020 (Border Color)**: Associato al chip VIC-II. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#d020).

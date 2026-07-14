---
title: Drawing the sun
source_url: https://elite.bbcelite.com/deep_dives/drawing_the_sun.html
category: deep-dive
topics:
- basic
- assembly
difficulty: beginner
language: mixed
hardware:
- CPU
- SID
- KERNAL
- CIA
related:
- keyboard-handling
- music-player
- sound-programming
- joystick-reading
- memory-map
- kernal-routines
- sid-registers
- cia-registers
scraped_at: '2026-07-14'
---

# Drawing the sun

## Drawing and storing the sun, and the systems on the Short-range Chart

The sun in Elite is an absolute sight to behold, with its flickering fringes and bright, white glare that lights up even the darkest corners of space. Perhaps surprisingly, it turns out to be quite a lot easier to draw the sun than the meridians and craters of the planets.

It also comes in three flavours. First, there's the white-hot sun of the BBC Micro and Acorn Electron versions:

![The sun in BBC Micro Elite](https://elite.bbcelite.com/images/cassette/sun.png) 

						Then there's the red-and-yellow sun of the 6502 Second Processor and BBC Master versions:

![The sun in 6502 Second Processor Elite](https://elite.bbcelite.com/images/6502sp/sun.png) 

						And finally, there's the super-hot blue star of the NES version:

![The sun in NES Elite](https://elite.bbcelite.com/images/nes/general/sun.png) 

						Let's see what it takes to let there be light in the Elite universe.

## Line by line

													 ------------

						Unlike the planets, which are drawn as circles, the sun is drawn by the [SUN](https://elite.bbcelite.com/cassette/main/subroutine/sun_part_1_of_4.html) routine as a set of horizontal lines, with one line per pixel line on-screen. This is how the shimmering edges are drawn, by randomly making the lines shorter or longer (more on that later). The exact same process is used to remove the sun from the screen in the [WPLS](https://elite.bbcelite.com/cassette/main/subroutine/wpls.html) routine.

Note that the NES version of Elite calculates sun lines in the same way as the other versions, but it doesn't store the results, as it doesn't need to remove the sun from the screen. Also, the horizontal line-drawing routines are optimised for drawing the sun into tiles; see the deep dive on [drawing lines in the NES version](https://elite.bbcelite.com/drawing_lines_in_the_nes_version.html) for more details.

In all versions, each sun line is defined by two parameters: the coordinate of the centre of the line, and the length of the line from its centre to one end (which we call the "half-width", as it's half the width of the full horizontal line). For the sun, all the lines have the same centre x-coordinate, which is the same x-coordinate as the centre of the sun.

Given this, we can draw the sun line by line, and all we need to calculate is the half-width of the line for that particular y-coordinate. We can do this using nothing more complicated than Pythagoras - there's no need for any trigonometry here. Consider drawing a sun line near the bottom of a sun with radius K, let's say the line that is V lines below the centre. It looks something like this:

```
                         _ - _
                      =         =
                    =             =                   |`.
                   =               =                  |  `.  K
  We want          =       |`.     =                V |    `.
  to draw           =      |  `.  =         __-->     |      `.
  this line ------>  ._____|____`.   ___.--´          +--------`
                         - _ -                     SQRT(K^2 - V^2)
```
						Looking at the triangle from the centre of the sun down to the horizontal line we want to draw, we can apply Pythagoras to calculate that the half-width of the line we want to draw is SQRT(K^2 - V^2), so along with the value of V we have all the data we need to draw that line, and by extension the whole ball of fire.

## Flickering fringes

													 ------------------

						The sun's flickering fringes are easy enough to implement in this model.

We start by calculating a figure between 0 and 7, with bigger numbers for bigger suns, and call this the "fringe size", which we store in CNT. This defines the width of the pulsating fringe around the sun (which explains why the sun stops flickering when it's far away - it has a fringe size of 0).

Then, when calculating the half-width of each line using the method above, we simply pick a random number between 0 and the fringe size, and add it to the half-width. This makes the sun symmetrical around its vertical meridian, and as the random number changes for each line and for each redraw of the sun, the sun's fringes shimmer and flicker. It's simple but very effective, and it adds very little effort, even to the erase procedure, as we can see in the next section.

## Drawing and storing sun lines with SUN

													 --------------------------------------

						As with all objects in the sky, we can erase the sun from the screen by drawing it a second time in the same place as before, so it cancels out the existing sun using EOR logic. Although the maths above isn't complex, it is still pretty time-consuming, especially with a large sun on the screen, so as with the planets, the sun has its own line heap, stored at LSO, which stores the data for every line in the current sun. (Note that the NES version is an exception, as it uses screen buffers for each frame and doesn't need to erase the screen contents, so it doesn't have any line heaps at all. See the deep dive on [drawing vector graphics using NES tiles](https://elite.bbcelite.com/drawing_vector_graphics_using_nes_tiles.html) for details.)

The first location at LSO has a special meaning:

- LSO = 1 indicates the line heap contains data
- LSO = &FF indicates the line heap is empty

Because the sun is made up of lines and it can fill the entire space view, the sun's line heap contains 192 values, one for each of the lines on the screen. The value in LSO+Y contains details of the sun's line on pixel row Y, with a 0 indicating there is no line, and a non-zero value containing the half-width of the sun line on that y-coordinate. Along with the sun's centre coordinates in SUNX and SUNY, the line heap contains everything we need to know in order to draw the sun, all without having to recalculate anything.

This also applies to the random fringe factor that we add to the half-width to make the sun shimmer. As we're only storing the half-width and that contains the random fringe size, we can store and redraw shimmering suns with no more effort than a clean ball sun. It's remarkably elegant for such a complicated- looking graphical effect.

## Drawing flicker-free and efficient sun lines

													 --------------------------------------------

						The SUN routine combines the drawing of the new sun and the removal of the old one into one pass through the line heap, from the bottom of the screen to the top (so from the end of the heap to the start). We do this in [part 2](https://elite.bbcelite.com/cassette/main/subroutine/sun_part_2_of_4.html) by starting at the bottom and plotting each sun line in turn from the line heap as we move up the screen. As each line is plotted, thus erasing the old sun, it is removed from the line heap.

We do this until we reach the point where we need to start drawing the new sun, at which point we move into [part 3](https://elite.bbcelite.com/cassette/main/subroutine/sun_part_3_of_4.html). This part of the code removes the old sun line and replaces it with the new one, and this is done in a rather clever way that's much more efficient than simply erasing the old line and drawing the new one. The code works out what we need to add or erase from each end of the old sun line to turn it into the new sun line, and then it only applies those changes, leaving alone any part of the line that needs to remain white. This minimises the amount of on-screen change, and because of this the sun is totally flicker-free, unlike the ships and planets (which are erased and redrawn using EOR logic, and which therefore flicker noticeably). This approach also minimises the amount of line-drawing that's required, making it quicker than a simple erase-and-replace approach would be.

After updating each line, we replace the value in the line heap with the new line's half-width, so the new sun can be erased in the same way. Once the new sun is drawn, we then keep heading up the screen in [part 4](https://elite.bbcelite.com/cassette/main/subroutine/sun_part_4_of_4.html), where we redraw any remaining lines from the old sun, thus removing them from the screen, and leaving just the new sun on show.

The LSO line heap block shares its memory with the ship line heap for the space station. This memory can be shared as our local bubble of universe can support either the sun or a space station, but not both.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
_ - _
                      =         =
                    =             =                   |`.
                   =               =                  |  `.  K
  We want          =       |`.     =                V |    `.
  to draw           =      |  `.  =         __-->     |      `.
  this line ------>  ._____|____`.   ___.--´          +--------`
                         - _ -                     SQRT(K^2 - V^2)
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/drawing_the_sun.html](https://elite.bbcelite.com/deep_dives/drawing_the_sun.html)*

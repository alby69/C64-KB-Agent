---
title: Line-clipping
source_url: https://elite.bbcelite.com/deep_dives/line-clipping.html
category: deep-dive
topics:
- basic
- assembly
difficulty: beginner
language: mixed
hardware:
- SID
- KERNAL
related:
- music-player
- sound-programming
- memory-map
- kernal-routines
- sid-registers
scraped_at: '2026-07-14'
---

# Line-clipping

## Efficiently clipping an extended line to the part that's on-screen

Space is big. Vintage computer screens, however, are not big. Elite's space view is a whopping 256 pixels across and 192 pixels high, and somehow we have to cram planets, suns and seat-of-the-pants space battles into this tiny, thumbnail-sized bit of cathode-ray real estate. This isn't easy.

The first part of the solution is to simulate not only the part of space that's visible on-screen, but the surroundings too. Elite's extended screen coordinate system takes care of this - see the deep dive on [extended screen coordinates](https://elite.bbcelite.com/extended_screen_coordinates.html) for details.

The second part of the solution is efficient line-clipping, which ensures that large shapes like the planet below only appear within the space view, and don't extend down into the dashboard:

![A clipped planet BBC Micro Elite](https://elite.bbcelite.com/images/cassette/clipping.png) 

						The extended screen coordinate system caters for objects outside of the screen bounds, so when the game actually comes to draw these objects in the space view, it needs to work out exactly which lines to draw on-screen, and that's where the line-clipping routines come in. They take lines made up of 16-bit coordinates and work out whether any of that line is on-screen, and return the portion that's visible. In a sense, the screen is a small portal onto the wider universe, and line-clipping is the process of working out what we can see through that portal.

Line-clipping is done in two stages. The first stage in routine [LL145](https://elite.bbcelite.com/cassette/main/subroutine/ll145_part_1_of_4.html) works out whether the line intersects the screen at any point, and if it does, then the second stage in routine [LL118](https://elite.bbcelite.com/cassette/main/subroutine/ll118.html) clips the line and returns the portion that appears on-screen, which we then need to draw.

Let's see how these two stages work.

## LL145: Working out whether to clip a line

													 -----------------------------------------

						The line-clipping routine starts with a call to LL145, which checks whether the line is worth clipping - in other words, whether the line passes through the screen at any point. As the actual clipping process the LL118 routine, is quite involved, it's worth spending time checking whether we need to call it at all.

Here's a breakdown of how LL145 determines whether a line is partly or wholly on screen, and therefore whether it's worth sending to LL118 to be clipped.

- If both coordinates are on-screen, then return with success as the line doesn't need clipping and already fits on-screen
- Otherwise, set XX13 to reflect which point(s) are on-screen and off-screen

- If both points are off-screen and both points are past the same screen edge, then return with failure
- If moving both points left by one screen doesn't move at least one of them past the left edge of the screen (i.e. if neither of them is in the vertical screen-wide strip to the right of the screen), return with failure
- If moving both points up by one screen doesn't move at least one of them past the top edge of the screen (i.e. if neither of them is in the horizontal screen-high strip below the bottom of the screen), return with failure (this test needs to be done only using the space view portion of the screen)

- Calculate the line gradient from the 16-bit coordinates, calculating it the right way round to make it a fractional gradient:
								- Calculate (delta_x / delta_y) if delta_x < delta_y
- Calculate (delta_y / delta_x) if delta_x >= delta_y
 

- Do the actual clipping by calling LL118 to move one end of the line at a time (so if both points need moving on-screen, we call LL118 twice)
- If both the original coordinates were off-screen, double-check that the clipped line is indeed on-screen, and if not return with failure
- Return the clipped line with success, and with XX13 and SWAP set to describe the kind of clipping we had to do

## LL118: Clipping a line

													 ----------------------

						[LL118](https://elite.bbcelite.com/cassette/main/subroutine/ll118.html) is called by LL145 when we think a line crosses the screen. It only clips one end of the line, so if LL145 finds that both ends need clipping, it calls LL118 twice, once for each end.

This is how it works. Given a point (x1, y1), we move the point along the line until it is on-screen, which effectively clips the (x1, y1) end of a line to be on the screen. The movement process depends on the line's gradient, the direction of slope (i.e. top left to bottom right, or top right to bottom left), and the steepness of slope (i.e. is it more vertical than horizontal).

For example, if x1 is negative, i.e. off the left edge of the screen, we move the point right along the line until x1 = 0. We calculate the new y1 by multiplying the distance travelled in the x-direction by the gradient.

Similar logic is applied when the point is off-screen to the right, top or bottom. Also, because the gradient is always stored as a fractional value (it's less than 1.0, just expressed as a byte), then when the line is more vertical than horizontal, the value stored is actually 1 / gradient, as that way it fits into the byte. Because of this, if the line is more vertical than horizontal, we have to divide by the gradient rather than multiply to get the same result.

---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/line-clipping.html](https://elite.bbcelite.com/deep_dives/line-clipping.html)*

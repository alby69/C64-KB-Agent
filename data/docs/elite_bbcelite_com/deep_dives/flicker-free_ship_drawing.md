---
title: Flicker-free ship drawing
source_url: https://elite.bbcelite.com/deep_dives/flicker-free_ship_drawing.html
category: deep-dive
topics:
- basic
- assembly
- sprite programming
difficulty: beginner
language: mixed
hardware:
- KERNAL
- SID
related:
- sid-registers
- sound-programming
- vic-ii-registers
- memory-map
- kernal-routines
- music-player
- sprite-programming
- raster-interrupts
scraped_at: '2026-07-20'
---

# Flicker-free ship drawing

## How the BBC Master and Apple II versions reduce flicker when drawing ships

Probably the most celebrated feature of the BBC Master version of Elite is its flicker-free ship animation, an improvement that is obvious from the moment the Cobra Mk III twists into view on the game's title screen. While the original versions of Elite shimmer like old black-and-white movies, the ships in the Master version morph smoothly through each twist and turn, with barely any flicker at all.

![The title screen in BBC Master Elite](https://elite.bbcelite.com/images/master/title.png) 

						Contrary to what you might expect, this isn't because the Master is equipped with shadow RAM, and there are no clever bank-switching tricks being used here. Instead, the Master's slicker ship animation is down to a relatively simple tweak to the original ship-drawing routines at LL9 and SHPPT, a change that requires only a tiny number of extra bytes but really transforms the quality of Elite's graphics. Indeed, this improved algorithm was first seen in the Apple II version of Elite, which was released slightly earlier in 1986, the same year as the BBC Master version; the Apple II may have been approaching a decade of service by this point, but its version of Elite was still beautifully flicker-free, though the slower graphics didn't show it off quite as well as the faster Master.

You can read more about the standard ship-drawing process in the deep dive on [drawing ships](https://elite.bbcelite.com/drawing_ships.html), and the deep dive on [backporting the algorithm](https://elite.bbcelite.com/backporting_the_flicker-free_algorithm.html) contains the actual code changes. For the purposes of this deep dive, let's look at the differences between the original and flicker-free versions.

## Removing flicker from LL9

													 -------------------------

						All the code changes for flicker-free ship drawing can be found in the main ship-drawing routines at [LL9](https://elite.bbcelite.com/master/main/subroutine/ll9_part_1_of_12.html) (for nearby wireframe ships) and [SHPPT](https://elite.bbcelite.com/master/main/subroutine/shppt.html) (for distant ship dots), while the actual line-drawing in the new system is done in [LSPUT](https://elite.bbcelite.com/master/main/subroutine/lsput.html). Let's look at LL9 first.

In the following, the "old ship" is the ship that is already shown on-screen, and the "new ship" is the one that we want to replace it with. When we call the ship-drawing routine, we know that the ship line heap contains the lines of the old on-screen ship that we need to erase, and as we draw the new ship, we need to make sure we replace the contents of the ship line heap with the lines of the new ship, so the whole cycle can continue.

The following table compares the [old ship-drawing routine](https://elite.bbcelite.com/cassette/main/subroutine/ll9_part_1_of_12.html) in the BBC Micro versions with the [new flicker-free system](https://elite.bbcelite.com/master/main/subroutine/ll9_part_1_of_12.html) in the BBC Master, and you can click on the step numbers in the first column of the table to see the individual code variations in those stages of LL9.

| Step | Old approach | New approach | 
|---|---|---|
| [#1](https://elite.bbcelite.com/compare/main/subroutine/ll9_part_1_of_12.html) | Erase the old ship by drawing the contents of ship line heap | Initialise flicker-free animation by setting up the pointers in LSNUM | 
| #2-#8 | Calculate the visibility of the new ship's faces and vertices (the code in these steps is unchanged in the flicker-free version) | |
| [#9](https://elite.bbcelite.com/compare/main/subroutine/ll9_part_9_of_12.html) | Draw the laser line, if there is one, using LL30 | Draw the laser line, if there is one, using LSPUT | 
| [#10](https://elite.bbcelite.com/compare/main/subroutine/ll9_part_10_of_12.html) | Calculate the visibility of the new ship's edges (the code in this step is broadly similar in the flicker-free version) | |
| [#11](https://elite.bbcelite.com/compare/main/subroutine/ll9_part_11_of_12.html) | Store the visible edges in the ship line heap | Draw each visible edge using LSPUT | 
| [#12](https://elite.bbcelite.com/compare/main/subroutine/ll9_part_12_of_12.html) | Draw all the lines in the ship line heap to draw the new ship | Draw any remaining lines from the old ship in the ship line heap | 

The flicker-free initialisation in step #1 works like this:

- Point LSNUM to the start of the ship line heap
- Point LSNUM2 to the end of the current ship line heap, so it points to the last line of the on-screen ship (or set it to 0 if there is no ship currently on-screen)

Then the new [LSPUT](https://elite.bbcelite.com/master/main/subroutine/lsput.html) routine in steps #9 and #11 works like this:

- Draw the new line
- Fetch the corresponding old line from position LSNUM in the ship line heap
- Store the new line in the heap at this position, replacing the old one
- Draw the old line to remove it from the screen
- Increment LSNUM to point to the next old line in the ship line heap

In this way the ship is erased and redrawn one line at a time, instead of being erased all in one go and then being redrawn in full, and that's how the Master version reduces flicker. It's a surprisingly simple change, and we can also apply it to ship dots with very little effort.

## Removing flicker from SHPPT

													 ---------------------------

						The [SHPPT](https://elite.bbcelite.com/master/main/subroutine/shppt.html) routine, which draws distant ships as dots, is also reworked and in exactly the same way, as it uses the same ship line heap approach as LL9 (it draws one line for the top dash and another line for the bottom dash, so even the dots are wireframes). So in the flicker-free world it uses the exact same approach as LL9, using LSNUM and LSPUT in the same way to produce flicker-free ship dots as well.

You can see the changes side-by-side by [comparing the different versions of SHPPT](https://elite.bbcelite.com/compare/main/subroutine/shppt.html), or by looking at how the [old dot-drawing routine](https://elite.bbcelite.com/cassette/main/subroutine/shppt.html) in the BBC Micro versions compares with the [new flicker-free system](https://elite.bbcelite.com/master/main/subroutine/shppt.html) in the BBC Master. The changes are identical to those made to the ship-drawing routine, just for dot lines instead of wireframes.

So, both ships and ship dots are drawn in the Master version without flicker, and using the exact same approach. Given that both ships and ship dots are already being stored in the ship line heap as individual line segments, this is a change that has a very low impact in terms of code, but a very high impact on-screen.

The moment the penny dropped and the authors realised they could do this? I bet that was a good day...

---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/flicker-free_ship_drawing.html](https://elite.bbcelite.com/deep_dives/flicker-free_ship_drawing.html)*

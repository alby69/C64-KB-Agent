---
title: The ball line heap
source_url: https://elite.bbcelite.com/deep_dives/the_ball_line_heap.html
category: deep-dive
topics:
- sprite programming
- assembly
difficulty: beginner
language: mixed
hardware:
- CPU
- KERNAL
- CIA
related:
- keyboard-handling
- joystick-reading
- raster-interrupts
- memory-map
- sprite-programming
- vic-ii-registers
- kernal-routines
- cia-registers
scraped_at: '2026-07-14'
---

# The ball line heap

## How we remember the lines used to draw circles so they can be redrawn

The planet, the sun and ships in our local bubble of universe are complicated things, and we have to use an awful lot of maths to calculate their shapes on-screen. Not surprisingly, all that maths takes up quite a bit of processor time. We can remove shapes from the screen by drawing the same shapes again in exactly the same place (which erases them because it's all done with EOR logic), so if we can avoid having to repeat all those intensive calculations for that second drawing, that would save a lot of time and effort.

Not surprisingly, Elite has a solution - three of them, to be precise. Instead of repeating the calculations for the second drawing, Elite has a set of three "line heaps" where all the drawing information gets stored, so it's a simple process to redraw, and therefore erase, any shape on-screen, from ships to planets:

![A view of Diso in BBC Micro Elite](https://elite.bbcelite.com/images/ellipses/diso.png) 

						(Note that the NES version is an exception, as it uses screen buffers for each frame and doesn't need to erase the screen contents, so it doesn't have any line heaps at all. See the deep dive on [drawing vector graphics using NES tiles](https://elite.bbcelite.com/drawing_vector_graphics_using_nes_tiles.html) for details.)

There are three types of line heap used in Elite:

- The ball line heap, which is used by the [BLINE](https://elite.bbcelite.com/cassette/main/subroutine/bline.html)routine when drawing circles (as well as polygonal rings like the launch and hyperspace tunnel)
- The sun line heap, which is used by the SUN routine when drawing the sun (see the deep dive on [drawing the sun](https://elite.bbcelite.com/drawing_the_sun.html)for details)
- The ship line heap, one per ship in the local bubble of universe, which is used by the LL9 routine when drawing ships (see the deep dive on [drawing ships](https://elite.bbcelite.com/drawing_ships.html)for details)

Here we take a look at the ball line heap that's stored at [LSX2](https://elite.bbcelite.com/cassette/main/workspace/wp.html#lsx2) and [LSY2](https://elite.bbcelite.com/cassette/main/workspace/wp.html#lsy2), and with the pointer in [LSP](https://elite.bbcelite.com/cassette/main/workspace/zp.html#lsp).

## Drawing and storing circles with BLINE

													 --------------------------------------

						We draw a circle by repeated calls to BLINE, passing the next point around the circle with each subsequent call, until the circle (or half-circle) is drawn.

Calling the routine with a value of &FF in FLAG initialises the line heap and stores the first point in memory rather than in the heap, so it's ready for the second call to BLINE, which is when we actually have a segment to draw and store in the line heap.

The routine keeps a tally of the points passed to it on each call, storing them in the line heaps at LSX2 and LSY2, and using the line heap pointer in LSP (which points to the end of the heap). It also keeps the point from the previous call to BLINE in K5(3 2 1 0), so it can draw a segment between the last point and this one.

If a line doesn't fit on-screen, then it isn't drawn or stored in the heap. Instead a &FF marker is inserted into the LSY2 entry at the current position, which indicates to the next call to BLINE that it should start a new segment. In this way broken, non-continuous lines can still be stored in the line heap.

Keeping the points in the line heap lets us quickly redraw the circle without needing to regenerate all the points, so it is easy to remove the circle from the screen by simply redrawing all the segments stored in the line heaps. This is done in [WPLS2](https://elite.bbcelite.com/cassette/main/subroutine/wpls2.html).

## How the LSX2 and LSY2 heaps are structured

													 ------------------------------------------

						The ball line heap is stored in 78 bytes at LSX2 and another 78 bytes at LSY2. The LSP variable points to the number of the first free entry at the end of the heap, so LSP = 1 indicates that the heap is empty.

The first location at LSX2 has a special meaning:

- LSX2 = 0 indicates the line heap contains data
- LSX2 = &FF indicates the line heap is empty

Meanwhile, if a y-coordinate in LSY2 is &FF, then this means the next point in the heap represents the start of a new segment, rather than a continuation of the previous one. Specifically, this is the layout in the heap:

LSX2 ... X1 X2 ... LSY2 ... &FF Y1 Y2 ...

The first entry in the table at LSY2 is always &FF, as the first point is always the start of a segment, so the start of a non-empty line heap looks like this:

LSX2 0 X1 X2 X3 ... LSY2 &FF Y1 Y2 Y3 ...

When a planet is plotted for the second time to remove it from screen, the heaps are reset by setting LSP to 1 and inserting a &FF at the start of LSX2. See WPLS2 for details.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
LSX2  ...      X1  X2 ...
  LSY2  ... &FF  Y1  Y2 ...
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
LSX2  0    X1  X2  X3 ...
  LSY2  &FF  Y1  Y2  Y3 ...
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/the_ball_line_heap.html](https://elite.bbcelite.com/deep_dives/the_ball_line_heap.html)*

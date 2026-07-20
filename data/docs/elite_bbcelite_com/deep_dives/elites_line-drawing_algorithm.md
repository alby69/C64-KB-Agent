---
title: Elite's line-drawing algorithm
source_url: https://elite.bbcelite.com/deep_dives/elites_line-drawing_algorithm.html
category: deep-dive
topics:
- basic
- assembly
difficulty: beginner
language: mixed
hardware:
- KERNAL
- SID
- CPU
- CIA
related:
- sid-registers
- sound-programming
- joystick-reading
- keyboard-handling
- kernal-routines
- memory-map
- music-player
- cia-registers
scraped_at: '2026-07-20'
---

# Elite's line-drawing algorithm

## The main line-drawing algorithm used to draw non-horizontal lines

Most of what you see in the space view in Elite is composed of straight lines. The ships are drawn using wireframes that are made up of straight lines, the planets are made from circles and arcs that consist of lots of small, straight lines, and the sun is no more than a sequence of horizontal lines, drawn along a vertical axis. Having a fast line-drawing algorithm is essential in a game like Elite.

Horizontal lines are a special case and have their own optimised routine at [HLOIN](https://elite.bbcelite.com/cassette/main/subroutine/hloin.html), but all non-horizontal lines in Elite are drawn by the [LOIN](https://elite.bbcelite.com/cassette/main/subroutine/loin_part_1_of_7.html) routine. This routine draws lines by stepping along the gentlest slope of each line, drawing one pixel at a time, so lines drawn by this method are stepped in quite a distinctive manner, as you can see from this close-up of the lines in a Cobra Mk III:

![A close-up of lines in BBC Micro Elite](https://elite.bbcelite.com/images/cassette/line-drawing.png) 

						Let's look at how the line-drawing algorithm works.

## The core algorithm

													 ------------------

						The basic idea is quite simple. Let's consider a line from (X1, Y1) to (X2, Y2), where that line slopes down and right at a reasonably shallow angle, like this:

```
  (X1, Y1) ''-..__
                  ''--..__
                          ''--..__
                                  ''--.._
                                          (X2, Y2)
```
						As we move along the line from (X1, Y1) to (X2, Y2), let's say that we move across by delta_x and down by delta_y, like this:

```
           <---------- delta_x --------->
  (X1, Y1) ''-..__                                    ^
                  ''--..__                            | delta_y
                          ''--..__                    |
                                  ''--.._             v
                                          (X2, Y2)
```
						So we have the following:

- As we move along the line by delta_x in the x-direction, we move down by delta_y in the y-direction.

If we divide each side of the triangle by delta_x, we also get the following:

- As we move along the line by 1 in the x-direction, we move down by (delta_y / delta_x) in the y-direction.

This is the core of the algorithm: if we step along the x-axis, 1 pixel at a time, then if we also move down by (delta_y / delta_x) in the y-direction and plot a point each time, we'll have our line. In pseudo-code, it looks like this:

```
  function line(x1, y1, x2, y2)
    delta_x = x2 - x1
    delta_y = y2 - y1
    y = y1
    for x from x1 to x2
      plot(x, y)
      y = y + (delta_y / delta_x)
```
						If our screen had an infinite resolution, then this would do nicely... but, of course, it doesn't, so we need to refine this idea. Internally we still do the same calculation for y, but when we come to plot the point with plot(x, y), we need to convert y into an integer. We could just convert y to the nearest integer each time, but working with floating point numbers is pretty slow, so the algorithm speeds things up by using the concept of a "slope error".

We're drawing a pixel line, so each time we step along the x-axis by 1 pixel, we have a choice of either staying where we are in the y-axis, or moving down one line (i.e. incrementing y by 1). We can't increase y by fractions, so instead, each time we step along the x-axis, we keep a running total of how far we would step down in the y-axis if we weren't constrained by only being able to move down by 1. In other words, we keep a tally of the (delta_y / delta_x)'s that we would ideally be adding to y, until we know we've moved onto the next line, at which point we add 1 to y. This tally is known as the "slope error", as it's a running tally of the current error between our pixels and the real slope of the line.

There's one final tweak, and that's starting our slope error tally at 0.5, which denotes the centre of the starting pixel. So the final algorithm looks like this:

```
  function line(x1, y1, x2, y2)
    delta_x = x2 - x1
    delta_y = y2 - y1
    slope_err = abs(delta_y / delta_x)
    error = 0.5
    y = y1
    for x from x1 to x2
      plot(x, y)
      error = error + slope_err
      if error >= 1.0 then
        y = y + 1
        error = error - 1.0
```
             ## Implementing the algorithm in 8-bit integers

            							 --------------------------------------------

						You may have noticed that the algorithm above still uses real numbers. When we actually use this approach in Elite, we multiply all the real numbers by 256, so that 256 is equivalent to 1.0. We can now initialise error to 128, and instead of checking whether error >= 1.0, we can check whether error is >= 256, like this:

```
  function line(x1, y1, x2, y2)
    delta_x = x2 - x1
    delta_y = y2 - y1
    slope_err = abs(delta_y / delta_x)
    error = 128
    y = y1
    for x = x1 to x2
      plot(x, y)
      error = error + slope_err
      if error >= 256 then
        y = y + 1
        error = error - 256
```
						There is one final improvement. If we use a single byte to store the error, then error >= 256 is the same as saying "has the addition just overflowed", in which case we don't need to subtract 256 as the byte will already have rolled around to 0. So here is the final algorithm used in Elite:

```
  function line(x1, y1, x2, y2)
    delta_x = x2 - x1
    delta_y = y2 - y1
    slope_err = abs(delta_y / delta_x)
    error = 128
    y = y1
    for x = x1 to x2
      plot(x, y)
      error = error + slope_err
      if C flag is set then
        y = y + 1
```
						This is the algorithm that's implemented in [part 4 of the LOIN routine](https://elite.bbcelite.com/cassette/main/subroutine/loin_part_4_of_7.html), for gently sloping lines that go right and down. It uses Q, S, X and Y as follows:

```
  Q = |delta_y| / |delta_x|
  S = 128
  Y = Y1
  for X = X1 to X2
    plot(X, Y)
    S = S + Q
    if C flag set then
      inc Y
```
						The full LOIN routine implements the same basic algorithm multiple times, tweaked to cater for all the other variations of sloping line (such as more vertical lines that slope sharply up and to the left, for example). But the same principles apply, just with different signs.

Also, it's worth noting that Elite doesn't plot the first pixel in any of its lines. This is to prevent corners from disappearing; if you imagine us drawing a triangle by drawing a line from point A to point B, then from B to C, and then from C to A again, then if we plotted all the end points, each of the triangle's vertices (A, B and C) would be plotted twice, once as the start of a line, and again as the end of the line. Normally this wouldn't be a problem, but because Elite draws everything on-screen using EOR logic (so objects can be drawn and then erased by simply drawing them again), this would mean the corner points would disappear, and that would look very strange. So there is logic in the LOIN routine to omit the first pixel from each line, and there's similar logic in the HLOIN routine, which omits the rightmost pixel from horizontal lines for the same reason.

Note that the original versions of Elite contain a bug where the last pixel is skipped instead of the first pixel, but only when drawing lines that go right and up or left and down. This leads to a messy line join between this kind of line and lines with different slopes. This bug was fixed in the advanced versions, and can be seen in [part 3 of LOIN](https://elite.bbcelite.com/cassette/main/subroutine/loin_part_3_of_7.html).

## Summary of the routine

													 ----------------------

						To help with understanding the 7 parts of the line-drawing routine, here's a summary of what each part does.

```
  1. Calculate delta_x, delta_y
     Choose either parts 2-4 or parts 5-7
```
						If the line is closer to being horizontal than vertical, we step right along the x-axis:

```
  2. Potentially swap coordinates so X1 < X2
     Set up screen address variables
     Calculate |delta_y| / |delta_x|
     Choose either part 3 or part 4
```
```
  3. The line is going right and up (no swap) or left and down (swap)
     X1 < X2 and Y1 > Y2
     Draw from (X1, Y1) at bottom left to (X2, Y2) at top right
     If we swapped, don't plot (X1, Y1)
```
```
  4. The line is going right and down (no swap) or left and up (swap)
     X1 < X2 and Y1 <= Y2
     Draw from (X1, Y1) at top left to (X2, Y2) at bottom right
     If we didn't swap, skip plotting (X1, Y1)
```
						If the line is closer to being vertical than horizontal, we step up along the y-axis:

```
  5. Potentially swap coordinates so Y1 >= Y2
     Set up screen address variable
     Calculate |delta_x| / |delta_y|
     Choose either part 6 or part 7
```
```
  6. The line is going up and left (no swap) or down and right (swap)
     X1 < X2 and Y1 >= Y2
     Draw from (X1, Y1) at bottom right to (X2, Y2) at top left
     If we didn't swap, skip plotting (X1, Y1)
```
```
  7. The line is going up and right (no swap) or down and left (swap)
     X1 >= X2 and Y1 >= Y2
     Draw from (X1, Y1) at bottom left to (X2, Y2) at top right
     If we didn't swap, skip plotting (X1, Y1)
```
					Note that in the cassette and disc versions, the second part of the second test in step 3 is actually coded as Y1-1 > Y2 (and the corresponding test in step 4 as Y1-1 <= Y2). This was corrected to Y1 > Y2 and Y1 <= Y2 in the 6502 Second Processor version, so that's the version I've included above.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
(X1, Y1) ''-..__
                  ''--..__
                          ''--..__
                                  ''--.._
                                          (X2, Y2)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
<---------- delta_x --------->

  (X1, Y1) ''-..__                                    ^
                  ''--..__                            | delta_y
                          ''--..__                    |
                                  ''--.._             v
                                          (X2, Y2)
```

### Snippet Codice (BASIC)

```basic
function line(x1, y1, x2, y2)
    delta_x = x2 - x1
    delta_y = y2 - y1
    y = y1
    for x from x1 to x2
      plot(x, y)
      y = y + (delta_y / delta_x)
```

### Snippet Codice (BASIC)

```basic
function line(x1, y1, x2, y2)
    delta_x = x2 - x1
    delta_y = y2 - y1
    slope_err = abs(delta_y / delta_x)
    error = 0.5
    y = y1
    for x from x1 to x2
      plot(x, y)
      error = error + slope_err
      if error >= 1.0 then
        y = y + 1
        error = error - 1.0
```

### Snippet Codice (BASIC)

```basic
function line(x1, y1, x2, y2)
    delta_x = x2 - x1
    delta_y = y2 - y1
    slope_err = abs(delta_y / delta_x)
    error = 128
    y = y1
    for x = x1 to x2
      plot(x, y)
      error = error + slope_err
      if error >= 256 then
        y = y + 1
        error = error - 256
```

### Snippet Codice (BASIC)

```basic
function line(x1, y1, x2, y2)
    delta_x = x2 - x1
    delta_y = y2 - y1
    slope_err = abs(delta_y / delta_x)
    error = 128
    y = y1
    for x = x1 to x2
      plot(x, y)
      error = error + slope_err
      if C flag is set then
        y = y + 1
```

### Snippet Codice (BASIC)

```basic
Q = |delta_y| / |delta_x|
  S = 128
  Y = Y1
  for X = X1 to X2
    plot(X, Y)
    S = S + Q
    if C flag set then
      inc Y
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
1. Calculate delta_x, delta_y
     Choose either parts 2-4 or parts 5-7
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
2. Potentially swap coordinates so X1 < X2
     Set up screen address variables
     Calculate |delta_y| / |delta_x|
     Choose either part 3 or part 4
```

### Snippet Codice (BASIC)

```basic
3. The line is going right and up (no swap) or left and down (swap)
     X1 < X2 and Y1 > Y2
     Draw from (X1, Y1) at bottom left to (X2, Y2) at top right
     If we swapped, don't plot (X1, Y1)
```

### Snippet Codice (BASIC)

```basic
4. The line is going right and down (no swap) or left and up (swap)
     X1 < X2 and Y1 <= Y2
     Draw from (X1, Y1) at top left to (X2, Y2) at bottom right
     If we didn't swap, skip plotting (X1, Y1)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
5. Potentially swap coordinates so Y1 >= Y2
     Set up screen address variable
     Calculate |delta_x| / |delta_y|
     Choose either part 6 or part 7
```

### Snippet Codice (BASIC)

```basic
6. The line is going up and left (no swap) or down and right (swap)
     X1 < X2 and Y1 >= Y2
     Draw from (X1, Y1) at bottom right to (X2, Y2) at top left
     If we didn't swap, skip plotting (X1, Y1)
```

### Snippet Codice (BASIC)

```basic
7. The line is going up and right (no swap) or down and left (swap)
     X1 >= X2 and Y1 >= Y2
     Draw from (X1, Y1) at bottom left to (X2, Y2) at top right
     If we didn't swap, skip plotting (X1, Y1)
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/elites_line-drawing_algorithm.html](https://elite.bbcelite.com/deep_dives/elites_line-drawing_algorithm.html)*

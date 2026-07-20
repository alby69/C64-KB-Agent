---
title: Drawing circles
source_url: https://elite.bbcelite.com/deep_dives/drawing_circles.html
category: deep-dive
topics:
- basic
- assembly
difficulty: intermediate
language: mixed
hardware:
- KERNAL
- SID
related:
- sid-registers
- sound-programming
- memory-map
- kernal-routines
- music-player
scraped_at: '2026-07-20'
---

# Drawing circles

## The routines that draw planets and the hyperspace and docking tunnels

You never forget your first journey in Elite, and a lot of that is down to the circle routine. The launch tunnel rushing past as you punch your way out of the station - that's the circle routine:

![The launch tunnel in the BBC Micro cassette version of Elite](https://elite.bbcelite.com/images/cassette/launch.png) 

						The planet Lave, hanging in space in front of you in all its rotating glory - that's the circle routine:

![The launch view of Lave in the BBC Micro cassette version of Elitee](https://elite.bbcelite.com/images/ellipses/lave.png) 

						The nearby systems you can choose to visit on the Short-range Chart are all those inside a circle drawn by the circle routine:

![The Short-range Chart in the BBC Micro cassette version of Elite](https://elite.bbcelite.com/images/cassette/short-range_chart.png) 

						And the hyperspace tunnel? You guessed it. It's the circle routine again:

![The hyperspace tunnel in the BBC Micro cassette version of Elite](https://elite.bbcelite.com/images/cassette/hyperspace.png) 

						Let's take a look at how all these circles are drawn.

## The circle-drawing routines

													 ---------------------------

						Circles are drawn by the following routines: [CIRCLE](https://elite.bbcelite.com/cassette/main/subroutine/circle.html) (for planets), [TT128](https://elite.bbcelite.com/cassette/main/subroutine/tt128.html) (for charts) and [CIRCLE2](https://elite.bbcelite.com/cassette/main/subroutine/circle2.html) (which does the actual drawing). This latter routine draws a circle by starting at the bottom of the circle - or at 6 o'clock if you think of it as a clock face - and moving anti-clockwise in steps defined by the size of the step size in STP. The whole circle is divided into 64 steps and the step number is stored in CNT, so if STP were 2, CNT would be 0, 2, 4 and so on up to and including 64. So we work our way around the circle like this:

| CNT | Quadrant | Clock | 
|---|---|---|
| 0 to 16 | Bottom-right quadrant | 6 o'clock to 3 o'clock | 
| 16 to 32 | Top-right quadrant | 3 o'clock to 12 o'clock | 
| 32 to 48 | Top-left quadrant | 12 o'clock to 9 o'clock | 
| 48 to 64 | Bottom-left quadrant | 9 o'clock to 6 o'clock | 

If we can work out the coordinates of the point on the circle at step CNT, then we can draw the circle by simply drawing lines between each point, with each line being a segment of the circle. We can draw smooth circles by having smaller segments, as with the circles on the charts, or we can draw more polygonal circles by having large segments, as with the launch tunnel. The circle's "step size" determines how many of the 64 points make up each segment, so smaller step sizes give smoother circles (the step size is typically 2, 4 or 8 points).

So let's consider the step where CNT is around 5, say, so that's around 5 o'clock. The sine table at SNE contains 32 values that cover half a circle, so we can think of CNT as the angle that we have travelled through as we work our way round the circle, with 64 covering the whole thing. So 5 o'clock looks like this (I've put a "c" for the angle CNT as it's a bit of a tight squeeze):

```
        _ - _
     =         =                     |`.                          |`.
   =             =                   |c `.                        |c `.  K
  =               =                  |    `. K         K * cos(c) |    `.
  =       |`.     =        __-->     |      `.                    |      `.
   =      |  `.  =  ___.--´          |        `.                  +--------`
    =     |    `.                    |     __--´    ----->        K * sin(c)
     `--__|__--´                     |__--´
```
						So if the centre of the circle (the top of the triangle above) is at the origin (0, 0), then using basic trigonometry, we can see that at step number CNT, the point on the circle is at these coordinates:

x = K * sin(CNT) y = K * cos(CNT)

The SNE table only gives us positive results, so for other quadrants of the circle, we'll need to set the signs of x and y according to the particular quadrant we're in, but the magnitude of the coordinates will be as above. Specifically, we need to do the following (as screen y-coordinates are positive down the screen and screen x-coordinates are positive to the right):

| CNT | Quadrant | Polarity | 
|---|---|---|
| 0 to 16 | Bottom-right quadrant | So x is +ve and y is +ve | 
| 16 to 32 | Top-right quadrant | So x is +ve and y is -ve | 
| 32 to 48 | Top-left quadrant | So x is -ve and y is -ve | 
| 48 to 64 | Bottom-left quadrant | So x is -ve and y is +ve | 

To get the final screen coordinates of the point at count CNT, we have to add the results from above to the coordinates of the centre of the circle, as the origin of the screen is at the top-left, not in the centre of the circle. We do this with the following:

x = K * sin(CNT) + K3(1 0) y = K * cos(CNT) + K4(1 0)

Perhaps surprisingly, the circle routine does not use any lines of symmetry to reduce the number of points calculated in the circle. Instead, speed comes from the use of the pre-calculated sine and cosine lookup tables - see the deep dive on [the sine, cosine and arctan tables](https://elite.bbcelite.com/the_sine_cosine_and_arctan_tables.html) for details.

And that's how we draw the planet and chart circles in a step-wise fashion using the sine table.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
_ - _
     =         =                     |`.                          |`.
   =             =                   |c `.                        |c `.  K
  =               =                  |    `. K         K * cos(c) |    `.
  =       |`.     =        __-->     |      `.                    |      `.
   =      |  `.  =  ___.--´          |        `.                  +--------`
    =     |    `.                    |     __--´    ----->        K * sin(c)
     `--__|__--´                     |__--´
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
x = K * sin(CNT)

  y = K * cos(CNT)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
x = K * sin(CNT) + K3(1 0)

  y = K * cos(CNT) + K4(1 0)
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/drawing_circles.html](https://elite.bbcelite.com/deep_dives/drawing_circles.html)*

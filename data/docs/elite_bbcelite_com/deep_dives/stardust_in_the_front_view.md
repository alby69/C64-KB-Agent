---
title: Stardust in the front view
source_url: https://elite.bbcelite.com/deep_dives/stardust_in_the_front_view.html
category: deep-dive
topics:
- sprite programming
- assembly
- input handling
difficulty: beginner
language: mixed
hardware:
- CPU
- KERNAL
- CIA
- VIC-II
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

# Stardust in the front view

## The algorithms behind the stardust particles in the front view

The small particles of dust out there in space - which I've called "stardust" in this commentary, though I'm not sure what the official term is - is an essential way of making us feel like we are flying through space in our Cobra. Pulling back on the joystick and watching the stardust fly down and backwards is still a seriously immersive feeling. You really feel like those particles are slamming into your windshield as you shoot through space and into the ether.

Here's a video showing the stardust in action:

The [STARS1](https://elite.bbcelite.com/cassette/main/subroutine/stars1.html) routine looks after stardust in the front view. It is responsible for moving the stardust towards us according to our speed (so the dust rushes past us), and applying our current pitch and roll to each particle of dust, so the stardust moves correctly when we steer our ship. This approach is used in all the 6502 versions of Elite, even the NES version; the latter uses sprites to display the stardust particles, but the underlying calculations are the same.

The STARS6 routine processes stardust in the rear view, and is essentially the reverse of STARS1. Let's take a look at how STARS1 works.

## Processing stardust

													 -------------------

						The process in STARS1 breaks down into three stages:

- Moving the stardust towards us
- Applying roll to the stardust
- Applying pitch to the stardust

Let's look at these three stages in more detail. Throughout the calculations below, we disregard the low bytes from the angle calculations, just like in part 5 of MVEIT.

Note that each particle of stardust has its own (x, y, z) coordinate. Stardust coordinates are not true 3D space coordinates - when stardust is drawn, the z value is purely used to determine the size of the stardust dot that is displayed, and that's it. The dot is drawn at screen coordinate (x, y), so when thinking about stardust, we're really thinking about a 2D plane, with the z-coordinate only being used when moving the stardust towards us, and when determining how it should look.

Each of the coordinates is stored as 16-bit sign-magnitude value, as in (x_hi x_lo) and (y_hi y_lo). The coordinates for the Y-th particle of stardust are stored in (SX+Y SXL+Y), (SY+Y SYL+Y) and (SZ+Y SZL+Y) respectively. The origin for stardust particles is the centre of the screen, at the crosshairs.

## Moving the stardust towards us

													 ------------------------------

						The following calculations move the stardust away from the centre of the screen by a distance proportionate to our speed, so dust that is further away from us (i.e. with a high value of z) moves by a smaller amount to create a sense of perspective.

These are the calculations:

1. q = 64 * speed / z_hi 2. z = z - speed * 64 3. y = y + |y_hi| * q 4. x = x + |x_hi| * q

We move the particle towards us by reducing the z-coordinate by the current speed - that's the easy part. We then calculate a factor q that determines how far we should move the stardust particle away from the centre point, and apply that factor by multiplying the x and y screen coordinates by (1 + q), which has the effect of making particles near the centre (small x and y) move less than particles near the edges (high x and y).

Essentially, this is using the fact that when we project 3D (x, y, z) coordinates onto a 2D screen, the calculation is essentially:

x_screen = x / z y_screen = y / z

so if we reduce z (i.e. move the particle near to us) then the x and y screen coordinates should increase by an inverse but proportional amount.

## Applying roll to the stardust

													 -----------------------------

						The following calculations apply the current roll angle alpha to the stardust:

5. y = y + alpha * x / 256 6. x = x - alpha * y / 256

These are essentially the same as the roll equations from MVS4, which work in the same way when projected onto the 2D screen, as we can ignore the z axis when rolling.

## Applying pitch to the stardust

													 ------------------------------

						The following calculations apply the current pitch angle beta to the stardust:

7. x = x + 2 * (beta * y / 256) ^ 2 8. y = y - beta * 256

The second one is essentially the same as the pitch equation from MVS4, just applied to the y-coordinate projected into 2D (i.e. divided by z).

The first one, though, is still a bit of a mystery. Removing this part of the calculation doesn't seem to affect the look of the stardust field, and with the maximum magnitude of beta being 8, and y always being less than 120, the maximum delta applied to x is:

```
  2 * (beta * y / 256) ^ 2 = 2 * (8 * y / 256) ^ 2
                           = 2 * 64 * y^2 / 65536
                           = y^2 / 512
                           = 28
```
out of 256 pixels across the screen, and that's at the extremities of the screen and with full pitch. Perhaps this is a fisheye effect that makes space feel more curved when pitching is high? For now, I don't have an answer...

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
1. q = 64 * speed / z_hi
  2. z = z - speed * 64
  3. y = y + |y_hi| * q
  4. x = x + |x_hi| * q
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
x_screen = x / z
  y_screen = y / z
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
5. y = y + alpha * x / 256
  6. x = x - alpha * y / 256
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
7. x = x + 2 * (beta * y / 256) ^ 2
  8. y = y - beta * 256
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
2 * (beta * y / 256) ^ 2 = 2 * (8 * y / 256) ^ 2
                           = 2 * 64 * y^2 / 65536
                           = y^2 / 512
                           = 28
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/stardust_in_the_front_view.html](https://elite.bbcelite.com/deep_dives/stardust_in_the_front_view.html)*

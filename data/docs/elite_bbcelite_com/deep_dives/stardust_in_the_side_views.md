---
title: Stardust in the side views
source_url: https://elite.bbcelite.com/deep_dives/stardust_in_the_side_views.html
category: deep-dive
topics:
- sprite programming
- assembly
- input handling
difficulty: intermediate
language: assembly
hardware:
- VIC-II
- CIA
- SID
- CPU
- KERNAL
related:
- cia-registers
- keyboard-handling
- sound-programming
- music-player
- raster-interrupts
- joystick-reading
- memory-map
- sprite-programming
- vic-ii-registers
- kernal-routines
- sid-registers
scraped_at: '2026-07-14'
---

# Stardust in the side views

## The algorithms behind the stardust particles in the side views

The small particles of dust out there in space - which I've called "stardust" in this commentary, though I'm not sure what the official term is - is an essential way of making us feel like we are flying through space in our Cobra. Pulling back on the joystick and watching the stardust fly down and backwards is still a seriously immersive feeling. You really feel like those particles are slamming into your windshield as you shoot through space and into the ether.

Here's a video showing the stardust in action:

The [STARS2](https://elite.bbcelite.com/cassette/main/subroutine/stars2.html) routine moves the stardust sideways according to our speed and which side we are looking out of, and applies our current pitch and roll to each particle of dust, so the stardust moves correctly when we steer our ship. This approach is used in all the 6502 versions of Elite, even the NES version; the latter uses sprites to display the stardust particles, but the underlying calculations are the same.

Let's look at this process in more detail. It breaks down into three stages:

- Moving the stardust sideways
- Applying pitch to the stardust (rotating around the mid-point)
- Applying roll to the stardust (up and down)

## Moving the stardust sideways

													 ----------------------------

						First, we want to move the stardust sideways, in the correct direction for the current view. The further away the stardust particle (i.e. with a higher value of z) the slower it should move, to give a sense of perspective.

These are the calculations:

1. delta_x = 8 * 256 * speed / z_hi 2. x = x + delta_x

We sign the delta_x value as negative for the left view, where particles go from right to left, and positive for the right view, where particles go from left to right, and then we add the delta to the x-coordinate to move the stardust particle past our side window as we speed along.

## Applying pitch to the stardust (rotating)

													 -----------------------------------------

						The following calculations apply the current pitch angle beta to the stardust:

3. x = x + beta * y 4. y = y - beta * x

These are essentially the same as the roll equations from MVS4, just using the pitch angle beta, because when we are looking out of the side views, when the ship pitches, the side views rotate around the middle, just like the front view does when we roll.

## Applying roll to the stardust (up/down)

													 ---------------------------------------

						The following calculations apply the current roll angle alpha to the stardust:

5. x = x - alpha * x * y 6. y = y + alpha * y * y + alpha

The significant part here is adding alpha to y (or, more specifically, ALPHA * 256). This means that as we roll the ship and alpha increases, the stardust out of the side view goes up and down, which is pretty intuitive.

The other part is currently a bit of a mystery, along with the pitch calculations in STARS1. More analysis needed here...

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
1. delta_x = 8 * 256 * speed / z_hi
  2. x = x + delta_x
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
3. x = x + beta * y
  4. y = y - beta * x
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
5. x = x - alpha * x * y
  6. y = y + alpha * y * y + alpha
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/stardust_in_the_side_views.html](https://elite.bbcelite.com/deep_dives/stardust_in_the_side_views.html)*

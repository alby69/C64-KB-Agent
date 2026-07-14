---
title: In the crosshairs
source_url: https://elite.bbcelite.com/deep_dives/in_the_crosshairs.html
category: deep-dive
topics:
- assembly
difficulty: intermediate
language: assembly
hardware:
- CPU
- KERNAL
related:
- memory-map
- kernal-routines
scraped_at: '2026-07-14'
---

# In the crosshairs

## How the game knows whether an enemy is being hit by our laser fire

During combat, one of the most important calculations we need to perform is whether we have another ship in our sights. We need to calculate this when we're trying to hit another ship with our lasers, and when we're trying to get the enemy in our sights so we can lock a missile onto the target.

![Firing at a ship in 6502 Second Processor Elite](https://elite.bbcelite.com/images/6502sp/crosshairs.png) 

						In both cases, we use the [HITCH](https://elite.bbcelite.com/cassette/main/subroutine/hitch.html) routine to work out just how close to the crosshairs that ship really is. Let's take a look at how the HITCH routine works.

There are a number of steps we have to take to work out whether a ship is in our crosshairs. They are as follows.

- Make sure the ship is in front of us (z_sign is positive)
- Make sure this isn't the planet or sun (bit 7 of the ship type is clear)
- Make sure the ship isn't exploding (bit 5 of byte #31 is clear)
- Make sure the ship is close enough to be targeted or hit (both x_hi and y_hi are 0)
- Test whether our crosshairs are within the targetable area for this ship

This last one needs further explanation. Each ship type has, as part of its blueprint, a 16-bit value that defines the area of the ship that can be locked onto by a missile or hit by laser fire. The bigger this value, the easier the ship is to hit.

The key to the calculation is the observation that the ship's x- and y-coordinates give the horizontal and vertical distances between our line of fire and the ship. This is because the z-axis points out of the nose of our ship, and is therefore the same as our line of fire, so the other two axes give the deviation of the other ship's position from this line.

We've already confirmed in the checks above that x_hi and y_hi are both zero, so we calculate this:

(S R) = x_lo^2 + y_lo^2

which, using Pythagoras, is the same as the square of the distance from our crosshairs to the ship.

If this calculation doesn't fit into the 16 bits of (S R) then we know we can't be aiming at the ship, but if it does, we compare (S R) with the 16-bit targetable area from the ship's blueprint, and if (S R) is less than the targetable area, the ship is determined to be in our crosshairs and can be hit or targeted.

So the targetable area is the square of the distance that the ship can be from the centre of our crosshairs but still be locked onto by our missiles or hit by our lasers.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
(S R) = x_lo^2 + y_lo^2
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/in_the_crosshairs.html](https://elite.bbcelite.com/deep_dives/in_the_crosshairs.html)*

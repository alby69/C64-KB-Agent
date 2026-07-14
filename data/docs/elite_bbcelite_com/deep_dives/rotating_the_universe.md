---
title: Rotating the universe
source_url: https://elite.bbcelite.com/deep_dives/rotating_the_universe.html
category: deep-dive
topics:
- assembly
- input handling
difficulty: intermediate
language: assembly
hardware:
- CPU
- KERNAL
- CIA
related:
- keyboard-handling
- joystick-reading
- memory-map
- kernal-routines
- cia-registers
scraped_at: '2026-07-14'
---

# Rotating the universe

## What happens to the rest of the universe when we rotate our ship?

When we rotate our ship with the keyboard or joystick, it turns out that it's a lot easier to rotate the whole universe around our Cobra, rather than rotating our ship and ending up having to include our orientation into every other calculation. Because there is no up or down in space, rotating the whole universe has the same effect, as everything is drawn from the perspective of our cockpit.

In other words, if we pitch or roll when fighting Thargoids near the sun, then the game will actually rotate the Thargoid mothership, the two Thargons, the sun and the off-screen planet, rather than rotating our own ship:

![Thargoids and Thargons in the 6502 Second Processor version of Elite](https://elite.bbcelite.com/images/6502sp/thargoids.png) 

						[Part 5 of the MVEIT routine](https://elite.bbcelite.com/cassette/main/subroutine/mveit_part_5_of_9.html) is responsible for performing this act of seeming omnipotence, and it does this by rotating the (x, y, z) coordinate of the ship we are processing, by the pitch and roll angles alpha (roll) and beta (pitch), so the ship moves as we pitch and roll.

It does this using the exact same rotation equations that MVS4 uses in part 7 to rotate the ship's orientation vectors (see the deep dive on [pitching and rolling](https://elite.bbcelite.com/pitching_and_rolling.html) for details of the maths behind the following). But just as with part 7, there is a twist, and yet again, the twist is all about Minsky.

The twist is that, this time, the pitch and roll calculations are done in a mixed-up order. In MVS4, we do the roll calculations first:

y = y - alpha * x x = x + alpha * y

and then we do the pitch calculations:

y = y - beta * z z = z + beta * y

and because we use the updated y in the x and z calculations, we get to enjoy a more accurate result because of the Minsky effect, like this:

x -> x + alpha * (y - alpha * x) y -> y - alpha * x - beta * z z -> z + beta * (y - alpha * x - beta * z)

The calculation used here is very similar, but we switch the order of the x and z calculations, by doing these two first:

y = y - alpha * x z = z + beta * y

and then these two:

y = y - beta * z x = x + alpha * y

The result is this really complex set of transformations:

x -> x + alpha * (y - alpha * x - beta * (z + beta * (y - alpha * x))) y -> y - alpha * x - beta * (z + beta * (y - alpha * x)) z -> z + beta * (y - alpha * x)

This is a pretty hard-to-follow variation on the classic Minsky equations implemented in MVS4, but it still encapsulates the essence of the Minsky approach, which is to use the updated values when calculating. It's just that this time we use the updated values of both y and z in the calculation, and that leads to a different result.

We implement this variation in the [MV40](https://elite.bbcelite.com/cassette/main/subroutine/mv40.html) routine, using K2 to store the updated value of Y as we progress through the above stages:

1. K2 = y - alpha * x 2. z = z + beta * K2 3. y = K2 - beta * z 4. x = x + alpha * y

We also discard the low bytes from the angle multiplications, so all of the above multiplications get divided by 256. This effectively converts the values of alpha and beta from their stored value ranges of 0 to 31 and 0 to 8 in ALP1 and BET1 into the ranges 0 to 0.125 and 0 to 0.03125. These figures work well as small angles in radians, which is why we can apply the small angle approximation to them above.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
y = y - alpha * x
  x = x + alpha * y
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
y = y - beta * z
  z = z + beta * y
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
x -> x + alpha * (y - alpha * x)
  y -> y - alpha * x - beta * z
  z -> z + beta * (y - alpha * x - beta * z)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
y = y - alpha * x
  z = z + beta * y
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
y = y - beta * z
  x = x + alpha * y
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
x -> x + alpha * (y - alpha * x - beta * (z + beta * (y - alpha * x)))
  y -> y - alpha * x - beta * (z + beta * (y - alpha * x))
  z -> z + beta * (y - alpha * x)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
1. K2 = y - alpha * x
  2. z = z + beta * K2
  3. y = K2 - beta * z
  4. x = x + alpha * y
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/rotating_the_universe.html](https://elite.bbcelite.com/deep_dives/rotating_the_universe.html)*

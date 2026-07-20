---
title: Extended screen coordinates
source_url: https://elite.bbcelite.com/deep_dives/extended_screen_coordinates.html
category: deep-dive
topics:
- basic
- assembly
difficulty: beginner
language: mixed
hardware:
- KERNAL
- SID
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

# Extended screen coordinates

## The extended 16-bit screen coordinate system behind the space view

When simulating its universe of ships, stars and space stations, Elite uses large numbers - space is big, after all. The ship coordinates are stored as sign-magnitude numbers with 16 bits for the magnitudes, while the planet and sun coordinates go all the way up to 23-bit magnitudes (as they can be a lot further away from us than ships and stations).

To maintain accuracy when projecting these shapes onto the screen, Elite uses 16-bit screen coordinates for the calculations. The screen itself is only 256 pixels across, which fits into 8 bits, so this means during the projection, ships often project onto coordinates that are off-screen. For example, the planet below extends beyond the screen boundary, to the right of the screen and past the bottom of the dashboard, and the whole planet is stored in memory, even if it isn't shown on-screen:

![A clipped planet BBC Micro Elite](https://elite.bbcelite.com/images/cassette/clipping.png) 

						This is intentional, and happens all the time when you're speeding past enemy ships or slamming into the walls of a space station. Hammering the keyboard with a sudden pitch-and-roll manoeuvre brings ships into view that were otherwise minding their own business in the depths of space, but even though we couldn't see them, they were there all along.

The extended screen coordinate system is a key part of the simulation. The [PROJ](https://elite.bbcelite.com/cassette/main/subroutine/proj.html) routine that projects space coordinates onto the screen produces 16-bit coordinates as a result of the projection, which then get clipped by the [LL145](https://elite.bbcelite.com/cassette/main/subroutine/ll145_part_1_of_4.html) routine, but the way these 16-bit coordinates relate to the screen is delightfully simple. Let's take a look.

## A wall of screens

													 -----------------

						First, let's consider a 256x256 screen (the space view in Elite is actually 256 pixels wide and 192 pixels high, but we'll come to that in a moment). The screen (x, y) coordinates would look like this, when expressed in hexadecimal:

```
                        (&00, &00)      (&FF, &00)
                               +----------+
                               |          |
                               |          |
                               |          |
                               +----------+
                        (&00, &FF)      (&FF, &FF)
```
						These coordinates are 8-bit values, as the screen is only 256 pixels wide. In the extended coordinate system, there's an additional high byte. Let's set that high byte for our screen to 0, so in terms of 16-bit coordinates, we have the following coordinates:

```
                     (&0000, &0000)    (&00FF, &0000)
                               +----------+
                               |          |
                               |          |
                               |          |
                               +----------+
                     (&0000, &00FF)    (&00FF, &00FF)
```
						Let's describe this screen, where the high byte of the x- and y-coordinates is &00, like this:

```
                               +----------+
                               |          |
                               | &00, &00 |
                               |          |
                               +----------+
```
						Now let's tack another 256x256 screen onto the right of this one. The screen x-coordinates of this new screen would have a high byte of 1 instead of 0, like this:

```
                     (&0100, &0000)    (&01FF, &0000)
                               +----------+
                               |          |
                               |          |
                               |          |
                               +----------+
                     (&0100, &00FF)    (&01FF, &00FF)
```
						which we can also write like this:

```
                               +----------+
                               |          |
                               | &01, &00 |
                               |          |
                               +----------+
```
						Putting the neighbours side by side, we get this:

```
                         +----------+----------+
                         |          |          |
                         | &00, &00 | &01, &00 |
                         |          |          |
                         +----------+----------+
```
						We can also bolt another screen onto the bottom, like this:

```
                         +----------+----------+
                         |          |          |
                         | &00, &00 | &01, &00 |
                         |          |          |
                         +----------+----------+
                         |          |
                         | &00, &01 |
                         |          |
                         +----------+
```
						and, if we consider the extended screen coordinates to be signed 16-bit values using two's complement, we can extend the screens in all directions, like this:

```
  +----------+     +----------+----------+----------+     +----------+
  |          |     |          |          |          |     |          |
  | &80, &80 | ... | &FF, &80 | &00, &80 | &01, &80 | ... | &7F, &80 |
  |          |     |          |          |          |     |          |
  +----------+     +----------+----------+----------+     +----------+
       :                :          :          :                :
       :                :          :          :                :
       :                :          :          :                :
  +----------+     +----------+----------+----------+     +----------+
  |          |     |          |          |          |     |          |
  | &80, &FF | ... | &FF, &FF | &00, &FF | &01, &FF | ... | &7F, &FF |
  |          |     |          |          |          |     |          |
  +----------+     +----------+----------+----------+     +----------+
  |          |     |          |          |          |     |          |
  | &80, &00 | ... | &FF, &00 | &00, &00 | &01, &00 | ... | &7F, &00 |
  |          |     |          |          |          |     |          |
  +----------+     +----------+----------+----------+     +----------+
  |          |     |          |          |          |     |          |
  | &80, &01 | ... | &FF, &01 | &00, &01 | &01, &01 | ... | &7F, &01 |
  |          |     |          |          |          |     |          |
  +----------+     +----------+----------+----------+     +----------+
       :                :          :          :                :
       :                :          :          :                :
       :                :          :          :                :
  +----------+     +----------+----------+----------+     +----------+
  |          |     |          |          |          |     |          |
  | &80, &7F | ... | &FF, &7F | &00, &7F | &01, &7F | ... | &7F, &7F |
  |          |     |          |          |          |     |          |
  +----------+     +----------+----------+----------+     +----------+
```
						This is the extended coordinate system used in Elite. You can think of it as a bank of individual screens, where the entire view is projected onto all the screens, but the game just shows the screen in the middle to the player. The extended coordinates cover a 256x256 mesh of individual 256x256 screens, which is easily enough space to project 3D space coordinates onto the screen in the middle.

## Checking whether a coordinate is on-screen

													 ------------------------------------------

						The clever part about all this is how quickly we can check whether a screen coordinate is visible in the space view, and how easy it is to get the actual screen coordinate we need for drawing. Given an extended screen coordinate, this is how we check whether it's on-screen:

- The first check is on the high byte. If either of the x- or y-coordinate's high bytes is non-zero, then the coordinate isn't in the &00, &00 screen in the above diagram, so it is definitely off-screen. If they are both zero, we move on to the next check.
- If both high bytes are zero, then the second check is to make sure the coordinate is in the space view rather than the dashboard. This is a simple check whether the low byte of the y-coordinate is less than 192, as the space view is made up of the top 192 pixel rows. If it is less than 192, the coordinate is indeed in the space view, otherwise it's hidden by the dashboard.
- If the coordinate is in the space view, then we can simply take the low bytes to get the screen coordinate for drawing.

In this way Elite effectively projects its universe onto a huge, cinematic bank of screens, and then works out which parts of the projection appear in the space view using three quick comparisons against 0 and 192. It's elegant and fast, as so much of this game's code is.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
(&00, &00)      (&FF, &00)
                               +----------+
                               |          |
                               |          |
                               |          |
                               +----------+
                        (&00, &FF)      (&FF, &FF)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
(&0000, &0000)    (&00FF, &0000)
                               +----------+
                               |          |
                               |          |
                               |          |
                               +----------+
                     (&0000, &00FF)    (&00FF, &00FF)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
+----------+
                               |          |
                               | &00, &00 |
                               |          |
                               +----------+
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
(&0100, &0000)    (&01FF, &0000)
                               +----------+
                               |          |
                               |          |
                               |          |
                               +----------+
                     (&0100, &00FF)    (&01FF, &00FF)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
+----------+
                               |          |
                               | &01, &00 |
                               |          |
                               +----------+
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
+----------+----------+
                         |          |          |
                         | &00, &00 | &01, &00 |
                         |          |          |
                         +----------+----------+
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
+----------+----------+
                         |          |          |
                         | &00, &00 | &01, &00 |
                         |          |          |
                         +----------+----------+
                         |          |
                         | &00, &01 |
                         |          |
                         +----------+
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
+----------+     +----------+----------+----------+     +----------+
  |          |     |          |          |          |     |          |
  | &80, &80 | ... | &FF, &80 | &00, &80 | &01, &80 | ... | &7F, &80 |
  |          |     |          |          |          |     |          |
  +----------+     +----------+----------+----------+     +----------+
       :                :          :          :                :
       :                :          :          :                :
       :                :          :          :                :
  +----------+     +----------+----------+----------+     +----------+
  |          |     |          |          |          |     |          |
  | &80, &FF | ... | &FF, &FF | &00, &FF | &01, &FF | ... | &7F, &FF |
  |          |     |          |          |          |     |          |
  +----------+     +----------+----------+----------+     +----------+
  |          |     |          |          |          |     |          |
  | &80, &00 | ... | &FF, &00 | &00, &00 | &01, &00 | ... | &7F, &00 |
  |          |     |          |          |          |     |          |
  +----------+     +----------+----------+----------+     +----------+
  |          |     |          |          |          |     |          |
  | &80, &01 | ... | &FF, &01 | &00, &01 | &01, &01 | ... | &7F, &01 |
  |          |     |          |          |          |     |          |
  +----------+     +----------+----------+----------+     +----------+
       :                :          :          :                :
       :                :          :          :                :
       :                :          :          :                :
  +----------+     +----------+----------+----------+     +----------+
  |          |     |          |          |          |     |          |
  | &80, &7F | ... | &FF, &7F | &00, &7F | &01, &7F | ... | &7F, &7F |
  |          |     |          |          |          |     |          |
  +----------+     +----------+----------+----------+     +----------+
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/extended_screen_coordinates.html](https://elite.bbcelite.com/deep_dives/extended_screen_coordinates.html)*

---
title: Pitching and rolling by a fixed angle
source_url: https://elite.bbcelite.com/deep_dives/pitching_and_rolling_by_a_fixed_angle.html
category: deep-dive
topics:
- assembly
difficulty: beginner
language: assembly
hardware:
- SID
related:
- music-player
- sound-programming
- sid-registers
scraped_at: '2026-07-14'
---

# Pitching and rolling by a fixed angle

## How other ships manage to pitch and roll in space

We can pitch and roll our ship by varying amounts, as shown by the dashboard's DC and RL indicators, but enemy ships don't have such a luxury - it turns out they can only orientate themselves at a fixed speed. Specifically, they can only pitch or roll by a fixed amount each iteration of the main loop - by an angle of 1/16 radians, or 3.6 degrees.

For example, here's a video showing the space station rotating around its central axis, which is achieved by rotating the station by a small, fixed amount on each iteration of the main loop:

This fixed rotation speed makes life simpler for the game code, not only because the angle is small enough to apply the small angle approximation, but also because 1/16 is a power of 2. Let's see how this helps by looking at the calculation in MVS5 in more detail.

## Fixed angle calculations

													 ------------------------

						The [MVS5](https://elite.bbcelite.com/cassette/main/subroutine/mvs5.html) routine applies the same trigonometry as described in routine MVS4 (see the deep dive on [rotating the universe](https://elite.bbcelite.com/rotating_the_universe.html) for details). In MVS5 we rotated the ship's orientation vectors by our own pitch and roll, but this time the angle is fixed at a very small 1/16 radians (around 3.6 degrees) so the maths is rather simpler. If you refer to the documentation for MVS4, you can see that the equations for rolling a point (x, y, z) through an angle a to (x´, y´, z´) are:

x´ = x * cos(a) - y * sin(a) y´ = y * cos(a) + x * sin(a) z´ = z

In this case, angle a is fixed at 1/16 radians, so we can take the small angle approximations described in MVS4, and reduce them like this:

```
  sin a ~= a
         = 1/16
  cos a ~= 1 - (a * a) / 2
         = 1 - (1/16 * 1/16) / 2
         = 1 - (1/256) / 2
         = 1 - 1/512
```
						Plugging these into the above equations, we get:

```
  x´ = x * cos(a) - y * sin(a)
     = x * (1 - 1/512) - y / 16
  y´ = y * cos(a) + x * sin(a)
     = y * (1 - 1/512) + x / 16
  z´ = z
```
						so this is what routine MVS5 implements.

To clarify further, let's consider the example when X = 15 (roofv_x) and Y = 21 (sidev_x), which applies roll to the ship. If we consider the orientation vectors, this is how the three vectors look if we're sitting in in the ship's cockpit:

```
  roofv (points up out of the ship's sunroof...
  ^       or it would if it had one)
  |
  |
  |
  |    nosev (points forward out of the ship's nose
  |   /        and into the screen)
  |  /
  | /
  |/
  +-----------------------> sidev (points out of the
                                   ship's right view)
```
						If we are doing a roll, then the nosev vector won't change, but roofv and sidev will rotate around, so let's just consider the x-y plane (i.e. the screen) and ignore the z-axis. It looks like this when we roll to the left by angle a, rotating roofv to roofv´ and sidev to sidev´:

```
            roofv
               ^
  roofv´       |
        \      |
         \     |
          \    |
           \   |
            \  |                 __ sidev´     <-.
             \ |         __..--''                a`.
              \| __..--''                          |
               +-----------------------> sidev
```
						Applying trigonometry to the above diagram, we get:

roofv´ = roofv * cos(a) - sidev * sin(a) sidev´ = sidev * cos(a) + roofv * sin(a)

so calling MVS5 with X = 15 (roofv_x) and Y = 21 (sidev_x) and a negative RAT2 (as the roll angle a is anti-clockwise in our example), we get the following if we do the calculation for the x coordinates in-place:

roofv_x = roofv_x * (1 - 1/512) - sidev_x / 16 sidev_x = sidev_x * (1 - 1/512) + roofv_x / 16

Subsequent calls with X = 17, Y = 23 and X = 19, Y = 25 cover the y and z coordinates, so that's exactly what the roll section of routine MVS5 does, with the pitch section doing the same maths, but on roofv and nosev.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
x´ = x * cos(a) - y * sin(a)
  y´ = y * cos(a) + x * sin(a)
  z´ = z
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
sin a ~= a
         = 1/16

  cos a ~= 1 - (a * a) / 2
         = 1 - (1/16 * 1/16) / 2
         = 1 - (1/256) / 2
         = 1 - 1/512
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
x´ = x * cos(a) - y * sin(a)
     = x * (1 - 1/512) - y / 16

  y´ = y * cos(a) + x * sin(a)
     = y * (1 - 1/512) + x / 16

  z´ = z
```

### Snippet Codice (BASIC)

```basic
roofv (points up out of the ship's sunroof...
  ^       or it would if it had one)
  |
  |
  |
  |    nosev (points forward out of the ship's nose
  |   /        and into the screen)
  |  /
  | /
  |/
  +-----------------------> sidev (points out of the
                                   ship's right view)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
roofv
               ^
  roofv´       |
        \      |
         \     |
          \    |
           \   |
            \  |                 __ sidev´     <-.
             \ |         __..--''                a`.
              \| __..--''                          |
               +-----------------------> sidev
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
roofv´ = roofv * cos(a) - sidev * sin(a)

  sidev´ = sidev * cos(a) + roofv * sin(a)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
roofv_x = roofv_x * (1 - 1/512) - sidev_x / 16

  sidev_x = sidev_x * (1 - 1/512) + roofv_x / 16
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/pitching_and_rolling_by_a_fixed_angle.html](https://elite.bbcelite.com/deep_dives/pitching_and_rolling_by_a_fixed_angle.html)*

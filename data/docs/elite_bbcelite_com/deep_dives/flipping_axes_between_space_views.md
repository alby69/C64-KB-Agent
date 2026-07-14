---
title: Flipping axes between space views
source_url: https://elite.bbcelite.com/deep_dives/flipping_axes_between_space_views.html
category: deep-dive
topics:
- assembly
difficulty: beginner
language: mixed
hardware:
- SID
- KERNAL
related:
- music-player
- sound-programming
- memory-map
- kernal-routines
- sid-registers
scraped_at: '2026-07-14'
---

# Flipping axes between space views

## Details of how the different space views are implemented

Switching space views in Elite is one of those seemingly simple ideas that ends up adding so much to the believability of the game universe. When you're in deep space and an asteroid or a peaceful trader appears in the distance up ahead, the ability to flick to the side view and then the rear view to watch it speed past your windows is truly immersive; you really feel you're inside a spaceship powering through space. And docking without being able to use the side views to line up for your approach run? Forget it. Those space views are an essential aspect of the game.

But do we really have to write four different display routines for the four views? Luckily we don't, as the authors came up with a mathematical solution that is both wonderfully elegant and extremely efficient. The solution, implemented in the [PLUT](https://elite.bbcelite.com/cassette/main/subroutine/plut.html) routine, is to flip the axes for everything we want to display in the space view, so the axes used in the drawing routines will still work.

The axis-flipping is quite a quick process. Indeed, there were originally six views, with up and down thrown into the mix, but they ended up being dropped to save space. It would only have taken a few extra instructions to implement their flipped axes and stardust views, so the space would most likely have been saved by removing the code supporting the extra laser mounts in the Equip Ship screen).

Let's see what axis-flipping actually means.

## Flipping the axes

													 -----------------

						The solution to having multiple views is similar in concept to the way we process pitch and roll. When we rotate our ship, we don't actually move our ship at all - instead, we rotate the entire universe around us, in the opposite direction to our movement (see the deep dives on "Pitching and rolling" and "Rotating the universe" for more details on this process). We do a similar kind of thing when we switch views, but instead of rotating all the other ships and planets around us, we flip the axes instead, which is a much quicker process.

How do we do this? First, we need to talk about the three axes. In terms of our relationship to the universe, the z-axis always points into the screen, the y-axis always points up, and the x-axis always points to the right, like this:

```
    y
    ^
    |   z (into screen)
    |  /
    | /
    |/
    +---------> x
```
						This rule always applies, whichever view we are looking through. So when we're looking through the front view, the z-axis is into the screen, which is also the direction of travel - but if we switch to the left view, then the z-axis is still into the screen, but the direction of travel is now to our right, along the x-axis. So what was the z-axis is now the x-axis... so the axes just flipped. That flipping process is essentially what the PLUT routine does.

It's important to note that the local universe is stored in the ship data blocks at K% as if we are looking forward, so as far as the stored coordinates are concerned, the z-axis is always in the direction of travel. As part of the main flight loop, each ship data block is copied on turn into the INWK workspace, where the movement routines in MVEIT are applied, before the block is copied back into K% with the position of the ship updated.

It's after all the data has been copied back to K% that we start flipping axes to fit the current space view, but this flipped version of the ship doesn't get stored anywhere - the flipped data is only used for working out missile and laser lock, and for drawing the ship, as these are the parts that are affected by the view we're looking through.

Anyway, back to the process of flipping axes. If we are looking through the front view then there is no flipping to be done, as the ship coordinates in INWK are already using the correct axes, as mentioned above. If, however, we are looking to the sides or rear, then the PLUT routine takes the ship coordinates from INWK and switches the axes around, so that we can use the same routines to display what's in that view.

For example, take the z-axis, which points into the screen for the front view. We move it to point out of the screen if we are looking backwards, to the right if we're looking out of the left view, or to the left if we are looking out of the right view.

For the front view, then, we change nothing. Let's look at the other views in more detail, because this is one of those concepts that makes a lot more sense when you draw pretty diagrams.

## Rear view

													 ---------

						For the rear view, this is what our original universe axes look like when we are looking backwards:

```
                y
                ^
                |
                |
                |
                |
    x <---------+
               /
              z (out of screen)
```
						so to convert these axes into the standard "up, right, into-the-screen" set of axes we need for drawing to the screen, we need to do the changes on the left (with the original set of axes on the right for comparison):

y y ^ ^ | -z (into screen) | z (into screen) | / | / | / | / |/ |/ +---------> -x +---------> x

So to change the INWK workspace from the original axes on the right to the new set on the left, we need to change the signs of the x and z coordinates and vectors in INWK, which we can do by flipping the signs of the following:

- x_sign, z_sign
- nosev_x_hi, nosev_z_hi
- roofv_x_hi, roofv_z_hi
- sidev_x_hi, sidev_z_hi

So this is what we do in the PLUT routine for the rear view.

## Left view

													 ---------

						For the left view, this is what our original universe axes look like when we are looking to the left:

```
      y
      ^
      |
      |
      |
      |
      +---------> z
     /
    /
   /
  x (out of screen)
```
						so to convert these axes into the standard "up, right, into-the-screen" set of axes we need for drawing to the screen, we need to do the changes on the left (with the original set of axes on the right for comparison):

y y ^ ^ | -x (into screen) | z (into screen) | / | / | / | / |/ |/ +---------> z +---------> x

In other words, to go from the original set of axes on the right to the new set of axes on the left, we need to swap the x- and z-axes around, and flip the sign of the one now going in and out of the screen (i.e. the new z-axis). In other words, we swap the following values in INWK:

- x_lo and z_lo
- x_hi and z_hi
- x_sign and z_sign
- nosev_x_lo and nosev_z_lo
- roofv_x_lo and roofv_z_lo
- sidev_x_lo and sidev_z_lo

and then change the sign of the axis going in and out of the screen by flipping the signs of the following:

- z_sign
- nosev_z_hi
- roofv_z_hi
- sidev_z_hi

So this is what we do in the PLUT routine for the left view.

## Right view

													 ---------

						For the right view, this is what our original universe axes look like when we are looking to the right:

```
              y
              ^
              |   x (into screen)
              |  /
              | /
              |/
  z <---------+
```
						so to convert these axes into the standard "up, right, into-the-screen" set of axes we need for drawing to the screen, we need to do the changes on the left (with the original set of axes on the right for comparison):

y y ^ ^ | x (into screen) | z (into screen) | / | / | / | / |/ |/ +---------> -z +---------> x

In other words, to go from the original set of axes on the right to the new set of axes on the left, we need to swap the x- and z-axes around, and flip the sign of the one now going to the right (i.e. the new x-axis). In other words, we swap the following values in INWK:

- x_lo and z_lo
- x_hi and z_hi
- x_sign and z_sign
- nosev_x_lo and nosev_z_lo
- roofv_x_lo and roofv_z_lo
- sidev_x_lo and sidev_z_lo

and then change the sign of the axis going to the right by flipping the signs of the following:

- x_sign
- nosev_x_hi
- roofv_x_hi
- sidev_x_hi

So this is what we do in the PLUT routine for the right view.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
y
    ^
    |   z (into screen)
    |  /
    | /
    |/
    +---------> x
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
y
                ^
                |
                |
                |
                |
    x <---------+
               /
              z (out of screen)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
y                                           y
  ^                                           ^
  |   -z (into screen)                        |   z (into screen)
  |  /                                        |  /
  | /                                         | /
  |/                                          |/
  +---------> -x                              +---------> x
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
y
      ^
      |
      |
      |
      |
      +---------> z
     /
    /
   /
  x (out of screen)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
y                                           y
  ^                                           ^
  |   -x (into screen)                        |   z (into screen)
  |  /                                        |  /
  | /                                         | /
  |/                                          |/
  +---------> z                               +---------> x
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
y
              ^
              |   x (into screen)
              |  /
              | /
              |/
  z <---------+
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
y                                           y
  ^                                           ^
  |   x (into screen)                         |   z (into screen)
  |  /                                        |  /
  | /                                         | /
  |/                                          |/
  +---------> -z                              +---------> x
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/flipping_axes_between_space_views.html](https://elite.bbcelite.com/deep_dives/flipping_axes_between_space_views.html)*

---
title: Orientation vectors
source_url: https://elite.bbcelite.com/deep_dives/orientation_vectors.html
category: deep-dive
topics:
- basic
- assembly
difficulty: intermediate
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

# Orientation vectors

## The three vectors that determine a ship's orientation in space

Each ship in the Elite universe has its own set of three orientation vectors, which determine its orientation in space. These are fundamental aspects of the Elite universe, and form the basis for the ship-moving routines in [MVEIT](https://elite.bbcelite.com/cassette/main/subroutine/mveit_part_1_of_9.html) (moving the universe), [MVS4](https://elite.bbcelite.com/cassette/main/subroutine/mvs4.html) (pitching and rolling our ship) and [MVS5](https://elite.bbcelite.com/cassette/main/subroutine/mvs5.html) (pitching and rolling other ships).

There are three different vectors - nosev, roofv and sidev - with each of them pointing along one of the ship's main axes, like this:

- nosev points forward out of the nose of the ship
- roofv points up out of the ship's sunroof... or it would if it had one
- sidev points out of the ship's right view

So if we're looking at the Cobra Mk III on the title screen, like this:

![The title screen in the BBC Micro version of Elite](https://elite.bbcelite.com/images/cassette/title.png) 

						then this is how the orientation vectors are arranged:

- nosev points out of the nose, towards the bottom-right corner
- roofv points out of the roof, coming out of the screen to the top-right
- sidev points out of the right side, towards the bottom-left corner

(Note that there are five ships that have slightly different orientations to this standard model, namely Thargoids, Thargons, space stations, cargo canisters and asteroids. These orientations are described below.)

It might help to think of these vectors from the point of view of the ship's cockpit. From this perspective, the orientation vectors always look like this, with our ship at the origin:

roofv ^ | | | | nosev | / | / | / |/ +-----------------------> sidev

Every ship out there has its own set of orientation vectors, with nosev pointing out of that ship's nose, roofv pointing out of that ship's roof, and sidev out of that ship's right side. The orientation vectors are used in lots of places, for example:

- When we draw the ship on screen, we take the shape as defined by its blueprint, and rotate it so that it aligns with its orientation vectors, so the ship we draw on screen points the right way
- If an enemy ship is firing its lasers at us, we use that ship's nosev vector to work out whether it is pointing towards us, and therefore whether it can hit us
- When enemy ships pitch or roll, we can apply these movements by rotating their orientation vectors

Our ship doesn't have its own set of orientation vectors - at least, not explicitly. This is because our own ship's orientation vectors always align with the main coordinate axes: sidev aligns with the x-axis, which always points to the right from the point of view of our cockpit, while roofv aligns with the y-axis and points up, and nosev aligns with the z-axis, which always points into the screen.

## Storing the vectors in the ship data block

													 ------------------------------------------

						The three vectors are stored in bytes #9-26 of the ship's data block, so when we copy a ship's data into the internal workspace INWK, the vectors live in INWK+9 to INWK+26. Each vector coordinate is stored as a 16-bit sign-magnitude number, like this:

```
          [ INWK(10 9)  ]           [ INWK(16 15) ]           [ INWK(22 21) ]
  nosev = [ INWK(12 11) ]   roofv = [ INWK(18 17) ]   sidev = [ INWK(24 23) ]
          [ INWK(14 13) ]           [ INWK(20 19) ]           [ INWK(26 25) ]
```
						We can refer to these three vectors in various ways, such as these variations for the nosev vector:

```
  nosev = (nosev_x, nosev_y, nosev_z)
        = [ nosev_x nosev_y nosev_z ]
          [ nosev_x ]
        = [ nosev_y ]
          [ nosev_z ]
          [ (nosev_x_hi nosev_x_lo) ]
        = [ (nosev_y_hi nosev_y_lo) ]
          [ (nosev_z_hi nosev_z_lo) ]
```
						## Orthonormal vectors

													 -------------------

						The three orientation vectors are orthonormal, which means they are orthogonal (i.e. they are perpendicular to each other), and normal (i.e. each of the vectors has length 1).

We can rotate a ship about its centre by rotating these vectors, as in the MVS4 routine (see the deep dive on [pitching and rolling](https://elite.bbcelite.com/pitching_and_rolling.html) for more about this). However, because we use the small angle approximation to rotate in space, and it is not completely accurate, the three vectors tend to get a bit stretched over time, so periodically we have to tidy the vectors with the [TIDY](https://elite.bbcelite.com/cassette/main/subroutine/tidy.html) routine to ensure they remain as orthonormal as possible (see the deep dive on [tidying orthonormal vectors](https://elite.bbcelite.com/tidying_orthonormal_vectors.html) for details).

## Initialisation

													 --------------

						When a new ship is spawned, its vectors are initialised in the [INWK](https://elite.bbcelite.com/cassette/main/workspace/zp.html#inwk) workspace by the [ZINF](https://elite.bbcelite.com/cassette/main/subroutine/zinf.html) routine as follows:

sidev = (1, 0, 0) roofv = (0, 1, 0) nosev = (0, 0, -1)

So new ships are spawned facing out of the screen, as their nosev vectors point in a negative direction along the z-axis, which is positive into the screen and negative out of the screen. They are also spawned with roofv pointing up and sidev pointing right (though see below for some exceptions to this rule)

Internally, we store the unit vector with a length of (96 0), or &6000, as a 16-bit sign-magnitude number. We use this high value to make it easier to support fractional calculations, which wouldn't be possible if we used a value of 1 for the unit vector length; instead the value of (96 0) represents a length of 1, just scaled up to allow for accuracy. &60 with bit 7 set is &E0, so &E000 represents -1, and we can store the above vectors like this:

sidev = (&6000, 0, 0) roofv = (0, &6000, 0) nosev = (0, 0, &E000)

So in this case, nosev_z_hi = &E0 = -96, sidev_x_hi = &60 = 96 and so on, while all the low bytes are zero. For a discussion of just how big this initial vector is, see the deep dive on [a sense of scale](https://elite.bbcelite.com/a_sense_of_scale.html).

Planets are spawned in the same way as ships, i.e. with nosev pointing towards us, out of the screen, and with roofv pointing up and sidev pointing right. The orientation vectors are used to draw the planet's meridians and craters; for example, the crater is drawn at the end of the roofv vector, specifically when it is pointing away from us. See the deep dives on [drawing craters](https://elite.bbcelite.com/drawing_craters.html) and [drawing meridians and equators](https://elite.bbcelite.com/drawing_meridians_and_equators.html) for more details.

This means the crater is on the very top of the planet when we arrive out of hyperspace (or launch), and because the planet is set to pitch clockwise around the right-pointing sidev, it means roofv rolls to point towards us, and the crater is not shown immediately. If you launch from the station around a crater system like Zaonce, then the crater does indeed not appear for half a rotation, as roofv takes a while to rotate until it's pointing away from us.

## Rotation matrices and axes

													 --------------------------

						Sometimes we might refer to the orientation vectors as a matrix, with sidev as the first row, roofv as the second row, and nosev as the third row, like this:

[ sidev_x sidev_y sidev_z ] [ roofv_x roofv_y roofv_z ] [ nosev_x nosev_y nosev_z ]

though generally we talk about the individual vectors, because that's easier to understand. See the deep dive on [calculating vertex coordinates](https://elite.bbcelite.com/calculating_vertex_coordinates.html) for an example of the above matrix in use.

For the mathematically inclined, the three orientation vectors can be thought of as axes that define the 3D coordinate space orientated around the other ship - they form the basis for this space. To put it yet another way, the matrix above is a rotation matrix that transforms the axes of our ship into the axes of the other ship.

Finally, the orientation vectors define a left-handed universe, with the thumb as roofv, index finger as nosev, and middle finger as sidev.

## Non-standard orientations

													 -------------------------

						Not all ships are spawned with the nosev pointing towards us. For example, the space station is an exception; when we launch from the station, it is spawned with nosev pointing away from us, into the screen. This is because nosev points out of the station slot, and when we launch from it, we want the station to be spawned behind us, and with the slot facing forwards, in the same direction that we are looking. You can see this logic in the [TT110](https://elite.bbcelite.com/cassette/main/subroutine/tt110.html) launch routine, which places the new station behind us before calling [NWSPS](https://elite.bbcelite.com/cassette/main/subroutine/nwsps.html) to flip nosev before spawning the station with NWSHP.

The following ships don't have a standard orientation (all other ships follow the logical nose-roof-side pattern).

- Thargoid mothership:
								- nosev points out of one side of the mothership
- roofv points out of the other side of the mothership
- sidev points out of the roof of the mothership
 
- Thargon:
								- nosev points out of the Thargon's nose
- roofv points out of the side of the Thargon
- sidev points out of the roof of the Thargon
 
- Space station:
								- nosev points forward out of the docking slot
- roofv points out of the side of the space station in a direction that is parallel to the horizontal line of the slot
- sidev points out of the side of the space station in a direction that is perpendicular to the horizontal line of the slot
 
- Cargo canister:
								- nosev points out of the side of the canister, avoiding the apexes of the pentagonal cross-section and at right-angles to roofv
- roofv points out of the side of the canister, through one of the apexes of the pentagonal cross-section
- sidev points out of one end of the canister
 

The asteroid also follows its own orientation, but I'm not even going to try to describe which features appear to be the nose, roof and side, as they all just look like bumps to me.

One interesting (and presumably intentional) effect of the Thargoid and Thargon orientations can be seen when they pitch and roll. A pitching Thargoid actually spins like a traditional flying saucer (i.e. like a spinning top) as its roofv vector points out of its side (though a rolling Thargoid tilts back and forth as expected). When fighting Thargoids, you often find yourself orientating your ship to get them vertically aligned in your sights, which is because you can then track their sideways pitching with your own vertical pitching movement. This is different to the other ships, which expose their soft underbellies to your lasers when they try to pitch out of your way.

That's Thargoids for you. Different... and deadly.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
roofv
  ^
  |
  |
  |
  |    nosev
  |   /
  |  /
  | /
  |/
  +-----------------------> sidev
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
[ INWK(10 9)  ]           [ INWK(16 15) ]           [ INWK(22 21) ]
  nosev = [ INWK(12 11) ]   roofv = [ INWK(18 17) ]   sidev = [ INWK(24 23) ]
          [ INWK(14 13) ]           [ INWK(20 19) ]           [ INWK(26 25) ]
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
nosev = (nosev_x, nosev_y, nosev_z)

        = [ nosev_x nosev_y nosev_z ]

          [ nosev_x ]
        = [ nosev_y ]
          [ nosev_z ]

          [ (nosev_x_hi nosev_x_lo) ]
        = [ (nosev_y_hi nosev_y_lo) ]
          [ (nosev_z_hi nosev_z_lo) ]
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
sidev = (1,  0,  0)
  roofv = (0,  1,  0)
  nosev = (0,  0, -1)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
sidev = (&6000, 0, 0)
  roofv = (0, &6000, 0)
  nosev = (0, 0, &E000)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
[ sidev_x sidev_y sidev_z ]
  [ roofv_x roofv_y roofv_z ]
  [ nosev_x nosev_y nosev_z ]
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/orientation_vectors.html](https://elite.bbcelite.com/deep_dives/orientation_vectors.html)*

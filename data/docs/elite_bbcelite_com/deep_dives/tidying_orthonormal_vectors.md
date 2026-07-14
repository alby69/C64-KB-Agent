---
title: Tidying orthonormal vectors
source_url: https://elite.bbcelite.com/deep_dives/tidying_orthonormal_vectors.html
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

# Tidying orthonormal vectors

## Making the orientation vectors orthonormal, and why this matters

There are an awful lot of rotations in Elite. When we pitch or roll, we rotate the entire universe around our ship, so every ship in our local bubble of universe gets rotated in space every time we tap our controls. Not only do we rotate the ship's position in space by our pitch and roll in part 5 of MVEIT, but we also rotate the ship's orientation vectors by our pitch and roll in MVS4, and we rotate the orientation vectors again, this time around the ship's centre, when we apply the ship's own pitch and roll in part 8 of MVEIT.

One of the problems with all this rotating is that we use the small angle approximation to rotate all these vectors in space. This is not completely accurate, so the three orientation vectors tend to get stretched over time, so periodically we have to tidy the vectors with the [TIDY](https://elite.bbcelite.com/cassette/main/subroutine/tidy.html) routine. If we don't do this, then ships and stations will slowly stretch out of shape, like this:

![A stretched space station when tidying is disabled](https://elite.bbcelite.com/images/cassette/tidying_vectors.png) 

						Just to show how important this is, here's a video of what happens to a space station if we disable the vector-tidying routine:

Elite's calculations rely on having orthonormal orientation vectors, which means the three orientation vectors are both orthogonal (perpendicular to each other) and normal (so each of the vectors has length 1). The TIDY routine therefore tidies up the vectors by making them orthogonal, before calling the [NORM](https://elite.bbcelite.com/cassette/main/subroutine/norm.html) routine to do the normalisation part, thus producing orthonormal vectors. Elite tidies one ship on most iterations of the main flight loop, as it's a time-consuming business (it actually tidies one ship slot on 12 out of every 16 iterations).

The challenge, then, is to take the three orientation vectors - nosev, roofv and sidev - and tweak them so that they are orthogonal and normal once again. Let's call these new, tweaked vectors nosev´, roofv´ and sidev´, and let's look at how we can calculate them.

## The first vector, nosev´

													 ------------------------

						First, let's normalise nosev, so it has length 1 (stored internally as 96), and let's call this nosev´. We start with the nose vector, as normalising it doesn't change the direction that the ship is pointing in, so if we happen to be looking at a ship as it gets tidied, at least it won't change direction.

## The second vector, roofv´

													 -------------------------

						Next, we want to tweak roofv into a new vector roofv´, where roofv´ is perpendicular to nosev´. When two vectors are perpendicular, their dot product is zero, so this means:

roofv´ . nosev´ = 0

This expands to:

nosev_x´ * roofv_x´ + nosev_y´ * roofv_y´ + nosev_z´ * roofv_z´ = 0

which we can expand to the following:

roofv_x´ = -(nosev_y´ * roofv_y´ + nosev_z´ * roofv_z´) / nosev_x´ roofv_y´ = -(nosev_x´ * roofv_x´ + nosev_z´ * roofv_z´) / nosev_y´ roofv_z´ = -(nosev_x´ * roofv_x´ + nosev_y´ * roofv_y´) / nosev_z´

Because time is of the essence, we would rather only calculate one of these, so we do a clever trick. If you think of two arbitrary lines on a piece of paper, then given any direction, it's possible to move the end of one of the lines in that direction so that the lines become parallel. In the case of our vectors, this means we can tweak roofv in one axis only - i.e. only change one of its x, y, and z coordinates - and can still get a vector that's at right-angles to nosev´.

So let's say that we tweak roofv in the x-axis only, then that means we leave roofv_y and roofv_z alone - so roofv_y´ = roofv_y and roofv_z´ = roofv_z. So this means:

roofv_x´ = -(nosev_y´ * roofv_y + nosev_z´ * roofv_z) / nosev_x´ roofv_y´ = roofv_y roofv_z´ = roofv_z

So we can just tweak roofv_x to roofv_x´, using this calculation:

roofv_x´ = -(nosev_y´ * roofv_y + nosev_z´ * roofv_z) / nosev_x´

and roofv´ will be perpendicular to nosev; then all we need to do is normalise roofv´ and we've got our second orthonormal vector.

We can do the same with any of the axes, leading to these two equations:

roofv_y´ = -(nosev_x´ * roofv_x + nosev_z´ * roofv_z) / nosev_y´ roofv_z´ = -(nosev_x´ * roofv_x + nosev_y´ * roofv_y) / nosev_z´

So how do we choose which coordinate axis to move? Well, seeing as we are going to be dividing by one of the coordinates of nosev´ in our calculation, and dividing by big numbers in integer arithmetic isn't so accurate (as we're dealing in integers here, not floating point numbers), we could always choose an equation with a low nosev value, and this is exactly what Elite does. First we check whether nosev_x´ is small, and if it is, we do this one:

roofv_x´ = -(nosev_y´ * roofv_y + nosev_z´ * roofv_z) / nosev_x´

Otherwise we check whether nosev_y´ is small, and if it is, we do this one:

roofv_y´ = -(nosev_x´ * roofv_x + nosev_z´ * roofv_z) / nosev_y´

Otherwise, we have no choice but to do this one:

roofv_z´ = -(nosev_x´ * roofv_x + nosev_y´ * roofv_y) / nosev_z´

And finally we normalise roofv, so it has length 1 (stored internally as 96)

## The third vector, sidev´

													 ------------------------

						So we have two vectors in nosev´ and roofv´ that are orthogonal and normal, so we just need to find a vector that is perpendicular to these two. There's an easy way to calculate such a vector, by using the cross-product.

The cross-product works like this. Consider two vectors, a and b, which have an angle theta between them. The cross-product of these two vectors, a x b, gives us another vector that is at right-angles to the first two, and which has length |a| * |b| * sin(theta).

In other words, if we calculate the following:

sidev = nosev x roofv

which we can do by breaking it down into axes:

```
  [ sidev_x ]   [ nosev_x´ ]   [ roofv_x´ ]
  [ sidev_y ] = [ nosev_y´ ] x [ roofv_y´ ]
  [ sidev_z ]   [ nosev_z´ ]   [ roofv_z´ ]
                [ nosev_z´ * roofv_y´ - nosev_y´ * roofv_z´ ]
              = [ nosev_x´ * roofv_z´ - nosev_z´ * roofv_x´ ]
                [ nosev_y´ * roofv_x´ - nosev_x´ * roofv_y´ ]
```
						then this sets sidev to a vector that is perpendicular to the others, and which has length |nosev´| * |roofv´| * sin(theta). We know that because nosev´ and roofv´ are orthonormal, theta must be a right-angle, and |nosev´| and |roofv´| must be 1, so this means sidev has length 1:

|nosev´| * |roofv´| * sin(theta) = 1 * 1 * 1 = 1

So if we calculate the following in the TIDY routine, this will set sidev to a vector of length 1 that's perpendicular to the other two, which is a third orthonormal vector - exactly what we want our third vector to be.

sidev_x´ = (nosev_z´ * roofv_y´ - nosev_y´ * roofv_z´) / 96 sidev_y´ = (nosev_x´ * roofv_z´ - nosev_z´ * roofv_x´) / 96 sidev_z´ = (nosev_y´ * roofv_x´ - nosev_x´ * roofv_y´) / 96

We divide by 96 as we use 96 to represent 1 internally. This means the length of nosev and roofv internally is actually 96, so the length of the cross-product would be 96 * 96. We want the length of sidev to be 96 (so it represents 1), so we divide by 96 to get the correct result.

This leaves us with orthonormal vectors, and this is how the TIDY routine tidies the orientation vectors, so the ships don't stretch and warp in space when they are rotated.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
roofv´ . nosev´ = 0
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
nosev_x´ * roofv_x´ + nosev_y´ * roofv_y´ + nosev_z´ * roofv_z´ = 0
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
roofv_x´ = -(nosev_y´ * roofv_y´ + nosev_z´ * roofv_z´) / nosev_x´
  roofv_y´ = -(nosev_x´ * roofv_x´ + nosev_z´ * roofv_z´) / nosev_y´
  roofv_z´ = -(nosev_x´ * roofv_x´ + nosev_y´ * roofv_y´) / nosev_z´
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
roofv_x´ = -(nosev_y´ * roofv_y + nosev_z´ * roofv_z) / nosev_x´
  roofv_y´ = roofv_y
  roofv_z´ = roofv_z
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
roofv_x´ = -(nosev_y´ * roofv_y + nosev_z´ * roofv_z) / nosev_x´
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
roofv_y´ = -(nosev_x´ * roofv_x + nosev_z´ * roofv_z) / nosev_y´
  roofv_z´ = -(nosev_x´ * roofv_x + nosev_y´ * roofv_y) / nosev_z´
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
roofv_x´ = -(nosev_y´ * roofv_y + nosev_z´ * roofv_z) / nosev_x´
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
roofv_y´ = -(nosev_x´ * roofv_x + nosev_z´ * roofv_z) / nosev_y´
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
roofv_z´ = -(nosev_x´ * roofv_x + nosev_y´ * roofv_y) / nosev_z´
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
sidev = nosev x roofv
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
[ sidev_x ]   [ nosev_x´ ]   [ roofv_x´ ]
  [ sidev_y ] = [ nosev_y´ ] x [ roofv_y´ ]
  [ sidev_z ]   [ nosev_z´ ]   [ roofv_z´ ]

                [ nosev_z´ * roofv_y´ - nosev_y´ * roofv_z´ ]
              = [ nosev_x´ * roofv_z´ - nosev_z´ * roofv_x´ ]
                [ nosev_y´ * roofv_x´ - nosev_x´ * roofv_y´ ]
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
|nosev´| * |roofv´| * sin(theta) = 1 * 1 * 1 = 1
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
sidev_x´ = (nosev_z´ * roofv_y´ - nosev_y´ * roofv_z´) / 96
  sidev_y´ = (nosev_x´ * roofv_z´ - nosev_z´ * roofv_x´) / 96
  sidev_z´ = (nosev_y´ * roofv_x´ - nosev_x´ * roofv_y´) / 96
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/tidying_orthonormal_vectors.html](https://elite.bbcelite.com/deep_dives/tidying_orthonormal_vectors.html)*

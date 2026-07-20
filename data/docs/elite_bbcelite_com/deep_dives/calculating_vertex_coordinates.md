---
title: Calculating vertex coordinates
source_url: https://elite.bbcelite.com/deep_dives/calculating_vertex_coordinates.html
category: deep-dive
topics:
- assembly
difficulty: intermediate
language: assembly
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

# Calculating vertex coordinates

## Determining whether a ship's vertex is visible or hidden from us

To understand the following, you'll probably want to have a look through the deep dive on [back-face culling](https://elite.bbcelite.com/back-face_culling.html), which describes how we can work out whether or not a ship's face is visible.

As part of the back-face cull, we projected the vector [x y z] onto the orientation vector space like this:

[x y z] projected onto sidev = [x y z] . sidev [x y z] projected onto roofv = [x y z] . roofv [x y z] projected onto nosev = [x y z] . nosev

We can express this exact same calculation in terms of matrix multiplication:

[ sidev ] [ x ] [ roofv ] . [ y ] [ nosev ] [ z ]

or, expanding it out fully:

```
                      [ sidev_x sidev_y sidev_z ]   [ x ]
  projected [x y z] = [ roofv_x roofv_y roofv_z ] . [ y ]
                      [ nosev_x nosev_y nosev_z ]   [ z ]
```
						This is just a different way of expressing the exact same equation as we used in [part 5 of LL9](https://elite.bbcelite.com/cassette/main/subroutine/ll9_part_5_of_12.html), just with a matrix instead of individual dot products.

## Transposing the rotation matrix

													 -------------------------------

						So the inverse matrix will map vectors in the orientation vector space back into normal ship space. The inverse of a rotation matrix is its transpose (as long as it is a unit matrix), so this is the calculation:

```
                      [ sidev_x roofv_x nosev_x ]   [ x ]
  projected [x y z] = [ sidev_y roofv_y nosev_y ] . [ y ]
                      [ sidev_z roofv_z nosev_z ]   [ z ]
```
						This takes a vector, which goes from the ship's centre to the vertex and is expressed in terms of the ship's axes (i.e. its orientation vectors), and instead expresses it in terms of our ship's axes (i.e. our orientation vectors).

Given this new vector, we can add the vector from our ship to the other ship, to get the vector from us to the vertex, expressed in our ship's coordinates:

```
                     [ sidev_x roofv_x nosev_x ]   [ x ]   [ x ]
  vector to vertex = [ sidev_y roofv_y nosev_y ] . [ y ] + [ y ]
                     [ sidev_z roofv_z nosev_z ]   [ z ]   [ z ]
```
						The code to calculate this equation takes up [part 6](https://elite.bbcelite.com/cassette/main/subroutine/ll9_part_6_of_12.html) and [part 7 of LL9](https://elite.bbcelite.com/cassette/main/subroutine/ll9_part_7_of_12.html). It's in two parts because there are two small subroutines that have rudely inserted themselves just before the big reveal. These are used by part 8 and don't play a part in this calculation (except to make it harder to follow).

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
[x y z] projected onto sidev = [x y z] . sidev
  [x y z] projected onto roofv = [x y z] . roofv
  [x y z] projected onto nosev = [x y z] . nosev
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
[ sidev ]   [ x ]
  [ roofv ] . [ y ]
  [ nosev ]   [ z ]
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
[ sidev_x sidev_y sidev_z ]   [ x ]
  projected [x y z] = [ roofv_x roofv_y roofv_z ] . [ y ]
                      [ nosev_x nosev_y nosev_z ]   [ z ]
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
[ sidev_x roofv_x nosev_x ]   [ x ]
  projected [x y z] = [ sidev_y roofv_y nosev_y ] . [ y ]
                      [ sidev_z roofv_z nosev_z ]   [ z ]
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
[ sidev_x roofv_x nosev_x ]   [ x ]   [ x ]
  vector to vertex = [ sidev_y roofv_y nosev_y ] . [ y ] + [ y ]
                     [ sidev_z roofv_z nosev_z ]   [ z ]   [ z ]
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/calculating_vertex_coordinates.html](https://elite.bbcelite.com/deep_dives/calculating_vertex_coordinates.html)*

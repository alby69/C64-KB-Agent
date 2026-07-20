---
title: The sine, cosine and arctan tables
source_url: https://elite.bbcelite.com/deep_dives/the_sine_cosine_and_arctan_tables.html
category: deep-dive
topics: []
difficulty: intermediate
language: none
hardware:
- KERNAL
related:
- memory-map
- kernal-routines
scraped_at: '2026-07-20'
---

# The sine, cosine and arctan tables

## The lookup tables used for the planet-drawing trigonometric functions

As described in the deep dives on [drawing circles](https://elite.bbcelite.com/drawing_circles.html) and [drawing ellipses](https://elite.bbcelite.com/drawing_ellipses.html), Elite's circle and ellipse routines use lookup tables to implement the required trigonometric functions. The result is some beautifully smooth planets and craters, like this:

![A view of Diso in BBC Micro Elite](https://elite.bbcelite.com/images/ellipses/diso.png) 

						The circle and ellipse routines use two trigonometric lookup tables, as follows:

- The [SNE](https://elite.bbcelite.com/cassette/main/variable/sne.html)table contains lookup values for sine and cosine. These values are used when drawing circles and ellipses, as the small angle approximation that we use when rotating ships in space isn't accurate enough for describing entire circles. For this, we need to be able to look up the sine and cosine of any angle, not just small ones, and for that we need a lookup table.
- The [ACT](https://elite.bbcelite.com/cassette/main/variable/act.html)table, meanwhile, contains lookup values for arctan, and is used by the[ARCTAN](https://elite.bbcelite.com/cassette/main/subroutine/arctan.html)routine. This is used when drawing the meridians and equators on planets in part 2 of PL9.

Let's have a look at how these tables work.

(Note that this approach is different to the trigonometry used in the rotation routines, which use the small angle approximation for speed - see the deep dive on [pitching and rolling](https://elite.bbcelite.com/pitching_and_rolling.html) for details).

## Sine table

													 ----------

						We use the sine table like this. To calculate the following:

sin(theta) * 256

where theta is in radians, we look up the value in:

SNE + (theta * 10)

Here's how this works. The value at byte number (theta * 10) is:

256 * ABS(SIN((theta * 10 / 64) * 2 * PI))

rounded to the nearest integer. If we expand the part that we pass to SIN():

```
  (theta * 10 / 64) * 2 * PI =  (theta / 6.4) * 2 * PI
                             =~ (theta / 6.4) * 6.28
                             =~ theta
```
						then substituting this into the above, we can see that the value at byte (theta * 10) is approximately:

256 * ABS(SIN(theta))

## Cosine table

            							 ------------

						So that's the sine lookup, but what about the cosine? To calculate the following:

cos(theta) * 256

where theta is in radians, we look up the value in:

SNE + ((theta * 10) + 16) mod 32

How does this work? Well, because of the way sine and cosine work in terms of right-angled triangles, the following holds true (using degrees for a second as it's easier to picture):

cos(theta) = sin(90 - theta) = sin(90 + theta)

So to get the cosine value, we just need to look up the sine of 90 + theta.

The 32 entries in the sine table cover half a circle, as they go from sin(0) to sin(31/64 * 2 * PI) and there are 2 * PI radians in a circle, so if 32 entries covers half a circle, 90 degrees is a half of that, or 16.

So to get the cosine, we look up the following value, applying mod 32 so the table lookup wraps around correctly if the index falls over the end:

SNE + ((theta * 10) + 16) mod 32

It's not 100% accurate, but it's easily good enough for our needs.

## Arctan table

													 ------------

						To calculate the following:

theta = arctan(t)

where 0 <= t < 1, we look up the value in:

ACT + (t * 32)

The result will be an integer representing the angle in radians, with 256 representing a full circle of 2 * PI radians.

The ACT table contains arctan values for arguments less than one - in other words, it contains values for arctan(0) through arctan(31/32), or angles in triangles where the length of the opposite is less than the length of the adjacent, so the angle is less than 45 degrees. This means the table contains values in the range 0 to 31.

The table does not support values of t >= 1 or t < 0 directly, but we can use the following calculations instead:

- For t > 1, arctan(t) = 64 - arctan(1 / t)
- For t < 0, arctan(-t) = 128 - arctan(t)

If t < -1, we can do the first one to get arctan(|t|), then the second to get arctan(-|t|).

The first one follows from the fact that arctan(t) + arctan(1 / t) = PI / 2, and we represent PI / 2 by 64 in our model.

The second one follows from the fact that arctan(-t) = PI - arctan(t) for the range 0 < arctan(t) < PI, and we represent PI by 128 in our model.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
sin(theta) * 256
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
SNE + (theta * 10)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
256 * ABS(SIN((theta * 10 / 64) * 2 * PI))
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
(theta * 10 / 64) * 2 * PI =  (theta / 6.4) * 2 * PI
                             =~ (theta / 6.4) * 6.28
                             =~ theta
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
256 * ABS(SIN(theta))
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
cos(theta) * 256
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
SNE + ((theta * 10) + 16) mod 32
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
cos(theta) = sin(90 - theta) = sin(90 + theta)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
SNE + ((theta * 10) + 16) mod 32
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
theta = arctan(t)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
ACT + (t * 32)
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/the_sine_cosine_and_arctan_tables.html](https://elite.bbcelite.com/deep_dives/the_sine_cosine_and_arctan_tables.html)*

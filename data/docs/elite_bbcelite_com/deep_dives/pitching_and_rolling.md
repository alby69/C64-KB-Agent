---
title: Pitching and rolling
source_url: https://elite.bbcelite.com/deep_dives/pitching_and_rolling.html
category: source-code
topics:
- assembly
- input handling
difficulty: beginner
language: assembly
hardware:
- CPU
- SID
- KERNAL
- CIA
related:
- keyboard-handling
- music-player
- sound-programming
- joystick-reading
- memory-map
- kernal-routines
- sid-registers
- cia-registers
scraped_at: '2026-07-14'
---

# Pitching and rolling

## Applying our pitch and roll to another ship's orientation in space

In order to understand the [MVS4](https://elite.bbcelite.com/cassette/main/subroutine/mvs4.html) routine, we need first to understand what it's for, so consider our Cobra Mk III sitting in deep space, minding its own business, when an enemy ship appears in the distance. Inside the little bubble of universe that Elite creates to simulate this scenario, our ship is at the origin (0, 0, 0), and the enemy ship has just popped into existence at (x, y, z), where the x-axis is to our right, the y-axis is up, and the z-axis is in the direction our Cobra is pointing in.

Here's a video of this scenario:

Of course, our first thought is to pitch and roll our Cobra to get the new arrival firmly into the crosshairs, and in doing this the enemy ship will appear to move in space, relative to us. For example, if we do a pitch by pulling back on the joystick or pressing "X", this will pull the nose of our Cobra Mk III up, and the point (x, y, z) will appear to move down in the sky in front of us.

So this routine calculates the movement of the enemy ship in space when we pitch and roll, as then the game can show the ship on-screen and work out whether our lasers are pointing in the correct direction to unleash fiery death on the pirate/cop/innocent trader in our sights.

## Pitch and roll

													 --------------

						To make it easier to work with the 3D rotations of pitching and rolling, we break down the movement into two separate rotations, the roll and the pitch, and we apply one of them first, and then the other (in Elite, we do the roll first, and then the pitch).

So let's look at the first one: the roll. Imagine we're sitting in our spaceship and do a roll to the right by pressing ">". From our perspective this is the same as the universe doing a roll to the left, so if we're looking out of the front of our ship, and there's a stationary enemy ship at (x, y, z), then rolling by an angle of a will look something like this:

y ^ (x´, y´, z´) | / | / <-. | / a`. | / | | / | / __ (x, y, z) | / __..--'' |/__..--'' +-----------------------> x

So the enemy ship will move from (x, y, z) to (x´, y´, z´) in our little bubble of universe. Moreover, because the enemy ship is stationary, rolling our ship won't change the enemy ship's z-coordinate - it will always be the same distance in front of us, however far we roll. So we know that z´ = z, but how do we calculate x´ and y´?

First, let's ditch the z-coordinate, as we know this doesn't change. This leaves us with a 2D rotation to consider; we are effectively only interested in what happens in the 2D plane at distance z in front of our ship (imagine a cinema screen at distance z, and that's what we're about to draw graphs on).

Now, let's look at the triangle formed by the original (x, y) point:

```
  ^
  |
  |
  |
  |
  |
  |         h       __ (x, y)
  |         __..--''  |
  | __..--''    t     | <------- y
  +----------------------->
       <---- x ---->
```
						In this triangle, let's call the angle at the origin t and the hypotenuse h, and we already know the adjacent side is x and the opposite side is y. If we plug these into the equations for sine and cosine, we get:

cos t = adjacent / hypotenuse = x / h sin t = opposite / hypotenuse = y / h

which gives us the following when we multiply both sides by h:

x = h * cos(t) y = h * sin(t)

(We could use Pythagoras to calculate h from x and y, but we don't need to - you'll see why in a minute.)

Now let's look at the 2D triangle formed by the new, post-roll (x´, y´) point:

^ (x´, y´) | /| | / | | / | | h / | | / | <------- y´ | / | | / | |/ t+a | +-----------------------> <-- x´ -->

In this triangle, the angle is now t + a (as we have rolled left by an angle of a), the hypotenuse is still h (because we're rotating around the origin), the adjacent is x´ and the opposite is y´. If we plug these into the equations for sine and cosine, we get:

cos(t + a) = adjacent / hypotenuse = x´ / h sin(t + a) = opposite / hypotenuse = y´ / h

which gives us the following when we multiply both sides by h:

x´ = h * cos(t + a) (i) y´ = h * sin(t + a) (ii)

We can expand these using the standard trigonometric formulae for compound angles, like this:

```
  x´ = h * cos(t + a)                                   (i)
     = h * (cos(t) * cos(a) - * sin(t) * sin(a))
     = h * cos(t) * cos(a) - h * sin(t) * sin(a)        (iii)
  y´ = h * sin(t + a)                                   (ii)
     = h * (sin(t) * cos(a) + cos(t) * sin(a))
     = h * sin(t) * cos(a) + h * cos(t) * sin(a)        (iv)
```
						and finally we can substitute the values of x and y that we calculated from the first triangle above:

```
  x´ = h * cos(t) * cos(a) - h * sin(t) * sin(a)        (iii)
     = x * cos(a) - y * sin(a)
  y´ = h * sin(t) * cos(a) + h * cos(t) * sin(a)        (iv)
     = y * cos(a) + x * sin(a)
```
						So, to summarise, if we do a roll of angle a, then the ship at (x, y, z) will move to (x´, y´, z´), where:

x´ = x * cos(a) - y * sin(a) y´ = y * cos(a) + x * sin(a) z´ = z

## Transformation matrices

            							 -----------------------

						We can express the exact same thing in matrix form, like this:

[ cos(a) sin(a) 0 ] [ x ] [ x * cos(a) + y * sin(a) ] [ -sin(a) cos(a) 0 ] x [ y ] = [ y * cos(a) - x * sin(a) ] [ 0 0 1 ] [ z ] [ z ]

The matrix on the left is therefore the transformation matrix for rolling through an angle a.

We can apply the exact same process to the pitch rotation, which gives us a transformation matrix for pitching through an angle b, as follows:

[ 1 0 0 ] [ x ] [ x ] [ 0 cos(b) -sin(b) ] x [ y ] = [ y * cos(b) - z * sin(a) ] [ 0 sin(b) cos(b) ] [ z ] [ y * sin(b) + z * cos(b) ]

Finally, we can multiply these two rotation matrices together to get a transformation matrix that applies roll and then pitch in one go:

[ cos(a) sin(a) 0 ] [ x ] [ -sin(a) * cos(b) cos(a) * cos(b) -sin(b) ] x [ y ] [ -sin(a) * sin(b) cos(a) * sin(b) cos(b) ] [ z ]

So, to move our enemy ship in space when we pitch and roll, we simply need to do this matrix multiplication. In 6502 assembly language. In a very small memory footprint. Oh, and it needs to be quick, too, because we're going to be using this routine a lot. Got that?

## Small angle approximation

													 -------------------------

						Luckily we can simplify the maths considerably by applying the "small angle approximation". This states that for small angles in radians, the following approximations hold true:

sin a ~= a cos a ~= 1 - (a^2 / 2) ~= 1 tan a ~= a

These approximations make sense when you look at the triangle geometry that is used to show the ratios of trigonometry, and imagine what happens when the angle gets small; for example, cosine is defined as the adjacent over the hypotenuse, and as the angle tends to 0, the hypotenuse "hinges" down on top of the adjacent, so it's intuitive that cos a tends to 1 for small angles.

The approximations above state that cos a approximates to 1 - (a^2 / 2), but Elite actually uses cos a ~= 1 and corrects for the inaccuracy by regularly calling the TIDY routine to. So dropping the small angle approximations into our rotation calculation above gives the following, much simpler version:

[ 1 a 0 ] [ x ] [ x + ay ] [ -a 1 -b ] x [ y ] = [ y - ax - bz ] [ -ab b 1 ] [ z ] [ z + b(y - ax) ]

So to move rotate a point (x, y, z) around the origin (the centre of our ship) by the current pitch and roll angles (alpha and beta), we just need to calculate these three relatively simple equations:

x -> x + alpha * y y -> y - alpha * x - beta * z z -> z + beta * (y - alpha * x)

There's a fascinating document on Ian Bell's Elite website that shows this exact calculation, in the author's own handwritten notes for the game. You can see it in the third image here:

[http://www.elitehomepage.org/design/](http://www.elitehomepage.org/design/)

just below the original design for the cockpit, before the iconic 3D scanner was added (which is a whole other story...).

## Minsky circles

													 --------------

						So that's what this routine does... it transforms x, y and z when we roll and pitch. But there is a twist. Let's write the transformation equations as you might write them in code (and, indeed this is how the routine itself is structured).

First, we do the roll calculations:

y = y - alpha * x x = x + alpha * y

and then we do the pitch calculations:

y = y - beta * z z = z + beta * y

At first glance this code looks the same as the matrix calculation above, but then you notice that the value of y used in the calculations of x and z is not the original value of y, but the updated value of y. In fact, the above code actually does the following transformation of (x, y, z):

x -> x + alpha * (y - alpha * x) y -> y - alpha * x - beta * z z -> z + beta * (y - alpha * x - beta * z)

Oops, that isn't what we wanted to calculate... except this version turns out to do a better job than our original matrix multiplication above. This new version, where we reuse the updated y in the calculations of x and z instead of the original y, was "invented by mistake when [Marvin Minsky] tried to save one register in a display hack", and inadvertently discovered a way to rotate points within a pretty good approximation of a circle without using complex maths. The method appeared as item 149 in the 1972 HAKMEM memo, and if that doesn't mean anything to you, see if you can take the time to look it up. It's worth the effort if you're interested in this kind of thing (and you're the one reading a commentary on 8-bit code from 1984, so I'm guessing this might include you - though if you're in a hurry, see [page 73 in this PDF](https://elite.bbcelite.com/pdfs/HAKMEM.pdf)).

Anyway, the rotation in Minsky's method doesn't describe a perfect circle, but instead it follows a slightly sheared ellipse, but that's close enough for 8-bit space combat in 192 x 256 pixels. So, coming back to the Elite source code, the MVS4 routine implements the rotation like this (shown here for the nosev orientation vectors, i.e. nosev_x, nosev_y and nosev_z):

Roll calculations:

nosev_y = nosev_y - alpha * nosev_x_hi nosev_x = nosev_x + alpha * nosev_y_hi

Pitch calculations:

nosev_y = nosev_y - beta * nosev_z_hi nosev_z = nosev_z + beta * nosev_y_hi

And that's how we rotate a point around the origin by pitch alpha and roll beta, using the small angle approximation to make the maths easier, and incorporating the Minsky circle algorithm to make the rotation more stable.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
y

  ^         (x´, y´, z´)
  |       /
  |      /    <-.
  |     /       a`.
  |    /          |
  |   /
  |  /              __ (x, y, z)
  | /       __..--''
  |/__..--''
  +-----------------------> x
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
^
  |
  |
  |
  |
  |
  |         h       __ (x, y)
  |         __..--''  |
  | __..--''    t     | <------- y
  +----------------------->
       <---- x ---->
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
cos t = adjacent / hypotenuse = x / h
  sin t = opposite / hypotenuse = y / h
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
x = h * cos(t)
  y = h * sin(t)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
^         (x´, y´)
  |       /|
  |      / |
  |     /  |
  |  h /   |
  |   /    | <------- y´
  |  /     |
  | /      |
  |/ t+a   |
  +----------------------->
  <-- x´ -->
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
cos(t + a) = adjacent / hypotenuse = x´ / h

  sin(t + a) = opposite / hypotenuse = y´ / h
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
x´ = h * cos(t + a)                                   (i)

  y´ = h * sin(t + a)                                   (ii)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
x´ = h * cos(t + a)                                   (i)
     = h * (cos(t) * cos(a) - * sin(t) * sin(a))
     = h * cos(t) * cos(a) - h * sin(t) * sin(a)        (iii)

  y´ = h * sin(t + a)                                   (ii)
     = h * (sin(t) * cos(a) + cos(t) * sin(a))
     = h * sin(t) * cos(a) + h * cos(t) * sin(a)        (iv)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
x´ = h * cos(t) * cos(a) - h * sin(t) * sin(a)        (iii)
     = x * cos(a) - y * sin(a)

  y´ = h * sin(t) * cos(a) + h * cos(t) * sin(a)        (iv)
     = y * cos(a) + x * sin(a)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
x´ = x * cos(a) - y * sin(a)
  y´ = y * cos(a) + x * sin(a)
  z´ = z
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
[  cos(a)  sin(a)  0 ]     [ x ]     [ x * cos(a) + y * sin(a) ]
  [ -sin(a)  cos(a)  0 ]  x  [ y ]  =  [ y * cos(a) - x * sin(a) ]
  [    0       0     1 ]     [ z ]     [            z            ]
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
[ 1    0        0    ]     [ x ]     [            x            ]
  [ 0  cos(b)  -sin(b) ]  x  [ y ]  =  [ y * cos(b) - z * sin(a) ]
  [ 0  sin(b)   cos(b) ]     [ z ]     [ y * sin(b) + z * cos(b) ]
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
[       cos(a)           sin(a)         0    ]     [ x ]
  [ -sin(a) * cos(b)  cos(a) * cos(b)  -sin(b) ]  x  [ y ]
  [ -sin(a) * sin(b)  cos(a) * sin(b)   cos(b) ]     [ z ]
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
sin a ~= a
  cos a ~= 1 - (a^2 / 2) ~= 1
  tan a ~= a
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
[  1   a   0 ]     [ x ]     [    x + ay     ]
  [ -a   1  -b ]  x  [ y ]  =  [ y - ax  - bz  ]
  [ -ab  b   1 ]     [ z ]     [ z + b(y - ax) ]
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
x -> x + alpha * y
  y -> y - alpha * x - beta * z
  z -> z + beta * (y - alpha * x)
```

### Snippet Codice (Dialetto: DASM)

#### Routine Identificate:
- **`http`** (unknown): No description available

```assembly
http://www.elitehomepage.org/design/
```

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
nosev_y = nosev_y - alpha * nosev_x_hi
  nosev_x = nosev_x + alpha * nosev_y_hi
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
nosev_y = nosev_y - beta * nosev_z_hi
  nosev_z = nosev_z + beta * nosev_y_hi
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/pitching_and_rolling.html](https://elite.bbcelite.com/deep_dives/pitching_and_rolling.html)*

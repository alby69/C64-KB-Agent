---
title: Generating system data
source_url: https://elite.bbcelite.com/deep_dives/generating_system_data.html
category: deep-dive
topics:
- memory management
- basic
- assembly
difficulty: beginner
language: mixed
hardware:
- KERNAL
related:
- memory-map
- kernal-routines
scraped_at: '2026-07-14'
---

# Generating system data

## The algorithms behind the procedural generation of system data

The Data on System screen is, under the hood, a work of mathematical art. Every bit of data on that screen is procedurally generated from the system seeds, specifically from parts of s0_hi, s1_hi and s1_lo. This enables the game to produce system data like the following, all from three 16-bit numbers:

![The Data on System screen for Lave in the BBC Micro cassette version of Elite](https://elite.bbcelite.com/images/cassette/data_on_lave.png) 

						For more details on the system seeds see the deep dive on [galaxy and system seeds](https://elite.bbcelite.com/galaxy_and_system_seeds.html), but given a set of seeds, let's see how we can generate the data shown in the Data on System screen, and at the end of the article we'll look at how the system charts are generated, and how the seeds determine the layout of the system's planet and sun for our arrival from hyperspace.

## Summary

													 -------

						The following bits of data are generated in routine [TT24](https://elite.bbcelite.com/cassette/main/subroutine/tt24.html) and are stored in locations QQ3 to QQ7:

| Variable | Contents | Range | 
|---|---|---|
| [QQ3](https://elite.bbcelite.com/cassette/main/workspace/wp.html#qq3) | Economy | 0 to 7 | 
| [QQ4](https://elite.bbcelite.com/cassette/main/workspace/wp.html#qq4) | Government | 0 to 7 | 
| [QQ5](https://elite.bbcelite.com/cassette/main/workspace/wp.html#qq5) | Tech level | 0 to 14 | 
| [QQ6](https://elite.bbcelite.com/cassette/main/workspace/wp.html#qq6) | Population * 10 | 1 to 71 | 
| [QQ7](https://elite.bbcelite.com/cassette/main/workspace/wp.html#qq7) | Productivity | 96 to 62480 | 

The species type and average radius aren't stored anywhere, but are generated on-the-fly in routine [TT25](https://elite.bbcelite.com/cassette/main/subroutine/tt25.html) when displaying the system data.

Let's look at how these bits of data are all generated.

## Economy

													 -------

						The economy is given by a 3-bit value, taken from bits 0-2 of s0_hi. This value determines the prosperity of the economy:

| Bits 0-2 | Decimal | Prosperity | 
|---|---|---|
| %000 or %101 | 0 or 5 | Rich | 
| %001 or %110 | 1 or 6 | Average | 
| %010 or %111 | 2 or 7 | Poor | 
| %011 or %100 | 3 or 4 | Mainly | 

while bit 2 determines the type of economy:

| Bit 2 | Decimal | Economy type | 
|---|---|---|
| %0 | 0 | Industrial | 
| %1 | 1 | Agricultural | 

Putting these two together, we get the following range of economies, which is stored in the QQ28 variable:

| QQ28 | Economy type | 
|---|---|
| 0 | Rich Industrial | 
| 1 | Average Industrial | 
| 2 | Poor Industrial | 
| 3 | Mainly Industrial | 
| 4 | Mainly Agricultural | 
| 5 | Rich Agricultural | 
| 6 | Average Agricultural | 
| 7 | Poor Agricultural | 

If the government is an anarchy or feudal state, we need to fix the economy so it can't be rich (as that wouldn't make sense). We do this by setting bit 1 of the economy value, giving possible values of %010, %011, %110, %111. Looking at the prosperity list above, we can see this forces the economy to be poor, mainly, average, or poor respectively, so there's now a 50% chance of the system being poor, a 25% chance of it being average, and a 25% chance of it being "Mainly Agricultural" or "Mainly Industrial".

The highest economy value is 7 and the lowest is 0.

## Government

													 ----------

						The government is given by a 3-bit value, taken from bits 3-5 of s1_lo, which is stored in the QQ4 variable. This value determine the type of government as follows:

| QQ4 | Government type | 
|---|---|
| 0 | Anarchy | 
| 1 | Feudal | 
| 2 | Multi-government | 
| 3 | Dictatorship | 
| 4 | Communist | 
| 5 | Confederacy | 
| 6 | Democracy | 
| 7 | Corporate State | 

The highest government value is 7 and the lowest is 0.

## Tech level

													 ----------

						The tech level is calculated as follows:

flipped_economy + (s1_hi AND %11) + (government / 2)

where flipped_economy is the economy value with its bits inverted (keeping it as a 3-bit value, so if the economy is %001, flipped_economy is %110). The division is done using LSR and the addition uses ADC, so this rounds up the division for odd-numbered government types.

Flipping the three economy bits gives the following spread of numbers:

| Flipped bits 0-2 | Decimal | Prosperity | 
|---|---|---|
| %111 or %010 | 7 or 2 | Rich | 
| %110 or %001 | 6 or 1 | Average | 
| %101 or %000 | 5 or 0 | Poor | 
| %100 or %011 | 4 or 3 | Mainly | 

This, on average, gives a higher number to rich states compared with poor states, as well as giving higher values to industrial economies compared to agricultural, all of which makes a reasonable basis for a measurement of technology level.

The highest tech level is 7 + 3 + (7 / 2) = 14 (when rounded up) and the lowest is 0. When shown on-screen by the [TT25](https://elite.bbcelite.com/cassette/main/subroutine/tt25.html) routine, this value is incremented to give a tech level range of 1 to 15.

Incidentally, the planet's type depends on its tech level. If bit 1 of the planet's tech level is set then the planet has a crater, otherwise it has a meridian and an equator. This means that planets with tech level ending in %10 or %11 will have craters, so that's 2, 3, 6, 7, 10, 11 or 14. When shown on-screen, this means that planets with tech levels of 3, 4, 7, 8, 11, 12 or 15 will have craters, while tech levels 1, 2, 5, 6, 9, 10, 13 and 14 will have meridians and equators.

## Population

													 ----------

						The population is calculated as follows:

(tech level * 4) + economy + government + 1

This means that systems with higher tech levels, better economies and more stable governments have higher populations, with the tech level having the most influence. The number stored is actually the population * 10 (in billions), so we can display it to one decimal place by calling the pr2 subroutine (so if the population value is 52, it means 5.2 billion).

The highest population is 14 * 4 + 7 + 7 + 1 = 71 (7.1 billion) and the lowest is 1 (0.1 billion).

## Species type

													 ------------

						The species type is either Human Colonials, or it's an alien species that consists of up to three adjectives and a species name (so you can get anything from "Rodents" and "Fierce Frogs" to "Black Fat Felines" and "Small Yellow Bony Lobsters").

As with the rest of the system data, the species is built from various bits in the seeds. Specifically, all the bits in s2_hi are used, along with bits 0-2 of s0_hi and s1_hi, and bit 7 of s2_lo.

First, we check bit 7 of s2_lo. If it is clear, print "Human Colonials" and stop, otherwise this is an alien species, so we move onto the following steps. (In the following steps, the potential range of the calculated value of A is 0-7, and if a match isn't made, nothing is printed for that step.)

- Set A = bits 2-4 of s2_hi
- If A = 0, print "Large "
- If A = 1, print "Fierce "
- If A = 2, print "Small "
- Set A = bits 5-7 of s2_hi
- If A = 0, print "Green "
- If A = 1, print "Red "
- If A = 2, print "Yellow "
- If A = 3, print "Blue "
- If A = 4, print "Black "
- If A = 5, print "Harmless "
- Set A = bits 0-2 of (s0_hi EOR s1_hi)
- If A = 0, print "Slimy "
- If A = 1, print "Bug-Eyed "
- If A = 2, print "Horned "
- If A = 3, print "Bony "
- If A = 4, print "Fat "
- If A = 5, print "Furry "
- Add bits 0-1 of s2_hi to A from step 3, and take bits 0-2 of the result
- If A = 0, print "Rodents "
- If A = 1, print "Frogs "
- If A = 2, print "Lizards "
- If A = 3, print "Lobsters "
- If A = 4, print "Birds "
- If A = 5, print "Humanoids "
- If A = 6, print "Felines "
- If A = 7, print "Insects"

So if we print an adjective at step 3, then the only options for the species name are from A to A + 3 (because we add a 2-bit number) in step 4. So only certain combinations are possible:

- Only rodents, frogs, lizards and lobsters can be slimy
- Only frogs, lizards, lobsters and birds can be bug-eyed
- Only lizards, lobsters, birds and humanoids can be horned
- Only lobsters, birds, humanoids and felines can be bony
- Only birds, humanoids, felines and insects can be fat
- Only humanoids, felines, insects and rodents can be furry

So however hard you look, you will never find slimy humanoids, bony insects, fat rodents or furry frogs, which is probably for the best.

## Gross productivity

													 ------------------

						The gross productivity is calculated as follows:

(flipped_economy + 3) * (government + 4) * population * 8

Productivity is measured in millions of credits, so a productivity of 23740 would be displayed as "23740 M CR".

The highest productivity is 10 * 11 * 71 * 8 = 62480, while the lowest is 3 * 4 * 1 * 8 = 96 (so the range is between 96 and 62480 million credits).

## Average radius

													 --------------

						The average radius is calculated as follows:

((s2_hi AND %1111) + 11) * 256 + s1_hi

The highest average radius is (15 + 11) * 256 + 255 = 6911 km, and the lowest is 11 * 256 = 2816 km.

## System charts

													 -------------

						We also use the system seeds to generate each system's position and appearance on the system charts.

The coordinates of the system on the Long-range Chart are given in s1_hi (for the x-coordinate) and s0_hi (for the y-coordinate). As the galactic chart is half as tall as it is wide, the y-coordinate is halved using a right shift, so the final result is:

Galactic x-coordinate = s1_hi Galactic y-coordinate = s0_hi >> 1

The size of the dot on the Long-range Chart is determined as follows:

s2_lo OR %01010000

This result is passed to the [PIXEL](https://elite.bbcelite.com/cassette/main/subroutine/pixel.html) routine as the ZZ parameter, which draws pixels in these sizes:

- Double-height four-pixel square ZZ < 80
- Single-height two-pixel dash when 80 <= ZZ <= 143
- Single-height one-pixel dot when ZZ > 143

Because the calculation above is always at least 80 (as %01010000 = 80), systems are shown on the chart as single-height one-pixel dots or single-height two-pixel dashes.

The size of the star on the Short-range Chart is determined as follows:

(s2_lo AND %00000001) + 2 + C flag

This will be either 2, 3 or 4, depending on the value of bit 0, and whether the C flag is set. The latter will vary depending on the result of the call to the [cpl](https://elite.bbcelite.com/cassette/main/subroutine/cpl.html) routine, which prints the system name. If cpl returns with the C flag clear then it will be either a small or medium star, and if it returns with the C flag set then it will be either a medium or large star.

## Spawning the planet

													 -------------------

						The seeds also determine the position of the planet in 3D space when we hyperspace to a new system. The position also depends on bit 0 of FIST at the point when we arrive in the system. FIST contains our legal status.

Whenever we arrive in a new system, the [SOLAR](https://elite.bbcelite.com/cassette/main/subroutine/solar.html) starts by shifting the value of FIST to the right by one place, so every time we arrive in a new system, our legal status improves a bit. Bit 0 of FIST shifts out into the C flag, and we use that bit in the following calculation.

In the following, the high and low bytes of the 24-bit space coordinates are all zero, and only the x_sign, y_sign and z_sign bytes are set by the seeds, so the results are (x_sign 0 0), (y_sign 0 0) and (z_sign 0 0).

The space coordinates of the planet are determined as follows:

((s0_hi AND %00000111) + 6 + bit 0 of FIST) >> 1

This value is used for z_sign, the top byte of the planet's coordinate, which is set to (z_sign 0 0).

The above calculation includes a right-shift, which sets the C flag to bit 0 of the result before the shift is performed. To set x_sign and y_sign, we right-rotate the value we just put into z_sign, so that bit 7 is set to the C flag and shifts the rest of z_sign along by one.

For example, s0_hi for Lave is %10101101, so the calculation is:

```
    ((%10101101 AND %00000111) + 6 + bit 0 of FIST) >> 1
  = (%101 + 6 + bit 0 of FIST) >> 1
  = %1011 >> 1   if bit 0 of FIST was clear before we arrived in the system
    %1100 >> 1   if bit 0 of FIST was set before we arrived in the system
```
						So if bit 0 of FIST was clear before we arrived in the system, we get:

z_sign = %1011 >> 1 = %101 = 5 (and this sets the C flag) x_sign = ROR %101 = %10000010 = -2 y_sign = x_sign

and if bit 0 of FIST was set before we arrived in the system, we get:

z_sign = %1100 >> 1 = %110 = 6 (and this clears the C flag) x_sign = ROR %110 = %00000011 = 3 y_sign = x_sign

so the planet Lave is spawned at:

x = -(2 0 0) y = -(2 0 0) z = (5 0 0)

if we arrive there with bit 0 of FIST clear, or:

x = (3 0 0) y = (3 0 0) z = (6 0 0)

if we arrive there with bit 0 of FIST set.

## Spawning the sun

													 ----------------

						The sun's position is also determined by the seeds in the [SOLAR](https://elite.bbcelite.com/cassette/main/subroutine/solar.html) routine, but this calculation is a little simpler.

The z-coordinate of the sun is determined as follows:

(s1_hi AND %00000111) OR %10000001

This value is used for z_sign, the top byte of the sun's coordinate, which is set to (z_sign 0 0). As the above calculation sets bit 7, this ensures the sun is always behind us when we arrive, with the distance ranging from (1 0 0) to (7 0 0).

The x- and y-coordinates of the sun are determined as follows:

s2_hi AND %00000011

This value is used for both x_sign and y_sign, so the sun is either dead centre in our rear laser crosshairs, or off to the top left by a distance of (1 0 0) or (2 0 0) when we look out the back.

For Lave, s1_hi is %00010100 and s2_hi is %00010101, so we have:

z_sign = (%00010100 AND %00000111) OR %10000001 = %10000101 = -5 x_sign = %00010101 AND %00000011 = %01 = 1 y_sign = x_sign

So the sun around Lave is always spawned at:

x = (1 0 0) y = (1 0 0) z = -(5 0 0)

which is a fair distance behind us and slightly off to the top left if we look out of the rear view.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
flipped_economy + (s1_hi AND %11) + (government / 2)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
(tech level * 4) + economy + government + 1
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
(flipped_economy + 3) * (government + 4) * population * 8
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
((s2_hi AND %1111) + 11) * 256 + s1_hi
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
Galactic x-coordinate = s1_hi

  Galactic y-coordinate = s0_hi >> 1
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
s2_lo OR %01010000
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
(s2_lo AND %00000001) + 2 + C flag
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
((s0_hi AND %00000111) + 6 + bit 0 of FIST) >> 1
```

### Snippet Codice (BASIC)

```basic
((%10101101 AND %00000111) + 6 + bit 0 of FIST) >> 1

  = (%101 + 6 + bit 0 of FIST) >> 1

  = %1011 >> 1   if bit 0 of FIST was clear before we arrived in the system

    %1100 >> 1   if bit 0 of FIST was set before we arrived in the system
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
z_sign = %1011 >> 1 = %101 = 5 (and this sets the C flag)

  x_sign = ROR %101 = %10000010 = -2

  y_sign = x_sign
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
z_sign = %1100 >> 1 = %110 = 6 (and this clears the C flag)

  x_sign = ROR %110 = %00000011 = 3

  y_sign = x_sign
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
x = -(2 0 0)
  y = -(2 0 0)
  z =  (5 0 0)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
x = (3 0 0)
  y = (3 0 0)
  z = (6 0 0)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
(s1_hi AND %00000111) OR %10000001
```

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`s2_hi`** (unknown): No description available

```assembly
s2_hi AND %00000011
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
z_sign = (%00010100 AND %00000111) OR %10000001 = %10000101 = -5

  x_sign = %00010101 AND %00000011 = %01 = 1

  y_sign = x_sign
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
x =  (1 0 0)
  y =  (1 0 0)
  z = -(5 0 0)
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/generating_system_data.html](https://elite.bbcelite.com/deep_dives/generating_system_data.html)*

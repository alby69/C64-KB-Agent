---
title: The I.F.F. system
source_url: https://elite.bbcelite.com/deep_dives/elite-a_the_iff_system.html
category: deep-dive
topics:
- memory management
- assembly
- basic
difficulty: intermediate
language: mixed
hardware:
- KERNAL
related:
- memory-map
- kernal-routines
scraped_at: '2026-07-20'
---

# The I.F.F. system

## Friend or foe? Adding ship information to the 3D scanner

One of the most interesting features that Angus Duggan added to Elite-A is the I.F.F. system, which is an optional upgrade to the 3D scanner. In the original disc version of Elite, missiles are shown on the scanner in yellow (or white if we have an escape pod fitted), while all other ships are shown in green (or cyan with an escape pod). Apart from the location of each ship, there isn't any other information available, so there is no way of telling whether we are looking at an asteroid, a peaceful trader, a violent pirate or a vengeful cop.

The "Identification Friend or Foe" system (I.F.F. for short) upgrades the scanner to show a lot more information about what's actually out there. At the same time, the standard scanner is downgraded so it no longer shows missiles in a different colour, so there's quite an incentive to upgrade when you get the chance.

To show this new information, the I.F.F. system adds stripes to the sticks on the scanner, to help us distinguish potentially aggressive ships from friendly ones. The I.F.F. colours for the normal dashboard palette are:

| Index | Dot colour | Stick colour(s) | Ship types | 
|---|---|---|---|
| 0 | Green | Green | Clean | 
| 1 | Yellow | Yellow | Station tracked | 
| 2 | Green | Green and yellow | Debris | 
| 3 | Yellow | Yellow and red | Missile | 
| 4 | Green | Green and red | Offender/fugitive | 

while the colours for the escape pod dashboard palette are:

| Index | Dot colour | Stick colour(s) | Ship types | 
|---|---|---|---|
| 0 | Cyan | Cyan | Clean | 
| 1 | White | White | Station tracked | 
| 2 | Cyan | Cyan and white | Debris | 
| 3 | White | White and red | Missile | 
| 4 | Cyan | Cyan and red | Offender/fugitive | 

If the I.F.F. system is not fitted, all ships are shown using the clean colour (i.e. green or cyan), including missiles. See the next section for a breakdown of what constitutes station-tracked ships and debris.

Let's take a look at how Angus added these colour schemes to the normal 3D scanner.

## Base colours and EOR values

													 ---------------------------

						First of all, the [SCAN](https://elite.bbcelite.com/elite-a/flight/subroutine/scan.html) routine has been modified in Elite-A to support different colours for both the dot and the stick, by introducing two colours for each ship on the scanner - the base colour and the EOR value. The base colour is the colour of the dot and the colour of one of the stripes in the stick, while the EOR value is applied to the base colour to give the colour of the other stripe in the stick. This second colour is obtained by EOR'ing the base colour with the EOR value, so if the EOR value is 0, the stick doesn't have stripes and is all in the base colour, as n EOR 0 = n.

So the first task we have when drawing a ship on the I.F.F. system is to determine the base colour and EOR value, depending on the type and status of the ship. This logic is implemented in the [iff_index](https://elite.bbcelite.com/elite-a/loader/subroutine/iff_index.html) routine, which returns an index value as follows:

- Clean = innocent trader or innocent bounty hunter
- Station tracked = cop, space station or escape pod
- Debris = cargo canister, alloy plate, asteroid, boulder or splinter
- Missile
- Offender/fugitive = pirate or non-innocent bounty hunter

If there is no I.F.F. system fitted, the index returned is always 0, the same as for a clean ship.

We now use the returned index as an offset into two tables, first to fetch the base colour from the [iff_base](https://elite.bbcelite.com/elite-a/flight/variable/iff_base.html) table, and then to fetch the EOR value from the [iff_xor](https://elite.bbcelite.com/elite-a/flight/variable/iff_xor.html) table. The base colour table simply contains the mode 5 colour byte for that type of ship, but the EOR value is rather more complex, so let's look at that in more detail.

## Adding stripes to the stick

													 ---------------------------

						The EOR values in the [iff_xor](https://elite.bbcelite.com/elite-a/flight/variable/iff_xor.html) table have the following effect on the colour of the stick:
						

| Value | Effect | 
|---|---|
| %00000000 | Stick is a solid colour, in the base colour | 
| %00001111 | Stick is striped, in the base colour and base colour EOR %01 | 
| %11110000 | Stick is striped, in the base colour and base colour EOR %10 | 
| %11111111 | Stick is striped, in the base colour and base colour EOR %11 | 

Let's take the example of debris, which has an index of 2 from the iff_index routine. We therefore fetch the base colour from iff_base + 2, which is &FF. This is %11111111, or a four-pixel byte of colour %11, or colour 3 in mode 5, or green/cyan (green for the normal palette, cyan in the escape pod palette). So far so good.

We now look up the EOR value from iff_xor + 2, which is &0F. This is %00001111, or a four-pixel mode 5 byte of %01 values. Applying this EOR to the base colour (%11) gives:

%11 EOR %01 = %10 = 2

and colour 2 in mode 5 is yellow/white (yellow for the normal palette, white in the escape pod palette). So the stick colour for debris when we have an I.F.F. system fitted is:

Green/cyan (the base colour) striped with yellow/white (the colour after applying the EOR value)

If there is no I.F.F. system fitted, the index is 0 and the EOR value is 0, which doesn't affect the default colour.

In this way, the I.F.F. system adds quite a bit of useful information to the scanner without breaking the scanner's iconic design. When you're jumping your way through a new system, it's really useful to know whether you just ran into a family of green traders, a field of green and yellow asteroids, a criminal-seeking bunch of yellow cops... or, worst of all, a rabid pack of green and red pirates firing off yellow and red missiles. Getting a heads-up can make the difference between a successful trip, and a one-way ticket into the cold, hard vacuum of space...

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
%11 EOR %01 = %10 = 2
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
Green/cyan (the base colour)
  striped with yellow/white (the colour after applying the EOR value)
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/elite-a_the_iff_system.html](https://elite.bbcelite.com/deep_dives/elite-a_the_iff_system.html)*

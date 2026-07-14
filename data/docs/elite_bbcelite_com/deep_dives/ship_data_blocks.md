---
title: Ship data blocks
source_url: https://elite.bbcelite.com/deep_dives/ship_data_blocks.html
category: source-code
topics:
- sprite programming
- memory management
- assembly
difficulty: intermediate
language: assembly
hardware:
- SID
- CIA
related:
- cia-registers
- keyboard-handling
- sound-programming
- music-player
- raster-interrupts
- joystick-reading
- sprite-programming
- vic-ii-registers
- sid-registers
scraped_at: '2026-07-14'
---

# Ship data blocks

## Storing data for each of the ships in the local bubble of universe

As described in the deep dive on [the local bubble of universe](https://elite.bbcelite.com/the_local_bubble_of_universe.html), every ship in the local bubble has its own set of associated data structures. One of these is the ship data block, stored in the [K% workspace](https://elite.bbcelite.com/cassette/main/workspace/k_per_cent.html), and that's what we're going to look at in this article.

The ship data block contains information about the ship's status, its location in space, its orientation and so on. Each ship in the local bubble also has an entry in the lookup table at [UNIV](https://elite.bbcelite.com/cassette/main/variable/univ.html) that points to its data block in K%, and along with the ship slots at [FRIN](https://elite.bbcelite.com/cassette/main/workspace/wp.html#frin) and the ship blueprints at [XX21](https://elite.bbcelite.com/cassette/main/variable/xx21.html), we have everything we need to simulate the world of Elite (see the deep dive on [the local bubble of universe](https://elite.bbcelite.com/the_local_bubble_of_universe.html) for details of the ship slots and how they work).

For example, here's a screenshot of the [Elite Universe Editor](https://elite.bbcelite.com/hacks/elite_universe_editor.html), which allows you to edit the ships in the local bubble:

![The ship ID poster in Elite Universe Editor](https://elite.bbcelite.com/images/elite_universe_editor/ship_id.png) 

						Each of these ships, including the planet, has its own data block that describes where the ship is in space, the direction it's pointing in, and so on. But before we go any further, let's talk about the terminology we're going to use when describing ships and ship data blocks.

## Ship data terminology

													 ---------------------

						Throughout this documentation, we're going to refer to "ships" and "ship data blocks" for all the different object types in the vicinity, not just ships. The same blocks, pointers and data structures are used not only for ships, but also for cargo canisters, missiles, escape pods, asteroids, space stations, planets and suns, but that's a bit of a mouthful compared to "ships", so "ships" it is.

When working with a ship's data - such as when we move a ship in MVEIT, or spawn a child ship in SFS1 - we normally work with the data in the [INWK](https://elite.bbcelite.com/cassette/main/workspace/zp.html#inwk) workspace, as INWK is in zero page and is therefore faster and more memory efficient to manipulate. The ship data blocks in the K% workspace are therefore copied into INWK before they are worked on, and new ship blocks are created in INWK before being copied to K%. As a result, the layout of the INWK data block is identical the layout of each ship data block in K%.

Note that in the NES version, each ship data block at K% has four extra bytes. Bytes #37 to #40 of the ship data block are used to store the random seeds for the ship's explosion cloud, though they aren't copied to INWK, which stays the same size. The rest of the ship block is the same.

It's also important to note that INWK is known as XX1 in some parts of the codebase, namely those parts that were written by David Braben on his Acorn Atom, where he was only allowed to use label names starting with two letters, followed by numbers (this is why the source code is full of catchy labels like TT26 and LL9). Because we might end up talking about ship data in INWK, K% or XX1, this commentary refers to "ship byte #5" for byte #5 of the ship data (y_sign), or "ship byte #32" for byte #32 (the AI flag), and so on. Most of the time we will be working with INWK or XX1, but every now and then the bytes in the K% block are manipulated directly, which we will point out in the comments.

There are 36 bytes of data in each ship's block, and as mentioned above, they all have the same format, though not all bytes are used for all ship types. Planets, for example, don't have AI or missiles, though it would be fun if they did...

Let's take a look at the format of a typical ship data block.

## Summary of the ship data block format

													 -------------------------------------

						The bytes in each ship data block are arranged as follows:

| Byte # | Description | 
|---|---|
| #0-2 | Ship's x-coordinate in space = (x_sign x_hi x_lo) | 
| #3-5 | Ship's y-coordinate in space = (y_sign y_hi y_lo) | 
| #6-8 | Ship's z-coordinate in space = (z_sign z_hi z_lo) | 
| #9-14 | Orientation vector nosev = [ nosev_x nosev_y nosev_z ] | 
| #15-19 | Orientation vector roofv = [ roofv_x roofv_y roofv_z ] | 
| #21-26 | Orientation vector sidev = [ sidev_x sidev_y sidev_z ] | 
| #27 | Speed | 
| #28 | Acceleration | 
| #29 | Roll counter | 
| #30 | Pitch counter | 
| #31 | Exploding state Killed state "Is being drawn on-screen" flag "Is visible on the scanner" flag Missile count | 
| #32 | AI flag Aggression level Hostility flag (stations and missiles only) E.C.M. flag | 
| #33-34 | Ship line heap address pointer (non-NES versions) | 
| #33 | The number of the ship on the scanner (NES version) | 
| #34 | The cloud counter for the explosion cloud (NES version) | 
| #35 | Energy level | 
| #36 | [NEWB flags](https://elite.bbcelite.com/deep_dives/advanced_tactics_with_the_newb_flags.html)(enhanced versions only) | 

Note that in the NES version, INWK+33 and INWK+34 are no longer used to store the ship line heap address, as the NES doesn't have a ship line heap (as ships don't need to be erased line-by-line in that version). Instead INWK+33 contains the number of the ship on the scanner, and INWK+34 contains the cloud counter for the explosion cloud.

Let's look at these in more detail.

## Ship coordinates (bytes #0-8)

													 -----------------------------

						These bytes contain the ship's location in space relative to our ship. The x-axis goes to the right, the y-axis goes up and the z-axis goes into the screen.

| Byte # | Description | 
|---|---|
| #0 | x_lo | 
| #1 | x_hi | 
| #2 | x_sign | 

| Byte # | Description | 
|---|---|
| #3 | y_lo | 
| #4 | y_hi | 
| #5 | y_sign | 

| Byte # | Description | 
|---|---|
| #6 | z_lo | 
| #7 | z_hi | 
| #8 | z_sign | 

The coordinates are stored as 24-bit sign-magnitude numbers, where the sign of the number is stored in bit 7 of the sign byte, and the other 23 bits contain the magnitude of the number without any sign (i.e. the absolute values |x|, |y| and |z|).

We can also write the coordinates like this:

- x-coordinate = (x_sign x_hi x_lo) = INWK(2 1 0)
- y-coordinate = (y_sign y_hi y_lo) = INWK(5 4 3)
- z-coordinate = (z_sign z_hi z_lo) = INWK(8 7 6)

## Orientation vectors (bytes #9-26)

													 ---------------------------------

						The ship's orientation vectors determine its orientation in space. There are three vectors, named according to the direction they point in (i.e. out of the ship's nose, the ship's roof, or the ship's right side):

| Byte # | Description | 
|---|---|
| #9 | nosev_x_lo | 
| #10 | nosev_x_hi | 
| #11 | nosev_y_lo | 
| #12 | nosev_y_hi | 
| #13 | nosev_z_lo | 
| #14 | nosev_z_hi | 

| Byte # | Description | 
|---|---|
| #15 | roofv_x_lo | 
| #16 | roofv_x_hi | 
| #17 | roofv_y_lo | 
| #18 | roofv_y_hi | 
| #19 | roofv_z_lo | 
| #20 | roofv_z_hi | 

| Byte # | Description | 
|---|---|
| #21 | sidev_x_lo | 
| #22 | sidev_x_hi | 
| #23 | sidev_y_lo | 
| #24 | sidev_y_hi | 
| #25 | sidev_z_lo | 
| #26 | sidev_z_hi | 

The vector coordinates are stored as 16-bit sign-magnitude numbers, where the sign of the number is stored in bit 7 of the high byte. See the deep dive on [orientation vectors](https://elite.bbcelite.com/orientation_vectors.html) for more information.

## Ship movement (bytes #27-30)

													 ----------------------------

						This block controls the ship's movement in space.

| Byte # | Description | 
|---|---|
| #27 | Speed, in the range 1-40 | 
| #28 | Acceleration, which gets added to the speed once, in MVEIT, before being zeroed again | 
| #29 | Roll counter Bits 0-6 = The counter. If this is 127 (%1111111) then damping is disabled and the ship keeps rolling forever, otherwise damping is enabled and the counter reduces by 1 for every iteration of the main flight loop. The ship rolls by a fixed amount (1/16 radians, or 3.6 degrees) for every iteration where the counter is greater than 0.Bit 7 = The direction of roll (a positive roll counter rolls the ship clockwise, a negative roll counter rolls it anti-clockwise)
 | 
| #30 | Pitch counter Bits 0-6 = The counter. If this is 127 (%1111111) then damping is disabled and the ship keeps pitching forever, otherwise damping is enabled and the counter reduces by 1 for every iteration of the main flight loop. The ship pitches by a fixed amount (1/16 radians, or 3.6 degrees) for every iteration where the counter is greater than 0.Bit 7 = The direction of pitch (a positive pitch counter makes the ship dive, a negative pitch counter makes the ship climb)
 | 

See the deep dive on [pitching and rolling by a fixed angle](https://elite.bbcelite.com/pitching_and_rolling_by_a_fixed_angle.html) for more details on the pitch and roll that the above counters apply to a ship.

## Ship flags (bytes #31-32)

													 -------------------------

						These two flags contain a lot of information about the ship, and they are consulted often.

| Byte # | Description | 
|---|---|
| #31 | Exploding state Killed state "Is being drawn on-screen" flag "Is visible on the scanner" flag Missile count Bits 0-2: %nnn = number of missiles or Thargons (maximum 7)Bit 3: 0 = isn't currently being drawn on-screen1 = is currently being drawn on-screen
Bit 4: 0 = don't show on scanner1 = do show on scanner
Bit 5: 0 = ship is not exploding1 = ship is exploding
Bit 6: 0 = ship is not firing lasers1 = ship is firing lasers
 0 = explosion has not been drawn
 1 = explosion has been drawn
Bit 7: 0 = ship has not been killed1 = ship has been killed
 | 
| #32 | AI flag Aggression level Hostility flag (stations and missiles only) E.C.M. flag For ships:
										Bit 0: 0 = no E.C.M.1 = has E.C.M.
Bits 1-6: %nnnnnn = aggression level (0 to 63)(see
 [TACTICS part 7](https://elite.bbcelite.com/cassette/main/subroutine/tactics_part_7_of_7.html))Bit 7: 0 = dumb1 = AI enabled (apply
 [TACTICS](https://elite.bbcelite.com/cassette/main/subroutine/tactics_part_2_of_7.html)to ship)
Bit 0: 0 = no E.C.M.For the space station:
										Bit 0: 1 = has E.C.M. (always set for the station)Bit 7: 0 = friendly (BBC cassette and Electron versions)dumb (enhanced versions)
 1 = hostile (BBC cassette and Electron versions)
 AI enabled (enhanced versions, apply
 [TACTICS](https://elite.bbcelite.com/cassette/main/subroutine/tactics_part_2_of_7.html))
For missiles:
										Bit 0: 0 = no lock/launched1 = target locked
Bits 1-5: %nnnnn = target's slot numberBit 6: 0 = friendly1 = hostile
Bit 7: 0 = dumb1 = AI enabled (apply
 [TACTICS](https://elite.bbcelite.com/cassette/main/subroutine/tactics_part_2_of_7.html)to missile)
Bit 0: 0 = no lock/launched
 | 

## Heap pointer and energy (bytes #33-35)

													 --------------------------------------

						The final three bytes are as follows:

| Byte # | Description | 
|---|---|
| #33 | Low byte of ship line heap address pointer in INWK(34 33) | 
| #34 | High byte of ship line heap address pointer in INWK(34 33) | 
| #35 | Ship energy | 

In the NES version, there is no ship line heap, so the first two bytes are repurposed:

| Byte # | Description | 
|---|---|
| #33 | The number of the ship on the scanner | 
| #34 | The cloud counter for the explosion cloud | 

## NEWB flags (byte #36)

													 ---------------------

						The enhanced versions of Elite have a much more sophisticated tactics routine than the original BBC Micro cassette and Acorn Electron versions. At the core of this advanced routine is the set of NEWB flags, which were added to the cassette version as it grew into the disc version. The NEWB flags live in byte #36 of the ship data block.

For details of the NEWB flags, see the deep dive on [advanced tactics with the NEWB flags](https://elite.bbcelite.com/deep_dives/advanced_tactics_with_the_newb_flags.html).

---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/ship_data_blocks.html](https://elite.bbcelite.com/deep_dives/ship_data_blocks.html)*

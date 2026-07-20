---
title: Ship blueprints
source_url: https://elite.bbcelite.com/deep_dives/ship_blueprints.html
category: source-code
topics:
- assembly
- graphics
difficulty: intermediate
language: assembly
hardware:
- KERNAL
- SID
- CPU
related:
- sid-registers
- sound-programming
- memory-map
- kernal-routines
- music-player
scraped_at: '2026-07-20'
---

# Ship blueprints

## Specifications for all the different types of ship in the universe

Every ship in Elite has a blueprint that defines that ship's characteristics (note that in this context, "ship" refers not only to ships, but also cargo canisters, space stations, escape pods, missiles and asteroids). These blueprints are the in-game equivalent of the last section of the Space Trader's Flight Training Manual - a real life version of the Observer's Guide to Ships in Service.

This is such an important aspect of Elite that the original game came with a poster showing the range of ships available in the BBC Micro cassette version:

![The ship identification poster](https://elite.bbcelite.com/images/elite_universe_editor/ship_id.jpg) 

						In this article we take a look at how ship blueprints are implemented in Elite. If you want to see how the different ship specifications compare to each other, then see the deep dive on [comparing ship specifications](https://elite.bbcelite.com/comparing_ship_specifications.html), and to see exactly how large these ships are, see the deep dive on [a sense of scale](https://elite.bbcelite.com/a_sense_of_scale.html).

## Ship blueprints

													 ---------------

						There is a lookup table at [XX21](https://elite.bbcelite.com/cassette/main/variable/xx21.html) that contains the addresses of all the ship blueprints used in the game. Ship type 1 (the Sidewinder at [SHIP_SIDEWINDER](https://elite.bbcelite.com/cassette/main/variable/ship_sidewinder.html)) is first in the table, then ship type 2 (the Viper at [SHIP_VIPER](https://elite.bbcelite.com/cassette/main/variable/ship_viper.html)) is next, and so on up to ship type 13 (the escape pod at [SHIP_ESCAPE_POD](https://elite.bbcelite.com/cassette/main/variable/ship_escape_pod.html)). For all ships except the Python, the blueprints themselves are stored in sequence just after the table; the Python is stored at [SHIP_PYTHON](https://elite.bbcelite.com/cassette/main/variable/ship_python.html), just above screen memory at &7F00.

There are 13 ship types in the BBC Micro cassette version, though the two Cobra Mk III entries share the same ship blueprint, so there are only 12 distinct ship designs. Here they are, along with the corresponding configuration variables where they exist:

| # | Ship | Configuration variable | 
|---|---|---|
| 1 | [Sidewinder](https://elite.bbcelite.com/cassette/main/variable/ship_sidewinder.html) | - | 
| 2 | [Viper](https://elite.bbcelite.com/cassette/main/variable/ship_viper.html) | COPS | 
| 3 | [Mamba](https://elite.bbcelite.com/cassette/main/variable/ship_mamba.html) | - | 
| 4 | [Python](https://elite.bbcelite.com/cassette/main/variable/ship_python.html) | - | 
| 5 | [Cobra Mk III (bounty hunter)](https://elite.bbcelite.com/cassette/main/variable/ship_cobra_mk_3.html) | - | 
| 6 | [Thargoid](https://elite.bbcelite.com/cassette/main/variable/ship_thargoid.html) | THG | 
| 7 | [Cobra Mk III (trader)](https://elite.bbcelite.com/cassette/main/variable/ship_cobra_mk_3.html) | CYL | 
| 8 | [Coriolis station](https://elite.bbcelite.com/cassette/main/variable/ship_coriolis.html) | SST | 
| 9 | [Missile](https://elite.bbcelite.com/cassette/main/variable/ship_missile.html) | MSL | 
| 10 | [Asteroid](https://elite.bbcelite.com/cassette/main/variable/ship_asteroid.html) | AST | 
| 11 | [Canister](https://elite.bbcelite.com/cassette/main/variable/ship_canister.html) | OIL | 
| 12 | [Thargon](https://elite.bbcelite.com/cassette/main/variable/ship_thargon.html) | TGL | 
| 13 | [Escape pod](https://elite.bbcelite.com/cassette/main/variable/ship_escape_pod.html) | ESC | 

The Acorn Electron list is slightly smaller, as there are no Thargoids in this version, and again the two Cobras share a blueprint:

| # | Ship | Configuration variable | 
|---|---|---|
| 1 | [Sidewinder](https://elite.bbcelite.com/electron/main/variable/ship_sidewinder.html) | - | 
| 2 | [Viper](https://elite.bbcelite.com/electron/main/variable/ship_viper.html) | COPS | 
| 3 | [Mamba](https://elite.bbcelite.com/electron/main/variable/ship_mamba.html) | - | 
| 4 | [Python](https://elite.bbcelite.com/electron/main/variable/ship_python.html) | - | 
| 5 | [Cobra Mk III (bounty hunter)](https://elite.bbcelite.com/electron/main/variable/ship_cobra_mk_3.html) | - | 
| 6 | [Cobra Mk III (trader)](https://elite.bbcelite.com/electron/main/variable/ship_cobra_mk_3.html) | CYL | 
| 7 | [Coriolis station](https://elite.bbcelite.com/electron/main/variable/ship_coriolis.html) | SST | 
| 8 | [Missile](https://elite.bbcelite.com/electron/main/variable/ship_missile.html) | MSL | 
| 9 | [Asteroid](https://elite.bbcelite.com/electron/main/variable/ship_asteroid.html) | AST | 
| 10 | [Canister](https://elite.bbcelite.com/electron/main/variable/ship_canister.html) | OIL | 
| 11 | [Escape pod](https://elite.bbcelite.com/electron/main/variable/ship_escape_pod.html) | ESC | 

The other versions of 6502 Elite - BBC Micro disc, 6502 Second Processor, Commodore 64, Apple II, BBC Master and NES - contain rather more ships. Here's the full list, though note that the Elite logo only appears in the 6502 Second Processor version, the Apple II version doesn't include the Cougar, and the BBC Micro disc version doesn't include the rock hermit or the Cougar:

| # | Ship | Configuration variable | 
|---|---|---|
| 1 | [Missile](https://elite.bbcelite.com/6502sp/main/variable/ship_missile.html) | MSL | 
| 2 | [Coriolis station](https://elite.bbcelite.com/6502sp/main/variable/ship_coriolis.html) | SST | 
| 3 | [Escape pod](https://elite.bbcelite.com/6502sp/main/variable/ship_escape_pod.html) | ESC | 
| 4 | [Alloy plate](https://elite.bbcelite.com/6502sp/main/variable/ship_plate.html) | PLT | 
| 5 | [Canister](https://elite.bbcelite.com/6502sp/main/variable/ship_canister.html) | OIL | 
| 6 | [Boulder](https://elite.bbcelite.com/6502sp/main/variable/ship_boulder.html) | - | 
| 7 | [Asteroid](https://elite.bbcelite.com/6502sp/main/variable/ship_asteroid.html) | AST | 
| 8 | [Splinter](https://elite.bbcelite.com/6502sp/main/variable/ship_splinter.html) | SPL | 
| 9 | [Shuttle](https://elite.bbcelite.com/6502sp/main/variable/ship_shuttle.html) | SHU | 
| 10 | [Transporter](https://elite.bbcelite.com/6502sp/main/variable/ship_transporter.html) | - | 
| 11 | [Cobra Mk III](https://elite.bbcelite.com/6502sp/main/variable/ship_cobra_mk_3.html) | CYL | 
| 12 | [Python](https://elite.bbcelite.com/6502sp/main/variable/ship_python.html) | - | 
| 13 | [Boa](https://elite.bbcelite.com/6502sp/main/variable/ship_boa.html) | - | 
| 14 | [Anaconda](https://elite.bbcelite.com/6502sp/main/variable/ship_anaconda.html) | ANA | 
| 15 | [Rock hermit](https://elite.bbcelite.com/6502sp/main/variable/ship_rock_hermit.html) | HER | 
| 16 | [Viper](https://elite.bbcelite.com/6502sp/main/variable/ship_viper.html) | COPS | 
| 17 | [Sidewinder](https://elite.bbcelite.com/6502sp/main/variable/ship_sidewinder.html) | SH3 | 
| 18 | [Mamba](https://elite.bbcelite.com/6502sp/main/variable/ship_mamba.html) | - | 
| 19 | [Krait](https://elite.bbcelite.com/6502sp/main/variable/ship_krait.html) | KRA | 
| 20 | [Adder](https://elite.bbcelite.com/6502sp/main/variable/ship_adder.html) | ADA | 
| 21 | [Gecko](https://elite.bbcelite.com/6502sp/main/variable/ship_gecko.html) | - | 
| 22 | [Cobra Mk I](https://elite.bbcelite.com/6502sp/main/variable/ship_cobra_mk_1.html) | - | 
| 23 | [Worm](https://elite.bbcelite.com/6502sp/main/variable/ship_worm.html) | WRM | 
| 24 | [Cobra Mk III (pirate)](https://elite.bbcelite.com/6502sp/main/variable/ship_cobra_mk_3_p.html) | CYL2 | 
| 25 | [Asp Mk II](https://elite.bbcelite.com/6502sp/main/variable/ship_asp_mk_2.html) | ASP | 
| 26 | [Python (pirate)](https://elite.bbcelite.com/6502sp/main/variable/ship_python_p.html) | - | 
| 27 | [Fer-de-lance](https://elite.bbcelite.com/6502sp/main/variable/ship_fer_de_lance.html) | - | 
| 28 | [Moray](https://elite.bbcelite.com/6502sp/main/variable/ship_moray.html) | - | 
| 29 | [Thargoid](https://elite.bbcelite.com/6502sp/main/variable/ship_thargoid.html) | THG | 
| 30 | [Thargon](https://elite.bbcelite.com/6502sp/main/variable/ship_thargon.html) | TGL | 
| 31 | [Constrictor](https://elite.bbcelite.com/6502sp/main/variable/ship_constrictor.html) | CON | 
| 32 | [Elite logo](https://elite.bbcelite.com/6502sp/main/variable/ship_logo.html) | LGO | 
| 33 | [Cougar](https://elite.bbcelite.com/6502sp/main/variable/ship_cougar.html) | COU | 
| 34 | [Dodo station](https://elite.bbcelite.com/6502sp/main/variable/ship_dodo.html) | DOD | 

Each ship blueprint defines a whole range of attributes, such as the ship's maximum speed, the number of missiles it can carry, and the size of the target area we need to hit with our laser. It also contains data that's used when managing the ship once it's spawned inside our local bubble of universe, like the maximum size of the ship line heap.

The blueprint also contains all the data we need to draw the ship on-screen. This includes the ship's vertices, edges and faces, the visibility distances, and the face normal scale factor, all of which are used in the ship drawing routine at LL9. See the deep dive on [drawing ships](https://elite.bbcelite.com/drawing_ships.html) for more details.

## Ship characteristics

													 --------------------

						For each ship blueprint, the first 20 bytes define the main characteristics of this ship type. They are as follows:

| Byte # | Description | 
|---|---|
| #0 | Maximum number of cargo canisters released when destroyed | 
| #1-2 | The ship's targetable area, which represents how far the ship can be from the centre of our crosshairs and still be locked onto by our missiles or hit by our lasers, as described in the HITCH routine (16-bit value, 1 = low byte, 2 = high byte) | 
| #3 | Edges data offset low byte (offset is from byte #0) | 
| #4 | Faces data offset low byte (offset is from byte #0) | 
| #5 | Maximum heap size for plotting ship = 1 + 4 * max. no of visible edges | 
| #6 | Number * 4 of the vertex used for the ship's laser position, for when the ship fires its lasers | 
| #7 | Explosion count = 4 * n + 6, where n = number of vertices used as origins for explosion clouds | 
| #8 | Number of vertices * 6 | 
| #9 | Number of edges | 
| #10-11 | The bounty awarded for the destruction of this ship in Cr * 10 (16-bit little-endian value, 10 = low byte, 11 = high byte) | 
| #12 | Number of faces * 4 | 
| #13 | Visibility distance, beyond which we show the ship as a dot | 
| #14 | Maximum energy/shields | 
| #15 | Maximum speed | 
| #16 | Edges data offset high byte (can be negative and point to another ship's edge net) | 
| #17 | Faces data offset high byte | 
| #18 | Face normals are scaled down by 2 ^ this value to enable us to store more accurate fractional data in the table | 
| #19 | %00 lll mmm, where: Bits 0-2 = number of missilesBits 3-5 = laser power
 | 

## Vertex definitions

													 ------------------

						Next come the vertex definitions. Each vertex is made up of eight values stored in six bytes, as follows:

| Byte # | Description | 
|---|---|
| #0 | Magnitude of the vertex's x-coordinate, with the origin in the middle of the ship | 
| #1 | Magnitude of the vertex's y-coordinate | 
| #2 | Magnitude of the vertex's z-coordinate | 
| #3 | %xyz vvvvv, where: Bits 0-4 = visibility distance, beyond which the vertex is not shownBits 7-5 = the sign bits of x, y and z
 | 
| #4 | %ffff ffff, where: Bits 0-3 = the number of face 1Bits 4-7 = the number of face 2
 | 
| #5 | %ffff ffff, where: Bits 0-3 = the number of face 3Bits 4-7 = the number of face 4
 | 

## Edge definitions

													 ----------------

						Then we have the edge definitions. Each edge is made up of five values stored in four bytes, as follows:

| Byte # | Description | 
|---|---|
| #0 | Visibility distance, beyond which the edge is not shown | 
| #1 | %ffff ffff, where: Bits 0-3 = the number of face 1Bits 4-7 = the number of face 2
 | 
| #2 | The number of the vertex at the start of the edge | 
| #3 | The number of the vertex at the end of the edge | 

## Face definitions

													 ----------------

						Finally we have the face definitions. Each face is made up of four values stored in four bytes, as follows. Note that the visibility distance works in the opposite way for faces than for the ship, vertices and edges, in that the face is always shown when it's further away than the visibility distance.

| Byte # | Description | 
|---|---|
| #0 | %xyz vvvvv, where: Bits 0-4 = visibility distance, beyond which the face is always shownBits 7-5 = the sign bits of normal_x, normal_y and normal_z
 | 
| #1 | Magnitude of the face normal's x-coordinate, normal_x | 
| #2 | Magnitude of the face normal's y-coordinate, normal_y | 
| #3 | Magnitude of the face normal's z-coordinate, normal_z | 

To make the source code easier to follow, we use three macros (called VERTEX, EDGE and FACE) that let us separate out the different values, and which squash the data into the above bytes at compile time.

---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/ship_blueprints.html](https://elite.bbcelite.com/deep_dives/ship_blueprints.html)*

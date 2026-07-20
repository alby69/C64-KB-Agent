---
title: Comparing ship specifications
source_url: https://elite.bbcelite.com/deep_dives/comparing_ship_specifications.html
category: source-code
topics:
- assembly
difficulty: beginner
language: assembly
hardware:
- KERNAL
- SID
- CPU
- CIA
related:
- sid-registers
- sound-programming
- joystick-reading
- keyboard-handling
- kernal-routines
- memory-map
- music-player
- cia-registers
scraped_at: '2026-07-20'
---

# Comparing ship specifications

## A detailed comparison of in-game statistics for the different ships in Elite

Here's a comparison of all the different ships in Elite, using the values from within the source code. There is a lot of information, so I have split it up into a number of tables (click a link to jump that table):

- [Table 1: Ship hardware](https://elite.bbcelite.com#hardware)
- [Table 2: Ship wireframes](https://elite.bbcelite.com#wireframes)
- [Table 3: Ship dimensions](https://elite.bbcelite.com#dimensions)
- [Table 4: Ship spawning](https://elite.bbcelite.com#spawning)
- [Table 5: Ship colours](https://elite.bbcelite.com#colours)

The tables include every ship that you can meet in-flight in the official game, so they don't include the Elite logo from the 6502 Second Processor version, the hanger blueprints from the docked code in the BBC Micro disc version, or any ships from Elite-A. To find out how large these ships are in-game, see the deep dive on [a sense of scale](https://elite.bbcelite.com/a_sense_of_scale.html).

Note that the tables are pretty wide - to see all the different attributes, you may need to scroll the window to the right.


													 ----------------------

						The following table contains the hardware specifications for each ship. This data comes from the ship blueprints, which are described in more detail in the deep dive on [ship blueprints](https://elite.bbcelite.com/ship_blueprints.html).

Click on the table headers to sort by that specification. The table shows the values from the BBC Master version of Elite, and footnotes point out any variations in the other versions.

| Ship name and blueprint | Laser power | Missile count | Maximum shield energy | Maximum speed | Bounty (Cr) | Targetable area (n x n) | Maximum canisters on demise | Gun vertex | Explosion count | 
|---|---|---|---|---|---|---|---|---|---|
| [Adder](https://elite.bbcelite.com/master/game_data/variable/ship_adder.html) | 2 | 0 | 85 | 24 | 4 | 50 | 0 | 0 | 4 | 
| [Alloy plate](https://elite.bbcelite.com/master/game_data/variable/ship_plate.html) | 0 | 0 | 16 | 16 | 0 | 10 | 0 | 0 | 1 | 
| [Anaconda](https://elite.bbcelite.com/master/game_data/variable/ship_anaconda.html) | 7 | 7 | 252 | 14 | 0 | 100 | 7 | 12 | 10 | 
| [Asp Mk II](https://elite.bbcelite.com/master/game_data/variable/ship_asp_mk_2.html) | 5 | 1 | 150 | 40 | 20 | 60 | 0 | 8 | 5 | 
| [Asteroid](https://elite.bbcelite.com/master/game_data/variable/ship_asteroid.html) | 0 | 0 | 60 | 30 | 0.5 | 80 | 0 | 0 | 7 | 
| [Boa](https://elite.bbcelite.com/master/game_data/variable/ship_boa.html) | 3 | 4 | 250 | 24 | 0 | 70 | 5 | 0 | 8 | 
| [Boulder](https://elite.bbcelite.com/master/game_data/variable/ship_boulder.html) | 0 | 0 | 20 | 30 | 0.1 | 30 | 0 | 0 | 2 | 
| [Cargo canister](https://elite.bbcelite.com/master/game_data/variable/ship_canister.html) | 0 | 0 | 17 | 15 | 0 | 20 | 0 | 0 | 3 | 
| [Cobra Mk I](https://elite.bbcelite.com/master/game_data/variable/ship_cobra_mk_1.html) | 2 | 2 | 90 | 26 | 7.5 | 99 | 3 | 10 | 5 | 
| [Cobra Mk III](https://elite.bbcelite.com/master/game_data/variable/ship_cobra_mk_3.html) | 2 | 3 | 150 | 28 | 0 | 95 | 3 | 21 | 9 | 
| [Cobra Mk III (pirate)](https://elite.bbcelite.com/master/game_data/variable/ship_cobra_mk_3_p.html) | 2 | 2 | 150 | 28 | 17.5 | 95 | 1 | 21 | 9 | 
| [Constrictor](https://elite.bbcelite.com/master/game_data/variable/ship_constrictor.html) | 6 | 4 | 252 | 36 | 0 | 65 | 3 | 0 | 10 | 
| [Coriolis station](https://elite.bbcelite.com/master/game_data/variable/ship_coriolis.html) | 0 | 6 | 240 | 0 | 0 | 160 | 0 | 0 | 12 | 
| [Cougar](https://elite.bbcelite.com/master/game_data/variable/ship_cougar.html) | 6 | 4 | 252 | 40 | 0 | 70 | 3 | 0 | 9 | 
| [Dodo station](https://elite.bbcelite.com/master/game_data/variable/ship_dodo.html) | 0 | 0 | 240 | 0 | 0 | 180 | 0 | 0 | 12 1 | 
| [Escape pod](https://elite.bbcelite.com/master/game_data/variable/ship_escape_pod.html) | 0 | 0 | 17 | 8 | 0 | 16 | 0 | 0 | 4 | 
| [Fer-de-Lance](https://elite.bbcelite.com/master/game_data/variable/ship_fer_de_lance.html) | 2 | 2 | 160 | 30 | 0 | 40 | 0 | 0 | 5 | 
| [Gecko](https://elite.bbcelite.com/master/game_data/variable/ship_gecko.html) | 2 | 0 | 70 | 30 | 5.5 | 99 | 0 | 0 | 5 | 
| [Krait](https://elite.bbcelite.com/master/game_data/variable/ship_krait.html) | 2 | 0 | 80 | 30 | 10 | 60 | 1 | 0 | 3 | 
| [Mamba](https://elite.bbcelite.com/master/game_data/variable/ship_mamba.html) | 2 | 2 | 90 | 30 | 15 | 70 | 1 | 0 | 7 | 
| [Missile](https://elite.bbcelite.com/master/game_data/variable/ship_missile.html) | 0 | 0 | 2 | 44 | 0 | 40 | 0 | 0 | 1 | 
| [Moray](https://elite.bbcelite.com/master/game_data/variable/ship_moray.html) | 2 | 0 | 100 | 25 | 5 | 30 | 1 | 0 | 5 | 
| [Python](https://elite.bbcelite.com/master/game_data/variable/ship_python.html) | 3 | 3 | 250 | 20 | 0 2 | 80 3 | 5 4 | 0 | 9 5 | 
| [Python (pirate)](https://elite.bbcelite.com/master/game_data/variable/ship_python_p.html) | 3 | 3 | 250 | 20 | 20 | 80 | 2 | 0 | 9 | 
| [Rock hermit](https://elite.bbcelite.com/master/game_data/variable/ship_rock_hermit.html) | 0 | 2 | 180 | 30 | 0 | 80 | 7 | 0 | 11 | 
| [Shuttle](https://elite.bbcelite.com/master/game_data/variable/ship_shuttle.html) | 0 | 0 | 32 | 8 | 0 | 50 | 15 | 0 | 8 | 
| [Sidewinder](https://elite.bbcelite.com/master/game_data/variable/ship_sidewinder.html) | 2 | 0 | 70 | 37 | 5 | 65 | 0 | 0 | 6 | 
| [Splinter](https://elite.bbcelite.com/master/game_data/variable/ship_splinter.html) | 0 | 0 | 20 | 10 | 0 | 16 | 0 | 0 | 4 | 
| [Thargoid](https://elite.bbcelite.com/master/game_data/variable/ship_thargoid.html) | 2 | 6 | 240 | 39 | 50 | 99 | 0 | 15 | 8 | 
| [Thargon](https://elite.bbcelite.com/master/game_data/variable/ship_thargon.html) | 2 | 0 | 20 | 30 | 5 | 40 | 0 | 0 | 3 | 
| [Transporter](https://elite.bbcelite.com/master/game_data/variable/ship_transporter.html) | 0 | 0 | 32 | 10 | 0 | 50 | 0 | 12 | 5 | 
| [Viper](https://elite.bbcelite.com/master/game_data/variable/ship_viper.html) | 2 | 1 | 140 6 | 32 | 0 | 75 | 0 | 0 | 9 | 
| [Worm](https://elite.bbcelite.com/master/game_data/variable/ship_worm.html) | 1 | 0 | 30 | 23 | 0 | 99 | 0 | 0 | 3 | 

## Footnotes for table 1

						                             ---------------------

						- ^
- ^
- ^
- ^
- ^
- ^


													 ------------------------

						The following table contains statistics about the 3D wireframes defined for each ship. This data mainly comes from the ship blueprints, which are described in more detail in the deep dive on [ship blueprints](https://elite.bbcelite.com/ship_blueprints.html). The kill points sre stored in the [KWH%](https://elite.bbcelite.com/master/game_data/variable/kwh_per_cent.html) and [KWL%](https://elite.bbcelite.com/master/game_data/variable/kwl_per_cent.html) variables.

Click on the table headers to sort by that specification. The table shows the values from the BBC Master version of Elite, and footnotes point out any variations in the other versions.

| Ship name and blueprint | Maximum edge count 7 | Number of vertices | Number of edges | Number of faces | Visibility distance | Normals scaled by | Market item if scooped | Kill points 8 | Versions containing this ship 9 | 
|---|---|---|---|---|---|---|---|---|---|
| [Adder](https://elite.bbcelite.com/master/game_data/variable/ship_adder.html) | 24 | 18 | 29 | 15 | 20 10 | 4 | - | 0.3515625 | Enhanced | 
| [Alloy plate](https://elite.bbcelite.com/master/game_data/variable/ship_plate.html) | 4 | 4 | 4 | 1 | 5 | 8 | Alloys | 0.0390625 | Enhanced | 
| [Anaconda](https://elite.bbcelite.com/master/game_data/variable/ship_anaconda.html) | 22 | 15 | 25 | 12 | 36 11 | 2 | - | 1.0 | Enhanced | 
| [Asp Mk II](https://elite.bbcelite.com/master/game_data/variable/ship_asp_mk_2.html) | 25 | 19 | 28 | 12 | 40 | 2 | - | 1.08203125 | Enhanced | 
| [Asteroid](https://elite.bbcelite.com/master/game_data/variable/ship_asteroid.html) | 16 | 9 | 21 | 14 | 50 | 2 | - | 0.03125 | All | 
| [Boa](https://elite.bbcelite.com/master/game_data/variable/ship_boa.html) | 22 | 13 | 24 | 13 | 40 | 1 | - | 0.83203125 | Enhanced | 
| [Boulder](https://elite.bbcelite.com/master/game_data/variable/ship_boulder.html) | 11 | 7 | 15 | 10 | 20 | 4 | - | 0.0234375 | Enhanced | 
| [Cargo canister](https://elite.bbcelite.com/master/game_data/variable/ship_canister.html) | 12 | 10 | 15 | 7 | 12 | 4 | - | 0.0390625 | All | 
| [Cobra Mk I](https://elite.bbcelite.com/master/game_data/variable/ship_cobra_mk_1.html) | 17 | 11 | 18 | 10 | 19 | 4 | - | 0.6640625 | Enhanced | 
| [Cobra Mk III](https://elite.bbcelite.com/master/game_data/variable/ship_cobra_mk_3.html) | 38 | 28 | 38 | 13 | 50 | 2 | - | 0.9140625 | All | 
| [Cobra Mk III (pirate)](https://elite.bbcelite.com/master/game_data/variable/ship_cobra_mk_3_p.html) | 38 | 28 | 38 | 13 | 50 | 2 | - | 1.1640625 | Enhanced | 
| [Constrictor](https://elite.bbcelite.com/master/game_data/variable/ship_constrictor.html) | 19 | 17 | 24 | 10 | 45 | 4 | - | 5.33203125 | Enhanced | 
| [Coriolis station](https://elite.bbcelite.com/master/game_data/variable/ship_coriolis.html) | 21 | 16 | 28 | 14 | 120 | 1 | - | - | All | 
| [Cougar](https://elite.bbcelite.com/master/game_data/variable/ship_cougar.html) | 25 | 19 | 25 | 6 | 34 | 4 | - | 5.33203125 | Advanced 12 | 
| [Dodo station](https://elite.bbcelite.com/master/game_data/variable/ship_dodo.html) | 24 | 24 | 34 | 12 | 125 | 1 | - | - | Enhanced | 
| [Escape pod](https://elite.bbcelite.com/master/game_data/variable/ship_escape_pod.html) | 6 | 4 | 6 | 4 | 8 | 16 13 | Slaves | 0.0625 | All | 
| [Fer-de-Lance](https://elite.bbcelite.com/master/game_data/variable/ship_fer_de_lance.html) | 26 | 19 | 27 | 10 | 40 | 2 | - | 1.25 | Enhanced | 
| [Gecko](https://elite.bbcelite.com/master/game_data/variable/ship_gecko.html) | 16 | 12 | 17 | 9 | 18 | 8 | - | 0.33203125 | Enhanced | 
| [Krait](https://elite.bbcelite.com/master/game_data/variable/ship_krait.html) | 21 | 17 | 21 | 6 | 20 14 | 2 | - | 0.33203125 | Enhanced | 
| [Mamba](https://elite.bbcelite.com/master/game_data/variable/ship_mamba.html) | 23 | 25 | 28 | 5 | 25 | 4 | - | 0.5 | All | 
| [Missile](https://elite.bbcelite.com/master/game_data/variable/ship_missile.html) | 20 | 17 | 24 | 9 | 14 | 4 | - | 0.58203125 | All | 
| [Moray](https://elite.bbcelite.com/master/game_data/variable/ship_moray.html) | 17 | 14 | 19 | 9 | 40 | 4 | - | 0.75 | Enhanced | 
| [Python](https://elite.bbcelite.com/master/game_data/variable/ship_python.html) | 21 | 11 | 26 | 13 | 40 | 1 | - | 0.6640625 | All | 
| [Python (pirate)](https://elite.bbcelite.com/master/game_data/variable/ship_python_p.html) | 21 | 11 | 26 | 13 | 40 | 1 | - | 1.1640625 | Enhanced | 
| [Rock hermit](https://elite.bbcelite.com/master/game_data/variable/ship_rock_hermit.html) | 16 | 9 | 21 | 14 | 50 | 2 | - | 0.33203125 | Enhanced | 
| [Shuttle](https://elite.bbcelite.com/master/game_data/variable/ship_shuttle.html) | 27 | 19 | 30 | 13 | 22 | 4 | - | 0.0625 | Enhanced | 
| [Sidewinder](https://elite.bbcelite.com/master/game_data/variable/ship_sidewinder.html) | 15 | 10 | 15 | 7 | 20 | 4 | - | 0.33203125 | All | 
| [Splinter](https://elite.bbcelite.com/master/game_data/variable/ship_splinter.html) | 6 | 4 | 6 | 4 | 8 | 32 | Minerals | 0.0390625 | Enhanced | 
| [Thargoid](https://elite.bbcelite.com/master/game_data/variable/ship_thargoid.html) | 25 | 20 | 26 | 10 | 55 | 4 | - | 2.6640625 | Standard | 
| [Thargon](https://elite.bbcelite.com/master/game_data/variable/ship_thargon.html) | 16 | 10 | 15 | 7 | 20 | 4 | Alien items | 0.12890625 | Standard | 
| [Transporter](https://elite.bbcelite.com/master/game_data/variable/ship_transporter.html) | 36 | 37 | 46 | 14 | 16 | 4 | - | 0.06640625 | Enhanced | 
| [Viper](https://elite.bbcelite.com/master/game_data/variable/ship_viper.html) | 19 | 15 | 20 | 7 | 23 | 2 | - | 0.1015625 | All | 
| [Worm](https://elite.bbcelite.com/master/game_data/variable/ship_worm.html) | 18 | 10 | 16 | 8 | 19 | 8 | - | 0.1953125 | Enhanced | 

## Footnotes for table 2

						                             ---------------------

						- ^
- ^- [combat rank](https://elite.bbcelite.com/combat_rank.html)for details.
- ^- Standard ships appear in the BBC Micro cassette version, plus all enhanced and advanced versions.
- Enhanced ships appear in the BBC Micro disc version, plus all advanced versions.
- Advanced ships appear in the 6502 Second Processor, Commodore 64, Apple II, BBC Master and NES versions.
 
- ^
- ^
- ^
- ^
- ^


													 ------------------------

						The following table contains ship dimensions, in terms of space coordinates. The x-axis runs from left to right (width), the y-axis from down to up (height), and the z-axis points into the screen (depth). This data comes from the ship blueprints, which are described in more detail in the deep dive on [ship blueprints](https://elite.bbcelite.com/ship_blueprints.html).

The volume is a simple calculation of the size of the ship's 3D bounding box. The last column shows the size of an equivalent cube that has the same volume.

Note that I have swapped the x- and y-coordinates for the Thargoid, so the dimensions match all the other ships. In the Thargoid blueprint, the wireframe is actually rotated through 90 degrees around the z-axis, making it tall and thin rather than short and wide; this is so when the mothership pitches, it rotates like an old-school flying saucer.

Click on the table headers to sort by that specification.

| Ship name and blueprint | Min x | Max x | Width | Min y | Max y | Height | Min z | Max z | Depth | Volume | Cube size | 
|---|---|---|---|---|---|---|---|---|---|---|---|
| [Adder](https://elite.bbcelite.com/master/game_data/variable/ship_adder.html) | -30 | 30 | 60 | -7 | 7 | 14 | -40 | 40 | 80 | 67,200 | 40.7 | 
| [Alloy plate](https://elite.bbcelite.com/master/game_data/variable/ship_plate.html) | -15 | 19 | 34 | -46 | 38 | 84 | -9 | 11 | 20 | 57,120 | 38.5 | 
| [Anaconda](https://elite.bbcelite.com/master/game_data/variable/ship_anaconda.html) | -69 | 69 | 138 | -47 | 53 | 100 | -58 | 254 | 312 | 4,305,600 | 162.7 | 
| [Asp Mk II](https://elite.bbcelite.com/master/game_data/variable/ship_asp_mk_2.html) | -69 | 69 | 138 | -18 | 14 | 32 | -45 | 83 | 128 | 565,248 | 82.7 | 
| [Asteroid](https://elite.bbcelite.com/master/game_data/variable/ship_asteroid.html) | -80 | 70 | 150 | -80 | 80 | 160 | -75 | 70 | 145 | 3,480,000 | 151.5 | 
| [Boa](https://elite.bbcelite.com/master/game_data/variable/ship_boa.html) | -62 | 62 | 124 | -65 | 40 | 105 | -107 | 93 | 200 | 2,604,000 | 137.6 | 
| [Boulder](https://elite.bbcelite.com/master/game_data/variable/ship_boulder.html) | -28 | 30 | 58 | -10 | 37 | 47 | -39 | 13 | 52 | 141,752 | 52.1 | 
| [Cargo canister](https://elite.bbcelite.com/master/game_data/variable/ship_canister.html) | -24 | 24 | 48 | -13 | 16 | 29 | -15 | 15 | 30 | 41,760 15 | 34.7 | 
| [Cobra Mk I](https://elite.bbcelite.com/master/game_data/variable/ship_cobra_mk_1.html) | -66 | 66 | 132 | -12 | 12 | 24 | -38 | 60 | 98 | 310,464 | 67.7 | 
| [Cobra Mk III](https://elite.bbcelite.com/master/game_data/variable/ship_cobra_mk_3.html) | -128 | 128 | 256 | -24 | 26 | 50 | -40 | 90 | 130 | 1,664,000 | 118.5 | 
| [Cobra Mk III (pirate)](https://elite.bbcelite.com/master/game_data/variable/ship_cobra_mk_3_p.html) | -128 | 128 | 256 | -24 | 26 | 50 | -40 | 90 | 130 | 1,664,000 | 118.5 | 
| [Constrictor](https://elite.bbcelite.com/master/game_data/variable/ship_constrictor.html) | -54 | 54 | 108 | -7 | 13 | 20 | -40 | 80 | 120 | 259,200 | 63.8 | 
| [Coriolis station](https://elite.bbcelite.com/master/game_data/variable/ship_coriolis.html) | -160 | 160 | 320 | -160 | 160 | 320 | -160 | 160 | 320 | 32,768,000 | 320.0 | 
| [Cougar](https://elite.bbcelite.com/master/game_data/variable/ship_cougar.html) | -60 | 60 | 120 | -14 | 14 | 28 | -40 | 67 | 107 | 359,520 | 71.1 | 
| [Dodo station](https://elite.bbcelite.com/master/game_data/variable/ship_dodo.html) | -231 | 231 | 462 | -243 | 243 | 486 | -196 | 196 | 392 | 88,016,544 | 444.8 | 
| [Escape pod](https://elite.bbcelite.com/master/game_data/variable/ship_escape_pod.html) | -7 | 21 | 28 | -14 | 14 | 28 | -12 | 36 | 48 | 37,632 | 33.5 | 
| [Fer-de-Lance](https://elite.bbcelite.com/master/game_data/variable/ship_fer_de_lance.html) | -40 | 40 | 80 | -14 | 18 | 32 | -52 | 108 | 160 | 409,600 | 74.3 | 
| [Gecko](https://elite.bbcelite.com/master/game_data/variable/ship_gecko.html) | -66 | 66 | 132 | -14 | 8 | 22 | -23 | 47 | 70 | 203,280 | 58.8 | 
| [Krait](https://elite.bbcelite.com/master/game_data/variable/ship_krait.html) | -90 | 90 | 180 | -18 | 18 | 36 | -48 | 96 | 144 | 933,120 | 97.7 | 
| [Mamba](https://elite.bbcelite.com/master/game_data/variable/ship_mamba.html) | -64 | 64 | 128 | -8 | 8 | 16 | -32 | 64 | 96 | 196,608 | 58.1 | 
| [Missile](https://elite.bbcelite.com/master/game_data/variable/ship_missile.html) | -12 | 12 | 24 | -12 | 12 | 24 | -44 | 68 | 112 | 64,512 | 40.1 | 
| [Moray](https://elite.bbcelite.com/master/game_data/variable/ship_moray.html) | -60 | 60 | 120 | -27 | 18 | 45 | -40 | 65 | 105 | 567,000 | 82.8 | 
| [Python](https://elite.bbcelite.com/master/game_data/variable/ship_python.html) | -96 | 96 | 192 | -48 | 48 | 96 | -112 | 224 | 336 | 6,193,152 | 183.6 | 
| [Python (pirate)](https://elite.bbcelite.com/master/game_data/variable/ship_python_p.html) | -96 | 96 | 192 | -48 | 48 | 96 | -112 | 224 | 336 | 6,193,152 | 183.6 | 
| [Rock hermit](https://elite.bbcelite.com/master/game_data/variable/ship_rock_hermit.html) | -80 | 70 | 150 | -80 | 80 | 160 | -75 | 70 | 145 | 3,480,000 | 151.5 | 
| [Shuttle](https://elite.bbcelite.com/master/game_data/variable/ship_shuttle.html) | -20 | 20 | 40 | -20 | 20 | 40 | -27 | 35 | 62 | 99,200 | 46.3 | 
| [Sidewinder](https://elite.bbcelite.com/master/game_data/variable/ship_sidewinder.html) | -64 | 64 | 128 | -16 | 16 | 32 | -28 | 36 | 64 | 262,144 | 64.0 | 
| [Splinter](https://elite.bbcelite.com/master/game_data/variable/ship_splinter.html) | -24 | 12 | 36 | -25 | 42 | 67 | -10 | 16 | 26 | 62,712 | 39.7 | 
| [Thargoid](https://elite.bbcelite.com/master/game_data/variable/ship_thargoid.html) | -164 | 164 | 328 | -24 | 32 | 56 | -164 | 164 | 328 | 6,024,704 | 182.0 | 
| [Thargon](https://elite.bbcelite.com/master/game_data/variable/ship_thargon.html) | -9 | 9 | 18 | -38 | 38 | 76 | -32 | 40 | 72 | 98,496 | 46.2 | 
| [Transporter](https://elite.bbcelite.com/master/game_data/variable/ship_transporter.html) | -33 | 33 | 66 | -8 | 10 | 18 | -26 | 30 | 56 | 66,528 | 40.5 | 
| [Viper](https://elite.bbcelite.com/master/game_data/variable/ship_viper.html) | -48 | 48 | 96 | -16 | 16 | 32 | -24 | 72 | 96 | 294,912 | 66.6 | 
| [Worm](https://elite.bbcelite.com/master/game_data/variable/ship_worm.html) | -26 | 26 | 52 | -10 | 14 | 24 | -25 | 35 | 60 | 74,880 | 42.1 | 

## Footnotes for table 3

						                             ---------------------

						- ^- Looking at the pentagonal ends of the canister, we can work out the length of the bottom, horizontal edge of the pentagon by looking at the z-distance from point (24, -13, 9) to point (24, -13, -9), for example. This gives us an edge size of 18.
- The area of a pentagon with side s is 5 * s^2 / 4 * tan(36), and plugging 18 into this gives us an area of 557.4.
- The canister has a length of 48, so if we multiply this by the pentagon area of 557.4, we get a total volume of 26,756.9 cubic coordinates.
 


													 ----------------------

						The following table contains details of when ships are spawned and how they behave.

The spawning code is in [part 1](https://elite.bbcelite.com/master/main/subroutine/main_game_loop_part_1_of_6.html), [part 3](https://elite.bbcelite.com/master/main/subroutine/main_game_loop_part_3_of_6.html) and [part 4](https://elite.bbcelite.com/master/main/subroutine/main_game_loop_part_4_of_6.html) of the main game loop. See the deep dive on [program flow of the main game loop](https://elite.bbcelite.com/program_flow_of_the_main_game_loop.html) for details.

The default personality flags that are used on spawning come from the [E%](https://elite.bbcelite.com/master/game_data/variable/e_per_cent.html) table. See the deep dive on [advanced tactics with the NEWB flags](https://elite.bbcelite.com/advanced_tactics_with_the_newb_flags.html) for details.

Click on the table headers to sort by that specification.

| Ship name and blueprint | Spawn as junk | Spawn as a pack hunter | Spawn as a lone bounty hunter | Spawn as a trader | Spawn as a cop | Personality flags (NEWB) | 
|---|---|---|---|---|---|---|
| [Adder](https://elite.bbcelite.com/master/game_data/variable/ship_adder.html) | No | Yes | No | No | No | Hostile Pirate Escape pod | 
| [Alloy plate](https://elite.bbcelite.com/master/game_data/variable/ship_plate.html) | Yes | No | No | No | No | - | 
| [Anaconda](https://elite.bbcelite.com/master/game_data/variable/ship_anaconda.html) | No | No | No | Yes | No | Trader Innocent Escape pod | 
| [Asp Mk II](https://elite.bbcelite.com/master/game_data/variable/ship_asp_mk_2.html) | No | No | Yes | No | No | Hostile Pirate Escape pod | 
| [Asteroid](https://elite.bbcelite.com/master/game_data/variable/ship_asteroid.html) | Yes | No | No | No | No | - | 
| [Boa](https://elite.bbcelite.com/master/game_data/variable/ship_boa.html) | No | No | No | Yes | No | Innocent Escape pod | 
| [Boulder](https://elite.bbcelite.com/master/game_data/variable/ship_boulder.html) | Yes | No | No | No | No | - | 
| [Cargo canister](https://elite.bbcelite.com/master/game_data/variable/ship_canister.html) | Yes | No | No | No | No | - | 
| [Cobra Mk I](https://elite.bbcelite.com/master/game_data/variable/ship_cobra_mk_1.html) | No | Yes | No | No | No | Hostile Pirate Escape pod | 
| [Cobra Mk III](https://elite.bbcelite.com/master/game_data/variable/ship_cobra_mk_3.html) | No | No | No | Yes | No | Innocent Escape pod | 
| [Cobra Mk III (pirate)](https://elite.bbcelite.com/master/game_data/variable/ship_cobra_mk_3_p.html) | No | Yes | Yes | No | No | Hostile Pirate Escape pod | 
| [Constrictor](https://elite.bbcelite.com/master/game_data/variable/ship_constrictor.html) | No | No | No | No | No | Hostile | 
| [Coriolis station](https://elite.bbcelite.com/master/game_data/variable/ship_coriolis.html) | No | No | No | No | No | - | 
| [Cougar](https://elite.bbcelite.com/master/game_data/variable/ship_cougar.html) | No | No | No | No | No | Innocent | 
| [Dodo station](https://elite.bbcelite.com/master/game_data/variable/ship_dodo.html) | No | No | No | No | No | - | 
| [Escape pod](https://elite.bbcelite.com/master/game_data/variable/ship_escape_pod.html) | Yes | No | No | No | No | Trader | 
| [Fer-de-Lance](https://elite.bbcelite.com/master/game_data/variable/ship_fer_de_lance.html) | No | No | Yes | No | No | Bounty hunter Escape pod | 
| [Gecko](https://elite.bbcelite.com/master/game_data/variable/ship_gecko.html) | No | Yes | No | No | No | Hostile Pirate | 
| [Krait](https://elite.bbcelite.com/master/game_data/variable/ship_krait.html) | No | Yes | No | No | No | Hostile Pirate Escape pod | 
| [Mamba](https://elite.bbcelite.com/master/game_data/variable/ship_mamba.html) | No | Yes | No | No | No | Hostile Pirate Escape pod | 
| [Missile](https://elite.bbcelite.com/master/game_data/variable/ship_missile.html) | No | No | No | No | No | - | 
| [Moray](https://elite.bbcelite.com/master/game_data/variable/ship_moray.html) | No | No | No | No | No | Hostile Pirate | 
| [Python](https://elite.bbcelite.com/master/game_data/variable/ship_python.html) | No | No | No | Yes | No | Innocent Escape pod | 
| [Python (pirate)](https://elite.bbcelite.com/master/game_data/variable/ship_python_p.html) | No | No | Yes | No | No | Hostile Pirate Escape pod | 
| [Rock hermit](https://elite.bbcelite.com/master/game_data/variable/ship_rock_hermit.html) | No | No | No | No | No | Trader Innocent Escape pod | 
| [Shuttle](https://elite.bbcelite.com/master/game_data/variable/ship_shuttle.html) | Yes | No | No | No | No | Trader Innocent | 
| [Sidewinder](https://elite.bbcelite.com/master/game_data/variable/ship_sidewinder.html) | No | Yes | No | No | No | Hostile Pirate | 
| [Splinter](https://elite.bbcelite.com/master/game_data/variable/ship_splinter.html) | Yes | No | No | No | No | - | 
| [Thargoid](https://elite.bbcelite.com/master/game_data/variable/ship_thargoid.html) | No | No | No | No | No | Hostile Pirate | 
| [Thargon](https://elite.bbcelite.com/master/game_data/variable/ship_thargon.html) | No | No | No | No | No | Hostile | 
| [Transporter](https://elite.bbcelite.com/master/game_data/variable/ship_transporter.html) | Yes | No | No | No | No | Trader Innocent Cop | 
| [Viper](https://elite.bbcelite.com/master/game_data/variable/ship_viper.html) | No | No | No | No | Yes | Bounty hunter Cop Escape pod | 
| [Worm](https://elite.bbcelite.com/master/game_data/variable/ship_worm.html) | No | Yes | No | No | No | Hostile Trader | 


													 ---------------------

						The following table shows ship colours. First, for the 6502 Second Processor and BBC Master versions of Elite only, it shows the colours of the 3D wireframes in the space view (all other versions have monochrome wireframes). Second, it also lists the colours used to show the different ship sticks on the 3D scanner. The data comes from the [shpcol](https://elite.bbcelite.com/master/main/variable/shpcol.html) and [scacol](https://elite.bbcelite.com/master/main/variable/scacol.html) tables.

Click on the table headers to sort by that specification.

| Ship name and blueprint | Ship colour (6502SP, Master) | Scanner colour (BBC) | Scanner colour (6502SP) | Scanner colour (Master) | Scanner colour (C64) | Scanner colour (Apple) | Scanner colour (NES) | 
|---|---|---|---|---|---|---|---|
| [Adder](https://elite.bbcelite.com/master/game_data/variable/ship_adder.html) | Cyan | Green | Cyan | Cyan | Yellow | White | Yellow | 
| [Alloy plate](https://elite.bbcelite.com/master/game_data/variable/ship_plate.html) | Cyan | Green | Blue | Blue | Yellow | Red | Blue | 
| [Anaconda](https://elite.bbcelite.com/master/game_data/variable/ship_anaconda.html) | Cyan | Green | Magenta | Magenta | Yellow | White | Yellow | 
| [Asp Mk II](https://elite.bbcelite.com/master/game_data/variable/ship_asp_mk_2.html) | Cyan | Green | Cyan | Cyan | Yellow | White | Yellow | 
| [Asteroid](https://elite.bbcelite.com/master/game_data/variable/ship_asteroid.html) | Red | Green | Red | Red | Red | Red | Blue | 
| [Boa](https://elite.bbcelite.com/master/game_data/variable/ship_boa.html) | Cyan | Green | Magenta | Magenta | Yellow | White | Yellow | 
| [Boulder](https://elite.bbcelite.com/master/game_data/variable/ship_boulder.html) | Red | Green | Red | Red | Red | Red | Blue | 
| [Cargo canister](https://elite.bbcelite.com/master/game_data/variable/ship_canister.html) | Cyan | Green | Blue | Blue | Yellow | Red | Blue | 
| [Cobra Mk I](https://elite.bbcelite.com/master/game_data/variable/ship_cobra_mk_1.html) | Cyan | Green | Cyan | Cyan | Yellow | White | Yellow | 
| [Cobra Mk III](https://elite.bbcelite.com/master/game_data/variable/ship_cobra_mk_3.html) | Cyan | Green | Cyan | Cyan | Yellow | White | Yellow | 
| [Cobra Mk III (pirate)](https://elite.bbcelite.com/master/game_data/variable/ship_cobra_mk_3_p.html) | Cyan | Green | Cyan | Cyan | Yellow | White | Yellow | 
| [Constrictor](https://elite.bbcelite.com/master/game_data/variable/ship_constrictor.html) | Cyan | Green | Cyan | Cyan | Yellow | White | Yellow | 
| [Coriolis station](https://elite.bbcelite.com/master/game_data/variable/ship_coriolis.html) | Cyan | Green | Green | Green | Green | Blue | Green | 
| [Cougar](https://elite.bbcelite.com/master/game_data/variable/ship_cougar.html) | Cyan | - | Cyan | None | None | - | None | 
| [Dodo station](https://elite.bbcelite.com/master/game_data/variable/ship_dodo.html) | Cyan | Green | Green | Green | Green | Blue | Green | 
| [Escape pod](https://elite.bbcelite.com/master/game_data/variable/ship_escape_pod.html) | Cyan | Green | Blue | Blue | Yellow | Red | Blue | 
| [Fer-de-Lance](https://elite.bbcelite.com/master/game_data/variable/ship_fer_de_lance.html) | Cyan | Green | Cyan | Cyan | Yellow | White | Yellow | 
| [Gecko](https://elite.bbcelite.com/master/game_data/variable/ship_gecko.html) | Cyan | Green | Cyan | Cyan | Yellow | White | Yellow | 
| [Krait](https://elite.bbcelite.com/master/game_data/variable/ship_krait.html) | Cyan | Green | Cyan | Cyan | Yellow | White | Yellow | 
| [Mamba](https://elite.bbcelite.com/master/game_data/variable/ship_mamba.html) | Cyan | Green | Cyan | Cyan | Yellow | White | Yellow | 
| [Missile](https://elite.bbcelite.com/master/game_data/variable/ship_missile.html) | Yellow | Yellow | Yellow | Yellow | Green | Blue | White | 
| [Moray](https://elite.bbcelite.com/master/game_data/variable/ship_moray.html) | Cyan/red/black/yellow stripes | Green | Cyan | Cyan | Yellow | White | Yellow | 
| [Python](https://elite.bbcelite.com/master/game_data/variable/ship_python.html) | Cyan | Green | Magenta | Magenta | Yellow | White | Yellow | 
| [Python (pirate)](https://elite.bbcelite.com/master/game_data/variable/ship_python_p.html) | Cyan | Green | Magenta | Magenta | Yellow | White | Yellow | 
| [Rock hermit](https://elite.bbcelite.com/master/game_data/variable/ship_rock_hermit.html) | Red | Green | Red | Red | Red | Red | Blue | 
| [Shuttle](https://elite.bbcelite.com/master/game_data/variable/ship_shuttle.html) | Cyan | Green | Cyan | Cyan | Yellow | White | Yellow | 
| [Sidewinder](https://elite.bbcelite.com/master/game_data/variable/ship_sidewinder.html) | Cyan | Green | Cyan | Cyan | Yellow | White | Yellow | 
| [Splinter](https://elite.bbcelite.com/master/game_data/variable/ship_splinter.html) | Red | Green | Red | Red | Red | Red | Blue | 
| [Thargoid](https://elite.bbcelite.com/master/game_data/variable/ship_thargoid.html) | Cyan/red stripes | Green | White | White | White | Fuzzy | Green | 
| [Thargon](https://elite.bbcelite.com/master/game_data/variable/ship_thargon.html) | Cyan/red stripes | Green | Cyan | Cyan | Yellow | White | White | 
| [Transporter](https://elite.bbcelite.com/master/game_data/variable/ship_transporter.html) | Cyan | Green | Cyan | Cyan | Yellow | White | Yellow | 
| [Viper](https://elite.bbcelite.com/master/game_data/variable/ship_viper.html) | Cyan | Green | Cyan | Cyan | Yellow | White | Yellow | 
| [Worm](https://elite.bbcelite.com/master/game_data/variable/ship_worm.html) | Cyan | Green | Blue | Blue | Yellow | Blue | Yellow |

---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/comparing_ship_specifications.html](https://elite.bbcelite.com/deep_dives/comparing_ship_specifications.html)*

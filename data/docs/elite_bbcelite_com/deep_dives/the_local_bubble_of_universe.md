---
title: The local bubble of universe
source_url: https://elite.bbcelite.com/deep_dives/the_local_bubble_of_universe.html
category: source-code
topics:
- sprite programming
- memory management
- basic
- assembly
difficulty: beginner
language: mixed
hardware:
- CPU
- KERNAL
- CIA
related:
- keyboard-handling
- joystick-reading
- raster-interrupts
- memory-map
- sprite-programming
- vic-ii-registers
- kernal-routines
- cia-registers
scraped_at: '2026-07-14'
---

# The local bubble of universe

## The data structures used to simulate the universe around our ship

One of the most impressive aspects of Elite is how expansive the universe feels. The eight galaxies and 2048 systems no doubt have something to do with this, but while they might make you feel like nothing more than a pale blue dot in the background of a cosmic snapshot, the experience of flying around in system space is a lot more visceral. That feeling in the pit of your stomach when a group of pirates pings into view on the scanner, while you're busy surfing the sun's rays for precious fuel while trying not to boil the outer hull into stardust... there's a real sense of being there, out in the black. Clearly a 32K micro from the early 1980s can't actually be home to an entire solar system, so how does Elite simulate things closer to home?

The answer is in the "local bubble of universe", which stores all the details of our immediate vicinity, along with the major bodies in the current system. Take, for example, the famous screenshot from the back of the box for the BBC Micro version:

![BBC Micro Elite screenshot](https://elite.bbcelite.com/images/general/Elite-BBCMicro.png) 

						In this local bubble, there are 12 ships that we can see on the 3D scanner, plus the sun and planet (the latter being off-screen). Interestingly, the standard BBC Micro version only supports a maximum of ten ships (plus the sun and planet), so this is either a doctored screenshot or an enhanced version of the game - I suspect it's the former, as that would be a lot easier than trying to squeeze more ship slots into the memory-starved BBC Micro.

To see just how big the local bubble is, see the deep dive on [a sense of scale](https://elite.bbcelite.com/a_sense_of_scale.html).

Let's start by looking at how the local bubble is stored in-game.

## Data structures in the local bubble

													 -----------------------------------

						The local bubble is made up of the following data structures:

- The ship slots at [FRIN](https://elite.bbcelite.com/cassette/main/workspace/wp.html#frin)
- The ship data block lookup table at [UNIV](https://elite.bbcelite.com/cassette/main/variable/univ.html)
- The ship data blocks at [K%](https://elite.bbcelite.com/cassette/main/workspace/k_per_cent.html)
- The ship blueprints at [XX21](https://elite.bbcelite.com/cassette/main/variable/xx21.html)

Using these, the local bubble can store details on all the ships in the vicinity, plus the planet, sun and space station. Note that to keep things simple, we call any object in the vicinity a "ship", whether it's a spaceship, or a space station, the planet, the sun, a missile, an escape pod, an asteroid or a cargo canister. Also, the bubble can only contain either the sun or the space station, but not both at the same time, as they share the same slot. The planet is always present.

Specifically, the maximum number of ships is defined by the configuration variable [NOSH](https://elite.bbcelite.com/cassette/all/workspaces.html#nosh), which varies between versions. So the bubble can contain up to 12 ships on the BBC Micro cassette, BBC Micro disc, Acorn Electron and BBC Master versions (i.e. up to ten spaceships, plus the planet and sun/station), up to 20 ships on the 6502 Second Processor version (i.e. 18 spaceships), and up to eight ships on the NES version (i.e. six spaceships). See the [feature comparison table](https://elite.bbcelite.com/compare/feature_comparison.html) for more comparisons.

Let's look at these structures in more detail.

## The ship slots at FRIN

													 ----------------------

						Each ship in our local bubble of universe has its own "ship slot" in the table at FRIN. Ships get added to slots by the NWSHP routine, and when they get killed or fly too far away to be in the bubble, they get removed from the table by the KILLSHP routine, and the whole table gets shuffled down to close up the gap. This means that the next free gap is always at the end of the table, assuming it isn't full (if it is, NWSHP returns with a flag to say that no new ship was created).

The local bubble always contains the planet, plus either the sun or the space station (but not both). The first two slots are reserved for this purpose as follows.

The first ship slot at location FRIN is always reserved for the planet. It contains 128 or 130, depending on the type of planet:

- 128 for a planet with an equator and meridian
- 130 for a planet with a crater

The second ship slot at FRIN+1 is always reserved for the sun and the space station. They can share the same slot because we only ever have one of them in our local bubble of universe at any one time - the sun disappears when we enter the space station's safe zone, and it reappears when we leave it again. This slot always contains one of the following:

- #SST for the space station (i.e. 2 or 8)
- 129 for the sun

Any actual ships in our local bubble start at slot FRIN+2. There can be up to 11 ships in the local bubble, and for each of these, there's a slot containing the ID for that ship type. Ship types correspond to the blueprint numbers in the lookup table at XX21; the BBC Micro cassetts version has 13 entries in XX21, so in this version the ship type will be a value from 1-13 (though this part of the slot table never contains an 8, which is the ship ID for the Coriolis station in this version, as we have already reserved the second ship slot at FRIN+1 for the space station). Some ship types have corresponding configuration variables that make the source code a bit easier to follow - such as #COPS for the Viper - but not all of them do.

The different ship types and their IDs in the various versions of Elite are listed in the deep dive on [ship blueprints](https://elite.bbcelite.com/ship_blueprints.html). Ship IDs start from 1; if a ship slot is empty, it contains 0.

Note that some ships come in multiple flavours, and some ships share blueprints. For example, in the BBC Micro and Acorn Electron versions, the Cobra Mk III comes in two flavours: a ship type of 5 is a bounty hunting Cobra, while a ship type of 7 is a more peaceful trader. Both ships use the same blueprint when drawn on-screen, which saves memory but their tactical behaviour is quite different. The more advanced versions of Elite tend not to share blueprints, as they can afford the duplication.

## The ship data block lookup table at UNIV

													 ----------------------------------------

						For each occupied ship slot in the table at FRIN, there is a corresponding address in the lookup table at UNIV that points to that ship's data block. The ship data blocks are stored in the K% workspace, and the addresses in UNIV map to the ship slots in FRIN just as you would expect:

- UNIV points to the ship data block for the planet in slot FRIN
- UNIV+1 points to the ship data block for the sun or space station in slot FRIN+1
- UNIV+2 points to the ship data block for the ship in slot FRIN+2
- UNIV+3 points to the ship data block for the ship in slot FRIN+3

...and so on up to UNIV+12. Because each ship data block is always the same size (36 bytes), the addresses in the UNIV table are hard-coded and don't change.

## The ship data blocks at K%

													 --------------------------

						As noted above, the local bubble of universe can contain up to #NOSH ships, one for each slot in FRIN and address in UNIV. Each of those ships has its own ship data block of 36 (NI%) bytes that contains information such as the ship's position in space, its speed, its rotation, its energy levels and so on. It also contains a pointer to that ship's ship line heap which is where we store details of all the lines that are required to draw the ship on-screen, so that it's easy to remove the ship from the screen by redrawing the exact same shape again (see the deep dive on [drawing ships](https://elite.bbcelite.com/drawing_ships.html) for more details).

In the BBC Micro cassette and disc versions of Elite, these 12 blocks of ship data live in the first 432 bytes of the workspace at K% (&0900 to &0AD4), while the ship line heaps are stored in descending order from the start of the WP workspace. This is the layout of the ship data blocks and ship line heaps in memory, shown when we are in the process of adding a new ship to the local bubble in the NWSHP routine:

+-----------------------------------+ &0F34 | | | WP workspace | | | +-----------------------------------+ &0D40 = WP | | | Current ship line heap | | | +-----------------------------------+ SLSP | | | Proposed heap for new ship | | | +-----------------------------------+ INWK(34 33) | | . . . . . . . . . . | | +-----------------------------------+ INF + NI% | | | Proposed data block for new ship | | | +-----------------------------------+ INF | | | Existing ship data blocks | | | +-----------------------------------+ &0900 = K%

If we want to update a ship's data, which we want to do when moving the ship in space during the main flight loop, then instead of working with the data in the K% workspace, we first copy the whole block to the INWK workspace. This "inner workspace" is in zero page, where it is much quicker and more efficient to access memory locations. When we are done updating the ship's data, we copy it back to the relevant location in K%, as pointed to by the UNIV table.

See the deep dive on [ship data blocks](https://elite.bbcelite.com/ship_data_blocks.html) for details of the 36 bytes and the information that they contain.

## The ship blueprints at XX21

													 ---------------------------

						Each ship type has an associated ship blueprint that contains fixed data about that specific ship type, such as its maximum speed or the size of the target area we need to hit with our lasers to cause damage. The blueprints also contain data on the ship's vertices, faces and edges, which are used to draw the ship on-screen.

The table at XX21 contains the blueprint addresses for the various ship types. See the deep dive on [ship blueprints](https://elite.bbcelite.com/ship_blueprints.html) for more details of the blueprints and the information that they contain.

## Codice Estratto

### Snippet Codice (BASIC)

```basic
+-----------------------------------+   &0F34
  |                                   |
  | WP workspace                      |
  |                                   |
  +-----------------------------------+   &0D40 = WP
  |                                   |
  | Current ship line heap            |
  |                                   |
  +-----------------------------------+   SLSP
  |                                   |
  | Proposed heap for new ship        |
  |                                   |
  +-----------------------------------+   INWK(34 33)
  |                                   |
  .                                   .
  .                                   .
  .                                   .
  .                                   .
  .                                   .
  |                                   |
  +-----------------------------------+   INF + NI%
  |                                   |
  | Proposed data block for new ship  |
  |                                   |
  +-----------------------------------+   INF
  |                                   |
  | Existing ship data blocks         |
  |                                   |
  +-----------------------------------+   &0900 = K%
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/the_local_bubble_of_universe.html](https://elite.bbcelite.com/deep_dives/the_local_bubble_of_universe.html)*

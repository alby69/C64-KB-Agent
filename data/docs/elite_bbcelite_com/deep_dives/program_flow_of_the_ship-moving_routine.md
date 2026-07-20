---
title: Program flow of the ship-moving routine
source_url: https://elite.bbcelite.com/deep_dives/program_flow_of_the_ship-moving_routine.html
category: deep-dive
topics:
- assembly
- graphics
difficulty: beginner
language: mixed
hardware:
- KERNAL
related:
- memory-map
- kernal-routines
scraped_at: '2026-07-20'
---

# Program flow of the ship-moving routine

## A breakdown of the routine that moves the entire universe around us

The Elite universe is well-known for being immersive, and one of the most convincing aspects of the bubble of universe around our Cobra Mk III is how all the other objects around us move independently, from ships and space stations to entire planets and suns. This is no static universe with chunky bitmap backdrops or the predictable alien shuffle of Space Invaders - this is a convincing reality where pirates fly rings around rookie pilots while Coriolis stations pump out wave after wave of deadly law-enforcing Vipers.

So it's no surprise that the main ship-moving routine at MVEIT does a lot of heavy lifting. That said, the amount of effort is greatly reduced by the fact that the universe rotates around our ship, rather than the other way round. When we pitch or roll our Cobra, our ship actually stays put and the game rotates the entire universe around us in the opposite direction to the way we're rotating. The end result is the same because the universe is nice and simple, but the calculations are a lot easier to implement.

The MVEIT routine gets called by the main flight loop for each nearby ship. It rotates the current ship by the pitch and roll angles (which are set up to move the universe in the correct direction) while also applying the ship's own individual movements, such as its speed, orientation changes, and so on.

The MVEIT also calls the TACTICS routine to apply tactics to ships with AI enabled (see the deep dive on [program flow of the tactics routine](https://elite.bbcelite.com/program_flow_of_the_tactics_routine.html) for more details).

## Program flow

													 ------------

						Here's a breakdown of how the game implements a universe that literally revolves around us.

- The main entry point for the moving routine
- Tidy the orientation vectors for one of the ship slots (by calling TIDY)

- Apply tactics to ships with AI enabled (by calling TACTICS)
- Remove the ship from the scanner, so we can move it (by calling SCAN)

- Move the ship forward (along the vector pointing in the direction of travel) according to its speed

- Apply acceleration to the ship's speed (if acceleration is non-zero), and then zero the acceleration as it's a one-off change

- Rotate the ship's location in space by the amount of pitch and roll of our ship

- Move the ship in space according to our speed

- Rotate the ship's orientation vectors according to our pitch and roll (MVS4)

- If the ship we are processing is rolling or pitching itself, rotate it and apply damping if required

- If the ship is exploding or being removed, hide it on the scanner
- Otherwise redraw the ship on the scanner, now that it's been moved

---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/program_flow_of_the_ship-moving_routine.html](https://elite.bbcelite.com/deep_dives/program_flow_of_the_ship-moving_routine.html)*

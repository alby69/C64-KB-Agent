---
title: Program flow of the main game loop
source_url: https://elite.bbcelite.com/deep_dives/program_flow_of_the_main_game_loop.html
category: source-code
topics:
- sprite programming
- basic
- assembly
difficulty: intermediate
language: mixed
hardware:
- KERNAL
related:
- raster-interrupts
- memory-map
- kernal-routines
- sprite-programming
- vic-ii-registers
scraped_at: '2026-07-14'
---

# Program flow of the main game loop

## The sequence of events in the main game loop and the main flight loop

Here is a high-level look at the main program flow, from the title screen to the end of life as we know it, via the main game loop and the main flight loop. The following is mainly about the flight aspects of the game, as the docked screens don't really have much of a flow, they just get shown when the relevant keys are pressed.

Each section is broken down into parts that mirror the structure of the source code, and the routine names below link to the source code for the BBC Micro cassette version, so you can follow along.

## Title sequence

													 --------------

						The main title sequence, with its iconic rotating ships, is shown when the game starts, or restarts following a "GAME OVER" message.

- Reset the stack pointer to clear any previous return addresses

- Show the "Load New Commander (Y/N)?" title screen (TITLE)
- Process loading of commander file, if selected

- Copy last saved commander NA% to current commander TP

- Show the "Press Fire or Space, Commander" title screen (TITLE)
- Set target system to home system
- Process arrival in system closest to target

- Set the docked flag
- Jump to the docked section of the main game loop (FRCE, see below) with f8 "pressed" to show Status Mode

## Main game loop

													 --------------

						The main game loop starts when we begin a new game. When docked, only parts 5 and 6 form the game loop, but the whole loop from parts 2 to 6 is run when we are in space (part 1 is a subroutine that's called from part 2).

[1/6: Main game loop (Part 1 of 6)](https://elite.bbcelite.com/cassette/main/subroutine/main_game_loop_part_1_of_6.html)

- Potentially called from part 2
- Spawn a trader

[2/6: Main game loop (Part 2 of 6)](https://elite.bbcelite.com/cassette/main/subroutine/main_game_loop_part_2_of_6.html)

- Call the main flight loop (see below)
- Clear any expired in-flight messages from the screen
- On 255 out of 256 iterations, skip straight to MLOOP in part 5
- Potentially spawn a trader by jumping up to part 1
- Potentially spawn a cargo canister or an asteroid

[3/6: Main game loop (Part 3 of 6)](https://elite.bbcelite.com/cassette/main/subroutine/main_game_loop_part_3_of_6.html)

- Potentially spawn a cop, with a higher chance if we've been bad

[4/6: Main game loop (Part 4 of 6)](https://elite.bbcelite.com/cassette/main/subroutine/main_game_loop_part_4_of_6.html)

- Potentially spawn a lone bounty hunter, a Thargoid, or a group of 1-4 pirates

[5/6: Main game loop (Part 5 of 6)](https://elite.bbcelite.com/cassette/main/subroutine/main_game_loop_part_5_of_6.html)

- Main entry point for main game loop at MLOOP
- Cool down the lasers
- Update the dashboard (DIALS)
- If this is not a space view, scan for cursor keys

[6/6: Main game loop (Part 6 of 6)](https://elite.bbcelite.com/cassette/main/subroutine/main_game_loop_part_6_of_6.html)

- Entry point for displaying a specific screen at FRCE
- Process function keys and other non-flight keys (TT102)
- If docked, loop back to part 5 (MLOOP)
- If in-flight, loop back to part 2

## Main flight loop

													 ----------------

						The main flight loop is called from the main game loop, but only if we are in space. It deals with all the flight aspects of the game, calling the various moving and tactics routines as required.

[1/16: Main flight loop (Part 1 of 16)](https://elite.bbcelite.com/cassette/main/subroutine/main_flight_loop_part_1_of_16.html)

- Main entry point for main flight loop at M%
- Seed the random number generator

[2/16: Main flight loop (Part 2 of 16)](https://elite.bbcelite.com/cassette/main/subroutine/main_flight_loop_part_2_of_16.html)

- Calculate the alpha and beta angles from the current pitch and roll

[3/16: Main flight loop (Part 3 of 16)](https://elite.bbcelite.com/cassette/main/subroutine/main_flight_loop_part_3_of_16.html)

- Scan for flight keys and process the results

Now start looping through all the ships in the local bubble, and for each one, do parts 4-12:

[4/16: Main flight loop (Part 4 of 16)](https://elite.bbcelite.com/cassette/main/subroutine/main_flight_loop_part_4_of_16.html)

- Copy the ship's data block from K% to INWK
- Set XX0 to point to the ship's blueprint (if this is a ship)

[5/16: Main flight loop (Part 5 of 16)](https://elite.bbcelite.com/cassette/main/subroutine/main_flight_loop_part_5_of_16.html)

- If an energy bomb has been set off and this ship can be killed, kill it and increase the kill tally

[6/16: Main flight loop (Part 6 of 16)](https://elite.bbcelite.com/cassette/main/subroutine/main_flight_loop_part_6_of_16.html)

- Move the ship in space by calling the MVEIT routine (see the deep dive on [program flow of the ship-moving routine](https://elite.bbcelite.com/program_flow_of_the_ship-moving_routine.html)for details). MVEIT also calls the main tactics routine at TACTICS to implement ship AI (see the deep dive on[program flow of the tactics routine](https://elite.bbcelite.com/program_flow_of_the_tactics_routine.html)for more)
- Copy the updated ship's data block from INWK back to K%

[7/16: Main flight loop (Part 7 of 16)](https://elite.bbcelite.com/cassette/main/subroutine/main_flight_loop_part_7_of_16.html)

- Check how close we are to this ship and work out if we are docking, scooping or colliding with it

[8/16: Main flight loop (Part 8 of 16)](https://elite.bbcelite.com/cassette/main/subroutine/main_flight_loop_part_8_of_16.html)

- Process us potentially scooping this item

[9/16: Main flight loop (Part 9 of 16)](https://elite.bbcelite.com/cassette/main/subroutine/main_flight_loop_part_9_of_16.html)

- Entry point for docking checks at ISDK
- Process docking with space station, which can take us to the main loop via BAY (if we dock successfully) or DEATH (if we don't)

[10/16: Main flight loop (Part 10 of 16)](https://elite.bbcelite.com/cassette/main/subroutine/main_flight_loop_part_10_of_16.html)

- Remove scooped item after both successful and failed scooping attempts
- Process collisions, which can lead to DEATH

[11/16: Main flight loop (Part 11 of 16)](https://elite.bbcelite.com/cassette/main/subroutine/main_flight_loop_part_11_of_16.html)

- If this isn't the front space view, flip the ship coordinates' axes (PLUT)
- Process missile lock
- Process our laser firing

[12/16: Main flight loop (Part 12 of 16)](https://elite.bbcelite.com/cassette/main/subroutine/main_flight_loop_part_12_of_16.html)

- Draw the ship (LL9)
- Process the removal of killed ships

Loop back up to part 4 to do the next ship in the local bubble until we have processed them all

[13/16: Main flight loop (Part 13 of 16)](https://elite.bbcelite.com/cassette/main/subroutine/main_flight_loop_part_13_of_16.html)

- Show energy bomb effect (if applicable)
- Charge shields and energy banks

[14/16: Main flight loop (Part 14 of 16)](https://elite.bbcelite.com/cassette/main/subroutine/main_flight_loop_part_14_of_16.html)

- Spawn a space station if we are close enough to the planet

[15/16: Main flight loop (Part 15 of 16)](https://elite.bbcelite.com/cassette/main/subroutine/main_flight_loop_part_15_of_16.html)

- Perform an altitude check with the planet, which can lead to DEATH
- Perform an altitude check with the sun, which can also lead to DEATH
- Process fuel scooping

[16/16: Main flight loop (Part 16 of 16)](https://elite.bbcelite.com/cassette/main/subroutine/main_flight_loop_part_16_of_16.html)

- Process laser pulsing
- Process E.C.M. energy drain
- Call the stardust routine if we are on a space view (STARS)
- Return from the main flight loop

## Death

													 -----

						The death routine is called when we die (or quit the game by pausing and pressing ESCAPE). It's a one-way street and eventually loops back to the start to show the title screen again.

- We have been killed, so display the chaos of our destruction above a "GAME OVER" sign

- Clean up a number of variables and workspaces, ready for the next attempt
- Return to TT170 to start the whole process again

---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/program_flow_of_the_main_game_loop.html](https://elite.bbcelite.com/deep_dives/program_flow_of_the_main_game_loop.html)*

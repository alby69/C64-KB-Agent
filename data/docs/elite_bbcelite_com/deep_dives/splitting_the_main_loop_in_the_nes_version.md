---
title: Splitting the main loop in the NES version
source_url: https://elite.bbcelite.com/deep_dives/splitting_the_main_loop_in_the_nes_version.html
category: deep-dive
topics:
- assembly
difficulty: beginner
language: assembly
hardware:
- CPU
- KERNAL
related:
- memory-map
- kernal-routines
scraped_at: '2026-07-14'
---

# Splitting the main loop in the NES version

## How the main flight loop is split and shared with the combat demo

Broadly speaking, the NES version of Elite has the same main loop structure as the other 6502 versions, and it uses the same main loop counter to schedule tasks (see the deep dives on [program flow of the main game loop](https://elite.bbcelite.com/program_flow_of_the_main_game_loop.html) and [scheduling tasks with the main loop counter](https://elite.bbcelite.com/scheduling_tasks_with_the_main_loop_counter.html) for details). However in the NES version, the main flight loop gets split up into separate subroutines to support the "game-in-game" concept of the playable combat demo, where you get to take on three ships in combat without it affecting your in-game commander:

![The combat demo in NES Elite](https://elite.bbcelite.com/images/nes/demo/combat_practice.png) 

						The main game loop is essentially the same in all the 6502 versions, with [part 2 of the main game loop](https://elite.bbcelite.com/nes/bank_0/subroutine/main_game_loop_part_2_of_6.html) calling the main flight loop using a JSR M% instruction. In the original versions, the 16 parts of the main flight loop then follow on from each other in the codebase, so all 16 parts get run sequentially to simulate the local bubble and draw all the ships. When the flight loop is done, we return to part 2 of the main game loop and around we go again. The main flight loop is long, but it's a simple enough structure.

In the NES version, calling M% from the main game loop still jumps to part 1 of the main flight loop, and parts 1 to 3 are still consecutive, with part 1 falling into part 2, and part 2 falling into part 3. But things change at the end of part 3, with the code splitting up into a handful of subroutines like this:

- Parts 4 to 12 of the main flight loop are moved into a separate routine at [MAL1](https://elite.bbcelite.com/nes/bank_0/subroutine/main_flight_loop_part_4_of_16.html). In the original version of Elite, this part of the main flight loop is responsible for looping through each ship slot to process the ships in the bubble, but in NES Elite the new routine at MAL1 processes just one slot (given in X). The bones of this part of the main loop are the same as in the original version, it's just that the logic has been moved to a separate subroutine, and that routine only processes one ship.
- A new routine called [FlightLoop4To16](https://elite.bbcelite.com/nes/bank_0/subroutine/flightloop4to16.html)implements the loop that surrounds parts 4 to 12 of the original. This loop works through each ship slot and processes the contents, which we can do in the new structure by simply calling MAL1 for each populated slot. So FlightLoop4To16 effectively replaces parts 4 to 12 in the original, and it also falls through into part 13 to 16 of the main flight loop, so calling FlightLoop4To16 does exactly that - it implements parts 4 to 16 of the original flight loop.
- M% is still the entry point for the main flight loop, and it is still in [part 2 of the loop](https://elite.bbcelite.com/nes/bank_0/subroutine/main_flight_loop_part_2_of_16.html), as before. Calling M% therefore starts the main flight loop, and when we get to the end of[part 3](https://elite.bbcelite.com/nes/bank_0/subroutine/main_flight_loop_part_3_of_16.html), we call FlightLoop4To16 to run parts 4 to 16. After returning from that call we fall into another new routine,[DrawSpaceViewInNMI](https://elite.bbcelite.com/nes/bank_0/subroutine/drawspaceviewinnmi.html), which configures the NMI handler to send the space view that we just drew to the PPU, and when that's done, we return from the main flight loop and back to the main game loop.

The point of all this splitting up is that the main flight loop can now be run independently from different parts of the codebase. Specifically, [DEATH](https://elite.bbcelite.com/nes/bank_0/subroutine/death.html) and [RunDemoFlightLoop](https://elite.bbcelite.com/nes/bank_0/subroutine/rundemoflightloop.html) both call FlightLoop4To16 to simulate their own bubbles, one for showing the detritus of our demise, and the other for spawning the three ships of the combat demo (see the deep dive on [the NES combat demo](https://elite.bbcelite.com/the_nes_combat_demo.html) for more on the latter). There are some blocks of logic in the main flight loop that behave differently depending on where the loop has been called from - for example, [part 15 of the flight loop](https://elite.bbcelite.com/nes/bank_0/subroutine/main_flight_loop_part_15_of_16.html#ma93) checks whether we have killed all three ships in the combat demo and triggers the scroll text if we have - but generally the code in the main loop is identical to the other versions, it's just split out separately.

In comparison, the demo mode in the 6502 Second Processor version doesn't use the main flight loop, but instead it implements its own loop just for the demo (see the deep dive on [the 6502 Second Processor demo mode](https://elite.bbcelite.com/6502sp_demo_mode.html) for details). The demo isn't playable, so this approach works fine, but the NES solution is a lot more flexible, even if it comes at the expense of having a nice, clean, sequential flight loop.

---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/splitting_the_main_loop_in_the_nes_version.html](https://elite.bbcelite.com/deep_dives/splitting_the_main_loop_in_the_nes_version.html)*

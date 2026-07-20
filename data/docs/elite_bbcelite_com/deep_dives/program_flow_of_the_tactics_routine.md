---
title: Program flow of the tactics routine
source_url: https://elite.bbcelite.com/deep_dives/program_flow_of_the_tactics_routine.html
category: source-code
topics:
- assembly
difficulty: beginner
language: assembly
hardware:
- KERNAL
- SID
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

# Program flow of the tactics routine

## How ships and missiles work out attack patterns... or how to run away

Ships in Elite seem to have purpose - it's part of the reason why the Elite universe feels so alive. Later versions of the game expand on the simpler artificial intelligence in the BBC versions: the version of Elite for the Acorn Archimedes is particularly celebrated for having ships that genuinely seem to be going about their business, with busy lives of their own. But even in the memory-constrained cassette version on the BBC Micro, the universe feels as if it is piloted by real people... or real aliens, if you're unlucky enough to bump into the Thargoids.

The heart of Elite's convincing AI is the [TACTICS](https://elite.bbcelite.com/cassette/main/subroutine/tactics_part_2_of_7.html) routine. This gets applied to every ship that has bit 7 set in ship byte #32, and it is called by the MVEIT routine, which itself is called on every iteration of the main loop. However, because it takes quite a bit of time to apply tactics to a ship, they are only applied to one or two ships on each iteration of the main flight loop, depending on the value of the main loop counter in MCNT.

## Program flow

													 ------------

						Let's see how ships in Elite are brought to life by stepping through the TACTICS routine. You might want to start with part 2, as that's where the main entry point is (the following is in the order in which it appears in the source code).

- Entry point for missile tactics at TA34, called from part 1 for missiles only
- If E.C.M. is active, destroy the missile
- If the missile is hostile towards us, then check how close it is. If it hasn't reached us, jump to part 3 so it can streak towards us, otherwise we've been hit, so process a large amount of damage to our ship, which can lead to DEATH
- Otherwise see how close the missile is to its target. If it has not yet reached its target, give the target a chance to activate its E.C.M. if it has one, otherwise jump to part 3
- If it has reached its target and the target is the space station, destroy the missile, potentially damaging us if we are nearby
- If it has reached its target and the target is a ship, destroy the missile and the ship, potentially damaging us if we are nearby

- Main entry point for TACTICS routine
- If this is a missile, jump up to the missile code in part 1
- If this is an escape pod, point it at the planet and jump to part 7
- If this is the space station and it is hostile, spawn a cop and we're done
- If this is a lone Thargon without a mothership, set it adrift aimlessly and we're done
- If this is a pirate and we are within the space station safe zone, stop the pirate from attacking
- Recharge the ship's energy banks by 1

- Calculate the dot product of the ship's nose vector (i.e. the direction it is pointing) with the vector between us and the ship so we can work out later on whether the enemy ship can hit us with its lasers

- Rarely (2.5% chance) roll the ship by a noticeable amount
- If the ship has at least half its energy banks full, jump to part 6 to consider firing the lasers
- If the ship isn't really low on energy, jump to part 5 to consider firing a missile
- Rarely (10% chance) the ship runs out of both energy and luck, and bails, launching an escape pod and drifting in space

- If the ship doesn't have any missiles, skip to the next part
- If an E.C.M. is firing, skip to the next part
- Randomly decide whether to fire a missile (or, in the case of Thargoids, release a Thargon), and if we do, we're done

- If the ship is not pointing at us, skip to the next part
- If the ship is pointing at us but not accurately, fire its laser at us and skip to the next part
- If we are in the ship's crosshairs, register some damage to our ship, slow down the attacking ship, make the noise of us being hit by laser fire (which could end in DEATH), and we're done

- Work out which direction the ship should be moving, depending on whether it's an escape pod, where it is, which direction it is pointing, and how aggressive it is. At this point XX15 contains the normalised vector from our ship to the ship we are applying AI tactics to (or the normalised vector from the target to the missile - in both cases it's the vector from the potential victim to the attacker). We now check these conditions:
								- This is a trader (in enhanced versions) or escape pod (in standard versions) and XX15 is pointing towards the planet
- The ship is pretty close to us, or it's just not very aggressive (though there is a random factor at play here too), and XX15 is still pointing from our ship towards the enemy ship
- The ship is aggressive (though again, there's an element of randomness here), and XX15 is pointing from the enemy ship towards our ship
- This is a missile heading for a target, and XX15 is pointing from the missile towards the target
 
- Set the pitch and roll counters to head in that direction
- Speed up or slow down, depending on where the ship is in relation to us

---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/program_flow_of_the_tactics_routine.html](https://elite.bbcelite.com/deep_dives/program_flow_of_the_tactics_routine.html)*

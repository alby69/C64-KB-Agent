---
title: Ship blueprints in the BBC Micro disc version
source_url: https://elite.bbcelite.com/deep_dives/ship_blueprints_in_the_disc_version.html
category: deep-dive
topics:
- basic
- assembly
- graphics
difficulty: intermediate
language: mixed
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

# Ship blueprints in the BBC Micro disc version

## How the BBC Micro disc version loads its ship blueprints into memory

When you launch from the space station in the disc version of BBC Micro Elite, there's an awful lot of disc activity - noticeably more than when you dock. This is because the flight code, once loaded, initiates a second load of the ship blueprints.

Unlike the 6502 Second Processor version, there is only room for around 12-13 ship blueprints at any one time, and because there are 32 different ship types in the disc version, with 29 distinct designs, a compromise has to be made. That compromise comes in the form of 16 files, called D.MOA through D.MOP, each of which contains 11-14 ship blueprints that can fit into memory at any one time. Here's the disc catalogue for the disc version, showing those files alongside the main game code binaries:

![The contents of the disc for the BBC Micro disc version of Elite](https://elite.bbcelite.com/images/disc/disc_contents.png) 

						Here's a list of the files and what they contain:

| # | Ship | [A](https://elite.bbcelite.com/disc/all/elite_ships_a.html) | [B](https://elite.bbcelite.com/disc/all/elite_ships_b.html) | [C](https://elite.bbcelite.com/disc/all/elite_ships_c.html) | [D](https://elite.bbcelite.com/disc/all/elite_ships_d.html) | [E](https://elite.bbcelite.com/disc/all/elite_ships_e.html) | [F](https://elite.bbcelite.com/disc/all/elite_ships_f.html) | [G](https://elite.bbcelite.com/disc/all/elite_ships_g.html) | [H](https://elite.bbcelite.com/disc/all/elite_ships_h.html) | [I](https://elite.bbcelite.com/disc/all/elite_ships_i.html) | [J](https://elite.bbcelite.com/disc/all/elite_ships_j.html) | [K](https://elite.bbcelite.com/disc/all/elite_ships_k.html) | [L](https://elite.bbcelite.com/disc/all/elite_ships_l.html) | [M](https://elite.bbcelite.com/disc/all/elite_ships_m.html) | [N](https://elite.bbcelite.com/disc/all/elite_ships_n.html) | [O](https://elite.bbcelite.com/disc/all/elite_ships_o.html) | [P](https://elite.bbcelite.com/disc/all/elite_ships_p.html) | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Missile](https://elite.bbcelite.com/disc/missile_ship_blueprint/variable/ship_missile.html) | * | * | * | * | * | * | * | * | * | * | * | * | * | * | * | * | 
| 2 | [Coriolis](https://elite.bbcelite.com/disc/ship_blueprints_a/variable/ship_coriolis.html) | * | * | * | * | * | * | * | * | ||||||||
| " | [Dodo](https://elite.bbcelite.com/disc/ship_blueprints_b/variable/ship_dodo.html) | * | * | * | * | * | * | * | * | ||||||||
| 3 | [Escape pod](https://elite.bbcelite.com/disc/ship_blueprints_a/variable/ship_escape_pod.html) | * | * | * | * | * | * | * | * | * | * | * | * | * | * | * | |
| 4 | [Alloy plate](https://elite.bbcelite.com/disc/ship_blueprints_a/variable/ship_plate.html) | * | * | * | * | * | * | * | * | ||||||||
| 5 | [Canister](https://elite.bbcelite.com/disc/ship_blueprints_a/variable/ship_canister.html) | * | * | * | * | * | * | * | * | * | * | * | * | * | * | * | * | 
| 6 | [Boulder](https://elite.bbcelite.com/disc/ship_blueprints_b/variable/ship_boulder.html) | * | * | * | * | * | |||||||||||
| 7 | [Asteroid](https://elite.bbcelite.com/disc/ship_blueprints_c/variable/ship_asteroid.html) | * | * | * | * | * | * | * | |||||||||
| 8 | [Splinter](https://elite.bbcelite.com/disc/ship_blueprints_c/variable/ship_splinter.html) | * | * | * | * | * | * | * | |||||||||
| 9 | [Shuttle](https://elite.bbcelite.com/disc/ship_blueprints_h/variable/ship_shuttle.html) | * | |||||||||||||||
| 10 | [Transporter](https://elite.bbcelite.com/disc/ship_blueprints_f/variable/ship_transporter.html) | * | |||||||||||||||
| 11 | [Cobra Mk III](https://elite.bbcelite.com/disc/ship_blueprints_b/variable/ship_cobra_mk_3.html) | * | * | * | * | * | * | * | * | * | * | * | |||||
| 12 | [Python](https://elite.bbcelite.com/disc/ship_blueprints_a/variable/ship_python.html) | * | * | * | |||||||||||||
| 13 | [Boa](https://elite.bbcelite.com/disc/ship_blueprints_c/variable/ship_boa.html) | * | * | ||||||||||||||
| 14 | [Anaconda](https://elite.bbcelite.com/disc/ship_blueprints_l/variable/ship_anaconda.html) | * | |||||||||||||||
| 15 | [Rock hermit](https://elite.bbcelite.com/disc/ship_blueprints_c/variable/ship_asteroid.html) | * | * | * | * | * | * | * | |||||||||
| 16 | [Viper](https://elite.bbcelite.com/disc/ship_blueprints_a/variable/ship_viper.html) | * | * | * | * | * | * | * | * | * | * | * | * | * | * | * | * | 
| 17 | [Sidewinder](https://elite.bbcelite.com/disc/ship_blueprints_a/variable/ship_sidewinder.html) | * | * | * | * | * | * | * | * | * | * | * | * | * | |||
| 18 | [Mamba](https://elite.bbcelite.com/disc/ship_blueprints_a/variable/ship_mamba.html) | * | * | * | * | * | * | * | * | * | |||||||
| 19 | [Krait](https://elite.bbcelite.com/disc/ship_blueprints_a/variable/ship_krait.html) | * | * | * | * | * | * | * | * | * | * | * | * | ||||
| 20 | [Adder](https://elite.bbcelite.com/disc/ship_blueprints_b/variable/ship_adder.html) | * | * | * | * | ||||||||||||
| 21 | [Gecko](https://elite.bbcelite.com/disc/ship_blueprints_d/variable/ship_gecko.html) | * | * | * | * | * | * | * | |||||||||
| 22 | [Cobra Mk I](https://elite.bbcelite.com/disc/ship_blueprints_d/variable/ship_cobra_mk_1.html) | * | * | * | * | * | * | ||||||||||
| 23 | [Worm](https://elite.bbcelite.com/disc/ship_blueprints_b/variable/ship_worm.html) | * | * | ||||||||||||||
| 24 | [Cobra Mk III](https://elite.bbcelite.com/disc/ship_blueprints_a/variable/ship_cobra_mk_3_p.html) P | * | * | * | * | * | |||||||||||
| 25 | [Asp Mk II](https://elite.bbcelite.com/disc/ship_blueprints_n/variable/ship_asp_mk_2.html) | * | * | ||||||||||||||
| 26 | [Python](https://elite.bbcelite.com/disc/ship_blueprints_i/variable/ship_python_p.html) P | * | * | ||||||||||||||
| 27 | [Fer-de-lance](https://elite.bbcelite.com/disc/ship_blueprints_a/variable/ship_fer_de_lance.html) | * | * | ||||||||||||||
| 28 | [Moray](https://elite.bbcelite.com/disc/ship_blueprints_k/variable/ship_moray.html) | * | |||||||||||||||
| 29 | [Thargoid](https://elite.bbcelite.com/disc/ship_blueprints_d/variable/ship_thargoid.html) | * | * | ||||||||||||||
| 30 | [Thargon](https://elite.bbcelite.com/disc/ship_blueprints_d/variable/ship_thargon.html) | * | * | ||||||||||||||
| 31 | [Constrictor](https://elite.bbcelite.com/disc/ship_blueprints_g/variable/ship_constrictor.html) | * | 

Notes:

- Only the BBC Micro disc version and Elite-A use ship files: all the other versions of Elite store all ship blueprints in memory. Elite-A has its own set of ship files - see the deep dive on [ship blueprints in Elite-A](https://elite.bbcelite.com/elite-a_ship_blueprints.html)for details.
- The missile blueprint is always present in memory (in the disc version, it lives above screen memory at location &7F00).
- Every ship file contains blueprints for the missile, cargo canister, Viper and Cobra Mk III (either trader or pirate).
- All but one ship file contain the blueprint for the escape pod: file "M" does not. The ships still have escape pods configured in their NEWB bytes, so if they reach the point where they choose to launch their escape pods, the pods won't actually spawn (though their ships will still fall dormant). See the deep dive on [advanced tactics with the NEWB flags](https://elite.bbcelite.com/advanced_tactics_with_the_newb_flags.html)for more details.
- Rock hermits (ship type 15) use the Asteroid blueprint.
- The two ships marked P are pirate versions of the Python and Cobra Mk III, which have their own blueprints with different attributes to the non-pirate versions.

Given the table above, let's see how the disc version works out which one of these files to load when we launch from the station.

## Choosing a file to load

													 -----------------------

						In most systems, the ship blueprints file that gets loaded is randomly chosen, but there are some rules around the range of files that can be picked, depending on the system we are in. The [LOMOD](https://elite.bbcelite.com/disc/flight/subroutine/lomod.html) routine is the core loading routine, and it chooses a number between 0 and 15, converts that into a letter between A and P, and then loads the relevant blueprints file, from D.MOA to D.MOP.

Here are the rules for generating the number between 0 and 15:

- If we are in the Constrictor's system in mission 1 (Orarra in the first galaxy), we always choose 6 (for file D.MOG), as that's the only file that contains the Constrictor blueprint
- We now construct a number, as follows:
								- Bit 0:
										- 0 for systems with tech level 0-9 (so we always load the Coriolis station blueprint)
- 1 for systems with tech level 10-14 (so we always load the Dodo station blueprint)
 
- Bit 1:
										- 0 for dangerous systems (anarchy, feudal, multi-government)
- 1 for all other, safer systems
 
- Bit 2: random
- Bit 3: random
- Bits 4-7: 0
 
- Bit 0:
										
- If mission 2 has started and we have picked up the plans, or we are in witchspace, we override this choice with D.MOC (low tech systems) or D.MOD (high tech systems), as these are the only two files containing Thargoids and Thargons

This means that, outside of the mission and witchspace overrides:

- Low tech level systems load files A, C, E, G, I, K, M, O (which contain the Coriolis station)
								- Of which dangerous low tech systems load files A, E, I, M
- Of which safer low tech systems load files C, G, K, O
 
- High tech level systems load files B, D, F, H, J, L, N, P (which contain the Dodo station)
								- Of which dangerous high tech systems load files B, F, J, N
- Of which safer high tech systems load files D, H, L, P
 
- Dangerous system load files A, B, E, F, I, J, M, N
								- Of which dangerous low tech systems load files A, E, I, M
- Of which dangerous high tech systems load files B, F, J, N
 
- Safer system load files C, D, G, H, K, L, O, P
								- Of which safer low tech systems load files C, G, K, O
- Of which safer high tech systems load files D, H, L, P
 

So now you know what all that extra chunka-chunka is about when you hit the launch button in the disc version.

---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/ship_blueprints_in_the_disc_version.html](https://elite.bbcelite.com/deep_dives/ship_blueprints_in_the_disc_version.html)*

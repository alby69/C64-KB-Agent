---
title: Buying and flying ships in Elite-A
source_url: https://elite.bbcelite.com/deep_dives/elite-a_buying_and_flying_ships.html
category: deep-dive
topics:
- basic
- assembly
difficulty: beginner
language: mixed
hardware:
- KERNAL
- SID
- CIA
- BASIC ROM
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

# Buying and flying ships in Elite-A

## What it's like to save up for and fly your dream ship in Elite-A

In the original Elite, it's all about the Cobra Mk III. It has four missile slots, it has four laser mounts, it has a cargo capacity of 20 tonnes that can be expanded to 35 tonnes... and if you don't like it, tough. You are a Cobra Mk III pilot, and that's that.

Angus Duggan's Elite-A is different. You start off in an Adder, and you can buy and fly lots of other ships - 15 of them in total. In order of increasing price, you can work your way up from the Adder to the Gecko, Moray, Cobra Mk I, Iguana, Ophidian, Chameleon, Cobra Mk III, Fer-de-Lance, Ghavial, Monitor, Python, Boa, Asp Mk II and Anaconda. The cockpit and controls remain the same, but different ships handle differently in flight, and they all support different levels of equipment and cargo.

![The Elite-A ship-buying screen](https://elite.bbcelite.com/images/elite-a/buying_ships.png) 

						Let's look at how Angus added all these different flyable ships to Elite-A.

## Buying ships in Elite-A

													 -----------------------

						Buying ships is pretty straightforward. The price list is stored in the [new_ships](https://elite.bbcelite.com/elite-a/docked/variable/new_ships.html) table, along with the ship names, and the process of buying and part-exchanging ships is handled by the [n_buyship](https://elite.bbcelite.com/elite-a/docked/subroutine/n_buyship.html) routine, which is called from the [EQSHP](https://elite.bbcelite.com/elite-a/docked/subroutine/eqshp.html) routine if CTRL is being held down. The range of ships on offer increases with the economy of the current system, with the number of ships for sale being given by the following:

15 - 2 * economy

The current system's economy ranges from 0 to 7, so the number of ships for sale is smaller in less advanced economies, and ranges from all 15 ship types for rich industrial economies, down to just one, the Adder, for poor agricultural economies.

When we buy a new ship, the price of our original ship is refunded, and we get to climb board our shiny, new purchase. Internally, this is what happens:

- Memory between LASER (the start of our current ship's equipment table) and LASER+36 (our legal status in FIST) is zeroed, so buying a ship not only removes all the equipment we had installed in the previous ship (which is why it's wise to sell all your equipment before buying a new one), but it also resets our legal status to clean.
- The type of ship we just bought is stored in [cmdr_type](https://elite.bbcelite.com/elite-a/docked/workspace/up.html#cmdr_type), which is in the current ship data block in the UP workspace, alongside all the other details of our ship's equipment (cmdr_type actually uses one of the unused bytes that were originally put in for up and down lasers, a feature that was built into early versions of the original game, but was later dropped without reclaiming the equipment bytes). This value is also saved as part of the commander save file at[NA%](https://elite.bbcelite.com/elite-a/loader/variable/na_per_cent.html).
- The [n_load](https://elite.bbcelite.com/elite-a/docked/subroutine/n_load.html)routine is called to load the flight characteristics and set the name token for our new ship.
- Our fuel level is set to the hyperspace range of our new ship, so our new ship comes with a full tank.
- The dashboard's missile indicators are reset so they show the correct number of missiles fitted to our new ship (which will be zero).

The meat of the above process is in the [n_load](https://elite.bbcelite.com/elite-a/docked/subroutine/n_load.html) routine, which does two things:

- Extended text token 132 in the QQ18 table is updated with the name of the ship type, so that printing token 132 always shows our current ship type.
- The flight characteristics of the new ship type are copied from the [new_details](https://elite.bbcelite.com/elite-a/docked/variable/new_details.html)table to a new section of our current ship data block, between[new_pulse](https://elite.bbcelite.com/elite-a/docked/workspace/up.html#new_pulse)and[new_max](https://elite.bbcelite.com/elite-a/docked/workspace/up.html#new_max).

The flight characteristics form the core of flying new ships in Elite-A, so let's take a deeper look at what's going on here.

## Flying ships in Elite-A

													 -----------------------

						Each ship type in Elite-A comes with its own set of flight characteristics. These are stored in the [new_details](https://elite.bbcelite.com/elite-a/docked/variable/new_details.html) table, and when we buy a new ship, these values are copied into a new set of locations in the current ship data block. Here's a list of all the flight characteristics and their locations in the current ship data block, along with links to the code that implements them:

- [new_pulse](https://elite.bbcelite.com/elite-a/docked/workspace/up.html#new_pulse)contains the power level of pulse lasers when fitted to this ship type. As with all the laser changes, this simply changes the power level stored in LASER though LASER+3 for this type of laser - the higher the level, the more damage it causes.
- [new_beam](https://elite.bbcelite.com/elite-a/docked/workspace/up.html#new_beam)contains the power level of beam lasers when fitted to this ship type.
- [new_military](https://elite.bbcelite.com/elite-a/docked/workspace/up.html#new_military)contains the power level of military lasers when fitted to this ship type.
- [new_mining](https://elite.bbcelite.com/elite-a/docked/workspace/up.html#new_mining)contains the power level of mining lasers when fitted to this ship type.
- [new_mounts](https://elite.bbcelite.com/elite-a/docked/workspace/up.html#new_mounts)contains the available laser mounts in this ship (1 = Front only, 2 = Front and rear, 4 = Front, rear, left and right). This is used to restrict the range of available views in the- [qv](https://elite.bbcelite.com/elite-a/docked/subroutine/qv.html)routine, which is called when buying or selling lasers.
- [new_missiles](https://elite.bbcelite.com/elite-a/docked/workspace/up.html#new_missiles)contains the maximum number of missiles that can be fitted to this ship type. This number is checked when buying new missiles in- [EQSHP](https://elite.bbcelite.com/elite-a/docked/subroutine/eqshp.html), allowing a larger maximum value to be stored in NOMSL (the current number of missiles) for ships that support more missiles, or a smaller maximum value for those that don't.
- [new_shields](https://elite.bbcelite.com/elite-a/docked/workspace/up.html#new_shields)contains this ship type's shield level. If our ship is damaged and the level of damage is less than our shield level, then the ship emerges unscathed. If the damage level is greater than the shield level, then the damage level is reduced by the shield level before being applied to the ship (i.e. the shields absorb the amount of damage given in new_shields). See the- [n_oops](https://elite.bbcelite.com/elite-a/flight/subroutine/n_oops.html)routine for the associated code.
- [new_energy](https://elite.bbcelite.com/elite-a/docked/workspace/up.html#new_energy)contains this ship type's ship energy refresh rate when fitted with an energy unit. This value is stored in the- [ENGY](https://elite.bbcelite.com/elite-a/docked/workspace/up.html#engy)variable, which contains the rate of our current ship's energy refresh rate, just as it does in all versions of Elite (it's just that it's always 1 in the other versions, or 2 if you have the naval energy unit from mission 2).
- [new_speed](https://elite.bbcelite.com/elite-a/docked/workspace/up.html#new_speed)contains this ship type's maximum speed, which is checked in- [part 3 of the main flight loop](https://elite.bbcelite.com/elite-a/flight/subroutine/main_flight_loop_part_3_of_16.html)when accelerating.
- [new_hold](https://elite.bbcelite.com/elite-a/docked/workspace/up.html#new_hold)contains the amount of free space in this ship type's hold (though the value is actually the amount of free space plus 1, as this makes the maths slightly easier). In Elite-A, hold space is taken up by both equipment and cargo, so this value is checked in a number of places, such as- [tnpr1](https://elite.bbcelite.com/elite-a/flight/subroutine/tnpr1.html)(when scooping),- [tnpr](https://elite.bbcelite.com/elite-a/docked/subroutine/tnpr.html)(when buying cargo) and- [EQSHP](https://elite.bbcelite.com/elite-a/docked/subroutine/eqshp.html)(when buying equipment).
- [new_range](https://elite.bbcelite.com/elite-a/docked/workspace/up.html#new_range)contains this ship type's hyperspace range (i.e. the size of the fuel tank). The range is stored as the number of light years multiplied by 10, so a value of 1 represents 0.1 light years, while 70 represents 7.0 light years. This figure is only used when buying fuel in- [EQSHP](https://elite.bbcelite.com/elite-a/docked/subroutine/eqshp.html), as the fuel level in- [QQ14](https://elite.bbcelite.com/elite-a/docked/workspace/up.html#qq14)can already support larger numbers for larger tanks.
- [new_costs](https://elite.bbcelite.com/elite-a/docked/workspace/up.html#new_costs)contains the price table offset for this ship type. In Elite-A the- [PRXS](https://elite.bbcelite.com/elite-a/docked/variable/prxs.html)table (which contains equipment prices) has multiple sections, for the different types of ship we can buy, and the offset into this table for this ship type is held here. See the- [EQSHP](https://elite.bbcelite.com/elite-a/docked/subroutine/eqshp.html)routine for more on buying equipment.
- [new_max](https://elite.bbcelite.com/elite-a/docked/workspace/up.html#new_max)contains this ship type's maximum pitch/roll rate. This limits the maximum rate of pitching and rolling using a simple restriction in- [part 2 of the main flight loop](https://elite.bbcelite.com/elite-a/flight/subroutine/main_flight_loop_part_2_of_16.html).
- [new_min](https://elite.bbcelite.com/elite-a/docked/workspace/up.html#new_min)contains this ship type's minimum pitch/roll rate. This is always equal to 255 - new_max, so when we buy a new ship, the correct value is calculated rather than being fetched from the new_details table (there are default values for this in the new_details table, though these are commented out). It limits the minimum rate of pitching and rolling using a simple restriction in- [part 2 of the main flight loop](https://elite.bbcelite.com/elite-a/flight/subroutine/main_flight_loop_part_2_of_16.html).
- [new_space](https://elite.bbcelite.com/elite-a/docked/workspace/up.html#new_space)has a label and a reserved byte in the original source, but it appears to be unused, so this is presumably a flight characteristic that was dropped at some stage.

The flight characteristics are fixed for each specific ship type, and they are extracted from the new_details table every time we buy a new ship or load a new commander file. In this way the characteristics don't need to be saved, any more than the ship blueprint details need to be saved; only the ship type is saved in the commander file, and the flight characteristics are expanded at load time.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
15 - 2 * economy
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/elite-a_buying_and_flying_ships.html](https://elite.bbcelite.com/deep_dives/elite-a_buying_and_flying_ships.html)*

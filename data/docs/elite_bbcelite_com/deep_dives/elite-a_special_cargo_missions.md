---
title: Special cargo missions
source_url: https://elite.bbcelite.com/deep_dives/elite-a_special_cargo_missions.html
category: deep-dive
topics:
- basic
- assembly
difficulty: beginner
language: mixed
hardware:
- KERNAL
- CIA
related:
- keyboard-handling
- joystick-reading
- memory-map
- kernal-routines
- cia-registers
scraped_at: '2026-07-14'
---

# Special cargo missions

## Procedurally generating delivery missions and tracking progress

The special cargo delivery mission is one of the things Angus Duggan added to Elite-A to make things a bit more interesting on the gameplay front. The concept is pretty familiar to anyone who has played any of the later games in the Elite series: you pick up a mission to deliver an unspecified item to a distant system, paying a small fee to take on the mission, and the quicker you get to your destination, the higher the payout. Dawdle too long, and you might even lose the mission completely, making a loss on the deal. Some missions may adversely affect your legal status, but illegal missions have higher payouts. It might not be glamorous work, but somebody's got to do it.

The special cargo screen appears if you press CTRL-f1 when docked:

![The Elite-A Special Cargo screen](https://elite.bbcelite.com/images/elite-a/special_cargo.png) 

						Under the hood, delivery missions are a lot more interesting than the above description makes them sound. Let's take a look at how special cargos and their delivery missions work in Elite-A.

## Delivering the goods

													 --------------------

						Let's start by looking at what an in-progress mission looks like (we'll cover the process of generating new missions below). If we have a special cargo in the hold and we're on our way to the destination, these are the pertinent variables:

- [cmdr_cour](https://elite.bbcelite.com/elite-a/docked/workspace/up.html#cmdr_cour)contains the current mission reward. This 16-bit number starts out at a high value, and is halved every time we dock. This is the only time it is reduced - it isn't halved on hyperspace jumps, only on docking.
- [cmdr_courx](https://elite.bbcelite.com/elite-a/docked/workspace/up.html#cmdr_courx)and- [cmdr_coury](https://elite.bbcelite.com/elite-a/docked/workspace/up.html#cmdr_coury)contain the galactic (x, y) coordinates of the destination system for this mission.

If we complete the mission by docking at the destination system, then we get paid the number of credits left in the cmdr_cour variable, divided by 10 (as credits in Elite are always stored to one decimal place, so 100.0 credits is stored as 1000). This means that if we do a delivery mission by fuel scooping and hyperspacing only, with no docking, then we will get the maximum payout, but if we decide to dock *en route*, that will seriously eat into our profits as the payout will halve each time we do. Indeed, the reward can halve all the way to zero, as it's implemented with a right shift, so if we dock too many times, the mission will simply cease to exist (as we only have a mission in progress if cmdr_cour is greater than zero).

The [cour_dock](https://elite.bbcelite.com/elite-a/docked/subroutine/cour_dock.html) routine in the docked code is called every time we dock, and it takes care of reducing the reward or, if we have just arrived at the destination, paying out on delivery. The three variables are also saved as part of the commander save file at [NA%](https://elite.bbcelite.com/elite-a/loader/variable/na_per_cent.html), where they slot nicely into the four unused bytes just before the missile count at NOMSL (we need four bytes as cmdr_cour is a two-byte number). This means that when we save the game, we also save the mission status, which is essential for long delivery journeys.

This is all pretty straightforward, but the really interesting part is how Angus designed the mission generation system, so let's look at that next.

## Generating special cargo missions

													 ---------------------------------

						If we're interested in taking on a delivery mission, then we can bring up the Special Cargo screen by pressing CTRL-f1 when docked. This shows a list of destinations and mission costs, which remain the same while we are docked (though it does refresh if we choose to pay a docking fee). Sometimes there are lots of missions and sometimes there are none, but the list is different every time we dock, even if we've been to that station before.

It's no surprise, then, to discover that the list of available special cargo missions is produced using procedural generation. This process takes a variety of factors and uses them to generate a list of missions. Angus chose factors that don't change while we are docked, so the list stays the same every time it is generated during the same station visit, but as soon as we launch (or pay the docking fee), these factors change and so does the list of available missions.

When we actually take on a mission, the only variables we need to store are [cmdr_cour](https://elite.bbcelite.com/elite-a/docked/workspace/up.html#cmdr_cour), [cmdr_courx](https://elite.bbcelite.com/elite-a/docked/workspace/up.html#cmdr_courx) and [cmdr_coury](https://elite.bbcelite.com/elite-a/docked/workspace/up.html#cmdr_coury) (see above). The mission generation process therefore needs to generate not only a user-friendly menu of available missions, but it also needs to generate a reward, cost and destination for each mission. Then when we choose a mission, we can pay the mission cost and, assuming the fee transaction goes through, we can populate the three mission variables to kick the mission off.

This process is implemented in the [cour_buy](https://elite.bbcelite.com/elite-a/docked/subroutine/cour_buy.html) routine, which is called from the [TT219](https://elite.bbcelite.com/elite-a/docked/subroutine/tt219.html) routine if CTRL is being held down. If we aren't already doing a delivery mission, cour_buy gets to work generating a list of available missions to display on screen. This process involves creating a sequence of systems from across the galaxy, and generating a mission for each one until we have either run out of systems or we've generated enough missions.

This sequence of systems is defined by a starting system, and a step number that is added to the system number each time to get the next system in the sequence. Let's call the starting system i and the step j, and let's call the maximum menu size n. We therefore generate our mission list by first generating a mission to system i, then to system i + j, then to system i + 2j, and so on until we have either run out of systems (i.e. the system number is now greater than 255, the highest valid system number), or we already have enough missions in the list (i.e. we have already generated n missions).

So given a set of i, j and n values, we can generate a mission list, and we can repeat the process. This is what we want in order to be able to offer mission lists that are the same for the duration of a station visit, but change once we leave and come back. Let's look at how we set these three values in the first place.

## Setting the mission values

													 --------------------------

						So that we always generate the same mission list during each station visit, we need to choose values of i, j and n that won't change while we go about our station business, buying cargo or checking the encyclopedia or whatever else takes our fancy. This is how we generate values of i, j and n for each station visit:

- i contains the first system to try:

```
      i = QQ26 EOR QQ0 EOR QQ1 EOR FIST EOR TALLY
```
							```
      j = FIST + GCNT + cmdr_type
```
							```
      n = i + j - cmdr_courx - cmdr_coury
```
						
						Running through the variables that are used above, we can see that they all remain stable during a station visit:

- [QQ26](https://elite.bbcelite.com/elite-a/docked/workspace/up.html#qq26)contains the random value used to randomise market data
- [QQ0](https://elite.bbcelite.com/elite-a/docked/workspace/up.html#qq0)contains the current system's galactic x-coordinate
- [QQ1](https://elite.bbcelite.com/elite-a/docked/workspace/up.html#qq1)contains the current system's galactic y-coordinate
- [FIST](https://elite.bbcelite.com/elite-a/docked/workspace/up.html#fist)contains our legal status
- [TALLY](https://elite.bbcelite.com/elite-a/docked/workspace/up.html#tally)contains the low byte of our combat rank
- [GCNT](https://elite.bbcelite.com/elite-a/docked/workspace/up.html#gcnt)contains the current galaxy number
- [cmdr_type](https://elite.bbcelite.com/elite-a/docked/workspace/up.html#cmdr_type)contains our current ship type
- [cmdr_courx](https://elite.bbcelite.com/elite-a/docked/workspace/up.html#cmdr_courx)and- [cmdr_coury](https://elite.bbcelite.com/elite-a/docked/workspace/up.html#cmdr_coury)contain the coordinates of the last delivery mission we took on, or 0 if we have never done a delivery mission

These values will only change if we change system, pay a docking fee to update the market (which will change the value of QQ26), or buy a new ship (which will change the value of cmdr_type). In all these cases we do indeed want to change the mission menu, but if instead we just sit tight, selling some equipment or checking out the charts or whatever else one does in a space station, then the values of i, j and n won't change, and neither will the mission menu.

Now we have our values, let's look at how we can generate a mission list from them.

## Generating a menu of delivery missions

													 --------------------------------------

						As noted above, we generate a list of missions by stepping through a sequence of systems, generating missions as we go and displaying them in a menu. Given a set of values in i, j and n, this is how we do it:

- Generate a mission for system i, assuming it isn't the same as the current system
- Set i = i + j
- Repeat steps 1 and 2 until we have either generated n missions, or i > 255

This is essentially what happens in the [cour_loop part of the cour_buy](https://elite.bbcelite.com/elite-a/docked/subroutine/cour_buy.html#cour_loop) routine, which calls the [cour_count](https://elite.bbcelite.com/elite-a/docked/subroutine/cour_count.html) routine to generate the missions and update the loop counters.

Of course, the above is an algorithm rather than an implementation, so here are the actual steps that the code uses to generate the mission menu:

- Set x = 0
- Set c = 0
- Do the following loop:
								- First, we fetch the details for system x + i, using the following inner loop:
										- Get the three 16-bit system seeds for system x by calling [TT20](https://elite.bbcelite.com/elite-a/docked/subroutine/tt20.html)
- Increment x
- If x > 255 then we have run out of systems in the galaxy to work with, so stop generating new missions, as we are done
- Decrement i
- If i > 0, loop back to do the next system
 
- Get the three 16-bit system seeds for system x by calling 
- If the three 16-bit system seeds we just fetched do not match the current system, then generate a mission from these seeds, display the mission in the menu, and store the details in memory
- Increment c
- Set i = j
- Loop back until c >= n, at which point we have generated n menu entries and we are done
 
- First, we fetch the details for system x + i, using the following inner loop:
										

For reference, in the [cour_buy](https://elite.bbcelite.com/elite-a/docked/subroutine/cour_buy.html) routine, i is stored in INWK, j is stored in INWK+1, c is stored in INWK+3, x is stored in INWK+6, and n is stored in QQ25.

Once the menu has been displayed using the above process, we wait for the player to choose a mission, and if they do, we copy the relevant mission details into cmdr_cour, cmdr_courx and cmdr_coury. The only missing part is how we generate these mission details for each specific destination in the menu, so let's look at that part next.

## Procedurally generating one mission

													 -----------------------------------

						The [cour_count](https://elite.bbcelite.com/elite-a/docked/subroutine/cour_count.html) routine generates the details of a specific mission, given the value of j and the set of three 16-bit system seeds for the mission's destination (see the deep dive on [galaxy and system seeds](https://elite.bbcelite.com/galaxy_and_system_seeds.html) for details of the system seeds and the data they represent). Let's look at how this works by taking each mission detail in turn.

The first one is easy: the coordinates of the mission's destination. We already have a set of seeds for the system in question, and s1_hi contains the x-coordinate and s0_hi the y-coordinate.

The next one is the legality of this mission, where zero means it is perfectly legal but higher values are increasingly damaging to our own legal status. Specifically, when we take on a mission, its legality is added to our legal status in FIST, so if it's zero then it doesn't affect us, but if it's non-zero, it makes us more notorious, with higher values making us even more criminal. The legal status is calculated as follows:

s1_hi EOR s2_hi EOR j

If this value is less than our current legal status in FIST, then it is used as the mission's legality, otherwise the legality is set to 0 (perfectly legal). This means we are only offered missions that are as naughty as we are, which makes sense - the more criminal we are, the dodgier the offers.

The final two pieces of information are the mission reward and the size of the fee we have to pay to take the mission. The cost of the fee is approximately one-eighth of the reward, and the reward is based on the distance to the destination, so we start off by calculating the distance using Pythagoras:

delta_x = |destination_x - current_x| delta_y = |destination_y - current_y| / 2 dist = SQRT(delta_x ^ 2 + delta_y ^ 2)

We halve the y-coordinate distance because the galaxy in Elite is rectangular rather than square, and is twice as wide (x-axis) as it is high (y-axis), so to get a distance that matches the shape of the long-range galaxy chart, we need to halve the distance between the vertical y-coordinates.

Next, we calculate the following:

A = max(dist, (s0_hi EOR s2_hi EOR j) / 8) OR legality

This takes a pretty random value (s0_hi EOR s2_hi EOR j) that is always the same for this particular station visit, and divides it by 8 to give a range of 0 to 63. If this is less than the distance we just calculated then we bump it up so it's always at least as big as the distance, and then we potentially bump it up further by OR'ing it with the legality, which will be higher with more dubious missions.

In other words, A is a pretty random figure that is higher for longer missions, and probably higher again for illegal deliveries. We use this figure to calculate the reward and cost as follows:

cost(1 0) = (A A) / 8 reward(1 0) = (A cost)

So the low bytes of both are the same, and the high byte of the reward is 8 times the high byte of the cost.

And that's how Elite-A generates missions in a procedural way that guarantees the mission menu will stay the same every time we generate it, while still appearing to be pretty random. Very clever stuff!

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
i = QQ26 EOR QQ0 EOR QQ1 EOR FIST EOR TALLY
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
j = FIST + GCNT + cmdr_type
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
n = i + j - cmdr_courx - cmdr_coury
```

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`s1_hi`** (unknown): No description available

```assembly
s1_hi EOR s2_hi EOR j
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
delta_x = |destination_x - current_x|

  delta_y = |destination_y - current_y| / 2

  dist = SQRT(delta_x ^ 2 + delta_y ^ 2)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
A = max(dist, (s0_hi EOR s2_hi EOR j) / 8) OR legality
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
cost(1 0) = (A A) / 8

  reward(1 0) = (A cost)
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/elite-a_special_cargo_missions.html](https://elite.bbcelite.com/deep_dives/elite-a_special_cargo_missions.html)*

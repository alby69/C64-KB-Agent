---
title: The Trumbles mission
source_url: https://elite.bbcelite.com/deep_dives/the_trumbles_mission.html
category: deep-dive
topics:
- sprite programming
- basic
- assembly
difficulty: intermediate
language: mixed
hardware:
- CPU
- BASIC ROM
- KERNAL
- VIC-II
related:
- raster-interrupts
- memory-map
- kernal-routines
- sprite-programming
- vic-ii-registers
scraped_at: '2026-07-14'
---

# The Trumbles mission

## Furry fun in the Commodore 64 and NES versions of Elite

Compared to the BBC Micro version from which it was converted, the Commodore 64 version of Elite comes with an extra feature in the form of the Trumbles mission. Offered when you reach 6553.6 credits (in the NES version) or 5017.6 credits (in the Commodore 64 version), it comes in the form of an offer you can't rightly refuse (though you can if you like).

![The Trumbles mission briefing view in Commodore 64 Elite](https://elite.bbcelite.com/images/c64/trumbles_mission.png) 

						This mission is also present in the NES version, where the invitation looks like this:

![The Trumbles mission briefing view in NES Elite](https://elite.bbcelite.com/images/nes/missions/trumbles.png) 

						In a more readable form, this is the invitation:

Good day Commander MARK, allow me to introduce myself. I am the Merchant Prince of Thrun and I find myself forced to sell my most treasured possession.

I am offering you, for the paltry sum of just 5000CR the rarest thing in the Known Universe.

Will you take it?

YES/NO


Who wouldn't say yes to this, even if it takes away most of our hard-earned cash? And so we agree to the deal, and our cargo hold then looks like this, with one furry "Little Squeaky" to keep us company:

![The Trumbles inventory view in NES Elite](https://elite.bbcelite.com/images/nes/missions/trumbles_inventory_1.png) 

						Thing is, if you play the game and come back to your inventory, this happens:

![The Trumbles inventory view in NES Elite](https://elite.bbcelite.com/images/nes/missions/trumbles_inventory_2.png) 

						And then this happens:

![The Trumbles inventory view in NES Elite](https://elite.bbcelite.com/images/nes/missions/trumbles_inventory_3.png) 

						And then this happens:

![The Trumbles inventory view in NES Elite](https://elite.bbcelite.com/images/nes/missions/trumbles_inventory_4.png) 

						And in case you think that having a Commodore 64 makes you immune, this happens:

![The Trumbles inventory view in Commodore 64 Elite](https://elite.bbcelite.com/images/c64/trumbles_inventory.png) 

						And so on. The problem is, this furry, friendly, cuddly and cute cargo really likes to breed, filling up the hold with offspring and devouring any food we might buy; you can even hear them chattering away as they keep multiplying.

Incidentally, as you can see above, the Commodore 64 version calls these critters "Trumbles" in the inventory, but in the NES version they are "Little Squeakys" - perhaps Nintendo felt that the term Trumbles was a bit too close to their trademarked inspiration, the Tribbles from Star Trek.

In the Commodore 64 version, stowed Trumbles will also hoof down any narcotics we buy, which presumably only encourages the noisy orgy kicking off in the cargo bay. The slightly less risqué NES version doesn't have narcotics but has rare species instead, but the Little Squeakys don't seem to want to eat any of them, presumably because they are one.

Exclusively to the Commodore 64 version, the Trumbles eventually make their way onto the canopy, courtesy of the machine's hardware sprites (see the deep dive on [sprite usage in Commodore 64 Elite](https://elite.bbcelite.com/sprite_usage_in_commodore_64_elite.html) for details). Here's a screen invasion of Trumbles in the Commodore 64 version:

As you can see, not only do the Trumbles invade the screen, but they're noisy little critters that crawl around everywhere, merrily obscuring the space view and dashboard.

In the NES version, the canopy stays mercifully clear, as the NES has better uses for its sprites (see the deep dive on [sprite usage in NES Elite](https://elite.bbcelite.com/sprite_usage_in_nes_elite.html) for details).
						

It turns out the only way to get rid of the little critters is to fly so close to the sun that they die off (they even survive the use of the Escape pod, so this is the only way). Unlike the Commodore 64 version, the NES version even has sound effects of them being euthanised in the hold as the temperatures climb - not so cute and furry now, eh!

It's a bit of light relief rather than a full-blown mission, but until you know the solution, it can really feel like the latter.

## The Trumble routines

													 --------------------

						Out of all the 6502 versions of Elite, the Trumbles mission only appears in the Commodore 64 and NES versions. The Commodore 64 version is the only one with sprites; the NES version is purely text-based.

As with the other missions, the [DOENTRY](https://elite.bbcelite.com/nes/bank_0/subroutine/doentry.html) routine contains all the Trumble logic, and the [TP](https://elite.bbcelite.com/disc/docked/workspace/up.html#tp) variable in the save file contains our status. The Trumble mission can be triggered at any point after we reach 6553.6 credits, so the only check is whether CASH+1 is greater than zero. If it is and we haven't already done the mission (i.e. bit 4 of TP is clear), then the mission briefing in text token 199 is shown by calling the [TBRIEF](https://elite.bbcelite.com/nes/bank_0/subroutine/tbrief.html) routine.

Once the mission is offered, bit 4 of TP is set so we don't offer the mission again. If the mission is accepted, then the number of Trumbles in the hold is set to 1 by incrementing the [TRIBBLE](https://elite.bbcelite.com/nes/common/workspace/wp.html#tribble) variable, and all the rest follows on from this innocuous step. The variable name gives a clue as to the inspiration for this mission; the name was changed to Trumble to avoid incurring the wrath of the owners of the Tribble™ name.

Trumbles breed in two places. They always breed when we jump into a new system, courtesy of the [SOLAR](https://elite.bbcelite.com/nes/bank_0/subroutine/solar.html) routine, and this is where they also consume any food or narcotics in the hold. There is also a 14% chance of them breeding in each iteration of the main loop via the code in [part 5 of the main game loop](https://elite.bbcelite.com/nes/bank_0/subroutine/main_game_loop_part_5_of_6.html#nolasct), which also looks after the noises that the Trumbles make.

In the Commodore 64 version, as you get more and more Trumbles, they start to appear as on-screen sprites. They crawl across the space view, courtesy of the [MVTRIBS](https://elite.bbcelite.com/c64/main/subroutine/mvtribs.html) routine. They spill over into the normally empty screen margins, too:

![The Trumbles in Commodore 64 Elite](https://elite.bbcelite.com/images/c64/trumbles_on_screen.png) 

						The high temperatures near the sun finally kill off our troublesome cargo, thanks to the code in [part 15 of the main flight loop](https://elite.bbcelite.com/nes/bank_0/subroutine/main_flight_loop_part_15_of_16.html). Not surprisingly, they make a racket as they go, until finally TRIBBLE reaches zero and our furry fun is over.

Goodness knows what would happen if you fed them after midnight. Best not to think about it...

---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/the_trumbles_mission.html](https://elite.bbcelite.com/deep_dives/the_trumbles_mission.html)*

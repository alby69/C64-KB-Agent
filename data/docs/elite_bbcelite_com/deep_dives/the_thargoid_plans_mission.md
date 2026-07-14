---
title: The Thargoid Plans mission
source_url: https://elite.bbcelite.com/deep_dives/the_thargoid_plans_mission.html
category: deep-dive
topics:
- basic
- assembly
difficulty: beginner
language: mixed
hardware:
- CPU
- SID
- BASIC ROM
- KERNAL
related:
- music-player
- sound-programming
- memory-map
- kernal-routines
- sid-registers
scraped_at: '2026-07-14'
---

# The Thargoid Plans mission

## Evading the Thargoid threat in the depths of the third galaxy

There are two missions in the enhanced versions of Elite (i.e. all 6502 versions except for the Acorn Electron and BBC Micro cassette). The first mission is described in the deep dive on [the Constrictor mission](https://elite.bbcelite.com/the_constrictor_mission.html), and once that is completed, it's only a matter of time before we see this screen again:

![The INCOMING MESSAGE screen in BBC Micro Elite](https://elite.bbcelite.com/images/missions/incoming.png) 

						This time the mission is slightly less convoluted, though it's probably more difficult. It's offered to pilots who are in the third galaxy and have a combat rating that is at least 3/8 of the way from Dangerous to Deadly, so that's quite a way through the game. The briefing looks like this:

![The first briefing screen for the Thargoid maps mission in BBC Micro Elite](https://elite.bbcelite.com/images/missions/mission_2a.png) 

						Or, in a more readable form:

Attention Commander MARK, I am Captain Fortesque of Her Majesty's Space Navy. We have need of your services again.

If you would be so good as to go to Ceerdi you will be briefed.

If successful, you will be well rewarded.

MESSAGE ENDS


What a tease! Of course, we now have to fly to Ceerdi, which is probably on the other side of the galaxy, if you're unlucky. This is what happened to me, with Ceerdi being a good 55.6 light-year journey away (it's the cross on the right):

![The Long-range Chart showing Ceerdi in BBC Micro Elite](https://elite.bbcelite.com/images/missions/ceerdi_long_range_chart.png) 

						Docking at Ceerdi brings up another incoming message, this time in two parts:

![The second briefing screen for the Thargoid maps mission in BBC Micro Elite](https://elite.bbcelite.com/images/missions/mission_2b.png) 

						![The third briefing screen for the Thargoid maps mission in BBC Micro Elite](https://elite.bbcelite.com/images/missions/mission_2c.png) 

						It reads as follows, complete with amusingly ironic spelling mistake:

Good day Commander MARK.

I am Agent Blake of Naval Intellegence.

As you know, the Navy have been keeping the Thargoids off your ass out in deep space for many years now. Well the situation has changed.

Our boys are ready for a push right to the home system of those mothers.

I have obtained the defence plans for their Hive Worlds. The beetles know we've got something but not what. If I transmit the plans to our base on Birera they'll intercept the transmission. I need a ship to make the run.

You're elected.

The plans are unipulse coded within this transmission.

You will be paid.

Good luck Commander.

MESSAGE ENDS


Of course, Birera is on the other side of the galaxy, a good 60.8 light years from Ceerdi:

![The Long-range Chart showing Birera in BBC Micro Elite](https://elite.bbcelite.com/images/missions/birera_long_range_chart.png) 

						And - you guessed it - the Thargoids have got wind of our little scheme, so every step of the way from Ceerdi to Birera, Thargoids and their accompanying Thargons make our lives pretty difficult.

Assuming we reach Birera, we get another incoming message, as follows:

![The debriefing screen for the Thargoid maps mission in BBC Micro Elite](https://elite.bbcelite.com/images/missions/mission_2d.png) 

						It reads:

Well done Commander.

You have served us well and we shall remember.

We did not expect the Thargoids to find out about you.

For the moment please accept this Navy Extra Energy Unit as payment.

MESSAGE ENDS


As mentioned, we now have a Naval Energy Unit fitted (though it's still called an Energy Unit in the Status Mode screen). This energy unit is much more effective, recharging the energy bars by three units each time, rather than the two units of the standard energy unit or the one unit of the standard Cobra Mk III. It's a very useful reward, and we also get awarded 256 kill points, which equates to one whole "Right On Commander!".

After all those Thargoids, we've earned it!

## The mission routines

													 --------------------

						The Thargoid Plans mission appears in every version of 6502 Elite apart from the BBC Micro cassette and Acorn Electron versions, which have no missions at all.

The logic is rather simpler in this mission than in the Constrictor mission. Again, the [DOENTRY](https://elite.bbcelite.com/disc/docked/subroutine/doentry.html) routine in the docked code contains all the mission logic, and the [TP](https://elite.bbcelite.com/disc/docked/workspace/up.html#tp) variable in the save file contains our status. The Constrictor mission leaves bits 0 and 1 of TP set to %10, which ensures that DOENTRY skips the Constrictor mission logic and starts applying the next mission's code, as follows:

- If bits 0-3 of TP are %0010, then the Constrictor mission is finished and the Thargoid mission is not yet in progress, so check the following:
								- Is TALLY+1 >= 5 (i.e. have we reached a combat rank of at least 3/8 of the way from Dangerous to Deadly)?
- Are we in galaxy 3?
 [BRIEF2](https://elite.bbcelite.com/disc/docked/subroutine/brief2.html)routine to display the initial "go to Ceerdi" briefing and set bit 2 of TP (so bits 0-3 of TP are now %0110). If the answer to either or both of these is "no", then we jump straight to the docking bay and skip the rest of the mission logic.
- If bits 0-3 of TP are %0110, then the Thargoid mission is in progress but we haven't yet picked up the plans from Ceerdi, so we now check whether we have just docked at Ceerdi at galactic coordinates (215, 84).
								- If we have reached Ceerdi, then we jump to the [BRIEF3](https://elite.bbcelite.com/disc/docked/subroutine/brief3.html)routine to display the briefing where we pick up the plans and set bits 0-3 of TP %1010.
- If we haven't reached Ceerdi yet, then we jump straight to the docking bay and skip the rest of the mission logic.
 
- If we have reached Ceerdi, then we jump to the 
- If bits 0-3 of TP are %1010, then the Thargoid mission is in progress and we have picked up the plans from Ceerdi, so we now check whether we have just docked at Birera at galactic coordinates (63, 72).
								- If we have reached Birera, then we jump to the [DEBRIEF2](https://elite.bbcelite.com/disc/docked/subroutine/debrief2.html)routine to display the congratulations message and get our reward. At this point bit 2 of TP is set, leaving bits 0-3 of TP set to %1110 to indicate that the mission is done and dusted, and to ensure that in future we pass through the above logic and either on to the docking bay (in the BBC versions) or into the logic for[the Trumbles mission](https://elite.bbcelite.com/the_trumbles_mission.html)(in the other 6502 versions).
- If we haven't reached Birera yet, then we jump straight to the docking bay and skip the rest of the mission logic.
 
- If we have reached Birera, then we jump to the 

There are no extended system description overrides in this mission, but the ship-spawning logic behaves differently if this mission is in progress. When we have the plans on-board, [part 4 of the main game loop](https://elite.bbcelite.com/disc/flight/subroutine/main_game_loop_part_4_of_6.html) will spawn a Thargoid and Thargon companion 22% of the time when spawning is considered. That's a lot of Thargoids over such a long journey. This continues until the mission is completed, at which point things go back to normal.
						

Here are some other points of note:

- The name of the Navy captain in the above message is always Fortesque, but it is implemented using the [MT27](https://elite.bbcelite.com/disc/docked/subroutine/mt27.html)routine, which is called when printing an EJMP 27 token from the extended token table. This shows a different name depending on the galaxy, but as we have to be in the third galaxy to so this mission, the captain's name is always Fortesque.
- In the NES version, the captain's name varies between different languages. In English he's Captain Fortesque, in German he's Käpitan Habsburg, and in French he's le capitain de Romanche.
- In the BBC Micro disc version, the mission status affects which ship data files are loaded. Specifically, the [LOMOD](https://elite.bbcelite.com/disc/flight/subroutine/lomod.html)routine ensures that ship blueprints file D.MOC (low tech systems) or D.MOD (high tech systems) are always loaded when we are carrying the plans, as these are the only two files containing the Thargoid and Thargon ship blueprints. See the deep dive on[ship blueprints in the disc version](https://elite.bbcelite.com/ship_blueprints_in_the_disc_version.html)for details.
- The incoming message text is token 216 in [TKN1](https://elite.bbcelite.com/disc/docked/variable/tkn1.html), the mission briefing telling us to go to Ceerdi is token 11, the briefing where we get the plans is token 222, and the mission debriefing is token 223.

For the Acornsoft versions, this is the last mission we're offered, as there are only two of them (this one and [the Constrictor mission](https://elite.bbcelite.com/the_constrictor_mission.html)). For the other 6502 versions there is one further mission, of sorts: see the deep dive on [the Trumbles mission](https://elite.bbcelite.com/the_trumbles_mission.html) for all the furry details.

---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/the_thargoid_plans_mission.html](https://elite.bbcelite.com/deep_dives/the_thargoid_plans_mission.html)*

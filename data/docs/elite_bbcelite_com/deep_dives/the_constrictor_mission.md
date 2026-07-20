---
title: The Constrictor mission
source_url: https://elite.bbcelite.com/deep_dives/the_constrictor_mission.html
category: deep-dive
topics:
- basic
- assembly
difficulty: intermediate
language: mixed
hardware:
- KERNAL
- SID
- CPU
- BASIC ROM
related:
- sid-registers
- sound-programming
- memory-map
- kernal-routines
- music-player
scraped_at: '2026-07-20'
---

# The Constrictor mission

## Hunting high and low for the stolen Constrictor

I can still remember the thrill of my first mission in Elite. I'd cut my teeth on the BBC Micro cassette version of the game, which didn't have any missions, but I eventually saved up enough pocket money for a disc drive, and the first thing I did was to post my Elite cassette to Acornsoft to be upgraded into the disc version. And then, one day, when I was flying around galaxy 1, minding my own business, I docked and saw this:

![The INCOMING MESSAGE screen in BBC Micro Elite](https://elite.bbcelite.com/images/missions/incoming.png) 

						I nearly fell out of my pilot seat. What was this? Could this be a mission, like the ones I'd heard about in the Acorn press? And then this wondrous sight appeared, spinning away in the middle of the screen:

![The rotating Constrictor in BBC Micro Elite](https://elite.bbcelite.com/images/missions/mission_1_ship.png) 

						By this point I knew all the ships by sight, and this was a new one. It slowly drifted up towards the top of the screen, and then I hit the jackpot:

![The first briefing screen for the Constrictor mission in BBC Micro Elite](https://elite.bbcelite.com/images/missions/mission_1a.png) 

						Finally, a mission! And a mission so detailed that it needed a second screen:

![The second briefing screen for the Constrictor mission in BBC Micro Elite](https://elite.bbcelite.com/images/missions/mission_1b.png) 

						I scribbled down the details, which looked like this:

Greetings Commander MARK, I am Captain Curruthers of Her Majesty's Space Navy and I beg a moment of your valuable time.

We would like you to do a little job for us.

The ship you see here is a new model, the Constrictor, equiped with a top secret new shield generator.

Unfortunately it's been stolen.

It went missing from our ship yard on Xeer five months ago and was last seen at Reesdice.

Your mission, should you decide to accept it, is to seek and destroy this ship.

You are cautioned that only Military Lasers will penetrate the new shields and that the Constrictor is fitted with an E.C.M.System.

Good luck, Commander.

MESSAGE ENDS


I still get goosebumps reading this; it's one of my favourite gaming moments, and in this article I'm going to relive that mission, and look at how the mission system works under the hood.

## The Constrictor mission

													 -----------------------

						The clue in the mission briefing is to travel to Reesdice. If you're at the starting system of Lave, it's a 53.2 light-year journey across the galaxy (Reesdice is the small cross to the right in this Long-range Chart):

![The Long-range Chart showing Reesdice in BBC Micro Elite](https://elite.bbcelite.com/images/missions/reesdice_long_range_chart.png) 

						Flying there takes a while, but when you dock at Reesdice and look at the Data on System screen, there's something new - the extended system description has been replaced by a mission-specific clue, all in capitals so you can't miss it. Here's what it looks like:

![The mission message at Reesdice in BBC Micro Elite](https://elite.bbcelite.com/images/missions/reesdice.png) 

						I scribbled this down, too:

A STRANGE LOOKING SHIP LEFT HERE A WHILE BACK. LOOKED BOUND FOR AREXE.


Heading to Arexe gives you a new message:

![The mission message at Arexe in BBC Micro Elite](https://elite.bbcelite.com/images/missions/arexe_1.png) 

						I scribbled this down as well, spelling mistake and all:

YEP, A WIERD NEW SHIP HAD A GALACTIC HYPERDRIVE FITTED HERE. USED IT TOO.


It turns out that some of the mission messages are randomly generated, and refreshing the Data on System screen gives you a different version. Here's another version of the message at Arexe:

![The mission message at Arexe in BBC Micro Elite](https://elite.bbcelite.com/images/missions/arexe_2.png) 

						This one's also in my notes, complete with typo:

YEP, A UNUSAL NEW SHIP HAD A GALACTIC HYPERDRIVE FITTED HERE. USED IT TOO.


There is at least one grammatically correct version of this message, though. Here it is:

![The mission message at Arexe in BBC Micro Elite](https://elite.bbcelite.com/images/missions/arexe_3.png) 

						And here it is in a more readable form:

YEP, A PECULIAR NEW SHIP HAD A GALACTIC HYPERDRIVE FITTED HERE. USED IT TOO.


So you need a galactic hyperdrive to continue with the mission, which might take a while if you're short on cash. But when you activate it, you arrive here:

![The Long-range Chart for arriving in galaxy 2 in BBC Micro Elite](https://elite.bbcelite.com/images/missions/galaxy_2_long_range_chart.png) 

						And specifically, at the system of Ororra:

![The Short-range Chart for arriving in  galaxy 2 in BBC Micro Elite](https://elite.bbcelite.com/images/missions/galaxy_2_short_range_chart.png) 

						At this point the trail appears to have gone cold - there are no mission briefings, and Ororra doesn't have a capitalised hint in its Data on System screen. But it turns out there are quite a few systems scattered around the galaxy with hints, including one at Cearso, just a short hop from our arrival point. Here it is:

![The mission message at Cearso in BBC Micro Elite](https://elite.bbcelite.com/images/missions/cearso_1.png) 

						And here it is in slightly more legible text:

I HEAR A STRANGE LOOKING SHIP APPEARED AT ERRIUS.


This message also has an alternative if you refresh the screen, and this one's a cracker:

![The mission message at Cearso in BBC Micro Elite](https://elite.bbcelite.com/images/missions/cearso_2.png) 

						Or, if that screenshot text is too small, here it is:

GET YOUR IRON ASS OVER TO ERRIUS.


Now that's a mission statement! Of course, Errius is a bit of a hike at 39.6 light years away, but that's the nature of the ship-hunting game, so off we go again:

![The Long-range Chart showing Errius in BBC Micro Elite](https://elite.bbcelite.com/images/missions/errius_long_range_chart.png) 

						The messages continue. At Errius we get another clue:

THIS UNUSUAL SHIP DEHYPED HERE FROM NOWHERE, SUN SKIMMED AND JUMPED. I HEAR IT WENT TO INBIBE.


The hint at Inbibe keeps the chase going:

SCOUNDREL SHIP WENT FOR ME AT AUSAR. MY LASERS DIDN'T EVEN SCRATCH THE SON OF A BITCH.


And there's yet another hint when we dock at Ausar:

OH DEAR ME YES. A FRIGHTFUL ROGUE WITH WHAT I BELIEVE YOU PEOPLE CALL A LEAD POSTERIOR SHOT UP LOTS OF THOSE BEASTLY PIRATES AND WENT TO USLERI.


Finally, in Usleri, we get our last hint:

![The mission message at Usleri in BBC Micro Elite](https://elite.bbcelite.com/images/missions/usleri_1.png) 

						This says:

YOU CAN TACKLE THE EVIL SCOUNDREL IF YOU LIKE. HE'S AT ORARRA.


Though you definitely want to refresh this one, as the other version is a lot more fun:

![The mission message at Usleri in BBC Micro Elite](https://elite.bbcelite.com/images/missions/usleri_2.png) 

						This says:

YOU CAN TACKLE THE VICIOUS WHORESON BEETLE HEADFLAP EAR'D KNAVE IF YOU LIKE. HE'S AT ORARRA.


[Aside: This is actually a quote from Shakespeare, specifically from Act 4 Scene 1 of The Taming of the Shrew, where Petruchio calls a servant "a whoreson beetle-headed, flap-ear'd knave!". The original BBC Micro disc version of Elite gets this quote wrong - as you can see, it says "whoreson beetle *headflap* ear'd knave" above - but this was fixed in the 6502 Second Processor and BBC Master versions, which correctly call the Constrictor thief a "whoreson beetle headed flap ear'd knave". Interestingly, the NES version ditches Shakespeare in favour of a much tamer shrew, opting instead for the rather less flowery and considerably more succint "wretch".]

So it's time to head to Orarra for the showdown, which is just a short hop from Usleri. It doesn't appear on the Short-range Chart, but a quick search in the Long-range Chart shows that it's really close:

![The Long-range Chart showing Orarra in BBC Micro Elite](https://elite.bbcelite.com/images/missions/orarra_long_range_chart.png) 

						And in fact it is within range, but the Short-range Chart is rather coy about showing its name, though it does show the crosshairs at the top of the screen:

![The Short-range Chart showing Orarra in BBC Micro Elite](https://elite.bbcelite.com/images/missions/orarra_short_range_chart.png) 

						Anyway, flying to Orarra and hanging around in deep space will eventually bring on a fight to the death with the Constrictor. Here he is, about to make the mistake of flying into my laser sights. Rookie mistake!

![The Constrictor in BBC Micro Elite](https://elite.bbcelite.com/images/missions/constrictor.png) 

						It might take a while, but assuming we win, there's a final message waiting for us back in the station:

![The debriefing screen for the Constrictor mission in BBC Micro Elite](https://elite.bbcelite.com/images/missions/mission_1c.png) 

						It says:

Congratulations Commander!

There will always be a place for you in Her Majesty's Space Navy.

And maybe sooner than you think...

MESSAGE ENDS


We also get our rewards: 5,000 credits, plus 256 kill points, which equates to one whole "Right On Commander!".

And that's the first mission in Elite; maybe you had to be there, but for some of us, this was such a thrill ride. Let's see how it all works in the code.

## The mission routines and tokens

													 -------------------------------

						The Constrictor mission appears in every version of 6502 Elite apart from the BBC Micro cassette and Acorn Electron versions, which have no missions at all.

The [DOENTRY](https://elite.bbcelite.com/disc/docked/subroutine/doentry.html) routine in the docked code contains all the mission logic, and because missions are designed to take a long time, there's a flag in the commander save file called [TP](https://elite.bbcelite.com/disc/docked/workspace/up.html#tp) that stores the current mission status. The DOENTRY routine is called every time we dock, and it checks the flags in TP and compares it with our current situation, and if we meet the criteria for a mission, it calls one of the many briefing routines to display the relevant mission details.

Bits 0 and 1 of TP contain the flags for the Constrictor mission. For this mission, DOENTRY applies the following logic:

- If bits 0-1 of TP are %00, then the Constrictor mission has not been started yet, so check the following:
								- Is TALLY+1 > 0 (i.e. have we reached a combat rank of Competent and earned a grand total of at least 256 kill points, which is another 128 kill points beyond the promotion to Competent)?
- Are we in either of the first two galaxies?
 [BRIEF](https://elite.bbcelite.com/disc/docked/subroutine/brief.html)routine to display the Constrictor briefing and set bit 0 of TP (so bits 0-1 of TP are now %01). If the answer to either or both of these is "no", then we jump straight to the docking bay and skip the rest of the mission logic, as we are not yet ready for the mission.
- If bits 0-1 of TP are %01, then the Constrictor mission is already in progress, so we stop checking further and fall through into the other mission checks. In the BBC Micro version this will take us to the docking bay as there is only one other mission ([the Thargoid Plans mission](https://elite.bbcelite.com/the_thargoid_plans_mission.html)), and we can only start that once we've killed the Constrictor. In the other 6502 versions it is possible to do[the Trumbles mission](https://elite.bbcelite.com/the_trumbles_mission.html)at the same time as the others, so in theory we could be offered the Trumbles mission straight after accepting the Constrictor mission, though it's pretty unlikely we'd be Competent without having already met the criteria for the Trumbles offer.
- If bits 0-1 of TP are %11, then we have just killed the Constrictor (the [KILLSHP](https://elite.bbcelite.com/disc/flight/subroutine/killshp.html)routine sets bit 1 of TP when this happens, so TP goes from %01 to %11). If this is the case, we jump to the[DEBRIEF](https://elite.bbcelite.com/disc/docked/subroutine/debrief.html)routine to display the congratulations message and get our reward. At this point bit 0 of TP is cleared, leaving bits 0-1 of TP set to %10 to indicate that the mission is done and dusted, and to ensure that in future we pass through the above logic and into the checks for the Thargoid Plans mission (see the deep dive on[the Thargoid Plans mission](https://elite.bbcelite.com/the_thargoid_plans_mission.html)for details).

As well as the DOENTRY logic for when we dock, the game displays the mission hints using the extended system description overrides described in the deep dive on [extended system descriptions](https://elite.bbcelite.com/extended_system_descriptions.html). Specifically, the [RUGAL](https://elite.bbcelite.com/disc/docked/variable/rugal.html) and [RUPLA](https://elite.bbcelite.com/disc/docked/variable/rupla.html) tables define a selection of capitalised tokens from the [RUTOK](https://elite.bbcelite.com/disc/docked/variable/rutok.html) table that get shown instead of the normal extended system descriptions, but only when the Constrictor mission is in progress. The tokens are as follows:

| Galaxy | System | Token | Text | 
|---|---|---|---|
| 1 | Xeer | 2 | THE CONSTRICTOR WAS LAST SEEN AT REESDICE, COMMANDER. | 
| 1 | Reesdice | 3 | A [130-134] LOOKING SHIP LEFT HERE A WHILE BACK. LOOKED BOUND FOR AREXE. | 
| 1 | Arexe | 4 | YEP, A [130-134] NEW SHIP HAD A GALACTIC HYPERDRIVE FITTED HERE. USED IT TOO. | 
| 2 | Errius | 5 | THIS [130-134] SHIP DEHYPED HERE FROM NOWHERE, SUN SKIMMED AND JUMPED. I HEAR IT WENT TO INBIBE. | 
| 2 | Inbibe | 6 | [91-95] SHIP WENT FOR ME AT AUSAR. MY LASERS DIDN'T EVEN SCRATCH THE [91-95]. | 
| 2 | Ausar | 7 | OH DEAR ME YES. A FRIGHTFUL ROGUE WITH WHAT I BELIEVE YOU PEOPLE CALL A LEAD POSTERIOR SHOT UP LOTS OF THOSE BEASTLY PIRATES AND WENT TO USLERI. | 
| 2 | Usleri | 8 | YOU CAN TACKLE THE [170-174] [91-95] IF YOU LIKE. HE'S AT ORARRA. | 
| 2 | Bebege | 10 | Random Errius message | 
| 2 | Cearso | 11 | Random Errius message | 
| 2 | Dicela | 12 | Random Errius message | 
| 2 | Eringe | 13 | Random Errius message | 
| 2 | Gexein | 14 | Random Errius message | 
| 2 | Isarin | 15 | Random Errius message | 
| 2 | Letibema | 16 | Random Errius message | 
| 2 | Maisso | 17 | Random Errius message | 
| 2 | Onen | 18 | Random Errius message | 
| 2 | Ramaza | 19 | Random Errius message | 
| 2 | Sosole | 20 | Random Errius message | 
| 2 | Tivere | 21 | Random Errius message | 
| 2 | Veriar | 22 | Random Errius message | 
| 2 | Orarra | 24 | THERE'S A REAL [91-95] PIRATE OUT THERE. | 
| 3 | Xeveon | 23 | BOY ARE YOU IN THE WRONG GALAXY! | 

The various Errius messages that are picked by random are in tokens 106 to 110 of the extended token table at [TKN1](https://elite.bbcelite.com/disc/docked/variable/tkn1.html), and are as follows:

| Token | Text | 
|---|---|
| 106 | I HEAR A [130-134] LOOKING SHIP APPEARED AT ERRIUS. | 
| 107 | YEAH, I HEAR A [130-134] SHIP LEFT ERRIUS A WHILE BACK. | 
| 108 | GET YOUR IRON ASS OVER TO ERRIUS. | 
| 109 | SOME [91-95] NEW SHIP WAS SEEN AT ERRIUS. | 
| 110 | TRY ERRIUS | 

Finally, the random tokens in the above translate into the following options, with one of the options being randomly chosen each time the text is displayed:

| Token range | Text | 
|---|---|
| [91-95] | SON OF A BITCH SCOUNDREL BLACKGUARD ROGUE WHORESON BEETLE HEAD FLAP EAR'D KNAVE | 
| [130-134] | FUNNY WIERD UNUSUAL STRANGE PECULIAR | 
| [170-174] | KILLER DEADLY EVIL LETHAL VICIOUS | 

Here are some other points of interest:

- The last invective in token 95 is "WHORESON BEETLE HEAD FLAP EAR'D KNAVE" in the disc version, but by the time of the 6502 Second Processor version, it had been changed to "WHORESON BEETLE HEADED FLAP EAR'D KNAVE", which presumably scans better. It's good to see the authors refining the quality of their insults over time (though, sadly, the NES version changes it to "WRETCH", which is just not the same).
- The names of the Navy captains in the above messages are different depending on which galaxy you are in when the mission is offered (which is a nice touch). If we receive the briefing in galaxy 1 then it's from Captain Carruthers, but if we are in galaxy 2 then it's from Captain Fosdyke Smythe. The names are implemented in the [MT27](https://elite.bbcelite.com/disc/docked/subroutine/mt27.html)routine, which is called when printing an EJMP 27 token from the extended token table.
- In the NES version, the captains' names vary between different languages. In English they're Captain Carruthers and Captain Fosdyke Smythe, in German they're Käpitan Richtofen and Käpitan Vanderbilt, and in French they're le capitain de Remigny and le capitain de Sevigny.
- The mission hint in the mission briefing is also different depending on the galaxy you are in when the mission is offered. If we are in galaxy 1 then the hint is "was last seen at Reesdice", but if we're in galaxy 2, the hint is "is believed to have jumped to this galaxy". The hints are implemented in the [MT28](https://elite.bbcelite.com/disc/docked/subroutine/mt28.html)routine, which is called when printing an EJMP 28 token from the extended token table.
- The incoming message text is token 216 in [TKN1](https://elite.bbcelite.com/disc/docked/variable/tkn1.html), the mission briefing with the rotating ship is token 10, and the mission debriefing is token 15.
- In the BBC Micro disc version, the mission status affects which ship data files are loaded. Specifically, the [LOMOD](https://elite.bbcelite.com/disc/flight/subroutine/lomod.html)routine ensures that the ship blueprints file D.MOG is loaded for the Constrictor fight, as that's the only data file that contains the Constrictor blueprint. See the deep dive on[ship blueprints in the disc version](https://elite.bbcelite.com/ship_blueprints_in_the_disc_version.html)for details.

And that's it - mission accomplished! See the deep dives on [the Thargoid Plans mission](https://elite.bbcelite.com/the_thargoid_plans_mission.html) and [the Trumbles mission](https://elite.bbcelite.com/the_trumbles_mission.html) for more mission-related reading.

MESSAGE ENDS

---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/the_constrictor_mission.html](https://elite.bbcelite.com/deep_dives/the_constrictor_mission.html)*

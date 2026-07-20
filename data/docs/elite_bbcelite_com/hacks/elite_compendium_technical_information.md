---
title: Technical information for the Elite Compendium
source_url: https://elite.bbcelite.com/hacks/elite_compendium_technical_information.html
category: source-code
topics:
- basic
- assembly
- sprite programming
- input handling
difficulty: beginner
language: mixed
hardware:
- CIA
- SID
- CPU
- VIC-II
- KERNAL
- BASIC ROM
related:
- sid-registers
- sound-programming
- vic-ii-registers
- joystick-reading
- keyboard-handling
- kernal-routines
- memory-map
- music-player
- sprite-programming
- raster-interrupts
- cia-registers
scraped_at: '2026-07-20'
---

# Technical information for the Elite Compendium

## Details of all the hacks and enhancements in the Elite Compendium

The Elite Compendium combines a number of my Elite hacks into the ultimate Acornsoft Elite experience. This page describes the hacks that are unique to the Compendium, such as red enemy lasers in the BBC Master version:

![Red enemy lasers on the BBC Master in the Elite Compendium](https://elite.bbcelite.com/images/elite_compendium/red_lasers.png) 

						The BBC versions of the Compendium have their own repositories. The BBC Master version is built by the [elite-compendium-bbc-master repository](https://github.com/markmoxon/elite-compendium-bbc-master) and the BBC Micro version is built by the [elite-compendium-bbc-micro repository](https://github.com/markmoxon/elite-compendium-bbc-micro). These parent repositories include the relevant branches of the different versions of Elite as submodules, and they bundle these up with the menu program to form the final Compendium discs.

If you want to see exactly how the code for a Compendium version of Elite differs from the code in the original Acornsoft version, you can check out the various compendium-related branches in the accompanying repositories. Here's a complete list of all Compendium version branches:

- See the [elite-compendium branch](https://github.com/markmoxon/elite-source-code-bbc-master/tree/elite-compendium/1-source-files/main-sources)for modifications related to BBC Master Compendium Elite.
- See the [elite-compendium branch](https://github.com/markmoxon/elite-source-code-6502-second-processor/tree/elite-compendium/1-source-files/main-sources)for modifications related to 6502 Second Processor Compendium Elite.
- See the [elite-compendium branch](https://github.com/markmoxon/elite-source-code-acorn-electron/tree/elite-compendium/1-source-files/main-sources)for modifications related to Acorn Electron Compendium Elite.
- See the [elite-compendium-music branch](https://github.com/markmoxon/elite-source-code-acorn-electron/tree/elite-compendium-music/1-source-files/main-sources)for modifications related to musical Acorn Electron Compendium Elite.
- See the [bbc-micro-b-plus branch](https://github.com/markmoxon/elite-source-code-bbc-master/tree/bbc-micro-b-plus/1-source-files/main-sources)for modifications related to BBC Master Compendium Elite on the BBC Micro B+.
- See the [bbc-micro-b-plus-music branch](https://github.com/markmoxon/elite-source-code-bbc-master/tree/bbc-micro-b-plus-music/1-source-files/main-sources)for modifications related to musical BBC Master Compendium Elite on the BBC Micro B+.
- See the [elite-compendium-bbc-micro branch](https://github.com/markmoxon/elite-source-code-bbc-micro-disc/tree/elite-compendium-bbc-micro/1-source-files/main-sources)for modifications related to BBC Micro Compendium Elite.
- See the [elite-compendium-bbc-master branch](https://github.com/markmoxon/elite-source-code-bbc-micro-disc/tree/elite-compendium-bbc-master/1-source-files/main-sources)for modifications related to BBC Micro Compendium Elite on the BBC Master.
- See the [elite-compendium branch](https://github.com/markmoxon/elite-source-code-bbc-micro-cassette/tree/elite-compendium/1-source-files/main-sources)for modifications related to BBC Micro cassette Compendium Elite.

You can search the source code files in these branches for "Mod:" to see every single modification that I've made to the original code to produce the Compendium version.

You can find links below to all the other hacks that are included in the Compendium, but first let's look at all the Compendium exclusives.

## The Trumbles mission

													 --------------------

						The Commodore 64 version of Elite introduced the world to the Trumbles, a cuddly collection of furry friends that you can accept as a gift from the not-at-all-shady Merchant Prince of Thrun:

![The Trumbles mission on the BBC Master in the Elite Compendium](https://elite.bbcelite.com/images/elite_compendium/bbc_trumbles1.png) 

						If you accept, then you start off with just one Trumble in the hold:

![The Trumbles mission on the BBC Master in the Elite Compendium](https://elite.bbcelite.com/images/elite_compendium/bbc_trumbles2.png) 

						Soon enough it breeds, and then breeds some more, until it all gets totally out of control and a mass of Trumbles takes up all of your cargo space, eating all your food and narcotics before crawling out of the airlock and (in the Commodore 64 version), smothering your Cobra's canopy and blocking your view.

![The Trumbles mission on the BBC Master in the Elite Compendium](https://elite.bbcelite.com/images/elite_compendium/bbc_trumbles3.png) 

						This lighthearted mission was added to take advantage of the Commodore 64's hardware sprites, which made it easy to overlay fluffy aliens over the top of the space view. However the mission was dropped when the 6502 Second Processor and Commodore 64 versions were merged to create the BBC Master version, as the latter doesn't support sprites (though quite a lot of Trumble code remains in the Master version, albeit dormant).

Luckily for those of us trying to stick to the Elite canon, the NES version of Elite also contains the Trumbles mission, but without the sprites (the NES does have sprites, but they are all to make the game work on a console - see the deep dive on [sprite usage in NES Elite](https://elite.bbcelite.com/deep_dives/sprite_usage_in_nes_elite.html) for details). The Trumbles mission in the Compendium is therefore a relatively simple port of the NES version's Trumble-related code, some of which is already in the Master binaries (such as the breeding code in [SOLAR](https://elite.bbcelite.com/master/main/subroutine/solar.html)), while other code is in the Master source but is commented out (such as the mission checks in [DOENTRY](https://elite.bbcelite.com/master/main/subroutine/doentry.html#en4) and the briefing routine in [TBRIEF](https://elite.bbcelite.com/master/main/subroutine/tbrief.html)). Finally, other parts of the code are left blank in the Master, like text tokens 198 and 199 in [TKN1](https://elite.bbcelite.com/nes/bank_2/variable/tkn1.html), which are simply empty strings in the Master version but contain the mission briefing in the NES version.

Note that I stuck to calling them Trumbles in-game, just like the Commodore 64 version, rather than using the NES's rather more trademark-savvy Squeakys. The trigger point, however, is the 6553.6 credit score of the NES, so the Compendium version is a genuinely hybrid mission.

For more information, see the deep dive on [the Trumbles mission](https://elite.bbcelite.com/deep_dives/the_trumbles_mission.html).

## Docking and fuel scoop improvements

													 -----------------------------------

						The NES version makes docking a lot easier than in previous versions. The most obvious difference is that you start the game with a docking computer already installed, but there are other more subtle changes in the NES version, too. I thought long and hard about whether to backport these features into the Compendium, but I think they're worthy improvements to quality of life (though I haven't backported the ability to engage the station's docking computer if you don't have one yourself - that feels like a step too far!).

Here's the NES code that I backported to the Compendium:

- The station no longer spawns traders, like Transporters or Shuttles, while the docking computer is activated - see [part 2 of TACTICS](https://elite.bbcelite.com/nes/bank_0/subroutine/tactics_part_2_of_7.html).
- Once you're inside the station's safe zone and you've activated your docking computer, you can press "J" to dock instantly - see [WARP](https://elite.bbcelite.com/nes/bank_0/subroutine/warp.html#warp1).
- Fuel scoops will only work when you are moving - see [part 15 of the main flight loop](https://elite.bbcelite.com/nes/bank_0/subroutine/main_flight_loop_part_15_of_16.html#nokilltr).

I grew up on the BBC Micro cassette version of Elite, which didn't have enough memory for a fancy AI-powered autopilot, so for me having an optional insta-dock is a bit like coming home.

In the first version of the Compendium, I backported another docking-related feature, but I have now removed it. In the NES version the docking computer can no longer kill you - see [part 9 of the main flight loop](https://elite.bbcelite.com/nes/bank_0/subroutine/main_flight_loop_part_9_of_16.html#ma62) for the code. However, it turns out that some players enjoy the hint of danger that comes with possible death by docking, so I've removed this feature and the docking computer can once again prove fatal. If this proves too much for your nerves, you can always hit "J" to dock instantly and safely, so the Compendium is the best of both worlds.
						

## Red enemy lasers

													 ----------------

						The BBC Master is known for its flicker-free ships when compared to earlier versions of Elite. The improved algorithm gives much smoother ship-drawing, and it's such a simple fix that it was the first Elite hack that I backported, and is still one of the best (see the [flicker-free hack](https://elite.bbcelite.com/flicker-free_elite_technical_information.html) for more information).

It is not perfect, however. The 6502 Second Processor version of Elite came out a year before the BBC Master version, and although it flickers, it does have one thing that the BBC Master doesn't: red enemy lasers. They look great, so much so that the cyan lasers of the BBC Master version look positively dull. Here's a fight with the BBC Master's standard cyan lasers:

![Cyan enemy lasers in the BBC Master Elite](https://elite.bbcelite.com/images/elite_compendium/cyan_lasers.png) 

						and here's the same fight with the 6502 Second Processor version's red lasers:

![Red enemy lasers on the BBC Master in the Elite Compendium](https://elite.bbcelite.com/images/elite_compendium/red_lasers.png) 

						Red lasers are so much better!

The reason for this backwards step is that the Master's improved algorithm treats the enemy's laser line as just another line in the heap. The improved algorithm draws and removes lines one at a time in way that means we simply don't know which line in the heap is the laser line, so it isn't possible to know when to erase and redraw the line in red rather than cyan. As a result the laser line has to be drawn in cyan, albeit without a flicker.

The solution is to extract the laser line from within the line heap and always store it as the first line in the heap. If there is no laser being fired then this slot is blank, but if there is a line in there then we know to draw and erase it in red. Because the ship heaps are sized to cater for a laser line as well as the maximum number of visible edges in the ship blueprint, we don't need to resize the heap, we just need to ensure that new ships are spawned with a blank laser line at the start of the heap. We can denote a blank laser line by having a y-coordinate of 255 in the start point, as this will never happen with a valid laser line (as the maximum y-coordinate in the space view is 191).

## Enabling the keyboard fire key for joysticks

													 --------------------------------------------

						If you've tried playing BBC Micro Elite with a joystick whose fire button is on the body of the stick housing rather than being a trigger on the stick itself - such as a Delta 14B or a Bitstik - then because the "A" key on the keyboard doesn't fire lasers in joystick mode, you have to keep switching your non-steering hand between the keyboard and the fire button on the joystick. It's a bit of a pain.

The BBC Master version of Elite fixes this by leaving the "A" key enabled when in joystick mode. This means you can have one hand steering with the stick and the other on the keyboard, and you can leave them there. For the Compendium I've backported this implementation to all the other versions, so the "A" key keeps working in joystick and Bitstik mode in the BBC Micro, 6502 Second Processor and Teletext versions too.

## Delta 14B support

													 -----------------

						The code to support the Delta 14B joystick and keypad comes straight from Elite-A, Angus Duggan's epic extended version of Elite. For details of how this code works, check out the deep dive on [Delta 14B joystick support](https://elite.bbcelite.com/deep_dives/elite-a_delta_14b_joystick_support.html).

I had to changes for the BBC Master, as the key logger is in a different order to the original BBC Micro version. For the 6502 Second Processor, the Delta 14B code slotted nicely into the KEYBOARD routine in the I/O processor, but I had to extend the API call to transmit the Delta 14B configuration setting from the parasite, so the I/O processor would know whether or not to scan the Delta 14B buttons.

## Slowing down the co-pro version

													 -------------------------------

						Elite on the BBC Micro's 3MHz 6502 Second Processor is brutally fast - so fast that it's arguably not much fun. Run the same game on the BBC Master's 4MHz internal 65C102 co-processor, and even an iron ass won't save you. It's way too fast.

The version of 6502 Second Processor Elite in the Elite Compendium therefore contains code to make the main flight loop wait until a minimum number of vertical syncs have passed before moving on to the next iteration. This ensures that the game never runs too fast, but it also doesn't speedbump the processor when a lot is happening, so you rarely get slowdown in normal play, and if things do hot up and the engine does start to struggle, at least you know it would be doing the same in the original version.

It's a lot more enjoyable this way, I think.

## Fixing the delete file bug

													 --------------------------

						The BBC Master version of Elite has a nasty file-related bug in the [DELT](https://elite.bbcelite.com/master/main/subroutine/delt.html) routine (a bug which was fixed for the BBC Master Compact). If you delete a file using the disc access menu, then the code for the save option gets corrupted - specifically, when updating the delete command string in [DELI](https://elite.bbcelite.com/master/main/variable/deli.html) with the name of the file to delete, the code accidentally spills over into the save command string in [savosc](https://elite.bbcelite.com/master/main/variable/savosc.html), overwriting the first character (the "S" of the "SAVE" command). So if you then try to save your commander, you get a "Bad command" error and the file isn't saved.

It's a one-instruction fix, but makes a big difference.

## Fixing the extended system description (NRU%) bug

													 -------------------------------------------------

						At the start of the main source file in both the [6502 Second Processor](https://elite.bbcelite.com/6502sp/all/workspaces.html) and [BBC Master](https://elite.bbcelite.com/master/all/workspaces.html) versions, the configuration variable NRU% is set to 0, unlike the BBC Micro disc and NES versions, which correctly set NRU% to match the number of entries in the RUGAL table. This is a bug, and it breaks the extended system description routine in [PDESC](https://elite.bbcelite.com/master/main/subroutine/pdesc.html).

The effect is to make PDESC search in the wrong place for system description override data; specifically, instead of searching the [RUGAL](https://elite.bbcelite.com/master/game_data/variable/rugal.html) table for system/mission criteria, it first searches RUGAL-1 and then searches RUGAL+254 to RUGAL+0. RUGAL is only 25 bytes long in the 6502 Second Processor version and 26 bytes long in the Master version, and it is followed by the [RUTOK](https://elite.bbcelite.com/master/game_data/variable/rutok.html) text token table, so this means PDESC ends up searching RUTOK for override criteria instead of RUGAL, and if it finds a match, it then tries to print text tokens from the unrelated memory after the end of RUTOK. This doesn't end well.

For example, if we are at system 3 in galaxy 0 (Biarge) during mission 1, then PDESC matches the &83 at location RUGAL-1+224, so it then tries to print token 224 from RUTOK. This crashes the game as RUTOK only contains 27 tokens, so the print routine ends up in a sea of nulls after the end of the game code, where it infinitely loops looking for the non-existent token 224.

The fix is easy - just change NRU% back to the number of entries in the RUGAL table and the bug goes away.

## Fixing the Moray spawning bug

													 -----------------------------

						If you look at the spawning routines, it turns out the Moray, in ship blueprint 28, is never spawned. Traders can fly the [Cobra Mk III, Python, Boa or Anaconda](https://elite.bbcelite.com/master/main/subroutine/main_game_loop_part_1_of_6.html); lone bounty hunters can be found in the [Cobra Mk III, Asp Mk II, Python and Fer-de-lance](https://elite.bbcelite.com/master/main/subroutine/main_game_loop_part_4_of_6.html#label_2); pirates favour [Sidewinders, Mambas, Kraits, Adders, Geckos, Cobras Mk I and III, and Worms](https://elite.bbcelite.com/master/main/subroutine/main_game_loop_part_4_of_6.html#mt1); and the cops stick to the [trusty Viper](https://elite.bbcelite.com/master/main/subroutine/main_game_loop_part_3_of_6.html). Stations regularly spawn [Transporters and Shuttles](https://elite.bbcelite.com/master/main/subroutine/tactics_part_2_of_7.html), and [Thargoids and Thargons](https://elite.bbcelite.com/master/main/subroutine/main_game_loop_part_4_of_6.html#fothg2) appear every now and then, and while the [Constrictor](https://elite.bbcelite.com/master/main/subroutine/main_game_loop_part_4_of_6.html#yescon) and [Cougar](https://elite.bbcelite.com/master/main/subroutine/main_game_loop_part_4_of_6.html#fothg) are the rarest ships, they do actually appear in-game.

The Moray, however, never gets invited to the ball; the spawning routines simply never choose blueprint 28. This is not only a huge waste of an entire ship blueprint, but it's especially sad as the Moray has a multi-coloured ship wireframe, just like the Thargoids. It is quite a special ship, and it even appears in *The Dark Wheel*, the novella that comes with the game:

To the right, running a parallel course towards the Faraway tunnel, was an odd-shaped ship, with powerful lights flickering on and off. It was catching the sun and Alex could see how it was slowly spinning about its central axis. Fish-like fins opened and closed. Across its sleek hull a rapid pattern of coloured lights rippled.

A Moray. A subaqua vessel, designed for both space and undersea voyaging. The Moray was a rare ship indeed to see in space, especially about to undertake a hyperspace transit. On worlds like Regiti and Aona, where the only land was the tips of volcanoes, rising above the oceans, the Moray was both freighter and public transport, a vital ship-link between the undersea cities that were developing in such hostile environments.

The Moray's frantic colour signalling ceased. Alex noticed that his father was watching the animalistic display (the coding had been developed from the signalling of a terrestrial aquatic creature, the squid) with a frown on his face. 'Something up?' Jason shrugged. 'Not sure. Probably not.'


In all it's a bit of a tragedy that the Moray never gets spawned, so the Compendium fixes this bug by tweaking the list of bounty hunter ships to include the Moray. It appears rarely, which is befitting such an exotic ship, but at least it is no longer excluded.

## Making space for all these hacks in the BBC Micro

													 -------------------------------------------------

						Music aside, all of the hacks included in the Compendium fit nicely into main memory in the BBC Master and 6502 Second Processor versions of Elite; the music lives in sideways RAM, as it's pretty big. This is also true of Teletext Elite, as teletext screen mode 7 only takes up 1K of screen RAM compared to 7.75K of RAM for the original game's screen mode, and this is enough extra space to cater for all the extra hacks.

But what about the original BBC Micro version, where space is legendarily tight? Well, for the Compendium we are already loading a ROM image into sideways RAM for the music, and it turns out there's a bit of free space at the end of the ROM, as the music only takes around 12K of the 16K ROM image. So for the BBC Micro versions of Compendium Elite, we can move code from the main game into sideways RAM, freeing up space for the hacks.

The process is relatively straightforward. First we pick a routine to move - preferably a routine that isn't used during combat, as there is a speed penalty when switching to sideways RAM - and we then update the BeebAsm source to build that routine in the sideways RAM address space. We save this out as a separate binary file that we can tack onto the music ROM image file, and we replace the original routine in the main game code with a small bit of code that switches to the sideways ROM image, calls the moved routine, and switches back once it returns.

These are the routines that have been moved to squeeze in the Compendium hacks:

- BBC Micro cassette
								- rom-extra1.bin = TT22 (Long-range Chart), TT15 (Draw crosshairs)
- rom-extra2.bin = TT210 (Inventory)
- rom-extra3.bin = TT23 (Short-range Chart)
- rom-extra4.bin = TT111 (Set current system to nearest)
- rom-extra5.bin = EQSHP (Equip ship)
- rom-extra6.bin = cpl (Print the selected system name)
- rom-extra7.bin = OOPS (Take some damage)
- rom-extra8.bin = TIDY (Orthonormalise orientation vectors)
 
- BBC Micro disc version on the BBC Micro
								- rom-extra1.bin = TT22 (Long-range Chart), TT15 (Draw crosshairs)
- rom-extra2.bin = TT210 (Inventory)
- rom-extra3.bin = TT23 (Short-range Chart)
- rom-extra4.bin = TT111 (Set current system to nearest)
- rom-extra5.bin = cpl (Print the selected system name)
- rom-extra6.bin = OOPS (Take some damage)
- rom-extra7.bin = TIDY (Orthonormalise orientation vectors)
 
- BBC Micro disc version on the BBC Master
								- rom-extra1.bin = TT22 (Long-range Chart), TT15 (Draw crosshairs)
- rom-extra2.bin = TT210 (Inventory)
- rom-extra3.bin = TT23 (Short-range Chart)
- rom-extra4.bin = TT111 (Set current system to nearest)
 

Each routine is saved out as rom-extra1.bin, rom-extra2.bin and so on, and a simple cat command in the Makefile appends all the ROM extras onto the end of the music ROM. In this way we can extend the available memory for Elite without needing any further hardware beyond the 16K of sideways RAM that the music already requires.

## Information on the other hacks in the Compendium

													 ------------------------------------------------

						The Compendium also includes a number of hacks that are available for a larger range of computers (including the Acorn Electron and Commodore 64). You can read more about them in their own sections of the site. Here are the details:

- Compendium version of Elite on the Acorn Electron:
- Flicker-free Elite:
- Acornsoft Elite... with music:
- BBC Micro disc Elite on the BBC Master:
- BBC Master Elite on the BBC Micro B+:
- Teletext Elite:
- Elite Universe Editor:

---
*Fonte originale: [https://elite.bbcelite.com/hacks/elite_compendium_technical_information.html](https://elite.bbcelite.com/hacks/elite_compendium_technical_information.html)*

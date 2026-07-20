---
title: Comparing NES Elite with the other versions
source_url: https://elite.bbcelite.com/deep_dives/comparing_nes_elite_with_the_other_versions.html
category: manual
topics:
- basic
- assembly
- sprite programming
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

# Comparing NES Elite with the other versions

## The features that make NES Elite so unique

Technically speaking, the NES version of Elite is a conversion of the original BBC Micro game, and an examination of the game code bears this out. Most of ROM banks 0, 1 and 2 contain the original Acornsoft code, albeit tweaked in a number of places, with the original code making up around 30% of the NES codebase (the majority of the other 70% is made up of graphics data, music data and multi-language text). This core 30% can directly trace its roots back to the original 1984 release, via the 1986 BBC Master version from which the NES version was derived; the beating heart of the 1991 game is quite literally the original 1984 classic, just dressed up in some very fancy new clothes.

Those clothes do make quite a difference, though. Let's take a look at the big changes that everyone knows about, and some of the smaller ones that you might only spot by poking through the code.

## Graphical improvements in NES Elite

													 -----------------------------------

						The most obvious update for NES Elite is the improvement in the graphics. I'm not talking about the space view here, which is monochrome in the NES version, and is therefore a bit of a step backwards from the four-colour space view of the BBC Master version (though the NES version's graphics are 100% rock-steady and flicker-free, which can't be said of any of the other 6502-based versions).

The main graphical improvements are as follows:

- There are lots of colourful images on the various information screens, which are displayed using a combination of background tiles and hardware sprites to create images with bigger palettes than would be otherwise possible (see the deep dive on [displaying two-layer images](https://elite.bbcelite.com/displaying_two-layer_images.html)for details on how these wonderful pieces of pixel art are created). Here's the Data on System screen, where we discover that although Riedquat is a lawless hell-hole, it sure is pretty:![The Riedquat data screen in NES Elite](/images/nes/general/data_on_riedquat.png)  
- The Status Mode screen contains a picture of us, the player, with our appearance changing as we work our way up through the rankings, make pots of money and flirt with the law (the latter earning us some extremely cool dark glasses). Here's what we look like as a law-abiding, super-rich Elite pilot, complete with fancy earrings and a shiny medallion:
								![The maximum commander in NES Elite](/images/nes/commander/max_commander.png)  
- The Equip Ship screen shows our Cobra Mk III, with all the equipment we have fitted shown in their correct slots. Here's the full loadout in all its glory:
								![The Cobra Mk III with a full loadout on the NES Elite Equip Ship screen](/images/nes/commander/max_equipment.png)  
- The dashboard has a much more three-dimensional look to it, compared to the rather flat dashboards of the earlier versions:
								![The space view showing a space station in NES Elite](/images/nes/general/station.png)  
- Stardust particles are implemented using sprites, so they are much rounder than the simple dots and dashes of the earlier versions. And because they are sprites they can be in different colours, so although the wireframe aspects of NES Elite are cyan on black, stardust can appear in pale yellow and dark cyan too (see the deep dive on [sprite usage in NES Elite](https://elite.bbcelite.com/sprite_usage_in_nes_elite.html)for details on the stardust and all the other sprite-based graphics):![Stardust particles in NES Elite](/images/nes/general/stardust_left.png)  

Overall, the improved graphics are the NES version's killer feature, even if the actual space view still feels a little bit stuck in the 1980s.

## The interface

													 -------------

						Looking beyond the graphics, the most obvious difference in NES Elite is the user interface, and in particular the addition of the icon bar. The NES doesn't have a keyboard, but instead comes with two eight-button controllers, so the authors had to come up with a way of supporting the huge number of controls and options in Elite, while using only a tiny number of buttons.

The icon bar is the result, and here it is, populated with all the available weapon options in our pimped-up Cobra Mk III:

![The maximum commander in space in NES Elite](https://elite.bbcelite.com/images/nes/commander/max_commander_in_space.png) 

						The buy and sell screens have also been tweaked to work with the controllers, with the addition of a highlight bar that lets you select what you want to buy:

![The Lave market prices screen in NES Elite](https://elite.bbcelite.com/images/nes/general/market_lave.png) 

						This is a big improvement on the original versions, in which you have to step forwards through each available item one at a time, and the only way to go back through the list is to start again.

There's also a new Save and Load screen that allows you to save your commander into one of eight slots that are kept intact by the battery in the cartridge.

![The Save and Load screen in NES Elite](https://elite.bbcelite.com/images/nes/general/save_and_load.png) 

						This is one area where things get a bit tricky, as the interface is perhaps not as intuitive as it could be, and entering a commander name using a NES controller is an utterly painful process. Though it's still an improvement on having to use cassette tapes to store your precious commander files, so at least there's that...

## Other big changes

													 -----------------

						The Commodore 64 version of Elite broke new ground by introducing music into the game, and the NES takes the baton and runs with it. Not only can we enjoy the "Elite Theme" on the title screen and "The Blue Danube" when activating the docking computer, but there are two additional tunes that play during the combat demo, "Assassin's Touch" (during the scroll text) and "Game Theme" (during the combat demo). Written by David Whittaker, who also coded the sound routines, they're just as catchy as the original music.

The NES version also supports multiple languages, so not only do we have the standard English version, but we can also choose German or French from the Start screen. Here's Commander Jameson in German, where he is, of course, known as Kommandant Jameson:
						![The maximum commander in German in NES Elite](https://elite.bbcelite.com/images/nes/languages/max_commander_german.png) 

						

And here is Commandant Jameson in French:

![The maximum commander in French in NES Elite](https://elite.bbcelite.com/images/nes/languages/max_commander_french.png) 

						You can see in these screenshots how the layout of the screen changes depending on the language, as the word length is quite different and things need to be shuffled around to fit. Unfortunately, this also breaks some of the styling, as can be seen towards the left end of the cash levels; see the deep dive on [multi-language support in NES Elite](https://elite.bbcelite.com/multi-language_support_in_nes_elite.html) to read more about what's going wrong here.

Other notable features of NES Elite include the following:

- The game has a unique font design amongst the 6502 versions, which also includes accented characters for various languages.
- There's an introductory combat practice demo for new pilots that takes the [scroll text of 6502 Second Processor Elite](https://elite.bbcelite.com/6502sp_demo_mode.html)and adds a fully playable combat demo, where you have to kill three ships in as short a time as possible before you can start the game (though you can just skip it if you're feeling confident).
- The Start screen doesn't just show the iconic rotating Cobra Mk III, but it cycles through an entire list of ships, from the Cobra Mk III to the Krait, Adder, Asp Mk II, Thargoid, Gecko, Mamba, Fer-de-lance, Transporter, Missile, Sidewinder and Viper.
- If you leave the game idling at the Start screen, it will eventually start auto-playing the combat demo. See the deep dive on [the NES combat demo](https://elite.bbcelite.com/the_nes_combat_demo.html)for details.
- The Trumbles mission from the Commodore 64 version is included, though without the cute sprites. See the deep dive on [the Trumbles mission](https://elite.bbcelite.com/the_trumbles_mission.html)for the low-down.
- You can use a docking computer without actually owning one, so new players don't have to learn how to dock manually. There's a docking fee of five credits to pay if you use the station's auto-docking feature (and you have to dock manually if you can't afford it). Commanders with their own docking computers do not get charged a fee.
- The fast-forward button on the icon bar not only lets you speed up the scroll text and skip the combat demo, but it also enables in-system jumping (when allowed) and insta-docks if the docking computer is enabled.
- Enemy tactics have been slightly improved compared to the other versions.
- Narcotics, slaves and liquor/wines are no more - they have been renamed to rare species, robot slaves and beverages. They retain the same legal status, though, so trading in rare species and robot slaves will get you noticed by the police, and while Trumbles in the Commodore 64 version of Elite will start eating any narcotics or food in your hold, they only eat food in the NES version (see [SOLAR](https://elite.bbcelite.com/nes/bank_0/subroutine/solar.html)for the munching code).
- NES Elite has a whopping 29 different sound effects, way more than the handful in the BBC Micro versions (see the deep dive on [sound effects in NES Elite](https://elite.bbcelite.com/sound_effects_in_nes_elite.html)for a list).
- The NES version supports a maximum of eight ships and 20 stardust particles, while the Acornsoft versions typically support 12 ships and 18 particles.

That's quite a few new features, but there are no new ship types or equipment and no new missions, so the core gameplay is pretty much unchanged.

## Smaller changes

													 ---------------

						On top of the flagship changes above, there are loads of small tweaks in the codebase for NES Elite. Most of these are to do with the changed interface and completely different graphics, sound and controller systems on the NES, but there are some interesting gameplay tweaks as well. The following is not an exhaustive list, they're just some of the more intriguing changes that I spotted while trawling through the code.

- In NES Elite, the docking computer can no longer kill you (see [part 9 of the main flight loop](https://elite.bbcelite.com/nes/bank_0/subroutine/main_flight_loop_part_9_of_16.html#ma62)).
- You can no longer scoop fuel if you're not moving (see [part 15 of the main flight loop](https://elite.bbcelite.com/nes/bank_0/subroutine/main_flight_loop_part_15_of_16.html#nokilltr)).
- The station no longer launches transporters out of the slot if the docking computer is activated, so you can't get killed that way any more (see [part 2 of TACTICS](https://elite.bbcelite.com/nes/bank_0/subroutine/tactics_part_2_of_7.html)).
- You can force a mis-jump into witchspace by holding either the up or down key when the hyperspace counter runs down, which is rather easier than the CTRL-based dance you have to do in the BBC versions (see [TT18](https://elite.bbcelite.com/nes/bank_0/subroutine/tt18.html#hypr2)).
- There's a cheat mode that's triggered if you save your commander as "Cheater" (English), "Betrug" (German) or "Tricher" (French). This gives you 10,000 credits and can only be done once, and afterwards you can't change your commander's name; once a cheater, always a cheater (see [cheatCmdrName](https://elite.bbcelite.com/nes/bank_6/variable/cheatcmdrname.html)for the cheat names and[ChangeCmdrName](https://elite.bbcelite.com/nes/bank_6/subroutine/changecmdrname.html#cnme4)for the code).
- You can also view a scroll text showing the game's credits. On the title screen with the rotating ships, hold down and then release A, B, Select, and Start on controller 1, and a scroll text will appear showing who contributed to the game (see [creditsText1](https://elite.bbcelite.com/nes/bank_6/variable/creditstext1.html),[creditsText2](https://elite.bbcelite.com/nes/bank_6/variable/creditstext2.html)and[creditsText3](https://elite.bbcelite.com/nes/bank_6/variable/creditstext3.html)for the text and[ShowScrollText](https://elite.bbcelite.com/nes/bank_6/subroutine/showscrolltext.html#scro14)for the code).
- There's a button combination to clear all eight save slots. To do this, hold up, left, B and Select on controller 1 and reset the console (see [ChooseLanguage](https://elite.bbcelite.com/nes/bank_6/subroutine/chooselanguage.html#clan2)and[ResetSaveSlots](https://elite.bbcelite.com/nes/bank_6/subroutine/resetsaveslots.html)).
- Thargoids don't always spawn with accompanying Thargons, unlike in the original versions, and if they are spawned alone, they are slightly less aggressive (see [part 4 of the main game loop](https://elite.bbcelite.com/nes/bank_0/subroutine/main_game_loop_part_4_of_6.html#fothg2)).
- Lasers heat up more slowly in NES Elite, going up by 6 in each main loop iteration rather than 8 (see [LASLI](https://elite.bbcelite.com/nes/bank_0/subroutine/lasli.html)).
- The limit on individual stocks of gold, platinum, gem-stones and alien items in the hold is increased by one (see [tnpr](https://elite.bbcelite.com/nes/bank_0/subroutine/tnpr.html)).
- Spawned ships have different speeds and rock hermits are spawned as Cobras rather than asteroids (see [part 1 of the main game loop](https://elite.bbcelite.com/nes/bank_0/subroutine/main_game_loop_part_1_of_6.html)).
- We become a baddie quicker in the NES version, graduating from offender to fugitive at FIST level 40 rather than 50 (see [PrintLegalStatus](https://elite.bbcelite.com/nes/bank_0/subroutine/printlegalstatus.html)).

Finally, here are some technical differences of note:

- There are minor differences in the standard text tokens (CONT 7 no longer makes a beep and the position of the tab stop in CONT 9 is now language-specific) and in the extended text tokens (EJMP 9, 23 and 29 are subtly different text positions, while EJMP 26 no longer waits for text from the keyboard, but instead prints a space and switch to single cap).
- INWK+33 and INWK+34 are no longer used to store the ship line heap address, as the NES doesn't have a ship line heap (ships don't need to be erased line-by-line any more). Instead INWK+33 contains the number of the ship on the scanner, and INWK+34 contains the cloud counter for the explosion cloud.
- Each ship data block at K% has four extra bytes in the NES version. Bytes #37 to #40 of the ship data block are used to store the random seeds for the ship's explosion cloud, though they aren't copied to INWK, which stays the same size.

There are lots of other minor differences, but that's probably enough to be getting on with for now...

---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/comparing_nes_elite_with_the_other_versions.html](https://elite.bbcelite.com/deep_dives/comparing_nes_elite_with_the_other_versions.html)*

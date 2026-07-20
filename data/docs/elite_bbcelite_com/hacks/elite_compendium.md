---
title: Elite Compendium
source_url: https://elite.bbcelite.com/hacks/elite_compendium.html
category: reference
topics:
- basic
- assembly
- sprite programming
- input handling
difficulty: intermediate
language: mixed
hardware:
- CIA
- SID
- CPU
- VIC-II
- KERNAL
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

# Elite Compendium

## Bringing all the best Elite hacks together in four feature-packed discs

The Elite Compendium is a collection of the very best of Acornsoft Elite, updated with as many hacks and enhancements as I've been able to fit in. If you're looking to play 8-bit Elite, then this is a pretty good place to start.

The Compendium is available for the BBC Master 128, the BBC Micro B/B+ with 16K of sideways RAM, and the Acorn Electron with 16K of sideways RAM. There is also an Addendum with versions for the BBC Micro B+. This is what you get:

| Disc menu | Contents | 
|---|---|
| ![The menu for the BBC Master version of the Elite Compendium](https://elite.bbcelite.com/images/elite_compendium/menu.png) | BBC Master 128 Enhanced Compendium versions of:
											BBC Master 128 Elite6502 Second Processor EliteBBC Micro disc EliteTeletext Elite
Elite Universe Editor[Download or play in your browser](https://elite.bbcelite.com/elite_compendium_downloads.html)
 | 
| ![The menu for the BBC Micro version of the Elite Compendium](https://elite.bbcelite.com/images/elite_compendium/menu_bbc_micro.png)  | BBC Micro B/B+ with 16K of sideways RAM Enhanced Compendium versions of:
											BBC Micro disc Elite6502 Second Processor EliteBBC Micro cassette EliteTeletext Elite
Elite Universe Editor[Download or play in your browser](https://elite.bbcelite.com/elite_compendium_downloads.html)
 | 
| ![The menu for the Acorn Electron version of the Elite Compendium](https://elite.bbcelite.com/images/elite_compendium/menu_electron.png) | Acorn Electron with 16K of sideways RAM Enhanced Compendium versions of:
											Acorn Electron EliteAcorn Electron Elite with music
Flicker-free Electron cassette Elite[Download or play in your browser](https://elite.bbcelite.com/elite_compendium_downloads.html)
 | 
| ![The menu for the BBC Micro B+ version of the Elite Compendium](https://elite.bbcelite.com/images/elite_compendium/menu_bbc_micro_b_plus.png)  | BBC Micro B+ Compendium Addendum Enhanced Compendium versions of:
											BBC Master 128 EliteBBC Master 128 Elite with music
For the BBC Micro B+ and B+128, which can also run the BBC Micro version of the Compendium above[Download](https://elite.bbcelite.com/elite_compendium_downloads.html)
 | 

## Main enhancements in the Compendium versions of Elite

													 -----------------------------------------------------

						All the extra features and enhancements in the Compendium versions of Elite have been backported from other versions of the game, so everything is part of the official Elite canon. These are the most important enhancements in the Compendium:

| Feature | Details | Taken from | 
|---|---|---|
| Flicker-free | I've added flicker-free ships and planets using the algorithm from the Apple II (read more about [flicker-free Elite](https://elite.bbcelite.com/hacks/flicker-free_elite.html)) | Apple II | 
| Music | I've added the music from the Commodore 64 version, with two different tunes and options to swap tunes, disable music and change the volume (read more about [musical Elite](https://elite.bbcelite.com/hacks/bbc_elite_with_music.html)) | Commodore 64 | 
| Volume | I've added volume control for all sound effects (pause the game and use "<" and ">" to change the volume of music and sound effects) | BBC Master | 
| Trumbles | I've backported the non-sprite version of the Trumbles mission from the NES version (read more about [the Trumbles mission](https://elite.bbcelite.com/deep_dives/the_trumbles_mission.html)) | NES | 
| Docking | I've backported a couple of docking computer improvements from the NES version, to make auto-docking a bit more enjoyable: The station no longer spawns traders, like Transporters or Shuttles, while the docking computer is activatedOnce you're inside the station's safe zone and you've activated your docking computer, you can press "J" to dock instantly
 | NES | 
| Fuel scoops | Fuel scoops will only work when you are moving, which makes a lot more sense | NES | 
| Joysticks | When joysticks are enabled, the "fire laser" key on the keyboard is no longer disabled, so you can have one hand on the stick and one on the keyboard | BBC Master | 
| Delta 14B | Taking inspiration from Angus Duggan's Elite-A, I've added full support for the Voltmace Delta 14B joystick, so if you are lucky enough to own one of these and the accompanying 14B/1 adaptor box, you can now fly your Cobra Mk III without relying on the keyboard | Elite-A | 

All of the Compendium versions of Elite contain all of the above enhancements, with the following exceptions:

- The Compendium version of BBC Micro cassette Elite doesn't include the Trumbles mission, as this version doesn't include any missions at all.
- The Compendium version of Acorn Electron Elite doesn't include volume control as the hardware can't support it.

These are the main features of the Compendium, but there's more, so let's look at exactly what you get in each Compendium version.

## More details about the enhanced Compendium versions of Elite

													 ------------------------------------------------------------

						There are quite a few other features in the Compendium versions of Elite, so here's a complete breakdown of every single enhancement:

| Version | Extra enhancements in the Compendium version of Elite | 
|---|---|
| BBC Master 128 Elite | Includes all the enhancements shown above (flicker-free, music, volume, Trumbles, docking, fuel scoops, joysticks and Delta 14B)Enemies have red lasers rather than cyan, just like the 6502 Second Processor versionI've fixed the following bugs from the original release:
										Deleting a file no longer breaks the "save commander" option, unlike in the official releaseThe Data on System screen now works for all systems (in the official release, it breaks for some systems - for example, visiting Biarge during the Constrictor mission will hang the game)The Moray can now be spawned as a bounty hunter, albeit rarely (in the official release, the Moray never spawns at all, and the ship is never seen in-game)Joysticks are now disabled when the docking computer is running
When played on the BBC Micro B+, you need sideways RAM to support music, so there are two versions on the Compendium Addendum: the version for the B+128 includes music, while the version for the unexpanded B+ does not (the B+128 version will also work on the B+ with 16K of sideways RAM)
 | 
| 6502 Second Processor Elite | Includes all the enhancements shown above (flicker-free, music, volume, Trumbles, docking, fuel scoops, joysticks and Delta 14B)I've slowed down spaceflight so it's about the same speed as standard Elite, as otherwise the game is all but unplayable on the super-fast co-processor (though the power of the co-pro still ensures that there is minimal slowdown when things get busy)I've fixed the following bugs from the original release:
										The Data on System screen now works for all systems (in the official release, it breaks for some systems - for example, visiting Biarge during the Constrictor mission will hang the game)The Moray can now be spawned as a bounty hunter, albeit rarely (in the official release, the Moray never spawns at all, and the ship is never seen in-game)
 | 
| BBC Micro disc Elite | Includes all the enhancements shown above (flicker-free, music, volume, Trumbles, docking, fuel scoops, joysticks and Delta 14B)I've updated the original 1984 release to run on the Master as well as the BBC Micro (read more about [BBC Micro disc Elite on the BBC Master](https://elite.bbcelite.com/bbc_master_disc_elite.html))
 | 
| BBC Micro cassette Elite | Includes all the enhancements shown above except for the Trumbles mission (so that's flicker-free, music, volume, docking, fuel scoops, joysticks and Delta 14B)You can now save and load commanders from disc, though to keep the experience authentic, there are no options for cataloguing the disc, changing drive number or deleting files; instead, commanders are only supported on drive 0 (in directory E, as with the disc version), and you have to know the name of the commander to load in advanceNote that all docking in this version is already instant, so simply engaging the docking computer will take you to the docking bay (there's no need to press "J")
 | 
| Acorn Electron Elite | Includes all the enhancements shown above except for volume (so that's flicker-free, music, Trumbles, docking, fuel scoops, joysticks and Delta 14B; the standard Electron can't physically support different volumes)Also includes every feature from the BBC Micro disc version (except the four-colour dashboard)Comes in two versions, with or without music; the non-music version runs on all filing systems, including Plus 3 ADFS, while the music version needs E00 DFS, MMFS or ADFS
 | 
| Teletext Elite | Includes all the enhancements shown above (flicker-free, music, volume, Trumbles, docking, fuel scoops, joysticks and Delta 14B)This is BBC Micro disc Elite, converted to run entirely in teletext mode 7 for peak 1980s nostalgia (read more about [Teletext Elite](https://elite.bbcelite.com/hacks/teletext_elite.html))
 | 

Because of the extra memory required by all these Elite hacks, the Compendium versions of Elite need a BBC Master 128, a BBC Micro with 16K of sideways RAM, or an Acorn Electron with 16K of sideways RAM. You will also need a 6502 co-processor if you want to play the 6502 Second Processor version of Elite.

The following also come with the Elite Compendium. They aren't specially enhanced Compendium versions, but they're still worth a look:

| Version | Details | 
|---|---|
| Elite Universe Editor | Create your own universes and "press play" to see them come to lifeComes with seven example universes, including the iconic screenshots from the Acornsoft and Commodore 64 game boxesThe BBC Micro version requires a 6502 Second ProcessorRead more about the [Elite Universe Editor](https://elite.bbcelite.com/hacks/elite_universe_editor.html), where you can also find[full instructions](https://elite.bbcelite.com/hacks/elite_universe_editor_instructions_bbc.html)
 | 
| Flicker-free Acorn Electron cassette Elite | This is an enhanced version of the original cassette version that doesn't require sideways RAMIt loads from disc but still uses the tape for saving and loading commander filesContains flicker-free ships and planets, the escape capsule animation, three sizes of stardust and high-fidelity planets (read more about [flicker-free Electron Elite](https://elite.bbcelite.com/flicker-free_elite_technical_information.html))
 | 

Apart from the Elite Universe Editor and the use of teletext in Teletext Elite, all of the hacks included in the Compendium are 100% canon - they are all taken from official versions of 6502 Elite, as noted above. This means they were all written by Elite's authors, Ian Bell and David Braben (with Aidan Bell and Julie Dunn composing the music). So the flicker-free drawing algorithm is from Apple II Elite, the music comes from the Commodore 64 version, the docking computer enhancements are from the NES version, red enemy lasers are from the 6502 Second Processor version, and so on.

So the Compendium is effectively a Greatest Hits of the original Elite, and in terms of gameplay, nothing new has been added; it's all original Bell and Braben brilliance, just backported to work on the BBC Master and BBC Micro.

## What else is on the disc?

													 -------------------------

						The Compendium also contains three commander files on drive 0, which you can load into any version of Elite via the save and load menu (press "Y" on the title screen or press "@" when docked):

- MISS1 is for those who want to play the [Constrictor mission](https://elite.bbcelite.com/deep_dives/the_constrictor_mission.html); load it, launch from the station, dock once again (you have a docking computer) and the mission will start.
- MISS2 is for those who want to play the [Thargoid Plans mission](https://elite.bbcelite.com/deep_dives/the_thargoid_plans_mission.html), and you can trigger it in the same way.
- MAX is a maxed-out commander to let you hit the ground running.

All of these commanders will also trigger the [Trumbles mission](https://elite.bbcelite.com/deep_dives/the_trumbles_mission.html) when you dock:

![The Trumbles mission on the BBC Master in the Elite Compendium](https://elite.bbcelite.com/images/elite_compendium/bbc_trumbles1.png) 

						If you load MISS1 or MISS2, then the Trumble mission will be offered on your second docking, as the first docking will trigger the missions shown above; if you load MAX, then the Trumbles will be offered on your first docking. Remember that the Compendium implements instant docking with the docking computer, so the quickest way to trigger a mission is to load the relevant commander file, then press f0 to launch, "C" to activate the docking computer, "J" to insta-dock, and then you will be offered the mission.

The BBC versions of the Compendium also contain a full collection of universe files on drive 2, which you can load into the Elite Universe Editor. See the [Universe Editor instructions](https://elite.bbcelite.com/hacks/elite_universe_editor_instructions_bbc.html#example) for details.

---
*Fonte originale: [https://elite.bbcelite.com/hacks/elite_compendium.html](https://elite.bbcelite.com/hacks/elite_compendium.html)*

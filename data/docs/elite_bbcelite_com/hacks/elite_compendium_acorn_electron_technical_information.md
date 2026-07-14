---
title: Technical information on the Compendium version of Acorn Electron Elite
source_url: https://elite.bbcelite.com/hacks/elite_compendium_acorn_electron_technical_information.html
category: source-code
topics:
- sprite programming
- basic
- assembly
- graphics
- memory management
- input handling
difficulty: intermediate
language: mixed
hardware:
- BASIC ROM
- CIA
- SID
- CPU
- KERNAL
related:
- cia-registers
- keyboard-handling
- sound-programming
- music-player
- raster-interrupts
- joystick-reading
- memory-map
- sprite-programming
- vic-ii-registers
- kernal-routines
- sid-registers
scraped_at: '2026-07-14'
---

# Technical information on the Compendium version of Acorn Electron Elite

## How I backported BBC Micro disc Elite to the Acorn Electron with sideways RAM

The Compendium version of Electron Elite is a massively extended and enhanced variant of the original, but at its core it is still Acorn Electron Elite: all the extra features have been added on to the original code, as opposed to being a backport of a different version from a different platform. Fans of the original will feel right at home, as this is Electron Elite, lovingly enhanced into the game that it should have been.

In this article I'll take a deeper look at all the extra features, especially the use of sideways RAM, which gives the game a considerable speed boost compared to the 1984 original.

If you want to see exactly how the code for the Compendium version of Electron Elite differs from the code in the original Acornsoft version, you can check out the relevant branches in the project repository:

- See the [elite-compendium branch](https://github.com/markmoxon/elite-source-code-acorn-electron/tree/elite-compendium/1-source-files/main-sources)for modifications related to Acorn Electron Compendium Elite.
- See the [elite-compendium-music branch](https://github.com/markmoxon/elite-source-code-acorn-electron/tree/elite-compendium-music/1-source-files/main-sources)for modifications related to musical Acorn Electron Compendium Elite.

You can search the source code files in these branches for "Mod:" to see every single modification that I've made to the original code to produce the Compendium version.

## Speeding up the Acorn Electron version

													 --------------------------------------

						On the Acorn Electron, the Compendium version of Elite is a lot faster than the original. Here's a side-by-side comparison, with the original version on the left and the Compendium on the right:

The bulk of this improvement is down to the use of sideways RAM. All versions of the Elite Compendium use sideways RAM, but on the Electron the impact is far more profound than simply having more memory to play with.

On the Electron, the custom ULA controls the entire system, and all memory access is done via the ULA. Due to cost-cutting in the design of the RAM system and the need to interleave screen memory access with main memory, code can only access locations in main memory at 1MHz, which is half the 2MHz access speed that the BBC Micro boasts. This is the primary reason that the Electron is noticeably slower than the BBC Micro.

However, this speed restriction only applies to main memory, i.e. from address &0000 to &7FFF. Memory from &8000 to &FFFF is accessed at the full 2MHz, so fetching data and instructions from the operating system and language ROMs is as fast as on the BBC Micro. Because sideways RAM lives at &8000, this means it can also be accessed at 2MHz. The Electron has the same 2MHz 6502 CPU as the BBC Micro, so code that lives above address &8000 and which only accesses data from above &8000 will effectively run at the same speed as it would on the BBC.

For the Compendium version of Electron Elite, I've moved all speed-critical code and variables into sideways RAM. I've left zero page alone, as although it is accessed at 1MHz, the 6502's faster and smaller zero-page instructions cancel out any advantage of moving zero page variables into sideways RAM.

The speed difference is impressive. It doesn't run as fast as BBC Micro Elite, because we still have to access screen memory at 1MHz (as screen memory runs from &5800 to &7FFF), but outside of screen-poking, the core flight code runs as fast as it possibly can. Non-critical code still lives in main memory, as we don't need to speed up aspects like trading, system charts or saving commander files, but everything that matters is now in sideways RAM.

On top of this, I've backported the logarithm-based multiplication and division routines from the 6502 Second Processor, which run noticeably faster than the loop-based routines from the original version (though they take up a lot more memory). And I've backported various specialist routines, such as the dedicated horizontal line-drawing routine at HLOIN, which were left out of the Electron version due to a lack of free space.

In all, this extra speed and memory means the Electron can finally run all the features of BBC Micro Elite, and without grinding to a halt.

## New features in the Acorn Electron version

													 ------------------------------------------

						To bring Acorn Electron Elite up to the level of the other 6502 versions, I not only wanted to backport all the extra features from the BBC Micro disc version of Elite, but I also wanted to add as many extra Compendium features as possible.

With the exception of the four-colour dashboard, Electron players can now enjoy everything that the BBC Micro had back in 1984. Here's a complete list of features I've added to the Compendium version of Electron Elite, and below that is a blow-by-blow comparison between the various versions.

Unless otherwise stated, features have been backported from the BBC Micro disc version of Elite.

- Speed improvements
								- Significant speed increase over the standard version due to fast sideways RAM
- Logarithm-based maths routines for a further speed boost (6502 Second Processor)
- Optimised routines (such as HLOIN) backported from various other 6502 versions
 
- Graphical improvements
								- Flicker-free ships (BBC Master)
- Flicker-free planets (using the same algorithm as ships)
- Circular planets with meridians, equators and craters (no more 50p planets!)
- Energy bomb lightning effect (BBC Master)
- Escape capsule animation
- Three sizes of stardust rather than two (one-pixel stardust added)
- Variable star sizes in the Short-range Chart
 
- In-station features
								- Extra lasers (military, mining)
- Improved selling mechanism (sell all or part of your cargo)
- Extended system descriptions (edible poets!)
- System search in the Long-range Chart
- Hold SHIFT to move the chart pointer more quickly
 
- In-flight features
								- All 31 ship and station designs from the BBC Micro disc version
- Advanced enemy tactics (NEWB) and spawning logic
- Suns, cabin temperatures and fuel scooping
- Fuel scoops only work when moving (NES)
- Asteroid mining
- Thargoids and witchspace
 
- Docking
								- Proper docking computer sequence
- Pressing "J" will dock instantly when docking computer is activated (NES)
- Transporters no longer spawn in the station slot when we're auto-docking (NES)
- The ship hangar is shown on docking
 
- Missions
								- Both BBC Micro missions (Constrictor and Thargoid plans)
- Trumbles mission (Commodore 64 and NES)
 
- Loading and saving
								- Disc access menu for saving, loading, cataloguing and deleting commander files
- Full support for ADFS, DFS and MMFS on all media, including the Plus 3
- The Acornsoft loading screen no longer has the panel for showing tape progress
 
- Joysticks
								- Joystick support added for Plus 1 analogue joysticks (BBC Micro)
- Joystick support added for Slogger and First Byte digital joysticks (BBC Master Compact)
- Full button support added for the Delta 14B joystick with Delta 14B/1 adaptor box (Elite-A)
- Keyboard fire button still works when joysticks are enabled (BBC Master)
 
- Bug fixes and tweaks
								- Includes bug fixes from the Elite Compendium (Data on System, Moray spawning)
- Broken sound priorities and durations have been fixed in the sound generation routine
- The second title screen now has a rotating Constrictor instead of a Mamba (so the Compendium has its own unique ship, rather than reusing the BBC Micro cassette's Mamba)
 

Notes:

- When launching, hyperspacing, docking and restarting, there is a small pause while the game loads ship blueprints from disc, just like the BBC Micro disc version.
- When using ADFS on the Plus 3, the screen might flicker during disc access.
- All features from the original BBC Micro disc version are included except for the four-colour dashboard.
- All features from the Elite Compendium are included except for volume control (the standard Electron can't physically support this).

Here's a feature-by-feature comparison showing how the Compendium version of Electron Elite has finally caught up with the original 1984 versions. (See the full [feature comparison table](https://elite.bbcelite.com/compare/feature_comparison.html) for more information on the items in the table and to compare all the other versions of 6502 Elite.)

| Feature | BBC Micro Cassette | BBC Micro Disc | Compendium Electron | Standard Electron | 
|---|---|---|---|---|
| Release year | 1984 | 1984 | 2025 | 1984 | 
| Ship types | 13 | 31 | 31 | 11 | 
| Thargoids, Thargons | Yes | Yes | Yes | No | 
| Dodo space station | No | Yes | Yes | No | 
| Cougar | No | No | No | No | 
| Cougar has a cloaking device | n/a | n/a | n/a | n/a | 
| Rock hermits | No | No | No | No | 
| Distinct ship designs | 12 | 29 | 29 | 10 | 
| Max. ships in the local bubble | 10 | 10 | 10 | 10 | 
| Max. cops in the local bubble | 4 | 4 | 3 | 3 | 
| Bytes in each ship's data block | 36 | 37 | 37 | 36 | 
| Enhanced AI and spawning (NEWB) | No | Yes | Yes | No | 
| Ships that Anacondas can spawn | n/a | Worm | Worm | n/a | 
| Colours in the space view | 2 | 2 | 2 | 2 | 
| Colours in the dashboard | 4 | 4 | 2 | 2 | 
| Flashing dashboard indicators | Yes | Yes | No | No | 
| Ship colours in the 3D scanner | 2 | 2 | 1 | 1 | 
| Dot height in the 3D scanner (pixels) | 2 | 2 | 2 | 2 | 
| Compass dot (in front) | Thick yellow | Thick yellow | Thick white | Thick white | 
| Compass dot (behind) | Thin green | Thin green | Thin white | Thin white | 
| Space view height (pixels) | 192 | 192 | 192 | 192 | 
| Space view width (pixels) | 256 | 256 | 256 | 256 | 
| Dashboard height (pixels) | 56 | 56 | 56 | 56 | 
| Dashboard width (pixels) | 128 | 128 | 256 | 256 | 
| Escape pod colour scheme | Palette | Palette | No | No | 
| Mining lasers and asteroid mining | No | Yes | Yes | No | 
| Military lasers | No | Yes | Yes | No | 
| Crosshair colour varies with laser type | No | No | No | No | 
| Crosshair design varies with laser type | No | No | No | No | 
| Enemy laser colour | White | White | White | White | 
| Proper docking computer | No | Yes | Yes | No | 
| Sun, fuel scooping, cabin temperature | Yes | Yes | Yes | No | 
| Planet meridians and craters | Yes | Yes | Yes | No | 
| Extended text tokens | No | Yes | Yes | No | 
| Extended system descriptions | No | Yes | Yes | No | 
| Missions | No | 2 | 3 | No | 
| Energy bomb kills Constrictor | n/a | Yes | Yes | n/a | 
| Energy bomb kills Thargoids | Yes | Yes | Yes | n/a | 
| Energy bomb graphical effect | Flash | Flash | Lightning | No | 
| "Press Fire or Space" ship | Mamba | Krait | Constrictor | Mamba | 
| Search for systems by name | No | Yes | Yes | No | 
| Key to move chart pointer quickly | No | SHIFT | SHIFT | No | 
| Buy/sell specific amounts of cargo | No | Yes | Yes | No | 
| Buy all available cargo with "Y" | No | Yes | Yes | No | 
| Display ship hangar on docking | No | Yes | Yes | No | 
| Launch tunnel colour | White | White | White | White | 
| Disc access menu | No | Yes | Yes | No | 
| Revert to default commander | No | No | No | No | 
| Fractional kill counts | No | No | No | No | 
| Kill count varies by ship type | No | No | No | No | 
| Kill count for cargo, asteroids, escape pods, Thargons | No | Yes | Yes | No | 
| "S/E" indicator width (in space view pixels) | 6 | 6 | 7 | 7 | 
| Fuel goes red when low | Yes | Yes | No | No | 
| Volume control | No | No | No | No | 
| Sound effects | Standard | Standard | Basic | Basic | 
| Laser sound attack phase amplitude | 112 | 126 | n/a | n/a | 
| Save screenshot | No | No | No | No | 
| Send trade screens to printer | No | No | No | No | 
| Logarithm-based maths routines | No | No | Yes | No | 
| Hostile ships spawning distance | 32 | 25 | 32 | 32 | 
| Galactic hyperspace counts down from | 15 | 15 | 15 | 15 | 
| Hyperspace countdown text column | 5 | 6 | 5 | 5 | 
| Rings in the hyperspace tunnel | 16 | 16 | 16 | 16 | 
| Witchspace | Yes | Yes | Yes | No | 
| Launch escape pod in witchspace | Fatal | Yes | Yes | n/a | 
| Thargoids in witchspace | 4 | 4 | 2 | n/a | 
| Docking check #3 | Yes | No | Yes | Yes | 
| Docking check #4 vector | Station | Planet | Station | Station | 
| Docking check #4 angle | 22.0° | 26.3° | 22.0° | 22.0° | 
| Medium circle radius range | 8-60 | 8-60 | 8-60 | 9+ | 
| Explosion particles per vertex | 15 | 15 | 7 | 7 | 
| Stardust particles | 18 | 18 | 10 | 10 | 
| Top laser line vertical offset | 0 | 0 | 0 | 0 | 
| In-flight message position | Column 9 | Column 9 | Column 9 | Column 9 | 
| Max. junk shown on our death | 4 | 5 | 4 | 4 | 
| Version bit number in save file | 1 | 2 or 5 | 3 | 3 | 
| "Star Wars" scroll text and demo | No | No | No | No | 
| Random Saturn on load screen | Yes | Yes | Yes | Yes | 
| Title banners on load screen | Yes | Yes | Yes | Yes | 
| Saturn planet dot counts | 1280 | 768 | 1280 | 1280 | 
| Saturn ring dot counts | 1280 | 819 | 1280 | 1280 | 
| Saturn dot plotting logic | OR | Overwrite | OR | OR | 
| TINA hook | No | No | No | No | 
| Joystick support | Yes | Yes | Yes | No | 
| Bitstik support | No | Yes | Yes | No | 
| Loading pause on launch/dock | No | Yes | Yes | No | 

As well as the list above, the Compendium version of Acorn Electron Elite has the following Compendium-specific features:

- Flicker-free ships
- Flicker-free planets
- Trumbles mission
- Docking computer improvements
- Fuel scoop improvements
- Joystick improvements
- Music
- Delta 14B joystick support

Read [about the Elite Compendium](https://elite.bbcelite.com/elite_compendium.html) for more information on these extra features.

---
*Fonte originale: [https://elite.bbcelite.com/hacks/elite_compendium_acorn_electron_technical_information.html](https://elite.bbcelite.com/hacks/elite_compendium_acorn_electron_technical_information.html)*

---
title: Playing the musical version of Acornsoft Elite
source_url: https://elite.bbcelite.com/hacks/bbc_elite_with_music_downloads.html
category: tool
topics:
- basic
- assembly
difficulty: intermediate
language: mixed
hardware:
- KERNAL
- SID
- CPU
- CIA
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

# Playing the musical version of Acornsoft Elite

## How to download and play Acornsoft Elite with music

The [Elite Compendium](https://elite.bbcelite.com/elite_compendium.html) is a great way to enjoy musical Elite in combination with my other hacks - see the [download page](https://elite.bbcelite.com/elite_compendium_downloads.html) for details. Or you can play musical Elite by choosing one of the following:

- BBC Micro Elite with music
- 6502 Second Processor Elite with music
- BBC Master 128 Elite with music
- BBC Master Compact Elite with music
- BBC Master Elite with music on the BBC Micro B+128
- Acorn Electron Elite with music
								- [Play online](https://0xc0de6502.github.io/electroniq/?dfs&autoboot&ram6&disk0=https://elite.bbcelite.com/versions/elite_compendium/elite-compendium-acorn-electron.dsd)as part of the Elite Compendium
- [Download DSD](https://elite.bbcelite.com/versions/elite_compendium/elite-compendium-acorn-electron.dsd)of the Elite Compendium
 

To load the musical version of Elite, simply insert the disc image and press SHIFT-D-BREAK (for DFS), SHIFT-M-BREAK (for MMFS), SHIFT-S-BREAK (for Micro SPI) or use the *DBOOT command (for all SD card solutions); emulators tend to map BREAK to F12, so press SHIFT-D-F12. The disc will automatically load if you're playing it in a browser. For the BBC Micro and Acorn Electron versions, you will need at least 16K of sideways RAM, though note that not all sideways RAM solutions are supported (see below). The BBC Micro B+128 and BBC Master come with sideways RAM as standard.

If you want to enjoy a bit of *docking à la Blue Danube*, then you will need to load the maxed-out commander file that's included in the disc image. To do this, press "Y" on the title screen to bring up the menu, press "1" to choose the load option, enter "MAX" (without the quotes) as the commander name, and press "0" for the drive number. This will give you a fully stocked commander, and when you launch into space by pressing f0 (or f10 if you're playing in your browser), you can then press "C" to engage the docking computer, and can sit back and enjoy that iconic music while the docking computer does its stuff.

If you just want to hear the docking music, you can also swap the tunes around to hear the Blue Danube on the title screen, as described in the next section.

## Stopping, starting and swapping music

													 -------------------------------------

						To go along with the music, there are two new game configuration options, also ported from the Commodore 64 version. As with the existing game options, you can toggle these settings by first pausing the game (press COPY on a real machine, or End in most emulators), and then pressing the relevant option key. You will hear a beep confirming your choice, and you can then return to the game by pressing DELETE on a real machine, or backspace in most emulators.

The new music-related configuration options are:

- M - toggle music on and off (while leaving the sound effects alone)
- E - swap tunes, so the docking music is played on the title screen, and the title music is played when docking (or, if this is the second press, swap them back)

The music will also be disabled if you turn off the game's sound using the game's Q configuration option.

## Changing the volume

													 -------------------

						The BBC Master version of Elite already lets you change the volume of the game's sound effects, and this has been extended so it changes the music volume as well. The volume control system has also been backported to the BBC Micro and 6502 Second Processor versions of musical Elite, so us lowly Beeb owners can finally enjoy a quieter game without having to stuff a sock into the loudspeaker grille. Note that you can't change the volume in the Electron version as the underlying hardware doesn't support this.

You can change the volume by pausing the game (press COPY on a real machine, or End in most emulators), and then doing the following:

- Press "<" to reduce the volume by one notch
- Press ">" to increase the volume by one notch

The volume setting runs from 1 (very quiet) up to 8 (wake the neighbours). In the BBC Master versions, the game's initial volume will start at full volume if Loud is configured (i.e. *CONFIGURE LOUD), or half volume if Quiet is configured (i.e. *CONGFIGURE QUIET). On the BBC Micro and 6502 Second Processor versions, the game starts at full volume. If music is playing when you pause the game, it will continue playing so you can easily change the volume to the level you are happy with; otherwise the game will beep at the currently selected volume as you alter it.

Sound effects are disabled while music is playing, to prevent clashing.

You can return to the game by pressing DELETE on a real machine, or backspace in most emulators.

## Notes on sideways RAM

													 ---------------------

						When loading, the game will check for the presence of sideways RAM, and if successful it will load the music and ask you to press a key to play the game. If the game can't find any sideways RAM, then it will tell you and give up. Note that your sideways RAM must be writeable, so if you are on a BBC Micro and have a read/write switch fitted, make sure it's in the write-enable position.

Note that the game will only work with sideways RAM that uses the ROMSEL latch at SHEILA &FE30 to switch banks. The BBC Master's sideways RAM is fine, but some types of BBC Micro sideways RAM use the RAMSEL latch at SHEILA &FE32, while others use the user port at SHEILA &FE60 and &FE62, and I'm afraid there just isn't enough free memory in Elite to support all these different styles of sideways RAM. In particular, owners of Solidisk or Watford Electronics sideways RAM may be out of luck here.

The Acorn Electron should be fine, as all the sideways RAM systems work in the same way.  See [playing the Compendium version of Acorn Electron Elite](https://elite.bbcelite.com/elite_compendium_acorn_electron_downloads.html) for details of the various sideways RAM options for the Electron.


													 ---------------

						Acornsoft Elite with music has had the following releases:

- 2023-02-10 - Initial release of the BBC Micro version
- 2023-03-09 - Added options for toggling music on/off and swapping tunes, and stop music when sound is disabled
- 2023-03-10 - Fixed an issue in the BBC Micro version where music could sometimes be disabled on load
- 2023-03-10 - Initial release of the BBC Master 128 and BBC Master Compact versions
- 2023-03-13 - Updated sideways RAM checks to check for &FE30-style RAM only, as that's the only type that is supported
- 2023-03-14 - Fixed an issue in the BBC Master versions that could corrupt music when scanning for key presses
- 2023-03-14 - Initial release of the 6502 Second Processor version
- 2023-03-15 - Fixed an issue in the BBC Master versions that crashed the game on pause
- 2023-04-14 - Updated the copyright notice for the Commodore 64 music in all versions
- 2023-12-11 - Improved the sideways RAM loader and updated BBC Master support to cover MOS 3.50 as well as MOS 3.20
- 2024-01-03 - New features for the BBC Micro and 6502 Second Processor: backported the volume control system from the BBC Master and applied it to music and sound effects; disabled sound effects while music is playing to prevent clashes
- 2024-01-04 - New features and bug fixes for the BBC Master 128 and BBC Master Compact: extended the volume control system to apply to music as well as sound effects; set the game's initial volume according to the quiet/loud configuration setting; disabled sound effects while music is playing to prevent clashes; fixed random noises when accessing the disc; stopped filing system errors from crashing the game
- 2024-05-09 - Fixed the keyboard translation routine in the BBC Micro version to make it more reliable on the B+
- 2024-07-11 - Applied the volume setting to explosions in the BBC Micro version, as they weren't being muted
- 2025-08-19 - Released the Acorn Electron musical version as part of the Elite Compendium
- 2025-08-30 - Released the BBC Micro B+128 musical version
- 2025-09-18 - Fixed the catalogue and delete options in the B+128 disc menu, which weren't working on real hardware
- 2026-01-15 - Updated the music loader to my own version that skips sideways RAM banks that already contain ROM images

You can check the release for a given disc image by loading the disc and typing *TYPE README to display the credits. The build date is at the end.

---
*Fonte originale: [https://elite.bbcelite.com/hacks/bbc_elite_with_music_downloads.html](https://elite.bbcelite.com/hacks/bbc_elite_with_music_downloads.html)*

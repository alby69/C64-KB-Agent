---
title: Playing the Elite Universe Editor
source_url: https://elite.bbcelite.com/hacks/elite_universe_editor_downloads.html
category: manual
topics:
- basic
- assembly
difficulty: intermediate
language: assembly
hardware:
- CPU
- SID
- KERNAL
related:
- music-player
- sound-programming
- memory-map
- kernal-routines
- sid-registers
scraped_at: '2026-07-14'
---

# Playing the Elite Universe Editor

## How to download and play the Elite Universe Editor

*The  Elite Compendium is a great way to enjoy all of my Elite hacks, including the Universe Editor - see the download page for details.*

To start creating your own universes in Elite, you can do the following:

- Run the [6502 Second Processor](https://bbc.xania.org/?coProcessor=true&autoboot&disc=https://elite.bbcelite.com/versions/elite_universe_editor/elite-universe-editor-bbc.ssd)version in your browser. This is the most powerful and fastest version, and is recommended.
- Run the [BBC Master](https://bbc.xania.org/?model=Master&autoboot&disc=https://elite.bbcelite.com/versions/elite_universe_editor/elite-universe-editor-bbc.ssd)version in your browser. This version is less powerful, but the Master version has flicker-free graphics, so it looks better.
- Download the BBC version of the Universe Editor [as a disc image](https://elite.bbcelite.com/versions/elite_universe_editor/elite-universe-editor-bbc.ssd)that will run in an emulator, on a BBC Micro or BBC Master with a 6502 Second Processor, or on a standard BBC Master 128.
- Download the Commodore 64 version of the Universe Editor [as a D64 disk image for PAL](https://elite.bbcelite.com/versions/elite_universe_editor/elite-universe-editor-c64-pal.d64)or[as a D64 disk image for NTSC](https://elite.bbcelite.com/versions/elite_universe_editor/elite-universe-editor-c64-ntsc.d64). This will run in an emulator or on a standard Commodore 64. PAL is the best version to use for emulators and most European machines, while NTSC is the best version to use for most machines from the Americas.

To load the Universe Editor on a BBC, simply insert the disc image and press SHIFT-D-BREAK (for DFS), SHIFT-M-BREAK (for MMFS), SHIFT-S-BREAK (for Micro SPI) or use the *DBOOT command (for all SD card solutions); emulators tend to map BREAK to F12, so press SHIFT-D-F12. The disc will automatically load if you're playing it in a browser.

To load the Universe Editor on a Commodore 64, insert the disk image and enter LOAD "*",* followed by RUN (or just drag the disk image into your emulator).

You can swap universe files between all the different versions across both platforms, so pick the version that suits you (though note that the Master and Commodore 64 versions don't support every feature from the BBC Micro 6502 Second Processor version - [see the technical information](https://elite.bbcelite.com/elite_universe_editor_technical_information.html#master) for details).


													 ---------------

						The Universe Editor has had the following releases:

- 2022-10-27 - Initial release (BBC version)
- 2023-01-12 - Commodore 64 version released alongside an updated BBC version, with an improved file format to support both platforms, and various minor bug fixes for the BBC version
- 2024-08-27 - Fixed a minor issue with the BOXART2 universe file that would make it take up more memory than required

You can check the release for a given disc image by loading the disc and typing *TYPE README to display the credits. The build date is at the end.

Not that universe files saved from the initial 2022-10-27 release need to be converted to work in later versions. There is a BASIC program called B.CONVERT included on later versions to do this conversion. See the [see the technical information](https://elite.bbcelite.com/elite_universe_editor_technical_information.html#file) for details


													 ------------

						On the 6502 Second Processor version, explosions can leave some of their particles behind when deleted or selected (and striped ships like Thargoids and Morays can sometimes do the same). You can get rid of any unwanted explosion particles by simply changing to a different view and back again. This issue does not affect the BBC Master version, where explosions are better behaved.

As noted in the [technical information](https://elite.bbcelite.com/elite_universe_editor_technical_information.html#master), loading files that were created on the 6502 Second Processor version into the BBC Master version can be a bit hit and miss.

If you find any bugs in the Universe Editor, then you can let me know via [this Stardot thread](https://stardot.org.uk/forums/viewtopic.php?f=74&t=25753) or by [emailing me](https://www.markmoxon.com/guestbook). I'll see what I can do to help.

---
*Fonte originale: [https://elite.bbcelite.com/hacks/elite_universe_editor_downloads.html](https://elite.bbcelite.com/hacks/elite_universe_editor_downloads.html)*

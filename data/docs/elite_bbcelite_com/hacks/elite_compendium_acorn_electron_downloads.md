---
title: Playing the Compendium version of Acorn Electron Elite
source_url: https://elite.bbcelite.com/hacks/elite_compendium_acorn_electron_downloads.html
category: reference
topics:
- basic
- assembly
- input handling
difficulty: intermediate
language: mixed
hardware:
- KERNAL
- SID
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

# Playing the Compendium version of Acorn Electron Elite

## How to download and play the improved version of Acorn Electron Elite

The [Elite Compendium](https://elite.bbcelite.com/elite_compendium.html) is the best way to enjoy the Compendium version of Acorn Electron Elite, in combination with my other hacks - see the [download page](https://elite.bbcelite.com/elite_compendium_downloads.html) for details.

This page looks at the requirements for running the Compendium version of Acorn Electron Elite.

## Hardware requirements

													 ---------------------

						To run the Compendium version of Elite on the Acorn Electron, you'll need 16K of sideways RAM and a proper storage system (i.e. floppy disc, SD card or similar). There are both traditional and modern options that provide these features.

- If you want to stick to original hardware, the Compendium will work with Acorn's Plus 1 expansion system with a sideways RAM cartridge, and with the Plus 3 disc drive. All of these could be bought back in the 1980s, though they don't necessarily come cheap these days.
- If you're OK with a modern solution, there are lots of options:
								- The easiest and most cost-effective solutions are from [Ramtop Retro](http://www.ramtop-retro.uk/). The Elite Compendium works out-of-the-box on the ElkSD64, ElkSD128, ElkSD-Plus1 and Plus 1 Mini; I actually developed the game on the latter, and I really like this bit of kit. All of the above products come with at least 16K of sideways RAM and an SD card interface, and the Plus 1 Mini and ElkSD128 also support digital joysticks (but not analogue joysticks). These are all highly recommended options.
- If you want all the bells and whistles, including support for both analogue joysticks and digital joysticks, then [Retro Hardware](https://www.ebay.co.uk/usr/daveejh)sells the mighty New Plus 1. This has a built-in SD card interface, and sideways RAM can be added either in cartridge form (available from the same seller), or as a single 62256 RAM chip (if you have the AP6 version of the New Plus 1). The New Plus 1 costs more than the Ramtop Plus 1 Mini, but it does more too. It's pretty great.
 
- The easiest and most cost-effective solutions are from 

You can also combine old and new hardware - for example, if you have an original Plus 1, then Ramtop Retro's ElkSD-Plus1 will provide everything you need to run the Compendium. Elite should work with most other storage and sideways RAM expansion options, as they are all pretty standard, but if you have any problems, let me know [via this Stardot thread](https://www.stardot.org.uk/forums/viewtopic.php?t=31334) and I'll investigate.

Note that while the Compendium version of Elite will run on all the Electron's filing systems, including the Plus 3, the musical version of Compendium Elite need PAGE to be set to &0E00. This means it will only work on E00 DFS, MMFS or ADFS, as it needs the extra space for the music data and driver.

Finally, the Delta 14B joystick support in the musical version of the Compendium requires not only a Delta 14B/1 adaptor box, but also a user port interface for the Electron. In theory all user port interfaces are supported, but as this is such a specialist combination of hardware, I haven't been able to test many combinations, so your mileage may vary.

## Joysticks

													 ---------

						The Compendium version of Elite supports three different types of joystick: analogue joysticks via the Plus 1, and digital joysticks via the Slogger and First Byte interfaces.

For the Slogger interface, you need to configure the address it uses to &FCD0 by setting the left switch to A and the right switch to D. If you are using a Ramtop Retro product with a joystick interface, such as the ElkSD128 or Plus 1 Mini, then it will already be configured this way.

You can switch to joysticks in-game by pausing the game with COPY, and then pressing "K" until the correct type of joystick is chosen. The current setting is shown in the top-left corner of the screen, as follows:

- +1 indicates that Plus 1 analogue joysticks are configured
- SL indicates that Slogger digital joysticks are configured
- FB indicates that First Byte digital joysticks are configured
- KB indicates that the keyboard is configured and joysticks are disabled

The musical version of the Compendium contains a further two options that support the Delta 14B/1 adaptor box for the Delta 14B joystick:

- DA indicates that the Delta 14B/1 adaptor box in user port A is configured
- DB indicates that the Delta 14B/1 adaptor box in user port B is configured

If your user port interface only has one user port, then choosing port B is probably the correct option (though there's no harm in trying both). See [playing the Elite Compendium](https://elite.bbcelite.com/hacks/elite_compendium_downloads.html) for more details about Delta 14B support.

If you are using Plus 1 analogue sticks then you can also configure joysticks by pressing the fire button on the second title screen (when it says "Press Space or Fire, Commander").

If you are using Slogger or First Byte digital joysticks, then the fire button will not be recognised the first time you see the title screen. Instead you should start the game by pressing any key when it says "Press Space or Fire, Commander", and then pause the game with COPY and select the correct joystick type as described above. If you subsequently die, or quit and return to the title screen, then you can now press fire on both title screens to keep your joystick configured; it's only the first time through the title screen that you that you have to press a key. (This is because checking for a fire button when an interface is absent can return random results, and unlike the Plus 1, there's no way of detecting whether the Slogger or First Byte interfaces are fitted, so you have to tell the game which interface you have before it can safely detect the fire button on the title screens.)

Note that some interfaces, like the ElkSD128 and Plus 1 Mini, allow you to map digital joysticks to the Plus 1 analogue port. This will enable you to use a digital joystick when Plus 1 joysticks are configured, by mapping each direction on the joystick to a full movement of the analogue joystick (i.e. to full pitch or roll). Note that this works differently to the Slogger or First Byte interfaces, which use the same joystick code as the BBC Master Compact version of Elite; with these latter options, each direction on the joystick is effectively mapped to the keyboard controls, so the longer you hold the joystick in one direction, the steeper the climb or roll becomes. The ElkSD128 and Plus 1 Mini support all three joystick options, so you can choose the one that best suits your flying style.


													 ---------------

						The Compendium version of Acorn Electron Elite has had the following releases:

- 2025-07-09 - Initial release
- 2025-07-20 - Fixed an issue with file deletion in ADFS on the Acorn Electron
- 2025-08-09 - Remove the docking fee, as my implementation turned out to be different to the original NES feature
- 2025-08-19 - Released the Compendium for the Acorn Electron with 16K sideways RAM, including a new musical version
- 2025-09-18 - Fixed a bug where the docking computer would dither about in deep space for ages before eventually deciding to make its approach
- 2025-09-29 - Fixed a bug that prevented scooping from working with non-canister items
- 2025-10-31 - Added support for the Delta 14B joystick with Delta 14B/1 adaptor box

You can check the release for a given disc image by loading the disc and typing *TYPE README to display the credits. The build date is at the end.


													 ------------

						In version 2.00 of the ACP DFS, the disc catalogue gets a bit scrambled (it works but is pretty hard to read). Upgrading to version 2.20 fixes this.

---
*Fonte originale: [https://elite.bbcelite.com/hacks/elite_compendium_acorn_electron_downloads.html](https://elite.bbcelite.com/hacks/elite_compendium_acorn_electron_downloads.html)*

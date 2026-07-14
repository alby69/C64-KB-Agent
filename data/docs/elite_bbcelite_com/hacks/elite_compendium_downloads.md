---
title: Playing the Elite Compendium
source_url: https://elite.bbcelite.com/hacks/elite_compendium_downloads.html
category: tool
topics:
- basic
- assembly
- input handling
difficulty: beginner
language: mixed
hardware:
- CPU
- SID
- KERNAL
- CIA
related:
- keyboard-handling
- music-player
- sound-programming
- joystick-reading
- memory-map
- kernal-routines
- sid-registers
- cia-registers
scraped_at: '2026-07-14'
---

# Playing the Elite Compendium

## How to download and play the Elite Compendium

![A Transporter leaving the space station on the BBC Master in the Elite Compendium](https://elite.bbcelite.com/images/elite_compendium/transporter.png) 

						You can play the Elite Compendium in a web browser, in an emulator, or on a real BBC Master 128, BBC Micro B/B+ or Acorn Electron (for the BBC Micro and Electron you'll need 16K of sideways RAM). Here are the options:

| Version | Play online | Download disc image | 
|---|---|---|
| BBC Master 128 | [Play online](https://bbc.xania.org/?model=Master&autoboot&disc=https://elite.bbcelite.com/versions/elite_compendium/elite-compendium-bbc-master.dsd)[Play online (6502SP)](https://bbc.xania.org/?model=Master&coProcessor=true&autoboot&disc=https://elite.bbcelite.com/versions/elite_compendium/elite-compendium-bbc-master.dsd) | [DSD disc image](https://elite.bbcelite.com/versions/elite_compendium/elite-compendium-bbc-master.dsd)[SSD image drive 0](https://elite.bbcelite.com/versions/elite_compendium/elite-compendium-bbc-master-drive-0.ssd)[SSD image drive 2](https://elite.bbcelite.com/versions/elite_compendium/elite-compendium-bbc-master-drive-2.ssd) | 
| BBC Micro B/B+ | [Play online](https://bbc.xania.org/?autoboot&disc=https://elite.bbcelite.com/versions/elite_compendium/elite-compendium-bbc-micro.dsd)[Play online (6502SP)](https://bbc.xania.org/?coProcessor=true&autoboot&disc=https://elite.bbcelite.com/versions/elite_compendium/elite-compendium-bbc-micro.dsd) | [DSD disc image](https://elite.bbcelite.com/versions/elite_compendium/elite-compendium-bbc-micro.dsd)[SSD image drive 0](https://elite.bbcelite.com/versions/elite_compendium/elite-compendium-bbc-micro-drive-0.ssd)[SSD image drive 2](https://elite.bbcelite.com/versions/elite_compendium/elite-compendium-bbc-micro-drive-2.ssd) | 
| Acorn Electron | [Play online](https://0xc0de6502.github.io/electroniq/?dfs&autoboot&ram6&disk0=https://elite.bbcelite.com/versions/elite_compendium/elite-compendium-acorn-electron.dsd) | [ADF disc image](https://elite.bbcelite.com/versions/elite_compendium/elite-compendium-acorn-electron.adf)[DSD disc image](https://elite.bbcelite.com/versions/elite_compendium/elite-compendium-acorn-electron.dsd)[SSD image drive 0](https://elite.bbcelite.com/versions/elite_compendium/elite-compendium-acorn-electron-drive-0.ssd)[SSD image drive 2](https://elite.bbcelite.com/versions/elite_compendium/elite-compendium-acorn-electron-drive-2.ssd) | 
| BBC Micro B+ Addendum | - | [SSD disc image](https://elite.bbcelite.com/versions/elite_compendium/elite-compendium-bbc-micro-b-plus.ssd) | 

Here's how to choose the best option:

- If you want to play the Compendium right here in your browser, simply choose the relevant "Play online" link.
- If you want to play the Compendium version of 6502 Second Processor Elite, or the Elite Universe Editor on the BBC Micro, then choose the relevant "Play online (6502SP)" link.
- If you want to run the Compendium in an emulator or on a real machine using a Gotek, then you probably want the DSD (double-sided disc) image.
- If you want to run the Compendium on a real machine using an SD card solution, then you probably want the two SSD (single-sided disc) images, as most SD cards don't support DSD images.
- If you want to run the Compendium Addendum for the BBC Micro B+, then your only option is to download the SSD (single-sided disc) image, as no online emulators support the B+.
- If you want to run the Compendium on a real Electron with a Plus 3, then the ADF disc image is probably the best choice.

Once you've chosen your option, you'll want to load the Compendium, so let's look at that next.

## Loading the Compendium disc

													 ---------------------------

						If you're playing in a browser, just click the relevant link above and the Elite Compendium will automatically load and show you the menu with all the available options. You can either read more information by highlighting an option and pressing the left or right arrow, and you can choose which option to run by pressing RETURN.

Commander files for the game are on drive 0, while universe files for the Universe Editor are on drive 2.

If you want to use a disc image, then:

- If you're playing the BBC version in an emulator or on a real machine using a device like a Gotek, insert the DSD disc image into drive 0 and press SHIFT-D-BREAK (or SHIFT-D-F12 on most emulators).
- If you're using an SD card system like the Turbo MMC or Micro SPI on the BBC or the ElkSD128 on the Electron, first add the two SSD images to your SD card, and then use the *DIN command to insert the images into drive 0 and drive 2. You can then load the Compendium by booting from drive 0, using either SHIFT-M-BREAK (for MMFS), SHIFT-S-BREAK (for Micro SPI) or the *DBOOT command. For example, if you add the two SSD images to slots 256 and 257 on the SD card, with the drive 0 image in slot 256 and the drive 2 image in slot 257, then you can run the Compendium like this:
 *DIN 2 257
 *DBOOT 256
 The first command inserts the image in slot 257 into drive 2, and the second command inserts the image in slot 256 into drive 0 and boots the disc. The disc titles include the drive number and platform type, so CompendiumB0 is drive 0 for the BBC Micro, while CompendiumE2 is drive 2 for the Electron.
- To load the Electron ADFS version, just insert the ADF image and use SHIFT-A-BREAK.

If you're playing in an emulator or on real hardware, then here are the hardware requirements:

- For the BBC Master version, all options work on a standard BBC Master 128 except for 6502 Second Processor Elite, which needs a BBC Master Turbo (i.e. a BBC Master 128 with an internal 65C102 Second Processor) or a BBC Master 128 with an external 6502 Second Processor.
- For the BBC Micro version, all options work on a BBC Micro with 16K of sideways RAM except for 6502 Second Processor Elite (which needs sideways RAM and a 6502 Second Processor) and the Elite Universe Editor (which needs a 6502 Second Processor). Note that not all BBC Micro sideways RAM solutions are supported (see the section below for more details).
- For the Acorn Electron version, the Compendium version of Acorn Electron Elite needs 16K of sideways RAM, and the musical version needs sideways RAM and an E00 DFS, MMFS or ADFS. The flicker-free cassette version works on a standard, unexpanded Electron. See [playing the Compendium version of Acorn Electron Elite](https://elite.bbcelite.com/elite_compendium_acorn_electron_downloads.html)for details of the various sideways RAM options for the Electron.

When playing the Compendium versions of Teletext Elite, BBC Micro Elite or Acorn Electron Elite, ensure that the disc is inserted when launching or docking, so the game can load the correct files (just like the original BBC Micro disc version).

## Using a Delta 14B joystick

													 --------------------------

						The Voltmace Delta 14B joystick and Delta 14B/1 adaptor box are supported in all versions of Elite in the BBC Micro and BBC Master Compendiums, as well as in the musical version of Electron Compendium Elite.

![The Voltmace Delta 14B joystick and 14B/1 adaptor box](https://elite.bbcelite.com/images/elite_compendium/delta_14b_and_adaptor.jpg) 

						The Compendium lets you use the buttons on the Delta 14B for the most important flight controls, so you don't have to keep reaching for the keyboard. You use the joystick part for flying and moving the chart crosshairs, and you use the buttons for the following:

![Delta 14B buttons in the Elite Compendium](https://elite.bbcelite.com/images/elite_compendium/delta_14b_buttons.png) 

						You can download [a PDF of these instructions](https://elite.bbcelite.com/pdfs/Elite-Compendium-Delta-14B-controls.pdf) for easy reference, or here they are in text form:

Fire laser Fire laser Slow down Fire laser Speed up Unarm missile Fire missile Target missile Front view E.C.M. Rear view Docking computer off In-system jump Docking computer on

To get all this working, you will need both a Delta 14B joystick and a Delta 14B/1 adaptor box, as well as a real BBC Micro, BBC Master or Acorn Electron, as no emulators currently support the Delta 14B system. If you don't already have these, then the joysticks pop up on eBay reasonably regularly, but the adaptor box can be really hard to find. Luckily you can buy modern reproductions of the 14B/1 from Stardot legend ukwebb; see [this Stardot thread](https://stardot.org.uk/forums/viewtopic.php?t=24981) for details. I have one of his adaptor boxes (it's in the picture above), and I can highly recommend it.

For the Electron, you will also need a Plus 1 and a user port interface. In theory any user port interface should work, and for options that provide two user ports, you can use either port A or port B.

To set everything up for Elite, first make sure your computer is switched off, and then connect the 14B/1 adaptor box to the analogue port and plug the ribbon cable into the user port. Next, attach your Delta 14B joystick to the rear socket; don't attach it to the side socket, as that isn't supported.

- For the BBC Micro and BBC Master, you can now load any version of Elite from the Compendium and start the game. While you are still docked, configure the game to use the Delta 14B by pausing the game with COPY, pressing "L" (which will give a confirmation beep), and then pressing DELETE to unpause the game.
 To switch back to the keyboard, repeat the COPY-L-DELETE process. You can still use the keyboard controls while using the Delta 14B, with the exception of the steering, which has to be done with the stick.
- For the Electron, load the musical version of the Compendium and start the game. You can configure the game to use the Delta 14B by pausing the game with COPY and pressing "K" until "DA" or "DB" are shown ("DA" is for when your adaptor box is plugged into port A, and "DB" is for when your adaptor box is plugged into port B; if you only have one port then "BD" is probably the right option). Then press DELETE to unpause the game, and you should be able to use the buttons on your joystick

You can now enjoy the future of gaming, 1984-style.

Note that because the Elite Compendium supports instant docking when you have a docking computer fitted, so does the Delta 14B. To dock instantly, simply press the bottom-right button to enable the docking computer, and then press the middle-bottom button to skip the docking sequence and dock. This is about as convenient as docking gets...

## Notes on sideways RAM

													 ---------------------

						When loading Elite, the Compendium will check for the presence of sideways RAM, and if successful it will load a ROM image into sideways RAM and ask you to press a key to play the game. If the game can't find any sideways RAM, then it will tell you and give up. Note that your sideways RAM must be writeable, so if you are on a BBC Micro and have a read/write switch fitted, make sure it's in the write-enable position.

Note that on the BBC Micro, the game will only work with sideways RAM that uses the ROMSEL latch at SHEILA &FE30 to switch banks. The BBC Master's sideways RAM is fine, but some types of BBC Micro sideways RAM use the RAMSEL latch at SHEILA &FE32, while others use the user port at SHEILA &FE60 and &FE62, and I'm afraid there just isn't enough free memory in Elite to support all these different styles of sideways RAM. In particular, owners of Solidisk or Watford Electronics sideways RAM may be out of luck here.

The Acorn Electron should be fine, as all the sideways RAM systems work in the same way.  See [playing the Compendium version of Acorn Electron Elite](https://elite.bbcelite.com/elite_compendium_acorn_electron_downloads.html) for details of the various sideways RAM options for the Electron.


													 ---------------

						The Elite Compendium has had the following releases:

- 2024-01-11 - Initial release
- 2024-01-12 - Fixed the Data on System bug in the 6502 Second Processor version
- 2024-05-04 - Fixed an issue with corrupted ship rotation on the BBC Master version
- 2024-05-15 - Fixed the Moray bug from the original BBC Master and 6502 Second Processor versions, and fixed an issue with Thargoids corrupting the screen in the BBC Master version
- 2024-05-17 - Fixed an issue with Thargoids corrupting the screen in the 6502 Second Processor version
- 2024-06-30 - Added the joystick fire button fix to the BBC Micro, Teletext and 6502 Second Processor versions, and fixed the volume controls in the 6502 Second Processor version
- 2024-06-30 - Released the Compendium for the BBC Micro with 16K sideways RAM
- 2024-07-01 - Updated BBC Micro version to work with IntegraB board
- 2024-07-08 - Added all Compendium-specific features to the BBC Micro disc, Teletext and 6502 Second Processor versions
- 2024-07-10 - Added all applicable Compendium-specific features to the BBC Micro cassette version
- 2024-07-12 - Applied the volume setting to explosions in all the BBC Micro versions, as they weren't being muted
- 2024-08-27 - Fixed a minor issue with the BOXART2 universe file that would make it take up more memory than required
- 2024-11-02 - Added Delta 14B support to all versions of Elite
- 2025-05-06 - Removed encryption from the 6502 Second Processor version to improve compatibility with different sideways RAM boards
- 2025-07-10 - Revert the change that prevented the docking computer from killing you, so those who like it can enjoy a hint of danger (and those who don't can just insta-dock)
- 2025-08-09 - Remove the docking fee, as my implementation turned out to be different to the original NES feature
- 2025-08-19 - Released the Compendium for the Acorn Electron with 16K sideways RAM
- 2025-08-31 - Released the Compendium Addendum for the BBC Micro B+ and improved the help text in all the Compendium menus
- 2025-09-14 - Updated the Compendium disc titles to include a platform identifier (i.e. B/B+/M/E) and, for SSDs, a drive number (i.e. 0/2)
- 2025-09-18 - Fixed a bug in the Acorn Electron version where the docking computer would dither about in deep space for ages before eventually deciding to make its approach
- 2025-09-18 - Fixed the catalogue and delete options in the BBC Micro B+ Compendium disc menu, which weren't working on real hardware
- 2025-09-29 - Fixed a bug in the Acorn Electron version that prevented scooping from working with non-canister items
- 2025-10-31 - Added support for the Delta 14B joystick with Delta 14B/1 adaptor box to the Acorn Electron musical version
- 2026-01-12 - Added co-processor checks to the BBC Micro B+ Compendium loader
- 2026-01-15 - Updated the music loader to my own version that skips sideways RAM banks that already contain ROM images
- 2026-04-03 - Updated BBC Master version to fix a bug in the original where joysticks weren't being disabled during automated docking

You can check the release for a given disc image by loading the disc and typing *TYPE README to display the credits. The build date is at the end.


													 ------------

						On the BBC Master, the buttons on the Delta 14B can sometimes be a little flaky (though the BBC Micro is fine). Specifically, if you press the "go faster" button in the top-right, it can sometimes trigger the "target missile" button just below it. I've also seen it trigger the "rear view" button below that, but this is rarer. This is more of an annoyance than a problem, but it's worth knowing about.

On the Acorn Electron, the disc catalogue gets a bit scrambled in version 2.00 of the ACP DFS (it works but is pretty hard to read). Upgrading to version 2.20 fixes this.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
Fire laser                                    Fire laser
  Slow down              Fire laser             Speed up
  Unarm missile          Fire missile           Target missile
  Front view             E.C.M.                 Rear view
  Docking computer off   In-system jump         Docking computer on
```



---
*Fonte originale: [https://elite.bbcelite.com/hacks/elite_compendium_downloads.html](https://elite.bbcelite.com/hacks/elite_compendium_downloads.html)*

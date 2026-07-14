---
title: Playing Elite 3D
source_url: https://elite.bbcelite.com/hacks/elite_3d_downloads.html
category: manual
topics:
- basic
- assembly
difficulty: intermediate
language: mixed
hardware:
- CPU
- KERNAL
related:
- memory-map
- kernal-routines
scraped_at: '2026-07-14'
---

# Playing Elite 3D

## How to download and play Elite 3D

![The iconic Elite box screenshot in anaglyph 3D](https://elite.bbcelite.com/images/elite_3d/boxart2.png) 

						You can play Elite 3D in a web browser, or on a BBC Master or BBC Micro that's got a 6502 Second Processor fitted. You will also need a pair of anaglyph 3D glasses (see below). Here are your options:

- Play Elite 3D [in your browser](https://bbc.xania.org/?model=Master&coProcessor=true&autoboot&disc=https://elite.bbcelite.com/versions/elite_3d/elite-6502sp-3d-sng45.ssd).
- Download Elite 3D [as a disc image](https://elite.bbcelite.com/versions/elite_3d/elite-6502sp-3d-sng45.ssd). This will run in an emulator, or on a real BBC Master or BBC Micro using a device like a Gotek.

To load Elite 3D, insert the disc image and press SHIFT-D-BREAK (for DFS), SHIFT-M-BREAK (for MMFS), SHIFT-S-BREAK (for Micro SPI) or use the *DBOOT command (for all SD card solutions); emulators tend to map BREAK to F12, so press SHIFT-D-F12. The disc will automatically load if you're playing it in a browser.

Elite 3D will run on all the various 6502 Second Processors, but faster is better. The BBC Micro's 3MHz 65C02 co-processor will cope fine, but the Master's 4MHz internal 65C102 co-processor is a better choice, and if you have a PiTubeDirect then you might like to try the fast 65C02 or 65C102 co-processors. The game is frame-limited, so will be playable even on the fastest machines (unlike the original version).

If you want to start with a fully kitted-out ship and lots of cash, then you can load the maxed-out commander file that's included in the disc image. To do this, press "Y" on the title screen to bring up the menu, press "1" to choose the load option, enter "MAX" (without the quotes) as the commander name, and press "0" for the drive number.

## Anaglyph 3D glasses

													 -------------------

						If you want to have the best experience in anaglyph 3D, then you need a decent pair of 3D glasses. It's pretty difficult to find really good glasses that will work with retro hardware, but here's what you need to know.

Anaglyph 3D glasses consist of coloured lenses, typically red for the left eye and cyan for the right eye (although Elite 3D supports five different colour schemes - see the page on [configuring Elite 3D](https://elite.bbcelite.com/elite_3d_configuration.html) for details). They can be cheap cardboard specs, fancy plastic wraparounds, or even clip-on lenses for those of us who already need glasses to read our computer screens:

![Various pairs of 3D anaglyph glasses](https://elite.bbcelite.com/images/elite_3d/3d_specs.jpg) 

						The idea is that the lens colours match the on-screen colours as closely as possible, so the red lens only lets red and white light through and blocks cyan light, while the cyan lens only lets cyan and white light through and blocks red light. In this way each eye only sees one on-screen colour, and this produces a stereoscopic effect.

The problem is that lens colours are hard to control, and so are on-screen colours, so getting them to match is a bit of a hit-and-miss affair. I have a number of different pairs of 3D specs, and in some of them the cyan filter is really light and you can easily see the red lines through it, while in others it's a lot darker and blocks the opposite colour more effectively. Sometimes the cyan is actually blue, as in the clip-on pair in the above photo; it's a bit of a minefield, really.

With the cheaper cardboard glasses, I've found that stacking multiple pairs of specs can help, but it's all a bit Heath Robinson. Also, some players find that even for red-cyan glasses, it can help to play with the palette, with a popular setting being the third option (left eye = red, right eye = green, both eyes = yellow). That's the authentic 1980s anaglyph experience for you - it never was that reliable, even back in the day, and hacking the glasses is all part of the fun.

To help you optimise your system to work with your individual glasses and screen setup, see the section on [configuring Elite 3D](https://elite.bbcelite.com/elite_3d_configuration.html).

## Playing Elite in 3D

													 -------------------

						In Elite 3D, the whole game has been converted to work while wearing anaglyph 3D glasses. In practice you may want to doff your specs when you don't need them, as the effect can be a bit wearing, but if you're happy in your 1980s 3D paradise, then you can stay there for the duration.

The in-station screens have been designed to work with or without 3D glasses. The text and system charts appear in both eyes, so although they glimmer a bit, they should work. The dashboard is similar, and should appear reasonably clear, even through anaglyph glasses.

The space view shows all the ships, stations, suns, planets and stardust in anaglyph 3D, so you'll definitely want to wear your glasses for flying:

![The first screenshot from the manual in Elite 3D](https://elite.bbcelite.com/images/elite_3d/manual.png) 

						Here's what you need to know about playing Elite in anaglyph 3D:

- The dashboard and laser sights are shown in both eyes (i.e. white in the default red/cyan scheme), so they sit on what's known as the "projection plane", which is where your eyes naturally focus. 3D objects like ships and planets tend to be either in front of or behind this plane. I find that staring at the laser sights and relaxing my eyes can help the 3D effect kick in; also, narrowing your eyes can help the third dimension "pop" into view.
- The view name ("Front view", "Back view" etc.) only appears briefly on-screen when you change to a new view, as otherwise it is pretty distracting. I have also removed the white box surrounding the space view to make it easier to see the 3D effect.
- As the dashboard is now monochrome, I have enabled flashing dashboard colours by default (so indicators flash black and white when too high or too low). I have disabled flashing for the speed indicator, as it's just annoying for it to flash all the time at full speed.
- The escape pod is now shown in the equipment section of the Status Mode screen, as the dashboard no longer changes colour to indicate this. The large cargo bay is now shown in the Inventory instead of the Status Mode screen. This is the same as the Acorn Electron version of Elite.
- Missiles are shown with a central dot when seeking (i.e. when they are yellow in the normal game) or a central line when they have a target lock (i.e. when they are red in the normal game).
- I have limited the frame rate to make the game playable, as the 6502 Second Processor version is otherwise too fast to play. This means that faster co-processors (such as the super-fast PiTubeDirect) can reduce judder pretty well while still ensuring the game doesn't get too fast.

Apart from the above, this is the standard and full version of 6502 Second Processor Elite, and all features are present. This includes the scroll text demo, which you can start from the title screen by pressing TAB. And it's all in 3D, just as you would expect.

If you want to configure the anaglyph 3D effect to get the best from your particular setup, see the section on [configuring Elite 3D](https://elite.bbcelite.com/elite_3d_configuration.html). For more details of how the anaglyph effect is implemented in Elite 3D, see the [technical information](https://elite.bbcelite.com/elite_3d_technical_information.html).


													 ---------------

						Elite 3D has had the following releases:

- 2024-09-24 - Initial release
- 2024-09-25 - Fixed an issue where the size of the sun could randomly change and reduced the size of the sun's separation to make it easier on the eyes

You can check the release for a given disc image by loading the disc and typing *TYPE README to display the credits. The build date is at the end.


													 ------------

						When the planet is clipped by the top-right corner of the screen, it can sometimes make the top line of the screen flicker. This is actually a bug that affects all released versions of BBC Micro Elite, but you don't normally notice the problem because it is hidden by the box around the space view; it just makes the top line of the box flicker every now and then, and only when the planet is clipped by the top-right corner. However, because Elite 3D no longer has a box surrounding the space view, the flickering top line is much more obvious. It is part of the original code, though, and not a bug with Elite 3D.

If you load a universe file that contains a sun, then changing the parallax level with "D" will corrupt the fringes slightly. You can fix this by reloading the file.

---
*Fonte originale: [https://elite.bbcelite.com/hacks/elite_3d_downloads.html](https://elite.bbcelite.com/hacks/elite_3d_downloads.html)*

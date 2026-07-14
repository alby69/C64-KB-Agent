---
title: Technical information for flicker-free Elite
source_url: https://elite.bbcelite.com/hacks/flicker-free_elite_technical_information.html
category: source-code
topics:
- memory management
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

# Technical information for flicker-free Elite

## Details of how flicker-free Elite weaves its magic

There are two flicker-free flavours of Elite on this site: flicker-free ships and flicker free planets. Let's take a look at how they work.

## Flicker-free ships

													 ------------------

						The improved ship-drawing algorithm in flicker-free Elite originally appeared in the 1986 Apple II and BBC Master versions of Elite. This is the algorithm that I backported to the original 1984 BBC Micro and Acorn Electron versions of Elite, as well as the 1985 versions for the 6502 Second Processor and Commodore 64, and the unofficial version for the Commodore Plus/4.

For more information on the flicker-free algorithm and the backporting process, see the following deep dives:

- The [flicker-free ship drawing](https://elite.bbcelite.com/deep_dives/flicker-free_ship_drawing.html)deep dive looks at the newer algorithm and how it differs from the earlier, more flickery version in the original game.
- The deep dive on [backporting the flicker-free algorithm](https://elite.bbcelite.com/deep_dives/backporting_the_flicker-free_algorithm.html)looks at exactly what was involved in taking the improved algorithm from the BBC Master and squeezing it into the original versions of Elite.

See the [introduction](https://elite.bbcelite.com/flicker-free_elite.html) to see how the two algorithms compare, side-by-side.

## Flicker-free planets

													 --------------------

						In the original Apple II and BBC Master versions, planets still flicker, as they are displayed by a completely different part of the code. When the authors fixed the flicker, they only did so in the ship-drawing routines.

To get rid of this final bit of flicker, I have applied the same algorithm to the planet-drawing routines, so planets are also erased and redrawn one line at a time. Players of the BBC Micro disc version, BBC Master, 6502 Second Processor, Acorn Electron, Commodore 64, Commodore Plus/4 and Apple II can now enjoy both flicker-free ships *and* planets; unfortunately there isn't enough spare memory in all versions of Elite for this modification, so flicker-free planets are not supported on the BBC Micro cassette version or in Elite-A, where memory is really tight. See the page on [playing flicker-free Elite](https://elite.bbcelite.com/flicker-free_elite_downloads.html) for details of all the different versions.

The bulk of the flicker-free planet change is implemented in the DrawPlanetLine routine, which is injected into the BLINE routine to implement the same single erase/redraw algorithm as in the ship-drawing improvement (the BLINE routine manages the ball line heap for circles and ellipses). Because planet circles, craters, equators and meridians are all managed by the same heap, this fix reduces flicker for the entire planet, not just the circular outline.

Adding the algorithm to the ball line code does indeed reduce flicker, but it doesn't get rid of it entirely, because unlike ships, planets are quite often static, hanging in the sky as we fly towards them. This means that lines often get erased and redrawn in exactly the same place, which still leads to a small hint of flicker; the same issue affects ships, but because they are always moving, it is far less obvious.

To get around this, there is a further addition to the code in the form of the DrawNewPlanetLine routine, which checks whether or not a line has moved, and only erases and redraws the line if it is in a different place. If the line hasn't moved, then the erase/redraw process is skipped, so lines that don't move on-screen do not flicker. Due to memory constraints, this extra routine isn't present in the BBC Micro disc version, so planets do still have a slight shimmer in that version, though the flicker is still considerably improved over the original.

Here's the flicker-free BBC Master version, showing a rock-steady planet:

There is still a very tiny amount of flicker, which kicks in when the number of lines in the line heap changes. In this case we may erase a line in one place and redraw it in a different place, which does produce a tiny glimmer, but overall the extended algorithm does a pretty good job of fixing planet flicker. This effect is particularly noticeable when the planet is partially off-screen, and although the BBC Micro is quick enough to turn this into a slight glimmer, it is a bit more noticeable on the Commodore 64, Plus/4 and Apple II. But it's still a huge improvement over the original, flickery release, even if the flicker-free version isn't strictly free of flicker.

There is also the overlap effect that comes from drawing lines on top of each other, such as when the meridian or equator reaches the planet's edge; this is a consequence of the EOR-plotting approach used by Elite, rather than the erase/redraw flicker that this modification fixes, so it's still present.

To see the code behind this, you can search the [elite-source.asm](https://github.com/markmoxon/elite-source-code-bbc-master/blob/flicker-free/1-source-files/main-sources/elite-source.asm) source file in the [flicker-free branch of the elite-source-code-bbc-master repository](https://github.com/markmoxon/elite-source-code-bbc-master/tree/flicker-free). Look for "Mod:" to see the modifications for flicker-free planet drawing. You can also see the exact same modifications in the [elite-source.asm](https://github.com/markmoxon/elite-source-code-apple-ii/blob/flicker-free/1-source-files/main-sources/elite-source.asm) source file in the [flicker-free branch of the elite-source-code-apple-ii repository](https://github.com/markmoxon/elite-source-code-apple-ii/tree/flicker-free)

If you want to see the modifications in the original BBC Micro Elite, which doesn't include the extra DrawNewPlanetLine routine, then you can search the [elite-source-flight.asm](https://github.com/markmoxon/elite-source-code-bbc-micro-disc/blob/flicker-free/1-source-files/main-sources/elite-source-flight.asm) source file in the [flicker-free branch of the elite-source-code-bbc-micro-disc repository](https://github.com/markmoxon/elite-source-code-bbc-micro-disc/tree/flicker-free). Look for "Mod:" to see the modifications for both flicker-free ship and planet drawing.

Finally, for details of how the flicker-free improvements have been added to the Commodore 64 and Plus/4, you have two options. If you want to explore the code modifications, then search the [elite-source.asm](https://github.com/markmoxon/elite-source-code-commodore-64/blob/flicker-free/1-source-files/main-sources/elite-source.asm) file in the [flicker-free branch of the elite-source-code-commodore-64 repository](https://github.com/markmoxon/elite-source-code-commodore-64/tree/flicker-free). As with the other repositories, look for "Mod:" to see the modifications for both flicker-free ship and planet drawing.

Another option is the the [flicker-free Commodore 64 Elite repository](https://github.com/markmoxon/c64-elite-flicker-free), which contains the same flicker-free code, but instead of having the modifications integrated into the original source code and the whole game being rebuilt, this repository patches the changes into the game binary. The end result is exactly the same, but the first repository is much easier to follow if you want to explore the modifications, while this second one is an interesting journey into patching. (The patching approach came first, before the Commodore 64 source code was released, which is why there are two repositories.)

## Finding space on the Electron

													 -----------------------------

						Astonishingly, there is enough spare room in the Acorn Electron for the full version of flicker-free planets. Although the game binary uses up almost every single byte of space, leaving only 13 bytes of unused space, it turns out that not all of the game code is actually used, and when those parts are removed, there is not only enough space for flicker-free planets, but for some other improvements as well.

The Electron version still contains the same unused multiplication routines as the BBC Micro (a [duplicate of MULTU](https://elite.bbcelite.com/electron/main/subroutine/unused_duplicate_of_multu.html) and the unused [MUT3](https://elite.bbcelite.com/electron/main/subroutine/mut3.html) routine), so there are 28 unused bytes there that can be reused... and on top of that, the authors left the [ARCTAN](https://elite.bbcelite.com/electron/main/subroutine/arctan.html) routine (70 bytes) and [ACT](https://elite.bbcelite.com/electron/main/variable/act.html) table (32 bytes) intact, even though they are only ever used to draw meridians and equators on planets, a feature that isn't present in the Electron version. There are 11 unused bytes in [part 2 of the main flight loop](https://elite.bbcelite.com/electron/main/subroutine/main_flight_loop_part_2_of_16.html) that are skipped using a JMP (so presumably this was code that was inserted at some point, and then deemed unnecessary, so it was just skipped), and there is a chunk of 39 bytes in the [TT17](https://elite.bbcelite.com/electron/main/subroutine/tt17.html) routine that enable you to move the crosshairs with a joystick, but as the Electron version doesn't support joysticks, this can also be removed (and in doing so, this fixes a bug in the original where you can still select joystick control, and in doing so break the crosshairs on the charts).

Another way of saving a few precious bytes is to move variables from main memory into zero page, as instructions that access zero page are one byte smaller than their equivalents that access main memory. There are two zero-page locations just after [YY](https://elite.bbcelite.com/electron/main/workspace/zp.html#yy) in Electron Elite that are no longer used - they are used to store the sun's centre axis coordinates in BBC Micro Elite, and the Electron version doesn't have suns - so we can move two variables from main memory into zero page. The best candidates are QQ29, which is used 29 times in the codebase, and QQ3, which is used 10 times, so moving these from the [WP workspace](https://elite.bbcelite.com/electron/main/workspace/wp.html) into zero page frees up a total of 41 bytes in main memory (29 plus 10, plus one byte each for the variable).

Finally, there are some instructions that set the HFX variable in the [LL164](https://elite.bbcelite.com/electron/main/subroutine/ll164.html) routine, which can be removed as HFX isn't used anywhere; in the BBC Micro is it used to switch off the split-screen mode for the hyperspace effect, but there is no split-screen mode in the Electron, so that's another one that can be used. Indeed, there are various other optimisations that could free up a few more bytes, but there aren't any other minor BBC Micro features to port to the Electron; Thargoids, suns, meridians and craters all take up large amounts of code, so they will have to stay as BBC Micro-only features.

Altogether these tweaks free up enough memory to add the following features to Electron Elite:

- Flicker-free ships
- Flicker-free planets
- The escape capsule animation from the BBC Micro has been added, which is not present in the original Electron version
- There are now three sizes of stardust (like the BBC Micro) rather than two, with the addition of one-pixel stardust
- Planets are more high-fidelity, so the planet's circle looks more like the BBC Micro, and less like a 50p; this does slow things down a little, but overall the faster algorithm for flicker-free planets compensates for this
- For the SSD disc version, the black box that shows loading progress has been removed from the Acornsoft loading screen (it is still used to show loading progress in the UEF cassette version)

So the Electron version might not have Thargoids, suns or detailed planets, but it now has one feature that the standard BBC Micro version does not have room for: flicker-free planets. Head over to the [downloads page](https://elite.bbcelite.com/flicker-free_elite_downloads.html) to get hold of the improved version.

To see the code behind this, you can search the [elite-source.asm](https://github.com/markmoxon/elite-source-code-acorn-electron/blob/flicker-free/1-source-files/main-sources/elite-source.asm) source file in the [flicker-free branch of the elite-source-code-acorn-electron repository](https://github.com/markmoxon/elite-source-code-acorn-electron/tree/flicker-free). Look for "Mod:" to see the modifications for all the in-game features listed above.

---
*Fonte originale: [https://elite.bbcelite.com/hacks/flicker-free_elite_technical_information.html](https://elite.bbcelite.com/hacks/flicker-free_elite_technical_information.html)*

---
title: Technical information for Teletext Elite
source_url: https://elite.bbcelite.com/hacks/teletext_elite_technical_information.html
category: source-code
topics:
- raster interrupts
- assembly
- graphics
- basic
difficulty: advanced
language: mixed
hardware:
- KERNAL
related:
- vic-ii-registers
- memory-map
- kernal-routines
- sprite-programming
- raster-interrupts
scraped_at: '2026-07-20'
---

# Technical information for Teletext Elite

## Details of how Elite was converted to use teletext

![Teletext Elite rear space view](https://elite.bbcelite.com/images/teletext_elite/station_view.png) 

						Under the hood, Teletext Elite is identical to the disc version of BBC Micro Elite, but instead of setting up a mode 4/5 split-screen mode and poking pixels into screen memory, we stay in mode 7 and poke sixels and text characters into screen memory.

To make this process easier, we can scale from the original mode 4/5 screen pixels to mode 7 sixels as follows:

- The original Elite screen mode is 256x248 pixels, with 256x192 pixels for the space view and 256x56 pixels for the dashboard (see the deep dive on [the split-screen mode](https://elite.bbcelite.com/deep_dives/the_split-screen_mode.html)for details).
- Mode 7 is 40x25 characters, with columns 0 to 39 and rows 0 to 24. Each character is three sixels high by two sixels wide, so that gives us a resolution of 80x75 sixels.
- A quick divide-by-4 converts the 256x192 pixels of the space view into 64x48 sixels (i.e. 16 mode 7 character rows of 32 characters each).
- This leaves nine mode 7 character rows, which I split between the title, message bar and dashboard. This gives seven character rows for the dashboard, which works out at exactly one character row for each of the seven controls.
- The space view is not a full screen width - it's 32 characters out of 40 - but because it is sandwiched between two full-width blue title bars, it feels a lot wider than 64 sixels.
- The space view in the original game is 192 pixels high, which equates to 24 standard character rows in mode 4, so to accommodate screens like the Status Mode screen and Market Prices screen, we have to use the whole mode 7 screen height.

Here's a summary of the mode 7 screen structure in the space view, during flight:

| Character row | Contents | 
|---|---|
| 0 | Title row showing the space view name and hyperspace countdown | 
| 1-16 | 16 rows for the space view (48 vertical sixels mapped to 192 pixels via a factor of 4) | 
| 17 | Message row showing current in-flight message | 
| 18-24 | 7 rows for the dashboard (one row per control) | 

And here's the structure of the trade screens and charts:

| Character row | Contents | 
|---|---|
| 0 | Galfax header | 
| 2 | Title row showing the current screen name | 
| 3-24 | Contents (text and graphics) | 

Next, here's a full list of routines that poke into screen memory; these are the core routines that have been modified in Teletext Elite to poke sixels and text instead of pixels. The links will take you to the source code for the original disc version, without the Teletext modifications (to see the latter, see below for information on [exploring the Teletext Elite source code](https://elite.bbcelite.com#source)).

| Routine | Purpose | 
|---|---|
| [LOIN](https://elite.bbcelite.com/disc/flight/subroutine/loin_part_1_of_7.html) | Draw a line | 
| [HLOIN](https://elite.bbcelite.com/disc/flight/subroutine/hloin.html) | Draw a horizontal line | 
| [PX3](https://elite.bbcelite.com/disc/flight/subroutine/px3.html) | Plot a single pixel at (X, Y) within a character block | 
| [PIXEL](https://elite.bbcelite.com/disc/flight/subroutine/pixel.html) | Draw a 1-pixel dot, 2-pixel dash or 4-pixel square | 
| [CHPR](https://elite.bbcelite.com/disc/docked/subroutine/chpr.html) | Print a character at the text cursor (docked) | 
| [TT26](https://elite.bbcelite.com/disc/flight/subroutine/tt26.html) | Print a character at the text cursor (flight) | 
| [CLYNS](https://elite.bbcelite.com/disc/flight/subroutine/clyns.html)/[LYN](https://elite.bbcelite.com/disc/flight/subroutine/lyn.html) | Clear the bottom three text rows of the mode 4 screen | 
| [CPIX2](https://elite.bbcelite.com/disc/flight/subroutine/cpix2.html) | Draw a single-height dash on the dashboard | 
| [DILX](https://elite.bbcelite.com/disc/flight/subroutine/dilx.html) | Update a bar-based indicator on the dashboard | 
| [DIL2](https://elite.bbcelite.com/disc/flight/subroutine/dil2.html) | Update the roll or pitch indicator on the dashboard | 
| [MSBAR](https://elite.bbcelite.com/disc/flight/subroutine/msbar.html) | Draw a specific indicator in the dashboard's missile bar | 
| [HANGER](https://elite.bbcelite.com/disc/docked/subroutine/hanger.html) | Display the ship hangar | 
| [HAS2](https://elite.bbcelite.com/disc/docked/subroutine/has2.html) | Draw a hangar background line from left to right | 
| [HAS3](https://elite.bbcelite.com/disc/docked/subroutine/has3.html) | Draw a hangar background line from right to left | 
| [SCAN](https://elite.bbcelite.com/disc/flight/subroutine/scan.html) | Display the current ship on the scanner | 
| [SHPPT](https://elite.bbcelite.com/disc/flight/subroutine/shppt.html) | Draw a distant ship as a point rather than a full wireframe | 

Finally, in addition to the above, the loader has been updated in a few important places, to disable the split-screen mode and plot sixels for the Saturn loading screen instead of pixels:

| Routine | Purpose | 
|---|---|
| [B%](https://elite.bbcelite.com/disc/loader_3/variable/b_per_cent.html) | VDU commands for setting the square mode 4 screen | 
| [IRQ1](https://elite.bbcelite.com/disc/loader_3/subroutine/irq1.html) | The main screen-mode interrupt handler | 
| [PIX](https://elite.bbcelite.com/disc/loader_3/subroutine/pix.html) | Draw a single pixel at a specific coordinate | 

You can see every single modification made in Teletext Elite in the source code (see the next section).


													 ----------------------------------------

						The source code for Teletext Elite is available for you to explore. It is fully documented and fully buildable on modern computers, and includes labelled modifications in the main game's source code so you can see exactly how I modified the original disc version of Elite to bring it into the world of sixels.

To see the source and learn how to build Teletext Elite on your own machine, visit the project's [GitHub repository](https://github.com/markmoxon/teletext-elite).

---
*Fonte originale: [https://elite.bbcelite.com/hacks/teletext_elite_technical_information.html](https://elite.bbcelite.com/hacks/teletext_elite_technical_information.html)*

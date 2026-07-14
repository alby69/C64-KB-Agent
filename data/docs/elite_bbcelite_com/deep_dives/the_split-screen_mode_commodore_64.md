---
title: The split-screen mode in Commodore 64 Elite
source_url: https://elite.bbcelite.com/deep_dives/the_split-screen_mode_commodore_64.html
category: source-code
topics:
- sprite programming
- basic
- raster interrupts
- assembly
- graphics
difficulty: beginner
language: mixed
hardware:
- VIC-II
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

# The split-screen mode in Commodore 64 Elite

## How the VIC-II makes it easy to implement the Commodore version's split screen

When the BBC Micro version of Elite came out in 1984 it was clearly a technical marvel, with more than 2000 star systems, slick wireframe graphics and open-ended gameplay. But for us fans of the BBC Micro, one of the most groundbreaking aspects was the split-screen mode, the likes of which we'd never seen before.

Here it is in all its glory, combining the high-resolution monochrome space view with the lower-resolution, four-colour dashboard:

![BBC Micro Elite screenshot](https://elite.bbcelite.com/images/general/Elite-BBCMicro.png) 

						This devilry was implemented using timers and interrupts and ULAs and CRTC controllers, and it's still an impressive achievement, even all these years later. You can read about how it's done in the deep dive on [the split-screen mode in BBC Micro Elite](https://elite.bbcelite.com/the_split-screen_mode.html).

It turns out that the Commodore 64 version of Elite also has a split-screen mode, but nobody really talks about it. The reason? It turns out it's easy to create split-screen modes using the Commodore 64's powerful VIC-II video controller chip, without needing to jump through all the hoops that the original version of Elite has to.

![Commodore 64 Elite screenshot](https://elite.bbcelite.com/images/general/Elite-Commodore64.png) 

						Let's see how the Commodore 64's split-screen mode works in Elite.

## The two different screen modes

													 ------------------------------

						The BBC Micro and Commodore 64 have a surprising amount in common when it comes to the Elite screen. For example, both versions have a monochrome space view in the upper part of the screen, and the structure of the space view in screen memory is identical between the two platforms (it's one bit per pixel, arranged in character blocks of eight rows of eight pixels). And both versions have a colour dashboard, and again the structure of screen memory is the same (this time it's two bits per pixel, arranged in character blocks of eight rows of four pixels). Pixels in the dashboard are twice as wide as pixels in the space view, to enable the colour information to jump from two possible values to four.

But there are quite a few differences, too. The Commodore 64 has a much more sophisticated palette system than the BBC Micro, so while the dashboard in the BBC supports just four colours, the Commodore 64 dashboard can make the most of the machine's 16-colour palette. Similarly, the palette for the upper part of the Commodore 64 screen can also be changed for each character block, so although the space view is kept as black and white, the box border is yellow, as it actually sits one pixel outside the space view and can take a different palette than the main view. For more details on how the Elite screen gets its colour in Commodore 64 Elite, see the deep dive on [colouring the Commodore 64 bitmap screen](https://elite.bbcelite.com/colouring_the_commodore_64_bitmap_screen.html).

On top of this, the Commodore 64 has eight hardware sprites, which are used to include coloured laser sights, with different colours and designs depending on the type of laser. In fact, if you accept the Trumbles mission, the monochrome space view gets smothered in a whole rainbow of colours:

![The Trumbles in Commodore 64 Elite](https://elite.bbcelite.com/images/c64/trumbles_on_screen.png) 

						The only downside of the Commodore 64's implementation is the reduced vertical resolution: the BBC Micro screen is 248 pixels high, while the Commodore 64 screen is just 200 pixels high. It's the space view that takes the hit, at a height of 144 pixels compared to the BBC's 192 pixels, which makes the BBC's space view about 35% taller than on the Commodore 64.

But beautiful things come in small packages, and the Commodore 64 version is certainly a looker. Let's see how this mix of colours and resolutions is achieved.

## The raster interrupt

													 --------------------

						As with the BBC Micro, the split-screen mode in the Commodore 64 version is implemented using interrupts. The idea is the same: the CRT screen on these old-school computers gets drawn by an electron beam hitting the screen, and the beam starts at the top-left of the screen and moves horizontally to the right, drawing each line pixel by pixel before moving down to the next line and drawing that one in the same way. When the beam reaches the bottom of the screen, it jumps back to the top-left corner again and repeats this process. On PAL systems this is done 50 times a second to produce a 50Hz screen, while on NTSC systems it is done 60 times a second for a 60Hz screen.

To implement a split-screen mode for our space view and dashboard, we do the following. We start drawing the screen from the top of the space view using the high-resolution monochrome screen mode, and when the beam reaches the top of the dashboard, we reprogram the hardware to change to the low-resolution multicolour screen mode. This means that the dashboard gets drawn in wider pixels with more colour, and when we reach the bottom of the screen and jump back to the top, we switch back into the monochrome screen mode to draw the space view once again.

On the BBC Micro, this is not trivial. It involves setting timers to trigger interrupts at the correct point in the screen-drawing process, which isn't particularly easy; see the deep dive on [the split-screen mode in BBC Micro Elite](https://elite.bbcelite.com/the_split-screen_mode.html) for all the gory details.

On the Commodore 64 it's a very different story. The VIC-II chip that manages the Commodore 64's graphics has a built-in interrupt that does exactly what we need. This is the "raster interrupt", and once we have set up the system to enable this kind of interrupt, we can tell the VIC-II chip to generate an interrupt on a specific raster line by simply doing the following:

LDA #line_number STA VIC+$12

That's it: that's pretty much all we need to do to generate a raster interrupt for the split screen. How we actually use this interrupt to implement the split screen is discussed in the next section.

To be fair, we do have to set things up to support the raster interrupt: specifically, we have to create an interrupt handler and point the interrupt vector at it, and we need to configure the VIC-II and CIA chips to enable the raster interrupt. We'll look at the interrupt handler in the next section, and the setup is done in [part 4 of the game loader](https://elite.bbcelite.com/c64/game_loader/subroutine/elite_loader_part_4_of_7.html) and the [COLD](https://elite.bbcelite.com/c64/main/subroutine/cold.html) routine.

Importantly, the raster line number is actually a 9-bit number, with the top bit being configured in bit 7 of VIC register $11, so we also have to make sure to clear this, as the line numbers we want to interrupt are less than 256. It's important to get all this right, but it's still nothing compared to the hoops we have to jump through on the BBC Micro...

## The interrupt routine

													 ---------------------

						The interrupt routine at [COMIRQ1](https://elite.bbcelite.com/c64/main/subroutine/comirq1.html) handles all the game's interrupt logic, including the raster interrupt. This routine is also responsible for setting the next raster interrupt, so when it gets called at the top of the screen, it sets up another raster interrupt for the top of the dashboard, and when it gets called at the top of the dashboard, it sets another raster interrupt for the top of the screen. As a result COMIRQ1 gets called twice every screen refresh, and on each call it flips the [RASTCT](https://elite.bbcelite.com/c64/main/variable/rastct.html) variable between 0 and 1, to record which part of the screen is now being drawn. This flip happens after it tells the VIC-II chip to change the screen mode, so on entry into the routine, a 0 in RASTCT indicates that we are about to draw the space view, while a 1 in RASTCT means we are about to draw the dashboard.

The value of RASTCT is used as an index into a number of two-byte variables that are used to implement all sorts of screen effects, from the split screen to the energy bomb. These variable names are worth the entry price alone; the Elite source code is known for having some intriguing labels, and it feels as if whoever wrote this part of the code was going through a psychedelic jazz- and folk-inspired period, perhaps in homage to all the happy colours of the Commodore 64 palette. Here they are in all their glory:

- [zebop](https://elite.bbcelite.com/c64/main/variable/zebop.html)and- [abraxas](https://elite.bbcelite.com/c64/main/variable/abraxas.html)control the screen RAM addresses for the upper and lower parts of the screen. See the deep dive on- [colouring the Commodore 64 bitmap screen](https://elite.bbcelite.com/colouring_the_commodore_64_bitmap_screen.html)for more about screen RAM.
- [innersec](https://elite.bbcelite.com/c64/main/variable/innersec.html)determines the two values of RASTCT, which are hard-coded to 0 and 1. Presumably these values are in a variable to enable an extended number of screen splits, though the game only implements two.
- [shango](https://elite.bbcelite.com/c64/main/variable/shango.html)contains the raster line numbers for changing between the upper and lower parts of the screen. They are hard-coded to 51 for the top of the space view and 51 + 143 for the top of the dashboard.
- [moonflower](https://elite.bbcelite.com/c64/main/variable/moonflower.html)and- [caravanserai](https://elite.bbcelite.com/c64/main/variable/caravanserai.html)control the screen modes used for the upper and lower parts of the screen, so the split can be disabled for non-flight views (see below); they are also used to implement the energy bomb effect by flicking the space view in and out of multicolour bitmap mode. For normal flight, these two variables configure the top portion of the screen to be in standard bitmap mode (for the space view), and the lower portion to be in multicolour bitmap mode (for the dashboard).
- [santana](https://elite.bbcelite.com/c64/main/variable/santana.html)and- [lotus](https://elite.bbcelite.com/c64/main/variable/lotus.html)control the resolution and palette of the explosion sprite, so we can hide explosions from the dashboard portion of the screen.
- [welcome](https://elite.bbcelite.com/c64/main/variable/welcome.html)controls the background colours of the upper and lower parts of the screen, and is used by the energy bomb to flash the screen's background colour.

See the [COMIRQ1](https://elite.bbcelite.com/c64/main/subroutine/comirq1.html) routine for details of how these variables are used to set the VIC-II registers to affect the screen.

Note that unlike BBC Micro Elite, the dashboard in Commodore 64 Elite is not a permanent on-screen fixture. To fit the non-flight views onto the shorter screen, we need to remove the dashboard, which means the text views look like this:

![The Status Mode screen in Commodore 64 Elite](https://elite.bbcelite.com/images/c64/status.png) 

						and both system charts are also dashboard-free:

![The Short-range Chart in Commodore 64 Elite](https://elite.bbcelite.com/images/c64/short-range_chart.png) 

						![The Long-range Chart in Commodore 64 Elite](https://elite.bbcelite.com/images/c64/long-range_chart.png) 

						When switching to a text view, we must therefore update the values in the interrupt variables to prevent the bottom portion of the screen from switching into low-resolution multicolour mode. Specifically, we update caravanserai to switch off the split screen, and we update abraxas to point to a bank of screen RAM that contains colour information for the text views, so that text in the bottom portion of the screen is shown in white rather than the mixed colours of the dashboard. This logic is implemented in the [TTX66K](https://elite.bbcelite.com/c64/main/subroutine/ttx66k.html) routine.

Conversely, when switching back to a flight view, we need to reinstate the split screen by reverting abraxas and caravanserai. Not only that, but we need to put the dashboard bitmap back on-screen, which is done in the [wantdials](https://elite.bbcelite.com/c64/main/subroutine/wantdials.html) routine. The game loader stores up a copy of the dashboard binary at location DSTORE%, which the wantdials routine can copy into the screen bitmap to make the dashboard reappear (see the [Commodore 64 Elite memory map](https://elite.bbcelite.com/the_elite_memory_map_commodore_64.html) to see where DSTORE% fits into memory).

And that's how the Commodore 64 version's split screen mode works. It might not get the glory of the BBC Micro version, but it's just as important in making the game look good.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
LDA #line_number
  STA VIC+$12
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/the_split-screen_mode_commodore_64.html](https://elite.bbcelite.com/deep_dives/the_split-screen_mode_commodore_64.html)*

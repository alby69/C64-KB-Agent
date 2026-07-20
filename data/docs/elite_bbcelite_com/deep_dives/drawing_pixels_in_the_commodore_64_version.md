---
title: Drawing pixels in the Commodore 64 version
source_url: https://elite.bbcelite.com/deep_dives/drawing_pixels_in_the_commodore_64_version.html
category: manual
topics:
- basic
- assembly
- graphics
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

# Drawing pixels in the Commodore 64 version

## Updating the bitmap screen in the Commodore 64 version of Elite

Even though the Commodore 64's graphics are driven by a completely different chip to the BBC Micro and Acorn Electron, it turns out that the Commodore's pixel routines are a mash-up of the code from both Acorn platforms. Let's take a look.

The BBC Micro's graphics come courtesy of a 6845 CRTC chip, a custom-built Video ULA and a 6522 System VIA timer, and they look like this:

![A space station in BBC Micro cassette Elite](https://elite.bbcelite.com/images/cassette/docking_checks.png) 

						The Acorn Electron's graphics are handled by its custom Ferranti ULA, and they look like this:

![Electron Elite screenshot](https://elite.bbcelite.com/images/general/Elite-Electron.png) 

						The Commodore 64's graphics are managed by the VIC-II video processor, and they look like this:

![A space station in Commodore 64 Elite](https://elite.bbcelite.com/images/c64/station.png) 

						There are two big differences between the Acorn platforms that are relevant to Elite. First, the Electron can't support the custom 256-pixel wide mode that the BBC Micro uses, as that's implemented by reprogramming the 6845, which the Electron doesn't have; and second, the Electron can't easily support the split-screen mode, as that relies on the 6522 System VIA timer, which is also missing from the Electron. As a result the Electron uses the standard mode 4 screen for both the space view and its black-and-white dashboard. This mode is 320 pixels wide, and it displays the game in the middle 256 pixels of the screen, with a blank border of 32 pixels on each side of the game screen.

The Commodore 64's VIC-II is a lot more powerful than the chips in both the BBC Micro and the Acorn Electron, and this is obvious in the colourful dashboard, yellow borders and chunky laser crosshairs. That said, the screen isn't as tall, so there is a bit of a trade-off: the VIC-II's standard bitmap screen mode that's used for the space view is 320 pixels wide but only 200 pixels high, which is quite a bit smaller than the 248-pixel height of the Acorn versions.

Let's see how all this influences the pixel-drawing routines on the Commodore 64.

## Standard bitmap mode

													 --------------------

						The Commodore 64 separates its screen bitmap from colour information (see the deep dive on [colouring the Commodore 64 bitmap screen](https://elite.bbcelite.com/colouring_the_commodore_64_bitmap_screen.html) for information about the latter). And Commodore 64 Elite also has a split screen, with the space view using standard bitmap mode while the dashboard uses multicolour bitmap mode (see the deep dive on [the split-screen mode in Commodore 64 Elite](https://elite.bbcelite.com/the_split-screen_mode_commodore_64.html) for details).

On top of this, it turns out that the standard and multicolour screen bitmaps on the Commodore have an identical structure to the BBC Micro's screen modes 4 and 5, which are used in a customised 256-pixel wide form for the space view and dashboard in BBC Micro Elite. The Acorn Electron uses standard mode 4 for both the space view and dashboard, so for the VIC-II the authors converted their Acorn-based pixel-drawing routines as follows:

- The Commodore 64 uses the space view pixel-drawing routines from the Acorn Electron, as the structure of the standard bitmap screen on the Commodore is identical to that of the standard mode 4 screen on the BBC (320 pixels wide with a game screen of 256 pixels in the centre).
- The Commodore 64 uses the dashboard pixel-drawing routines from the BBC Micro, as the structure of the multicolour bitmap screen on the Commodore is identical to the custom mode 5 screen on the BBC. However it also incorporates row-hopping and margin calculations from the Acorn Electron, as the multicolour bitmap screen on the Commodore is 160 double-width pixels wide, which is much closer to the Electron's 320 single-width pixels than the BBC Micro's 128 double-width pixels.

There is one more subtle difference. Because we can set colour palettes for the screen individually at the character level, the Commodore 64 version draws its box borders just outside of the 256-pixel wide playing area, in the outer margins, where it can colour them yellow rather than white. The Acorn Electron version could do this if it wanted to, but for convenience it uses the same border routines as the BBC Micro, which has no choice but to draw its border box just inside the space view as the entire screen is only 256 pixels wide.

To be explicit, each pixel row on the Commodore 64 looks like this:

30 blank 2 yellow 256 pixels of 2 yellow 30 blank pixels pixels game screen pixels pixels

which looks like this in terms of bytes in a character row:

```
  24 blank     8 line      256 bytes of       8 line      24 blank
    bytes       bytes       game screen        bytes        bytes
```
						The line bytes each have two pixels in yellow along one vertical edge, to form the border. They get drawn by the [TTX66K](https://elite.bbcelite.com/c64/main/subroutine/ttx66k.html) routine.

As with the BBC Micro and Electron, each character row is 8 pixels high, so the 24 bytes of the margin and the 8 bytes of the border line cover an area of 32 pixels across and 8 pixels high, while the character row of visible screen is 256 pixels wide and 8 pixels high.

For the Commodore 64 space view, which uses standard bitmap mode, the layout of pixels is identical to the Acorn Electron, so we can use the same pixel-plotting approach (see the deep dive on [drawing pixels in the Electron version](https://elite.bbcelite.com/drawing_pixels_in_the_electron_version.html) for details). There is one speed-up, though, which takes advantage of the extra memory in the Commodore 64 compared to the Electron: instead of manually calculating the address in screen memory of each character row, we use a lookup table at [ylookupl](https://elite.bbcelite.com/c64/main/variable/ylookupl.html) and [ylookuph](https://elite.bbcelite.com/c64/main/variable/ylookuph.html) to fetch the address, which is much quicker than the algorithmic approach in the Electron version.

Similarly, when drawing to the Commodore 64 dashboard, which uses multicolour bitmap mode, the bitmap structure is the same as the BBC Micro's mode 5, so we can use the same approach to draw pixels, with two bits per pixel and four pixels per byte (see the deep dive on [drawing colour pixels on the BBC Micro](https://elite.bbcelite.com/drawing_colour_pixels_in_mode_5.html) for details). However, when converting pixel coordinates into screen addresses, or when moving to the next character row when drawing lines, we need to add 320 to the screen address rather than 256, and for that use the logic from the Acorn Electron rather than the BBC Micro.

You can see all of this in action in the [CPIX2](https://elite.bbcelite.com/c64/main/subroutine/cpix2.html) and [PIXEL](https://elite.bbcelite.com/c64/main/subroutine/pixel.html) routines, and in [part 3 of LOIN](https://elite.bbcelite.com/c64/main/subroutine/loin_part_3_of_7.html), for example.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
30 blank     2 yellow     256 pixels of     2 yellow     30 blank
   pixels       pixels       game screen       pixels       pixels
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
24 blank     8 line      256 bytes of       8 line      24 blank
    bytes       bytes       game screen        bytes        bytes
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/drawing_pixels_in_the_commodore_64_version.html](https://elite.bbcelite.com/deep_dives/drawing_pixels_in_the_commodore_64_version.html)*

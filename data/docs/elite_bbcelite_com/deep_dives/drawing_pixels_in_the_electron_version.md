---
title: Drawing pixels in the Electron version
source_url: https://elite.bbcelite.com/deep_dives/drawing_pixels_in_the_electron_version.html
category: deep-dive
topics:
- basic
- assembly
- graphics
difficulty: beginner
language: mixed
hardware:
- KERNAL
- SID
related:
- sid-registers
- sound-programming
- memory-map
- kernal-routines
- music-player
scraped_at: '2026-07-20'
---

# Drawing pixels in the Electron version

## Poking pixels into screen memory in the Acorn Electron version of Elite

The BBC Micro version of Elite has a custom screen mode that makes life pretty easy when poking pixels into screen memory. The main reason is the [square custom screen mode](https://elite.bbcelite.com/drawing_monochrome_pixels_in_mode_4.html), which is based on mode 4, but with a reduced width and height (it has 32 character columns and 31 character rows, compared to 40 columns and 32 rows in the standard mode 4 screen). This custom screen mode is not only much easier to work with, as it's exactly 256 pixels wide, but is also takes up less memory than standard mode 4 - 2,304 bytes fewer, to be exact.

The Electron, however, doesn't contain the 6845 CRTC chip, so it has no choice but to use standard mode 4. This forces the dashboard to be monochrome, like the space view, though it does mean the scanner has a higher resolution than the BBC's more colourful equivalent:

![Electron Elite screenshot](https://elite.bbcelite.com/images/general/Elite-Electron.png) 

						This is the main reason why Electron Elite has fewer features than BBC Elite: 2,304 bytes is a good 10% of the game code, so 10% of the features had to be dropped. But this memory hit is not the only downside of the Electron's use of standard mode 4; it's also more of a pain to work out which screen memory addresses we should be poking to display pixels on-screen, because instead of each screen row being a nice, clean 256 pixels across, the screen rows in standard mode 4 are 320 pixels wide.

That said, the visible part of the game screen - i.e. the space view and dashboard - are still only 256 pixels across, as they are exactly the same shape as the BBC version. So what we actually have in the Electron version is a blank border of 32 pixels on the left, and another blank border of 32 pixels on the right, with 256 pixels of game screen in the middle... and there's also a whole blank character row at the end of screen memory, which gets used in the BBC Micro version for the Python ship blueprint, but which has to remain blank in the Electron version as it's still visible (though it does get shifted to the top of the screen by changing the address of the start of screen memory in the loader, which pushes the whole screen down a line). It isn't a particularly simple setup.

To be explicit, each character row looks like this:

```
    32 blank bytes       256 bytes of visible screen       32 blank bytes
```
						where each character row is 8 pixels high, so the 32 bytes of blank border cover an area of 32 pixels across and 8 pixels high, while the character row of visible screen is 256 pixels wide and 8 pixels high. The layout of individual bits within each character row is the same as in BBC Elite (see the deep dive on [drawing monochrome pixels on the BBC Micro](https://elite.bbcelite.com/drawing_monochrome_pixels_in_mode_4.html) for details), but whereas in the BBC version we can easily work out the starting address for each character row by counting one page of memory (256 bytes) for each row - so point (x, y) is in the character row at page y div 8 - the calculation is rather more involved for the Electron.

## Calculating the character row

													 -----------------------------

						Given all this, let's take a look at how we can calculate the screen memory location for a specific pixel (x, y).

We start by calculating the screen address of the first visible pixel in the character row containing (x, y). To do this, we take the start address of screen memory (&5800), add 32 bytes to skip the first line's left border, and then we add 320 bytes for each character row that we need to move down (as each character row contains 32 + 256 + 32 = 320 bytes). This gives us the address of the first visible pixel on the row we want, so if "char row" is the number of the character row containing our pixel, the screen address of the start of that row will be:

```
     &5800 + (char row * 320) + 32
   = &5800 + (char row * (256 + 64)) + 32
   = &5800 + (char row * 256) + (char row * 64) + 32
```
						We can calculate the number of the character row containing the (x, y) pixel using y div 8, as each row is 8 pixels high, so plugging this into the above, we now get:

```
     &5800 + (char row * 256) + (char row * 64) + 32
   = &5800 + ((y div 8) * 256) + ((y div 8) * 64) + 32
```
						So we now have the screen address of the first visible pixel on the character row containing the point (x, y).

To get the address of the character block on this row that contains (x, y), we need to move right by the correct number of character blocks, which is x div 8, and there are 8 bytes per character block, so we need to add (x div 8) * 8, or (x >> 3) * 8, which can be implemented in code most easily as x AND %11111000.

So the final calculation to find the character block containing (x, y) is:

```
     &5800 + ((y div 8) * 256) + ((y div 8) * 64) + 32 + (x AND %11111000)
```
						So that's what we calculate when we want to convert a pixel coordinate into a screen memory address on the Electron - you can see this in action in the [CPIX2](https://elite.bbcelite.com/electron/main/subroutine/cpix2.html) routine, for example. The same process is used by routine [TT26](https://elite.bbcelite.com/electron/main/subroutine/tt26.html) to work out where to poke on-screen text, and you'll see the same logic dotted throughout the main line-drawing routine at [LL9](https://elite.bbcelite.com/electron/main/subroutine/loin_part_2_of_7.html).

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
32 blank bytes       256 bytes of visible screen       32 blank bytes
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
&5800 + (char row * 320) + 32
   = &5800 + (char row * (256 + 64)) + 32
   = &5800 + (char row * 256) + (char row * 64) + 32
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
&5800 + (char row * 256) + (char row * 64) + 32
   = &5800 + ((y div 8) * 256) + ((y div 8) * 64) + 32
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
&5800 + ((y div 8) * 256) + ((y div 8) * 64) + 32 + (x AND %11111000)
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/drawing_pixels_in_the_electron_version.html](https://elite.bbcelite.com/deep_dives/drawing_pixels_in_the_electron_version.html)*

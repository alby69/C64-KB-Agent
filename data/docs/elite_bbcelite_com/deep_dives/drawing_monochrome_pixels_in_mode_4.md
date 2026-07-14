---
title: Drawing monochrome pixels on the BBC Micro
source_url: https://elite.bbcelite.com/deep_dives/drawing_monochrome_pixels_in_mode_4.html
category: deep-dive
topics:
- memory management
- basic
- assembly
- graphics
difficulty: beginner
language: mixed
hardware:
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

# Drawing monochrome pixels on the BBC Micro

## Poking screen memory to display monochrome pixels in the space view

Everything boils down to pixels in the end. Even the most complicated ship battle, with ship hulls glinting in the glow of the distant sun and sparkling clouds of explosive dust dissipating into the cold vacuum of space... even this scene of destruction and mayhem is made up of pixels, each of them either black or white. We are all made of stars, and the stars are all made of pixels.

Clearly, then, plotting pixels (which we do in the [PIXEL](https://elite.bbcelite.com/cassette/main/subroutine/pixel.html) routine) is a vital part of simulating the universe, and the space view in Elite - the monochrome mode 4 part - is designed to make the process as efficient as possible. You can clearly see the monochrome mode 4 space view in-game, as it's an obvious contrast with the four-colour mode 5 dashboard:

![BBC Micro Elite screenshot](https://elite.bbcelite.com/images/general/Elite-BBCMicro.png) 

						The mode definition is set up by the loader code in elite-loader.asm, where the 6845 CRTC chip is programmed to show a screen mode with exactly 256 pixels in each row. Each pixel takes up one bit in the space view, so that means the top part of Elite's split-screen mode consists of 192 rows of pixels, with 256 bits in in each row.

So can we just plot a pixel by setting that bit on the relevant row in screen memory? Unfortunately not, as the way the BBC Micro stores its screen memory isn't completely straightforward, and to understand Elite's drawing routines, an understanding of this memory structure is essential.

## Screen memory

													 -------------

						First up, the simple part. Because mode 4 is a monochrome screen mode, each pixel is represented by one bit (1 for white, 0 for black). It's more complex for the four-colour mode 5 that's used for the dashboard portion of the screen, but for mode 4 it's as simple as it gets.

However, screen memory is not laid out as you would expect. It isn't a simple sequence of 256-bit lines, one for each horizontal pixel line, but instead the screen is split into rows and columns. Each row is 8 pixels high, and each column is 8 pixels wide, so the 192x256 space view has 24 rows and 32 columns. That 8x8 size is the same size as a standard BBC Micro text character, so the screen memory is effectively split up into character rows and columns (and it's no coincidence that these match the character layout used in Elite, where XC and YC hold the location of the text cursor, with XC in the range 0 to 32 and YC in the range 0 to 23).

The mode 4 screen starts in memory at &6000, and each character row takes up 8 rows of 256 bits, or 256 bytes, so that means each character row takes up one page of memory. So the first character row starts at &6000, the second character row starts at &6100, and so on.

Each character row on the screen is laid out like this in memory, where each digit (0, 1, 2 etc.) represents a pixel, or bit:

```
        01234567 ->-.      ,------->- 01234567->-.
                     |    |                       |
   ,-------<--------´     |     ,-------<--------´
  |                       |    |
   `->- 01234567 ->-.     |     `->- 01234567 ->-.
                     |    |                       |
   ,-------<--------´     |     ,-------<--------´
  |                       |    |
   `->- 01234567 ->-.     |     `->- 01234567 ->-.
                     |    |                       |
   ,-------<--------´     |     ,-------<--------´
  |                       |    |
   `->- 01234567 ->-.     |     `->- 01234567 ->-.
                     |    |                       |
   ,-------<--------´     |     ,-------<--------´
  |                       |    |
   `->- 01234567 ->-.     |     `->- 01234567 ->-.
                     |    |                       |
   ,-------<--------´     |     ,-------<--------´
  |                       |    |
   `->- 01234567 ->-.     |     `->- 01234567 ->-.
                     |    |                       |
   ,-------<--------´     |     ,-------<--------´
  |                       |    |
   `->- 01234567 ->-.     |     `->- 01234567 ->-.      ^
                     |    |                       |     :
   ,-------<--------´     |     ,-------<--------´      :
  |                       |    |                        |
   `->- 01234567 ->------´      `->- 01234567 ->-------´
```
						The left-hand half of the diagram displays one 8x8 character's worth of pixels, while the right-hand half shows a second 8x8 character's worth, and so on along the row, for 32 characters. Specifically, the diagram above would produce the following pixels in the top-left corner of the screen:

0123456701234567 0123456701234567 0123456701234567 0123456701234567 0123456701234567 0123456701234567 0123456701234567 0123456701234567

So let's imagine we want to draw a 2x2 bit of stardust on the screen at pixel location (7, 2) - where the origin (0, 0) is in the top-left corner - so that the top-left corner of the screen looks like this:

................ ................ .......XX....... .......XX....... ................ ................ ................ ................

Let's split this up to match the above diagram a bit more closely:

........ ........ ........ ........ .......X X....... .......X X....... ........ ........ ........ ........ ........ ........ ........ ........

As this is the first screen row, the address of the top-left corner is &6000. The first byte is the first row on the left, the second byte is the second row, and so on, like this:

&6000 = ........ &6008 = ........ &6001 = ........ &6009 = ........ &6002 = .......X &600A = X....... &6003 = .......X &600B = X....... &6004 = ........ &600C = ........ &6005 = ........ &600D = ........ &6006 = ........ &600E = ........ &6007 = ........ &600F = ........

So you can see that if we want to draw our 2x2 bit of stardust, we need to do the following:

Set &6002 = %00000001 Set &6003 = %00000001 Set &600A = %10000000 Set &600B = %10000000

Or, if we want to draw our stardust without obliterating anything that's already on-screen in this area, we can use EOR logic, like this:

Set &6002 = ?&6002 EOR %00000001 Set &6003 = ?&6002 EOR %00000001 Set &600A = ?&6002 EOR %10000000 Set &600B = ?&6002 EOR %10000000

where ?&6002 denotes the current value of location &6002. Because of the way EOR works:

0 EOR x = x 1 EOR x = NOT x

this means that the screen display will only change when we want to poke a bit with value 1 into the screen memory (i.e. paint it white), and when we're doing this, it will invert what's already on-screen. This not only means that poking a 0 into the screen memory means "leave this pixel as it is", it also means we can draw something on the screen, and then redraw the exact same thing to remove it from the screen, which can be a lot more efficient than clearing the whole screen and redrawing the whole thing every time something moves.

(The downside of EOR screen logic is that when white pixels overlap, they go black, but that's not a particularly big deal in space - and it also means that things like in-flight messages show up as black when they overlap the sun, without complex logic.)

## Converting pixel coordinates to screen locations

													 ------------------------------------------------

						Given the above, we clearly need a way of converting pixel coordinates like (7, 2) into screen memory locations. There are two parts to this - first, we need to find out which character block we need to write into, and second, which pixel row and column within that character corresponds to the pixel we want to paint.

The first step is pretty easy. The screen is split up into character rows and columns, with 8 pixels per character in both directions, so we can simply divide the pixel coordinates by 8 to get the character location. Let's look at some examples:

(7, 2) becomes (0.875, 0.25) (57, 82) becomes (7.125, 10.25) (191, 255) becomes (23.875, 31.875)

So the first pixel is at (0.875, 0.25), which is the same as saying it's in the first character block (0, 0), and is at position (0.875, 0.25) within that character. For the second example, the pixel is inside character (7, 10) and is at position (0.125, 0.25) within that character, and the third is in character (23, 31) at (0.875, 0.875) inside the character.

We can now codify this. To get the character block that contains a specific pixel, we can divide the coordinates by 8 and ignore any remainder to get the result we want, which is what the div operator does. So:

(7, 2) is in character block (7 div 8, 2 div 8) = (0, 0) (57, 82) is in character block (57 div 8, 82 div 8) = (7, 10) (191, 255) is in character block (191 div 8, 255 div 8) = (23, 31)

We can do the div 8 operation really easily in assembly language, by shifting right three times, so in assembly, we get this:

Pixel (x, y) is in the character block at (x >> 3, y >> 3)

Next, we can then use the remainder to work out where our pixel is within this 8x8 character block. The remainder is given by the mod operator, so:

(7, 2) is at pixel (7 mod 8, 2 mod 8) = (7, 2) (57, 82) is at pixel (57 mod 8, 82 mod 8) = (1, 2) (191, 255) is at pixel (191 mod 8, 255 mod 8) = (7, 7)

We can do a mod 8 operation really easily in assembly language by simply AND'ing with 7, so in assembly, we get this:

Pixel (x, y) is at position (x AND 7, y AND 7) within the character

And this is the algorithm that's implemented in this routine, though with a small twist.

## Poking bytes into screen addresses

													 ----------------------------------

						To summarise, in order to paint pixel (x, y) on the screen, we need to update this character block:

(x >> 3, y >> 3)

and this specific pixel within that character block:

(x AND 7, y AND 7)

As mentioned above, we can update this pixel by poking a byte into screen memory, so now we need to work out which memory location we need to update, and what to update it with.

We've already discussed how each character row takes up one page (256 bytes) of memory in Elite's mode 4 screen, so we can work out the page of the location we need to update by taking the y-coordinate of the character for the page. So, if (SCH SC) is the 16-bit address of the byte that we need to update in order to paint pixel (x, y) on the screen (i.e. SCH is the high byte and SC is the low byte), then we know:

SCH = &60 + y >> 3

because the first character row takes up page &60 (screen memory starts at &6000), and each character row takes up one page.

Next, within this page of memory, we want to update the character number x >> 3. Each character takes up 8x8 pixels, which is 64 bits, or 8 bytes, so we can calculate the memory location of where that character is stored in screen memory by multiplying the character number by 8, like this:

The character starts at byte (x >> 3) * 8 within the row's page

Next, we know that the pixel we want to update within this block is on row (y AND 7) in the character, and because there are 8 bits in each row (one byte), this is also the byte offset of the start of that row within the character block. So we also know this:

The pixel is in the character byte number (y AND 7)

So, to summarise, we know we need to update this byte in the row's memory page:

(x >> 3) * 8 + (y AND 7)

The final question is what to poke into this byte.

## The two TWOS tables

													 -------------------

						So we know which byte to update, and we also know which bit to set within that byte - it's bit number (x AND 7). We could always fetch that byte and EOR it with 1 shifted by the relevant number of spaces, but Elite chooses a slightly different approach, one which makes it easier for us to plot not only individual pixels, but also two pixels and even blocks of four.

There are two tables of bytes, one at [TWOS](https://elite.bbcelite.com/cassette/main/variable/twos.html) and the other at [TWOS2](https://elite.bbcelite.com/cassette/main/variable/twos2.html), that contain ready-made bytes for plotting one-pixel and two-pixel points. In each table, the byte at offset X contains a byte that, when poked into a character row, will plot a single-pixel at column X (for TWOS) or a two-pixel "dash" at column X (for TWOS2). As one example, this is what's in the fourth entry from each table (i.e. the entry at offset 3):

TWOS+3 = %00010000 TWOS2+3 = %00011000

This is the value we need to EOR with the byte we worked out above, where the offset is the bit number we want to set, i.e. (x AND 7). Or to put it another way, if we set the following:

SCH = &60 + y >> 3 SC = (x >> 3) * 8 + (y AND 7) X = x AND 7

then we want to fetch this byte:

TWOS+X

and poke it here:

(SCH SC)

to set the pixel (x, y) on-screen. (Or, if we want to set two pixels at this location, we can use TWOS2, and if we wants a 2x2 square of pixels setting, we can do the same again on the row below.)

And that's the approach used in the [PIXEL](https://elite.bbcelite.com/cassette/main/subroutine/pixel.html) routine.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
01234567 ->-.      ,------->- 01234567->-.
                     |    |                       |
   ,-------<--------´     |     ,-------<--------´
  |                       |    |
   `->- 01234567 ->-.     |     `->- 01234567 ->-.
                     |    |                       |
   ,-------<--------´     |     ,-------<--------´
  |                       |    |
   `->- 01234567 ->-.     |     `->- 01234567 ->-.
                     |    |                       |
   ,-------<--------´     |     ,-------<--------´
  |                       |    |
   `->- 01234567 ->-.     |     `->- 01234567 ->-.
                     |    |                       |
   ,-------<--------´     |     ,-------<--------´
  |                       |    |
   `->- 01234567 ->-.     |     `->- 01234567 ->-.
                     |    |                       |
   ,-------<--------´     |     ,-------<--------´
  |                       |    |
   `->- 01234567 ->-.     |     `->- 01234567 ->-.
                     |    |                       |
   ,-------<--------´     |     ,-------<--------´
  |                       |    |
   `->- 01234567 ->-.     |     `->- 01234567 ->-.      ^
                     |    |                       |     :
   ,-------<--------´     |     ,-------<--------´      :
  |                       |    |                        |
   `->- 01234567 ->------´      `->- 01234567 ->-------´
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
0123456701234567
  0123456701234567
  0123456701234567
  0123456701234567
  0123456701234567
  0123456701234567
  0123456701234567
  0123456701234567
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
................
  ................
  .......XX.......
  .......XX.......
  ................
  ................
  ................
  ................
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
........ ........
  ........ ........
  .......X X.......
  .......X X.......
  ........ ........
  ........ ........
  ........ ........
  ........ ........
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
&6000 = ........    &6008 = ........
  &6001 = ........    &6009 = ........
  &6002 = .......X    &600A = X.......
  &6003 = .......X    &600B = X.......
  &6004 = ........    &600C = ........
  &6005 = ........    &600D = ........
  &6006 = ........    &600E = ........
  &6007 = ........    &600F = ........
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
Set &6002 = %00000001
  Set &6003 = %00000001
  Set &600A = %10000000
  Set &600B = %10000000
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
Set &6002 = ?&6002 EOR %00000001
  Set &6003 = ?&6002 EOR %00000001
  Set &600A = ?&6002 EOR %10000000
  Set &600B = ?&6002 EOR %10000000
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
0 EOR x = x
  1 EOR x = NOT x
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
(7,   2)     becomes   (0.875,  0.25)
  (57,  82)    becomes   (7.125,  10.25)
  (191, 255)   becomes   (23.875, 31.875)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
(7,   2)     is in character block   (7   div 8,   2 div 8)   =   (0, 0)
  (57,  82)    is in character block   (57  div 8,  82 div 8)   =   (7, 10)
  (191, 255)   is in character block   (191 div 8, 255 div 8)   =   (23, 31)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
Pixel (x, y) is in the character block at (x >> 3, y >> 3)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
(7, 2)       is at pixel   (7   mod 8,   2 mod 8)   =   (7, 2)
  (57, 82)     is at pixel   (57  mod 8,  82 mod 8)   =   (1, 2)
  (191, 255)   is at pixel   (191 mod 8, 255 mod 8)   =   (7, 7)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
Pixel (x, y) is at position (x AND 7, y AND 7) within the character
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
(x >> 3, y >> 3)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
(x AND 7, y AND 7)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
SCH = &60 + y >> 3
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
The character starts at byte (x >> 3) * 8 within the row's page
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
The pixel is in the character byte number (y AND 7)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
(x >> 3) * 8 + (y AND 7)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
TWOS+3  = %00010000

  TWOS2+3 = %00011000
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
SCH = &60 + y >> 3
  SC = (x >> 3) * 8 + (y AND 7)
  X = x AND 7
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
TWOS+X
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
(SCH SC)
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/drawing_monochrome_pixels_in_mode_4.html](https://elite.bbcelite.com/deep_dives/drawing_monochrome_pixels_in_mode_4.html)*

---
title: base:fullscreen [Codebase64 wiki]
source_url: https://codebase.c64.org/doku.php?id=base%3Afullscreen
category: reference
topics:
- graphics
- assembly
- sprite programming
difficulty: beginner
language: mixed
hardware:
- KERNAL
- VIC-II
- SID
related:
- sid-registers
- memory-map
- music-player
- sprite-programming
- sound-programming
- kernal-routines
- vic-ii-registers
- raster-interrupts
scraped_at: '2026-07-20'
---

# base:fullscreen [Codebase64 wiki]

## Fullscreen vectors

Rendering lines into a single charset is a quite easy excursion, as we operate on the current pixel/line only. With filled areas, we have shared edges with other polygons, this raises complexity quite a bit. (And there's even more to make it complicated)

So let's define the goal to render a filled area into a single charset, where the screen is used as map. Whenever a new position on screen is taken, we can either add more content to the current char indicated by the screen/map, or allocate a new char to the current screen position and place it in the map.

The advantage of this approach is, that the screen is also our map and an indicator, if the current char we work on is yet pristine, or is allocated and thus has already underwent changes. This way the memory footprint is pretty small, a single buffer requires $0be8 bytes. Cleaning the screen is enough to start from scratch and there are several options to clean the charset. Compared to bitmap, this is way less to clean. With defining solid tiles, we can fill up larger areas by screen only. Dithered patterns can be used easily.

The disadvantages on the other hand are a rather complex code, where many extra cases apply, that are easily overseen in the beginning. Also the content/complexity is limited, as soon as the charset size is exceeded. Field tests at least show, that it takes quite a bit to reach the limit. Multiple Charsets and a split would be possible, yet adds even more complexity.

So how do we achieve that goal? As seen in skeleton.png, we render the outline of a face and fill all used chars to their upper/lower end. The remaining space inside the polygon consists then of empty 8×8 blocks that can be filled by placing the right code for a static filled block on screen.

![](https://codebase.c64.org/lib/exe/fetch.php?media=base:skeleton.png)


skeleton.png

When drawing the skeleton, we see, that when drawing the slope portions into the chars, we also need to fill some of the untouched areas of a char to complete the skeleton: Hereby we have areas in a char, where bytes are set by the slope, but also untouched areas that need to be filled somehow.

![](https://codebase.c64.org/lib/exe/fetch.php?media=base:fill_blocks.png)


White: Bytes written by the slope directly

Yellow: Bytes that additionally need to be set to make skeleton complete on a 8×8 grid

Depending on direction and left or right slope, we need to fill the remaining char to the top or bottom, in certain cases also partially or with multiple partial fills. Here begins the painful part i failed on two previous attempts. Then i realized, that i can not make any decision on which areas have to be filled, until i am done with a char in height. Entry- and exitpoints into a char in Y need to be looged in a buffer for left and right slope. Partial fills need to be done already as soon as they happen, or when left and right slope overlap in a final evaluation of the buffers with logged positions. After 8 lines of rendering the buffers are avaluated and the chars filled up as needed. If left and right slope do not overlap, the evaluation can be boiled down to a way simpler version, else complexity raises.

![](https://codebase.c64.org/lib/exe/fetch.php?w=320&tok=0b1765&media=base:reenter.png)


As shown, we can reenter a char and by that limit the yellow area to the top. The position where we reenter is only clear, when slope calculation reaches that point, not beforehand.

![](https://codebase.c64.org/lib/exe/fetch.php?w=320&tok=5412fb&media=base:double_reenter.png)


Partially fill bottom yellow area first, later also do another partial fill.

![](https://codebase.c64.org/lib/exe/fetch.php?media=base:min_left.png) 

![](https://codebase.c64.org/lib/exe/fetch.php?media=base:min_right.png) 

![](https://codebase.c64.org/lib/exe/fetch.php?media=base:max_left.png) 

![](https://codebase.c64.org/lib/exe/fetch.php?media=base:max_right.png)


Keeping track of the minimum (green) and maximum (red) positions on both sides of a polygon helps to process only the changed parts of the log. Also, this information helps us to set up a spanfill code, that fills the screen with solid blocks with speedcode.

A slope can be either left, right, steep, flat, increment or decrement in X. This means, we have 16 possible cases. Some cases however do not apply in certain situations. If we start rendering at the bottom and start with the same x/y coordinates for left and right, the following conditions will be never met, as right slope would cross left slope right away:

left side inc steep, right side dec steep

left side inc steep, right side dec flat

left side inc flat,  right side dec flat

left side inc flat,  right side dec steep

left side dec steep, right side dec flat

As a polygon opens at the bottom and slopes get closer again and close at the top, certain combinations will never happen, depending on current situation. In the overall rendering process however, all 16 variations can occur.

To allocate a new char in our map, we can simply do:

```
alloc
                ;fetch from screen
                lax (screen),y
                bne +
                inc charnum
                lax charnum
                sta (screen),y
+
                ;setup render target
                lda charset_hi,x
                sta <cset + 1
                lda charset_lo,x
                sta <cset
```
Further things to keep in mind:

Precalculated data: Advantages: Some things like sorting or clipping/tesselation can be done beforehand, this allows for less complexity when rendering. Faces can be sorted by their appearance on an axis. If we do so right to left, then the left side of a polygon can be always drawn write through, right side might need a merge with already set data.

Disadvantage: Data eats up pretty much memory

Clipping: One can easily underestimate the extra work that is inflicted by clipping vectors at the borders, some possible approaches are: Approach 1: Have an oversized canvas and always render the full object Approach 2: Object is a moving chargrid, clipping that grid is enough Approach 3: Object is in a sprite layer, clipping sprites needs extra handling for left/right and top/bottom Approach 4: Clip the data itself so it can't exceed borders Approach chosen here: Extend canvas to top/bottom to be able to draw outside of the normal screen, then copy over to sprites placed in border to avoid additional rendering technique, but also include Approach 4 for normal fullscreen behaviour and clipping on left and right side.

Fill with alternating patterns: Filling with dither patterns add even more complexity, depending if current y-position during rendering is odd or even, we need to set a different pattern at additional costs.

And finally, here we go for the sourcecode or all this:
[full.zip](https://codebase.c64.org/lib/exe/fetch.php?media=base:full.zip)

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
alloc
                ;fetch from screen
                lax (screen),y
                bne +
                inc charnum
                lax charnum
                sta (screen),y
+
                ;setup render target
                lda charset_hi,x
                sta <cset + 1
                lda charset_lo,x
                sta <cset
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Afullscreen](https://codebase.c64.org/doku.php?id=base%3Afullscreen)*

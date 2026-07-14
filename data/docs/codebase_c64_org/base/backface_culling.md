---
title: base:backface_culling [Codebase64 wiki]
source_url: https://codebase.c64.org/doku.php?id=base%3Abackface_culling
category: reference
topics:
- assembly
difficulty: beginner
language: assembly
hardware: []
related: []
scraped_at: '2026-07-14'
---

# base:backface_culling [Codebase64 wiki]

### Table of Contents

### Backface Culling

by Bitbreaker/Oxyron/Nuance

An easy way to find out if a face faces towards the viewer or away is to check whether the area covered by a face is positive (frontface) or negative (backface). This done by taking the first 3 vertices (already transformed into 2D) of that face and calculating the following:

(v1.y - v0.y) * (v2.x - v1.x) - (v1.x - v0.x) * (v2.y - v1.y)

If the result is positive, the face is visible and rendered, else it is discarded.

```
         ;calculate the signed area while copying the vertices into the vertexbuffer for drawing
         ldx faces+0,y
         lda vertices_x,x
         sta verticebuf_x+0
         lda vertices_y,x
         sta verticebuf_y+0
         ldx faces+1,y
         lda vertices_x,x
         sta verticebuf_x+1
         sec
         sbc verticebuf_x+0
         ;set up first factor
         sta z1_+1
         eor #$ff
         sta z2_+1
         lda vertices_y,x
         sta verticebuf_y+1
         sec
         sbc verticebuf_y+0
         ;set up second factor
         sta z3_+1
         eor #$ff
         sta z4_+1
         ldx faces+2,y
         lda vertices_x,x
         sta verticebuf_x+2
         sec
         sbc verticebuf_x+1
         ;multiplier 1
         tay
         
         lda vertices_y,x
         sta verticebuf_y+2
         sec
         sbc verticebuf_y+1
         ;multiplier 2
         tax
z3_      lda tmath1,y
         sec
z4_      sbc tmath2,y
         sec
z1_      sbc tmath1,x
         clc
z2_      adc tmath2,x
         ;skip if negative
         bmi +
         jsr drawface
+
```
Though things are fast, all this can be a bit unprecise when faces get small, so it is smart to let the filler test if x1 > x2 when drawing a line of a face and thus stopping filling if this happens, else you might end up in slight glitches.

### Backface Culling - Alot faster method

by JackAsser / Booze Design

Please see the attached PDF. [rotation_and_backface_culling_for_simple_demo.pdf](https://codebase.c64.org/lib/exe/fetch.php?media=base:rotation_and_backface_culling_for_simple_demo.pdf)

## Codice Estratto

### Snippet Codice (BASIC)

```basic
;calculate the signed area while copying the vertices into the vertexbuffer for drawing
         ldx faces+0,y
         lda vertices_x,x
         sta verticebuf_x+0
         lda vertices_y,x
         sta verticebuf_y+0

         ldx faces+1,y
         lda vertices_x,x
         sta verticebuf_x+1
         sec
         sbc verticebuf_x+0

         ;set up first factor
         sta z1_+1
         eor #$ff
         sta z2_+1

         lda vertices_y,x
         sta verticebuf_y+1
         sec
         sbc verticebuf_y+0

         ;set up second factor
         sta z3_+1
         eor #$ff
         sta z4_+1

         ldx faces+2,y
         lda vertices_x,x
         sta verticebuf_x+2
         sec
         sbc verticebuf_x+1

         ;multiplier 1
         tay
         
         lda vertices_y,x
         sta verticebuf_y+2
         sec
         sbc verticebuf_y+1

         ;multiplier 2
         tax

z3_      lda tmath1,y
         sec
z4_      sbc tmath2,y
         sec
z1_      sbc tmath1,x
         clc
z2_      adc tmath2,x

         ;skip if negative
         bmi +
         jsr drawface
+
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Abackface_culling](https://codebase.c64.org/doku.php?id=base%3Abackface_culling)*

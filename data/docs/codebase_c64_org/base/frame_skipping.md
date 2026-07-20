---
title: Frame skipping
source_url: https://codebase.c64.org/doku.php?id=base%3Aframe_skipping
category: reference
topics:
- raster interrupts
- assembly
difficulty: intermediate
language: assembly
hardware:
- SID
related:
- sid-registers
- music-player
- sprite-programming
- sound-programming
- vic-ii-registers
- raster-interrupts
scraped_at: '2026-07-20'
---

# Frame skipping

base:frame_skipping

                # Frame skipping

Once in a while you created some effect that just goes too quick when you update it every frame. The option is to have a check in order to skip your routine every other frame. Put this inside your IRQ.

start: inc skipper+1 // increase the check byte skipper: lda #$00 // check byte and #$01 // check first bit (even or odd number?) beq passroutine // skip routine on even numbers routine: // routine that will be executed every other frame passroutine: // the rest, executed every frame

base/frame_skipping.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`start`** (unknown): No description available
- **`skipper`** (unknown): No description available
- **`routine`** (unknown): No description available
- **`passroutine`** (unknown): routine that will be executed every other frame

```assembly
start:
   inc skipper+1      // increase the check byte
   
skipper:
   lda #$00           // check byte
   and #$01           // check first bit (even or odd number?)
   beq passroutine    // skip routine on even numbers
   
routine:
   // routine that will be executed every other frame
   
passroutine:
   // the rest, executed every frame
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Aframe_skipping](https://codebase.c64.org/doku.php?id=base%3Aframe_skipping)*

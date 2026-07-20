---
title: Very short play routine
source_url: https://codebase.c64.org/doku.php?id=base%3Avery_short_sid_playroutine
category: reference
topics:
- input handling
- raster interrupts
- assembly
- basic
difficulty: intermediate
language: mixed
hardware:
- CIA
- VIC-II
- SID
related:
- sid-registers
- keyboard-handling
- joystick-reading
- music-player
- sprite-programming
- sound-programming
- cia-registers
- vic-ii-registers
- raster-interrupts
scraped_at: '2026-07-20'
---


# Very short play routine

# Very short play routine

A very short music playroutine with fast forward function. Hold spacebar to fast forward the tune. For tunes between $0800-$9FFF

Coded by The Typhoon / Future Technologics 2009 in the year 1988 brought to the C64 Codebase by G-Fellow / Hokuto Force

Written directly in the MON of the Action Replay - Write in your MON of the Action Replay ' > 3000 SEI ' [RETURN] to start coding. To LIST your code in the Action Replay MON write ' D 3000 301F '

The example code is for a tune on $1000 with Init;$1000 and Play;$1003 - Start this code when you finished it, in the MON with 'G 3000' or in the Basic C=64 with 'SYS 3*4096' / You could write of course this play routine on every other place in the memory or simply load it to the specific adress in the memory when you once saved the code on floppy disk.

- .> 3000 SEI
- .> 3001 LDA #$00
- .> 3003 JSR $1000 ;Tune Init
- .> 3006 LDA $D012
- .> 3009 CMP #$72
- .> 300B BNE $3006
- .> 300D INC $D020
- .> 3010 JSR $1003 ;Tune Play
- .> 3013 DEC $D020
- .> 3016 LDA $DC01
- .> 3019 CMP #$EF
- .> 301B BEQ $3010
- .> 301D BNE $3006

---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Avery_short_sid_playroutine](https://codebase.c64.org/doku.php?id=base%3Avery_short_sid_playroutine)*


### Collegamenti e Riferimenti Hardware
- **$D020 (Border Color)**: Associato al chip VIC-II. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#d020).
- **$D012 (Raster Counter)**: Associato al chip VIC-II. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#d012).
- **$DC01 (CIA 1 Port B (Joystick 1, Keyboard))**: Associato al chip CIA. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#dc01).

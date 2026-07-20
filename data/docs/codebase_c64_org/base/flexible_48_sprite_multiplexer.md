---
title: base:flexible_48_sprite_multiplexer [Codebase64 wiki]
source_url: https://codebase.c64.org/doku.php?id=base%3Aflexible_48_sprite_multiplexer
category: tool
topics:
- sprite programming
difficulty: advanced
language: none
hardware:
- VIC-II
related:
- vic-ii-registers
- raster-interrupts
- sprite-programming
scraped_at: '2026-07-20'
---

# base:flexible_48_sprite_multiplexer [Codebase64 wiki]

base:flexible_48_sprite_multiplexer

                
![](https://codebase.c64.org/lib/exe/fetch.php?media=base:44sprs.png)


This is an update to the [Flexible 32 Sprite Multiplexer - Version 2](https://codebase.c64.org/doku.php?id=base:flexible_32_sprite_multiplexer_2) code to display up to 48 sprites.

[Updated sources available in the large archive here](https://codebase.c64.org/doku.php?id=projects:resurrection)

The assembled demo is at C64\SpriteMultiplexor\TestMultiplexor.prg and can be tested with CCS64 or Vice emulators.

To assemble open a command line window, change directory to C64\SpriteMultiplexor then use: ..\acme.exe -v3 TestMultiplexor.a

The sources have plenty of comments.

The C64\Scroller demonstration code also uses the multiplexer and shows how to hook in your own interrupt chain as well as some of the more advanced features for avoiding raster time overflows.

base/flexible_48_sprite_multiplexer.txt · Last modified:  by 127.0.0.1

---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Aflexible_48_sprite_multiplexer](https://codebase.c64.org/doku.php?id=base%3Aflexible_48_sprite_multiplexer)*

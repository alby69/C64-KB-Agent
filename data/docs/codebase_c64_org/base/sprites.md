---
title: Sprites
source_url: https://codebase.c64.org/doku.php?id=base%3Asprites
category: tutorial
topics:
- basic
- assembly
- sprite programming
difficulty: beginner
language: assembly
hardware:
- KERNAL
- CPU
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

# Sprites

base:sprites

                ### Table of Contents

# Sprites

Everything sprite related. This page contains all information on sprite programming, and other sections such as the VIC, demo coding and game coding sections link to this page, rather than having own links to sprite articles.

## Basic stuff

- [Introduction to Sprites](https://codebase.c64.org/doku.php?id=base:spriteintro)- by Oswald/Resource
- [Sprite X-coordinate calculus](https://codebase.c64.org/doku.php?id=base:sprite_x-coordinate_calculus)- by The_WOZ/soft154i
- [Ballon demo from Manual](https://codebase.c64.org/doku.php?id=base:ballon_demo_from_manual)- by Andreas Bujok

## Multiplexing

- [Sprite multiplexing](https://codebase.c64.org/doku.php?id=base:sprite_multiplexing)- aka- ["Rant 3"](http://cadaver.homeftp.net/rants/sprite.htm)- tutorial by Cadaver
- [Simple Sprite-Multiplexing using Sprite 1](https://codebase.c64.org/doku.php?id=base:simple_sprite-multiplexing_using_sprite_1)- by cbmhardware
- [Sprite Multiplexer](https://codebase.c64.org/doku.php?id=base:sprite_multiplexer)- by Fungus.
- [Sprite Multiplexer 2](https://codebase.c64.org/doku.php?id=base:sprite_multiplexer_2)- by Fungus. More advanced.
- [Sprite Multiplexer 3](https://codebase.c64.org/doku.php?id=base:sprite_multiplexer_3)- by Fungus. Even more advanced, but still got some bugs. Available here to express the idea.
- [Flexible 32 Sprite Multiplexer](https://codebase.c64.org/doku.php?id=base:flexible_32_sprite_multiplexer)- by Thcm. Advanced Multiplexer with a very fast sorting algo.
- [Flexible 32 Sprite Multiplexer - Version 2](https://codebase.c64.org/doku.php?id=base:flexible_32_sprite_multiplexer_2)- Updates by MP. Advanced Multiplexer with a very fast sorting algo.
- [Flexible 48 Sprite Multiplexer](https://codebase.c64.org/doku.php?id=base:flexible_48_sprite_multiplexer)- by MP. Source and demo unit test.

## Sorting Routines for Multiplexers

Several of the articles above touch on sort routines, and Cadaver's “Rant 3” compares a few. The following pages focus purely on sorting.

- [Sprite multiplexer sorting](https://codebase.c64.org/doku.php?id=base:sprite_multiplexer_sorting)- Sprite 'Y' sorting research by Falco Paul
- [Flagged Bucket Sort](https://codebase.c64.org/doku.php?id=base:flagged_bucket_sort)- a “fast worst case” sorter by Christopher Jam
- [A Faster Radix Sort](https://codebase.c64.org/doku.php?id=base:a_faster_radix_sort)- by lft

There are also information about sorting available on the [maths and algorithms](https://codebase.c64.org/doku.php?id=base:6502_6510_maths#sorting) page.

## Collision Detection

- [Simple Hardware Sprite to sprite collision](https://codebase.c64.org/doku.php?id=base:simple_hardware_sprite_to_sprite_collision)- by Richard Bayliss
- [Simple Software Sprite to sprite collision](https://codebase.c64.org/doku.php?id=base:simple_software_sprite_to_sprite_collision)- by Richard Bayliss
- [Simple Hardware Sprite to Background collision](https://codebase.c64.org/doku.php?id=base:simple_hardware_sprite_to_background_collision)- by Richard Bayliss
- [Hybrid Hardware/Software Sprite collision detection](https://codebase.c64.org/doku.php?id=base:hybrid_hardware_software_sprite_collision_detection)- by Flavioweb

## Tricks

- [Sprites in Bottom Sideborder](https://codebase.c64.org/doku.php?id=base:sprites_in_bottom_sideborder)- by Groepaz/Hitmen
- [Sprite FPP](https://codebase.c64.org/doku.php?id=base:sprite_fpp)how to display any gfx line at any place using sprites
- [Stretching Sprites](https://codebase.c64.org/doku.php?id=magazines:chacking5#the_demo_cornerstretching_sprites)by Pasi 'Albert' Ojala ( C= Hacking #5)
- [Sprite Interleave](https://codebase.c64.org/doku.php?id=base:sprite_interleave)to help with large sprite arrays - by Raistlin/Genesis*Project (with thanks to Christopher Jam)

## Demo Effects using Sprites

These are also available on the Demo Coding page.

- [Scrolltext using Sprites](https://codebase.c64.org/doku.php?id=base:scrolltext_using_sprites)- by Testicle
- [8 Sprite starfield](https://codebase.c64.org/doku.php?id=base:8_sprite_starfield)- by Richard Bayliss

## Various

- [Sprite Converter](https://codebase.c64.org/doku.php?id=base:sprite_converter)- a simple tool (Python script) to convert images to fields of sprites
- [Sprite Mirror](https://codebase.c64.org/doku.php?id=base:sprite_mirror)- by Antonio Savona
- [GIF to Sprites](https://codebase.c64.org/doku.php?id=base:gif_to_sprites)- Kick Assembler script to convert a formatted GIF to a sprite font

base/sprites.txt · Last modified:  by 127.0.0.1

---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Asprites](https://codebase.c64.org/doku.php?id=base%3Asprites)*

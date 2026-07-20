---
title: Game Programming
source_url: https://codebase.c64.org/doku.php?id=base%3Agame_programming
category: tutorial
topics:
- basic
- assembly
- raster interrupts
- input handling
- sprite programming
difficulty: beginner
language: assembly
hardware:
- CPU
- KERNAL
- CIA
- VIC-II
related:
- keyboard-handling
- memory-map
- joystick-reading
- sprite-programming
- kernal-routines
- cia-registers
- vic-ii-registers
- raster-interrupts
scraped_at: '2026-07-20'
---

# Game Programming

base:game_programming

                ### Table of Contents

# Game Programming

This section contains material specifically related to issues of game coding. Of course, “game coding” involves many things that are also covered elsewhere on the wiki, such as graphics programming, disk/keyboard/joystick access, sound programming, and so forth, but the articles listed on this page are nevertheless written with the specific topic of game programming in mind. For example, optimization priorities may be a bit different when coding a demo effect and when coding a game engine.

## General Tutorials

- From the “Learning ML” series by Craig Bruce, in C= Hacking:- [Learning ML 4](https://codebase.c64.org/doku.php?id=magazines:chacking4#learning_machine_language_-_part_4)- Development of a Space Invaders game (for the 64 and 128), part 1
 

- From the “Rants” series by Cadaver/Covert BitOps- [Multidirectional scrolling and the "game world"](https://codebase.c64.org/doku.php?id=base:rant4)- aka- ["Rant 4"](http://cadaver.homeftp.net/rants/scroll.htm)- article by Cadaver
- [Frameskipping, interpolation and re-entrant IRQ code](https://codebase.c64.org/doku.php?id=base:rant9)- aka- ["Rant 9"](http://cadaver.homeftp.net/rants/interp.htm)- article by Cadaver
- [Significant tricks & techniques in Metal Warrior 4](https://codebase.c64.org/doku.php?id=base:rant11)- aka- ["Rant 11"](http://cadaver.homeftp.net/rants/mw4trick.htm)- article by Cadaver
 

- [4 ways scroll](https://codebase.c64.org/doku.php?id=base:4_ways_scroll)- By Malcolm Bamber. How To Scroll Around A 2 By 2 Tile Based Map.

- Tile Maps - by Achim

- Graphic effects- [Static starfield](https://codebase.c64.org/doku.php?id=base:static_starfield)- by Achim
- [Simple parallax shifting](https://codebase.c64.org/doku.php?id=base:simple_parallax_shifting)- by Achim
- [Merge char bullets with background chars](https://codebase.c64.org/doku.php?id=base:merge_char_bullets)- by Achim
- [Character bullets](https://codebase.c64.org/doku.php?id=base:character_bullets)- by Achim
 

## Sprites

Sprites, aka hardware supported freely movable objects, are an essential part of most games.

- [Sprites](https://codebase.c64.org/doku.php?id=base:sprites)- General wiki section devoted to sprite programming
- [Sprite collision detection](https://codebase.c64.org/doku.php?id=base:sprite_collision_detection)- Using individual sprite 'boxes' to detect sprite-sprite collisions - by Achim
- [Moving sprites](https://codebase.c64.org/doku.php?id=base:moving_sprites)- Sort sprite movement from updating VIC registers - by Achim
- [Sprite projectiles](https://codebase.c64.org/doku.php?id=base:sprite_projectiles)- moving sprite projectiles in any direction - by Achim

## Various

- [High Score detection](https://codebase.c64.org/doku.php?id=base:high_score_detection)- By Richard Bayliss
- [Guide to programming games](https://codebase.c64.org/doku.php?id=base:guide_to_programming_games)- An article about designing, writing and compressing your own C64 game - by Richard Bayliss
- [Scoring points](https://codebase.c64.org/doku.php?id=base:scoring_points)- by Achim

## Sources for games

Here are sources for a few small games.

### by Hannu Nuotio

- [Quest for Cash](https://codebase.c64.org/doku.php?id=base:quest_for_cash)- A puzzle game
- [Pallo](https://codebase.c64.org/doku.php?id=base:pallo)- A “collect and avoid” game

### by HMVDVA/HeMa!

- [MicroPong](https://codebase.c64.org/doku.php?id=base:micropong)- The classic videogame for 2 players in 824bytes by Scout/Silicon Ltd. (as HMVDVA/HeMa!)

### by Richard Bayliss

- [Balloonacy II](https://codebase.c64.org/doku.php?id=base:balloonacy_ii)(DASM Source code) - The crazy balloon style adventure game
- [Duo Blast](https://codebase.c64.org/doku.php?id=base:duo_blast)- A simple 2 player game
- [For Speed We Need](https://codebase.c64.org/doku.php?id=base:for_speed_we_need)- A dodge racing game
- [Jeffy](https://codebase.c64.org/doku.php?id=base:jeffy)(TASS Source Code) - The crazy grab and avoid game written in 2005.
- [Racked Off](https://codebase.c64.org/doku.php?id=base:racked_off)(ACME Source code) - The funny arcade game
- [Hyper Duel](https://codebase.c64.org/doku.php?id=base:hyper_duel)(ACME Source code) - Fun 2 player game based on Super Dogfight, but weirder!
- [Bomb Chase 2009](https://codebase.c64.org/doku.php?id=base:bomb_chase_2009)(ACME Source code)

## Sources for PC/Mac Development Tools

- [Dev Tools written in Dark Basic](http://dark-well.pwp.blueyonder.co.uk/)- by Malcolm Bamber
- [C64 Studio Source Code](https://github.com/GeorgRottensteiner/C64Studio)- by Georg Rottensteiner

base/game_programming.txt · Last modified:  by 127.0.0.1

---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Agame_programming](https://codebase.c64.org/doku.php?id=base%3Agame_programming)*

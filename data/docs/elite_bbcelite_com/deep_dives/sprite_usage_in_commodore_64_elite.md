---
title: Sprite usage in Commodore 64 Elite
source_url: https://elite.bbcelite.com/deep_dives/sprite_usage_in_commodore_64_elite.html
category: deep-dive
topics:
- sprite programming
- basic
- assembly
- graphics
difficulty: beginner
language: mixed
hardware:
- CPU
- SID
- KERNAL
- VIC-II
related:
- sound-programming
- music-player
- raster-interrupts
- memory-map
- sprite-programming
- vic-ii-registers
- kernal-routines
- sid-registers
scraped_at: '2026-07-14'
---

# Sprite usage in Commodore 64 Elite

## Laser crosshairs, colourful explosions and lots of cuddly, furry Trumbles

The Commodore 64 supports hardware sprites, and Elite uses them in three different ways: for the different laser crosshairs, the colourful explosion sprite, and those pesky Trumbles. Sprites are an easy way to add colour to an otherwise black-and-white space view, and coupled with the colourful dashboard, it's easy to forget just how monochrome space really is.

See the deep dive on [colouring the Commodore 64 bitmap screen](https://elite.bbcelite.com/colouring_the_commodore_64_bitmap_screen.html) for more about the game's bitmap colour system, and read on for a look at the game's sprites.

## Elite's sprites

													 ---------------

						Here's a list of all seven sprite designs used in Commodore 64 Elite. These are defined in the [sprites source file](https://elite.bbcelite.com/c64/all/elite_sprites.html).

| Sprite | Description | 
|---|---|
| ![The pulse laser crosshairs in Commodore 64 Elite](https://elite.bbcelite.com/images/c64/pulse_laser.png) | Pulse laser crosshairs (in centre of screen) | 
| ![The beam laser crosshairs in Commodore 64 Elite](https://elite.bbcelite.com/images/c64/beam_laser.png) | Beam laser crosshairs (in centre of screen) | 
| ![The military laser crosshairs in Commodore 64 Elite](https://elite.bbcelite.com/images/c64/station.png) | Military laser crosshairs (in centre of screen) | 
| ![The mining laser crosshairs in Commodore 64 Elite](https://elite.bbcelite.com/images/c64/mining_laser.png) | Mining laser crosshairs (in centre of screen) | 
| ![The explosion sprite in Commodore 64 Elite](https://elite.bbcelite.com/images/c64/explosion.png) | Explosion sprite (inside the crosshairs) | 
| ![Trumble sprites in Commodore 64 Elite](https://elite.bbcelite.com/images/c64/trumbles_clipped1.png) | Trumble looking right (e.g. blue Trumble) | 
| ![Trumble sprites in Commodore 64 Elite](https://elite.bbcelite.com/images/c64/trumbles_clipped2.png) | Trumble looking left (e.g. grey Trumble) | 

There are eight hardware sprites supported by the Commodore 64's VIC-II chip. They are numbered 0 to 7, and in Elite they are used as follows:

| Sprite | Description | 
|---|---|
| 0 | Current laser crosshairs (pulse, beam, military, mining) | 
| 1 | Explosion sprite | 
| 2 | Trumble 0 (brown, looking right) | 
| 3 | Trumble 1 (grey, looking left) | 
| 4 | Trumble 2 (blue, looking right) | 
| 5 | Trumble 3 (white, looking left) | 
| 6 | Trumble 4 (green, looking right) | 
| 7 | Trumble 5 (brown, looking left) | 

These sprites are configured and manipulated by the following parts of the codebase:

- The correct laser crosshairs definition for the current view is allocated to sprite 0 by the [SIGHT](https://elite.bbcelite.com/c64/main/subroutine/sight.html)routine, using the colours in the[sightcol](https://elite.bbcelite.com/c64/main/variable/sightcol.html)variable.
- The explosion sprite is shown briefly as a flash of colour when a ship explodes. The sprite is shown on-screen by the [PTCLS2](https://elite.bbcelite.com/c64/main/subroutine/ptcls2.html)routine, which is called once from the explosion routine at[DOEXP](https://elite.bbcelite.com/c64/main/subroutine/doexp.html)at the start of the explosion. The sprite is removed from the screen by the[RDKEY](https://elite.bbcelite.com/c64/main/subroutine/rdkey.html)routine.
- The colours of the six Trumble sprites are set up in [part 4 of the game loader](https://elite.bbcelite.com/c64/game_loader/subroutine/elite_loader_part_4_of_7.html).
- The sprite definitions are mapped to the relevant sprite numbers in [part 7 of the game loader](https://elite.bbcelite.com/c64/game_loader/subroutine/elite_loader_part_7_of_7.html). This is also where the direction of gaze for the Trumble sprites is set. Sprite definitions are mapped to sprite numbers by writing to the sprite pointers in the last eight bytes of screen RAM, so we have to do this twice, as we have two banks of screen RAM, one for the space view and another for the text view (see the deep dive on[colouring the Commodore 64 bitmap screen](https://elite.bbcelite.com/colouring_the_commodore_64_bitmap_screen.html)for details).
- The Trumble sprites get moved around the screen in the [MVTRIBS](https://elite.bbcelite.com/c64/main/subroutine/mvtribs.html)routine, which moves one Trumble on each iteration of the main flight loop. It is only called if the Trumbles mission is in progress.

Sprite operations work by updating the relevant registers in the VIC-II chip. The [MVTRIBS](https://elite.bbcelite.com/c64/main/subroutine/mvtribs.html) and [SIGHT](https://elite.bbcelite.com/c64/main/subroutine/sight.html) routines are good places to see this in action.

---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/sprite_usage_in_commodore_64_elite.html](https://elite.bbcelite.com/deep_dives/sprite_usage_in_commodore_64_elite.html)*

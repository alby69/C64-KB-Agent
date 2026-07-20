---
title: Sprite usage in NES Elite
source_url: https://elite.bbcelite.com/deep_dives/sprite_usage_in_nes_elite.html
category: deep-dive
topics:
- basic
- assembly
- sprite programming
difficulty: beginner
language: mixed
hardware:
- KERNAL
- SID
- CPU
- VIC-II
related:
- sid-registers
- sound-programming
- vic-ii-registers
- memory-map
- kernal-routines
- music-player
- sprite-programming
- raster-interrupts
scraped_at: '2026-07-20'
---

# Sprite usage in NES Elite

## Stardust, scanners, images, crosshairs and more

When Elite was ported to the Commodore 64 in 1985, the authors took advantage of the new system's hardware sprite system. Commodore 64 Elite therefore has differently coloured and shaped laser sights depending on the type of laser fitted, there's a colourful explosion burst that flashes briefly when ships are destroyed, and the new Trumbles mission smothers the screen with oversized cuddly critters (which none of the other 6502 versions do - the Trumbles in the NES version don't manage to crawl out onto the cockpit canopy, thankfully). The original BBC Micro version doesn't have any sprites as the BBC Micro doesn't support them, so while these new sprite-based features are nice additions, they don't really change any core aspects of the game.

Sprites in NES Elite are much more important, and they play a vital role in getting Elite to work on the tile-based console. Let's take a look at sprite usage in the NES version.

## Sprites in the flight screen

													 ----------------------------

						The wireframe space view in NES Elite is monochrome, with cyan lines on a black background, and truth be told it is slightly bland; the 6502 Second Processor version from 1985 introduced four colours into the space view, and the BBC Master continued that tradition, so to find the 1991 NES version going back to monochrome space is a bit of a surprise. There are important technical reasons for this, as explained in the deep dive on [drawing vector graphics using NES tiles](https://elite.bbcelite.com/drawing_vector_graphics_using_nes_tiles.html), but luckily there's an easy way to bring a small splash of colour back into the space view: by using sprites.

When flying our Cobra Mk III through space, there are quite a few sprites on-screen. Consider this in-flight screenshot:

![A deep space view showing a planet and an asteroid in NES Elite](https://elite.bbcelite.com/images/nes/bitplanes/planet_asteroid.png) 

						If we hide the background and zoom in on the sprites, this is what they look like:

![Sprites on the flight screen in NES Elite](https://elite.bbcelite.com/images/nes/sprites/flight_sprites.png) 

						The sprites that you can see on-screen include the green laser sights in the middle of the space view, four yellow stardust particles, five cyan stardust particles, the pink icon bar pointer, the purple blob of sprite 0 just to the right of that, the green blobs of the compass and condition indicators just below the pointer, the two pink pitch and roll indicator bars, and in the middle of the 3D scanner, a solitary ship indicator for the asteroid.

The rest of the sprites are tucked away on the bottom row of the screen. These sprites are at a pixel y-coordinate of 240, which moves them off the bottom of the screen; this is the easiest way to remove sprites from view on the NES. In this off-screen collection of sprites, you can see a whole set of green 3D scanner sticks waiting their turn, as things can get a lot more hectic on the scanner. For example, here's a slightly more interesting example:

![The 3D scanner in NES Elite](https://elite.bbcelite.com/images/nes/sprites/scanner.png) 

						For this one, there are six sprites on the scanner, showing five ships (with one ship needing two sprites of a possible three):

![Sprites on the scanner in NES Elite](https://elite.bbcelite.com/images/nes/sprites/scanner_sprites.png) 

						In terms of sprite numbers, the flight screen uses the 64 available sprites like this:

- Sprite 0 is always used to implement the split screen (see the deep dive on [the split-screen mode in NES Elite](https://elite.bbcelite.com/the_split-screen_mode_nes.html)for details)
- Sprites 1 to 4 are always used for the pink icon bar pointer ([see MoveIconBarPointer](https://elite.bbcelite.com/nes/bank_7/subroutine/moveiconbarpointer.html))
- Sprites 5 to 8 are used for the laser sights (see [SIGHT](https://elite.bbcelite.com/nes/bank_3/subroutine/sight.html))
- Sprite 10 is the status indicator on the dashboard (see [DIALS](https://elite.bbcelite.com/nes/bank_6/subroutine/dials.html))
- Sprites 11 and 12 are the roll and pitch indicator bars (see [DIALS](https://elite.bbcelite.com/nes/bank_6/subroutine/dials.html))
- Sprite 13 is the compass dot (see [COMPAS](https://elite.bbcelite.com/nes/bank_0/subroutine/compas.html))
- Sprites 14 to 37 are for up to eight ships on the 3D scanner, with three sprites allocated to each ship - the taller the stick, the larger the number of sprites required for that ship (see [SCAN](https://elite.bbcelite.com/nes/bank_1/subroutine/scan.html))
- Sprites 38 to 57 are stardust particles, which can be shown in pale yellow and dark cyan (see [STARS](https://elite.bbcelite.com/nes/bank_1/subroutine/stars1.html)and[PIXEL2](https://elite.bbcelite.com/nes/bank_1/subroutine/pixel2.html))
- Sprites 59 to 62 are used to show a colourful explosion burst when a ship explodes (see [DrawExplosionBurst](https://elite.bbcelite.com/nes/bank_1/subroutine/drawexplosionburst.html))

Sprite 9, 58 and 63 are not used in the space view, and sprite 0 is always hidden behind the box edges, but the other 60 sprites can all appear on-screen during flight, bringing a much-needed splash of colour to the monochrome space view.

## Sprite-based images

													 -------------------

						Sprites are also used to create beautiful images throughout the game. The poster child for sprite usage is the two-layer image system, which is used to draw beautiful system and commander images like this:

![An example system image in NES Elite](https://elite.bbcelite.com/images/nes/two-layer_images/systemImage14_0.png) 

						These images are so pretty that they have their own deep dive: see [displaying two-layer images](https://elite.bbcelite.com/displaying_two-layer_images.html) for details.

Another great use of sprites is in the Equip Ship screen, which shows our ship's loadout on an image of the Cobra Mk III:
						![The Cobra Mk III with a full loadout on the NES Elite Equip Ship screen](https://elite.bbcelite.com/images/nes/commander/max_equipment.png) 

						

The Cobra image is drawn using background tiles, but all of the pieces of equipment are drawn on top of the spaceship using sprites. Here's a zoomed-in sprite layout for the above screen, showing all the individual pieces of equipment that are fitted to our maxed-out ship:

![Sprites on the Equip Ship screen in NES Elite](https://elite.bbcelite.com/images/nes/sprites/equipment_sprites.png) 

						Let's try to label each piece of equipment in the above image, with each letter representing one 8x8-pixel sprite:

```
                         a                    e     ff
                                      b       e     ff       c
                      ff    g            ki      a      hj
                      ff      e               l  mm  l
                h       n n       i
              j                     k
            b         oo              c
                        ppp
                         d
```
						Here's the equipment that each sprite represents:

| Key | Equipment | 
|---|---|
| a | Front laser | 
| b | Left laser | 
| c | Right laser | 
| d | Rear laser | 
| e | E.C.M. | 
| f | Docking computer | 
| g | Escape pod | 
| h | Missile 1 | 
| i | Missile 2 | 
| j | Missile 3 | 
| k | Missile 4 | 
| l | Large cargo bay | 
| m | Fuel scoops | 
| n | Galactic hyperdrive | 
| o | Energy unit | 
| p | Energy bomb | 

The [DrawEquipment](https://elite.bbcelite.com/nes/bank_6/subroutine/drawequipment.html) routine is responsible for drawing the relevant sprites, depending on the loadout. The patterns for both the Cobra and all the bits of equipment are in the packed image at [cobraImage](https://elite.bbcelite.com/nes/bank_3/variable/cobraimage.html), and the [equipSprites](https://elite.bbcelite.com/nes/bank_6/variable/equipsprites.html) table maps each piece of equipment to its respective sprites and patterns, along with all the coordinates and attributes needed to display the equipment sprites on the ship.

When actually playing the game, it isn't particularly easy to match the equipment to the sprites, but there's fun to be had trying to work out what changes on your ship following a shopping spree...

## Other sprites

													 -------------

						Outside of the two-layer images and equipment sprites, there other some images are drawn entirely out of sprites. The biggest of these is the Elite logo shown on the Save and Load screen, which is drawn using the [DrawSpriteImage](https://elite.bbcelite.com/nes/bank_6/subroutine/drawspriteimage.html) routine:

![The Save and Load screen in NES Elite](https://elite.bbcelite.com/images/nes/general/save_and_load.png) 

						The brackets and position markers on this screen are also sprites.

Sprites are also used in the following places:

- The square crosshair reticles on the system charts are shown using sprites, as are the systems on the Short-range Chart:
								![The Short-range Chart in NES Elite](/images/nes/general/short_range_chart.png)  
- The Inventory icon on the icon bar in the Market Prices screen is overlaid onto the icon bar using a sprite - that's the button under the pink icon bar pointer in the following shot:
								![The Lave market prices screen in NES Elite](/images/nes/general/market_lave.png)  

Incidentally, sprite patterns only ever come from pattern table 0 in Elite. Specifically, bit 3 of PPU_CTRL is only ever clear, and this maps the sprite pattern table to $0000 in the PPU, for pattern table 0.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
a                    e     ff
                                      b       e     ff       c
                      ff    g            ki      a      hj
                      ff      e               l  mm  l
                h       n n       i
              j                     k
            b         oo              c
                        ppp
                         d
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/sprite_usage_in_nes_elite.html](https://elite.bbcelite.com/deep_dives/sprite_usage_in_nes_elite.html)*

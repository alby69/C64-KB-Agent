---
title: Displaying two-layer images
source_url: https://elite.bbcelite.com/deep_dives/displaying_two-layer_images.html
category: source-code
topics:
- basic
- assembly
- sprite programming
difficulty: intermediate
language: mixed
hardware:
- KERNAL
- SID
- CIA
- VIC-II
related:
- sid-registers
- sound-programming
- vic-ii-registers
- joystick-reading
- keyboard-handling
- kernal-routines
- memory-map
- music-player
- sprite-programming
- raster-interrupts
- cia-registers
scraped_at: '2026-07-20'
---

# Displaying two-layer images

## The beautiful pixel art of the commander and system images

Of all the extra graphical touches that the authors added to the NES version of Elite, the most beautiful are the colourful system images from the Data on System screen. Here, for example, are the stunning green rings around Reorte:

![The Data on System view in NES Elite](https://elite.bbcelite.com/images/nes/general/data_on_reorte.png) 

						And here's the famous purple vista of everybody's favourite short-hop destination, Diso:

![The Data on System view in NES Elite](https://elite.bbcelite.com/images/nes/general/data_on_diso.png) 

						As well as the glorious system images, the Status Mode screen has a slightly less beautiful but no less entertaining rendering of the current commander, whose appearance changes as you make money and progress through the ranks. Here we are at the start of the game, as a poor pilot with a Harmless rank:

![The default commander in NES Elite](https://elite.bbcelite.com/images/nes/commander/default_commander.png) 

						And here we are at the end-game, with pots of money and an Elite rating:

![The maximum commander in NES Elite](https://elite.bbcelite.com/images/nes/commander/max_commander.png) 

						Let's see how these colourful images are displayed, and take a look at the whole range of system and commander images.

## Two-layer composition

													 ---------------------

						If you look closely at these images, they appear to have more colours than the NES screen supports. On the NES, each 2x2-tile part of the screen has the same palette applied to it, as defined in the attribute table, so the same four colours apply to each 16x16-pixel block. These colours have to include the background colour, which is defined as black in Elite, so NES images should only have three additional colours in each 16x16-pixel block.

But look at this rather lovely example of a system image:

![An example system image in NES Elite](https://elite.bbcelite.com/images/nes/two-layer_images/systemImage14_0.png) 

						At 64 pixels wide and 56 pixels high, this image is four attribute blocks wide and 3.5 blocks tall. Let's look at one of these attribute blocks, from the middle of the image:

![A zoomed-in example system image in NES Elite](https://elite.bbcelite.com/images/nes/two-layer_images/systemImage14_0_attribute_tile.png) 

						I can count six colours in this block: there are two shades of purple, a red, a white, a grey and a black. So what is going on here?

The answer is that the system and commander images have two layers. The background layer uses background tiles to fill in the greyscale elements, which in this example looks like this:

![An example background system image in NES Elite](https://elite.bbcelite.com/images/nes/two-layer_images/systemImage14_ram.png) 

						The foreground, meanwhile, is a sprite that's positioned over the top of the background. Sprites can have transparent pixels, and they also have their own palettes. In this example, the foreground sprite looks like this:

![An example foreground system image in NES Elite](https://elite.bbcelite.com/images/nes/two-layer_images/systemImage14_0_ppu.png) 

						If we want to change the palette of the system image, say to this:

![An example system image in NES Elite](https://elite.bbcelite.com/images/nes/two-layer_images/systemImage14_4.png) 

						then all we have to do is change the palette that is applied to the foreground sprite:

![An example foreground system image in NES Elite](https://elite.bbcelite.com/images/nes/two-layer_images/systemImage14_4_ppu.png) 

						We then draw our sprite over the top of the greyscale background, which always stays the same colour, as the colour of the background colours are defined by the view's attrribute table. Here are the view attributes for the Data on System screen, as defined by variable [viewAttributes10](https://elite.bbcelite.com/nes/bank_3/variable/viewattributes10.html), showing the colours available to each 2x2 block of tiles:

![The attributes for the Data on System view in NES Elite](https://elite.bbcelite.com/images/nes/understanding/data_on_lave_attr.png) 

						You can see the greyscale block on the right, which is where the system image goes.

The commander image is similar, except the image is split up into a background headshot and a colourful face. The headshot contains the backdrop, the clothing and some facial highlights, while the colourful face gets superimposed as a sprite. For example, this slightly scared-looking gentleman:

![An example commander image in NES Elite](https://elite.bbcelite.com/images/nes/two-layer_images/commanderImage5_0.png) 

						is made up of this background headshot image:

![An example background commander image in NES Elite](https://elite.bbcelite.com/images/nes/two-layer_images/headImage5_ram.png) 

						and this sprite-based face image:

![An example foreground commander image in NES Elite](https://elite.bbcelite.com/images/nes/two-layer_images/faceImage5_ppu.png) 

						In the commander's case the same palette is always used, and the only colour that changes is the backdrop, which gets set to blue when we're docked, or green, amber or red when we're in space (depending on how dangerous the situation is). However, there are various additional sprites that can be added, including left and right earrings and a medallion, which declare how rich we are, and dark glasses, which appear if our legal status is too far on the wrong side of the law. Here's the same pilot after he's made far too much money from trading in illegal goods:

![An example commander image with jewellery in NES Elite](https://elite.bbcelite.com/images/nes/two-layer_images/commander_with_jewellery.png) 

						## System colours and commander ranks

													 ----------------------------------

						The colour and design of each system image is set using the system seeds. The system seeds are used to generate all the data for each system, as described in the deep dives on the [galaxy and system seeds](https://elite.bbcelite.com/galaxy_and_system_seeds.html) and [generating system data](https://elite.bbcelite.com/generating_system_data.html). Not surprisingly, then, we use the same approach for choosing the system image.

System images are created by the [GetSystemImage](https://elite.bbcelite.com/nes/bank_5/subroutine/getsystemimage.html) routine. This calls the [GetSystemBack](https://elite.bbcelite.com/nes/bank_5/subroutine/getsystemback.html) routine to choose the style of image and unpack the grey background into the pattern buffers. It then unpacks the foreground patterns directly into the PPU's VRAM, ready for the latter to be assigned to the relevant sprites.

The style of the image is chosen by EOR'ing the values of the s0_hi, s1_hi and s2_hi seeds, extracting the low nibble and reducing it to fit into the range 0 to 14. We then use this to pick an image from [systemImage0](https://elite.bbcelite.com/nes/bank_5/variable/systemimage0.html) to [systemImage14](https://elite.bbcelite.com/nes/bank_5/variable/systemimage14.html).

The foreground sprite of the system image always uses sprite palette 1. The colours in this palette are defined in the [GetViewPalettes](https://elite.bbcelite.com/nes/bank_3/subroutine/getviewpalettes.html) routine, which calculates a number between 0 and 7 by EOR'ing the s0_lo, s2_hi and s1_lo seeds for the current system, shifting the result right by two places and flipping bits 2 and 3.

The results can be seen in the following image, which shows every variation of every system image that you'll come across in-game:

![All system images in NES Elite](https://elite.bbcelite.com/images/nes/two-layer_images/all_system_images.png) 

						If you want to see what all the individual system images look like, check out the system images folder in the [accompanying repository](https://github.com/markmoxon/elite-source-code-nes/tree/main/1-source-files/images/system-images/pngs). You can also find Python scripts that implement the [unpacking process](https://github.com/markmoxon/elite-source-code-nes/blob/main/2-build-files/unpack-data.py) and [combine the results](https://github.com/markmoxon/elite-source-code-nes/blob/main/2-build-files/combine-images.py) into image files.

## Commander ranks

													 ---------------

						The commander images shown on the Status Mode screen are based on combat rank, cash level and legal status. The style of headshot is calculated in the [GetHeadshotType](https://elite.bbcelite.com/nes/bank_4/subroutine/getheadshottype.html) routine, using a formula that gives the lower rank images more variation, specifically when it comes to reacting to danger.

It works like this. We take the current combat rank in TALLY(1 0) and reduce it to a value of 0 for Harmless to 8 for Elite (see the deep dive on [combat rank](https://elite.bbcelite.com/combat_rank.html) for more about the TALLY variable). We then calculate another value based on the ship's condition, to give 0 for docked and green conditions, 1 for yellow and 2 for red. We then calculate following index value:

3 * rank + condition

This is used as an index into the [headShotsByRank](https://elite.bbcelite.com/nes/bank_4/variable/headshotsbyrank.html) table to fetch the final commander image number to display, which is a value from 0 to 13 that corresponds to the [faceImage0](https://elite.bbcelite.com/nes/bank_4/variable/faceimage0.html) to [faceImage13](https://elite.bbcelite.com/nes/bank_4/variable/faceimage13.html) and [headImage0](https://elite.bbcelite.com/nes/bank_4/variable/headimage0.html) to [headImage13](https://elite.bbcelite.com/nes/bank_4/variable/headimage13.html) images.

The headShotsByRank is designed so that the ship's condition makes lower-rank commanders appear scared in dangerous conditions. In the following, the top row shows a Harmless commander reacting to danger, with the status condition going from green to yellow to red as we go from left to right. The middle row shows a Mostly Harmless pilot, while the bottom row is a commander with combat rank Poor:

![Scared commander images in NES Elite](https://elite.bbcelite.com/images/nes/two-layer_images/scared_commanders.png) 

						As you can see, by the time we get to Poor a yellow condition doesn't change our expression at all, and even a red condition only gets faintly pursed lips and slightly raised eyebrows. By the time we get to Average and above, danger doesn't faze our commander in any way at all.

On top of the commander face and headshot, the [GetHeadshotType](https://elite.bbcelite.com/nes/bank_4/subroutine/getheadshottype.html) routine adds various bits of jewellery to our commander, depending on our cash levels and legal status. These are displayed using sprites, one for each embellishment, with the patterns coming from the packed image data at [glassesImage](https://elite.bbcelite.com/nes/bank_4/variable/glassesimage.html). They are as follows:

- If we have more than 1,024.0 CR, we gain an earring in the left ear, courtesy of the [DrawLeftEarring](https://elite.bbcelite.com/nes/bank_6/subroutine/drawleftearring.html)routine.
- If we have more than 2,022.4 CR, we also get an earring in the right ear, put there by the [DrawRightEarring](https://elite.bbcelite.com/nes/bank_6/subroutine/drawrightearring.html)routine.
- If we have more than 1,002,700.8 CR, we also get a fancy medallion, via the [DrawMedallion](https://elite.bbcelite.com/nes/bank_6/subroutine/drawmedallion.html)routine.
- If we are a fugitive (i.e. our legal status in FIST is 40 or more), we also get a cool pair of dark sunglasses from the [DrawGlasses](https://elite.bbcelite.com/nes/bank_6/subroutine/drawglasses.html)routine.

The results can be seen in the following image, which shows every variation of every commander image in the game. Lower ranks are at the top and higher ranks are lower down (specifically, image 0 is on the first row and image 13 is at the bottom). All the possible variations and embellishments for each rank are shown on the same row:

![All commander images in NES Elite](https://elite.bbcelite.com/images/nes/two-layer_images/all_commander_images.png) 

						If you want to see what all the individual commander images look like, check out the commander images folder in the [accompanying repository](https://github.com/markmoxon/elite-source-code-nes/tree/main/1-source-files/images/commander-images/pngs). You can also find Python scripts that implement the [unpacking process](https://github.com/markmoxon/elite-source-code-nes/blob/main/2-build-files/unpack-data.py) and [combine the results](https://github.com/markmoxon/elite-source-code-nes/blob/main/2-build-files/combine-images.py) into image files.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
3 * rank + condition
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/displaying_two-layer_images.html](https://elite.bbcelite.com/deep_dives/displaying_two-layer_images.html)*

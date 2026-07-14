---
title: Drawing explosion clouds
source_url: https://elite.bbcelite.com/deep_dives/drawing_explosion_clouds.html
category: deep-dive
topics:
- sprite programming
- assembly
difficulty: intermediate
language: mixed
hardware:
- CPU
- KERNAL
- VIC-II
related:
- raster-interrupts
- memory-map
- kernal-routines
- sprite-programming
- vic-ii-registers
scraped_at: '2026-07-14'
---

# Drawing explosion clouds

## Drawing and storing explosion clouds for ships whose luck runs out...

Explosions in Elite are really rather beautiful. Here's a video of a Mamba glittering in the dark as it meets its maker:

Like the ships, planet and sun, explosion clouds take a lot of maths to draw, and like them, we store the results of all this maths in a heap. For explosion clouds, which we draw in the [DOEXP](https://elite.bbcelite.com/cassette/main/subroutine/doexp.html) routine, we use the same ship line heap that we use for lines, but instead of storing lines on the ship line heap, we store details of the ship's explosion cloud on the heap. We can use the same space as a ship is either a wireframe or an explosion cloud, but is never both.

Note that the NES version is an exception, as it uses screen buffers for each frame and doesn't need to erase the screen contents, so it doesn't have any line heaps at all. See the deep dive on [drawing vector graphics using NES tiles](https://elite.bbcelite.com/drawing_vector_graphics_using_nes_tiles.html) for details. The cloud-drawing process is the same, though - it just doesn't need to store the results in a heap.

For the other 6502 versions of Elite, this is the heap structure:

| Byte # | Description | 
|---|---|
| #0 | Cloud size | 
| #1 | Cloud counter, starts at 18, increases by 4 each time we redraw the cloud, cloud expands until 128, shrinks until it overflows, then the cloud disappears | 
| #2 | Explosion count for this ship from the blueprint (i.e. the number of vertices used as origins for explosion clouds) | 
| #3 to #6 | Random seeds to pass to DORND2 at the start of the drawing process, so we can redraw the exact same cloud again | 
| #7 onwards | Coordinates of the visible vertices for the exploding ship, so we can generate clouds around them (or, specifically, if byte #2 is n, the first n of them) | 

The block above is set up when a ship explodes, in place of the ship lines themselves, as exploding ships don't have any lines any more.

The process for drawing explosion clouds is as follows:

- Redraw the existing explosion cloud, if there is one, to remove it from the screen
- Increase the cloud counter by 4 (it starts at 18 for new explosions)
- Set the cloud size to cloud counter / distance, so the further away the cloud, the smaller it is, and as the cloud counter ticks onward, the cloud expands
- Use the cloud counter to determine the number of particles in each vertex cloud, so the cloud has more particles as the counter increases, until it gets past 128, after which the number decreases
- For the first n vertices (where n is the explosion count from the ship's blueprint), do the following:
								- Fetch the vertex coordinates from the XX3 workspace into the ship line heap
- Seed the random number generator with four bytes from the ship line heap
- Plot randomly placed points within the radius of the vertex, with the number of particles set above, with random sizes
 

As well as explosion clouds, the NES version draws an explosion burst, using colourful sprites to give the initial explosion a burst of yellow-orange colour in the otherwise monochrome space view. See the deep dive on [sprite usage in NES Elite](https://elite.bbcelite.com/sprite_usage_in_nes_elite.html) for details.

---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/drawing_explosion_clouds.html](https://elite.bbcelite.com/deep_dives/drawing_explosion_clouds.html)*

---
title: Drawing ships
source_url: https://elite.bbcelite.com/deep_dives/drawing_ships.html
category: source-code
topics:
- assembly
difficulty: beginner
language: mixed
hardware:
- SID
- KERNAL
- CIA
related:
- keyboard-handling
- music-player
- sound-programming
- joystick-reading
- memory-map
- kernal-routines
- sid-registers
- cia-registers
scraped_at: '2026-07-14'
---

# Drawing ships

## The main routine for drawing 3D wireframe ships in space

The ship-drawing routine at [LL9](https://elite.bbcelite.com/cassette/main/subroutine/ll9_part_1_of_12.html) is one of the most celebrated aspects of Elite. The 3D graphics are ground-breaking and breath-taking in equal measure, at least as far as 8-bit home computers are concerned, and even today the way that the ships and space stations move through space is impressive. Without its slick 3D graphics engine, Elite wouldn't have been nearly as immersive, and without its immersion, it just wouldn't have been Elite.

The beauty of Elite's ship-drawing routine is apparent from the very start, with the iconic rotating Cobra Mk III on the title screen:

![The title screen in the BBC Micro version of Elite](https://elite.bbcelite.com/images/cassette/title.png) 

						It doesn't take a rocket scientist to work out that Elite must have some pretty clever optimisations at the heart of its graphics routines, and this is indeed the case. Elite's 3D objects are stored in a way that makes visibility calculations relatively quick, so we can work out which parts of the ship need to be converted into screen coordinates and drawn, and (more to the point) which ones don't.

Let's look at visibility distances before moving on to the details of the ship-drawing process.

## Visibility distances

													 --------------------

						Ships are stored as collections of vertices (i.e. points in space) as you would imagine, and they also come bundled with data on all the edges in the shape, plus data on each face in the model. In addition, each of these vertices, edges and faces comes with its own "visibility distance" figure that enables us to quickly work out which of them are close enough to be worth considering, so we only spend time calculating what we need to draw, discarding anything we don't need. The whole process is aimed at narrowing down what we need to do, as quickly and easily as possible.

These are the visibility rules for the various components of the ship:

- If the ship is further away than the ship visibility distance in ship byte #13, we draw it as a dot and skip all the wireframe calculations
- A face is visible if one of these is true:
								- The ship is further away than that face's visibility distance
- The ship is closer than the face's visibility distance and the face is turned towards us
 
- A vertex is visible if at least one face associated with that vertex is visible
- An edge is visible if at least one face associated with that edge is visible

These rules get applied as we work our way through all the faces, vertices and edges in the process below.

## The ship line heap

													 ------------------

						Just as with the planet and sun, we need a way to remove ships from the screen quickly, so it's no surprise that each ship has its own storage heap for doing just that - the ship line heap. (Note that the NES version is an exception, as it uses screen buffers for each frame and doesn't need to erase the screen contents, so it doesn't have any line heaps at all. See the deep dive on [drawing vector graphics using NES tiles](https://elite.bbcelite.com/drawing_vector_graphics_using_nes_tiles.html) for details.)

Each ship has its own heap as part of the main ship line heap, which descends from location WP. The ship line heap is very simple - it contains sets of four coordinates, each of which describes a line in that ship's screen depiction. To draw the ship we simply work through the heap, drawing each line, and to remove the ship from the screen, we repeat the process.

The first byte of the heap contains the total number of bytes in the heap. Each line is stored as four bytes - X1, Y1, X2, Y2 - which describe the start and end screen coordinates for that line.

When a ship is added to our local bubble of universe, a ship line heap is reserved for that ship, with the heap size given in byte #5 of the ship's blueprint. This gives the maximum heap size needed for plotting ship, which is:

1 + 4 * max. no of visible edges

as there are four bytes needed for each line, plus 1 for the size byte at the start. So for the Sidewinder there are never more than 15 edges visible, so there will never be more than 15 lines on the ship line heap, so the maximum heap size is 1 + 4 * 15 = 61 bytes.

## The drawing workflow

													 --------------------

						The following process summarises the different steps in the LL9 routine. The part numbers match the breakdown of the source code, so you can refer to the code as you go.

- If the ship is a planet or sun, jump to PLANET to draw it
- If the ship has just been killed but isn't yet exploding, initialise a new explosion cloud
- If the ship is behind us, then it isn't visible, so remove it from the screen (by calling part 11 below to redraw it using EOR logic) and we're done

- If the ship is outside of our field of view, remove it from the screen and we're done
- If the ship is a long way away, jump to SHPPT to remove it from the screen and redraw it as a dot
- Flag the ship's laser vertex in the XX3 buffer, so we can check it in part 9 when processing laser fire
- Calculate the ship's distance from us, reduced to a value in the range 0-31 so it's testable against visibility distances
- If the ship is further away than the ship blueprint's visibility distance, jump to SHPPT to remove it from the screen and redraw it as a dot

- Fetch the ship's orientation vectors and normalise them
- Fetch the ship's x, y and z coordinates in space

- If the ship is exploding, set all the faces to be visible and skip down to part 6

- Work out the scale factor for the face normals so we can make them as big as possible while not overflowing, incorporating the scale factor from the blueprint
- Process the ship's faces and work out if they're visible, as follows:
								- If the ship is further away than a face's visibility distance, mark it as visible (this is the opposite to the other visibility distance tests)
- Otherwise work out if the face is pointing towards us or away from us using the dot product (see the deep dive on [back-face culling](https://elite.bbcelite.com/back-face_culling.html))
 

- Process the ship's vertices and work out which ones are visible:
								- If the ship is further away than the vertex's visibility distance, it is not visible
- If at least one face associated with this vertex is visible, the vertex is visible
 
- For visible vertices only:
								- Calculate the space coordinates of that vertex (see the deep dive on [calculating vertex coordinates](https://elite.bbcelite.com/calculating_vertex_coordinates.html)), starting the calculation in part 6...
 
- Calculate the space coordinates of that vertex (see the deep dive on 

- ...and finishing it in part 7, before moving on to part 8...

- ...to convert the visible vertex's space coordinates into screen coordinates

- If the ship is exploding, jump to DOEXP to display the explosion cloud
- Remove the ship from the screen
- If the ship is firing at us and its laser vertex (which we tagged in part 2) is visible, then calculate the laser beam line coordinates and add them to the ship line heap

- Process the ship's edges and work out which ones are visible:
								- If the ship is further away than the edge's visibility distance, it is not visible
- If at least one face associated with this edge is visible, the edge is visible
 

- For visible edges, add this edge to the ship line heap (i.e. add the screen coordinates of the start and end vertices)

- Draw the lines in the ship line heap, which draws the ship on screen (or removes it, if the ship is already on screen)

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
1 + 4 * max. no of visible edges
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/drawing_ships.html](https://elite.bbcelite.com/deep_dives/drawing_ships.html)*

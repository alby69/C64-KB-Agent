---
title: List of all subroutines in the Commodore 64 version of Elite
source_url: https://elite.bbcelite.com/c64/indexes/subroutines.html
category: source-code
topics:
- raster interrupts
- memory management
- basic
- graphics
- sprite programming
- assembly
- input handling
- sound generation
difficulty: advanced
language: mixed
hardware:
- CIA
- SID
- CPU
- VIC-II
- KERNAL
- BASIC ROM
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

# List of all subroutines in the Commodore 64 version of Elite

This index contains every subroutine and entry point that appears in the source code for the Commodore 64 version of Elite, grouped by category. An entry points is a label within a subroutine that is called from outside the subroutine, which typically implements a subset or variation of the functionality of the parent subroutine.

- [Charts](https://elite.bbcelite.com#charts)
- [Copy protection](https://elite.bbcelite.com#copy-protection)
- [Dashboard](https://elite.bbcelite.com#dashboard)
- [Drawing circles](https://elite.bbcelite.com#drawing-circles)
- [Drawing lines](https://elite.bbcelite.com#drawing-lines)
- [Drawing pixels](https://elite.bbcelite.com#drawing-pixels)
- [Drawing planets](https://elite.bbcelite.com#drawing-planets)
- [Drawing ships](https://elite.bbcelite.com#drawing-ships)
- [Drawing suns](https://elite.bbcelite.com#drawing-suns)
- [Drawing the screen](https://elite.bbcelite.com#drawing-the-screen)
- [Equipment](https://elite.bbcelite.com#equipment)
- [Flight](https://elite.bbcelite.com#flight)
- [Keyboard](https://elite.bbcelite.com#keyboard)
- [Loader](https://elite.bbcelite.com#loader)
- [Main loop](https://elite.bbcelite.com#main-loop)
- [Market](https://elite.bbcelite.com#market)
- [Maths (Arithmetic)](https://elite.bbcelite.com#maths-arithmetic)
- [Maths (Geometry)](https://elite.bbcelite.com#maths-geometry)
- [Missions](https://elite.bbcelite.com#missions)
- [Moving](https://elite.bbcelite.com#moving)
- [Save and load](https://elite.bbcelite.com#save-and-load)
- [Sound](https://elite.bbcelite.com#sound)
- [Stardust](https://elite.bbcelite.com#stardust)
- [Start and end](https://elite.bbcelite.com#start-and-end)
- [Status](https://elite.bbcelite.com#status)
- [Tactics](https://elite.bbcelite.com#tactics)
- [Text](https://elite.bbcelite.com#text)
- [Tube](https://elite.bbcelite.com#tube)
- [Universe](https://elite.bbcelite.com#universe)
- [Utility routines](https://elite.bbcelite.com#utility-routines)

| ## Charts | |
| [hm](https://elite.bbcelite.com/c64/main/subroutine/hm.html) | Select the closest system and redraw the chart crosshairs | 
| [HME2](https://elite.bbcelite.com/c64/main/subroutine/hme2.html) | Search the galaxy for a system | 
| [TT103](https://elite.bbcelite.com/c64/main/subroutine/tt103.html) | Draw a small set of crosshairs on a chart | 
| [TT105](https://elite.bbcelite.com/c64/main/subroutine/tt105.html) | Draw crosshairs on the Short-range Chart, with clipping | 
| [TT114](https://elite.bbcelite.com/c64/main/subroutine/tt114.html) | Display either the Long-range or Short-range Chart | 
| [TT123](https://elite.bbcelite.com/c64/main/subroutine/tt123.html) | Move galactic coordinates by a signed delta | 
| [TT16](https://elite.bbcelite.com/c64/main/subroutine/tt16.html) | Move the crosshairs on a chart | 
| [TT180](https://elite.bbcelite.com/c64/main/subroutine/tt123.html) | Contains an RTS | 
| [TT22](https://elite.bbcelite.com/c64/main/subroutine/tt22.html) | Show the Long-range Chart | 
| [TT23](https://elite.bbcelite.com/c64/main/subroutine/tt23.html) | Show the Short-range Chart | 
| ## Copy protection | |
| [Checksum](https://elite.bbcelite.com/c64/main/subroutine/checksum.html) | Checksum the code from $1000 to $9FFF and check against S%-1 | 
| ## Dashboard | |
| [ABORT](https://elite.bbcelite.com/c64/main/subroutine/abort.html) | Unarm missiles and update the dashboard indicators | 
| [ABORT2](https://elite.bbcelite.com/c64/main/subroutine/abort2.html) | Set/unset the lock target for a missile and update the dashboard | 
| [BUMP2](https://elite.bbcelite.com/c64/main/subroutine/bump2.html) | Bump up the value of the pitch or roll dashboard indicator | 
| [cntr](https://elite.bbcelite.com/c64/main/subroutine/cntr.html) | Apply damping to the pitch or roll dashboard indicator | 
| [COMPAS](https://elite.bbcelite.com/c64/main/subroutine/compas.html) | Update the compass | 
| [DIALS (Part 1 of 4)](https://elite.bbcelite.com/c64/main/subroutine/dials_part_1_of_4.html) | Update the dashboard: speed indicator | 
| [DIALS (Part 2 of 4)](https://elite.bbcelite.com/c64/main/subroutine/dials_part_2_of_4.html) | Update the dashboard: pitch and roll indicators | 
| [DIALS (Part 3 of 4)](https://elite.bbcelite.com/c64/main/subroutine/dials_part_3_of_4.html) | Update the dashboard: four energy banks | 
| [DIALS (Part 4 of 4)](https://elite.bbcelite.com/c64/main/subroutine/dials_part_4_of_4.html) | Update the dashboard: shields, fuel, laser & cabin temp, altitude | 
| [DIL](https://elite.bbcelite.com/c64/main/subroutine/dilx.html) | The range of the indicator is 0-16 (for the energy banks) | 
| [DIL-1](https://elite.bbcelite.com/c64/main/subroutine/dilx.html) | The range of the indicator is 0-32 (for the speed indicator) | 
| [DIL2](https://elite.bbcelite.com/c64/main/subroutine/dil2.html) | Update the roll or pitch indicator on the dashboard | 
| [DILX](https://elite.bbcelite.com/c64/main/subroutine/dilx.html) | Update a bar-based indicator on the dashboard | 
| [DILX+2](https://elite.bbcelite.com/c64/main/subroutine/dilx.html) | The range of the indicator is 0-64 (for the fuel indicator) | 
| [djd1](https://elite.bbcelite.com/c64/main/subroutine/redu2.html) | Auto-recentre the value in X, if keyboard auto-recentre is configured | 
| [DOT](https://elite.bbcelite.com/c64/main/subroutine/dot.html) | Draw a dash on the compass | 
| [ECBLB](https://elite.bbcelite.com/c64/main/subroutine/ecblb.html) | Light up the E.C.M. indicator bulb ("E") on the dashboard | 
| [ECBLB2](https://elite.bbcelite.com/c64/main/subroutine/ecblb2.html) | Start up the E.C.M. (light up the indicator, start the countdown and make the E.C.M. sound) | 
| [ECMOF](https://elite.bbcelite.com/c64/main/subroutine/ecmof.html) | Switch off the E.C.M. and turn off the dashboard bulb | 
| [MSBAR](https://elite.bbcelite.com/c64/main/subroutine/msbar.html) | Draw a specific indicator in the dashboard's missile bar | 
| [msblob](https://elite.bbcelite.com/c64/main/subroutine/msblob.html) | Display the dashboard's missile indicators in green | 
| [PZW](https://elite.bbcelite.com/c64/main/subroutine/pzw.html) | Fetch the current dashboard colours, to support flashing | 
| [RE2+2](https://elite.bbcelite.com/c64/main/subroutine/bump2.html) | Restore A from T and return from the subroutine | 
| [REDU2](https://elite.bbcelite.com/c64/main/subroutine/redu2.html) | Reduce the value of the pitch or roll dashboard indicator | 
| [SCAN](https://elite.bbcelite.com/c64/main/subroutine/scan.html) | Display the current ship on the scanner | 
| [SP1](https://elite.bbcelite.com/c64/main/subroutine/sp1.html) | Draw the space station on the compass | 
| [SP2](https://elite.bbcelite.com/c64/main/subroutine/sp2.html) | Draw a dot on the compass, given the planet/station vector | 
| [SPBLB](https://elite.bbcelite.com/c64/main/subroutine/spblb.html) | Light up the space station indicator ("S") on the dashboard | 
| [WPSHPS](https://elite.bbcelite.com/c64/main/subroutine/wpshps.html) | Clear the scanner, reset the ball line and sun line heaps | 
| ## Drawing circles | |
| [BLINE](https://elite.bbcelite.com/c64/main/subroutine/bline.html) | Draw a circle segment and add it to the ball line heap | 
| [CHKON](https://elite.bbcelite.com/c64/main/subroutine/chkon.html) | Check whether any part of a circle appears on the extended screen | 
| [CIRCLE](https://elite.bbcelite.com/c64/main/subroutine/circle.html) | Draw a circle for the planet | 
| [CIRCLE2](https://elite.bbcelite.com/c64/main/subroutine/circle2.html) | Draw a circle (for the planet or chart) | 
| [DOHFX](https://elite.bbcelite.com/c64/main/subroutine/dohfx.html) | Implement the #DOHFX <flag> command (update the hyperspace effect flag) | 
| [HFS1](https://elite.bbcelite.com/c64/main/subroutine/hfs2.html) | Don't clear the screen, and draw 8 concentric rings with the step size in STP | 
| [HFS2](https://elite.bbcelite.com/c64/main/subroutine/hfs2.html) | Draw the launch or hyperspace tunnel | 
| [LAUN](https://elite.bbcelite.com/c64/main/subroutine/laun.html) | Make the launch sound and draw the launch tunnel | 
| [LL164](https://elite.bbcelite.com/c64/main/subroutine/ll164.html) | Make the hyperspace sound and draw the hyperspace tunnel | 
| [TT128](https://elite.bbcelite.com/c64/main/subroutine/tt128.html) | Draw a circle on a chart | 
| [TT14](https://elite.bbcelite.com/c64/main/subroutine/tt14.html) | Draw a circle with crosshairs on a chart | 
| ## Drawing lines | |
| [EDGES](https://elite.bbcelite.com/c64/main/subroutine/edges.html) | Draw a horizontal line given a centre and a half-width | 
| [HL6](https://elite.bbcelite.com/c64/main/subroutine/loin_part_7_of_7.html) | Contains an RTS | 
| [HLOIN](https://elite.bbcelite.com/c64/main/subroutine/hloin.html) | Draw a horizontal line from (X1, Y1) to (X2, Y1) | 
| [HLOIN2](https://elite.bbcelite.com/c64/main/subroutine/hloin2.html) | Remove a line from the sun line heap and draw it on-screen | 
| [LASLI](https://elite.bbcelite.com/c64/main/subroutine/lasli.html) | Draw the laser lines for when we fire our lasers | 
| [LASLI-1](https://elite.bbcelite.com/c64/main/subroutine/lasli.html) | Contains an RTS | 
| [LASLI2](https://elite.bbcelite.com/c64/main/subroutine/lasli.html) | Just draw the current laser lines without moving the centre point, draining energy or heating up. This has the effect of removing the lines from the screen | 
| [LL118](https://elite.bbcelite.com/c64/main/subroutine/ll118.html) | Move a point along a line until it is on-screen | 
| [LL118-1](https://elite.bbcelite.com/c64/main/subroutine/ll118.html) | Contains an RTS | 
| [LL145 (Part 1 of 4)](https://elite.bbcelite.com/c64/main/subroutine/ll145_part_1_of_4.html) | Clip line: Work out which end-points are on-screen, if any | 
| [LL145 (Part 2 of 4)](https://elite.bbcelite.com/c64/main/subroutine/ll145_part_2_of_4.html) | Clip line: Work out if any part of the line is on-screen | 
| [LL145 (Part 3 of 4)](https://elite.bbcelite.com/c64/main/subroutine/ll145_part_3_of_4.html) | Clip line: Calculate the line's gradient | 
| [LL145 (Part 4 of 4)](https://elite.bbcelite.com/c64/main/subroutine/ll145_part_4_of_4.html) | Clip line: Call the routine in LL188 to do the actual clipping | 
| [LL147](https://elite.bbcelite.com/c64/main/subroutine/ll145_part_1_of_4.html) | Don't initialise the values in SWAP or A | 
| [LL30](https://elite.bbcelite.com/c64/main/subroutine/loin_part_1_of_7.html) | LL30 is a synonym for LOIN and draws a line from (X1, Y1) to (X2, Y2) | 
| [LOIN (Part 1 of 7)](https://elite.bbcelite.com/c64/main/subroutine/loin_part_1_of_7.html) | Draw a line: Calculate the line gradient in the form of deltas | 
| [LOIN (Part 2 of 7)](https://elite.bbcelite.com/c64/main/subroutine/loin_part_2_of_7.html) | Draw a line: Line has a shallow gradient, step right along x-axis | 
| [LOIN (Part 3 of 7)](https://elite.bbcelite.com/c64/main/subroutine/loin_part_3_of_7.html) | Draw a shallow line going right and up or left and down | 
| [LOIN (Part 4 of 7)](https://elite.bbcelite.com/c64/main/subroutine/loin_part_4_of_7.html) | Draw a shallow line going right and down or left and up | 
| [LOIN (Part 5 of 7)](https://elite.bbcelite.com/c64/main/subroutine/loin_part_5_of_7.html) | Draw a line: Line has a steep gradient, step up along y-axis | 
| [LOIN (Part 6 of 7)](https://elite.bbcelite.com/c64/main/subroutine/loin_part_6_of_7.html) | Draw a steep line going up and left or down and right | 
| [LOIN (Part 7 of 7)](https://elite.bbcelite.com/c64/main/subroutine/loin_part_7_of_7.html) | Draw a steep line going up and right or down and left | 
| [NLIN](https://elite.bbcelite.com/c64/main/subroutine/nlin.html) | Draw a horizontal line at pixel row 23 to box in a title | 
| [NLIN2](https://elite.bbcelite.com/c64/main/subroutine/nlin2.html) | Draw a screen-wide horizontal line at the pixel row in A | 
| [NLIN3](https://elite.bbcelite.com/c64/main/subroutine/nlin3.html) | Print a title and draw a horizontal line at row 19 to box it in | 
| [NLIN4](https://elite.bbcelite.com/c64/main/subroutine/nlin4.html) | Draw a horizontal line at pixel row 19 to box in a title | 
| [TT15](https://elite.bbcelite.com/c64/main/subroutine/tt15.html) | Draw a set of crosshairs | 
| ## Drawing pixels | |
| [CPIX2](https://elite.bbcelite.com/c64/main/subroutine/cpix2.html) | Draw a single-height dash on the dashboard | 
| [CPIX4](https://elite.bbcelite.com/c64/main/subroutine/cpix4.html) | Draw a double-height dot on the dashboard | 
| [PIXEL](https://elite.bbcelite.com/c64/main/subroutine/pixel.html) | Draw a one-pixel dot, two-pixel dash or four-pixel square | 
| [PIXEL2](https://elite.bbcelite.com/c64/main/subroutine/pixel2.html) | Draw a stardust particle relative to the screen centre | 
| [PX4](https://elite.bbcelite.com/c64/main/subroutine/pixel.html) | Contains an RTS | 
| ## Drawing planets | |
| [PL2](https://elite.bbcelite.com/c64/main/subroutine/pl2.html) | Remove the planet or sun from the screen | 
| [PL2-1](https://elite.bbcelite.com/c64/main/subroutine/pl2.html) | Contains an RTS | 
| [PL21](https://elite.bbcelite.com/c64/main/subroutine/pl21.html) | Return from a planet/sun-drawing routine with a failure flag | 
| [PL44](https://elite.bbcelite.com/c64/main/subroutine/pls6.html) | Clear the C flag and return from the subroutine | 
| [PL6](https://elite.bbcelite.com/c64/main/subroutine/pls6.html) | Contains an RTS | 
| [PL9 (Part 1 of 3)](https://elite.bbcelite.com/c64/main/subroutine/pl9_part_1_of_3.html) | Draw the planet, with either an equator and meridian, or a crater | 
| [PL9 (Part 2 of 3)](https://elite.bbcelite.com/c64/main/subroutine/pl9_part_2_of_3.html) | Draw the planet's equator and meridian | 
| [PL9 (Part 3 of 3)](https://elite.bbcelite.com/c64/main/subroutine/pl9_part_3_of_3.html) | Draw the planet's crater | 
| [PLANET](https://elite.bbcelite.com/c64/main/subroutine/planet.html) | Draw the planet or sun | 
| [PLS1](https://elite.bbcelite.com/c64/main/subroutine/pls1.html) | Calculate (Y A) = nosev_x / z | 
| [PLS2](https://elite.bbcelite.com/c64/main/subroutine/pls2.html) | Draw a half-ellipse | 
| [PLS22](https://elite.bbcelite.com/c64/main/subroutine/pls22.html) | Draw an ellipse or half-ellipse | 
| [PLS3](https://elite.bbcelite.com/c64/main/subroutine/pls3.html) | Calculate (Y A P) = 222 * roofv_x / z | 
| [PLS4](https://elite.bbcelite.com/c64/main/subroutine/pls4.html) | Calculate CNT2 = arctan(P / A) / 4 | 
| [PLS5](https://elite.bbcelite.com/c64/main/subroutine/pls5.html) | Calculate roofv_x / z and roofv_y / z | 
| [PLS6](https://elite.bbcelite.com/c64/main/subroutine/pls6.html) | Calculate (X K) = (A P+1 P) / (z_sign z_hi z_lo) | 
| [WP1](https://elite.bbcelite.com/c64/main/subroutine/wp1.html) | Reset the ball line heap | 
| [WPLS2](https://elite.bbcelite.com/c64/main/subroutine/wpls2.html) | Remove the planet from the screen | 
| ## Drawing ships | |
| [DOEXP](https://elite.bbcelite.com/c64/main/subroutine/doexp.html) | Draw an exploding ship | 
| [EE51](https://elite.bbcelite.com/c64/main/subroutine/ll9_part_1_of_12.html) | Remove the current ship from the screen, called from SHPPT before drawing the ship as a point | 
| [EXS1](https://elite.bbcelite.com/c64/main/subroutine/doexp.html) | Set (A X) = (A R) +/- random * cloud size | 
| [LL10-1](https://elite.bbcelite.com/c64/main/subroutine/ll9_part_2_of_12.html) | Contains an RTS | 
| [LL66](https://elite.bbcelite.com/c64/main/subroutine/ll9_part_8_of_12.html) | A re-entry point into the ship-drawing routine, used by the LL62 routine to store 128 - (U R) on the XX3 heap | 
| [LL70+1](https://elite.bbcelite.com/c64/main/subroutine/ll9_part_8_of_12.html) | Contains an RTS (as the first byte of an LDA instruction) | 
| [LL81+2](https://elite.bbcelite.com/c64/main/subroutine/ll9_part_11_of_12.html) | Draw the contents of the ship line heap, used to draw the ship as a dot from SHPPT | 
| [LL9 (Part 1 of 12)](https://elite.bbcelite.com/c64/main/subroutine/ll9_part_1_of_12.html) | Draw ship: Check if ship is exploding, check if ship is in front | 
| [LL9 (Part 2 of 12)](https://elite.bbcelite.com/c64/main/subroutine/ll9_part_2_of_12.html) | Draw ship: Check if ship is in field of view, close enough to draw | 
| [LL9 (Part 3 of 12)](https://elite.bbcelite.com/c64/main/subroutine/ll9_part_3_of_12.html) | Draw ship: Set up orientation vector, ship coordinate variables | 
| [LL9 (Part 4 of 12)](https://elite.bbcelite.com/c64/main/subroutine/ll9_part_4_of_12.html) | Draw ship: Set visibility for exploding ship (all faces visible) | 
| [LL9 (Part 5 of 12)](https://elite.bbcelite.com/c64/main/subroutine/ll9_part_5_of_12.html) | Draw ship: Calculate the visibility of each of the ship's faces | 
| [LL9 (Part 6 of 12)](https://elite.bbcelite.com/c64/main/subroutine/ll9_part_6_of_12.html) | Draw ship: Calculate the visibility of each of the ship's vertices | 
| [LL9 (Part 7 of 12)](https://elite.bbcelite.com/c64/main/subroutine/ll9_part_7_of_12.html) | Draw ship: Calculate the visibility of each of the ship's vertices | 
| [LL9 (Part 8 of 12)](https://elite.bbcelite.com/c64/main/subroutine/ll9_part_8_of_12.html) | Draw ship: Calculate the screen coordinates of visible vertices | 
| [LL9 (Part 9 of 12)](https://elite.bbcelite.com/c64/main/subroutine/ll9_part_9_of_12.html) | Draw ship: Draw laser beams if the ship is firing its laser at us | 
| [LL9 (Part 10 of 12)](https://elite.bbcelite.com/c64/main/subroutine/ll9_part_10_of_12.html) | Draw ship: Calculate the visibility of each of the ship's edges | 
| [LL9 (Part 11 of 12)](https://elite.bbcelite.com/c64/main/subroutine/ll9_part_11_of_12.html) | Draw ship: Add all visible edges to the ship line heap | 
| [LL9 (Part 12 of 12)](https://elite.bbcelite.com/c64/main/subroutine/ll9_part_12_of_12.html) | Draw ship: Draw all the visible edges from the ship line heap | 
| [PTCLS2](https://elite.bbcelite.com/c64/main/subroutine/ptcls2.html) | Draw the explosion along with an explosion sprite | 
| [SHPPT](https://elite.bbcelite.com/c64/main/subroutine/shppt.html) | Draw a distant ship as a point rather than a full wireframe | 
| ## Drawing suns | |
| [FLFLLS](https://elite.bbcelite.com/c64/main/subroutine/flflls.html) | Reset the sun line heap | 
| [RTS2](https://elite.bbcelite.com/c64/main/subroutine/sun_part_4_of_4.html) | Contains an RTS | 
| [SUN (Part 1 of 4)](https://elite.bbcelite.com/c64/main/subroutine/sun_part_1_of_4.html) | Draw the sun: Set up all the variables needed to draw the sun | 
| [SUN (Part 2 of 4)](https://elite.bbcelite.com/c64/main/subroutine/sun_part_2_of_4.html) | Draw the sun: Start from the bottom of the screen and erase the old sun line by line | 
| [SUN (Part 3 of 4)](https://elite.bbcelite.com/c64/main/subroutine/sun_part_3_of_4.html) | Draw the sun: Continue to move up the screen, drawing the new sun line by line | 
| [SUN (Part 4 of 4)](https://elite.bbcelite.com/c64/main/subroutine/sun_part_4_of_4.html) | Draw the sun: Continue to the top of the screen, erasing the old sun line by line | 
| [WPLS](https://elite.bbcelite.com/c64/main/subroutine/wpls.html) | Remove the sun from the screen | 
| [WPLS-1](https://elite.bbcelite.com/c64/main/subroutine/wpls.html) | Contains an RTS | 
| ## Drawing the screen | |
| [BLUEBAND](https://elite.bbcelite.com/c64/main/subroutine/blueband.html) | Clear two four-character borders along each side of the space view | 
| [BLUEBANDS](https://elite.bbcelite.com/c64/main/subroutine/bluebands.html) | Clear a four-character border along one side of the space view | 
| [BOMBOFF](https://elite.bbcelite.com/c64/main/subroutine/bomboff.html) | Switch off the energy bomb effect | 
| [BOX](https://elite.bbcelite.com/c64/main/subroutine/ttx66k.html) | Just draw the border box along the top and sides | 
| [BOX2](https://elite.bbcelite.com/c64/main/subroutine/box2.html) | Draw the left and right edges of the border box for the space view | 
| [BOXS](https://elite.bbcelite.com/c64/main/subroutine/boxs.html) | Draw a horizontal line across the screen at pixel y-coordinate X | 
| [BOXS2](https://elite.bbcelite.com/c64/main/subroutine/boxs2.html) | Draw a vertical line for the left or right border box edge | 
| [clss](https://elite.bbcelite.com/c64/main/subroutine/clss.html) | Clear the screen, move the text cursor to the top-left corner and jump back into the CHPR routine to print the next character | 
| [CLYNS](https://elite.bbcelite.com/c64/main/subroutine/clyns.html) | Clear the bottom three text rows of the space view | 
| [COMIRQ1](https://elite.bbcelite.com/c64/main/subroutine/comirq1.html) | The split screen and sound interrupt handler (the IRQ interrupt service hardware vector at $FFFE points here) | 
| [DET1](https://elite.bbcelite.com/c64/main/subroutine/det1.html) | Show or hide the dashboard (for when we die) | 
| [DOVDU19](https://elite.bbcelite.com/c64/main/subroutine/dovdu19.html) | Implement the #SETVDU19 <offset> command (change mode 1 palette) | 
| [TRADEMODE](https://elite.bbcelite.com/c64/main/subroutine/trademode.html) | Clear the screen and set up a trading screen | 
| [TT66](https://elite.bbcelite.com/c64/main/subroutine/tt66.html) | Clear the screen and set the current view type | 
| [TT66simp](https://elite.bbcelite.com/c64/main/subroutine/tt66simp.html) | Clear the whole screen inside the border box, and move the text cursor to the top-left corner | 
| [TTX66](https://elite.bbcelite.com/c64/main/subroutine/ttx66.html) | Clear the top part of the screen, draw a border box and configure the specified view | 
| [TTX66K](https://elite.bbcelite.com/c64/main/subroutine/ttx66k.html) | Clear the whole screen or just the space view (as appropriate), draw a border box, and if required, show the dashboard | 
| [wantdials](https://elite.bbcelite.com/c64/main/subroutine/wantdials.html) | Show the dashboard on-screen | 
| [WSCAN](https://elite.bbcelite.com/c64/main/subroutine/wscan.html) | Wait for the vertical sync | 
| [zonkscanners](https://elite.bbcelite.com/c64/main/subroutine/zonkscanners.html) | Hide all ships on the scanner | 
| ## Equipment | |
| [c](https://elite.bbcelite.com/c64/main/subroutine/prx.html) | Contains an RTS | 
| [eq](https://elite.bbcelite.com/c64/main/subroutine/eq.html) | Subtract the price of equipment from the cash pot | 
| [EQSHP](https://elite.bbcelite.com/c64/main/subroutine/eqshp.html) | Show the Equip Ship screen | 
| [err](https://elite.bbcelite.com/c64/main/subroutine/eqshp.html) | Beep, pause and go to the docking bay (i.e. show the Status Mode screen) | 
| [pres](https://elite.bbcelite.com/c64/main/subroutine/eqshp.html) | Given an item number A with the item name in recursive token Y, show an error to say that the item is already present, refund the cost of the item, and then beep and exit to the docking bay (i.e. show the Status Mode screen) | 
| [prx](https://elite.bbcelite.com/c64/main/subroutine/prx.html) | Return the price of a piece of equipment | 
| [prx-3](https://elite.bbcelite.com/c64/main/subroutine/prx.html) | Return the price of the item with number A - 1 | 
| [qv](https://elite.bbcelite.com/c64/main/subroutine/qv.html) | Print a menu of the four space views, for buying lasers | 
| [refund](https://elite.bbcelite.com/c64/main/subroutine/refund.html) | Install a new laser, processing a refund if applicable | 
| ## Flight | |
| [DCS1](https://elite.bbcelite.com/c64/main/subroutine/dcs1.html) | Calculate the vector from the ideal docking position to the ship | 
| [DENGY](https://elite.bbcelite.com/c64/main/subroutine/dengy.html) | Drain some energy from the energy banks | 
| [dockEd](https://elite.bbcelite.com/c64/main/subroutine/docked.html) | Print a message to say there is no hyperspacing allowed inside the station | 
| [DOCKIT](https://elite.bbcelite.com/c64/main/subroutine/dockit.html) | Apply docking manoeuvres to the ship in INWK | 
| [DOENTRY](https://elite.bbcelite.com/c64/main/subroutine/doentry.html) | Dock at the space station and work out any mission progression | 
| [ee3](https://elite.bbcelite.com/c64/main/subroutine/ee3.html) | Print the hyperspace countdown in the top-left of the screen | 
| [ESCAPE](https://elite.bbcelite.com/c64/main/subroutine/escape.html) | Launch our escape pod | 
| [Ghy](https://elite.bbcelite.com/c64/main/subroutine/ghy.html) | Perform a galactic hyperspace jump | 
| [hyp](https://elite.bbcelite.com/c64/main/subroutine/hyp.html) | Start the hyperspace process | 
| [LO2](https://elite.bbcelite.com/c64/main/subroutine/look1.html) | Contains an RTS | 
| [LOOK1](https://elite.bbcelite.com/c64/main/subroutine/look1.html) | Initialise the space view | 
| [me1](https://elite.bbcelite.com/c64/main/subroutine/me1.html) | Erase an old in-flight message and display a new one | 
| [me2](https://elite.bbcelite.com/c64/main/subroutine/me2.html) | Remove an in-flight message from the space view | 
| [mes9](https://elite.bbcelite.com/c64/main/subroutine/mes9.html) | Print a text token, possibly followed by " DESTROYED" | 
| [MESS](https://elite.bbcelite.com/c64/main/subroutine/mess.html) | Display an in-flight message | 
| [MJP](https://elite.bbcelite.com/c64/main/subroutine/mjp.html) | Process a mis-jump into witchspace | 
| [OOPS](https://elite.bbcelite.com/c64/main/subroutine/oops.html) | Take some damage | 
| [ou2](https://elite.bbcelite.com/c64/main/subroutine/ou2.html) | Display "E.C.M.SYSTEM DESTROYED" as an in-flight message | 
| [ou3](https://elite.bbcelite.com/c64/main/subroutine/ou3.html) | Display "FUEL SCOOPS DESTROYED" as an in-flight message | 
| [OUCH](https://elite.bbcelite.com/c64/main/subroutine/ouch.html) | Potentially lose cargo or equipment following damage | 
| [PLUT](https://elite.bbcelite.com/c64/main/subroutine/plut.html) | Flip the coordinate axes for the four different views | 
| [ptg](https://elite.bbcelite.com/c64/main/subroutine/mjp.html) | Called when the user manually forces a mis-jump | 
| [RTS111](https://elite.bbcelite.com/c64/main/subroutine/mjp.html) | Contains an RTS | 
| [SESCP](https://elite.bbcelite.com/c64/main/subroutine/sescp.html) | Spawn an escape pod from the current (parent) ship | 
| [SHD](https://elite.bbcelite.com/c64/main/subroutine/shd.html) | Charge a shield and drain some energy from the energy banks | 
| [SIGHT](https://elite.bbcelite.com/c64/main/subroutine/sight.html) | Draw the laser crosshairs | 
| [TT110](https://elite.bbcelite.com/c64/main/subroutine/tt110.html) | Launch from a station or show the front space view | 
| [TT147](https://elite.bbcelite.com/c64/main/subroutine/tt147.html) | Print an error when a system is out of hyperspace range | 
| [TT18](https://elite.bbcelite.com/c64/main/subroutine/tt18.html) | Try to initiate a jump into hyperspace | 
| [TTX110](https://elite.bbcelite.com/c64/main/subroutine/ttx110.html) | Set the current system to the nearest system and return to hyp | 
| [TTX111](https://elite.bbcelite.com/c64/main/subroutine/hyp.html) | Used to rejoin this routine from the call to TTX110 | 
| [WARP](https://elite.bbcelite.com/c64/main/subroutine/warp.html) | Perform an in-system jump | 
| [wW](https://elite.bbcelite.com/c64/main/subroutine/ww.html) | Start a hyperspace countdown | 
| [wW2](https://elite.bbcelite.com/c64/main/subroutine/ww.html) | Start the hyperspace countdown, starting the countdown from the value in A | 
| [zZ+1](https://elite.bbcelite.com/c64/main/subroutine/ghy.html) | Contains an RTS | 
| ## Keyboard | |
| [CTRL](https://elite.bbcelite.com/c64/main/subroutine/ctrl.html) | Scan the keyboard to see if CTRL is currently pressed | 
| [DK4](https://elite.bbcelite.com/c64/main/subroutine/dk4.html) | Scan for pause, configuration and secondary flight keys | 
| [DKJ1](https://elite.bbcelite.com/c64/main/subroutine/dkj1.html) | Read joystick and flight controls | 
| [DKS2](https://elite.bbcelite.com/c64/main/subroutine/dks2.html) | Read the joystick position | 
| [DKS3](https://elite.bbcelite.com/c64/main/subroutine/dks3.html) | Toggle a configuration setting and emit a beep | 
| [DKS4](https://elite.bbcelite.com/c64/main/subroutine/dks4.html) | Scan the keyboard to see if a specific key is being pressed | 
| [DKSANYKEY](https://elite.bbcelite.com/c64/main/subroutine/dksanykey.html) | An unused routine that scans a specific column in the keyboard matrix for a key press | 
| [DOKEY](https://elite.bbcelite.com/c64/main/subroutine/dokey.html) | Scan for the seven primary flight controls and apply the docking computer manoeuvring code | 
| [FLKB](https://elite.bbcelite.com/c64/main/subroutine/flkb.html) | Flush the keyboard buffer | 
| [FREEZE](https://elite.bbcelite.com/c64/main/subroutine/dk4.html) | Rejoin the pause routine after processing a screen save | 
| [out](https://elite.bbcelite.com/c64/main/subroutine/tt217.html) | Contains an RTS | 
| [PAUSE2](https://elite.bbcelite.com/c64/main/subroutine/pause2.html) | Wait until a key is pressed, ignoring any existing key press | 
| [RDKEY](https://elite.bbcelite.com/c64/main/subroutine/rdkey.html) | Scan the keyboard for key presses and the joystick, and update the key logger | 
| [t](https://elite.bbcelite.com/c64/main/subroutine/tt217.html) | As TT217 but don't preserve Y, set it to YSAV instead | 
| [T95](https://elite.bbcelite.com/c64/main/subroutine/tt102.html) | Print the distance to the selected system | 
| [TT102](https://elite.bbcelite.com/c64/main/subroutine/tt102.html) | Process function key, save key, hyperspace and chart key presses and update the hyperspace counter | 
| [TT17](https://elite.bbcelite.com/c64/main/subroutine/tt17.html) | Scan the keyboard for cursor key or joystick movement | 
| [TT214](https://elite.bbcelite.com/c64/main/subroutine/tt214.html) | Ask a question with a "Y/N?" prompt and return the response | 
| [TT217](https://elite.bbcelite.com/c64/main/subroutine/tt217.html) | Scan the keyboard until a key is pressed | 
| [U%](https://elite.bbcelite.com/c64/main/subroutine/u_per_cent.html) | Clear the key logger and reset a number of flight variables | 
| [YESNO](https://elite.bbcelite.com/c64/main/subroutine/yesno.html) | Wait until either "Y" or "N" is pressed | 
| [ZEKTRAN](https://elite.bbcelite.com/c64/main/subroutine/zektran.html) | Clear the key logger | 
| ## Loader | |
| [BEGIN](https://elite.bbcelite.com/c64/main/subroutine/begin.html) | Initialise the configuration variables and start the game | 
| [COLD](https://elite.bbcelite.com/c64/main/subroutine/cold.html) | Configure memory, set up interrupt handlers and configure the VIC-II, SID and CIA chips | 
| [CopyZeroPage (Disk Loader 2)](https://elite.bbcelite.com/c64/disk_loader_2/subroutine/copyzeropage.html) | Copy a page of data in a specified direction between zero page and the page at $CE00, omitting the first two bytes | 
| [DEEORS (Game Loader)](https://elite.bbcelite.com/c64/game_loader/subroutine/deeors.html) | Decrypt a multi-page block of memory | 
| [Elite GMA loader (Part 1 of 4) (Disk Loader 2)](https://elite.bbcelite.com/c64/disk_loader_2/subroutine/elite_gma_loader_part_1_of_4.html) | Skip past the table of track and sector numbers if present | 
| [Elite GMA loader (Part 2 of 4) (Disk Loader 2)](https://elite.bbcelite.com/c64/disk_loader_2/subroutine/elite_gma_loader_part_2_of_4.html) | Offer the option of a fast loader and run the disk protection code in the GMA3 file | 
| [Elite GMA loader (Part 3 of 4) (Disk Loader 2)](https://elite.bbcelite.com/c64/disk_loader_2/subroutine/elite_gma_loader_part_3_of_4.html) | Run the Elite loader in the GMA4 file | 
| [Elite GMA loader (Part 4 of 4) (Disk Loader 2)](https://elite.bbcelite.com/c64/disk_loader_2/subroutine/elite_gma_loader_part_4_of_4.html) | Load the GMA5 and GMA6 binaries and start the game | 
| [Elite loader (Part 1 of 7) (Game Loader)](https://elite.bbcelite.com/c64/game_loader/subroutine/elite_loader_part_1_of_7.html) | Unscramble the loader code and game data | 
| [Elite loader (Part 2 of 7) (Game Loader)](https://elite.bbcelite.com/c64/game_loader/subroutine/elite_loader_part_2_of_7.html) | Copy the game data to their correct locations | 
| [Elite loader (Part 3 of 7) (Game Loader)](https://elite.bbcelite.com/c64/game_loader/subroutine/elite_loader_part_3_of_7.html) | Configure the memory layout and the CIA chips | 
| [Elite loader (Part 4 of 7) (Game Loader)](https://elite.bbcelite.com/c64/game_loader/subroutine/elite_loader_part_4_of_7.html) | Configure the VIC-II for screen memory and sprites | 
| [Elite loader (Part 5 of 7) (Game Loader)](https://elite.bbcelite.com/c64/game_loader/subroutine/elite_loader_part_5_of_7.html) | Configure the screen bitmap and copy colour data into screen RAM | 
| [Elite loader (Part 6 of 7) (Game Loader)](https://elite.bbcelite.com/c64/game_loader/subroutine/elite_loader_part_6_of_7.html) | Copy colour data into colour RAM and configure more screen RAM | 
| [Elite loader (Part 7 of 7) (Game Loader)](https://elite.bbcelite.com/c64/game_loader/subroutine/elite_loader_part_7_of_7.html) | Set up the sprite pointers, make a copy of the dashboard bitmap in DSTORE% and copy the sprite definitions to SPRITELOC% | 
| [filename (Disk Loader 1)](https://elite.bbcelite.com/c64/disk_loader_1/subroutine/filename.html) | A wildcarded filename that matches the first GMA file on disk | 
| [load3 (Disk Loader 2)](https://elite.bbcelite.com/c64/disk_loader_2/subroutine/elite_gma_loader_part_3_of_4.html) | Jump to the entry point in elite-loader | 
| [LoadGMAFile (Disk Loader 2)](https://elite.bbcelite.com/c64/disk_loader_2/subroutine/loadgmafile.html) | Load a specific GMA file | 
| [LODATA (Game Loader)](https://elite.bbcelite.com/c64/game_loader/subroutine/lodata.html) | The binaries for recursive tokens and the game font | 
| [mvblock (Game Loader)](https://elite.bbcelite.com/c64/game_loader/subroutine/mvblock.html) | Copy a number of pages in memory | 
| [mvsm (Game Loader)](https://elite.bbcelite.com/c64/game_loader/subroutine/mvsm.html) | Copy 280 bytes in memory | 
| [NMIpissoff](https://elite.bbcelite.com/c64/main/subroutine/nmipissoff.html) | Acknowledge NMI interrupts and ignore them | 
| [OfferFastLoader (Disk Loader 2)](https://elite.bbcelite.com/c64/disk_loader_2/subroutine/offerfastloader.html) | Offer the option of using the fast loader, if we haven't already, and set up the fast loader if it is chosen | 
| [PrintString (Disk Loader 2)](https://elite.bbcelite.com/c64/disk_loader_2/subroutine/printstring.html) | Print the null-terminated string at offset X in loaderScreens | 
| [RelocateLoader (Disk Loader 1)](https://elite.bbcelite.com/c64/disk_loader_1/subroutine/relocateloader.html) | Load and run the GMA1 loader file | 
| [RunGMA (Disk Loader 1)](https://elite.bbcelite.com/c64/disk_loader_1/subroutine/rungma.html) | Load and run the GMA1 loader file | 
| [S%](https://elite.bbcelite.com/c64/main/subroutine/s_per_cent.html) | Checksum, decrypt and unscramble the main game code, and start the game | 
| [SetUpFastLoader (Disk Loader 2)](https://elite.bbcelite.com/c64/disk_loader_2/subroutine/setupfastloader.html) | Set up the fast loader so that calls to the Kernal's file functions use the fast loader routines instead | 
| [SetUpGMAFile (Disk Loader 2)](https://elite.bbcelite.com/c64/disk_loader_2/subroutine/setupgmafile.html) | Configure the filename parameters to load a specific GMA file | 
| [SHIPS (Game Loader)](https://elite.bbcelite.com/c64/game_loader/subroutine/ships.html) | The binaries for the ship blueprints | 
| [STARTUP](https://elite.bbcelite.com/c64/main/subroutine/startup.html) | Set the various vectors, interrupts and timers | 
| ## Main loop | |
| [FRCE](https://elite.bbcelite.com/c64/main/subroutine/main_game_loop_part_6_of_6.html) | The entry point for the main game loop if we want to jump straight to a specific screen, by pretending to "press" a key, in which case A contains the internal key number of the key we want to "press" | 
| [GOIN](https://elite.bbcelite.com/c64/main/subroutine/main_flight_loop_part_9_of_16.html) | We jump here from part 3 of the main flight loop if the docking computer is activated by pressing "C" | 
| [M%](https://elite.bbcelite.com/c64/main/subroutine/main_flight_loop_part_1_of_16.html) | The entry point for the main flight loop | 
| [Main flight loop (Part 1 of 16)](https://elite.bbcelite.com/c64/main/subroutine/main_flight_loop_part_1_of_16.html) | Seed the random number generator | 
| [Main flight loop (Part 2 of 16)](https://elite.bbcelite.com/c64/main/subroutine/main_flight_loop_part_2_of_16.html) | Calculate the alpha and beta angles from the current pitch and roll of our ship | 
| [Main flight loop (Part 3 of 16)](https://elite.bbcelite.com/c64/main/subroutine/main_flight_loop_part_3_of_16.html) | Scan for flight keys and process the results | 
| [Main flight loop (Part 4 of 16)](https://elite.bbcelite.com/c64/main/subroutine/main_flight_loop_part_4_of_16.html) | For each nearby ship: Copy the ship's data block from K% to the zero-page workspace at INWK | 
| [Main flight loop (Part 5 of 16)](https://elite.bbcelite.com/c64/main/subroutine/main_flight_loop_part_5_of_16.html) | For each nearby ship: If an energy bomb has been set off, potentially kill this ship | 
| [Main flight loop (Part 6 of 16)](https://elite.bbcelite.com/c64/main/subroutine/main_flight_loop_part_6_of_16.html) | For each nearby ship: Move the ship in space and copy the updated INWK data block back to K% | 
| [Main flight loop (Part 7 of 16)](https://elite.bbcelite.com/c64/main/subroutine/main_flight_loop_part_7_of_16.html) | For each nearby ship: Check whether we are docking, scooping or colliding with it | 
| [Main flight loop (Part 8 of 16)](https://elite.bbcelite.com/c64/main/subroutine/main_flight_loop_part_8_of_16.html) | For each nearby ship: Process us potentially scooping this item | 
| [Main flight loop (Part 9 of 16)](https://elite.bbcelite.com/c64/main/subroutine/main_flight_loop_part_9_of_16.html) | For each nearby ship: If it is a space station, check whether we are successfully docking with it | 
| [Main flight loop (Part 10 of 16)](https://elite.bbcelite.com/c64/main/subroutine/main_flight_loop_part_10_of_16.html) | For each nearby ship: Remove if scooped, or process collisions | 
| [Main flight loop (Part 11 of 16)](https://elite.bbcelite.com/c64/main/subroutine/main_flight_loop_part_11_of_16.html) | For each nearby ship: Process missile lock and firing our laser | 
| [Main flight loop (Part 12 of 16)](https://elite.bbcelite.com/c64/main/subroutine/main_flight_loop_part_12_of_16.html) | For each nearby ship: Draw the ship, remove if killed, loop back | 
| [Main flight loop (Part 13 of 16)](https://elite.bbcelite.com/c64/main/subroutine/main_flight_loop_part_13_of_16.html) | Show energy bomb effect, charge shields and energy banks | 
| [Main flight loop (Part 14 of 16)](https://elite.bbcelite.com/c64/main/subroutine/main_flight_loop_part_14_of_16.html) | Spawn a space station if we are close enough to the planet | 
| [Main flight loop (Part 15 of 16)](https://elite.bbcelite.com/c64/main/subroutine/main_flight_loop_part_15_of_16.html) | Perform altitude checks with the planet and sun and process fuel scooping if appropriate | 
| [Main flight loop (Part 16 of 16)](https://elite.bbcelite.com/c64/main/subroutine/main_flight_loop_part_16_of_16.html) | Process laser pulsing, E.C.M. energy drain, call stardust routine | 
| [Main game loop (Part 1 of 6)](https://elite.bbcelite.com/c64/main/subroutine/main_game_loop_part_1_of_6.html) | Spawn a trader (a Cobra Mk III, Python, Boa or Anaconda) | 
| [Main game loop (Part 2 of 6)](https://elite.bbcelite.com/c64/main/subroutine/main_game_loop_part_2_of_6.html) | Call the main flight loop, and potentially spawn a trader, an asteroid, or a cargo canister | 
| [Main game loop (Part 3 of 6)](https://elite.bbcelite.com/c64/main/subroutine/main_game_loop_part_3_of_6.html) | Potentially spawn a cop, particularly if we've been bad | 
| [Main game loop (Part 4 of 6)](https://elite.bbcelite.com/c64/main/subroutine/main_game_loop_part_4_of_6.html) | Potentially spawn a lone bounty hunter, a Thargoid, or up to four pirates | 
| [Main game loop (Part 5 of 6)](https://elite.bbcelite.com/c64/main/subroutine/main_game_loop_part_5_of_6.html) | Cool down lasers, make calls to update the dashboard | 
| [Main game loop (Part 6 of 6)](https://elite.bbcelite.com/c64/main/subroutine/main_game_loop_part_6_of_6.html) | Process non-flight key presses (docked keys) | 
| [MAL1](https://elite.bbcelite.com/c64/main/subroutine/main_flight_loop_part_4_of_16.html) | Marks the beginning of the ship analysis loop, so we can jump back here from part 12 of the main flight loop to work our way through each ship in the local bubble. We also jump back here when a ship is removed from the bubble, so we can continue processing from the next ship | 
| [me3](https://elite.bbcelite.com/c64/main/subroutine/main_game_loop_part_2_of_6.html) | Used by me2 to jump back into the main game loop after printing an in-flight message | 
| [MLOOP](https://elite.bbcelite.com/c64/main/subroutine/main_game_loop_part_5_of_6.html) | The entry point for the main game loop. This entry point comes after the call to the main flight loop and spawning routines, so it marks the start of the main game loop for when we are docked (as we don't need to call the main flight loop or spawning routines if we aren't in space) | 
| [NOMVETR](https://elite.bbcelite.com/c64/main/subroutine/main_flight_loop_part_1_of_16.html) | The re-entry point in the main game loop for when there are no sprites to move | 
| [TT100](https://elite.bbcelite.com/c64/main/subroutine/main_game_loop_part_2_of_6.html) | The entry point for the start of the main game loop, which calls the main flight loop and the moves into the spawning routine | 
| ## Market | |
| [BAY2](https://elite.bbcelite.com/c64/main/subroutine/tt219.html) | Jump into the main loop at FRCE, setting the key "pressed" to the Inventory key | 
| [dn](https://elite.bbcelite.com/c64/main/subroutine/dn.html) | Print the amount of money we have left in the cash pot, then make a short, high beep and delay for 1 second | 
| [gnum](https://elite.bbcelite.com/c64/main/subroutine/gnum.html) | Get a number from the keyboard | 
| [NWDAV4](https://elite.bbcelite.com/c64/main/subroutine/nwdav4.html) | Print an "ITEM?" error, make a beep and rejoin the TT210 routine | 
| [NWDAVxx](https://elite.bbcelite.com/c64/main/subroutine/tt210.html) | Used to rejoin this routine from the call to NWDAV4 | 
| [tnpr](https://elite.bbcelite.com/c64/main/subroutine/tnpr.html) | Work out if we have space for a specific amount of cargo | 
| [tnpr1](https://elite.bbcelite.com/c64/main/subroutine/tnpr1.html) | Work out if we have space for one tonne of cargo | 
| [TT151](https://elite.bbcelite.com/c64/main/subroutine/tt151.html) | Print the name, price and availability of a market item | 
| [TT152](https://elite.bbcelite.com/c64/main/subroutine/tt152.html) | Print the unit ("t", "kg" or "g") for a market item | 
| [TT160](https://elite.bbcelite.com/c64/main/subroutine/tt160.html) | Print "t" (for tonne) and a space | 
| [TT161](https://elite.bbcelite.com/c64/main/subroutine/tt161.html) | Print "kg" (for kilograms) | 
| [TT163](https://elite.bbcelite.com/c64/main/subroutine/tt163.html) | Print the headers for the table of market prices | 
| [TT167](https://elite.bbcelite.com/c64/main/subroutine/tt167.html) | Show the Market Price screen | 
| [TT16a](https://elite.bbcelite.com/c64/main/subroutine/tt16a.html) | Print "g" (for grams) | 
| [TT208](https://elite.bbcelite.com/c64/main/subroutine/tt208.html) | Show the Sell Cargo screen | 
| [TT210](https://elite.bbcelite.com/c64/main/subroutine/tt210.html) | Show a list of current cargo in our hold, optionally to sell | 
| [TT213](https://elite.bbcelite.com/c64/main/subroutine/tt213.html) | Show the Inventory screen | 
| [TT219](https://elite.bbcelite.com/c64/main/subroutine/tt219.html) | Show the Buy Cargo screen | 
| [var](https://elite.bbcelite.com/c64/main/subroutine/var.html) | Calculate QQ19+3 = economy * |economic_factor| | 
| ## Maths (Arithmetic) | |
| [ADD](https://elite.bbcelite.com/c64/main/subroutine/add.html) | Calculate (A X) = (A P) + (S R) | 
| [DORND](https://elite.bbcelite.com/c64/main/subroutine/dornd.html) | Generate random numbers | 
| [DORND2](https://elite.bbcelite.com/c64/main/subroutine/dornd.html) | Make sure the C flag doesn't affect the outcome | 
| [DV41](https://elite.bbcelite.com/c64/main/subroutine/dv41.html) | Calculate (P R) = 256 * DELTA / A | 
| [DV42](https://elite.bbcelite.com/c64/main/subroutine/dv42.html) | Calculate (P R) = 256 * DELTA / z_hi | 
| [DVID3B2](https://elite.bbcelite.com/c64/main/subroutine/dvid3b2.html) | Calculate K(3 2 1 0) = (A P+1 P) / (z_sign z_hi z_lo) | 
| [DVID4](https://elite.bbcelite.com/c64/main/subroutine/dvid4.html) | Calculate (P R) = 256 * A / Q | 
| [DVIDT](https://elite.bbcelite.com/c64/main/subroutine/dvidt.html) | Calculate (P+1 A) = (A P) / Q | 
| [FMLTU](https://elite.bbcelite.com/c64/main/subroutine/fmltu.html) | Calculate A = A * Q / 256 | 
| [FMLTU2](https://elite.bbcelite.com/c64/main/subroutine/fmltu2.html) | Calculate A = K * sin(A) | 
| [GC2](https://elite.bbcelite.com/c64/main/subroutine/gc2.html) | Calculate (Y X) = (A P) * 4 | 
| [GCASH](https://elite.bbcelite.com/c64/main/subroutine/gcash.html) | Calculate (Y X) = P * Q * 4 | 
| [itsoff](https://elite.bbcelite.com/c64/main/subroutine/dvidt.html) | Contains an RTS | 
| [LCASH](https://elite.bbcelite.com/c64/main/subroutine/lcash.html) | Subtract an amount of cash from the cash pot | 
| [LL120](https://elite.bbcelite.com/c64/main/subroutine/ll120.html) | Calculate (Y X) = (S x1_lo) * XX12+2 or (S x1_lo) / XX12+2 | 
| [LL121](https://elite.bbcelite.com/c64/main/subroutine/ll123.html) | Calculate (Y X) = (S R) / Q and set the sign to the opposite of the top byte on the stack | 
| [LL122](https://elite.bbcelite.com/c64/main/subroutine/ll120.html) | Calculate (Y X) = (S R) * Q and set the sign to the opposite of the top byte on the stack | 
| [LL123](https://elite.bbcelite.com/c64/main/subroutine/ll123.html) | Calculate (Y X) = (S R) / XX12+2 or (S R) * XX12+2 | 
| [LL128](https://elite.bbcelite.com/c64/main/subroutine/ll123.html) | Contains an RTS | 
| [LL129](https://elite.bbcelite.com/c64/main/subroutine/ll129.html) | Calculate Q = XX12+2, A = S EOR XX12+3 and (S R) = |S R| | 
| [LL133](https://elite.bbcelite.com/c64/main/subroutine/ll123.html) | Negate (Y X) and return from the subroutine | 
| [LL28](https://elite.bbcelite.com/c64/main/subroutine/ll28.html) | Calculate R = 256 * A / Q | 
| [LL28+4](https://elite.bbcelite.com/c64/main/subroutine/ll28.html) | Skips the A >= Q check and always returns with C flag cleared, so this can be called if we know the division will work | 
| [LL31](https://elite.bbcelite.com/c64/main/subroutine/ll28.html) | Skips the A >= Q check and does not set the R counter, so this can be used for jumping straight into the division loop if R is already set to 254 and we know the division will work | 
| [LL38](https://elite.bbcelite.com/c64/main/subroutine/ll38.html) | Calculate (S A) = (S R) + (A Q) | 
| [LL5](https://elite.bbcelite.com/c64/main/subroutine/ll5.html) | Calculate Q = SQRT(R Q) | 
| [LL61](https://elite.bbcelite.com/c64/main/subroutine/ll61.html) | Calculate (U R) = 256 * A / Q | 
| [LL62](https://elite.bbcelite.com/c64/main/subroutine/ll62.html) | Calculate 128 - (U R) | 
| [MAD](https://elite.bbcelite.com/c64/main/subroutine/mad.html) | Calculate (A X) = Q * A + (S R) | 
| [MAS3](https://elite.bbcelite.com/c64/main/subroutine/mas3.html) | Calculate A = x_hi^2 + y_hi^2 + z_hi^2 in the K% block | 
| [MCASH](https://elite.bbcelite.com/c64/main/subroutine/mcash.html) | Add an amount of cash to the cash pot | 
| [MLS1](https://elite.bbcelite.com/c64/main/subroutine/mls1.html) | Calculate (A P) = ALP1 * A | 
| [MLS2](https://elite.bbcelite.com/c64/main/subroutine/mls2.html) | Calculate (S R) = XX(1 0) and (A P) = A * ALP1 | 
| [MLTU2](https://elite.bbcelite.com/c64/main/subroutine/mltu2.html) | Calculate (A P+1 P) = (A ~P) * Q | 
| [MLTU2-2](https://elite.bbcelite.com/c64/main/subroutine/mltu2.html) | Set Q to X, so this calculates (A P+1 P) = (A ~P) * X | 
| [MLU1](https://elite.bbcelite.com/c64/main/subroutine/mlu1.html) | Calculate Y1 = y_hi and (A P) = |y_hi| * Q for Y-th stardust | 
| [MLU2](https://elite.bbcelite.com/c64/main/subroutine/mlu2.html) | Calculate (A P) = |A| * Q | 
| [MU1](https://elite.bbcelite.com/c64/main/subroutine/mu1.html) | Copy X into P and A, and clear the C flag | 
| [MU11](https://elite.bbcelite.com/c64/main/subroutine/mu11.html) | Calculate (A P) = P * X | 
| [MU5](https://elite.bbcelite.com/c64/main/subroutine/mu5.html) | Set K(3 2 1 0) = (A A A A) and clear the C flag | 
| [MU6](https://elite.bbcelite.com/c64/main/subroutine/mu6.html) | Set P(1 0) = (A A) | 
| [MULT1](https://elite.bbcelite.com/c64/main/subroutine/mult1.html) | Calculate (A P) = Q * A | 
| [MULT12](https://elite.bbcelite.com/c64/main/subroutine/mult12.html) | Calculate (S R) = Q * A | 
| [MULT3](https://elite.bbcelite.com/c64/main/subroutine/mult3.html) | Calculate K(3 2 1 0) = (A P+1 P) * Q | 
| [MULTS-2](https://elite.bbcelite.com/c64/main/subroutine/mls1.html) | Calculate (A P) = X * A | 
| [MULTU](https://elite.bbcelite.com/c64/main/subroutine/multu.html) | Calculate (A P) = P * Q | 
| [MUT1](https://elite.bbcelite.com/c64/main/subroutine/mut1.html) | Calculate R = XX and (A P) = Q * A | 
| [MUT2](https://elite.bbcelite.com/c64/main/subroutine/mut2.html) | Calculate (S R) = XX(1 0) and (A P) = Q * A | 
| [MUT3](https://elite.bbcelite.com/c64/main/subroutine/mut3.html) | An unused routine that does the same as MUT2 | 
| [PIX1](https://elite.bbcelite.com/c64/main/subroutine/pix1.html) | Calculate (YY+1 SYL+Y) = (A P) + (S R) and draw stardust particle | 
| [SPS2](https://elite.bbcelite.com/c64/main/subroutine/sps2.html) | Calculate (Y X) = A / 10 | 
| [SQUA](https://elite.bbcelite.com/c64/main/subroutine/squa.html) | Clear bit 7 of A and calculate (A P) = A * A | 
| [SQUA2](https://elite.bbcelite.com/c64/main/subroutine/squa2.html) | Calculate (A P) = A * A | 
| [TAS1](https://elite.bbcelite.com/c64/main/subroutine/tas1.html) | Calculate K3 = (x_sign x_hi x_lo) - V(1 0) | 
| [TIS1](https://elite.bbcelite.com/c64/main/subroutine/tis1.html) | Calculate (A ?) = (-X * A + (S R)) / 96 | 
| [TIS2](https://elite.bbcelite.com/c64/main/subroutine/tis2.html) | Calculate A = A / Q | 
| [TIS3](https://elite.bbcelite.com/c64/main/subroutine/tis3.html) | Calculate -(nosev_1 * roofv_1 + nosev_2 * roofv_2) / nosev_3 | 
| [TT113](https://elite.bbcelite.com/c64/main/subroutine/mcash.html) | Contains an RTS | 
| [VCSU1](https://elite.bbcelite.com/c64/main/subroutine/vcsu1.html) | Calculate vector K3(8 0) = [x y z] - coordinates of the sun or space station | 
| [VCSUB](https://elite.bbcelite.com/c64/main/subroutine/vcsub.html) | Calculate vector K3(8 0) = [x y z] - coordinates in (A V) | 
| ## Maths (Geometry) | |
| [ARCTAN](https://elite.bbcelite.com/c64/main/subroutine/arctan.html) | Calculate A = arctan(P / Q) | 
| [FAROF](https://elite.bbcelite.com/c64/main/subroutine/farof.html) | Compare x_hi, y_hi and z_hi with 224 | 
| [FAROF2](https://elite.bbcelite.com/c64/main/subroutine/farof2.html) | Compare x_hi, y_hi and z_hi with A | 
| [LL51](https://elite.bbcelite.com/c64/main/subroutine/ll51.html) | Calculate the dot product of XX15 and XX16 | 
| [m](https://elite.bbcelite.com/c64/main/subroutine/mas2.html) | Do not include A in the calculation | 
| [MA9](https://elite.bbcelite.com/c64/main/subroutine/mas1.html) | Contains an RTS | 
| [MAS1](https://elite.bbcelite.com/c64/main/subroutine/mas1.html) | Add an orientation vector coordinate to an INWK coordinate | 
| [MAS2](https://elite.bbcelite.com/c64/main/subroutine/mas2.html) | Calculate a cap on the maximum distance to the planet or sun | 
| [MAS4](https://elite.bbcelite.com/c64/main/subroutine/mas4.html) | Calculate a cap on the maximum distance to a ship | 
| [NO1](https://elite.bbcelite.com/c64/main/subroutine/norm.html) | Contains an RTS | 
| [NORM](https://elite.bbcelite.com/c64/main/subroutine/norm.html) | Normalise the three-coordinate vector in XX15 | 
| [PROJ](https://elite.bbcelite.com/c64/main/subroutine/proj.html) | Project the current ship or planet onto the screen | 
| [SPS1](https://elite.bbcelite.com/c64/main/subroutine/sps1.html) | Calculate the vector to the planet and store it in XX15 | 
| [SPS1+1](https://elite.bbcelite.com/c64/main/subroutine/sps1.html) | A BRK instruction | 
| [SPS3](https://elite.bbcelite.com/c64/main/subroutine/sps3.html) | Copy a space coordinate from the K% block into K3 | 
| [SPS4](https://elite.bbcelite.com/c64/main/subroutine/sps4.html) | Calculate the vector to the space station | 
| [TA2](https://elite.bbcelite.com/c64/main/subroutine/tas2.html) | Calculate the length of the vector in XX15 (ignoring the low coordinates), returning it in Q | 
| [TAS2](https://elite.bbcelite.com/c64/main/subroutine/tas2.html) | Normalise the three-coordinate vector in K3 | 
| [TAS3](https://elite.bbcelite.com/c64/main/subroutine/tas3.html) | Calculate the dot product of XX15 and an orientation vector | 
| [TAS4](https://elite.bbcelite.com/c64/main/subroutine/tas4.html) | Calculate the dot product of XX15 and one of the space station's orientation vectors | 
| [TAS6](https://elite.bbcelite.com/c64/main/subroutine/tas6.html) | Negate the vector in XX15 so it points in the opposite direction | 
| [TIDY](https://elite.bbcelite.com/c64/main/subroutine/tidy.html) | Orthonormalise the orientation vectors for a ship | 
| ## Missions | |
| [BAYSTEP](https://elite.bbcelite.com/c64/main/subroutine/brp.html) | Go to the docking bay (i.e. show the Status Mode screen) | 
| [BRIEF](https://elite.bbcelite.com/c64/main/subroutine/brief.html) | Start mission 1 and show the mission briefing | 
| [BRIEF2](https://elite.bbcelite.com/c64/main/subroutine/brief2.html) | Start mission 2 | 
| [BRIEF3](https://elite.bbcelite.com/c64/main/subroutine/brief3.html) | Receive the briefing and plans for mission 2 | 
| [BRIS](https://elite.bbcelite.com/c64/main/subroutine/bris.html) | Clear the screen, display "INCOMING MESSAGE" and wait for 2 seconds | 
| [BRP](https://elite.bbcelite.com/c64/main/subroutine/brp.html) | Print an extended token and show the Status Mode screen | 
| [BRPS](https://elite.bbcelite.com/c64/main/subroutine/debrief.html) | Print the extended token in A, show the Status Mode screen and return from the subroutine | 
| [DEBRIEF](https://elite.bbcelite.com/c64/main/subroutine/debrief.html) | Finish mission 1 | 
| [DEBRIEF2](https://elite.bbcelite.com/c64/main/subroutine/debrief2.html) | Finish mission 2 | 
| [MVTRIBS](https://elite.bbcelite.com/c64/main/subroutine/mvtribs.html) | Move the Trumble sprites around on-screen | 
| [NOSPRITES](https://elite.bbcelite.com/c64/main/subroutine/nosprites.html) | Disable all sprites and remove them from the screen | 
| [PAS1](https://elite.bbcelite.com/c64/main/subroutine/pas1.html) | Display a rotating ship at space coordinates (0, conhieght, 256) and scan the keyboard | 
| [PAUSE](https://elite.bbcelite.com/c64/main/subroutine/pause.html) | Display a rotating ship, waiting until a key is pressed, then remove the ship from the screen | 
| [TBRIEF](https://elite.bbcelite.com/c64/main/subroutine/tbrief.html) | Start mission 3 | 
| [THERE](https://elite.bbcelite.com/c64/main/subroutine/there.html) | Check whether we are in the Constrictor's system in mission 1 | 
| ## Moving | |
| [MV40](https://elite.bbcelite.com/c64/main/subroutine/mv40.html) | Rotate the planet or sun's location in space by the amount of pitch and roll of our ship | 
| [MV45](https://elite.bbcelite.com/c64/main/subroutine/mveit_part_6_of_9.html) | Rejoin the MVEIT routine after the rotation, tactics and scanner code | 
| [MVEIT (Part 1 of 9)](https://elite.bbcelite.com/c64/main/subroutine/mveit_part_1_of_9.html) | Move current ship: Tidy the orientation vectors | 
| [MVEIT (Part 2 of 9)](https://elite.bbcelite.com/c64/main/subroutine/mveit_part_2_of_9.html) | Move current ship: Call tactics routine, remove ship from scanner | 
| [MVEIT (Part 3 of 9)](https://elite.bbcelite.com/c64/main/subroutine/mveit_part_3_of_9.html) | Move current ship: Move ship forward according to its speed | 
| [MVEIT (Part 4 of 9)](https://elite.bbcelite.com/c64/main/subroutine/mveit_part_4_of_9.html) | Move current ship: Apply acceleration to ship's speed as a one-off | 
| [MVEIT (Part 5 of 9)](https://elite.bbcelite.com/c64/main/subroutine/mveit_part_5_of_9.html) | Move current ship: Rotate ship's location by our pitch and roll | 
| [MVEIT (Part 6 of 9)](https://elite.bbcelite.com/c64/main/subroutine/mveit_part_6_of_9.html) | Move current ship: Move the ship in space according to our speed | 
| [MVEIT (Part 7 of 9)](https://elite.bbcelite.com/c64/main/subroutine/mveit_part_7_of_9.html) | Move current ship: Rotate ship's orientation vectors by pitch/roll | 
| [MVEIT (Part 8 of 9)](https://elite.bbcelite.com/c64/main/subroutine/mveit_part_8_of_9.html) | Move current ship: Rotate ship about itself by its own pitch/roll | 
| [MVEIT (Part 9 of 9)](https://elite.bbcelite.com/c64/main/subroutine/mveit_part_9_of_9.html) | Move current ship: Redraw on scanner, if it hasn't been destroyed | 
| [MVS4](https://elite.bbcelite.com/c64/main/subroutine/mvs4.html) | Apply pitch and roll to an orientation vector | 
| [MVS5](https://elite.bbcelite.com/c64/main/subroutine/mvs5.html) | Apply a 3.6 degree pitch or roll to an orientation vector | 
| [MVT1](https://elite.bbcelite.com/c64/main/subroutine/mvt1.html) | Calculate (x_sign x_hi x_lo) = (x_sign x_hi x_lo) + (A R) | 
| [MVT1-2](https://elite.bbcelite.com/c64/main/subroutine/mvt1.html) | Clear bits 0-6 of A before entering MVT1 | 
| [MVT3](https://elite.bbcelite.com/c64/main/subroutine/mvt3.html) | Calculate K(3 2 1) = (x_sign x_hi x_lo) + K(3 2 1) | 
| [MVT6](https://elite.bbcelite.com/c64/main/subroutine/mvt6.html) | Calculate (A P+2 P+1) = (x_sign x_hi x_lo) + (A P+2 P+1) | 
| [SFS2](https://elite.bbcelite.com/c64/main/subroutine/sfs2.html) | Move a ship in space along one of the coordinate axes | 
| ## Save and load | |
| [BRKBK](https://elite.bbcelite.com/c64/main/subroutine/brkbk.html) | Set the standard BRKV handler for the game | 
| [CHECK](https://elite.bbcelite.com/c64/main/subroutine/check.html) | Calculate the checksum for the last saved commander data block | 
| [CHECK2](https://elite.bbcelite.com/c64/main/subroutine/check2.html) | Calculate the third checksum for the last saved commander data block (Commodore 64 and Apple II versions only) | 
| [DOSVN](https://elite.bbcelite.com/c64/main/subroutine/dosvn.html) | Implement the #DOSVN <flag> command (update the "save in progress" flag) | 
| [FILEPR](https://elite.bbcelite.com/c64/main/subroutine/filepr.html) | Display the currently selected media (disk or tape) | 
| [GTDRV](https://elite.bbcelite.com/c64/main/subroutine/gtdrv.html) | Get an ASCII disk drive number from the keyboard | 
| [GTNMEW](https://elite.bbcelite.com/c64/main/subroutine/gtnmew.html) | Fetch the name of a commander file to save or load | 
| [JAMESON](https://elite.bbcelite.com/c64/main/subroutine/jameson.html) | Restore the default JAMESON commander | 
| [KERNALSETUP](https://elite.bbcelite.com/c64/main/subroutine/kernalsetup.html) | Set up memory and interrupts so we can use the Kernal functions and configure the file system device number and filename | 
| [LOD](https://elite.bbcelite.com/c64/main/subroutine/lod.html) | Load a commander file | 
| [LOR](https://elite.bbcelite.com/c64/main/subroutine/lod.html) | Set the C flag and return from the subroutine | 
| [OTHERFILEPR](https://elite.bbcelite.com/c64/main/subroutine/otherfilepr.html) | Display the non-selected media (disk or tape) | 
| [SVE](https://elite.bbcelite.com/c64/main/subroutine/sve.html) | Display the disk access menu and process saving of commander files | 
| [tapeerror](https://elite.bbcelite.com/c64/main/subroutine/tapeerror.html) | Print either "TAPE ERROR" or "DISK ERROR" | 
| [TR1](https://elite.bbcelite.com/c64/main/subroutine/tr1.html) | Copy the last saved commander's name from NA% to INWK | 
| [TRNME](https://elite.bbcelite.com/c64/main/subroutine/trnme.html) | Copy the last saved commander's name from INWK to NA% | 
| ## Sound | |
| [april16](https://elite.bbcelite.com/c64/main/subroutine/startbd.html) | Start playing the docking music, irrespective of the current configuration settings | 
| [BDENTRY](https://elite.bbcelite.com/c64/main/subroutine/bdentry.html) | Start playing a new tune as background music | 
| [BDirqhere](https://elite.bbcelite.com/c64/main/subroutine/bdirqhere.html) | The interrupt routine for playing background music | 
| [BDlab1](https://elite.bbcelite.com/c64/main/subroutine/bdlab1.html) | Apply vibrato before cleaning up and returning from the interrupt routine | 
| [BDlab19](https://elite.bbcelite.com/c64/main/subroutine/bdlab19.html) | Increment the music data pointer in BDdataptr1(1 0) and fetch the next data byte into A | 
| [BDlab21](https://elite.bbcelite.com/c64/main/subroutine/bdlab21.html) | Clean up and return from the interrupt routine | 
| [BDlab23](https://elite.bbcelite.com/c64/main/subroutine/bdlab23.html) | Apply a vibrato frequency change to voice 3 | 
| [BDlab24](https://elite.bbcelite.com/c64/main/subroutine/bdlab24.html) | Apply a vibrato frequency change to voice 2 | 
| [BDlab3](https://elite.bbcelite.com/c64/main/subroutine/bdlab3.html) | Fetch the next two music data bytes and set the frequency of voice 1 (high byte then low byte) | 
| [BDlab4](https://elite.bbcelite.com/c64/main/subroutine/bdlab4.html) | Set the voice control register for voice 1 to value1 | 
| [BDlab5](https://elite.bbcelite.com/c64/main/subroutine/bdlab5.html) | Fetch the next two music data bytes and set the frequency of voice 2 (high byte then low byte) and the vibrato variables | 
| [BDlab6](https://elite.bbcelite.com/c64/main/subroutine/bdlab6.html) | Set the voice control register for voice 2 to value2 | 
| [BDlab7](https://elite.bbcelite.com/c64/main/subroutine/bdlab7.html) | Fetch the next two music data bytes and set the frequency of voice 3 (high byte then low byte) and the vibrato variables | 
| [BDlab8](https://elite.bbcelite.com/c64/main/subroutine/bdlab8.html) | Set the voice control register for voice 3 to value3 | 
| [BDRO1](https://elite.bbcelite.com/c64/main/subroutine/bdro1.html) | Process music command <#1 fh1 fl1> to set the frequency for voice 1 to (fh1 fl1) and the control register for voice 1 to value1 | 
| [BDRO10](https://elite.bbcelite.com/c64/main/subroutine/bdro10.html) | Process music command <#10 h1 l1 h2 l2 h3 l3> to set the pulse width to all three voices | 
| [BDRO11](https://elite.bbcelite.com/c64/main/subroutine/bdro11.html) | Process music command <#11>, which does the same as command <#9> and restarts the current tune | 
| [BDRO12](https://elite.bbcelite.com/c64/main/subroutine/bdro12.html) | Process music command <#12 n> to set value4 = n, which sets the rest length for commands #8 and #15 | 
| [BDRO13](https://elite.bbcelite.com/c64/main/subroutine/bdro13.html) | Process music command <#13 v1 v2 v3> to set value1, value2, value3 to the voice control register values for commands <#1> to <#3> | 
| [BDRO14](https://elite.bbcelite.com/c64/main/subroutine/bdro14.html) | Process music command <#14 vf fc cf> to set the volume and filter modes, filter control and filter cut-off frequency | 
| [BDRO15](https://elite.bbcelite.com/c64/main/subroutine/bdro15.html) | Process music command <#15> to rest for 2 * value4 interrupts | 
| [BDRO2](https://elite.bbcelite.com/c64/main/subroutine/bdro2.html) | Process music command <#2 fh1 fl1> to set the frequency for voice 2 to (fh2 fl2) and the control register for voice 2 to value2 | 
| [BDRO3](https://elite.bbcelite.com/c64/main/subroutine/bdro3.html) | Process music command <#3 fh1 fl1> to set the frequency for voice 3 to (fh3 fl3) and the control register for voice 3 to value3 | 
| [BDRO4](https://elite.bbcelite.com/c64/main/subroutine/bdro4.html) | Process music command <#4 fh1 fl1 fh2 fl2> to set the frequencies and voice control registers for voices 1 and 2 | 
| [BDRO5](https://elite.bbcelite.com/c64/main/subroutine/bdro5.html) | Process music command <#5 fh1 fl1 fh2 fl2 fh3 fl3> to set the frequencies and voice control registers for voices 1, 2 and 3 | 
| [BDRO6](https://elite.bbcelite.com/c64/main/subroutine/bdro6.html) | Process music command <#6> to increment value0 and move on to the next nibble of music data | 
| [BDRO7](https://elite.bbcelite.com/c64/main/subroutine/bdro7.html) | Process music command <#7 ad1 ad2 ad3 sr1 sr2 sr3> to set three voices' attack and decay length, sustain volume and release length | 
| [BDRO8](https://elite.bbcelite.com/c64/main/subroutine/bdro8.html) | Process music command <#8> to rest for value4 interrupts | 
| [BDRO9](https://elite.bbcelite.com/c64/main/subroutine/bdro9.html) | Process music command <#9> to restart the current tune | 
| [BDskip1](https://elite.bbcelite.com/c64/main/subroutine/bdirqhere.html) | Process the next nibble of music data in BDBUFF | 
| [BEEP](https://elite.bbcelite.com/c64/main/subroutine/beep.html) | Make a short, high beep | 
| [BELL](https://elite.bbcelite.com/c64/main/subroutine/bell.html) | Make a standard system beep | 
| [coffee](https://elite.bbcelite.com/c64/main/subroutine/coffee.html) | Return from the interrupt routine, for when we are making sound effects | 
| [coffeeex](https://elite.bbcelite.com/c64/main/subroutine/stopbd.html) | Restore the memory configuration and return from the subroutine | 
| [EXNO](https://elite.bbcelite.com/c64/main/subroutine/exno.html) | Make the sound of a laser strike on another ship | 
| [EXNO3](https://elite.bbcelite.com/c64/main/subroutine/exno3.html) | Make an explosion sound | 
| [HYPNOISE](https://elite.bbcelite.com/c64/main/subroutine/hypnoise.html) | Make the sound of the hyperspace drive being engaged | 
| [MUTOKCH](https://elite.bbcelite.com/c64/main/subroutine/mutokch.html) | Process a change in the docking music configuration setting | 
| [NOISE](https://elite.bbcelite.com/c64/main/subroutine/noise.html) | Make the sound whose number is in Y | 
| [NOISE2](https://elite.bbcelite.com/c64/main/subroutine/noise2.html) | Make a sound effect with a specific volume and release length | 
| [NOISEOFF](https://elite.bbcelite.com/c64/main/subroutine/noiseoff.html) | Turn off a specific sound effect in whichever voice it is currently playing in | 
| [SOFLUSH](https://elite.bbcelite.com/c64/main/subroutine/soflush.html) | Reset the sound buffers and turn off all sound channels | 
| [SOINT](https://elite.bbcelite.com/c64/main/subroutine/soint.html) | Process the contents of the sound buffer and send it to the sound chip, to make sound effects as part of the interrupt routine | 
| [SOUL3b](https://elite.bbcelite.com/c64/main/subroutine/soul3b.html) | Check whether this is the last voice when making sound effects in the interrupt routine, and return from the interrupt if it is | 
| [SOUL8](https://elite.bbcelite.com/c64/main/subroutine/soint.html) | Process the sound buffer from voice Y to 0 | 
| [SOUR1](https://elite.bbcelite.com/c64/main/subroutine/soflush.html) | Contains an RTS | 
| [startat](https://elite.bbcelite.com/c64/main/subroutine/startat.html) | Start playing the title music, if configured | 
| [startat2](https://elite.bbcelite.com/c64/main/subroutine/startbd.html) | Start playing the music at address (A X) + 1 | 
| [startbd](https://elite.bbcelite.com/c64/main/subroutine/startbd.html) | Start playing the docking music, if configured | 
| [stopat](https://elite.bbcelite.com/c64/main/subroutine/stopbd.html) | Stop playing the current music | 
| [stopbd](https://elite.bbcelite.com/c64/main/subroutine/stopbd.html) | Stop playing the docking music | 
| ## Stardust | |
| [FLIP](https://elite.bbcelite.com/c64/main/subroutine/flip.html) | Reflect the stardust particles in the screen diagonal and redraw the stardust field | 
| [nWq](https://elite.bbcelite.com/c64/main/subroutine/nwq.html) | Create a random cloud of stardust | 
| [NWSTARS](https://elite.bbcelite.com/c64/main/subroutine/nwstars.html) | Initialise the stardust field | 
| [STARS](https://elite.bbcelite.com/c64/main/subroutine/stars.html) | The main routine for processing the stardust | 
| [STARS1](https://elite.bbcelite.com/c64/main/subroutine/stars1.html) | Process the stardust for the front view | 
| [STARS2](https://elite.bbcelite.com/c64/main/subroutine/stars2.html) | Process the stardust for the left or right view | 
| [STARS6](https://elite.bbcelite.com/c64/main/subroutine/stars6.html) | Process the stardust for the rear view | 
| ## Start and end | |
| [BR1 (Part 1 of 2)](https://elite.bbcelite.com/c64/main/subroutine/br1_part_1_of_2.html) | Show the "Load New Commander (Y/N)?" screen and start the game | 
| [BR1 (Part 2 of 2)](https://elite.bbcelite.com/c64/main/subroutine/br1_part_2_of_2.html) | Show the "Press Fire or Space, Commander" screen and start the game | 
| [DEATH](https://elite.bbcelite.com/c64/main/subroutine/death.html) | Display the death screen | 
| [DEATH2](https://elite.bbcelite.com/c64/main/subroutine/death2.html) | Reset most of the game and restart from the title screen | 
| [DFAULT](https://elite.bbcelite.com/c64/main/subroutine/dfault.html) | Reset the current commander data block to the last saved commander | 
| [QU5](https://elite.bbcelite.com/c64/main/subroutine/br1_part_1_of_2.html) | Restart the game using the last saved commander without asking whether to load a new commander file | 
| [RES2](https://elite.bbcelite.com/c64/main/subroutine/res2.html) | Reset a number of flight variables and workspaces | 
| [RESET](https://elite.bbcelite.com/c64/main/subroutine/reset.html) | Reset most variables | 
| [TITLE](https://elite.bbcelite.com/c64/main/subroutine/title.html) | Display a title screen with a rotating ship and prompt | 
| [TT170](https://elite.bbcelite.com/c64/main/subroutine/tt170.html) | Main entry point for the Elite game code | 
| ## Status | |
| [BAD](https://elite.bbcelite.com/c64/main/subroutine/bad.html) | Calculate how bad we have been | 
| [BAY](https://elite.bbcelite.com/c64/main/subroutine/bay.html) | Go to the docking bay (i.e. show the Status Mode screen) | 
| [cmn](https://elite.bbcelite.com/c64/main/subroutine/cmn.html) | Print the commander's name | 
| [cmn-1](https://elite.bbcelite.com/c64/main/subroutine/cmn.html) | Contains an RTS | 
| [csh](https://elite.bbcelite.com/c64/main/subroutine/csh.html) | Print the current amount of cash | 
| [EXNO2](https://elite.bbcelite.com/c64/main/subroutine/exno2.html) | Process us making a kill | 
| [fwl](https://elite.bbcelite.com/c64/main/subroutine/fwl.html) | Print fuel and cash levels | 
| [STATUS](https://elite.bbcelite.com/c64/main/subroutine/status.html) | Show the Status Mode screen | 
| ## Tactics | |
| [ANGRY](https://elite.bbcelite.com/c64/main/subroutine/angry.html) | Make a ship or station hostile, and if this is a ship then enable the ship's AI and give it a kick of speed | 
| [fq1](https://elite.bbcelite.com/c64/main/subroutine/frs1.html) | Used to add a cargo canister to the universe | 
| [FR1](https://elite.bbcelite.com/c64/main/subroutine/fr1.html) | Display the "missile jammed" message | 
| [FR1-2](https://elite.bbcelite.com/c64/main/subroutine/fr1.html) | Clear the C flag and return from the subroutine | 
| [FRMIS](https://elite.bbcelite.com/c64/main/subroutine/frmis.html) | Fire a missile from our ship | 
| [FRS1](https://elite.bbcelite.com/c64/main/subroutine/frs1.html) | Launch a ship straight ahead of us, below the laser sights | 
| [GOPL](https://elite.bbcelite.com/c64/main/subroutine/tactics_part_3_of_7.html) | Make the ship head towards the planet | 
| [HI1](https://elite.bbcelite.com/c64/main/subroutine/hitch.html) | Contains an RTS | 
| [HITCH](https://elite.bbcelite.com/c64/main/subroutine/hitch.html) | Work out if the ship in INWK is in our crosshairs | 
| [SFRMIS](https://elite.bbcelite.com/c64/main/subroutine/sfrmis.html) | Add an enemy missile to our local bubble of universe | 
| [TA151](https://elite.bbcelite.com/c64/main/subroutine/tactics_part_7_of_7.html) | Make the ship head towards the planet | 
| [TA9-1](https://elite.bbcelite.com/c64/main/subroutine/tactics_part_7_of_7.html) | Contains an RTS | 
| [TACTICS (Part 1 of 7)](https://elite.bbcelite.com/c64/main/subroutine/tactics_part_1_of_7.html) | Apply tactics: Process missiles, both enemy missiles and our own | 
| [TACTICS (Part 2 of 7)](https://elite.bbcelite.com/c64/main/subroutine/tactics_part_2_of_7.html) | Apply tactics: Escape pod, station, lone Thargon, safe-zone pirate | 
| [TACTICS (Part 3 of 7)](https://elite.bbcelite.com/c64/main/subroutine/tactics_part_3_of_7.html) | Apply tactics: Calculate dot product to determine ship's aim | 
| [TACTICS (Part 4 of 7)](https://elite.bbcelite.com/c64/main/subroutine/tactics_part_4_of_7.html) | Apply tactics: Check energy levels, maybe launch escape pod if low | 
| [TACTICS (Part 5 of 7)](https://elite.bbcelite.com/c64/main/subroutine/tactics_part_5_of_7.html) | Apply tactics: Consider whether to launch a missile at us | 
| [TACTICS (Part 6 of 7)](https://elite.bbcelite.com/c64/main/subroutine/tactics_part_6_of_7.html) | Apply tactics: Consider firing a laser at us, if aim is true | 
| [TACTICS (Part 7 of 7)](https://elite.bbcelite.com/c64/main/subroutine/tactics_part_7_of_7.html) | Apply tactics: Set pitch, roll, and acceleration | 
| [yetanotherrts](https://elite.bbcelite.com/c64/main/subroutine/yetanotherrts.html) | Contains an RTS | 
| ## Text | |
| [BPRNT](https://elite.bbcelite.com/c64/main/subroutine/bprnt.html) | Print a 32-bit number, left-padded to a specific number of digits, with an optional decimal point | 
| [CHPR](https://elite.bbcelite.com/c64/main/subroutine/chpr.html) | Print a character at the text cursor by poking into screen memory | 
| [CHPR2](https://elite.bbcelite.com/c64/main/subroutine/chpr2.html) | Character print vector handler | 
| [crlf](https://elite.bbcelite.com/c64/main/subroutine/crlf.html) | Tab to column 21 and print a colon | 
| [DASC](https://elite.bbcelite.com/c64/main/subroutine/tt26.html) | DASC does exactly the same as TT26 and prints a character at the text cursor, with support for verified text in extended tokens | 
| [dec27](https://elite.bbcelite.com/c64/main/subroutine/tt26.html) | Contains an RTS | 
| [DETOK](https://elite.bbcelite.com/c64/main/subroutine/detok.html) | Print an extended recursive token from the TKN1 token table | 
| [DETOK2](https://elite.bbcelite.com/c64/main/subroutine/detok2.html) | Print an extended text token (1-255) | 
| [DETOK3](https://elite.bbcelite.com/c64/main/subroutine/detok3.html) | Print an extended recursive token from the RUTOK token table | 
| [dn2](https://elite.bbcelite.com/c64/main/subroutine/dn2.html) | Make a short, high beep and delay for 1 second | 
| [DOCOL](https://elite.bbcelite.com/c64/main/subroutine/docol.html) | Implement the #SETCOL <colour> command (set the current colour) | 
| [DOXC](https://elite.bbcelite.com/c64/main/subroutine/doxc.html) | Move the text cursor to a specific column | 
| [DOYC](https://elite.bbcelite.com/c64/main/subroutine/doyc.html) | Move the text cursor to a specific row | 
| [DTEN](https://elite.bbcelite.com/c64/main/subroutine/detok.html) | Print recursive token number X from the token table pointed to by (A V), used to print tokens from the RUTOK table via calls to DETOK3 | 
| [DTS](https://elite.bbcelite.com/c64/main/subroutine/detok2.html) | Print a single letter in the correct case | 
| [ex](https://elite.bbcelite.com/c64/main/subroutine/ex.html) | Print a recursive token | 
| [FEED](https://elite.bbcelite.com/c64/main/subroutine/feed.html) | Print a newline | 
| [INCYC](https://elite.bbcelite.com/c64/main/subroutine/incyc.html) | Move the text cursor to the next row | 
| [MT1](https://elite.bbcelite.com/c64/main/subroutine/mt1.html) | Switch to ALL CAPS when printing extended tokens | 
| [MT13](https://elite.bbcelite.com/c64/main/subroutine/mt13.html) | Switch to lower case when printing extended tokens | 
| [MT14](https://elite.bbcelite.com/c64/main/subroutine/mt14.html) | Switch to justified text when printing extended tokens | 
| [MT15](https://elite.bbcelite.com/c64/main/subroutine/mt15.html) | Switch to left-aligned text when printing extended tokens | 
| [MT16](https://elite.bbcelite.com/c64/main/subroutine/mt16.html) | Print the character in variable DTW7 | 
| [MT17](https://elite.bbcelite.com/c64/main/subroutine/mt17.html) | Print the selected system's adjective, e.g. Lavian for Lave | 
| [MT18](https://elite.bbcelite.com/c64/main/subroutine/mt18.html) | Print a random 1-8 letter word in Sentence Case | 
| [MT19](https://elite.bbcelite.com/c64/main/subroutine/mt19.html) | Capitalise the next letter | 
| [MT2](https://elite.bbcelite.com/c64/main/subroutine/mt2.html) | Switch to Sentence Case when printing extended tokens | 
| [MT23](https://elite.bbcelite.com/c64/main/subroutine/mt23.html) | Move to row 10, switch to white text, and switch to lower case when printing extended tokens | 
| [MT26](https://elite.bbcelite.com/c64/main/subroutine/mt26.html) | Fetch a line of text from the keyboard | 
| [MT27](https://elite.bbcelite.com/c64/main/subroutine/mt27.html) | Print the captain's name during mission briefings | 
| [MT28](https://elite.bbcelite.com/c64/main/subroutine/mt28.html) | Print the location hint during the mission 1 briefing | 
| [MT29](https://elite.bbcelite.com/c64/main/subroutine/mt29.html) | Move to row 6 and switch to lower case when printing extended tokens | 
| [MT5](https://elite.bbcelite.com/c64/main/subroutine/mt5.html) | Switch to extended tokens | 
| [MT6](https://elite.bbcelite.com/c64/main/subroutine/mt6.html) | Switch to standard tokens in Sentence Case | 
| [MT8](https://elite.bbcelite.com/c64/main/subroutine/mt8.html) | Tab to column 6 and start a new word when printing extended tokens | 
| [MT9](https://elite.bbcelite.com/c64/main/subroutine/mt9.html) | Clear the screen and set the current view type to 1 | 
| [plf](https://elite.bbcelite.com/c64/main/subroutine/plf.html) | Print a text token followed by a newline | 
| [plf2](https://elite.bbcelite.com/c64/main/subroutine/plf2.html) | Print text followed by a newline and indent of 6 characters | 
| [pr2](https://elite.bbcelite.com/c64/main/subroutine/pr2.html) | Print an 8-bit number, left-padded to 3 digits, and optional point | 
| [pr2+2](https://elite.bbcelite.com/c64/main/subroutine/pr2.html) | Print the 8-bit number in X to the number of digits in A | 
| [pr5](https://elite.bbcelite.com/c64/main/subroutine/pr5.html) | Print a 16-bit number, left-padded to 5 digits, and optional point | 
| [pr6](https://elite.bbcelite.com/c64/main/subroutine/pr6.html) | Print 16-bit number, left-padded to 5 digits, no point | 
| [prq](https://elite.bbcelite.com/c64/main/subroutine/prq.html) | Print a text token followed by a question mark | 
| [prq+3](https://elite.bbcelite.com/c64/main/subroutine/prq.html) | Print a question mark | 
| [qw](https://elite.bbcelite.com/c64/main/subroutine/qw.html) | Print a recursive token in the range 128-145 | 
| [R5](https://elite.bbcelite.com/c64/main/subroutine/r5.html) | Make a beep and jump back into the character-printing routine at CHPR | 
| [RR4](https://elite.bbcelite.com/c64/main/subroutine/chpr.html) | Restore the registers and return from the subroutine | 
| [RR4S](https://elite.bbcelite.com/c64/main/subroutine/rr4s.html) | A jump point that restores the registers and returns from the CHPR subroutine (so we can use a branch instruction to jump to RR4) | 
| [RRafter](https://elite.bbcelite.com/c64/main/subroutine/chpr.html) | A re-entry point from the clss routine to print the character in A | 
| [SETXC](https://elite.bbcelite.com/c64/main/subroutine/setxc.html) | An unused routine to move the text cursor to a specific column | 
| [SETYC](https://elite.bbcelite.com/c64/main/subroutine/setyc.html) | An unused routine to move the text cursor to a specific row | 
| [spc](https://elite.bbcelite.com/c64/main/subroutine/spc.html) | Print a text token followed by a space | 
| [TT11](https://elite.bbcelite.com/c64/main/subroutine/tt11.html) | Print a 16-bit number, left-padded to n digits, and optional point | 
| [TT162](https://elite.bbcelite.com/c64/main/subroutine/tt162.html) | Print a space | 
| [TT162+2](https://elite.bbcelite.com/c64/main/subroutine/tt162.html) | Jump to TT27 to print the text token in A | 
| [TT26](https://elite.bbcelite.com/c64/main/subroutine/tt26.html) | Print a character at the text cursor, with support for verified text in extended tokens | 
| [TT27](https://elite.bbcelite.com/c64/main/subroutine/tt27.html) | Print a text token | 
| [TT41](https://elite.bbcelite.com/c64/main/subroutine/tt41.html) | Print a letter according to Sentence Case | 
| [TT42](https://elite.bbcelite.com/c64/main/subroutine/tt42.html) | Print a letter in lower case | 
| [TT43](https://elite.bbcelite.com/c64/main/subroutine/tt43.html) | Print a two-letter token or recursive token 0-95 | 
| [TT44](https://elite.bbcelite.com/c64/main/subroutine/tt42.html) | Jumps to TT26 to print the character in A (used to enable us to use a branch instruction to jump to TT26) | 
| [TT45](https://elite.bbcelite.com/c64/main/subroutine/tt45.html) | Print a letter in lower case | 
| [TT46](https://elite.bbcelite.com/c64/main/subroutine/tt46.html) | Print a character and switch to capitals | 
| [TT48](https://elite.bbcelite.com/c64/main/subroutine/ex.html) | Contains an RTS | 
| [TT60](https://elite.bbcelite.com/c64/main/subroutine/tt60.html) | Print a text token and a paragraph break | 
| [TT67](https://elite.bbcelite.com/c64/main/subroutine/tt67.html) | Print a newline | 
| [TT67K](https://elite.bbcelite.com/c64/main/subroutine/tt67k.html) | Print a newline | 
| [TT68](https://elite.bbcelite.com/c64/main/subroutine/tt68.html) | Print a text token followed by a colon | 
| [TT69](https://elite.bbcelite.com/c64/main/subroutine/tt69.html) | Set Sentence Case and print a newline | 
| [TT73](https://elite.bbcelite.com/c64/main/subroutine/tt73.html) | Print a colon | 
| [TT74](https://elite.bbcelite.com/c64/main/subroutine/tt74.html) | Print a character | 
| [TTX69](https://elite.bbcelite.com/c64/main/subroutine/ttx69.html) | Print a paragraph break | 
| [VOWEL](https://elite.bbcelite.com/c64/main/subroutine/vowel.html) | Test whether a character is a vowel | 
| [WHITETEXT](https://elite.bbcelite.com/c64/main/subroutine/whitetext.html) | Switch to white text | 
| ## Tube | |
| [newosrdch](https://elite.bbcelite.com/c64/main/subroutine/newosrdch.html) | The custom OSRDCH routine for reading characters | 
| [PUTBACK](https://elite.bbcelite.com/c64/main/subroutine/putback.html) | Reset the OSWRCH vector in WRCHV to point to USOSWRCH | 
| ## Universe | |
| [cpl](https://elite.bbcelite.com/c64/main/subroutine/cpl.html) | Print the selected system name | 
| [GINF](https://elite.bbcelite.com/c64/main/subroutine/ginf.html) | Fetch the address of a ship's data block into INF | 
| [GTHG](https://elite.bbcelite.com/c64/main/subroutine/gthg.html) | Spawn a Thargoid ship and a Thargon companion | 
| [GVL](https://elite.bbcelite.com/c64/main/subroutine/gvl.html) | Calculate the availability of market items | 
| [hy5](https://elite.bbcelite.com/c64/main/subroutine/jmp.html) | Contains an RTS | 
| [hyp1](https://elite.bbcelite.com/c64/main/subroutine/hyp1.html) | Process a jump to the system closest to (QQ9, QQ10) | 
| [hyp1+3](https://elite.bbcelite.com/c64/main/subroutine/hyp1.html) | Jump straight to the system at (QQ9, QQ10) without first calculating which system is closest. We do this if we already know that (QQ9, QQ10) points to a system | 
| [hyR](https://elite.bbcelite.com/c64/main/subroutine/gvl.html) | Contains an RTS | 
| [jmp](https://elite.bbcelite.com/c64/main/subroutine/jmp.html) | Set the current system to the selected system | 
| [KILLSHP](https://elite.bbcelite.com/c64/main/subroutine/killshp.html) | Remove a ship from our local bubble of universe | 
| [KS1](https://elite.bbcelite.com/c64/main/subroutine/ks1.html) | Remove the current ship from our local bubble of universe | 
| [KS2](https://elite.bbcelite.com/c64/main/subroutine/ks2.html) | Check the local bubble for missiles with target lock | 
| [KS3](https://elite.bbcelite.com/c64/main/subroutine/ks3.html) | Set the SLSP ship line heap pointer after shuffling ship slots | 
| [KS4](https://elite.bbcelite.com/c64/main/subroutine/ks4.html) | Remove the space station and replace it with the sun | 
| [NwS1](https://elite.bbcelite.com/c64/main/subroutine/nws1.html) | Flip the sign and double an INWK byte | 
| [NWSHP](https://elite.bbcelite.com/c64/main/subroutine/nwshp.html) | Add a new ship to our local bubble of universe | 
| [NWSPS](https://elite.bbcelite.com/c64/main/subroutine/nwsps.html) | Add a new space station to our local bubble of universe | 
| [oh](https://elite.bbcelite.com/c64/main/subroutine/spin.html) | Contains an RTS | 
| [PDESC](https://elite.bbcelite.com/c64/main/subroutine/pdesc.html) | Print the system's extended description or a mission 1 directive | 
| [ping](https://elite.bbcelite.com/c64/main/subroutine/ping.html) | Set the selected system to the current system | 
| [SFS1](https://elite.bbcelite.com/c64/main/subroutine/sfs1.html) | Spawn a child ship from the current (parent) ship | 
| [SFS1-2](https://elite.bbcelite.com/c64/main/subroutine/sfs1.html) | Used to add a missile to the local bubble that that has AI (bit 7 set), is hostile (bit 6 set) and has been launched (bit 0 clear); the target slot number is set to 31, but this is ignored as the hostile flags means we are the target | 
| [SOLAR](https://elite.bbcelite.com/c64/main/subroutine/solar.html) | Set up various aspects of arriving in a new system | 
| [SOS1](https://elite.bbcelite.com/c64/main/subroutine/sos1.html) | Update the missile indicators, set up the planet data block | 
| [SPIN](https://elite.bbcelite.com/c64/main/subroutine/spin.html) | Randomly spawn cargo from a destroyed ship | 
| [SPIN2](https://elite.bbcelite.com/c64/main/subroutine/spin.html) | Remove any randomness: spawn cargo of a specific type (given in X), and always spawn the number given in A | 
| [tal](https://elite.bbcelite.com/c64/main/subroutine/tal.html) | Print the current galaxy number | 
| [TT111](https://elite.bbcelite.com/c64/main/subroutine/tt111.html) | Set the current system to the nearest system to a point | 
| [TT111-1](https://elite.bbcelite.com/c64/main/subroutine/tt111.html) | Contains an RTS | 
| [TT146](https://elite.bbcelite.com/c64/main/subroutine/tt146.html) | Print the distance to the selected system in light years | 
| [TT20](https://elite.bbcelite.com/c64/main/subroutine/tt20.html) | Twist the selected system's seeds four times | 
| [TT24](https://elite.bbcelite.com/c64/main/subroutine/tt24.html) | Calculate system data from the system seeds | 
| [TT25](https://elite.bbcelite.com/c64/main/subroutine/tt25.html) | Show the Data on System screen | 
| [TT54](https://elite.bbcelite.com/c64/main/subroutine/tt54.html) | Twist the selected system's seeds | 
| [TT70](https://elite.bbcelite.com/c64/main/subroutine/tt70.html) | Display "MAINLY " and jump to TT72 | 
| [TT72](https://elite.bbcelite.com/c64/main/subroutine/tt25.html) | Used by TT70 to re-enter the routine after displaying "MAINLY" for the economy type | 
| [TT81](https://elite.bbcelite.com/c64/main/subroutine/tt81.html) | Set the selected system's seeds to those of system 0 | 
| [ypl](https://elite.bbcelite.com/c64/main/subroutine/ypl.html) | Print the current system name | 
| [ypl-1](https://elite.bbcelite.com/c64/main/subroutine/ypl.html) | Contains an RTS | 
| [Ze](https://elite.bbcelite.com/c64/main/subroutine/ze.html) | Initialise the INWK workspace to a fairly aggressive ship | 
| [ZINF](https://elite.bbcelite.com/c64/main/subroutine/zinf.html) | Reset the INWK workspace and orientation vectors | 
| ## Utility routines | |
| [backtonormal](https://elite.bbcelite.com/c64/main/subroutine/backtonormal.html) | Disable the keyboard, set the SVN flag to 0, and return with A = 0 | 
| [BRBR](https://elite.bbcelite.com/c64/main/subroutine/brbr.html) | The standard BRKV handler for the game | 
| [CLDELAY](https://elite.bbcelite.com/c64/main/subroutine/cldelay.html) | Delay by iterating through 5 * 256 (1280) empty loops | 
| [DEEOR](https://elite.bbcelite.com/c64/main/subroutine/deeor.html) | Unscramble the main code | 
| [DEEORS](https://elite.bbcelite.com/c64/main/subroutine/deeors.html) | Decrypt a multi-page block of memory | 
| [DELAY](https://elite.bbcelite.com/c64/main/subroutine/delay.html) | Wait for a specified time, in either 1/50s of a second (on PAL systems) or 1/60s of a second (on NTSC systems) | 
| [mvbllop](https://elite.bbcelite.com/c64/main/subroutine/mvblockk.html) | Only copy Y bytes, rather than a whole page | 
| [mvblockK](https://elite.bbcelite.com/c64/main/subroutine/mvblockk.html) | Copy a specific number of pages in memory | 
| [SETL1](https://elite.bbcelite.com/c64/main/subroutine/setl1.html) | Set the 6510 input/output port register to control the memory map | 
| [SWAPPZERO](https://elite.bbcelite.com/c64/main/subroutine/swappzero.html) | A routine that swaps zero page with the page at $CE00, so that zero page changes made by Kernal functions can be reversed | 
| [SWAPPZERO (source disk variant)](https://elite.bbcelite.com/c64/main/subroutine/swappzero_source_disk_variant.html) | A routine that swaps zero page with the page at $CE00, so that zero page changes made by Kernal functions can be reversed | 
| [ZEBC](https://elite.bbcelite.com/c64/main/subroutine/zebc.html) | Zero-fill pages $B and $C | 
| [ZERO](https://elite.bbcelite.com/c64/main/subroutine/zero.html) | Reset the local bubble of universe and ship status | 
| [ZES1](https://elite.bbcelite.com/c64/main/subroutine/zes1.html) | Zero-fill the page whose number is in X | 
| [ZES1k](https://elite.bbcelite.com/c64/main/subroutine/zes1k.html) | Zero-fill the page whose number is in X | 
| [ZES2](https://elite.bbcelite.com/c64/main/subroutine/zes2.html) | Zero-fill a specific page | 
| [ZES2k](https://elite.bbcelite.com/c64/main/subroutine/zes2k.html) | Zero-fill a specific page | 
| [ZESNEW](https://elite.bbcelite.com/c64/main/subroutine/zesnew.html) | Zero-fill memory from SC(1 0) to the end of the page |

---
*Fonte originale: [https://elite.bbcelite.com/c64/indexes/subroutines.html](https://elite.bbcelite.com/c64/indexes/subroutines.html)*

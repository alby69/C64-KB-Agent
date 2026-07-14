---
title: The NES combat demo
source_url: https://elite.bbcelite.com/deep_dives/the_nes_combat_demo.html
category: manual
topics:
- assembly
difficulty: beginner
language: mixed
hardware:
- CPU
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

# The NES combat demo

## How the scroll text and combat practice works

One of the more entertaining features that the authors added to NES Elite is the combat demo. Bookended by 3D scroll texts, this optional part of the game gives you a pretty powerful ship and pits you against three relatively sleepy enemies, whom you have to eliminate in a timed bout of combat practice:

![The combat demo in NES Elite](https://elite.bbcelite.com/images/nes/demo/combat_practice.png) 

						It's a pleasant way to get familiar with the flight controls without the pressures of the live game, and you can jump into practice at any point by pressing Start on the title screen (though for pilots who don't need any more lessons, pressing Select will skip the demo and jump straight to the game).

The NES combat demo owes a lot to the 6502 Second Processor version of Elite, whose own demo mode is described in the deep dive on [the 6502 Second Processor demo mode](https://elite.bbcelite.com/6502sp_demo_mode.html). The same routines are used in both to display the 3D Star Wars scroll text, just with a few tweaks to reduce the amount of text shown on-screen in the NES version, and although the original 1985 demo wasn't playable and only showed a few ships flying around in a fixed pattern, the approach of having a flight loop outside of the main game is the same. And the idea of an auto-playing demo is carried over to the NES version too, as the game will play against itself if left alone long enough (see the deep dive on [auto-playing the NES combat demo](https://elite.bbcelite.com/auto-playing_the_combat_demo.html) for details).

Let's take a look at what makes the combat demo tick.

## The scroll text

													 ---------------

						The combat demo kicks off with an homage to the opening scroll text from Star Wars, which scrolls up the screen and into the far distance while David Whittaker's "Assassin's Touch" plays in the background. This music was composed specially for the NES version - see the deep dive on [music in NES Elite](https://elite.bbcelite.com/music_in_nes_elite.html) for more details.

Here's the opening scroll text from the demo:

![The scroll text in NES Elite](https://elite.bbcelite.com/images/nes/demo/scrolltext_1.png) 

						![The scroll text in NES Elite](https://elite.bbcelite.com/images/nes/demo/scrolltext_2.png) 

						As with the 6502 Second Processor version, the scroll text is implemented using the in-game 3D graphics engine, with the text being made up of lines that work in the exact same way as the lines in a wireframe ship, and which are drawn by the same line-drawing routines.

The [ShowScrollText](https://elite.bbcelite.com/nes/bank_6/subroutine/showscrolltext.html) routine sets up the screen for the demo, and then it calls [DrawScrollText](https://elite.bbcelite.com/nes/bank_6/subroutine/drawscrolltext.html) to start drawing the first scroll text. The text for this first scroll text is language-dependent, with the text coming from [scrollText1_EN](https://elite.bbcelite.com/nes/bank_6/variable/scrolltext1_en.html), [scrollText1_DE](https://elite.bbcelite.com/nes/bank_6/variable/scrolltext1_de.html) or [scrollText1_FR](https://elite.bbcelite.com/nes/bank_6/variable/scrolltext1_fr.html) as appropriate. The text is passed to the [DrawScrollFrames](https://elite.bbcelite.com/nes/bank_6/subroutine/drawscrollframes.html) routine, which in turn repeatedly calls the [DrawScrollFrame](https://elite.bbcelite.com/nes/bank_6/subroutine/drawscrollframe.html) routine to draw each individual frame of the scroll text.

Underlying all of this are the same tables as in the 6502 Second Processor version, but with a few tweaks to make life a bit more efficient when drawing a scroll text into tiles. The 2D letter-writing is implemented by the [GRIDSET](https://elite.bbcelite.com/nes/bank_6/subroutine/gridset.html) routine, which contains letter definitions in the [LTDEF](https://elite.bbcelite.com/nes/bank_6/variable/ltdef.html) table, just as in the 6502 Second Processor version. Characters in the scroll text are drawn using lines on a 3x6 numbered grid like this:

0 1 2 . . . 3 4 5 . . . 6 7 8 9 A B

The low nibble of each byte is the starting point for that line segment, and the high nibble is the end point, so a value of $28, for example, means "draw a line from point 8 to point 2". The LTDEF table contains definitions for all the characters we can use in the scroll text, as lines on the above grid.

The range of characters in the NES version is slightly different, and the paths used to trace the letters have been altered to be more compatible with tiles. As an example, take the letter "A", which looks like this in the 6502 Second Processor version:

$60, $02, $28, $35, $00

In the NES version the same shape is encoded like this:

$06, $02, $28, $35, $00

The first line is different - instead of going from position 0 down to position 6, we now go up from 6 to 0. This is because the next line starts from 0, so the new ordering ensures that lines are drawn more continuously, which helps to ensure fewer gaps in the lines if we start to run low on spare patterns. In practice we don't run out of patterns as the text is short enough to fit into the available patterns, but the letters have still been re-coded to minimise the risk.

The maths to project the scroll text onto the NES screen is a bit different to the original, and the NES scroll text disappears more quickly and at a closer distance than in the Second Processor version (which does slow down terribly with the much longer scroll effect, so this fix is a noticeable improvement). But the concept is the same, and the code was clearly lifted and converted directly from the 1985 version, which is nice to see.

## Combat practice

													 ---------------

						Once the scroll text has disappeared into the distance, the code jumps to the [PlayDemo](https://elite.bbcelite.com/nes/bank_0/subroutine/playdemo.html) routine, where combat practice starts. This routine sets up the local bubble for the main event by calling the [SetupDemoUniverse](https://elite.bbcelite.com/nes/bank_7/subroutine/setupdemouniverse.html) routine, and then it configures three ships - a Mamba, a Krait and a Sidewinder - via the [SetupDemoShip](https://elite.bbcelite.com/nes/bank_0/subroutine/setupdemoship.html) routine, before spawning them with the [NWSHP](https://elite.bbcelite.com/nes/bank_0/subroutine/nwshp.html) routine. The ships are configured to fly forwards over our heads before wheeling off to the sides, and it's really quite atmospheric, especially as another brand new David Whittaker tune, "Game Theme", starts to play as the ships appear.

The ship-spawning process is interesting as it relies on the way that the main loop in NES Elite has been split into smaller parts (as described in the deep dive on [splitting the main loop in the NES version](https://elite.bbcelite.com/splitting_the_main_loop_in_the_nes_version.html)). As each ship is spawned, the demo runs a fixed number of frames of the main flight loop, so the ships fly forwards and over our heads, one after the other. This is all controlled by calls to the [RunDemoFlightLoop](https://elite.bbcelite.com/nes/bank_0/subroutine/rundemoflightloop.html) routine, which in turn runs a fixed number of iterations of the flight loop via the [FlightLoop4To16](https://elite.bbcelite.com/nes/bank_0/subroutine/flightloop4to16.html) routine.

After spawning the three ships, the demo code hands over control to [part 5 of the main game loop](https://elite.bbcelite.com/nes/bank_0/subroutine/main_game_loop_part_5_of_6.html) to run the combat practice using the same loop as the main game. [Part 15 of the flight loop](https://elite.bbcelite.com/nes/bank_0/subroutine/main_flight_loop_part_15_of_16.html#ma93) contains code that checks whether we are in the demo rather than the main game, and if we have killed all three ships then it jumps back to [ShowScrollText](https://elite.bbcelite.com/nes/bank_6/subroutine/showscrolltext.html) to show the results in a scroll text like this:

![The scroll text in NES Elite](https://elite.bbcelite.com/images/nes/demo/results_1.png) 

						followed by an introduction to the rest of the game:

![The scroll text in NES Elite](https://elite.bbcelite.com/images/nes/demo/results_2.png) 

						![The scroll text in NES Elite](https://elite.bbcelite.com/images/nes/demo/results_3.png) 

						## Timing the results

													 ------------------

						The combat demo is timed, and as you can see above, the total time taken is shown as a scroll text once the third ship has been destroyed. The time taken is measured by the ([nmiTimerHi](https://elite.bbcelite.com/nes/common/workspace/zp.html#nmitimerhi) [nmiTimerLo](https://elite.bbcelite.com/nes/common/workspace/zp.html#nmitimerlo)) counter, which gets incremented by the NMI handler once every 50 VBlanks. On the PAL version this means the counter ticks up exactly once a second, while on the NTSC version it ticks up every 0.8333 seconds (so the timings on the NTSC version are inaccurate).

The scroll text showing the results is again language-dependent, with the text coming from [scrollText2_EN](https://elite.bbcelite.com/nes/bank_6/variable/scrolltext2_en.html), [scrollText2_DE](https://elite.bbcelite.com/nes/bank_6/variable/scrolltext2_de.html) or [scrollText2_FR](https://elite.bbcelite.com/nes/bank_6/variable/scrolltext2_fr.html) as appropriate. This scroll text contains four special characters, which show the time in (nmiTimerHi nmiTimerLo), broken down into minutes and seconds like this:

- $83 is the first digit of the minutes
- $82 is the second digit of the minutes
- $81 is the first digit of the seconds
- $80 is the second digit of the seconds

The [GRIDSET](https://elite.bbcelite.com/nes/bank_6/subroutine/gridset.html) routine implements these special values by fetching an ASCII value from the relevant byte in the the K5 variable, and then returning the lines for that character. The locations are as follows:

- Character $83 displays the character whose ASCII code is in location K5+3
- Character $82 displays the character whose ASCII code is in location K5+2
- Character $81 displays the character whose ASCII code is in location K5+1
- Character $80 displays the character whose ASCII code is in location K5

The [latter part of the ShowScrollText routine](https://elite.bbcelite.com/nes/bank_6/subroutine/showscrolltext.html#scro7) calculates the characters that we need in order to show the value of nmiTimer in minutes and seconds. It then sets the values of K5 though K5+3 to the ASCII characters that represent the individual digits of this time, so the scroll text can incorporate the correct numbers like this:

![The scroll text in NES Elite](https://elite.bbcelite.com/images/nes/demo/results_1.png) 

						On the subject of time, there's a 60 second penalty that's added for each missile that you use during combat practice. This is added by the [FRMIS](https://elite.bbcelite.com/nes/bank_0/subroutine/frmis.html) routine when a missile is launched, which displays the following warning before adding 60 seconds to (nmiTimerHi nmiTimerLo):

![A time penalty being applied in NES Elite](https://elite.bbcelite.com/images/nes/demo/penalty.png) 

						Alas, there don't seem to be any extra points awarded for brazenly shooting down missiles without even blinking. [Alex Ryder](http://www.elitehomepage.org/dkwheel.htm#A53) would not be impressed...

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
0   1   2
   .   .   .
   3   4   5
   .   .   .
   6   7   8
   9   A   B
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
$60, $02, $28, $35, $00
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
$06, $02, $28, $35, $00
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/the_nes_combat_demo.html](https://elite.bbcelite.com/deep_dives/the_nes_combat_demo.html)*

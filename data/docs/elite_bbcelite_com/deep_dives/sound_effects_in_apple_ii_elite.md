---
title: Sound effects in Apple II Elite
source_url: https://elite.bbcelite.com/deep_dives/sound_effects_in_apple_ii_elite.html
category: deep-dive
topics:
- memory management
- assembly
- sound generation
- basic
difficulty: beginner
language: mixed
hardware:
- KERNAL
- SID
- CPU
- CIA
related:
- sid-registers
- sound-programming
- joystick-reading
- keyboard-handling
- kernal-routines
- memory-map
- music-player
- cia-registers
scraped_at: '2026-07-20'
---

# Sound effects in Apple II Elite

## Attempting to make game sounds from a single, solitary click

One of the things I love about analysing assembly code from the 1980s is just how close you get to the hardware. There's nowhere to hide: there's absolutely nothing between the machine code (which we choose to write down as assembly language) and the voltages on the chip legs inside the box.

Take this example. 6502 assembly instructions are essentially representations of bit patterns, so if we consider the LDA #7 instruction, this is just a way of writing $A9 $07 in machine code, or %10101011 %00000111 if we think of it in binary. When this instruction is sent to the CPU, the zeroes and ones in the binary machine code are passed into the silicon with 5v for a set bit and 0v for a clear bit, giving the following voltages on the D0-D7 pins along the right edge of the 6502's black plastic DIP package:

```
    LDA                         #7
  = $A9                         $07
  = 1010 1001                   0000 0111
  = 5v 0v 5v 0v 5v 0v 0v 5v     0v 0v 0v 0v 0v 5v 5v 5v
```
						The 6502 doesn't use microcode, so by writing in assembly language, we are literally configuring the voltages in each beat of the CPU's silicon heart. For those of us who work as modern coders, this is such a breath of fresh air. There is no game engine, no framework, no compiler, no interpreter, no API, no bytecode, no library, no virtualisation, no kernel, no BIOS, no microcode and no operating system. It's surprisingly liberating.

More than any other version of Elite, the Apple II celebrates this simplicity and puts you directly in touch with the hardware. It does it with the disk routines (see the deep dive on [file operations with embedded Apple DOS](https://elite.bbcelite.com/file_operations_with_embedded_apple_dos.html)), and it does it with the interference patterns that colour the high-resolution graphics (see the deep dive on [drawing pixels in the Apple II version](https://elite.bbcelite.com/drawing_pixels_in_the_apple_ii_version.html)).

But in the case of the sound effects in Apple II Elite, this simplicity is almost brutalist, because while all the other 6502 systems that run Elite have dedicated sound chips that manage the generation of the game sounds, the Apple II has just a single, solitary click, and that's it. Heck, the stock Apple II doesn't even have timers or expose any interrupts that we can use to build our own sound driver. This is bare-metal binary at its finest.

Let's see how Elite manages to add its own click-track to everything from a laser beam to a missile launch.

## Making sounds on the Apple II

													 -----------------------------

						In the Apple II, there is only one way to make sound. The speaker is mapped to a soft switch at address $C030 (called SPEAKER). Accessing this address in any way, using any kind of write or read instruction, will move the position of the speaker cone once, either from "in" to "out", or from "out" to "in".

Each movement makes a clicking sound, and you can create notes by moving the speaker in and out at high-enough frequencies, which generates sound as a square wave. Higher notes need higher frequency clicks while lower notes need lower frequency clicks, and this corresponds to a shorter pause between clicks giving a higher note, and a longer pause between clicks giving a lower note. The pause between clicks is known as the period, so higher notes consist of more rapid clicks at higher frequencies and with shorter periods, while lower notes have lower frequencies and longer periods.

And that's it. To make any kind of sound, Elite has to make the correct number of clicks with the correct period to create the desired sound. Randomly changing the period while making a sound can create a white noise effect (which is particularly useful for explosions), and sounds can rise or fall in pitch by shortening or lengthening the period between each click.

Elite chooses to use the LDA $C030 instruction to create each click, so each time you see this instruction, that moves the speaker cone in or out. Sound effects are typically implemented using a loop where we make one click on each iteration around the loop. The length of the sound is defined by the number of iterations we make around this loop, and the pitch and type of sound is defined by the amount of time we pause between each iteration (which defines the amount of time between each click - in other words, it defines the period).

There is no sound chip, there is no sound synthesis, there is no operating system sound call, there is interrupt-driven background sound, and there is nowhere to hide. Let's see what Elite does with this incredibly basic sound system.

## The game sounds in Apple II Elite

													 ---------------------------------

						There are various sound routines in the Apple version of Elite. Some take parameters and can generate multiple sounds from the same loop structure, while others are dedicated to making specific noises.

Here's a list of all the sound routines, with details of where they are called from and the sounds they make. There is more explanation after the table.

| Routine | Sound effect | Called by | Clicks | Period loops | 
|---|---|---|---|---|
| [CLICK](https://elite.bbcelite.com/apple/main/subroutine/click.html) | Toggle the state of the speaker | [BOMBOFF](https://elite.bbcelite.com/apple/main/subroutine/bomboff.html) | 1 | N/A | 
| [LASNOISE](https://elite.bbcelite.com/apple/main/subroutine/lasnoise.html) | Our laser firing | [Main flight loop (Part 3 of 16)](https://elite.bbcelite.com/apple/main/subroutine/main_flight_loop_part_3_of_16.html) | 12 | 150 +2 each loop | 
| [LASNOISE](https://elite.bbcelite.com/apple/main/subroutine/lasnoise.html) | Us being hit by lasers | [TACTICS (Part 6 of 7)](https://elite.bbcelite.com/apple/main/subroutine/tactics_part_6_of_7.html) | 12 | 150 +2 each loop | 
| [SOBLIP](https://elite.bbcelite.com/apple/main/subroutine/soblip.html) | E.C.M (called once per main loop iteration while ECMA counts from 32 down to 1) | [Main flight loop (Part 16 of 16)](https://elite.bbcelite.com/apple/main/subroutine/main_flight_loop_part_16_of_16.html) | 21 | ECMA + 192 | 
| [SOBLIP](https://elite.bbcelite.com/apple/main/subroutine/soblip.html) | Hyperspace drive being engaged (called multiple times, passing a period in X that goes from 255 to 185 in jumps of 10) | [LL164](https://elite.bbcelite.com/apple/main/subroutine/ll164.html) | 91 | 255 for 90 loops 245 for 90 loops ... 195 for 90 loops 185 for 90 loop | 
| [SOBOMB](https://elite.bbcelite.com/apple/main/subroutine/sobomb.html) | Energy bomb (called once with each new zig-zag lightning bolt) | [BOMBEFF2](https://elite.bbcelite.com/apple/main/subroutine/bombeff2.html) | 26 | 7 * RND(224, 255) | 
| [SOBEEP](https://elite.bbcelite.com/apple/main/subroutine/sobeep.html) | Long, low beep | [BOOP](https://elite.bbcelite.com/apple/main/subroutine/boop.html) | 100 | 255 | 
| [SOBEEP](https://elite.bbcelite.com/apple/main/subroutine/sobeep.html) | Short, high beep | [BEEP](https://elite.bbcelite.com/apple/main/subroutine/beep.html)/[BELL](https://elite.bbcelite.com/apple/main/subroutine/bell.html) | 31 | 110 | 
| [SOEXPL](https://elite.bbcelite.com/apple/main/subroutine/soexpl.html) | Laser strike on another ship | [EXNO](https://elite.bbcelite.com/apple/main/subroutine/exno.html) | 16 | 50 + 7 * RND(255) +1 each loop | 
| [SOEXPL](https://elite.bbcelite.com/apple/main/subroutine/soexpl.html) | Collision, exploding cargo canister/missile | [EXNO3](https://elite.bbcelite.com/apple/main/subroutine/exno3.html) | 41 | 50 + 7 * RND(255) +1 each loop | 
| [SOEXPL](https://elite.bbcelite.com/apple/main/subroutine/soexpl.html) | Ship exploding | [EXNO2](https://elite.bbcelite.com/apple/main/subroutine/exno2.html) | 56 | 50 + 7 * RND(255) +1 each loop | 
| [SOEXPL](https://elite.bbcelite.com/apple/main/subroutine/soexpl.html) | Us dying | [DEATH](https://elite.bbcelite.com/apple/main/subroutine/death.html) | 211 | 50 + 7 * RND(255) +1 each loop | 
| [SOHISS](https://elite.bbcelite.com/apple/main/subroutine/sohiss.html) | Launch or hyperspace tunnel (called for each ring) | [HFS2](https://elite.bbcelite.com/apple/main/subroutine/hfs2.html) | 11 | RND(255) | 
| [SOHISS](https://elite.bbcelite.com/apple/main/subroutine/sohiss.html) | Enemy missile launch | [SFRMIS](https://elite.bbcelite.com/apple/main/subroutine/sfrmis.html) | 51 | RND(255) | 
| [SOHISS](https://elite.bbcelite.com/apple/main/subroutine/sohiss.html) | Our missile launch | [FRMIS](https://elite.bbcelite.com/apple/main/subroutine/frmis.html) | 121 | RND(255) | 
| [SOHISS](https://elite.bbcelite.com/apple/main/subroutine/sohiss.html) | Launching from a station (called twice in succession) | [LAUN](https://elite.bbcelite.com/apple/main/subroutine/laun.html) | 257 | RND(255) | 

In the above, RND(x) represents a random number between 0 and x inclusive, while RND(x, y) represents a random number between x and y inclusive.

The number of clicks defines the length of each sound, with the speaker moving in on one click and out on the next. If this value is passed to the sound routine as a parameter, then it is passed in the Y register. If a parameter is passed, then the number of clicks made is the parameter value plus 1, as every sound routine ends with an extra click.

The number of period loops defines the length of the pause between each click, so this defines the pitch and type of the sound effect. If this is passed to the sound routine as a parameter, it is passed in the X register.

Let's take a closer look at how these different sounds are generated.

## A simple beep

													 -------------

						Some sound effects are very simple, and the short, high beep generated by the [BEEP](https://elite.bbcelite.com/apple/main/subroutine/beep.html) routine is a good example. This sets two parameters - the length of the sound in Y (which is set to 30 for a short beep) and the period in X (which is set to 110 for a high beep) - and calls the [SOBEEP](https://elite.bbcelite.com/apple/main/subroutine/sobeep.html) routine, which contains the following sound loop:

STX T3 \ Store the period in T3 .BEEPL1 LDA $C030 \ 4 CPU cycles LDX T3 \ 3 CPU cycles DEX \ 2 CPU cycles BNE P%-1 \ 3 CPU cycles when branch is taken, 2 otherwise DEY \ 2 CPU cycles BNE BEEPL1 \ 3 CPU cycles when branch is taken, 2 otherwise

Inside the loop I have noted the number of cycles that each instruction takes, to feed into the following discussion. See the [SOBEEP](https://elite.bbcelite.com/apple/main/subroutine/sobeep.html) routine in the annotated source for an explanation of what the instructions actually do.

For a short, high beep sound, we enter the BEEPL1 loop with the number of iterations in Y (which was set to 30 by BEEP) and the period in T3 (which we've set to 110 with the STX T3 instruction). The loop now does the following:

- Make a click, which takes four CPU cycles for the LDA $C030 instruction.
- Set X to the period length in T3 (which we already set to 110), using a load instruction from zero page that takes three CPU cycles.
- Wait for a total of 5 * 110 - 1 CPU cycles, as each DEX takes two cycles and each successful BNE takes three cycles, giving five cycles per loop, and we repeat the loop X times where X = 110, with the final non-branching BNE taking two cycles rather than three (so we subtract one cycle). The branch destination of P%-1 means we branch back one instruction, so we keep repeating the DEX and BNE instructions until X reaches zero.
- Repeat the process 30 times (as Y = 30), taking another two and three cycles on each iteration to do the DEY and BNE instructions (with the final BNE only taking two cycles as the last branch is not taken).

There is one more final click after the end of this loop, so in all the BEEP routine makes 31 clicks, with a pause between each click of:

4 + 3 + 5 * 110 - 1 + 2 + 3 = 561 CPU cycles

To be totally accurate, there is a pause of 560 cycles before the final click, but this isn't significant.

The standard Apple II has its 6502 CPU clocked at 1.023 MHz, so each cycle takes around:

1 / 1,023,000 seconds = 0.000000978 seconds

(The Apple's CPU timing is a bit more convoluted than this, but this figure is close enough for our purposes.)

So BEEP makes a click every 561 cycles, which is every:

561 * 0.000000978 = 0.0005484 seconds

or:

1 / 0.0005484 = 1824 clicks per second

Each click represents one half of a square wave - with the speaker either going in or out to represent the wave going up or down - so this is equivalent to a square wave of frequency:

1824 / 2 = 912 Hz

This is pretty close to the frequency of A# in octave 5 (which is 923 Hz), so this is indeed a high beep sound. It lasts for 30 iterations, so that's:

30 * 0.0005484 = 0.016 seconds

which is indeed a short, high beep.

For the lower, longer beep that's produced by the [BOOP](https://elite.bbcelite.com/apple/main/subroutine/boop.html) routine, we enter the exact same loop, but with the number of iterations in Y set to 99 and the period in T3 set to 255. This leads to a pause between clicks of:

4 + 3 + 5 * 255 - 1 + 5 = 1286 CPU cycles

This is every:

1286 * 0.000000978 = 0.0012571 seconds

or:

1 / 0.0012571 = 795 clicks per second

which is a square wave with a frequency of:

795 / 2 = 398 Hz

This is around the frequency of G in octave 4 (which is 392 Hz), so that's a nice low beep sound. It lasts for 99 iterations, so that's:

99 * 0.0012571 = 0.12 seconds

which is quite a lot longer than the short beep.

All of the sound generation routines follow this same pattern: there's a loop of a specific duration, during which one click is made and we pause for the specified period before moving on the next click. It's the behaviour of the period during this loop that defines the sound, so let's take a look at a slightly more complicated example.

## Variable pitch

													 --------------

						One approach to creating new sound effects is to vary the period as the sound progresses, causing the sound's frequency to rise or fall. The E.C.M. sound produced by [SOBLIP](https://elite.bbcelite.com/apple/main/subroutine/soblip.html) is a good example of this, as the period in T3 gets decremented on each iteration, so the length of the pause between clicks goes down and the sound's frequency goes up.
						

This is achieved with a couple of relatively simple changes to the beep routine above:

.BEEPL2 LDA $C030 \ 4 CPU cycles DEC T3 \ 5 CPU cycles LDX T3 \ 3 CPU cycles DEX \ 2 CPU cycles NOP \ 2 CPU cycles BNE P%-2 \ 3 CPU cycles when branch is taken, 2 otherwise DEY \ 2 CPU cycles BNE BEEPL2 \ 3 CPU cycles when branch is taken, 2 otherwise

During each iteration, the period in T3 now gets decremented, so the pause code does one less loop on each successive iteration and the sound's frequency goes up. The pause code takes two more cycles per loop when compared to BEEP, as there is an extra NOP in there (which takes two cycles, so this lowers the sound's frequency compared to BEEP), but the logic is otherwise the same.

So each call to SOBLIP produces a sound that rises in frequency, and to make the full E.C.M. sound, we call SOBLIP once on each iteration of the main loop, passing the value of the E.C.M. counter into the routine as the starting period. The actual value passed is ECMA + 192, where ECMA counts down from 31 to 1 while the E.C.M. is activated, decrementing once on each main loop iteration. So the E.C.M. sound is made up of a sequence of pulse sounds, each of which rises in frequency as it plays, with the starting frequency of each pulse rising over the course of the whole sound (as the starting period drops as ECMA counts down).

The [LASNOISE](https://elite.bbcelite.com/apple/main/subroutine/lasnoise.html) routine, which makes the sound of our lasers firing, works along similar lines. It looks like this:

.BEEPL3 LDA $C030 \ 4 CPU cycles INC T3 \ 5 CPU cycles INC T3 \ 5 CPU cycles LDX T3 \ 3 CPU cycles DEX \ 2 CPU cycles BNE P%-1 \ 3 CPU cycles when branch is taken, 2 otherwise DEY \ 2 CPU cycles BNE BEEPL3 \ 3 CPU cycles when branch is taken, 2 otherwise

This is similar to the E.C.M. sound, except the period in T3 gets incremented twice on each loop rather than being decremented once, so the sound goes down in frequency, twice as fast as the E.C.M. sound goes up. And because LASNOISE doesn't have the extra NOP either, the overall frequency is higher than in the E.C.M. sound.

## White noise

													 -----------

						Another approach is to vary the period randomly on each iteration, to produce white noise. The [SOHISS](https://elite.bbcelite.com/apple/main/subroutine/sohiss.html) routine is a good example, with a loop that looks like this:

.SOHISS2 LDA $C030 \ 4 CPU cycles JSR DORND \ 42 CPU cycles DEX \ 2 CPU cycles NOP \ 2 CPU cycles NOP \ 2 CPU cycles BNE P%-3 \ 3 CPU cycles when branch is taken, 2 otherwise DEY \ 2 CPU cycles BNE SOHISS2 \ 3 CPU cycles when branch is taken, 2 otherwise

This isn't that different from the SOBEEP routine, except the length of the pause in each iteration, which is stored in the X register, is set to a random number between 0 and 255 by calling DORND, with the number changing for each pause loop. Each iteration of the pause loop takes nine clock cycles, as there are two NOP instructions in the loop, each of which takes two cycles. Also, the JSR DORND routine itself takes 42 cycles, so on average the period for this sound will be quite a lot longer than our standard beep, and it will also vary considerably between each click of the loudspeaker, leading to white noise.

The only parameter that is passed to the SOHISS routine is the length of the sound effect, so an enemy missile launch will last 50 iterations, compared to our missile launch at 120 iterations. The actual sound will be the same, though.

## White noise and variable pitch

													 ------------------------------

						Finally there is the [SOEXPL](https://elite.bbcelite.com/apple/main/subroutine/soexpl.html) routine, which combines random white noise with an increasing period, like this:

.BEEPL4 LDA $C030 \ 4 CPU cycles INC T3 \ 5 CPU cycles LDX T3 \ 3 CPU cycles DEX \ 2 CPU cycles NOP \ 2 CPU cycles NOP \ 2 CPU cycles BNE P%-3 \ 3 CPU cycles when branch is taken, 2 otherwise JSR DORND \ 42 CPU cycles DEX \ 2 CPU cycles NOP \ 2 CPU cycles BNE P%-2 \ 3 CPU cycles when branch is taken, 2 otherwise DEY \ 2 CPU cycles BNE BEEPL4 \ 3 CPU cycles when branch is taken, 2 otherwise

The first part increments the period like [LASNOISE](https://elite.bbcelite.com/apple/main/subroutine/lasnoise.html), while the second part creates white noise like [SOHISS](https://elite.bbcelite.com/apple/main/subroutine/sohiss.html). The overall effect is of a laser strike with a descending pitch, mixed with the white noise of an explosion.

It's also worth noting that when we call one of these sound routines, the entire CPU is devoted to making that sound, and everything else stops. Interestingly, the stock Apple II doesn't actually use any interrupts; these only come into play when expansion cards are fitted, so there is no system-wide interrupt system that we can use to implement background sounds. As a result, we need our sound routines to be short and snappy so they don't hog the processor for too long, or that will slow the game down too much.

So that's how the Apple II version of Elite makes sound effects from nothing but a simple click. The results might not win any prizes, but as an exercise in understanding the very basics of sound generation, it's a fascinating system.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
LDA                         #7
  = $A9                         $07
  = 1010 1001                   0000 0111
  = 5v 0v 5v 0v 5v 0v 0v 5v     0v 0v 0v 0v 0v 5v 5v 5v
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
STX T3               \ Store the period in T3

  .BEEPL1

   LDA $C030            \ 4 CPU cycles

   LDX T3               \ 3 CPU cycles

   DEX                  \ 2 CPU cycles
   BNE P%-1             \ 3 CPU cycles when branch is taken, 2 otherwise

   DEY                  \ 2 CPU cycles

   BNE BEEPL1           \ 3 CPU cycles when branch is taken, 2 otherwise
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
4 + 3 + 5 * 110 - 1 + 2 + 3 = 561 CPU cycles
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
1 / 1,023,000 seconds = 0.000000978 seconds
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
561 * 0.000000978 = 0.0005484 seconds
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
1 / 0.0005484 = 1824 clicks per second
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
1824 / 2 = 912 Hz
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
30 * 0.0005484 = 0.016 seconds
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
4 + 3 + 5 * 255 - 1 + 5 = 1286 CPU cycles
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
1286 * 0.000000978 = 0.0012571 seconds
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
1 / 0.0012571 = 795 clicks per second
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
795 / 2 = 398 Hz
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
99 * 0.0012571 = 0.12 seconds
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
.BEEPL2

   LDA $C030            \ 4 CPU cycles

   DEC T3               \ 5 CPU cycles
   LDX T3               \ 3 CPU cycles

   DEX                  \ 2 CPU cycles
   NOP                  \ 2 CPU cycles
   BNE P%-2             \ 3 CPU cycles when branch is taken, 2 otherwise

   DEY                  \ 2 CPU cycles

   BNE BEEPL2           \ 3 CPU cycles when branch is taken, 2 otherwise
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
.BEEPL3

   LDA $C030            \ 4 CPU cycles

   INC T3               \ 5 CPU cycles
   INC T3               \ 5 CPU cycles
   LDX T3               \ 3 CPU cycles

   DEX                  \ 2 CPU cycles
   BNE P%-1             \ 3 CPU cycles when branch is taken, 2 otherwise

   DEY                  \ 2 CPU cycles

   BNE BEEPL3           \ 3 CPU cycles when branch is taken, 2 otherwise
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
.SOHISS2

   LDA $C030            \ 4 CPU cycles

   JSR DORND            \ 42 CPU cycles

   DEX                  \ 2 CPU cycles
   NOP                  \ 2 CPU cycles
   NOP                  \ 2 CPU cycles
   BNE P%-3             \ 3 CPU cycles when branch is taken, 2 otherwise

   DEY                  \ 2 CPU cycles

   BNE SOHISS2          \ 3 CPU cycles when branch is taken, 2 otherwise
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
.BEEPL4

   LDA $C030            \ 4 CPU cycles

   INC T3               \ 5 CPU cycles
   LDX T3               \ 3 CPU cycles

   DEX                  \ 2 CPU cycles
   NOP                  \ 2 CPU cycles
   NOP                  \ 2 CPU cycles
   BNE P%-3             \ 3 CPU cycles when branch is taken, 2 otherwise

   JSR DORND            \ 42 CPU cycles

   DEX                  \ 2 CPU cycles
   NOP                  \ 2 CPU cycles
   BNE P%-2             \ 3 CPU cycles when branch is taken, 2 otherwise

   DEY                  \ 2 CPU cycles

   BNE BEEPL4           \ 3 CPU cycles when branch is taken, 2 otherwise
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/sound_effects_in_apple_ii_elite.html](https://elite.bbcelite.com/deep_dives/sound_effects_in_apple_ii_elite.html)*

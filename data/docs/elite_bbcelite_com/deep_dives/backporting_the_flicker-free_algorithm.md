---
title: Backporting the flicker-free algorithm
source_url: https://elite.bbcelite.com/deep_dives/backporting_the_flicker-free_algorithm.html
category: deep-dive
topics:
- memory management
- basic
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

# Backporting the flicker-free algorithm

## Applying the BBC Master's flicker-free algorithm to the other versions

Once you've seen the smoother animation and flicker-free ships in BBC Master and Apple II Elite, it does tend to make the older versions look a little less sophisticated. Luckily, the changes that Bell and Braben made for these versions don't require any fancy hardware or more memory; instead, it's all down to an improved ship-drawing algorithm, as explained in the deep dive on [flicker-free ship drawing](https://elite.bbcelite.com/flicker-free_ship_drawing.html) (which you probably want to read before exploring the code below).

This means it's relatively straightforward to backport these changes into all the other versions of 6502 Elite, even the Acorn Electron version and Angus Duggan's Elite-A. Here's a comparison in the latter, with the standard version on the left, and the flicker-free version on the right:

You can play the flicker-free versions via the [releases](https://elite.bbcelite.com/compare/releases.html) page, either in a browser or on real hardware; it's interesting to see the differences on-screen. I have also backported the algorithm to the Commodore 64 version; see the GitHub repository for [flicker-free Elite on the Commodore 64](https://github.com/markmoxon/c64-elite-flicker-free) for details.

There are three steps to the backporting process:

- Free up enough memory for the flicker-free code and the LSNUM and LSNUM2 variables
- Copy the LSPUT line-drawing routine from the Master
- Update the SHPPT and LL9 routines to support the flicker-free algorithm

Interestingly, this backporting process is identical for all the original versions of Elite (i.e. cassette, disc, Electron, 6502 Second Processor and Elite-A). The only difference is that in some cases, we have to move routines around to prevent the extra code from breaking branch instructions that would otherwise have to reach too far. The code changes themselves are the same, as they all share the same SHPPT and LL9 routines.

This is true even for the 6502 Second Processor version, which normally uses a line-queueing system when drawing ships, but we can replace this with the same flicker-free code as the other versions because the flicker-free algorithm draws lines by calling LL30, and this routine still draws a line, even on the Second Processor version, so dropping in the new algorithm just works.

Let's look at these three steps in turn. To be specific, let's look at backporting the flicker-free algorithm to the BBC Micro cassette version. To see the code differences for the other versions, you can check out the flicker-free branches in the accompanying repositories, but the updated routines in all versions are essentially the same as in the code below.

## 1. Finding enough memory

													 ------------------------

						Altogether, the flicker-free changes only require a small number of extra bytes compared to the original versions - in the BBC Micro cassette version, for example, we only need to find eight more bytes. That said, memory usage is famously tight in Elite, so this is easier said than done.

Luckily, all the versions of Elite that have serious memory constraints also contain an unused routine that the authors forgot to remove - it's a [duplicate of MULTU that is never called](https://elite.bbcelite.com/cassette/main/subroutine/unused_duplicate_of_multu.html). Removing this routine (or just commenting out the required number of instructions) easily gives us the space we need, even in Elite-A, where only [half of the duplicate routine](https://elite.bbcelite.com/elite-a/flight/subroutine/unused_duplicate_of_multu.html) is left in the flight code for us to remove.

We also need to find space in zero page for two new variables: LSNUM and LSNUM2. Elite already has one unused variable in zero page called [XX14](https://elite.bbcelite.com/cassette/main/workspace/zp.html#xx14), so we can simply use this for LSNUM. XX14 is followed by [RAT](https://elite.bbcelite.com/cassette/main/workspace/zp.html#rat), which is a temporary variable that isn't used by the ship-drawing routine, so we can reuse the same location for both RAT and LSNUM2, as they won't clash (see below for the code that does this).

So, step 1 is to comment out a chunk of the duplicate MULTU routine, replace XX14 with LSNUM, and share RAT with LSNUM2. Simple.

## 2. Copying over LSPUT

													 ---------------------

						As part of the new algorithm in the Master, there's an extra routine called [LSPUT](https://elite.bbcelite.com/master/main/subroutine/lsput.html), which draws a line, adding the line to the ship line heap (potentially replacing one of the lines already there), and then erasing the line that we just replaced. We need to port this over for the flicker-free code to call, which we can do by simply copying [LSPUT](https://elite.bbcelite.com/master/main/subroutine/lsput.html) directly from the Master, and inserting it after the last stage of the LL9 routine.

So, step 2 is to copy LSPUT from the Master and into the version we are updating. Easy.

## 3. Updating SHPPT and LL9

													 -------------------------

						The SHPPT routine draws ships as points for when they are far away, and the LL9 routine draws them as wireframes when they are closer. As the final step of backporting the new algorithm, we need to update both of these routines so that instead of erasing the whole ship before redrawing the whole ship again, they instead use the new LSPUT routine to draw and erase ships one line at a time.

Below you can see every single code change that we need to make to convert the BBC Micro cassette version to the flicker-free algorithm (specifically, the changes are in SHPPT and parts 1, 9, 10, 11 and 12 of LL9).

So, step 3 is to make the changes below... and then we're done.

## Exploring the code below

													 ------------------------

						To explore the code changes below, simply click a routine header to expand it, and click it again to shrink it back. Within the code that appears, the original and flicker-free code are shown side-by-side. You can tap one side to expand it, and tap it again to go back to showing both sides. Each side is sideways scrollable, so you can read the comments on small screens.

It might look like a lot of code, but that's because I've included all the routines in full, so you can see the differences *in situ*. There are surprisingly few differences between the two versions (especially when you realise that parts 2 to 8 of LL9 are completely unchanged). This is a delightfully simple change that makes a very noticeable improvement to the graphics, and without perceivable loss. That's well worth the effort of backporting, I'd say.

Name: XX14 Type: Variable Category: Zero page variable Summary: Unused variable that we can repurpose

Name: SHPPT Type: Subroutine Category: Drawing ships Summary: Draw a distant ship as a point rather than a full wireframe

Name: LL9 (Part 1 of 12) Type: Subroutine Category: Drawing ships Summary: Draw ship: Check if ship is exploding, check if ship is in front

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`Name`** (unknown): No description available
- **`Type`** (unknown): No description available
- **`Category`** (unknown): No description available
- **`Summary`** (unknown): No description available

```assembly
Name: XX14
       Type: Variable
   Category: Zero page variable
    Summary: Unused variable that we can repurpose
```

### Snippet Codice (BASIC)

```basic
OriginalFlicker-free .XX14

  SKIP 1                \ This byte appears to be unused
 .LSNUM

  SKIP 1                \ The pointer to the current position in the ship line
                        \ heap as we work our way through the new ship's edges
                        \ (and the corresponding old ship's edges) when drawing
                        \ the ship in the main ship-drawing routine at LL9

 .LSNUM2

  SKIP 0                \ The size of the existing ship line heap for the ship
                        \ we are drawing in LL9, i.e. the number of lines in the
                        \ old ship that is currently shown on-screen and which
                        \ we need to erase
```

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`Name`** (unknown): No description available
- **`Type`** (unknown): No description available
- **`Category`** (unknown): No description available
- **`Summary`** (unknown): No description available

```assembly
Name: SHPPT
       Type: Subroutine
   Category: Drawing ships
    Summary: Draw a distant ship as a point rather than a full wireframe


.SHPPT
```

### Snippet Codice (BASIC)

```basic
OriginalFlicker-free JSR EE51               \ Call EE51 to remove the ship's wireframe from the
                        \ screen, if there is one
 (Empty)
```

### Snippet Codice (BASIC)

```basic
JSR PROJ               \ Project the ship onto the screen, returning:
                        \
                        \   * K3(1 0) = the screen x-coordinate
                        \   * K4(1 0) = the screen y-coordinate
                        \   * A = K4+1

 ORA K3+1               \ If either of the high bytes of the screen coordinates
 BNE nono               \ are non-zero, jump to nono as the ship is off-screen

 LDA K4                 \ Set A = the y-coordinate of the dot

 CMP #Y*2-2             \ If the y-coordinate is bigger than the y-coordinate of
 BCS nono               \ the bottom of the screen, jump to nono as the ship's
                        \ dot is off the bottom of the space view
```

### Snippet Codice (BASIC)

```basic
OriginalFlicker-free LDY #2                 \ Call Shpt with Y = 2 to set up bytes 1-4 in the ship
 JSR Shpt               \ lines space, aborting the call to LL9 if the dot is
                        \ off the side of the screen. This call sets up the
                        \ first row of the dot (i.e. a four-pixel dash)

 LDY #6                 \ Set Y to 6 for the next call to Shpt

 LDA K4                 \ Set A = y-coordinate of dot + 1 (so this is the second
 ADC #1                 \ row of the two-pixel high dot)

 JSR Shpt               \ Call Shpt with Y = 6 to set up bytes 5-8 in the ship
                        \ lines space, aborting the call to LL9 if the dot is
                        \ off the side of the screen. This call sets up the
                        \ second row of the dot (i.e. another four-pixel dash,
                        \ on the row below the first one)
 JSR Shpt               \ Call Shpt to draw a horizontal 4-pixel dash for the
                        \ first row of the dot (i.e. a four-pixel dash)
 LDA K4                 \ Set A = y-coordinate of dot + 1 (so this is the second
 CLC                    \ row of the two-pixel high dot)
 ADC #1

 JSR Shpt               \ Call Shpt to draw a horizontal 4-pixel dash for the
                        \ first row of the dot (i.e. a four-pixel dash)
```

### Snippet Codice (BASIC)

```basic
LDA #%00001000         \ Set bit 3 of the ship's byte #31 to record that we
 ORA XX1+31             \ have now drawn something on-screen for this ship
 STA XX1+31
```

### Snippet Codice (BASIC)

```basic
OriginalFlicker-free LDA #8                 \ Set A = 8 so when we call LL18+2 next, byte #0 of the
                        \ heap gets set to 8, for the 8 bytes we just stuck on
                        \ the heap

 JMP LL81+2             \ Call LL81+2 to draw the ship's dot, returning from the
                        \ subroutine using a tail call

 PLA                    \ Pull the return address from the stack, so the RTS
 PLA                    \ below actually returns from the subroutine that called
                        \ LL9 (as we called SHPPT from LL9 with a JMP)
 JMP LSPUT              \ Jump to LSPUT to draw any remaining lines that are
                        \ still in the ship line heap and return from the
                        \ subroutine using a tail call
```

### Snippet Codice (BASIC)

```basic
.nono

 LDA #%11110111         \ Clear bit 3 of the ship's byte #31 to record that
 AND XX1+31             \ nothing is being drawn on-screen for this ship
 STA XX1+31
```

### Snippet Codice (BASIC)

```basic
OriginalFlicker-free RTS                    \ Return from the subroutine

.Shpt

                        \ This routine sets up four bytes in the ship line heap,
                        \ from byte Y-1 to byte Y+2. If the ship's screen point
                        \ turns out to be off-screen, then this routine aborts
                        \ the entire call to LL9, exiting via nono. The four
                        \ bytes define a horizontal 4-pixel dash, for either the
                        \ top or the bottom of the ship's dot

 STA (XX19),Y           \ Store A in byte Y of the ship line heap

 INY                    \ Store A in byte Y+2 of the ship line heap
 INY
 STA (XX19),Y

 LDA K3                 \ Set A = screen x-coordinate of the ship dot

 DEY                    \ Store A in byte Y+1 of the ship line heap
 STA (XX19),Y

 ADC #3                 \ Set A = screen x-coordinate of the ship dot + 3

 BCS nono-2             \ If the addition pushed the dot off the right side of
                        \ the screen, jump to nono-2 to return from the parent
                        \ subroutine early (i.e. LL9). This works because we
                        \ called Shpt from above with a JSR, so nono-2 removes
                        \ that return address from the stack, leaving the next
                        \ return address exposed. LL9 called SHPPT with a JMP.
                        \ so the next return address is the one that was put on
                        \ the stack by the original call to LL9. So the RTS in
                        \ nono will actually return us from the original call
                        \ to LL9, thus aborting the entire drawing process

 DEY                    \ Store A in byte Y-1 of the ship line heap
 DEY
 STA (XX19),Y

 RTS                    \ Return from the subroutine
 JMP LSPUT              \ Jump to LSPUT to draw any remaining lines that are
                        \ still in the ship line heap and return from the
                        \ subroutine 

.Shpt

                        \ This routine draws a horizontal 4-pixel dash, for
                        \ either the top or the bottom of the ship's dot

 STA Y1                 \ Store A in both y-coordinates, as this is a horizontal
 STA Y2                 \ dash at y-coordinate A


 LDA K3                 \ Set A = screen x-coordinate of the ship dot

 STA X1                 \ Store the x-coordinate of the ship dot in X1, as this
                        \ is where the dash starts

 CLC                    \ Set A = screen x-coordinate of the ship dot + 3
 ADC #3

 BCC P%+4               \ If the addition overflowed, set A = 255, the
 LDA #255               \ x-coordinate of the right edge of the screen

 STA X2                 \ Store the x-coordinate of the ship dot in X1, as this
                        \ is where the dash starts

 JMP LSPUT              \ Draw this edge using flicker-free animation, by first
                        \ drawing the ship's new line and then erasing the
                        \ corresponding old line from the screen, and return
                        \ from the subroutine using a tail call
```

### Snippet Codice (BASIC)

```basic
Name: LL9 (Part 1 of 12)
       Type: Subroutine
   Category: Drawing ships
    Summary: Draw ship: Check if ship is exploding, check if ship is in front


 This routine draws the current ship on the screen. This part checks to see if
 the ship is exploding, or if it should start exploding, and if it does it sets
 things up accordingly.

 It also does some basic checks to see if we can see the ship, and if not it
 removes it from the screen.

 In this code, XX1 is used to point to the current ship's data block at INWK
 (the two labels are interchangeable).

 Arguments:

   XX1                  XX1 shares its location with INWK, which contains the
                        zero-page copy of the data block for this ship from the
                        K% workspace

   INF                  The address of the data block for this ship in workspace
                        K%

   XX19(1 0)            XX19(1 0) shares its location with INWK(34 33), which
                        contains the ship line heap address pointer

   XX0                  The address of the blueprint for this ship

 Other entry points:

   EE51                 Remove the current ship from the screen, called from
                        SHPPT before drawing the ship as a point


.LL25

 JMP PLANET             \ Jump to the PLANET routine, returning from the
                        \ subroutine using a tail call

.LL9

 LDA TYPE               \ If the ship type is negative then this indicates a
 BMI LL25               \ planet or sun, so jump to PLANET via LL25 above

 LDA #31                \ Set XX4 = 31 to store the ship's distance for later
 STA XX4                \ comparison with the visibility distance. We will
                        \ update this value below with the actual ship's
                        \ distance if it turns out to be visible on-screen




	OriginalFlicker-free (Empty)
                        \ We now set things up for flicker-free ship plotting,
                        \ by setting the following:
                        \
                        \   LSNUM = offset to the first coordinate in the ship's
                        \           line heap
                        \
                        \   LSNUM2 = the number of bytes in the heap for the
                        \            ship that's currently on-screen (or 0 if
                        \            there is no ship currently on-screen)

 LDY #1                 \ Set LSNUM = 1, the offset of the first set of line
 STY LSNUM              \ coordinates in the ship line heap

 DEY                    \ Decrement Y to 0

 LDA #%00001000         \ If bit 3 of the ship's byte #31 is set, then the ship
 BIT INWK+31            \ is currently being drawn on-screen, so skip the
 BNE P%+5               \ following two instructions

 LDA #0                 \ The ship is not being drawn on screen, so set A = 0
                        \ so that LSNUM2 gets set to 0 below (as there are no
                        \ existing coordinates on the ship line heap for this
                        \ ship)

 EQUB &2C               \ Skip the next instruction by turning it into
                        \ &2C &B1 &BD, or BIT &BDB1 which does nothing apart
                        \ from affect the flags

 LDA (XX19),Y           \ Set LSNUM2 to the first byte of the ship's line heap,
 STA LSNUM2             \ which contains the number of bytes in the heap



 LDA #%00100000         \ If bit 5 of the ship's byte #31 is set, then the ship
 BIT XX1+31             \ is currently exploding, so jump down to EE28
 BNE EE28

 BPL EE28               \ If bit 7 of the ship's byte #31 is clear then the ship
                        \ has not just been killed, so jump down to EE28

                        \ Otherwise bit 5 is clear and bit 7 is set, so the ship
                        \ is not yet exploding but it has been killed, so we
                        \ need to start an explosion

 ORA XX1+31             \ Clear bits 6 and 7 of the ship's byte #31, to stop the
 AND #%00111111         \ ship from firing its laser and to mark it as no longer
 STA XX1+31             \ having just been killed

 LDA #0                 \ Set the ship's acceleration in byte #31 to 0, updating
 LDY #28                \ the byte in the workspace K% data block so we don't
 STA (INF),Y            \ have to copy it back from INWK later

 LDY #30                \ Set the ship's pitch counter in byte #30 to 0, to stop
 STA (INF),Y            \ the ship from pitching

 JSR EE51               \ Call EE51 to remove the ship from the screen

                        \ We now need to set up a new explosion cloud. We
                        \ initialise it with a size of 18 (which gets increased
                        \ by 4 every time the cloud gets redrawn), and the
                        \ explosion count (i.e. the number of particles in the
                        \ explosion), which go into bytes 1 and 2 of the ship
                        \ line heap. See DOEXP for more details of explosion
                        \ clouds

 LDY #1                 \ Set byte #1 of the ship line heap to 18, the initial
 LDA #18                \ size of the explosion cloud
 STA (XX19),Y

 LDY #7                 \ Fetch byte #7 from the ship's blueprint, which
 LDA (XX0),Y            \ determines the explosion count (i.e. the number of
 LDY #2                 \ vertices used as origins for explosion clouds), and
 STA (XX19),Y           \ store it in byte #2 of the ship line heap

                        \ The following loop sets bytes 3-6 of the of the ship
                        \ line heap to random numbers

.EE55

 INY                    \ Increment Y (so the loop starts at 3)

 JSR DORND              \ Set A and X to random numbers

 STA (XX19),Y           \ Store A in the Y-th byte of the ship line heap

 CPY #6                 \ Loop back until we have randomised the 6th byte
 BNE EE55

.EE28

 LDA XX1+8              \ Set A = z_sign

.EE49

 BPL LL10               \ If A is positive, i.e. the ship is in front of us,
                        \ jump down to LL10

.LL14

                        \ The following removes the ship from the screen by
                        \ redrawing it (or, if it is exploding, by redrawing the
                        \ explosion cloud). We call it when the ship is no
                        \ longer on-screen, is too far away to be fully drawn,
                        \ and so on

 LDA XX1+31             \ If bit 5 of the ship's byte #31 is clear, then the
 AND #%00100000         \ ship is not currently exploding, so jump down to EE51
 BEQ EE51               \ to redraw its wireframe

 LDA XX1+31             \ The ship is exploding, so clear bit 3 of the ship's
 AND #%11110111         \ byte #31 to denote that the ship is no longer being
 STA XX1+31             \ drawn on-screen

 JMP DOEXP              \ Jump to DOEXP to display the explosion cloud, which
                        \ will remove it from the screen, returning from the
                        \ subroutine using a tail call

.EE51

 LDA #%00001000         \ If bit 3 of the ship's byte #31 is clear, then there
 BIT XX1+31             \ is already nothing being shown for this ship, so
 BEQ LL10-1             \ return from the subroutine (as LL10-1 contains an RTS)

 EOR XX1+31             \ Otherwise flip bit 3 of byte #31 and store it (which
 STA XX1+31             \ clears bit 3 as we know it was set before the EOR), so
                        \ this sets this ship as no longer being drawn on-screen




	OriginalFlicker-free JMP LL155              \ Jump to LL155 to draw the ship, which removes it from
                        \ the screen, returning from the subroutine using a
                        \ tail call
 JMP LSPUT              \ Jump to LSPUT to draw the ship, which removes it from
                        \ the screen, returning from the subroutine using a
                        \ tail call



 RTS                    \ Return from the subroutine




       Name: LL9 (Part 9 of 12)
       Type: Subroutine
   Category: Drawing ships
    Summary: Draw ship: Draw laser beams if the ship is firing its laser at us


 This part sets things up so we can loop through the edges in the next part. It
 also adds a line to the ship line heap, if the ship is firing at us.

 When we get here, the heap at XX3 contains all the visible vertex screen
 coordinates.


.LL72

 LDA XX1+31             \ If bit 5 of the ship's byte #31 is clear, then the
 AND #%00100000         \ ship is not currently exploding, so jump down to EE31
 BEQ EE31

 LDA XX1+31             \ The ship is exploding, so set bit 3 of the ship's byte
 ORA #8                 \ #31 to denote that we are drawing something on-screen
 STA XX1+31             \ for this ship

 JMP DOEXP              \ Jump to DOEXP to display the explosion cloud,
                        \ returning from the subroutine using a tail call

.EE31




	OriginalFlicker-free LDA #%00001000         \ If bit 3 of the ship's byte #31 is clear, then there
 BIT XX1+31             \ is nothing already being shown for this ship, so skip
 BEQ LL74               \ to LL74 as we don't need to erase anything from the
                        \ screen

 JSR LL155              \ Otherwise call LL155 to draw the existing ship, which
                        \ removes it from the screen
 LDY #9                 \ Fetch byte #9 of the ship's blueprint, which is the
 LDA (XX0),Y            \ number of edges, and store it in XX20
 STA XX20



 LDA #%00001000         \ Set bit 3 of A so the next instruction sets bit 3 of
                        \ the ship's byte #31 to denote that we are drawing
                        \ something on-screen for this ship

.LL74

 ORA XX1+31             \ Apply bit 3 of A to the ship's byte #31, so if there
 STA XX1+31             \ was no ship already on screen, the bit is clear,
                        \ otherwise it is set




	OriginalFlicker-free LDY #9                 \ Fetch byte #9 of the ship's blueprint, which is the
 LDA (XX0),Y            \ number of edges, and store it in XX20
 STA XX20

 LDY #0                 \ We are about to step through all the edges, using Y
                        \ as a counter

 STY U                  \ Set U = 0 (though we increment it to 1 below)

 STY XX17               \ Set XX17 = 0, which we are going to use as a counter
                        \ for stepping through the ship's edges

 INC U                  \ We are going to start calculating the lines we need to
                        \ draw for this ship, and will store them in the ship
                        \ line heap, using U to point to the end of the heap, so
                        \ we start by setting U = 1
 LDY #0                 \ Set XX17 = 0, which we are going to use as a counter
 STY XX17               \ for stepping through the ship's edges




 BIT XX1+31             \ If bit 6 of the ship's byte #31 is clear, then the
 BVC LL170              \ ship is not firing its lasers, so jump to LL170 to
                        \ skip the drawing of laser lines

                        \ The ship is firing its laser at us, so we need to draw
                        \ the laser lines

 LDA XX1+31             \ Clear bit 6 of the ship's byte #31 so the ship doesn't
 AND #%10111111         \ keep firing endlessly
 STA XX1+31

 LDY #6                 \ Fetch byte #6 of the ship's blueprint, which is the
 LDA (XX0),Y            \ number * 4 of the vertex where the ship has its lasers

 TAY                    \ Put the vertex number into Y, where it can act as an
                        \ index into list of vertex screen coordinates we added
                        \ to the XX3 heap

 LDX XX3,Y              \ Fetch the x_lo coordinate of the laser vertex from the
 STX XX15               \ XX3 heap into XX15

 INX                    \ If X = 255 then the laser vertex is not visible, as
 BEQ LL170              \ the value we stored in part 2 wasn't overwritten by
                        \ the vertex calculation in part 6 and 7, so jump to
                        \ LL170 to skip drawing the laser lines

                        \ We now build a laser beam from the ship's laser vertex
                        \ towards our ship, as follows:
                        \
                        \   XX15(1 0) = laser vertex x-coordinate
                        \
                        \   XX15(3 2) = laser vertex y-coordinate
                        \
                        \   XX15(5 4) = x-coordinate of the end of the beam
                        \
                        \   XX12(1 0) = y-coordinate of the end of the beam
                        \
                        \ The end of the laser beam will be set positioned to
                        \ look good, rather than being directly aimed at us, as
                        \ otherwise we would only see a flashing point of light
                        \ as they unleashed their attack

 LDX XX3+1,Y            \ Fetch the x_hi coordinate of the laser vertex from the
 STX XX15+1             \ XX3 heap into XX15+1

 INX                    \ If X = 255 then the laser vertex is not visible, as
 BEQ LL170              \ the value we stored in part 2 wasn't overwritten by
                        \ a vertex calculation in part 6 and 7, so jump to LL170
                        \ to skip drawing the laser beam

 LDX XX3+2,Y            \ Fetch the y_lo coordinate of the laser vertex from the
 STX XX15+2             \ XX3 heap into XX15+2

 LDX XX3+3,Y            \ Fetch the y_hi coordinate of the laser vertex from the
 STX XX15+3             \ XX3 heap into XX15+3

 LDA #0                 \ Set XX15(5 4) = 0, so their laser beam fires to the
 STA XX15+4             \ left edge of the screen
 STA XX15+5

 STA XX12+1             \ Set XX12(1 0) = the ship's z_lo coordinate, which will
 LDA XX1+6              \ effectively make the vertical position of the end of
 STA XX12               \ the laser beam move around as the ship moves in space

 LDA XX1+2              \ If the ship's x_sign is positive, skip the next
 BPL P%+4               \ instruction

 DEC XX15+4             \ The ship's x_sign is negative (i.e. it's on the left
                        \ side of the screen), so switch the laser beam so it
                        \ goes to the right edge of the screen by decrementing
                        \ XX15(5 4) to 255

 JSR LL145              \ Call LL145 to see if the laser beam needs to be
                        \ clipped to fit on-screen, returning the clipped line's
                        \ end-points in (X1, Y1) and (X2, Y2)

 BCS LL170              \ If the C flag is set then the line is not visible on
                        \ screen, so jump to LL170 so we don't store this line
                        \ in the ship line heap




	OriginalFlicker-free LDY U                  \ Fetch the ship line heap pointer, which points to the
                        \ next free byte on the heap, into Y

 LDA XX15               \ Add X1 to the end of the heap
 STA (XX19),Y

 INY                    \ Increment the heap pointer

 LDA XX15+1             \ Add Y1 to the end of the heap
 STA (XX19),Y

 INY                    \ Increment the heap pointer

 LDA XX15+2             \ Add X2 to the end of the heap
 STA (XX19),Y

 INY                    \ Increment the heap pointer

 LDA XX15+3             \ Add Y2 to the end of the heap
 STA (XX19),Y

 INY                    \ Increment the heap pointer

 STY U                  \ Store the updated ship line heap pointer in U
 JSR LSPUT              \ Draw the laser line using flicker-free animation, by
                        \ first drawing the new laser line and then erasing the
                        \ corresponding old line from the screen




       Name: LL9 (Part 10 of 12)
       Type: Subroutine
   Category: Drawing ships
    Summary: Draw ship: Calculate the visibility of each of the ship's edges
             and, for flicker-free only, draw the visible ones


 This part calculates which edges are visible - in other words, which lines we
 should draw - and clips them to fit on the screen.

 When we get here, the heap at XX3 contains all the visible vertex screen
 coordinates.


.LL170

 LDY #3                 \ Fetch byte #3 of the ship's blueprint, which contains
 CLC                    \ the low byte of the offset to the edges data
 LDA (XX0),Y

 ADC XX0                \ Set V = low byte edges offset + XX0
 STA V

 LDY #16                \ Fetch byte #16 of the ship's blueprint, which contains
 LDA (XX0),Y            \ the high byte of the offset to the edges data

 ADC XX0+1              \ Set V+1 = high byte edges offset + XX0+1
 STA V+1                \
                        \ So V(1 0) now points to the start of the edges data
                        \ for this ship




	OriginalFlicker-free LDY #5                 \ Fetch byte #5 of the ship's blueprint, which contains
 LDA (XX0),Y            \ the maximum heap size for plotting the ship (which is
 STA T1                 \ 1 + 4 * the maximum number of visible edges) and store
                        \ it in T1

 LDY XX17               \ Set Y to the edge counter in XX17

.LL75
 LDY #5                 \ Fetch byte #5 of the ship's blueprint, which contains
 LDA (XX0),Y            \ the maximum heap size for plotting the ship (which is
 STA CNT                \ 1 + 4 * the maximum number of visible edges) and store
                        \ it in CNT

.LL75

 LDY #0                 \ Set Y = 0 so we start with byte #0



 LDA (V),Y              \ Fetch byte #0 for this edge, which contains the
                        \ visibility distance for this edge, beyond which the
                        \ edge is not shown

 CMP XX4                \ If XX4 > the visibility distance, where XX4 contains
 BCC LL78               \ the ship's z-distance reduced to 0-31 (which we set in
                        \ part 2), then this edge is too far away to be visible,
                        \ so jump down to LL78 to move on to the next edge

 INY                    \ Increment Y to point to byte #1

 LDA (V),Y              \ Fetch byte #1 for this edge into A, so:
                        \
                        \   A = %ffff ffff, where:
                        \
                        \     * Bits 0-3 = the number of face 1
                        \
                        \     * Bits 4-7 = the number of face 2




	OriginalFlicker-free INY                    \ Increment Y to point to byte #2
 (Empty)



 STA P                  \ Store byte #1 into P

 AND #%00001111         \ Extract the number of face 1 into X
 TAX

 LDA XX2,X              \ If XX2+X is non-zero then we decided in part 5 that
 BNE LL79               \ face 1 is visible, so jump to LL79

 LDA P                  \ Fetch byte #1 for this edge into A

 LSR A                  \ Shift right four times to extract the number of face 2
 LSR A                  \ from bits 4-7 into X
 LSR A
 LSR A
 TAX

 LDA XX2,X              \ If XX2+X is zero then we decided in part 5 that
 BEQ LL78               \ face 2 is hidden, so jump to LL78

.LL79

                        \ We now build the screen line for this edge, as
                        \ follows:
                        \
                        \   XX15(1 0) = start x-coordinate
                        \
                        \   XX15(3 2) = start y-coordinate
                        \
                        \   XX15(5 4) = end x-coordinate
                        \
                        \   XX12(1 0) = end y-coordinate
                        \
                        \ We can then pass this to the line clipping routine
                        \ before storing the resulting line in the ship line
                        \ heap




	OriginalFlicker-free LDA (V),Y              \ Fetch byte #2 for this edge into X, which contains
 TAX                    \ the number of the vertex at the start of the edge

 INY                    \ Increment Y to point to byte #3

 LDA (V),Y              \ Fetch byte #3 for this edge into Q, which contains
 STA Q                  \ the number of the vertex at the end of the edge
 INY                    \ Increment Y to point to byte #2

 LDA (V),Y              \ Fetch byte #2 for this edge into X, which contains
 TAX                    \ the number of the vertex at the start of the edge




 LDA XX3+1,X            \ Fetch the x_hi coordinate of the edge's start vertex
 STA XX15+1             \ from the XX3 heap into XX15+1

 LDA XX3,X              \ Fetch the x_lo coordinate of the edge's start vertex
 STA XX15               \ from the XX3 heap into XX15

 LDA XX3+2,X            \ Fetch the y_lo coordinate of the edge's start vertex
 STA XX15+2             \ from the XX3 heap into XX15+2

 LDA XX3+3,X            \ Fetch the y_hi coordinate of the edge's start vertex
 STA XX15+3             \ from the XX3 heap into XX15+3




	OriginalFlicker-free LDX Q                  \ Set X to the number of the vertex at the end of the
                        \ edge, which we stored in Q
 INY                    \ Increment Y to point to byte #3

 LDA (V),Y              \ Fetch byte #3 for this edge into X, which contains
 TAX                    \ the number of the vertex at the end of the edge



 LDA XX3,X              \ Fetch the x_lo coordinate of the edge's end vertex
 STA XX15+4             \ from the XX3 heap into XX15+4

 LDA XX3+3,X            \ Fetch the y_hi coordinate of the edge's end vertex
 STA XX12+1             \ from the XX3 heap into XX11+1

 LDA XX3+2,X            \ Fetch the y_lo coordinate of the edge's end vertex
 STA XX12               \ from the XX3 heap into XX12

 LDA XX3+1,X            \ Fetch the x_hi coordinate of the edge's end vertex
 STA XX15+5             \ from the XX3 heap into XX15+5

 JSR LL147              \ Call LL147 to see if the new line segment needs to be
                        \ clipped to fit on-screen, returning the clipped line's
                        \ end-points in (X1, Y1) and (X2, Y2)

 BCS LL78               \ If the C flag is set then the line is not visible on
                        \ screen, so jump to LL78 so we don't store this line
                        \ in the ship line heap




	OriginalFlicker-free (Empty)
 JSR LSPUT              \ Draw this edge using flicker-free animation, by first
                        \ drawing the ship's new line and then erasing the
                        \ corresponding old line from the screen




       Name: LL9 (Part 11 of 12)
       Type: Subroutine
   Category: Drawing ships
    Summary: Draw ship: Add all visible edges to the ship line heap


 This part adds all the visible edges to the ship line heap, so we can draw
 them in part 12.

 Other entry points:

   LL81+2               Draw the contents of the ship line heap, used to draw
                        the ship as a dot from SHPPT




	OriginalFlicker-free.LL80

 LDY U                  \ Fetch the ship line heap pointer, which points to the
                        \ next free byte on the heap, into Y

 LDA XX15               \ Add X1 to the end of the heap
 STA (XX19),Y

 INY                    \ Increment the heap pointer

 LDA XX15+1             \ Add Y1 to the end of the heap
 STA (XX19),Y

 INY                    \ Increment the heap pointer

 LDA XX15+2             \ Add X2 to the end of the heap
 STA (XX19),Y

 INY                    \ Increment the heap pointer

 LDA XX15+3             \ Add Y2 to the end of the heap
 STA (XX19),Y

 INY                    \ Increment the heap pointer

 STY U                  \ Store the updated ship line heap pointer in U

 CPY T1                 \ If Y >= T1 then we have reached the maximum number of
 BCS LL81               \ edge lines that we can store in the ship line heap, so
                        \ skip to LL81 so we don't loop back for the next edge

.LL78

 INC XX17               \ Increment the edge counter to point to the next edge

 LDY XX17               \ If Y >= XX20, which contains the number of edges in
 CPY XX20               \ the blueprint, jump to LL81 as we have processed all
 BCS LL81               \ the edges and don't need to loop back for the next one

 LDY #0                 \ Set Y to point to byte #0 again, ready for the next
                        \ edge

 LDA V                  \ Increment V by 4 so V(1 0) points to the data for the
 ADC #4                 \ next edge
 STA V
.LL78

 LDA LSNUM              \ If LSNUM >= CNT, skip to LL81 so we don't loop back
 CMP CNT                \ for the next edge (CNT was set to the maximum heap
 BCS LL81               \ size for this ship in part 10, so this checks whether
                        \ we have just run out of space in the ship line heap,
                        \ and stops drawing edges if we have)

 LDA V                  \ Increment V by 4 so V(1 0) points to the data for the
 CLC                    \ next edge
 ADC #4
 STA V



 BCC ll81               \ If the above addition didn't overflow, jump to ll81

 INC V+1                \ Otherwise increment the high byte of V(1 0), as we
                        \ just moved the V(1 0) pointer past a page boundary

.ll81




	OriginalFlicker-free JMP LL75               \ Loop back to LL75 to process the next edge

.LL81

                        \ We have finished adding lines to the ship line heap,
                        \ so now we need to set the first byte of the heap to
                        \ the number of bytes stored there

 LDA U                  \ Fetch the ship line heap pointer from U into A, which
                        \ points to the end of the heap, and therefore contains
                        \ the heap size

 LDY #0                 \ Store A as the first byte of the ship line heap, so
 STA (XX19),Y           \ the heap is now correctly set up
 INC XX17               \ Increment the edge counter to point to the next edge

 LDY XX17               \ If Y < XX20, which contains the number of edges in
 CPY XX20               \ the blueprint, loop back to LL75 to process the next
 BCC LL75               \ edge

.LL81

 JMP LSCLR              \ Jump down to part 12 below to draw any remaining lines
                        \ from the old ship that are still in the ship line heap





       Name: LL9 (Part 12 of 12)
       Type: Subroutine
   Category: Drawing ships
    Summary: Draw ship: Draw all the visible edges from the ship line heap


 This part draws the lines in the ship line heap, which is used both to draw
 the ship, and to remove it from the screen.




	OriginalFlicker-free.LL155

 LDY #0                 \ Fetch the first byte from the ship line heap into A,
 LDA (XX19),Y           \ which contains the number of bytes in the heap

 STA XX20               \ Store the heap size in XX20

 CMP #4                 \ If the heap size is less than 4, there is nothing to
 BCC LL118-1            \ draw, so return from the subroutine (as LL118-1
                        \ contains an RTS)

 INY                    \ Set Y = 1, which we will use as an index into the ship
                        \ line heap, starting at byte #1 (as byte #0 contains
                        \ the heap size)

.LL27
.LSCLR

 LDY LSNUM              \ Set Y to the offset in the line heap LSNUM

.LSC1

 CPY LSNUM2             \ If Y >= LSNUM2, jump to LSC2 to return from the ship
 BCS LSC2               \ drawing routine, because the index in Y is greater
                        \ than the size of the existing ship line heap, which
                        \ means we have alrady erased all the old ships lines
                        \ when drawing the new ship

                        \ If we get here then Y < LSNUM2, which means Y is
                        \ pointing to an on-screen line from the old ship that
                        \ we need to erase



 LDA (XX19),Y           \ Fetch the X1 line coordinate from the heap and store
 STA XX15               \ it in XX15

 INY                    \ Increment the heap pointer

 LDA (XX19),Y           \ Fetch the Y1 line coordinate from the heap and store
 STA XX15+1             \ it in XX15+1

 INY                    \ Increment the heap pointer

 LDA (XX19),Y           \ Fetch the X2 line coordinate from the heap and store
 STA XX15+2             \ it in XX15+2

 INY                    \ Increment the heap pointer

 LDA (XX19),Y           \ Fetch the Y2 line coordinate from the heap and store
 STA XX15+3             \ it in XX15+3

 JSR LL30               \ Draw a line from (X1, Y1) to (X2, Y2)

 INY                    \ Increment the heap pointer




	OriginalFlicker-free CPY XX20               \ If the heap counter is less than the size of the heap,
 BCC LL27               \ loop back to LL27 to draw the next line from the heap

 RTS                    \ Return from the subroutine
 JMP LSC1               \ Loop back to LSC1 to draw (i.e. erase) the next line
                        \ from the heap

.LSC2

 LDA LSNUM              \ Store LSNUM in the first byte of the ship line heap
 LDY #0
 STA (XX19),Y

.LSC3

 RTS                    \ Return from the subroutine






.codeBlockWrapper.compare > pre.initial { display: block }
.hide-code-1, .hide-code-2, .hide-code-3, .hide-code-4, .hide-code-5, .hide-code-6, .hide-code-7 { display: none }
.codeBlockWrapper .headerBlockWrapper { cursor: pointer; }
.codeBlockWrapper .headerBlockWrapper.hiding:not(:last-child) { border-bottom: none; }
.codeBlockWrapper .codeCompareBlock { padding-top: 2ch }



  var hideShow = function() {
    var blockNumber = this.getAttribute("data-block");
    var codeToToggle = document.getElementsByClassName("hide-code-" + blockNumber);

    showing = false
    for (var i = 0; i < codeToToggle.length; i++) {
      x = codeToToggle[i]
      if (x.style.display === "none" || x.style.display === "") {
        x.style.display = "block";
        showing = true
      } else {
        x.style.display = "none";
      }
    }
    if (showing) {
      this.classList.remove('hiding');
    } else {
      this.classList.add('hiding');
    }
  };

  var elements = document.getElementsByClassName("headerBlockWrapper");

  for (var i = 0; i < elements.length; i++) {
    elements[i].addEventListener('click', hideShow, false);
  }



				
					Flicker-free ship drawingDrawing circles
				
			

			
				Elite on the 6502 was written by Ian Bell and David Braben BBC Micro and Acorn Electron Elite © Acornsoft 19846502 Second Processor Elite © Acornsoft 1985Commodore 64 Elite © D. Braben and I. Bell 1985Apple II Elite © D. Braben and I. Bell 1986BBC Master Elite © Acornsoft 1986NES Elite © D. Braben and I. Bell 1991/1992Elite-A base code © as per BBC Micro EliteModifications by Angus Duggan © Angus DugganCommentary © Mark Moxon 2020
				All Rights Reserved
			

			
				Home page
			

			
				
					Using this site
					Home page Start at the very beginning
					Quick start guide All you need to know to start exploring this site
					All about this project
						Project history, building the source and more
						
							All about this project
							About this project The story of how this project came to be
							Terminology used in this commentary Read this before you explore the source code
							Building Elite from the source How to build your own working copy of Elite
							Useful links A collection of links to pages I've found useful during this project
							Acknowledgements The giants on whose shoulders this project stands
							Site history A short history of this site's development
							Site map A top-level map of this website
							To-do list Code that could benefit from a bit more analysis
						
					
					Playing with the Elite source code
					Playing 6502 Elite in the 21st century How to play all the versions of Elite analysed here
					Deep dive articles
						Over 130 articles on how Elite weaves its magic
						
							Index
							Index of all deep dive articlesDiscover how Elite works under the hood
							Deep dives
							Software archaeology Digging for clues in the original source code
								
									Software archaeology
									The Elite source code family tree Tracing the development history of 6502 Elite from the BBC Micro to the NES
									Building Commodore 64 Elite from the source disk How to build Commodore 64 Elite from the original BBC Micro source disk
									Building Apple II Elite from the source disk How to build Apple II Elite from the original BBC Micro source disk
								
							
							The main game loop The main game loop and task scheduler
								
									The main game loop
									Program flow of the main game loop The sequence of events in the main game loop and the main flight loop
									Scheduling tasks with the main loop counter How the main loop counter controls what we do and when we do it
									Splitting the main loop in the NES version How the main flight loop is split and shared with the combat demo
								
							
							Simulating the universe Procedural galaxies, system seeds, market prices
								
									Simulating the universe
									Galaxy and system seeds How system data is extracted from the galaxy and system seeds
									Generating system data The algorithms behind the procedural generation of system data
									Generating system names Producing system names from twisted seeds and two-letter tokens
									Twisting the system seeds How the system seeds are twisted to produce entire galaxies of stars
									Market item prices and availability The algorithms behind the generation of each system's cargo market
								
							
							Simulating the local bubble Spawning and managing ships in our local bubble
								
									Simulating the local bubble
									The local bubble of universe The data structures used to simulate the universe around our ship
									A sense of scale Space is big, but just how large are the star systems in 8-bit Elite?
									The space station safe zone Details of the calculations behind the space station safe zone
								
							
							Ship data Ship blueprints and ship data blocks
								
									Ship data
									Ship blueprints Specifications for all the different types of ship in the universe
									Comparing ship specifications A detailed comparison of in-game statistics for the different ships in Elite
									Ship data blocks Storing data for each of the ships in the local bubble of universe
									The elusive Cougar They say it is vanishingly rare... but just how rare is the mysterious Cougar?
								
							
							Moving and rotating in space Pitching, rolling and moving in 3D vector space
								
									Moving and rotating in space
									Pitching and rolling Applying our pitch and roll to another ship's orientation in space
									Pitching and rolling by a fixed angle How other ships manage to pitch and roll in space
									Program flow of the ship-moving routine A breakdown of the routine that moves the entire universe around us
									Rotating the universe What happens to the rest of the universe when we rotate our ship?
									Orientation vectors The three vectors that determine a ship's orientation in space
									Tidying orthonormal vectors Making the orientation vectors orthonormal, and why this matters
									Flipping axes between space views Details of how the different space views are implemented
								
							
							Docking and docking computers How to dock safely with a space station
								
									Docking and docking computers
									Docking checks The checks that determine whether we are docking... or just crashing
									The docking computer How the docking computer steers us home in the enhanced versions of Elite
								
							
							Tactics and combat Ranks, weapons and intelligent enemy ships
								
									Tactics and combat
									Combat rank The long, long road from Harmless to Elite
									In the crosshairs How the game knows whether an enemy is being hit by our laser fire
									Program flow of the tactics routine How ships and missiles work out attack patterns... or how to run away
									Advanced tactics with the NEWB flags How the enhanced versions of Elite give their ships a bit more personality
									Aggression and hostility in ship tactics Why some ships are peaceful traders while others seem hell-bent on revenge
								
							
							The scanner and dashboard The 3D elliptical scanner and other indicators
								
									The scanner and dashboard
									The 3D scanner The maths behind Elite's famous 3D elliptical scanner
									The dashboard indicators How the bar-based dashboard indicators display their data
								
							
							The split-screen mode Elite's custom and split-screen modes
								
									The split-screen mode
									The split-screen mode in BBC Micro Elite Elite's famous split-screen mode, dissected and explained in detail
									The split-screen mode in Commodore 64 Elite How the VIC-II makes it easy to implement the Commodore version's split screen
									The split-screen mode in NES Elite How the NES version implements a split-screen mode without hardware timers
								
							
							Drawing pixels Poking pixels directly into screen memory
								
									Drawing pixels
									Drawing monochrome pixels on the BBC Micro Poking screen memory to display monochrome pixels in the space view
									Drawing colour pixels on the BBC Micro Poking screen memory to display colour pixels in the dashboard view
									Drawing pixels in the Electron version Poking pixels into screen memory in the Acorn Electron version of Elite
									Drawing pixels in the Commodore 64 version Updating the bitmap screen in the Commodore 64 version of Elite
									Drawing pixels in the Apple II version Working with the Apple II's unique high-resolution graphics mode
									Drawing pixels in the NES version How the NES version pokes pixels into the console's tile-based screen
									Extended screen coordinates The extended 16-bit screen coordinate system behind the space view
								
							
							Drawing text Poking text characters into screen memory
								
									Drawing text
									Drawing text How Elite draws text on-screen by poking character bitmaps directly into screen memory
									Fonts in NES Elite The three different fonts used in the Nintendo version of Elite
								
							
							Drawing lines Line-drawing algorithms and efficient clipping
								
									Drawing lines
									Elite's line-drawing algorithm The main line-drawing algorithm used to draw non-horizontal lines
									Line-clipping Efficiently clipping an extended line to the part that's on-screen
									Drawing lines in the NES version Using tiles as stepping stones when drawing lines on the NES
								
							
							Drawing ships Drawing 3D wireframes and flicker-free ships
								
									Drawing ships
									Drawing ships The main routine for drawing 3D wireframe ships in space
									Back-face culling How Elite draws solid-looking 3D ships by only drawing visible faces
									Calculating vertex coordinates Determining whether a ship's vertex is visible or hidden from us
									Flicker-free ship drawing How the BBC Master and Apple II versions reduce flicker when drawing ships
									Backporting the flicker-free algorithm Applying the BBC Master's flicker-free algorithm to the other versions
								
							
							Drawing circles and ellipses Circles, ellipses, hyperspace and docking effects
								
									Drawing circles and ellipses
									Drawing circles The routines that draw planets and the hyperspace and docking tunnels
									The ball line heap How we remember the lines used to draw circles so they can be redrawn
									Drawing ellipses How Elite draws ellipses for the planet's crater, meridian and equator
								
							
							Drawing planets Craters, meridians and the dots of Saturn
								
									Drawing planets
									Drawing craters The algorithms behind the huge craters of planets like Diso
									Drawing meridians and equators The algorithms behind the meridians and equators of planets like Lave
									Drawing Saturn on the loading screen How the loader draws the dot-based Saturn in Elite's epic loading screen
								
							
							Drawing suns and explosions Shimmering suns and glittering explosion clouds
								
									Drawing suns and explosions
									Drawing the sun Drawing and storing the sun, and the systems on the Short-range Chart
									Drawing explosion clouds Drawing and storing explosion clouds for ships whose luck runs out...
								
							
							Drawing stardust How the tiny particles of moving stardust work
								
									Drawing stardust
									Stardust in the front view The algorithms behind the stardust particles in the front view
									Stardust in the side views The algorithms behind the stardust particles in the side views
								
							
							Missions The three missions in the 6502 versions of Elite
								
									Missions
									The Constrictor mission Hunting high and low for the stolen Constrictor
									The Thargoid Plans mission Evading the Thargoid threat in the depths of the third galaxy
									The Trumbles mission Furry fun in the Commodore 64 and NES versions of Elite
								
							
							Text Text tokenisation and the "goat soup" algorithm
								
									Text
									Printing text tokens Printing recursive text tokens, two-letter tokens and control codes
									Extended text tokens The extended text token system in the enhanced versions of Elite
									Extended system descriptions The famous "goat soup" algorithm that generates those strange and wonderful system descriptions
									Printing decimal numbers How to print big decimal numbers with decimal points and padding
									Multi-language support in NES Elite How the NES version supports English, German and French text
								
							
							Sound and music Iconic docking music and explosions in space
								
									Sound and music
									Sound effects in Commodore 64 Elite Making the most of the SID sound synthesiser
									Sound effects in Apple II Elite Attempting to make game sounds from a single, solitary click
									Sound effects in NES Elite The largest set of sound effects in all the 6502 Elites
									Music in Commodore 64 Elite The music driver behind the iconic Blue Danube and the catchy Elite Theme
									Music in NES Elite How David Whittaker's music module plays The Blue Danube
								
							
							Keyboards, joysticks and controllers Reading and logging Elite's multiple controls
								
									Keyboards, joysticks and controllers
									The key logger Supporting concurrent in-flight key presses using a key logger
									Reading the Commodore 64 keyboard matrix Scanning the Commodore 64 keyboard without using the operating system
									Bolting NES controllers onto the key logger How the NES version simulates a joystick and keyboard
									Working with the Apple II keyboard Trying to implement a game-ready key logger, one key press at a time
								
							
							Maths Arithmetic, geometry and random numbers
								
									Maths
									Adding sign-magnitude numbers Doing basic arithmetic with sign-magnitude numbers
									Calculating square roots The algorithm behind the square root routine
									Shift-and-add multiplication The main algorithm behind Elite's many multiplication routines
									Multiplication and division using logarithms Faster multiplication and division routines by using logarithm lookup tables
									Shift-and-subtract division The main algorithm behind Elite's many division routines
									The sine, cosine and arctan tables The lookup tables used for the planet-drawing trigonometric functions
									Generating random numbers The algorithm behind Elite's random number generation routines
								
							
							Saving and loading Commander files and competition codes
								
									Saving and loading
									Commander save files A description of each and every byte in the saved commander file
									The competition code All the information that's hidden in the Elite competition code
								
							
							Demonstration modes Self-playing demos and Star Wars scroll text
								
									Demonstration modes
									The Elite Demonstration Disc The secrets of Acornsoft's self-playing demo for the BBC Micro
									Code changes in the Demonstration Disc The differences between the cassette version and the demonstration disc
									The 6502 Second Processor demo mode All about the Star Wars-esque scroll text in the Tube-based version of Elite
									The NES combat demo How the scroll text and combat practice works
									Auto-playing the NES combat demo The magic of watching Elite playing itself
								
							
							Version-specific deep dives
							Memory maps Details of memory usage in the different versions
								
									Memory maps
									BBC Micro cassette Elite memory map Memory usage in the classic version of Elite, where space is really tight
									BBC Micro disc Elite memory map Memory usage in the enhanced disc version of Elite
									Acorn Electron Elite memory map Memory usage in the smallest and most basic version of Elite
									6502 Second Processor Elite memory map Memory usage in the Tube-based version of Elite
									Commodore 64 Elite memory map Memory usage in the musical version of Elite
									Apple II Elite memory map Memory usage in the flicker-free version of Elite
									BBC Master Elite memory map Memory usage in the smoothest version of Elite
									NES Elite memory map Memory usage in the only console-based version of Elite
								
							
							BBC Micro disc Elite Using a disc drive to create canonical Elite
								
									BBC Micro disc Elite
									Swapping between the docked and flight code Using the BBC's disc drive to swap out the game binaries when launching and docking
									Ship blueprints in the BBC Micro disc version How the BBC Micro disc version loads its ship blueprints into memory
								
							
							6502 Second Processor Elite Tube APIs, scroll texts, speech support and more
								
									6502 Second Processor Elite
									6502 Second Processor Tube communication How the 6502 Second Processor version of Elite talks over the Tube
									The TINA hook Adding your own custom code to the 6502 Second Processor version using TINA
									Secrets of the Executive version Infinite jumps, retro-futuristic fonts, speech support... and Pizzasoft?
								
							
							Commodore 64 Elite Colours, music, sprites and remote development
								
									Commodore 64 Elite
									Colouring the Commodore 64 bitmap screen Adding a distinctive dash of colour to the Commodore 64 dashboard
									Sprite usage in Commodore 64 Elite Laser crosshairs, colourful explosions and lots of cuddly, furry Trumbles
									Developing Commodore 64 Elite on a BBC Micro Sending Elite between 8-bit machines with the Programmer's Development System
								
							
							Apple II Elite Bringing 1970s technology into the 1980s
								
									Apple II Elite
									File operations with embedded Apple DOS Saving and loading commander files with a customised version of DOS 3.3
									Developing Apple II Elite on a BBC Micro Clues about the remote development of the Apple II version of Elite
								
							
							NES Elite Elite on the Nintendo Entertainment System
								
									NES Elite
									Comparing NES Elite with the other versions The features that make NES Elite so unique
									Understanding the NES for Elite The NES architecture and how it applies to Elite
									Splitting NES Elite across multiple ROM banks Details of the MMC1 controller and the 128K game ROM
									The pattern and nametable buffers How the NES version achieves its beautifully smooth wireframe graphics
									Bitplanes in NES Elite Squeezing two patterns into one tile using separate bitplanes
									Drawing vector graphics using NES tiles The art of the impossible: vector graphics on the NES
									Views and view types in NES Elite Configuring all the different views in the console version
									Image and data compression How images and data are compressed in NES Elite
									Displaying two-layer images The beautiful pixel art of the commander and system images
									Sprite usage in NES Elite Stardust, scanners, images, crosshairs and more
								
							
							Elite-A How Angus Duggan modified the original Elite
								
									Elite-A
									Making room for the modifications in Elite-A How Angus Duggan found enough spare memory for Elite-A's modifications
									Buying and flying ships in Elite-A What it's like to save up for and fly your dream ship in Elite-A
									Ship blueprints in Elite-A The enhanced logic behind Elite-A's sophisticated ship blueprints system
									The Encyclopedia Galactica Inside the encyclopedia, Elite-A's most recognisable modification
									The I.F.F. system Friend or foe? Adding ship information to the 3D scanner
									Fixing ship positions Why Elite spawns certain ships in certain places, and how Elite-A fixes this
									Special cargo missions Procedurally generating delivery missions and tracking progress
									Delta 14B joystick support All the controls of Elite in one single handset - the future is here!
									Tube communication in Elite-A How the 6502 Second Processor version of Elite-A talks over the Tube
									The original source files How the original Elite-A source was written, edited and compiled
								
							
						
					Elite hacks
						Universe editor, flicker-free, teletext and more
						
							Index
							Index of all Elite hacksA list of all the Elite hacks on this site
							Elite hacks
							Elite Compendium The best way to play all the hacked and enhanced versions of Elite
								
									Elite Compendium
									About the Elite Compendium Bringing all the best Elite hacks together in four feature-packed discs
									Playing the Elite Compendium How to download and play the Elite Compendium
									Technical information Details of all the hacks and enhancements in the Elite Compendium
								
							
							Elite Universe Editor Create your own Elite universes and "press play" to bring them to life
								
									Elite Universe Editor
									About the Elite Universe Editor Create your own Elite universes and "press play" to bring them to life
									Playing the Elite Universe Editor How to download and play the Elite Universe Editor
									A summary of keys All the keys used in all the different versions of the Elite Universe Editor
									Instructions for the BBC version Full instructions for the Elite Universe Editor on the BBC Micro and Master
									Instructions for the Commodore 64 version Full instructions for the Elite Universe Editor on the Commodore 64
									Technical information Details of how the Elite Universe Editor works under the bonnet
								
							
							Flicker-free Elite Improved ship drawing on the BBC Micro, Commodore 64 and Commodore Plus/4
								
									Flicker-free Elite
									About flicker-free Elite Improved ship drawing on the BBC Micro, Electron, Commodore and Apple
									Playing flicker-free Elite How to download and play flicker-free Elite, on the BBC, Commodore and Apple
									Technical information Details of how flicker-free Elite weaves its magic
								
							
							Compendium version of Electron Elite Super-fast Electron Elite with all the bells and whistles of the BBC versions
								
									Compendium version of Electron Elite
									About the Compendium version of Acorn Electron Elite Updating Acorn Electron Elite with all the bells and whistles of the BBC version
									Playing the Compendium version of Acorn Electron Elite How to download and play the improved version of Acorn Electron Elite
									Technical information How I backported BBC Micro disc Elite to the Acorn Electron with sideways RAM
								
							
							Teletext Elite The disc version of BBC Micro Elite, converted to run in teletext
								
									Teletext Elite
									About Teletext Elite The disc version of BBC Micro Elite, converted to run in teletext
									Playing Teletext Elite How to download and play Teletext Elite
									Instructions for Teletext Elite Full instructions for Teletext Elite on the BBC Micro
									Technical information Details of how Elite was converted to use teletext
								
							
							Elite over Econet Elite that loads over an Econet network and supports live multiplayer scoreboards
								
									Elite over Econet
									About Elite over Econet Econet support and multiplayer scoreboards for the BBC Micro, Electron and Archimedes
									Installing Elite over Econet How to install Elite on an Econet fileserver
									Playing Elite over Econet How to play Elite over an Econet network
									The Elite multiplayer scoreboard Running multiplayer Elite competitions with a live Econet-based scoreboard
									Playing Elite over Econet in an emulator How to set up BeebEm with an emulated Econet network that runs Elite
									Technical information Details of how Elite over Econet works
									Elite over Econet on the Acorn Archimedes Joining multiplayer scoreboards from the RISC OS version of Elite
								
							
							Elite 3D BBC Micro Elite in full anaglyph 3D - just add a pair of fancy coloured glasses
								
									Elite 3D
									About Elite 3D Taking 8-bit Elite into another dimension with anaglyph 3D and coloured specs
									Playing Elite 3D How to download and play Elite 3D, and how to configure the anaglyph settings
									Configuring Elite 3D How to configure the anaglyph settings in Elite 3D
									Technical information Details of how Elite 3D works
								
							
							BBC Master Elite on the BBC Micro B+ BBC Master Elite, converted to run on the BBC Micro B+
								
									BBC Master Elite on the BBC Micro B+
									About BBC Master Elite on the BBC Micro B+ Giving the BBC Micro B+ the full colour version of Elite that it deserves
									Playing BBC Master Elite on the BBC Micro B+ How to download and play BBC Master Elite on the BBC Micro B+
									Technical information Squeezing full colour BBC Master Elite into the weird extra memory on the B+
								
							
							Acornsoft Elite... with music! The title and docking music from the Commodore 64, shoehorned into Acornsoft Elite
								
									Acornsoft Elite... with music!
									About the musical version of Acornsoft Elite BBC Micro and Acorn Electron Elite, with added title and docking music
									Playing musical Acornsoft Elite How to download and play the musical version of Acornsoft Elite
									Technical information How the Commodore 64's music was ported to Elite on the BBC Micro and Electron
								
							
							BBC Micro disc Elite on the BBC Master The disc version of BBC Micro Elite, converted to run on the BBC Master
								
									BBC Micro disc Elite on the BBC Master
									About BBC Micro disc Elite on the BBC Master The disc version of BBC Micro Elite, converted to run on the BBC Master
									Playing BBC Micro disc Elite on the BBC Master How to download and play the original disc version of Elite on the BBC Master
									Technical information Details of how disc Elite was converted from the BBC Micro to the BBC Master
								
							
						
					

					

					Indexes to the source code
						A-Z indexes, code usage analysis and more
						
							Indexes to the source code
							BBC Micro cassette source code indexes
								A-Z indexes and indexes by category for the BBC Micro cassette version of Elite
								
									A-Z indexes for the BBC Micro cassette version
									A-Z index of the source code An index of every subroutine, entry point, variable, workspace and macro in the source code
									Source code cross-references Every label and variable in the source code and where they are used
									Indexes by category for the BBC Micro cassette version
									List of all subroutines by category Subroutines in the BBC Micro cassette version of Elite
									List of all variables by category Variables in the BBC Micro cassette version of Elite
									List of all workspaces by category Workspaces in the BBC Micro cassette version of Elite
									List of all macros by category Macros used in the BBC Micro cassette version of Elite
								
							
							BBC Micro disc source code indexes
								A-Z indexes and indexes by category for the BBC Micro disc version of Elite
								
									A-Z indexes for the BBC Micro disc version
									A-Z index of the source code An index of every subroutine, entry point, variable, workspace and macro in the source code
									Source code cross-references Every label and variable in the source code and where they are used
									Indexes by category for the BBC Micro disc version
									List of all subroutines by category Subroutines in the BBC Micro disc version of Elite
									List of all variables by category Variables in the BBC Micro disc version of Elite
									List of all workspaces by category Workspaces in the BBC Micro disc version of Elite
									List of all macros by category Macros used in the BBC Micro disc version of Elite
								
							
							Demonstration Disc source code indexes
								A-Z indexes and indexes by category for the Elite Demonstration Disc
								
									A-Z indexes for the Elite Demonstration Disc
									A-Z index of the source code An index of every subroutine, entry point, variable, workspace and macro in the source code
									Source code cross-references Every label and variable in the source code and where they are used
									Indexes by category for the Elite Demonstration Disc
									List of all subroutines by category Subroutines in the Elite Demonstration Disc
									List of all variables by category Variables in the Elite Demonstration Disc
									List of all workspaces by category Workspaces in the Elite Demonstration Disc
									List of all macros by category Macros used in the Elite Demonstration Disc
								
							
							Acorn Electron source code indexes
								A-Z indexes and indexes by category for the Electron version of Elite
								
									A-Z indexes for the Electron version
									A-Z index of the source code An index of every subroutine, entry point, variable, workspace and macro in the source code
									Source code cross-references Every label and variable in the source code and where they are used
									Indexes by category for the Electron version
									List of all subroutines by category Subroutines in the Electron version of Elite
									List of all variables by category Variables in the Electron version of Elite
									List of all workspaces by category Workspaces in the Electron version of Elite
									List of all macros by category Macros used in the Electron version of Elite
								
							
							6502 Second Processor source code indexes
								A-Z indexes and indexes by category for the 6502 Second Processor version of Elite
								
									A-Z indexes for the 6502 Second Processor version
									A-Z index of the source code An index of every subroutine, entry point, variable, workspace and macro in the source code
									Source code cross-references Every label and variable in the source code and where they are used
									Indexes by category for the 6502 Second Processor version
									List of all subroutines by category Subroutines in the 6502 Second Processor version of Elite
									List of all variables by category Variables in the 6502 Second Processor version of Elite
									List of all workspaces by category Workspaces in the 6502 Second Processor version of Elite
									List of all macros by category Macros used in the 6502 Second Processor version of Elite
								
							
							Commodore 64 source code indexes
								A-Z indexes and indexes by category for the Commodore 64 version of Elite
								
									A-Z indexes for the Commodore 64 version
									A-Z index of the source code An index of every subroutine, entry point, variable, workspace and macro in the source code
									Source code cross-references Every label and variable in the source code and where they are used
									Indexes by category for the Commodore 64 version
									List of all subroutines by category Subroutines in the Commodore 64 version of Elite
									List of all variables by category Variables in the Commodore 64 version of Elite
									List of all workspaces by category Workspaces in the Commodore 64 version of Elite
									List of all macros by category Macros used in the Commodore 64 version of Elite
								
							
							Apple II source code indexes
								A-Z indexes and indexes by category for the Apple II version of Elite
								
									A-Z indexes for the Apple II version
									A-Z index of the source code An index of every subroutine, entry point, variable, workspace and macro in the source code
									Source code cross-references Every label and variable in the source code and where they are used
									Indexes by category for the Apple II version
									List of all subroutines by category Subroutines in the Apple II version of Elite
									List of all variables by category Variables in the Apple II version of Elite
									List of all workspaces by category Workspaces in the Apple II version of Elite
									List of all macros by category Macros used in the Apple II version of Elite
								
							
							BBC Master source code indexes
								A-Z indexes and indexes by category for the BBC Master version of Elite
								
									A-Z indexes for the BBC Master version
									A-Z index of the source code An index of every subroutine, entry point, variable, workspace and macro in the source code
									Source code cross-references Every label and variable in the source code and where they are used
									Indexes by category for the BBC Master version
									List of all subroutines by category Subroutines in the BBC Master version of Elite
									List of all variables by category Variables in the BBC Master version of Elite
									List of all workspaces by category Workspaces in the BBC Master version of Elite
									List of all macros by category Macros used in the BBC Master version of Elite
								
							
							NES source code indexes
								A-Z indexes and indexes by category for the NES version of Elite
								
									A-Z indexes for the NES version
									A-Z index of the source code An index of every subroutine, entry point, variable, workspace and macro in the source code
									Source code cross-references Every label and variable in the source code and where they are used
									Indexes by category for the NES version
									List of all subroutines by category Subroutines in the NES version of Elite
									List of all variables by category Variables in the NES version of Elite
									List of all workspaces by category Workspaces in the NES version of Elite
									List of all macros by category Macros used in the NES version of Elite
								
							
							Elite-A source code indexes
								A-Z indexes and indexes by category for Elite-A
								
									A-Z indexes for Elite-A
									A-Z index of the source code An index of every subroutine, entry point, variable, workspace and macro in the source code
									Source code cross-references Every label and variable in the source code and where they are used
									Indexes by category for Elite-A
									List of all subroutines by category Subroutines in Elite-A
									List of all variables by category Variables in Elite-A
									List of all workspaces by category Workspaces in Elite-A
									List of all macros by category Macros used in Elite-A
								
							
							Indexes of variations
							Indexes of variations and code usage How code is shared between the different versions of Elite, and how it varies between versions
								
									Indexes of variations and code usage
									All shared code that contains variations Code that appears in multiple versions and which differs between versions
									All shared code that contains no variations Code that appears in multiple versions and which is the same in all versions
									Version-specific routines Code that appears in just one version of Elite
								
							
						
					

					Source code statistics Instruction counts and other source code stats
						
							Source code statistics
							Code statistics for the BBC Micro cassette version A breakdown of the BBC Micro cassette source code by category, type and number of instructions
							Code statistics for the BBC Micro disc version A breakdown of the BBC Micro disc source code by category, type and number of instructions
							Code statistics for the Elite Demonstration Disc A breakdown of the Elite Demonstration Disc source code by category, type and number of instructions
							Code statistics for the Acorn Electron version A breakdown of the Acorn Electron source code by category, type and number of instructions
							Code statistics for the 6502 Second Processor version A breakdown of the 6502 Second Processor source code by category, type and number of instructions
							Code statistics for the Commodore 64 version A breakdown of the Commodore 64 source code by category, type and number of instructions
							Code statistics for the Apple II version A breakdown of the Apple II source code by category, type and number of instructions
							Code statistics for the BBC Master version A breakdown of the BBC Master source code by category, type and number of instructions
							Code statistics for the NES version A breakdown of the NES source code by category, type and number of instructions
							Code statistics for Elite-A A breakdown of the Elite-A source code by category, type and number of instructions
						
					

					My software archaeology sites
					Mark Moxon's Software Archaeology
					Elite on the 6502
					Aviator on the BBC Micro
					Revs on the BBC Micro
					The Sentinel on the BBC Micro
					Lander on the Acorn Archimedes
					My writing sites
					Mark Moxon's Travel Writing
					Walking Land's End to John o'Groats
					Tubewalker: The Tube, on Foot
					Contact details and more
					Mark Moxon's Homepage
```

### Snippet Codice (BASIC)

```basic
OriginalFlicker-free (Empty)
                        \ We now set things up for flicker-free ship plotting,
                        \ by setting the following:
                        \
                        \   LSNUM = offset to the first coordinate in the ship's
                        \           line heap
                        \
                        \   LSNUM2 = the number of bytes in the heap for the
                        \            ship that's currently on-screen (or 0 if
                        \            there is no ship currently on-screen)

 LDY #1                 \ Set LSNUM = 1, the offset of the first set of line
 STY LSNUM              \ coordinates in the ship line heap

 DEY                    \ Decrement Y to 0

 LDA #%00001000         \ If bit 3 of the ship's byte #31 is set, then the ship
 BIT INWK+31            \ is currently being drawn on-screen, so skip the
 BNE P%+5               \ following two instructions

 LDA #0                 \ The ship is not being drawn on screen, so set A = 0
                        \ so that LSNUM2 gets set to 0 below (as there are no
                        \ existing coordinates on the ship line heap for this
                        \ ship)

 EQUB &2C               \ Skip the next instruction by turning it into
                        \ &2C &B1 &BD, or BIT &BDB1 which does nothing apart
                        \ from affect the flags

 LDA (XX19),Y           \ Set LSNUM2 to the first byte of the ship's line heap,
 STA LSNUM2             \ which contains the number of bytes in the heap
```

### Snippet Codice (BASIC)

```basic
LDA #%00100000         \ If bit 5 of the ship's byte #31 is set, then the ship
 BIT XX1+31             \ is currently exploding, so jump down to EE28
 BNE EE28

 BPL EE28               \ If bit 7 of the ship's byte #31 is clear then the ship
                        \ has not just been killed, so jump down to EE28

                        \ Otherwise bit 5 is clear and bit 7 is set, so the ship
                        \ is not yet exploding but it has been killed, so we
                        \ need to start an explosion

 ORA XX1+31             \ Clear bits 6 and 7 of the ship's byte #31, to stop the
 AND #%00111111         \ ship from firing its laser and to mark it as no longer
 STA XX1+31             \ having just been killed

 LDA #0                 \ Set the ship's acceleration in byte #31 to 0, updating
 LDY #28                \ the byte in the workspace K% data block so we don't
 STA (INF),Y            \ have to copy it back from INWK later

 LDY #30                \ Set the ship's pitch counter in byte #30 to 0, to stop
 STA (INF),Y            \ the ship from pitching

 JSR EE51               \ Call EE51 to remove the ship from the screen

                        \ We now need to set up a new explosion cloud. We
                        \ initialise it with a size of 18 (which gets increased
                        \ by 4 every time the cloud gets redrawn), and the
                        \ explosion count (i.e. the number of particles in the
                        \ explosion), which go into bytes 1 and 2 of the ship
                        \ line heap. See DOEXP for more details of explosion
                        \ clouds

 LDY #1                 \ Set byte #1 of the ship line heap to 18, the initial
 LDA #18                \ size of the explosion cloud
 STA (XX19),Y

 LDY #7                 \ Fetch byte #7 from the ship's blueprint, which
 LDA (XX0),Y            \ determines the explosion count (i.e. the number of
 LDY #2                 \ vertices used as origins for explosion clouds), and
 STA (XX19),Y           \ store it in byte #2 of the ship line heap

                        \ The following loop sets bytes 3-6 of the of the ship
                        \ line heap to random numbers

.EE55

 INY                    \ Increment Y (so the loop starts at 3)

 JSR DORND              \ Set A and X to random numbers

 STA (XX19),Y           \ Store A in the Y-th byte of the ship line heap

 CPY #6                 \ Loop back until we have randomised the 6th byte
 BNE EE55

.EE28

 LDA XX1+8              \ Set A = z_sign

.EE49

 BPL LL10               \ If A is positive, i.e. the ship is in front of us,
                        \ jump down to LL10

.LL14

                        \ The following removes the ship from the screen by
                        \ redrawing it (or, if it is exploding, by redrawing the
                        \ explosion cloud). We call it when the ship is no
                        \ longer on-screen, is too far away to be fully drawn,
                        \ and so on

 LDA XX1+31             \ If bit 5 of the ship's byte #31 is clear, then the
 AND #%00100000         \ ship is not currently exploding, so jump down to EE51
 BEQ EE51               \ to redraw its wireframe

 LDA XX1+31             \ The ship is exploding, so clear bit 3 of the ship's
 AND #%11110111         \ byte #31 to denote that the ship is no longer being
 STA XX1+31             \ drawn on-screen

 JMP DOEXP              \ Jump to DOEXP to display the explosion cloud, which
                        \ will remove it from the screen, returning from the
                        \ subroutine using a tail call

.EE51

 LDA #%00001000         \ If bit 3 of the ship's byte #31 is clear, then there
 BIT XX1+31             \ is already nothing being shown for this ship, so
 BEQ LL10-1             \ return from the subroutine (as LL10-1 contains an RTS)

 EOR XX1+31             \ Otherwise flip bit 3 of byte #31 and store it (which
 STA XX1+31             \ clears bit 3 as we know it was set before the EOR), so
                        \ this sets this ship as no longer being drawn on-screen
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
OriginalFlicker-free JMP LL155              \ Jump to LL155 to draw the ship, which removes it from
                        \ the screen, returning from the subroutine using a
                        \ tail call
 JMP LSPUT              \ Jump to LSPUT to draw the ship, which removes it from
                        \ the screen, returning from the subroutine using a
                        \ tail call
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
RTS                    \ Return from the subroutine
```

### Snippet Codice (BASIC)

```basic
Name: LL9 (Part 9 of 12)
       Type: Subroutine
   Category: Drawing ships
    Summary: Draw ship: Draw laser beams if the ship is firing its laser at us


 This part sets things up so we can loop through the edges in the next part. It
 also adds a line to the ship line heap, if the ship is firing at us.

 When we get here, the heap at XX3 contains all the visible vertex screen
 coordinates.


.LL72

 LDA XX1+31             \ If bit 5 of the ship's byte #31 is clear, then the
 AND #%00100000         \ ship is not currently exploding, so jump down to EE31
 BEQ EE31

 LDA XX1+31             \ The ship is exploding, so set bit 3 of the ship's byte
 ORA #8                 \ #31 to denote that we are drawing something on-screen
 STA XX1+31             \ for this ship

 JMP DOEXP              \ Jump to DOEXP to display the explosion cloud,
                        \ returning from the subroutine using a tail call

.EE31
```

### Snippet Codice (BASIC)

```basic
OriginalFlicker-free LDA #%00001000         \ If bit 3 of the ship's byte #31 is clear, then there
 BIT XX1+31             \ is nothing already being shown for this ship, so skip
 BEQ LL74               \ to LL74 as we don't need to erase anything from the
                        \ screen

 JSR LL155              \ Otherwise call LL155 to draw the existing ship, which
                        \ removes it from the screen
 LDY #9                 \ Fetch byte #9 of the ship's blueprint, which is the
 LDA (XX0),Y            \ number of edges, and store it in XX20
 STA XX20
```

### Snippet Codice (BASIC)

```basic
LDA #%00001000         \ Set bit 3 of A so the next instruction sets bit 3 of
                        \ the ship's byte #31 to denote that we are drawing
                        \ something on-screen for this ship

.LL74

 ORA XX1+31             \ Apply bit 3 of A to the ship's byte #31, so if there
 STA XX1+31             \ was no ship already on screen, the bit is clear,
                        \ otherwise it is set
```

### Snippet Codice (BASIC)

```basic
OriginalFlicker-free LDY #9                 \ Fetch byte #9 of the ship's blueprint, which is the
 LDA (XX0),Y            \ number of edges, and store it in XX20
 STA XX20

 LDY #0                 \ We are about to step through all the edges, using Y
                        \ as a counter

 STY U                  \ Set U = 0 (though we increment it to 1 below)

 STY XX17               \ Set XX17 = 0, which we are going to use as a counter
                        \ for stepping through the ship's edges

 INC U                  \ We are going to start calculating the lines we need to
                        \ draw for this ship, and will store them in the ship
                        \ line heap, using U to point to the end of the heap, so
                        \ we start by setting U = 1
 LDY #0                 \ Set XX17 = 0, which we are going to use as a counter
 STY XX17               \ for stepping through the ship's edges
```

### Snippet Codice (BASIC)

```basic
BIT XX1+31             \ If bit 6 of the ship's byte #31 is clear, then the
 BVC LL170              \ ship is not firing its lasers, so jump to LL170 to
                        \ skip the drawing of laser lines

                        \ The ship is firing its laser at us, so we need to draw
                        \ the laser lines

 LDA XX1+31             \ Clear bit 6 of the ship's byte #31 so the ship doesn't
 AND #%10111111         \ keep firing endlessly
 STA XX1+31

 LDY #6                 \ Fetch byte #6 of the ship's blueprint, which is the
 LDA (XX0),Y            \ number * 4 of the vertex where the ship has its lasers

 TAY                    \ Put the vertex number into Y, where it can act as an
                        \ index into list of vertex screen coordinates we added
                        \ to the XX3 heap

 LDX XX3,Y              \ Fetch the x_lo coordinate of the laser vertex from the
 STX XX15               \ XX3 heap into XX15

 INX                    \ If X = 255 then the laser vertex is not visible, as
 BEQ LL170              \ the value we stored in part 2 wasn't overwritten by
                        \ the vertex calculation in part 6 and 7, so jump to
                        \ LL170 to skip drawing the laser lines

                        \ We now build a laser beam from the ship's laser vertex
                        \ towards our ship, as follows:
                        \
                        \   XX15(1 0) = laser vertex x-coordinate
                        \
                        \   XX15(3 2) = laser vertex y-coordinate
                        \
                        \   XX15(5 4) = x-coordinate of the end of the beam
                        \
                        \   XX12(1 0) = y-coordinate of the end of the beam
                        \
                        \ The end of the laser beam will be set positioned to
                        \ look good, rather than being directly aimed at us, as
                        \ otherwise we would only see a flashing point of light
                        \ as they unleashed their attack

 LDX XX3+1,Y            \ Fetch the x_hi coordinate of the laser vertex from the
 STX XX15+1             \ XX3 heap into XX15+1

 INX                    \ If X = 255 then the laser vertex is not visible, as
 BEQ LL170              \ the value we stored in part 2 wasn't overwritten by
                        \ a vertex calculation in part 6 and 7, so jump to LL170
                        \ to skip drawing the laser beam

 LDX XX3+2,Y            \ Fetch the y_lo coordinate of the laser vertex from the
 STX XX15+2             \ XX3 heap into XX15+2

 LDX XX3+3,Y            \ Fetch the y_hi coordinate of the laser vertex from the
 STX XX15+3             \ XX3 heap into XX15+3

 LDA #0                 \ Set XX15(5 4) = 0, so their laser beam fires to the
 STA XX15+4             \ left edge of the screen
 STA XX15+5

 STA XX12+1             \ Set XX12(1 0) = the ship's z_lo coordinate, which will
 LDA XX1+6              \ effectively make the vertical position of the end of
 STA XX12               \ the laser beam move around as the ship moves in space

 LDA XX1+2              \ If the ship's x_sign is positive, skip the next
 BPL P%+4               \ instruction

 DEC XX15+4             \ The ship's x_sign is negative (i.e. it's on the left
                        \ side of the screen), so switch the laser beam so it
                        \ goes to the right edge of the screen by decrementing
                        \ XX15(5 4) to 255

 JSR LL145              \ Call LL145 to see if the laser beam needs to be
                        \ clipped to fit on-screen, returning the clipped line's
                        \ end-points in (X1, Y1) and (X2, Y2)

 BCS LL170              \ If the C flag is set then the line is not visible on
                        \ screen, so jump to LL170 so we don't store this line
                        \ in the ship line heap
```

### Snippet Codice (BASIC)

```basic
OriginalFlicker-free LDY U                  \ Fetch the ship line heap pointer, which points to the
                        \ next free byte on the heap, into Y

 LDA XX15               \ Add X1 to the end of the heap
 STA (XX19),Y

 INY                    \ Increment the heap pointer

 LDA XX15+1             \ Add Y1 to the end of the heap
 STA (XX19),Y

 INY                    \ Increment the heap pointer

 LDA XX15+2             \ Add X2 to the end of the heap
 STA (XX19),Y

 INY                    \ Increment the heap pointer

 LDA XX15+3             \ Add Y2 to the end of the heap
 STA (XX19),Y

 INY                    \ Increment the heap pointer

 STY U                  \ Store the updated ship line heap pointer in U
 JSR LSPUT              \ Draw the laser line using flicker-free animation, by
                        \ first drawing the new laser line and then erasing the
                        \ corresponding old line from the screen
```

### Snippet Codice (BASIC)

```basic
Name: LL9 (Part 10 of 12)
       Type: Subroutine
   Category: Drawing ships
    Summary: Draw ship: Calculate the visibility of each of the ship's edges
             and, for flicker-free only, draw the visible ones


 This part calculates which edges are visible - in other words, which lines we
 should draw - and clips them to fit on the screen.

 When we get here, the heap at XX3 contains all the visible vertex screen
 coordinates.


.LL170

 LDY #3                 \ Fetch byte #3 of the ship's blueprint, which contains
 CLC                    \ the low byte of the offset to the edges data
 LDA (XX0),Y

 ADC XX0                \ Set V = low byte edges offset + XX0
 STA V

 LDY #16                \ Fetch byte #16 of the ship's blueprint, which contains
 LDA (XX0),Y            \ the high byte of the offset to the edges data

 ADC XX0+1              \ Set V+1 = high byte edges offset + XX0+1
 STA V+1                \
                        \ So V(1 0) now points to the start of the edges data
                        \ for this ship
```

### Snippet Codice (BASIC)

```basic
OriginalFlicker-free LDY #5                 \ Fetch byte #5 of the ship's blueprint, which contains
 LDA (XX0),Y            \ the maximum heap size for plotting the ship (which is
 STA T1                 \ 1 + 4 * the maximum number of visible edges) and store
                        \ it in T1

 LDY XX17               \ Set Y to the edge counter in XX17

.LL75
 LDY #5                 \ Fetch byte #5 of the ship's blueprint, which contains
 LDA (XX0),Y            \ the maximum heap size for plotting the ship (which is
 STA CNT                \ 1 + 4 * the maximum number of visible edges) and store
                        \ it in CNT

.LL75

 LDY #0                 \ Set Y = 0 so we start with byte #0
```

### Snippet Codice (BASIC)

```basic
LDA (V),Y              \ Fetch byte #0 for this edge, which contains the
                        \ visibility distance for this edge, beyond which the
                        \ edge is not shown

 CMP XX4                \ If XX4 > the visibility distance, where XX4 contains
 BCC LL78               \ the ship's z-distance reduced to 0-31 (which we set in
                        \ part 2), then this edge is too far away to be visible,
                        \ so jump down to LL78 to move on to the next edge

 INY                    \ Increment Y to point to byte #1

 LDA (V),Y              \ Fetch byte #1 for this edge into A, so:
                        \
                        \   A = %ffff ffff, where:
                        \
                        \     * Bits 0-3 = the number of face 1
                        \
                        \     * Bits 4-7 = the number of face 2
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
OriginalFlicker-free INY                    \ Increment Y to point to byte #2
 (Empty)
```

### Snippet Codice (BASIC)

```basic
STA P                  \ Store byte #1 into P

 AND #%00001111         \ Extract the number of face 1 into X
 TAX

 LDA XX2,X              \ If XX2+X is non-zero then we decided in part 5 that
 BNE LL79               \ face 1 is visible, so jump to LL79

 LDA P                  \ Fetch byte #1 for this edge into A

 LSR A                  \ Shift right four times to extract the number of face 2
 LSR A                  \ from bits 4-7 into X
 LSR A
 LSR A
 TAX

 LDA XX2,X              \ If XX2+X is zero then we decided in part 5 that
 BEQ LL78               \ face 2 is hidden, so jump to LL78

.LL79

                        \ We now build the screen line for this edge, as
                        \ follows:
                        \
                        \   XX15(1 0) = start x-coordinate
                        \
                        \   XX15(3 2) = start y-coordinate
                        \
                        \   XX15(5 4) = end x-coordinate
                        \
                        \   XX12(1 0) = end y-coordinate
                        \
                        \ We can then pass this to the line clipping routine
                        \ before storing the resulting line in the ship line
                        \ heap
```

### Snippet Codice (BASIC)

```basic
OriginalFlicker-free LDA (V),Y              \ Fetch byte #2 for this edge into X, which contains
 TAX                    \ the number of the vertex at the start of the edge

 INY                    \ Increment Y to point to byte #3

 LDA (V),Y              \ Fetch byte #3 for this edge into Q, which contains
 STA Q                  \ the number of the vertex at the end of the edge
 INY                    \ Increment Y to point to byte #2

 LDA (V),Y              \ Fetch byte #2 for this edge into X, which contains
 TAX                    \ the number of the vertex at the start of the edge
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
LDA XX3+1,X            \ Fetch the x_hi coordinate of the edge's start vertex
 STA XX15+1             \ from the XX3 heap into XX15+1

 LDA XX3,X              \ Fetch the x_lo coordinate of the edge's start vertex
 STA XX15               \ from the XX3 heap into XX15

 LDA XX3+2,X            \ Fetch the y_lo coordinate of the edge's start vertex
 STA XX15+2             \ from the XX3 heap into XX15+2

 LDA XX3+3,X            \ Fetch the y_hi coordinate of the edge's start vertex
 STA XX15+3             \ from the XX3 heap into XX15+3
```

### Snippet Codice (BASIC)

```basic
OriginalFlicker-free LDX Q                  \ Set X to the number of the vertex at the end of the
                        \ edge, which we stored in Q
 INY                    \ Increment Y to point to byte #3

 LDA (V),Y              \ Fetch byte #3 for this edge into X, which contains
 TAX                    \ the number of the vertex at the end of the edge
```

### Snippet Codice (BASIC)

```basic
LDA XX3,X              \ Fetch the x_lo coordinate of the edge's end vertex
 STA XX15+4             \ from the XX3 heap into XX15+4

 LDA XX3+3,X            \ Fetch the y_hi coordinate of the edge's end vertex
 STA XX12+1             \ from the XX3 heap into XX11+1

 LDA XX3+2,X            \ Fetch the y_lo coordinate of the edge's end vertex
 STA XX12               \ from the XX3 heap into XX12

 LDA XX3+1,X            \ Fetch the x_hi coordinate of the edge's end vertex
 STA XX15+5             \ from the XX3 heap into XX15+5

 JSR LL147              \ Call LL147 to see if the new line segment needs to be
                        \ clipped to fit on-screen, returning the clipped line's
                        \ end-points in (X1, Y1) and (X2, Y2)

 BCS LL78               \ If the C flag is set then the line is not visible on
                        \ screen, so jump to LL78 so we don't store this line
                        \ in the ship line heap
```

### Snippet Codice (BASIC)

```basic
OriginalFlicker-free (Empty)
 JSR LSPUT              \ Draw this edge using flicker-free animation, by first
                        \ drawing the ship's new line and then erasing the
                        \ corresponding old line from the screen
```

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`Name`** (unknown): No description available
- **`Type`** (unknown): No description available
- **`Category`** (unknown): No description available
- **`Summary`** (unknown): No description available

```assembly
Name: LL9 (Part 11 of 12)
       Type: Subroutine
   Category: Drawing ships
    Summary: Draw ship: Add all visible edges to the ship line heap


 This part adds all the visible edges to the ship line heap, so we can draw
 them in part 12.

 Other entry points:

   LL81+2               Draw the contents of the ship line heap, used to draw
                        the ship as a dot from SHPPT
```

### Snippet Codice (BASIC)

```basic
OriginalFlicker-free.LL80

 LDY U                  \ Fetch the ship line heap pointer, which points to the
                        \ next free byte on the heap, into Y

 LDA XX15               \ Add X1 to the end of the heap
 STA (XX19),Y

 INY                    \ Increment the heap pointer

 LDA XX15+1             \ Add Y1 to the end of the heap
 STA (XX19),Y

 INY                    \ Increment the heap pointer

 LDA XX15+2             \ Add X2 to the end of the heap
 STA (XX19),Y

 INY                    \ Increment the heap pointer

 LDA XX15+3             \ Add Y2 to the end of the heap
 STA (XX19),Y

 INY                    \ Increment the heap pointer

 STY U                  \ Store the updated ship line heap pointer in U

 CPY T1                 \ If Y >= T1 then we have reached the maximum number of
 BCS LL81               \ edge lines that we can store in the ship line heap, so
                        \ skip to LL81 so we don't loop back for the next edge

.LL78

 INC XX17               \ Increment the edge counter to point to the next edge

 LDY XX17               \ If Y >= XX20, which contains the number of edges in
 CPY XX20               \ the blueprint, jump to LL81 as we have processed all
 BCS LL81               \ the edges and don't need to loop back for the next one

 LDY #0                 \ Set Y to point to byte #0 again, ready for the next
                        \ edge

 LDA V                  \ Increment V by 4 so V(1 0) points to the data for the
 ADC #4                 \ next edge
 STA V
.LL78

 LDA LSNUM              \ If LSNUM >= CNT, skip to LL81 so we don't loop back
 CMP CNT                \ for the next edge (CNT was set to the maximum heap
 BCS LL81               \ size for this ship in part 10, so this checks whether
                        \ we have just run out of space in the ship line heap,
                        \ and stops drawing edges if we have)

 LDA V                  \ Increment V by 4 so V(1 0) points to the data for the
 CLC                    \ next edge
 ADC #4
 STA V
```

### Snippet Codice (BASIC)

```basic
BCC ll81               \ If the above addition didn't overflow, jump to ll81

 INC V+1                \ Otherwise increment the high byte of V(1 0), as we
                        \ just moved the V(1 0) pointer past a page boundary

.ll81
```

### Snippet Codice (BASIC)

```basic
OriginalFlicker-free JMP LL75               \ Loop back to LL75 to process the next edge

.LL81

                        \ We have finished adding lines to the ship line heap,
                        \ so now we need to set the first byte of the heap to
                        \ the number of bytes stored there

 LDA U                  \ Fetch the ship line heap pointer from U into A, which
                        \ points to the end of the heap, and therefore contains
                        \ the heap size

 LDY #0                 \ Store A as the first byte of the ship line heap, so
 STA (XX19),Y           \ the heap is now correctly set up
 INC XX17               \ Increment the edge counter to point to the next edge

 LDY XX17               \ If Y < XX20, which contains the number of edges in
 CPY XX20               \ the blueprint, loop back to LL75 to process the next
 BCC LL75               \ edge

.LL81

 JMP LSCLR              \ Jump down to part 12 below to draw any remaining lines
                        \ from the old ship that are still in the ship line heap
```

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`Name`** (unknown): No description available
- **`Type`** (unknown): No description available
- **`Category`** (unknown): No description available
- **`Summary`** (unknown): No description available

```assembly
Name: LL9 (Part 12 of 12)
       Type: Subroutine
   Category: Drawing ships
    Summary: Draw ship: Draw all the visible edges from the ship line heap


 This part draws the lines in the ship line heap, which is used both to draw
 the ship, and to remove it from the screen.
```

### Snippet Codice (BASIC)

```basic
OriginalFlicker-free.LL155

 LDY #0                 \ Fetch the first byte from the ship line heap into A,
 LDA (XX19),Y           \ which contains the number of bytes in the heap

 STA XX20               \ Store the heap size in XX20

 CMP #4                 \ If the heap size is less than 4, there is nothing to
 BCC LL118-1            \ draw, so return from the subroutine (as LL118-1
                        \ contains an RTS)

 INY                    \ Set Y = 1, which we will use as an index into the ship
                        \ line heap, starting at byte #1 (as byte #0 contains
                        \ the heap size)

.LL27
.LSCLR

 LDY LSNUM              \ Set Y to the offset in the line heap LSNUM

.LSC1

 CPY LSNUM2             \ If Y >= LSNUM2, jump to LSC2 to return from the ship
 BCS LSC2               \ drawing routine, because the index in Y is greater
                        \ than the size of the existing ship line heap, which
                        \ means we have alrady erased all the old ships lines
                        \ when drawing the new ship

                        \ If we get here then Y < LSNUM2, which means Y is
                        \ pointing to an on-screen line from the old ship that
                        \ we need to erase
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
LDA (XX19),Y           \ Fetch the X1 line coordinate from the heap and store
 STA XX15               \ it in XX15

 INY                    \ Increment the heap pointer

 LDA (XX19),Y           \ Fetch the Y1 line coordinate from the heap and store
 STA XX15+1             \ it in XX15+1

 INY                    \ Increment the heap pointer

 LDA (XX19),Y           \ Fetch the X2 line coordinate from the heap and store
 STA XX15+2             \ it in XX15+2

 INY                    \ Increment the heap pointer

 LDA (XX19),Y           \ Fetch the Y2 line coordinate from the heap and store
 STA XX15+3             \ it in XX15+3

 JSR LL30               \ Draw a line from (X1, Y1) to (X2, Y2)

 INY                    \ Increment the heap pointer
```

### Snippet Codice (BASIC)

```basic
OriginalFlicker-free CPY XX20               \ If the heap counter is less than the size of the heap,
 BCC LL27               \ loop back to LL27 to draw the next line from the heap

 RTS                    \ Return from the subroutine
 JMP LSC1               \ Loop back to LSC1 to draw (i.e. erase) the next line
                        \ from the heap

.LSC2

 LDA LSNUM              \ Store LSNUM in the first byte of the ship line heap
 LDY #0
 STA (XX19),Y

.LSC3

 RTS                    \ Return from the subroutine
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/backporting_the_flicker-free_algorithm.html](https://elite.bbcelite.com/deep_dives/backporting_the_flicker-free_algorithm.html)*

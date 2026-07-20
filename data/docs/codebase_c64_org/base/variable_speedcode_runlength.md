---
title: Variable speedcode runlength
source_url: https://codebase.c64.org/doku.php?id=base%3Avariable_speedcode_runlength
category: reference
topics:
- raster interrupts
- assembly
- sprite programming
difficulty: beginner
language: assembly
hardware:
- KERNAL
- CIA
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

# Variable speedcode runlength

# Variable speedcode runlength

After you entered a segment of speed code at a certain spot by making use of some method discussed in the Article “[Dispatch on a byte](https://codebase.c64.org/doku.php?id=base:dispatch_on_a_byte)” we now want to exit that code at a certain spot.

Some code can be written that way, that we can also determine the runlength by the point where we enter and let it run until its end. But if we have explicit target addresses in our speedcode this just won't work.

```
                        ;<- enter here
        sta $0400
        sta $0401
        sta $0402
        sta $0403
        sta $0404
        sta $0405
        sta $0406
        sta $0407
        sta $0408
                        ;<- leave here
        sta $0409
        sta $040a
        sta $040b
        sta $040c
        sta $040d
        sta $040e
        sta $040f
```
So given the above example, we might want to enter at sta $0400 and leave after sta $0408, to do so we can modify the code and transform the upcoming sta to an rts command. After exiting the speedcode we then modify the rts back to a sta. Pretty much overhead and we would even need to call our speedcode as a subroutine. We can also leave the speedcode by a timed NMI, but that will also mean overhead in setting up and it will cost extra cycles for the IRQ and RTI.

We need speedcode with predictable runlengths (so no random penalty cycles apply) to do so, The setup is quite simple and no code has to be restored.

All you need is setting up a IRQ/NMI handler once beforehand as the exit point of your routine, setup the timer with 2 writes to e.g. $dd04/$dd05 and start a single shot timer run by setting $dd0e to $09. After that, jump to your speedcode segment and wait for the time interrupt to happen at the right spot.

An example could look like this:

```
          ;setup
          lda #$08
          sta $dd0e
          lda #$00
          sta $dd04
          sta $dd05
          lda $dd0d
          lda #$81
          sta $dd0d
          lda #<exit
          sta $fffa
          lda #>exit
          sta $fffb
          
          ...
          
          lda runlength_lo,x
          sta $dd04
          ;this can even be ommitted if we do not run more than 255 cycles
          ;lda runlength_hi,x
          ;sta $dd05
          tsx
          
          lda #$09
          sta $dd0e
          
ptr       jmp speedcode
speedcode
          sta $0400
          sta $0401
          sta $0402
          sta $0403
          sta $0404
          sta $0405
          sta $0406
          sta $0407
          sta $0408
          sta $0409
          sta $040a
          sta $040b
          sta $040c
          sta $040d
          sta $040e
          sta $040f
runlength_lo
          !byte $04,$08,$0c,$10,$14 ...
runlength_hi          
          !byte $00,$00,$00,$00,$00 ...
exit
          txs
          cli
          lda $dd0d
          ...
```
Regarding the cli instruction: This is important, as else normal irqs might be blocked until we restore the I-flag on the terminating rti, so find out for yourself if it is needed in your case. If so, you can just pull the original PC and flags from stack via pla/plp, instead of manipulating the stack pointer, or simply forgo on the cli if no further irq needs to happen.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
;<- enter here
        sta $0400
        sta $0401
        sta $0402
        sta $0403
        sta $0404
        sta $0405
        sta $0406
        sta $0407
        sta $0408
                        ;<- leave here
        sta $0409
        sta $040a
        sta $040b
        sta $040c
        sta $040d
        sta $040e
        sta $040f
```

### Snippet Codice (BASIC)

```basic
;setup
          lda #$08
          sta $dd0e
          lda #$00
          sta $dd04
          sta $dd05
          lda $dd0d
          lda #$81
          sta $dd0d
          lda #<exit
          sta $fffa
          lda #>exit
          sta $fffb
          
          ...
          
          lda runlength_lo,x
          sta $dd04
          ;this can even be ommitted if we do not run more than 255 cycles
          ;lda runlength_hi,x
          ;sta $dd05

          tsx
          
          lda #$09
          sta $dd0e
          
ptr       jmp speedcode

speedcode
          sta $0400
          sta $0401
          sta $0402
          sta $0403
          sta $0404
          sta $0405
          sta $0406
          sta $0407
          sta $0408
          sta $0409
          sta $040a
          sta $040b
          sta $040c
          sta $040d
          sta $040e
          sta $040f

runlength_lo
          !byte $04,$08,$0c,$10,$14 ...
runlength_hi          
          !byte $00,$00,$00,$00,$00 ...
exit
          txs
          cli
          lda $dd0d
          ...
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Avariable_speedcode_runlength](https://codebase.c64.org/doku.php?id=base%3Avariable_speedcode_runlength)*

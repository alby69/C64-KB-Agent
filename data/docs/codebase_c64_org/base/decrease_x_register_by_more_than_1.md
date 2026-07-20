---
title: Decreasing the X register by more than 1
source_url: https://codebase.c64.org/doku.php?id=base%3Adecrease_x_register_by_more_than_1
category: tool
topics:
- assembly
- sprite programming
difficulty: advanced
language: mixed
hardware:
- KERNAL
- CPU
- VIC-II
related:
- memory-map
- sprite-programming
- kernal-routines
- vic-ii-registers
- raster-interrupts
scraped_at: '2026-07-20'
---

# Decreasing the X register by more than 1

### Table of Contents

# Decreasing the X register by more than 1

Written by FTC/HT.

Sometimes you need/want to decrease the X register by more than one. That is often done by the following piece of code:

txa sec sbc #$xx ;where xx is (obviously) the value to decrease by.. tax

This procedure takes 8 cycles (and 5 bytes in mem). If the value of the carry flag is always known at this point in the code, the SEC instruction can be removed and the snippet would then take 6 cycles (and 4 bytes). However, there is another way to do it. You can use the illegal opcode SBX (sometimes called AXS). It operates like this:

- AND X with A and put result in X
- Subtract VALUE from X as if carry flag was set (but it doesn't matter if it's really set or not) and store result in X.

And the modified code snippet using SBX instead looks like this:

lda #$ff ;Next opcode contains a implicit AND with the A register so turn all bits ON! sbx #$xx ;where xx is the value to decrea... yes..

This code kills the A register of course, but so does the “standard” version above. It can be made even shorter by using a “txa” instruction instead of the “lda #$ff”. That works since X and A will be equal after the “txa”, and AND'ing a value with itself produces no change, hence the AND effect of SBX is “disarmed” and the subtraction will proceed as expected:

```
        txa
        sbx #$xx
```
Note that in this case you do not have to worry about the carry flag at all, and all in all the whole procedure takes only 4 cycles (and 3 bytes in mem).

If your assembler does not support illegal opcodes, remember that you can always use a .byte directive instead:

txa .byte $cb, $xx ;$cb = SBX/AXS

Another property of the SBX opcode is that it doesn't respeect the decimal mode, since it is derived from CPX rather than SBC. So if you need to perform table lookups and arithmetic in a tight interrupt routine there's no need to clear the decimal flag in case you've got some code running that operates in decimal mode.

# Examples

## Fill sprite with vertical pattern (containing $ff, $bf, $7f, $3f)

ldx #60 fs lda #xx sta spr+o0,x lda #yy sta spr+o1,x lda #$ff or $bf or $7f or $3f sta spr+o2,x axs#3 bpl fs rts

where o0,o1,o2 is an excluding choice of {0,1,2}. On one column of the sprite a must contain $ff, $bf, $7f or $3f, because if it is anded with the value of the x reg, x must be preserved. As x runs from 60 to 0 (where 63 is $3f) this is only the case for these four values.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
txa
	sec
	sbc #$xx ;where xx is (obviously) the value to decrease by..
	tax
```

### Snippet Codice (BASIC)

```basic
lda #$ff ;Next opcode contains a implicit AND with the A register so turn all bits ON!
	sbx #$xx ;where xx is the value to decrea... yes..
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
txa
        sbx #$xx
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
txa
	.byte $cb, $xx ;$cb = SBX/AXS
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
ldx #60
fs
lda #xx
sta spr+o0,x
lda #yy
sta spr+o1,x
lda #$ff or $bf or $7f or $3f
sta spr+o2,x
axs#3
bpl fs
rts
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Adecrease_x_register_by_more_than_1](https://codebase.c64.org/doku.php?id=base%3Adecrease_x_register_by_more_than_1)*

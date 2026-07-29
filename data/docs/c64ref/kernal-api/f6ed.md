---
title: or STOP Key F6ED/F770-F6FA/F77D
source_url: https://github.com/mist64/c64ref/blob/main/src/kernal/compute!'s_tool_kit:_kernal.txt
category: reference
topics:
- kernal-api
- system-routines
- jumps
difficulty: intermediate
language: assembly
hardware:
- C64
related:
- beq
- bne
- jmp
- jsr
- stop
scraped_at: '2026-07-29'
c64ref:
  module: kernal
  source_files:
  - compute!'s_tool_kit:_kernal.txt
  address: $F6ED
  sources:
  - name: 'COMPUTE!''s Tool Kit: Kernal'
    author: Dan Heeb
    description: 'ed by**: Indirect JMP through (0328) from Kernal STOP vector at
      FFE1.'
---

# $F6ED — or STOP Key F6ED/F770-F6FA/F77D ($F6ED)

## Panoramica
La routine KERNAL `None` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$F6ED`
- **Chiamata**: `JSR None` o `SYS 63213`


## Note per Fonte

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: Indirect JMP through (0328) from Kernal STOP vector at FFE1.

outine is called to test whether the STOP key is be-
ld down. When the STOP key is found down, this rou-
xits with the Z status flag set to 1, allowing the calling
e to test for this result with BEQ.

on 91 has the value of the keyboard scan for the
ey column during the last IRQ or NMI interrupt.

ation**:

 91.
ck for the value that indicates the STOP key is pressed,
/$FE.
STOP key is not pressed, then branch (BNE) to step 7 to
 with the accumulator containing last value in $91.
STOP key is pressed, then JSR FFCC (the Kernal
CFIN vector) to clear serial I/O and reset default input
 output devices, returning with accumulator cleared to 0.
 C6, the number of characters in the keyboard buffer,
s clearing the buffer.
tore the status of the comparison from step 2, thus
toring Z to 1 (BEQ condition).
.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
---
title: SuperCPU KickAssembler Library
source_url: https://codebase.c64.org/doku.php?id=base%3Asupercpu_kickassembler
category: tool
topics:
- assembly
difficulty: intermediate
language: mixed
hardware:
- CPU
- KERNAL
- CIA
related:
- keyboard-handling
- memory-map
- joystick-reading
- kernal-routines
- cia-registers
scraped_at: '2026-07-20'
---

# SuperCPU KickAssembler Library

### Table of Contents

# SuperCPU KickAssembler Library

Over the years after the SuperCPU became emulated in Vice, I've developed a series of pseudocommands and macros for KickAssembler to take advantage of the SuperCPU merely out of curiosity. It is now somewhat complete and ported into the wiki.

NB! Opcode descriptions are ripped from the “Programming the 65816” by WDC, there may be errors. Feel free to rectify or adjust as neccessary (in the routines as well as they are not fully tested and may contain bugs.

## Regular opcodes

The following opcodes does not need any special pseudocommands as they use the exact same opcode values as the 6510/6502 (NB! Some opcodes behaves differently as briefly indicated (and may also use a different amount of cycles)):

```
    asl - 16 bit accumulator mode shifts 16 bits
    bcc
    bcs
    beq
    bmi
    bne
    bpl
    brk - Resets Decimal Flag in native mode
    bvc
    bvs
    clc
    cld
    cli
    clv
    dex - 16 bit index register mode decreases 16 bit X with 1 (dex16 pseudo available)
    dey - 16 bit index register mode decreases 16 bit Y with 1 (dey16 pseudo available)
    inx - 16 bit index register mode increases 16 bit X with 1 (inx16 pseudo available)
    iny - 16 bit index register mode increases 16 bit Y with 1 (iny16 pseudo available)
    lsr - 16 bit accumulator mote shifts 16 bits
    nop
    php - Does not push the e-flag
    plp - Does not pull the e-flag
    rol - 16 bit accumulator mode shifts 16 bits
    ror - 16 bit accumulator mode shifts 16 bits
    rti - Pulls 4 bytes in native mode (+PB)
    rts
    sec
    sed
    sei
    stx - Stores 16 bits in 16 bit index register mode
    sty - Stores 16 bits in 16 bit index register mode
    tax - 16 bit index register mode copies 16 bits
    tay - 16 bit index register mode copies 16 bits
    tsx - 16 bit index register mode copies 16 bits
    txa - 16 bit accumulator register mode copies 16 bits
    txs - 16 bit index register mode copies 16 bits
    tya - 16 bit accumulator register mode copies 16 bits
```
## Pseudocommands

- [BRA / BRL](https://codebase.c64.org/doku.php?id=base:supercpu_bra)- Merged
- [DEC](https://codebase.c64.org/doku.php?id=base:supercpu_dec)- Decreases A or M with 1
- [DEX](https://codebase.c64.org/doku.php?id=base:supercpu_dex)- Decreases X with passed parameter
- [DEY](https://codebase.c64.org/doku.php?id=base:supercpu_dey)- Decreases Y with passed parameter
- [INC](https://codebase.c64.org/doku.php?id=base:supercpu_inc)- Increases A or M with 1
- [INX](https://codebase.c64.org/doku.php?id=base:supercpu_inx)- Increases X with passed parameter
- [INY](https://codebase.c64.org/doku.php?id=base:supercpu_iny)- Increases Y with passed parameter

The following opcodes are not implemented:

- COP - Coprocessor, Not usefull.
- WDM - Future Expansion, does not do anything.

## Macros

This section contains some usefull macros which will simplify coding the SuperCPU.

NB! They are implemented as pseudos, but should be made into Macros instead. Perhaps a future exercise.

## Issues

There are some hurdles which currently presents some of challenges;

- The VICE monitor (as far as I know), as of now, cannot handle 16 bit immediate values. So when stepping through code or listing code in the monitor all immediate values are treated as 8 bits (it's emulated as 16 but listed as 8!). This makes following code in the monitor a bit harder.

- KickAssembler does not allow you to do conditional trickery (.if) to an unresolved label. This is an issue for example when implementing a branch pseudo as it will not accept unresolved lables when calculating the relative branch distance in the pseudo when branching forwards (backwards works as the previous label is already resolved).

- Zero (Direct) Page addressing modes is also suffering from the unresolved label issue as the size of the absolute value is determined by a .if. If I remeber correctly, KickAssembler has a hard time passing ZP,x as KA automatically treats all as 16 bit but does some trickery later to shave down to 8 bits which does not pass well to pseudos. This may have been fixed though / I may recall wrong, so should be verified.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
asl - 16 bit accumulator mode shifts 16 bits
    bcc
    bcs
    beq
    bmi
    bne
    bpl
    brk - Resets Decimal Flag in native mode
    bvc
    bvs
    clc
    cld
    cli
    clv
    dex - 16 bit index register mode decreases 16 bit X with 1 (dex16 pseudo available)
    dey - 16 bit index register mode decreases 16 bit Y with 1 (dey16 pseudo available)
    inx - 16 bit index register mode increases 16 bit X with 1 (inx16 pseudo available)
    iny - 16 bit index register mode increases 16 bit Y with 1 (iny16 pseudo available)
    lsr - 16 bit accumulator mote shifts 16 bits
    nop
    php - Does not push the e-flag
    plp - Does not pull the e-flag
    rol - 16 bit accumulator mode shifts 16 bits
    ror - 16 bit accumulator mode shifts 16 bits
    rti - Pulls 4 bytes in native mode (+PB)
    rts
    sec
    sed
    sei
    stx - Stores 16 bits in 16 bit index register mode
    sty - Stores 16 bits in 16 bit index register mode
    tax - 16 bit index register mode copies 16 bits
    tay - 16 bit index register mode copies 16 bits
    tsx - 16 bit index register mode copies 16 bits
    txa - 16 bit accumulator register mode copies 16 bits
    txs - 16 bit index register mode copies 16 bits
    tya - 16 bit accumulator register mode copies 16 bits
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Asupercpu_kickassembler](https://codebase.c64.org/doku.php?id=base%3Asupercpu_kickassembler)*

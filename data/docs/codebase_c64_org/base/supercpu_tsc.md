---
title: TSC
source_url: https://codebase.c64.org/doku.php?id=base%3Asupercpu_tsc
category: reference
topics:
- sprite programming
- assembly
difficulty: intermediate
language: assembly
hardware:
- CPU
related:
- sprite-programming
- raster-interrupts
- vic-ii-registers
scraped_at: '2026-07-14'
---

# TSC

base:supercpu_tsc

                # TSC

```
    /*-------------------------------------------------------------------------
    OP CODE: TSC (Transfer Stack pointer to 16-bit aCcumulator)
    ===========================================================
    Addressing Modes:
        Implied                            ($3b - 1 byte, 2 cycles)
    Flags Affected:
        n - Set if most significant bit of transferred value is set; else
            cleared.
        z - Set if value transferred is zero; else cleared.
    Description:
        Transfer the value in the sixteen-bit stack pointer S to the
        sixteen-bit accumulator C, regardless of the setting of the
        accumulator/memory mode flag.
        An alternate mnemonic is TSA (transfer the value in the stack pointer
        to the A accumulator).
        In TSC, the “C” is used to indicate that sixteen bits are transferred
        regardless of the m flag. If the A accumulator is set to just eight
        bits (whether because the m flag is set, or because the processor is in
        6502 emulation mode), then it takes the value of the low byte of the
        stack pointer and the hidden B accumulator takes the value of the high
        byte of the stack pointer. (In emulation mode, B will always take a
        value of one, since the stack is confined to page one.)
        The stack pointer’s value is unchanged by the operation.
    Notes:
    -------------------------------------------------------------------------*/
    .pseudocommand tsc {
        .byte $3b
    }
```
base/supercpu_tsc.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
/*-------------------------------------------------------------------------
    OP CODE: TSC (Transfer Stack pointer to 16-bit aCcumulator)
    ===========================================================

    Addressing Modes:
        Implied                            ($3b - 1 byte, 2 cycles)

    Flags Affected:
        n - Set if most significant bit of transferred value is set; else
            cleared.
        z - Set if value transferred is zero; else cleared.

    Description:
        Transfer the value in the sixteen-bit stack pointer S to the
        sixteen-bit accumulator C, regardless of the setting of the
        accumulator/memory mode flag.

        An alternate mnemonic is TSA (transfer the value in the stack pointer
        to the A accumulator).

        In TSC, the “C” is used to indicate that sixteen bits are transferred
        regardless of the m flag. If the A accumulator is set to just eight
        bits (whether because the m flag is set, or because the processor is in
        6502 emulation mode), then it takes the value of the low byte of the
        stack pointer and the hidden B accumulator takes the value of the high
        byte of the stack pointer. (In emulation mode, B will always take a
        value of one, since the stack is confined to page one.)

        The stack pointer’s value is unchanged by the operation.

    Notes:

    -------------------------------------------------------------------------*/

    .pseudocommand tsc {
        .byte $3b
    }
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Asupercpu_tsc](https://codebase.c64.org/doku.php?id=base%3Asupercpu_tsc)*

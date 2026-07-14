---
title: TCD
source_url: https://codebase.c64.org/doku.php?id=base%3Asupercpu_tcd
category: reference
topics: []
difficulty: intermediate
language: none
hardware:
- CPU
related: []
scraped_at: '2026-07-14'
---

# TCD

base:supercpu_tcd

                # TCD

```
    /*-------------------------------------------------------------------------
    OP CODE: TCD (Transfer 16-Bit aCcumulator to Direct page register)
    ==================================================================
    
    Addressing Modes:
        Implied                            ($5b - 1 byte, 2 cycles)
    Flags Affected:
        n - Set if most significant bit of transferred value is set; else
            cleared.
        z - Set if value transferred is zero; else cleared.
    Description:
        Transfer the value in the sixteen-bit accumulator C to the direct page
        register D, regardless of the setting of the accumulator/memory mode
        flag.
        An alternate mnemonic is TAD, (transfer the value in the A accumulator
        to the direct page register).
        In TCD, the “C” is used to indicate that sixteen bits are transferred
        regardless of the m flag. If the A accumulator is set to just eight
        bits (whether because the m flag is set, or because the processor is in
        6502 emulation mode), then its value becomes the low byte of the direct
        page register and the value in the hidden B accumulator becomes the
        high byte of the direct page register.
        The accumulator’s sixteen-bit value is unchanged by the operation.
    Notes:
    -------------------------------------------------------------------------*/
    .pseudocommand tcd {
        .byte $5b
    }
```
base/supercpu_tcd.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
/*-------------------------------------------------------------------------
    OP CODE: TCD (Transfer 16-Bit aCcumulator to Direct page register)
    ==================================================================
    
    Addressing Modes:
        Implied                            ($5b - 1 byte, 2 cycles)

    Flags Affected:
        n - Set if most significant bit of transferred value is set; else
            cleared.
        z - Set if value transferred is zero; else cleared.

    Description:
        Transfer the value in the sixteen-bit accumulator C to the direct page
        register D, regardless of the setting of the accumulator/memory mode
        flag.

        An alternate mnemonic is TAD, (transfer the value in the A accumulator
        to the direct page register).

        In TCD, the “C” is used to indicate that sixteen bits are transferred
        regardless of the m flag. If the A accumulator is set to just eight
        bits (whether because the m flag is set, or because the processor is in
        6502 emulation mode), then its value becomes the low byte of the direct
        page register and the value in the hidden B accumulator becomes the
        high byte of the direct page register.

        The accumulator’s sixteen-bit value is unchanged by the operation.

    Notes:

    -------------------------------------------------------------------------*/

    .pseudocommand tcd {
        .byte $5b
    }
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Asupercpu_tcd](https://codebase.c64.org/doku.php?id=base%3Asupercpu_tcd)*

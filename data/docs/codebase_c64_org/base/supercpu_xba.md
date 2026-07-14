---
title: XBA
source_url: https://codebase.c64.org/doku.php?id=base%3Asupercpu_xba
category: reference
topics: []
difficulty: intermediate
language: none
hardware:
- KERNAL
- CPU
related:
- memory-map
- kernal-routines
scraped_at: '2026-07-14'
---

# XBA

base:supercpu_xba

                # XBA

```
    /*-------------------------------------------------------------------------
    OP CODE: XBA (eXchange the B and A accumulators)
    ================================================
    
    Addressing Modes:
        Implied                            ($eb - 1 byte, 3 cycles)
    Flags Affected:
        n - Set if most significant bit of new 8-bit value A accumulator is
            set; else cleared.
        z - Set if new 8-bit value in A accumulator is zero; else cleared.
    Description:
        B represents the high-order byte of the sixteen-bit C accumulator, and
        A in this case represents the loworder byte. XBA swaps the contents of
        the low-order and high-order bytes of C.
        An alternate mnemonic is SWA (swap the high and low bytes of the
        sixteen-bit A accumulator).
        XBA can be used to invert the low-order, high-order arrangement of a
        sixteen-bit value, or to temporarily store an eight-bit value from the
        A accumulator into B. Since it is an exchange, the previous contents of
        both accumulators are changed, replaced by the previous contents of the
        other.
        Neither the mode select flags nor the emulation mode flag affects this
        operation.
        The flags are changed based on the new value of the low byte, the A
        accumulator (that is, on the former value of the high byte, the B
        accumulator), even in sixteen-bit accumulator mode.
    Notes:
    -------------------------------------------------------------------------*/
    .pseudocommand xba {
        .byte $eb
    }
```
base/supercpu_xba.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
/*-------------------------------------------------------------------------
    OP CODE: XBA (eXchange the B and A accumulators)
    ================================================
    
    Addressing Modes:
        Implied                            ($eb - 1 byte, 3 cycles)

    Flags Affected:
        n - Set if most significant bit of new 8-bit value A accumulator is
            set; else cleared.
        z - Set if new 8-bit value in A accumulator is zero; else cleared.

    Description:
        B represents the high-order byte of the sixteen-bit C accumulator, and
        A in this case represents the loworder byte. XBA swaps the contents of
        the low-order and high-order bytes of C.

        An alternate mnemonic is SWA (swap the high and low bytes of the
        sixteen-bit A accumulator).

        XBA can be used to invert the low-order, high-order arrangement of a
        sixteen-bit value, or to temporarily store an eight-bit value from the
        A accumulator into B. Since it is an exchange, the previous contents of
        both accumulators are changed, replaced by the previous contents of the
        other.

        Neither the mode select flags nor the emulation mode flag affects this
        operation.

        The flags are changed based on the new value of the low byte, the A
        accumulator (that is, on the former value of the high byte, the B
        accumulator), even in sixteen-bit accumulator mode.

    Notes:

    -------------------------------------------------------------------------*/

    .pseudocommand xba {
        .byte $eb
    }
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Asupercpu_xba](https://codebase.c64.org/doku.php?id=base%3Asupercpu_xba)*

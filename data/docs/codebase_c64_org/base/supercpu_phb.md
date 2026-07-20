---
title: PHB
source_url: https://codebase.c64.org/doku.php?id=base%3Asupercpu_phb
category: reference
topics:
- assembly
- sprite programming
difficulty: intermediate
language: assembly
hardware:
- CPU
related:
- vic-ii-registers
- raster-interrupts
- sprite-programming
scraped_at: '2026-07-20'
---

# PHB

base:supercpu_phb

                # PHB

```
    /*-------------------------------------------------------------------------
    OP CODE: PHB (PusH data Bank register)
    ======================================
    Addressing Modes:
        Stack                            ($8b - 1 byte, 3 cycles)
    Flags Affected:
        N/A
    Description:
        Push the contents of the data bank register onto the stack.
        The single-byte contents of the data bank registers are pushed onto the
        stack; the stack pointer now points to the next available stack
        location, directly below the byte pushed. The data bank register itself
        is unchanged. Since the data bank register is an eight-bit register,
        only one byte is pushed onto the stack, regardless of the settings of
        the m and x mode select flags.
        While the 65816 always generates 24-bit addresses, most memory
        references are specified by a sixteenbit address. These addresses are
        concatenated with the contents of the data bank register to form a full
        24-bit address. This instruction lets the current value of the data
        bank register be saved prior to loading a new value.
    Notes:
    -------------------------------------------------------------------------*/
    .pseudocommand phb {
        .byte $8b
    }
```
base/supercpu_phb.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
/*-------------------------------------------------------------------------
    OP CODE: PHB (PusH data Bank register)
    ======================================

    Addressing Modes:
        Stack                            ($8b - 1 byte, 3 cycles)

    Flags Affected:
        N/A

    Description:
        Push the contents of the data bank register onto the stack.

        The single-byte contents of the data bank registers are pushed onto the
        stack; the stack pointer now points to the next available stack
        location, directly below the byte pushed. The data bank register itself
        is unchanged. Since the data bank register is an eight-bit register,
        only one byte is pushed onto the stack, regardless of the settings of
        the m and x mode select flags.

        While the 65816 always generates 24-bit addresses, most memory
        references are specified by a sixteenbit address. These addresses are
        concatenated with the contents of the data bank register to form a full
        24-bit address. This instruction lets the current value of the data
        bank register be saved prior to loading a new value.

    Notes:

    -------------------------------------------------------------------------*/

    .pseudocommand phb {
        .byte $8b
    }
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Asupercpu_phb](https://codebase.c64.org/doku.php?id=base%3Asupercpu_phb)*

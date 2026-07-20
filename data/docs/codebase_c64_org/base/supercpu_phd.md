---
title: PHD
source_url: https://codebase.c64.org/doku.php?id=base%3Asupercpu_phd
category: reference
topics:
- assembly
- sprite programming
difficulty: intermediate
language: assembly
hardware: []
related:
- vic-ii-registers
- raster-interrupts
- sprite-programming
scraped_at: '2026-07-20'
---

# PHD

base:supercpu_phd

                # PHD

```
    /*-------------------------------------------------------------------------
    OP CODE: PHD (PusH Direct page register)
    ========================================
    
    Addressing Modes:
        Stack (Push)                    ($0b - 1 byte, 4 cycles)
    Flags Affected:
        N/A
    Description:
        Push the contents of the direct page register D onto the stack.
        Since the direct page register is always a sixteen-bit register, this
        is always a sixteen-bit operation, regardless of the settings of the m
        and x mode select flags. The high byte of the direct page register is
        pushed first, then the low byte. The direct page register itself is
        unchanged. The stack pointer now points to the next available stack
        location, directly below the last byte pushed.
        By pushing the D register onto the stack, the local environment of a
        calling subroutine may easily be saved a called subroutine before
        modifying the D register to provide itself with its own direct page
        memory.
    Notes:
    -------------------------------------------------------------------------*/
    .pseudocommand phd {
        .byte $0b
    }
```
base/supercpu_phd.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
/*-------------------------------------------------------------------------
    OP CODE: PHD (PusH Direct page register)
    ========================================
    
    Addressing Modes:
        Stack (Push)                    ($0b - 1 byte, 4 cycles)

    Flags Affected:
        N/A

    Description:
        Push the contents of the direct page register D onto the stack.

        Since the direct page register is always a sixteen-bit register, this
        is always a sixteen-bit operation, regardless of the settings of the m
        and x mode select flags. The high byte of the direct page register is
        pushed first, then the low byte. The direct page register itself is
        unchanged. The stack pointer now points to the next available stack
        location, directly below the last byte pushed.

        By pushing the D register onto the stack, the local environment of a
        calling subroutine may easily be saved a called subroutine before
        modifying the D register to provide itself with its own direct page
        memory.

    Notes:

    -------------------------------------------------------------------------*/

    .pseudocommand phd {
        .byte $0b
    }
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Asupercpu_phd](https://codebase.c64.org/doku.php?id=base%3Asupercpu_phd)*

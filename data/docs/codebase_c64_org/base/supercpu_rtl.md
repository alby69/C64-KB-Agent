---
title: RTL
source_url: https://codebase.c64.org/doku.php?id=base%3Asupercpu_rtl
category: reference
topics:
- sprite programming
- assembly
difficulty: intermediate
language: mixed
hardware:
- KERNAL
related:
- sprite-programming
- memory-map
- raster-interrupts
- kernal-routines
- vic-ii-registers
scraped_at: '2026-07-14'
---

# RTL

base:supercpu_rtl

                # RTL

```
    /*-------------------------------------------------------------------------
    OP CODE: RTL (ReTurn from subroutine Long)
    ==========================================
    
    Addressing Modes:
        Stack                            ($6b - 1 byte, 6 cycles)
    Flags Affected:
        N/A
    Description:
        Pull the program counter (incrementing the stacked, sixteen-bit value
        by one before loading the program counter with it), then the program
        bank register from the stack.
        When a subroutine in another bank is called (via a jump to subroutine
        long instruction), the current bank address is pushed onto the stack
        along with the return address. To return to the calling bank, a long
        return instruction must be executed, which first pulls the return
        address from the stack, increments it, and loads the program counter
        with it, then pulls the calling bank from the stack and loads the
        program bank register. This transfers control to the instruction
        immediately following the original jump to subroutine long.
                                              STACK
                                    |                       |
                                    +-----------------------+
            Stack Pointer After  -->|  Return Bank Address  |
                                    +-----------------------+
                                    |  Return Address High  |
                                    +-----------------------+
                                    |  Return Address Low   |
                                    +-----------------------+
            Stack Pointer Before -->|                       |
                                    +-----------------------+
                                    |                       |
                                             Bank 0
    Notes:
    -------------------------------------------------------------------------*/
    .pseudocommand rtl {
        .byte $6b
    }
```
base/supercpu_rtl.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
/*-------------------------------------------------------------------------
    OP CODE: RTL (ReTurn from subroutine Long)
    ==========================================
    
    Addressing Modes:
        Stack                            ($6b - 1 byte, 6 cycles)

    Flags Affected:
        N/A

    Description:
        Pull the program counter (incrementing the stacked, sixteen-bit value
        by one before loading the program counter with it), then the program
        bank register from the stack.
        When a subroutine in another bank is called (via a jump to subroutine
        long instruction), the current bank address is pushed onto the stack
        along with the return address. To return to the calling bank, a long
        return instruction must be executed, which first pulls the return
        address from the stack, increments it, and loads the program counter
        with it, then pulls the calling bank from the stack and loads the
        program bank register. This transfers control to the instruction
        immediately following the original jump to subroutine long.

                                              STACK
                                    |                       |
                                    +-----------------------+
            Stack Pointer After  -->|  Return Bank Address  |
                                    +-----------------------+
                                    |  Return Address High  |
                                    +-----------------------+
                                    |  Return Address Low   |
                                    +-----------------------+
            Stack Pointer Before -->|                       |
                                    +-----------------------+
                                    |                       |
                                             Bank 0

    Notes:

    -------------------------------------------------------------------------*/

    .pseudocommand rtl {
        .byte $6b
    }
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Asupercpu_rtl](https://codebase.c64.org/doku.php?id=base%3Asupercpu_rtl)*

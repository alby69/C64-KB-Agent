---
title: PLX
source_url: https://codebase.c64.org/doku.php?id=base%3Asupercpu_plx
category: reference
topics:
- sprite programming
- assembly
difficulty: intermediate
language: mixed
hardware:
- KERNAL
- CPU
related:
- sprite-programming
- memory-map
- raster-interrupts
- kernal-routines
- vic-ii-registers
scraped_at: '2026-07-14'
---

# PLX

base:supercpu_plx

                # PLX

```
    /*-------------------------------------------------------------------------
    OP CODE: PLX (PulL index register X from stack)
    ===============================================
    
    Addressing Modes:
        Stack                            ($fa - 1 byte, 4 cycles¹)
        ¹ - Add 1 cycle if x = 0 (16-bit index registers)
    Flags Affected:
        n - Set if most significant bit of pulled value is set; else cleared.
        z - Set if value pulled is zero; else cleared.
    Description:
        Pull the value on the top of the stack into the X index register. The
        previous contents of the register are destroyed.
        8-bit index registers (all processors): The stack pointer is first
        incremented. Then the byte pointed to by the stack pointer is loaded
        into the register.
        16-bit index registers (65802/65816 only, x = 0): Both bytes of the
        index register are pulled. First the low-order byte of the index
        register is pulled, then the high-order byte of the index register is
        pulled.
        Unlike some other microprocessors, the 65x instructions to pull an
        index register affect the negative and zero flags.
    Notes:
    -------------------------------------------------------------------------*/
    .pseudocommand plx {
        .byte $fa
    }
```
base/supercpu_plx.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
/*-------------------------------------------------------------------------
    OP CODE: PLX (PulL index register X from stack)
    ===============================================
    
    Addressing Modes:
        Stack                            ($fa - 1 byte, 4 cycles¹)
        ¹ - Add 1 cycle if x = 0 (16-bit index registers)

    Flags Affected:
        n - Set if most significant bit of pulled value is set; else cleared.
        z - Set if value pulled is zero; else cleared.

    Description:
        Pull the value on the top of the stack into the X index register. The
        previous contents of the register are destroyed.

        8-bit index registers (all processors): The stack pointer is first
        incremented. Then the byte pointed to by the stack pointer is loaded
        into the register.

        16-bit index registers (65802/65816 only, x = 0): Both bytes of the
        index register are pulled. First the low-order byte of the index
        register is pulled, then the high-order byte of the index register is
        pulled.

        Unlike some other microprocessors, the 65x instructions to pull an
        index register affect the negative and zero flags.

    Notes:


    -------------------------------------------------------------------------*/

    .pseudocommand plx {
        .byte $fa
    }
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Asupercpu_plx](https://codebase.c64.org/doku.php?id=base%3Asupercpu_plx)*

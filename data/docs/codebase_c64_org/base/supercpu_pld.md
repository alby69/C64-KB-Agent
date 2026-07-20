---
title: PLD
source_url: https://codebase.c64.org/doku.php?id=base%3Asupercpu_pld
category: reference
topics:
- assembly
- sprite programming
difficulty: intermediate
language: assembly
hardware:
- KERNAL
related:
- memory-map
- sprite-programming
- kernal-routines
- vic-ii-registers
- raster-interrupts
scraped_at: '2026-07-20'
---

# PLD

base:supercpu_pld

                # PLD

```
    /*-------------------------------------------------------------------------
    OP CODE: PLD (PulL Direct page register)
    ========================================
    
    Addressing Modes:
        Stack                            ($ab - 1 byte, 5 cycles)
    Flags Affected:
        n - Set if most significant bit of pulled value is set; else cleared.
        z - Set if value pulled is zero; else cleared.
    Description:
        Pull the sixteen-bit value on top of the stack into the direct page
        register D, switching the direct page to that value.
        PLD is typically used to restore the direct page register to a previous
        value.
        Since the direct page register is a sixteen-bit register, two byte are
        pulled from the stack, regardless of the settings of the m and x mode
        select flags. The low byte of the direct page register is pulled first,
        then the high byte. The stack pointer now points to where the high byte
        just pulled was stored; this is now the next available stack location.
    Notes:
    -------------------------------------------------------------------------*/
    .pseudocommand pld {
        .byte $2b
    }
```
base/supercpu_pld.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
/*-------------------------------------------------------------------------
    OP CODE: PLD (PulL Direct page register)
    ========================================
    
    Addressing Modes:
        Stack                            ($ab - 1 byte, 5 cycles)

    Flags Affected:
        n - Set if most significant bit of pulled value is set; else cleared.
        z - Set if value pulled is zero; else cleared.

    Description:
        Pull the sixteen-bit value on top of the stack into the direct page
        register D, switching the direct page to that value.

        PLD is typically used to restore the direct page register to a previous
        value.

        Since the direct page register is a sixteen-bit register, two byte are
        pulled from the stack, regardless of the settings of the m and x mode
        select flags. The low byte of the direct page register is pulled first,
        then the high byte. The stack pointer now points to where the high byte
        just pulled was stored; this is now the next available stack location.

    Notes:


    -------------------------------------------------------------------------*/

    .pseudocommand pld {
        .byte $2b
    }
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Asupercpu_pld](https://codebase.c64.org/doku.php?id=base%3Asupercpu_pld)*

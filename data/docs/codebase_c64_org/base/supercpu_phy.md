---
title: PHY
source_url: https://codebase.c64.org/doku.php?id=base%3Asupercpu_phy
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

# PHY

base:supercpu_phy

                # PHY

```
    /*-------------------------------------------------------------------------
    OP CODE: PHY (PusH index register Y to stack)
    =============================================
    
    Addressing Modes:
        Stack                            ($5a - 1 byte, 3 cycles¹)
        ¹ - Add 1 cycle if x = 0 (16-bit index registers)
    Flags Affected:
        N/A
    Description:
        Push the contents of the Y index register onto the stack. The register
        itself is unchanged.
        
        8-bit index registers (all processors): The eight-bit contents of the
        index register are pushed onto the stack. The stack pointer now points
        to the next available stack location, directly below the byte pushed.
        16-bit index registers (65802/65816 only, x = 0): The sixteen-bit
        contents of the index register are pushed. The high byte is pushed
        first, then the low byte. The stack pointer now points to the next
        available stack location, directly below the last byte pushed.
    Notes:
    -------------------------------------------------------------------------*/
    .pseudocommand phy {
        .byte $5a
    }
```
base/supercpu_phy.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
/*-------------------------------------------------------------------------
    OP CODE: PHY (PusH index register Y to stack)
    =============================================
    
    Addressing Modes:
        Stack                            ($5a - 1 byte, 3 cycles¹)
        ¹ - Add 1 cycle if x = 0 (16-bit index registers)

    Flags Affected:
        N/A

    Description:
        Push the contents of the Y index register onto the stack. The register
        itself is unchanged.
        
        8-bit index registers (all processors): The eight-bit contents of the
        index register are pushed onto the stack. The stack pointer now points
        to the next available stack location, directly below the byte pushed.

        16-bit index registers (65802/65816 only, x = 0): The sixteen-bit
        contents of the index register are pushed. The high byte is pushed
        first, then the low byte. The stack pointer now points to the next
        available stack location, directly below the last byte pushed.

    Notes:

    -------------------------------------------------------------------------*/

    .pseudocommand phy {
        .byte $5a
    }
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Asupercpu_phy](https://codebase.c64.org/doku.php?id=base%3Asupercpu_phy)*

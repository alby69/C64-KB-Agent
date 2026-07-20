---
title: PEI
source_url: https://codebase.c64.org/doku.php?id=base%3Asupercpu_pei
category: tool
topics:
- basic
- assembly
- sprite programming
difficulty: intermediate
language: assembly
hardware:
- SID
related:
- sid-registers
- music-player
- sprite-programming
- sound-programming
- vic-ii-registers
- raster-interrupts
scraped_at: '2026-07-20'
---

# PEI

base:supercpu_pei

                # PEI

```
    /*-------------------------------------------------------------------------
    OP CODE: PEI (Push Effective Indirect address)
    ==============================================
    
    Addressing Modes:
        Stack (Direct Page Indirect)    ($d4 - 2 bytes, 6 cycles¹)
        ¹ - Add 1 cycle if low byte of Direct Page register is other than zero
            (DL< >0)
    Flags Affected:
        N/A
    Description:
        Push the sixteen-bit value located at the address formed by adding the
        direct page offset specified by the operand to the data page register.
        The mnemonic implies that the sixteen-bit data pushed is considered an
        address, although it can be any sixteen-bit data. This operation always
        pushes sixteen bits of data, irrespective of the settings of the m and
        x mode select flags.
        The first byte pushed is the byte at the direct page offset plus one
        (the high byte of the double byte stored at the direct page offset).
        The byte at the direct page offset itself (the low byte) is pushed
        next. The stack pointer now points to the next available stack
        location, directly below the last byte pushed.
        The assembler syntax is that of direct page indirect; however, unlike
        other instructions which use this assembler syntax, the effective
        indirect address, rather than the data stored at that address, is what
        is accessed and pushed onto the stack.
    Notes:
    -------------------------------------------------------------------------*/
    .pseudocommand pei val {
        .if (val.getType()==AT_INDIRECT) {
            .byte $d4, val.getValue()
        }
    }
```
base/supercpu_pei.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
/*-------------------------------------------------------------------------
    OP CODE: PEI (Push Effective Indirect address)
    ==============================================
    
    Addressing Modes:
        Stack (Direct Page Indirect)    ($d4 - 2 bytes, 6 cycles¹)
        ¹ - Add 1 cycle if low byte of Direct Page register is other than zero
            (DL< >0)

    Flags Affected:
        N/A

    Description:
        Push the sixteen-bit value located at the address formed by adding the
        direct page offset specified by the operand to the data page register.
        The mnemonic implies that the sixteen-bit data pushed is considered an
        address, although it can be any sixteen-bit data. This operation always
        pushes sixteen bits of data, irrespective of the settings of the m and
        x mode select flags.

        The first byte pushed is the byte at the direct page offset plus one
        (the high byte of the double byte stored at the direct page offset).
        The byte at the direct page offset itself (the low byte) is pushed
        next. The stack pointer now points to the next available stack
        location, directly below the last byte pushed.

        The assembler syntax is that of direct page indirect; however, unlike
        other instructions which use this assembler syntax, the effective
        indirect address, rather than the data stored at that address, is what
        is accessed and pushed onto the stack.

    Notes:

    -------------------------------------------------------------------------*/

    .pseudocommand pei val {
        .if (val.getType()==AT_INDIRECT) {
            .byte $d4, val.getValue()
        }
    }
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Asupercpu_pei](https://codebase.c64.org/doku.php?id=base%3Asupercpu_pei)*

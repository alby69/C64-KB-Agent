---
title: JSR
source_url: https://codebase.c64.org/doku.php?id=base%3Asupercpu_jsr
category: tool
topics:
- sprite programming
- assembly
difficulty: intermediate
language: assembly
hardware: []
related:
- sprite-programming
- raster-interrupts
- vic-ii-registers
scraped_at: '2026-07-14'
---

# JSR

base:supercpu_jsr

                # JSR

```
    /*-------------------------------------------------------------------------
    OP CODE: JSR (Jump to SubRoutine)
    =================================
    
    Addressing Modes:
        Absolute                         ($20 - 3 bytes, 6 cycles)
        Absolute Indexed Indirect        ($fc - 3 bytes, 8 cycles)
        Absolute Long                    ($22 - 4 bytes, 8 cycles)
    Flags Affected:
        N/A
    Description:
        Transfer control to the subroutine at the location specified by the
        operand, after first pushing onto the stack, as a return address, the
        current program counter value, that is, the address of the last
        instruction byte (the third byte of a three-byte instruction, the
        fourth byte of a four-byte instruction), not the address of the next
        instruction.
        If an absolute operand is coded and is less than or equal to $FFFF,
        absolute addressing is assumed by the assembler; if the value is
        greater than $FFFF, absolute long addressing is used.
        If long addressing is used, the current program counter bank is pushed
        onto the stack first. Next – or first in the more normal case of
        intra-bank addressing – the high order byte of the return address is
        pushed, followed by the low order byte. This leaves it on the stack in
        standard 65x order (lowest byte at the lowest address, highest byte at
        the highest address). After the return address is pushed, the stack
        pointer points to the next available location (next lower byte) on the
        stack. Finally, the program counter (and, in the case of long
        addressing, the program counter bank register) is loaded with the
        values specified by the operand, and control is transferred to the
        target location.
    Notes:
    -------------------------------------------------------------------------*/
    .pseudocommand jsr val {
        .if (val.getType()==AT_ABSOLUTE) {
            .if (val.getValue()<$10000) {
                .byte $20, <val.getValue(), >val.getValue()
            } else {
                .byte $22, <val.getValue(), >val.getValue(), val.getValue() >> 16
            }
        }
        .if (val.getType()==AT_ABSOLUTEX) {
            .byte $fc, <val.getValue(), >val.getValue()
        }
    }
```
base/supercpu_jsr.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
/*-------------------------------------------------------------------------
    OP CODE: JSR (Jump to SubRoutine)
    =================================
    
    Addressing Modes:
        Absolute                         ($20 - 3 bytes, 6 cycles)
        Absolute Indexed Indirect        ($fc - 3 bytes, 8 cycles)
        Absolute Long                    ($22 - 4 bytes, 8 cycles)

    Flags Affected:
        N/A

    Description:
        Transfer control to the subroutine at the location specified by the
        operand, after first pushing onto the stack, as a return address, the
        current program counter value, that is, the address of the last
        instruction byte (the third byte of a three-byte instruction, the
        fourth byte of a four-byte instruction), not the address of the next
        instruction.
        If an absolute operand is coded and is less than or equal to $FFFF,
        absolute addressing is assumed by the assembler; if the value is
        greater than $FFFF, absolute long addressing is used.
        If long addressing is used, the current program counter bank is pushed
        onto the stack first. Next – or first in the more normal case of
        intra-bank addressing – the high order byte of the return address is
        pushed, followed by the low order byte. This leaves it on the stack in
        standard 65x order (lowest byte at the lowest address, highest byte at
        the highest address). After the return address is pushed, the stack
        pointer points to the next available location (next lower byte) on the
        stack. Finally, the program counter (and, in the case of long
        addressing, the program counter bank register) is loaded with the
        values specified by the operand, and control is transferred to the
        target location.

    Notes:

    -------------------------------------------------------------------------*/

    .pseudocommand jsr val {
        .if (val.getType()==AT_ABSOLUTE) {
            .if (val.getValue()<$10000) {
                .byte $20, <val.getValue(), >val.getValue()
            } else {
                .byte $22, <val.getValue(), >val.getValue(), val.getValue() >> 16
            }
        }

        .if (val.getType()==AT_ABSOLUTEX) {
            .byte $fc, <val.getValue(), >val.getValue()
        }
    }
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Asupercpu_jsr](https://codebase.c64.org/doku.php?id=base%3Asupercpu_jsr)*

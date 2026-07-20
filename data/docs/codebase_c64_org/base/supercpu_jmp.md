---
title: JMP
source_url: https://codebase.c64.org/doku.php?id=base%3Asupercpu_jmp
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
scraped_at: '2026-07-20'
---

# JMP

base:supercpu_jmp

                # JMP

```
    /*-------------------------------------------------------------------------
    OP CODE: JMP (JuMP)
    ===================
    
    Addressing Modes:
        Absolute                         ($4c - 3 bytes, 3 cycles)
        Absolute Indirect                ($6c - 3 bytes, 5 cycles¹²)
        Absolute Indexed Indirect        ($7c - 3 bytes, 6 cycles)
        Absolute Long                    ($5c - 4 bytes, 4 cycles)
        Absolute Indirect Long           ($dc - 3 bytes, 6 cycles)
        ¹ - Add 1 cycle if 65C02
        ² - 6502: If low byte of addr is $FF (i.e., addr is $xxFF): yields
            incorrect result
    Flags Affected:
        N/A
    Description:
        Transfer control to the address specified by the operand field.
        The program counter is loaded with the target address. If a long JMP is
        executed, the program counter bank is loaded from the third byte of the
        target address specified by the operand.
    Notes:
    -------------------------------------------------------------------------*/
    .pseudocommand jmp val {
        .if (val.getType()==AT_ABSOLUTE) {
            .if (val.getValue()<$10000) {
                .byte $4c, <val.getValue(), >val.getValue()
            } else {
                .byte $5c, <val.getValue(), >val.getValue(), val.getValue() >> 16
            }
        }
        .if (val.getType()==AT_INDIRECT) {
            .byte $6c, <val.getValue(), >val.getValue()
        }
        .if (val.getType()==AT_IZEROPAGEX) {
            .byte $7c, <val.getValue(), >val.getValue()
        }
    }
    .pseudocommand jmp_l val {
        .if (val.getType()==AT_INDIRECT) {
            .byte $dc, <val.getValue(), >val.getValue()
        }
    }
```
base/supercpu_jmp.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
/*-------------------------------------------------------------------------
    OP CODE: JMP (JuMP)
    ===================
    
    Addressing Modes:
        Absolute                         ($4c - 3 bytes, 3 cycles)
        Absolute Indirect                ($6c - 3 bytes, 5 cycles¹²)
        Absolute Indexed Indirect        ($7c - 3 bytes, 6 cycles)
        Absolute Long                    ($5c - 4 bytes, 4 cycles)
        Absolute Indirect Long           ($dc - 3 bytes, 6 cycles)
        ¹ - Add 1 cycle if 65C02
        ² - 6502: If low byte of addr is $FF (i.e., addr is $xxFF): yields
            incorrect result

    Flags Affected:
        N/A

    Description:
        Transfer control to the address specified by the operand field.
        The program counter is loaded with the target address. If a long JMP is
        executed, the program counter bank is loaded from the third byte of the
        target address specified by the operand.

    Notes:

    -------------------------------------------------------------------------*/

    .pseudocommand jmp val {
        .if (val.getType()==AT_ABSOLUTE) {
            .if (val.getValue()<$10000) {
                .byte $4c, <val.getValue(), >val.getValue()
            } else {
                .byte $5c, <val.getValue(), >val.getValue(), val.getValue() >> 16
            }
        }
        .if (val.getType()==AT_INDIRECT) {
            .byte $6c, <val.getValue(), >val.getValue()
        }
        .if (val.getType()==AT_IZEROPAGEX) {
            .byte $7c, <val.getValue(), >val.getValue()
        }
    }

    .pseudocommand jmp_l val {
        .if (val.getType()==AT_INDIRECT) {
            .byte $dc, <val.getValue(), >val.getValue()
        }
    }
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Asupercpu_jmp](https://codebase.c64.org/doku.php?id=base%3Asupercpu_jmp)*

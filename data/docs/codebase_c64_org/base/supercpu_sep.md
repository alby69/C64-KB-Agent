---
title: SEP
source_url: https://codebase.c64.org/doku.php?id=base%3Asupercpu_sep
category: reference
topics:
- assembly
difficulty: intermediate
language: assembly
hardware:
- CPU
related: []
scraped_at: '2026-07-14'
---

# SEP

base:supercpu_sep

                # SEP

```
    /*-------------------------------------------------------------------------
    OP CODE: SEP (SEt status bits (P))
    ==================================
    
    Addressing Modes:
        Immediate                        ($e2 - 2 bytes, 3 cycles)
    Flags Affected:
        n - All flags for which an operand bit is set are set to one. All other
            flags are unaffected by the instruction. 65802/65816 emulation e=1
            & 65802/65816 native mode e=0
        v - All flags for which an operand bit is set are set to one. All other
            flags are unaffected by the instruction. 65802/65816 emulation e=1
            & 65802/65816 native mode e=0
        m - All flags for which an operand bit is set are set to one. All other
            flags are unaffected by the instruction. 65802/65816 native mode e=0
        x - All flags for which an operand bit is set are set to one. All other
            flags are unaffected by the instruction. 65802/65816 native mode e=0
        d - All flags for which an operand bit is set are set to one. All other
            flags are unaffected by the instruction. 65802/65816 emulation e=1
            & 65802/65816 native mode e=0
        i - All flags for which an operand bit is set are set to one. All other
            flags are unaffected by the instruction. 65802/65816 emulation e=1
            & 65802/65816 native mode e=0
        z - All flags for which an operand bit is set are set to one. All other
            flags are unaffected by the instruction. 65802/65816 emulation e=1
            & 65802/65816 native mode e=0
        c - All flags for which an operand bit is set are set to one. All other
            flags are unaffected by the instruction. 65802/65816 emulation e=1
            & 65802/65816 native mode e=0
    Description:
        For each one-bit in the operand byte, set the corresponding bit in the
        status register to one. For example, if bit three is set in the operand
        byte, bit three in the status register (the decimal flag) is set to one
        by this instruction. Zeroes in the operand byte cause no change to
        their corresponding status register bits.
        This instruction lets you set any flag or flags in the status register
        with a single two-byte instruction. Furthermore, it is the only direct
        means of setting the m and x mode select flags. (Instructions that pull
        the P status register indirectly affect the m and x mode select flags).
        6502 emulation mode (65802/65816, e=1): Neither the break flag nor bit
        five (the 6502’s non-flag bit) is affected by SEP.
    Notes:
    -------------------------------------------------------------------------*/
    .pseudocommand sep val {
        .byte $e2,val.getValue()
    }
```
base/supercpu_sep.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
/*-------------------------------------------------------------------------
    OP CODE: SEP (SEt status bits (P))
    ==================================
    
    Addressing Modes:
        Immediate                        ($e2 - 2 bytes, 3 cycles)

    Flags Affected:
        n - All flags for which an operand bit is set are set to one. All other
            flags are unaffected by the instruction. 65802/65816 emulation e=1
            & 65802/65816 native mode e=0
        v - All flags for which an operand bit is set are set to one. All other
            flags are unaffected by the instruction. 65802/65816 emulation e=1
            & 65802/65816 native mode e=0
        m - All flags for which an operand bit is set are set to one. All other
            flags are unaffected by the instruction. 65802/65816 native mode e=0
        x - All flags for which an operand bit is set are set to one. All other
            flags are unaffected by the instruction. 65802/65816 native mode e=0
        d - All flags for which an operand bit is set are set to one. All other
            flags are unaffected by the instruction. 65802/65816 emulation e=1
            & 65802/65816 native mode e=0
        i - All flags for which an operand bit is set are set to one. All other
            flags are unaffected by the instruction. 65802/65816 emulation e=1
            & 65802/65816 native mode e=0
        z - All flags for which an operand bit is set are set to one. All other
            flags are unaffected by the instruction. 65802/65816 emulation e=1
            & 65802/65816 native mode e=0
        c - All flags for which an operand bit is set are set to one. All other
            flags are unaffected by the instruction. 65802/65816 emulation e=1
            & 65802/65816 native mode e=0

    Description:
        For each one-bit in the operand byte, set the corresponding bit in the
        status register to one. For example, if bit three is set in the operand
        byte, bit three in the status register (the decimal flag) is set to one
        by this instruction. Zeroes in the operand byte cause no change to
        their corresponding status register bits.

        This instruction lets you set any flag or flags in the status register
        with a single two-byte instruction. Furthermore, it is the only direct
        means of setting the m and x mode select flags. (Instructions that pull
        the P status register indirectly affect the m and x mode select flags).

        6502 emulation mode (65802/65816, e=1): Neither the break flag nor bit
        five (the 6502’s non-flag bit) is affected by SEP.

    Notes:

    -------------------------------------------------------------------------*/

    .pseudocommand sep val {
        .byte $e2,val.getValue()
    }
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Asupercpu_sep](https://codebase.c64.org/doku.php?id=base%3Asupercpu_sep)*

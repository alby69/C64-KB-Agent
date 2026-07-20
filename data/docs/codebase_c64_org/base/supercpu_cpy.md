---
title: CPY
source_url: https://codebase.c64.org/doku.php?id=base%3Asupercpu_cpy
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

# CPY

base:supercpu_cpy

                # CPY

```
    //---------------------------------------------------------------------------------------------
    // PseudoCommand-OPC: CPY (ComPare index Register Y with memory)
    //
    // Addressing Modes:
    //   Immediate                               ($c0 - 2 bytes*, 2 cycles¹)
    //   Absolute                                ($cc - 3 bytes, 4 cycles¹)
    //   Direct Page (also DP)                   ($c4 - 2 bytes, 3 cycles¹²)
    //   * - Add 1 byte if x = 0 (16-bit index registers)
    //   ¹ - Add 1 cycle if x = 0 (16-bit index registers)
    //   ² - Add 1 cycle if low byte of Direct Page register is other than zero (DL< >0)
    //
    // Flags Affected:
    //   n - Set if most significant bit of result is set; else cleared.
    //   z - Set if result is zero; else cleared.
    //   c - Set if no borrow required (Y register value higher or same);
    //       cleared if borrow required (Y register value lower).
    //
    // Description:
    //   Subtract the data located at the effective address specified by the operand from the
    //   contents of the Y register, setting the carry, zero, and negative flags based on the
    //   result, but without altering the contents of either the memory location or the register.
    //   The result is not saved. The comparison is of unsigned values only (except for signed
    //   comparison for equality).
    //
    //   The primary use for the CPY instruction is to test the value of the Y index register
    //   against loop boundaries, setting the flags so that a conditional branch can be executed.
    //
    //   8-bit index registers (all processors): Data compared is eight-bit.
    //
    //   16-bit index registers (65802/65816 only, Y = 0): Data compared is sixteen-bit:
    //    - the low-order eight bits of the data in memory are located at the effective address;
    //    - the high-order eight bits are located at the effective address plus one.
    //---------------------------------------------------------------------------------------------
    .pseudocommand cpy16 val {
        .if (val.getType()==AT_IMMEDIATE) {
            .byte $c0, <val.getValue(), >val.getValue()
        }
        .if (val.getType()==AT_ABSOLUTE) {
            .if (val.getValue()<256) {
                .byte $c4, <val.getValue()       // Direct Page
            } else {
                .byte $cc, <val.getValue(), >val.getValue()
            }
        }
    }
```
base/supercpu_cpy.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
//---------------------------------------------------------------------------------------------
    // PseudoCommand-OPC: CPY (ComPare index Register Y with memory)
    //
    // Addressing Modes:
    //   Immediate                               ($c0 - 2 bytes*, 2 cycles¹)
    //   Absolute                                ($cc - 3 bytes, 4 cycles¹)
    //   Direct Page (also DP)                   ($c4 - 2 bytes, 3 cycles¹²)
    //   * - Add 1 byte if x = 0 (16-bit index registers)
    //   ¹ - Add 1 cycle if x = 0 (16-bit index registers)
    //   ² - Add 1 cycle if low byte of Direct Page register is other than zero (DL< >0)
    //
    // Flags Affected:
    //   n - Set if most significant bit of result is set; else cleared.
    //   z - Set if result is zero; else cleared.
    //   c - Set if no borrow required (Y register value higher or same);
    //       cleared if borrow required (Y register value lower).
    //
    // Description:
    //   Subtract the data located at the effective address specified by the operand from the
    //   contents of the Y register, setting the carry, zero, and negative flags based on the
    //   result, but without altering the contents of either the memory location or the register.
    //   The result is not saved. The comparison is of unsigned values only (except for signed
    //   comparison for equality).
    //
    //   The primary use for the CPY instruction is to test the value of the Y index register
    //   against loop boundaries, setting the flags so that a conditional branch can be executed.
    //
    //   8-bit index registers (all processors): Data compared is eight-bit.
    //
    //   16-bit index registers (65802/65816 only, Y = 0): Data compared is sixteen-bit:
    //    - the low-order eight bits of the data in memory are located at the effective address;
    //    - the high-order eight bits are located at the effective address plus one.
    //---------------------------------------------------------------------------------------------

    .pseudocommand cpy16 val {
        .if (val.getType()==AT_IMMEDIATE) {
            .byte $c0, <val.getValue(), >val.getValue()
        }
        .if (val.getType()==AT_ABSOLUTE) {
            .if (val.getValue()<256) {
                .byte $c4, <val.getValue()       // Direct Page
            } else {
                .byte $cc, <val.getValue(), >val.getValue()
            }
        }
    }
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Asupercpu_cpy](https://codebase.c64.org/doku.php?id=base%3Asupercpu_cpy)*

---
title: Different CPU types
source_url: https://codebase.c64.org/doku.php?id=base%3Adifferent_cpu_types
category: manual
topics: []
difficulty: advanced
language: basic
hardware:
- CPU
related: []
scraped_at: '2026-07-14'
---

# Different CPU types

base:different_cpu_types

                # Different CPU types

The Rockwell data booklet 29651N52 (technical information about R65C00 microprocessors, dated October 1984), lists the following differences between NMOS R6502 microprocessor and CMOS R65C00 family:

```
 1. Indexed addressing across page boundary.
        NMOS: Extra read of invalid address.
        CMOS: Extra read of last instruction byte.
 2. Execution of invalid op codes.
        NMOS: Some terminate only by reset. Results are undefined.
        CMOS: All are NOPs (reserved for future use).
 3. Jump indirect, operand = XXFF.
        NMOS: Page address does not increment.
        CMOS: Page address increments and adds one additional cycle.
 4. Read/modify/write instructions at effective address.
        NMOS: One read and two write cycles.
        CMOS: Two read and one write cycle.
 5. Decimal flag.
        NMOS: Indeterminate after reset.
        CMOS: Initialized to binary mode (D=0) after reset and interrupts.
 6. Flags after decimal operation.
        NMOS: Invalid N, V and Z flags.
        CMOS: Valid flag adds one additional cycle.
 7. Interrupt after fetch of BRK instruction.
        NMOS: Interrupt vector is loaded, BRK vector is ignored.
        CMOS: BRK is executed, then interrupt is executed.
```
base/different_cpu_types.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
1. Indexed addressing across page boundary.
        NMOS: Extra read of invalid address.
        CMOS: Extra read of last instruction byte.

 2. Execution of invalid op codes.
        NMOS: Some terminate only by reset. Results are undefined.
        CMOS: All are NOPs (reserved for future use).

 3. Jump indirect, operand = XXFF.
        NMOS: Page address does not increment.
        CMOS: Page address increments and adds one additional cycle.

 4. Read/modify/write instructions at effective address.
        NMOS: One read and two write cycles.
        CMOS: Two read and one write cycle.

 5. Decimal flag.
        NMOS: Indeterminate after reset.
        CMOS: Initialized to binary mode (D=0) after reset and interrupts.

 6. Flags after decimal operation.
        NMOS: Invalid N, V and Z flags.
        CMOS: Valid flag adds one additional cycle.

 7. Interrupt after fetch of BRK instruction.
        NMOS: Interrupt vector is loaded, BRK vector is ignored.
        CMOS: BRK is executed, then interrupt is executed.
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Adifferent_cpu_types](https://codebase.c64.org/doku.php?id=base%3Adifferent_cpu_types)*

---
title: TXY
source_url: https://codebase.c64.org/doku.php?id=base%3Asupercpu_txy
category: reference
topics: []
difficulty: intermediate
language: none
hardware:
- CPU
related: []
scraped_at: '2026-07-14'
---

# TXY

base:supercpu_txy

                # TXY

```
    /*-------------------------------------------------------------------------
    OP CODE: TXY (Transfer index register X to Y)
    =============================================
    
    Addressing Modes:
        Implied                            ($9b - 1 byte, 2 cycles)
    Flags Affected:
        n - Set if most significant bit of transferred value is set; else
            cleared.
        z - Set if value transferred is zero; else cleared.
    Description:
        Transfer the value in index register X to index register Y. The value
        in index register X is not changed by the operation. Note that the two
        registers are never different sizes.
        8-bit index registers (x=1): Value transferred is eight-bit.
        16-bit index registers (x=0): Value transferred is sixteen-bit.
    Notes:
    -------------------------------------------------------------------------*/
    .pseudocommand txy {
        .byte $9b
    }
```
base/supercpu_txy.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
/*-------------------------------------------------------------------------
    OP CODE: TXY (Transfer index register X to Y)
    =============================================
    
    Addressing Modes:
        Implied                            ($9b - 1 byte, 2 cycles)

    Flags Affected:
        n - Set if most significant bit of transferred value is set; else
            cleared.
        z - Set if value transferred is zero; else cleared.

    Description:
        Transfer the value in index register X to index register Y. The value
        in index register X is not changed by the operation. Note that the two
        registers are never different sizes.

        8-bit index registers (x=1): Value transferred is eight-bit.
        16-bit index registers (x=0): Value transferred is sixteen-bit.

    Notes:

    -------------------------------------------------------------------------*/

    .pseudocommand txy {
        .byte $9b
    }
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Asupercpu_txy](https://codebase.c64.org/doku.php?id=base%3Asupercpu_txy)*

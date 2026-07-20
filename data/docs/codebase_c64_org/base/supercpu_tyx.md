---
title: TYX
source_url: https://codebase.c64.org/doku.php?id=base%3Asupercpu_tyx
category: reference
topics: []
difficulty: intermediate
language: none
hardware:
- CPU
related: []
scraped_at: '2026-07-20'
---

# TYX

base:supercpu_tyx

                # TYX

```
    /*-------------------------------------------------------------------------
    OP CODE: TYX (Transfer index register Y to X)
    =============================================
    
    Addressing Modes:
        Implied                            ($bb - 1 byte, 2 cycles)
    Flags Affected:
        n - Set if most significant bit of transferred value is set; else
            cleared.
        z - Set if value transferred is zero; else cleared.
    Description:
        Transfer the value in index register Y to index register X. The value
        in index register Y is not changed by the operation. Note that the two
        registers are never different sizes.
        8-bit index registers (x=1): Value transferred is eight-bit.
        16-bit index registers (x=0): Value transferred is sixteen-bit.
    Notes:
    -------------------------------------------------------------------------*/
    .pseudocommand tyx {
        .byte $bb
    }
```
base/supercpu_tyx.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
/*-------------------------------------------------------------------------
    OP CODE: TYX (Transfer index register Y to X)
    =============================================
    
    Addressing Modes:
        Implied                            ($bb - 1 byte, 2 cycles)

    Flags Affected:
        n - Set if most significant bit of transferred value is set; else
            cleared.
        z - Set if value transferred is zero; else cleared.

    Description:
        Transfer the value in index register Y to index register X. The value
        in index register Y is not changed by the operation. Note that the two
        registers are never different sizes.

        8-bit index registers (x=1): Value transferred is eight-bit.
        16-bit index registers (x=0): Value transferred is sixteen-bit.

    Notes:

    -------------------------------------------------------------------------*/

    .pseudocommand tyx {
        .byte $bb
    }
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Asupercpu_tyx](https://codebase.c64.org/doku.php?id=base%3Asupercpu_tyx)*

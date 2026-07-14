---
title: 32 bit Galois LFSR random generator
source_url: https://codebase.c64.org/doku.php?id=base%3A32bit_galois_lfsr
category: reference
topics:
- assembly
difficulty: intermediate
language: assembly
hardware: []
related: []
scraped_at: '2026-07-14'
---

# 32 bit Galois LFSR random generator

base:32bit_galois_lfsr

                # 32 bit Galois LFSR random generator

A fast random generator based on the CRC32 algorythm.

It uses the CRC32 IEEE 802.3 polynom $04C11DB7 which produces a random number period of 2^32-1 (4.3 billion) numbers.

```
rnd:
        ASL random
        ROL random+1
        ROL random+2
        ROL random+3
        BCC .nofeedback
        LDA random
        EOR #$B7
        STA random
        LDA random+1
        EOR #$1D
        STA random+1
        LDA random+2
        EOR #$C1
        STA random+2
        LDA random+3
        EOR #$04
        STA random+3
.nofeedback:
        RTS
random: .BYTE $FF,$FF,$FF,$FF
```
base/32bit_galois_lfsr.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`rnd`** (unknown): No description available
- **`random`** (unknown): No description available

```assembly
rnd:
        ASL random
        ROL random+1
        ROL random+2
        ROL random+3
        BCC .nofeedback
        LDA random
        EOR #$B7
        STA random
        LDA random+1
        EOR #$1D
        STA random+1
        LDA random+2
        EOR #$C1
        STA random+2
        LDA random+3
        EOR #$04
        STA random+3
.nofeedback:
        RTS

random: .BYTE $FF,$FF,$FF,$FF
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3A32bit_galois_lfsr](https://codebase.c64.org/doku.php?id=base%3A32bit_galois_lfsr)*

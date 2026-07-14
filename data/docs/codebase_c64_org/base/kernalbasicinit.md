---
title: Initialization of Kernal and Basic system variables
source_url: https://codebase.c64.org/doku.php?id=base%3Akernalbasicinit
category: reference
topics:
- basic
- assembly
difficulty: intermediate
language: mixed
hardware:
- SID
- KERNAL
- CPU
related:
- sound-programming
- memory-map
- sid-registers
- music-player
- kernal-routines
scraped_at: '2026-07-14'
---

# Initialization of Kernal and Basic system variables

base:kernalbasicinit

                # Initialization of Kernal and Basic system variables

The following code does a software reset.

```
systeminit
    SEI
    CLD
    LDX #$FF
    TXS
    JSR $FF84    ; IOINIT - Initialize I/O
    ; Initialize SID registers (not done by Kernal reset routine):
    LDX #$17
    LDA #$00
lp1 STA $D400,X
    DEX
    BPL lp1
    ; RAMTAS (JSR $FF87) - Initialize System Constants
    ; $FF87 is not actually called because it would do
    ; a RAM-test which lasts a few seconds.
    ; The following code does the same as RAMTAS but
    ; without the RAM-test:
    LDA #$00
    TAY
lp2 STA $0002,Y
    STA $0200,Y
    STA $0300,Y
    INY
    BNE lp2
    LDX #$00
    LDY #$A0
    JSR $FD8C
    JSR $FF8A    ; RESTOR - Restore Kernal Vectors
    JSR $FF81    ; CINT - Initialize screen editor
    CLI
    ; Basic initializations (optional):
    JSR $E453    ; Initialize Vectors
    JSR $E3BF    ; Initialize BASIC RAM
    JSR $E422    ; Output Power-Up Message
    LDX #$FB
    TXS
```
base/kernalbasicinit.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`lp1`** (unknown): Initialize SID registers (not done by Kernal reset routine):
- **`lp2`** (unknown): The following code does the same as RAMTAS but without the RAM-test:

```assembly
systeminit
    SEI
    CLD
    LDX #$FF
    TXS
    JSR $FF84    ; IOINIT - Initialize I/O

    ; Initialize SID registers (not done by Kernal reset routine):

    LDX #$17
    LDA #$00
lp1 STA $D400,X
    DEX
    BPL lp1

    ; RAMTAS (JSR $FF87) - Initialize System Constants

    ; $FF87 is not actually called because it would do
    ; a RAM-test which lasts a few seconds.
    ; The following code does the same as RAMTAS but
    ; without the RAM-test:

    LDA #$00
    TAY
lp2 STA $0002,Y
    STA $0200,Y
    STA $0300,Y
    INY
    BNE lp2

    LDX #$00
    LDY #$A0
    JSR $FD8C

    JSR $FF8A    ; RESTOR - Restore Kernal Vectors
    JSR $FF81    ; CINT - Initialize screen editor
    CLI

    ; Basic initializations (optional):

    JSR $E453    ; Initialize Vectors
    JSR $E3BF    ; Initialize BASIC RAM
    JSR $E422    ; Output Power-Up Message
    LDX #$FB
    TXS
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Akernalbasicinit](https://codebase.c64.org/doku.php?id=base%3Akernalbasicinit)*

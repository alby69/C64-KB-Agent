---
title: Running a Basic program from Assembler
source_url: https://codebase.c64.org/doku.php?id=base%3Arunbasicprg
category: tool
topics:
- basic
- sprite programming
- assembly
difficulty: intermediate
language: assembly
hardware:
- KERNAL
- BASIC ROM
related:
- sprite-programming
- memory-map
- raster-interrupts
- kernal-routines
- vic-ii-registers
scraped_at: '2026-07-14'
---

# Running a Basic program from Assembler

base:runbasicprg

                # Running a Basic program from Assembler

Sometimes it is neccessary to run a Basic program from assembler code. To do this, it's a good idea to do a full [Kernal/Basic initialization](https://codebase.c64.org/doku.php?id=base:kernalbasicinit) before.

```
PRGEND = $1234    ; end of the Basic program
    LDA #<PRGEND
    STA $2D
    STA $AE
    LDA #>PRGEND
    STA $2E
    STA $AF
    JSR $A659    ; Reset execute pointer and do CLR
    JSR $A533    ; Rechain Lines
    JMP $A7AE    ; Basic Warm Start
```
base/runbasicprg.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
PRGEND = $1234    ; end of the Basic program

    LDA #<PRGEND
    STA $2D
    STA $AE
    LDA #>PRGEND
    STA $2E
    STA $AF

    JSR $A659    ; Reset execute pointer and do CLR
    JSR $A533    ; Rechain Lines
    JMP $A7AE    ; Basic Warm Start
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Arunbasicprg](https://codebase.c64.org/doku.php?id=base%3Arunbasicprg)*

---
title: Delay
source_url: https://codebase.c64.org/doku.php?id=base%3Adelay
category: tool
topics:
- raster interrupts
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

# Delay

base:delay

                # Delay

by Zed Yago

When stabilizing a IRQ, you often need a subroutine or macro which can delay a given amount of cycles.

```
delay:            ;delay 84-accu cycles, 0<=accu<=65
  lsr             ;2 cycles akku=akku/2 carry=1 if accu was odd, 0 otherwise
  bcc waste1cycle ;2/3 cycles, depending on lowest bit, same operation for both
waste1cycle:
  sta smod+1      ;4 cycles selfmodifies the argument of branch
  clc             ;2 cycles 
;now we have burned 10/11 cycles.. and jumping into a nopfield 
smod:
  bcc *+10        ;3 cycles
  .buf 32 $EA     ;just type 32x nop if your assembler doesnt support this command
                  ;  or type "!fill 32, $ea" if you are using ACME
  rts             ;6 cycles
```
base/delay.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
delay:            ;delay 84-accu cycles, 0<=accu<=65
  lsr             ;2 cycles akku=akku/2 carry=1 if accu was odd, 0 otherwise
  bcc waste1cycle ;2/3 cycles, depending on lowest bit, same operation for both
waste1cycle:
  sta smod+1      ;4 cycles selfmodifies the argument of branch
  clc             ;2 cycles 
;now we have burned 10/11 cycles.. and jumping into a nopfield 
smod:
  bcc *+10        ;3 cycles
  .buf 32 $EA     ;just type 32x nop if your assembler doesnt support this command
                  ;  or type "!fill 32, $ea" if you are using ACME
  rts             ;6 cycles
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Adelay](https://codebase.c64.org/doku.php?id=base%3Adelay)*

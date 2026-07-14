---
title: Protecting against soft-resets
source_url: https://codebase.c64.org/doku.php?id=base%3Aprotecting_against_soft-resets
category: reference
topics:
- basic
- assembly
difficulty: intermediate
language: mixed
hardware:
- VIC-II
- KERNAL
related:
- sprite-programming
- memory-map
- raster-interrupts
- kernal-routines
- vic-ii-registers
scraped_at: '2026-07-14'
---


# Protecting against soft-resets

base:protecting_against_soft-resets

                # Protecting against soft-resets

When the C64 gets a soft-reset signal, the first thing it does is check for an EPROM at $8000 (kernal routine [$FD02](http://unusedino.de/ec64/technical/aay/c64/romfd02.htm)). We can take advantage of this routine to redirect resets to our own code.

* = $0900 sei lda #$c3 ;the string "CBM80" at $8004 is used to check 8-ROM sta $8004 lda #$c2 sta $8005 lda #$cd sta $8006 lda #$38 sta $8007 lda #$30 sta $8008 lda #<reset ;redirect the vector at $8000 to our own code sta $8000 lda #>reset sta $8001 main inc $d020 ;just something to look at jmp *-3 reset lda #$2f ;reset data-direction register, otherwise the system won't start correctly sta $00 jsr $e5a8 ;optional, refresh the VIC jmp main ;go back to main code

Now try soft-resetting. Instead of going back to the basic screen, instead you'll see the inc $d020 effect.

Note that if you're using the kernal NMI routine ([$FE47](http://unusedino.de/ec64/technical/aay/c64/romfe43.htm)), also redirect the vector at $8002.

base/protecting_against_soft-resets.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
* = $0900
  sei
  lda #$c3 ;the string "CBM80" at $8004 is used to check 8-ROM
  sta $8004
  lda #$c2
  sta $8005
  lda #$cd
  sta $8006
  lda #$38
  sta $8007
  lda #$30
  sta $8008
  lda #<reset ;redirect the vector at $8000 to our own code
  sta $8000
  lda #>reset
  sta $8001
main
  inc $d020 ;just something to look at
  jmp *-3

reset
  lda #$2f ;reset data-direction register, otherwise the system won't start correctly
  sta $00
  jsr $e5a8 ;optional, refresh the VIC
  jmp main ;go back to main code
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Aprotecting_against_soft-resets](https://codebase.c64.org/doku.php?id=base%3Aprotecting_against_soft-resets)*


### Collegamenti e Riferimenti Hardware
- **$D020 (Border Color)**: Associato al chip VIC-II. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#d020).

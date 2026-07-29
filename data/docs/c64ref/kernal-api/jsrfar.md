---
title: ''
source_url: https://github.com/mist64/c64ref/blob/main/src/kernal/machine_language_routines.txt
category: reference
topics:
- kernal-api
- system-routines
- jumps
difficulty: intermediate
language: assembly
hardware:
- C64
related: []
scraped_at: '2026-07-29'
c64ref:
  module: kernal
  source_files:
  - machine_language_routines.txt
  address: $FF6E
  symbol: JSRFAR
  sources:
  - name: Machine Language Routines
    author: Todd D Heimarck
    description: outine jumps to a subroutine in a specified bank and re-
---

# JSRFAR —  ($FF6E)

## Panoramica
La routine KERNAL `JSRFAR` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF6E`
- **Chiamata**: `JSR JSRFAR` o `SYS 65390`


## Note per Fonte

### Machine Language Routines (Todd D Heimarck)
outine jumps to a subroutine in a specified bank and re-
to the calling routine in bank 15. Prior to calling this
e, you must store the bank number (0-15) of the target
e in location 2 and the address of the target routine in
ons 3-4 (in high-byte/low-byte order, opposite from the
arrangement). Load location 5 with the value you want
 in the status register when the target routine is called.
ehavior of many operating system routines is influenced
 status-register setting, particularly the state of the carry
oad 5 with the value 0 to clear carry, or with 1 to set
) To pass other register values to the routine you will be
g, store the desired accumulator value in location 6, the
for .X in 7, and the value for .Y in 8. Upon return, loca-
 will hold the status-register value at the time of exit, 6
old the accumulator value, 7 will hold the .X value, 8
old the .Y value, and 9 will hold the stack-pointer value.
stem is always configured for bank 15 upon exit.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
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
  address: $FF74
  symbol: INDFET
  sources:
  - name: Machine Language Routines
    author: Todd D Heimarck
    description: outine reads the contents of a location in a specified
---

# INDFET —  ($FF74)

## Panoramica
La routine KERNAL `INDFET` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF74`
- **Chiamata**: `JSR INDFET` o `SYS 65396`


## Note per Fonte

### Machine Language Routines (Todd D Heimarck)
outine reads the contents of a location in a specified
Prior to calling this routine; you must load a two-byte
age pointer with the address of the location to be read
th the base location if a series of bytes is to be read).

he routine with the accumulator holding the address
 zero-page pointer, .X holding the bank number (0-15)
e target location, and .Y holding an offset value which
e added to the address in the pointer. (Load .Y with 0 if
set is desired.) Upon return, the accumulator will hold
te from the specified address. The value in .Y is not
d.

d from a series of locations, it is necessary to reload
cumulator and .X values before every call to this routine,
u can read up to 256 sequential locations without
ng the address in the zero-page pointer by incrementing
ween calls.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
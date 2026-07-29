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
  address: $FF59
  symbol: LKUPLA
  sources:
  - name: Machine Language Routines
    author: Todd D Heimarck
    description: outine checks whether a specified logical file number is
---

# LKUPLA —  ($FF59)

## Panoramica
La routine KERNAL `LKUPLA` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF59`
- **Chiamata**: `JSR LKUPLA` o `SYS 65369`


## Note per Fonte

### Machine Language Routines (Todd D Heimarck)
outine checks whether a specified logical file number is
tly used. Call the routine with the accumulator holding
gical-file-number value in question. If that file number is
ble, the carry bit will be set upon return. (The logical file
 will still be in the accumulator.) However, if the num-
 used for a currently open file, then the carry bit will be
upon return, the accumulator will still hold the logical
umber, .X will hold the corresponding device number,
 will hold the corresponding secondary address.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
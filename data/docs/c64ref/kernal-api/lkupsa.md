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
  address: $FF5C
  symbol: LKUPSA
  sources:
  - name: Machine Language Routines
    author: Todd D Heimarck
    description: outine checks whether a specified secondary address is
---

# LKUPSA —  ($FF5C)

## Panoramica
La routine KERNAL `LKUPSA` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF5C`
- **Chiamata**: `JSR LKUPSA` o `SYS 65372`


## Note per Fonte

### Machine Language Routines (Todd D Heimarck)
outine checks whether a specified secondary address is
tly in use. Call the routine with .Y holding the secondary-
s value in question. If that secondary address is not
tly used, the status-register carry bit will be set upon re-
(The secondary-address value will still be in .Y.) How-
ii the number is used for a currently open file, the carry
ll be clear upon return, .Y will still hold the secondary
s, the accumulator will hold the associated logical file
, and .X will hold the corresponding device number.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
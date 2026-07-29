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
  address: $FF68
  symbol: SETBNK
  sources:
  - name: Machine Language Routines
    author: Todd D Heimarck
    description: ernal routine establishes the current memory bank from
---

# SETBNK —  ($FF68)

## Panoramica
La routine KERNAL `SETBNK` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF68`
- **Chiamata**: `JSR SETBNK` o `SYS 65384`


## Note per Fonte

### Machine Language Routines (Todd D Heimarck)
ernal routine establishes the current memory bank from
data will be read or to which data will be written dur-
ad/save operations, as well as the bank where the file-
or the I/O operations can be found. Call the routine
he accumulator holding the bank number for data and
ding the bank for the filename. All registers (.A, .X, and
e preserved during this routine.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
---
title: ODE
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
  address: $FF4D
  sources:
  - name: Machine Language Routines
    author: Todd D Heimarck
    description: s the equivalent of the BASIC command GO 64. It per-
---

# $FF4D — ODE ($FF4D)

## Panoramica
La routine KERNAL `None` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF4D`
- **Chiamata**: `JSR None` o `SYS 65357`


## Note per Fonte

### Machine Language Routines (Todd D Heimarck)
s the equivalent of the BASIC command GO 64. It per-
an immediate cold start of 64 mode. To get back to 128
it is necessary to reset the computer, or to tum it off
ck on.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
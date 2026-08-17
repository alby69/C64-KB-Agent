---
title: PFKEY
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
related:
- pfkey
scraped_at: '2026-07-29'
c64ref:
  module: kernal
  source_files:
  - machine_language_routines.txt
  address: $FF65
  symbol: PFKEY
  sources:
  - name: Machine Language Routines
    author: Todd D Heimarck
    description: ou turn on the 128, its function keys are predefined.
---


# PFKEY —  ($FF65)

## Panoramica
La routine KERNAL `PFKEY` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF65`
- **Chiamata**: `JSR PFKEY` o `SYS 65381`


## Note per Fonte

### Machine Language Routines (Todd D Heimarck)
ou turn on the 128, its function keys are predefined.
ng F3 prints DIRECTORY, F7 holds the LIST command,
 on. The PFKEY Kernal routine assigns a new definition
 of the 10 programmable function keys (F1-F8, SHIFT-
OP, and HELP).

he routine with the accumulator holding the address
hree-byte zero-page string descriptor, .X holding the key
 (1-10), and .Y holding the length of the new defi-
 string. The first two bytes of the descriptor in zero page
 contain the address of the definition string (in the
low-byte/high-byte order); the final byte should hold
nk number where the definition string is located. PFKEY
t check the key number for validity; a value outside the
able range may garble existing definitions. Upon return,
rry bit will be clear if the new definition was success-
added, or set if there was insufficient room in the defi-
 table for the new definition.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
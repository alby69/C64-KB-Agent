---
title: JMPFAR
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
  address: $FF71
  symbol: JMPFAR
  sources:
  - name: Machine Language Routines
    author: Todd D Heimarck
    description: jumps to a routine in a specified bank, with no return
---


# JMPFAR —  ($FF71)

## Panoramica
La routine KERNAL `JMPFAR` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF71`
- **Chiamata**: `JSR JMPFAR` o `SYS 65393`


## Note per Fonte

### Machine Language Routines (Todd D Heimarck)
jumps to a routine in a specified bank, with no return
 calling bank. Prior to calling this routine, you must store
nk number (0-15) of the target routine in location 2 and
dress of the target routine in locations 3-4 in high-
ow-byte order, opposite from the usual arrangement.
ocation 5 with the value you want placed in the status
er when the target routine is entered. (The behavior of
perating-system routines is influenced by the status-
er setting, particularly the state of the carry bit. Load 5
he value 0 to clear carry or with 1 to set carry.) To pass
register values, store the desired accumulator value in
on 6, the value for .X in 7, and the value for .Y in 8.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
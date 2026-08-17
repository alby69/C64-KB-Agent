---
title: INDCMP
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
  address: $FF7A
  symbol: INDCMP
  sources:
  - name: Machine Language Routines
    author: Todd D Heimarck
    description: outine compares .A to the number held in a memory
---


# INDCMP —  ($FF7A)

## Panoramica
La routine KERNAL `INDCMP` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF7A`
- **Chiamata**: `JSR INDCMP` o `SYS 65402`


## Note per Fonte

### Machine Language Routines (Todd D Heimarck)
outine compares .A to the number held in a memory
on in a specified bank. In preparing to call EMDCMP,
 two-byte zero-page pointer with the address of the
on with which the accumulator is to be compared (or
he base location if a series of bytes is to be compared),
tore the address of this pointer in location $02C8. Call
utine with the accumulator holding the byte to be com-
 .X holding the bank number (0-15) for the target loca-
and .Y holding an offset value which will be added to
dress in the pointer. (Load .Y with 0 if no offset is de-
) Upon return, the accumulator will still hold the byte
 and the status-register N, Z, and C (carry) bits will re-
the result of the comparison. The value in .Y will also be
ved, but it is necessary to reload .X with the bank num-
fore every call to this routine. You can compare up to
quential locations without changing the address in the
age pointer by simply incrementing .Y between calls.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
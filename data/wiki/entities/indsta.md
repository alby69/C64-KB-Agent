---
id: indsta
type: entity
title: INDSTA
aliases:
- INDSTA
tags:
- jumps
- system-routines
- kernal-api
sources:
- path: data/docs/c64ref/kernal-api/indsta.md
  sha256: 6e19093ff7ee7819c1d3b709bbfe4d25eaae187048c658e0a0b23a8fd298870b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-indsta
---

# INDSTA




# INDSTA —  ($FF77)

## Panoramica
La routine KERNAL `INDSTA` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF77`
- **Chiamata**: `JSR INDSTA` o `SYS 65399`


## Note per Fonte

### Machine Language Routines (Todd D Heimarck)
outine stores a value at an address in a specified bank.
 calling the routine, you must load a two-byte zero-page
r with the address of the location at which the byte is to
red (or with the base location if a series of bytes is to be
), and then store the address of this pointer in location
 Call the routine with the accumulator holding the byte
stored, .X holding the bank number (0-15) for the target
on, and .Y holding an offset value which will be added
 address in the pointer. (Load Y with 0 if no offset is de-
) Upon return, the accumulator will still hold the byte
 .Y is also preserved. To write to a series of locations,
st reload .X with the bank number before every call,
u can write to up to 256 sequential locations without
ng the address in the zero-page pointer by simply in-
ting .Y between calls.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-indsta]]

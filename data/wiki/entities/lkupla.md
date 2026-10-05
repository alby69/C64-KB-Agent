---
id: lkupla
type: entity
title: LKUPLA
aliases:
- LKUPLA
tags:
- jumps
- system-routines
- kernal-api
sources:
- path: data/docs/c64ref/kernal-api/lkupla.md
  sha256: ca7d54a845131b5f32704cd052531406cb84cf573474d48302c17865863be585
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-lkupla
---

# LKUPLA




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

## References
- Source: [[src-lkupla]]

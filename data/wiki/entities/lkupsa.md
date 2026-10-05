---
id: lkupsa
type: entity
title: LKUPSA
aliases:
- LKUPSA
tags:
- jumps
- system-routines
- kernal-api
sources:
- path: data/docs/c64ref/kernal-api/lkupsa.md
  sha256: 66de5370d267f67e3351f5dec485f80e996d8b8937c487c452f6c18f594daa33
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-lkupsa
---

# LKUPSA




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

## References
- Source: [[src-lkupsa]]

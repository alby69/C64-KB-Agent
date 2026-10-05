---
id: setbnk
type: entity
title: SETBNK
aliases:
- SETBNK
tags:
- jumps
- system-routines
- kernal-api
sources:
- path: data/docs/c64ref/kernal-api/setbnk.md
  sha256: ee6c5b98055df0f29f624b5edea3ec37837c6f5bc7445bd56d68fe1668ff2ea6
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-setbnk
---

# SETBNK




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

## References
- Source: [[src-setbnk]]

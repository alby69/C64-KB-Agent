---
id: ff4a
type: entity
title: E_ALL
aliases:
- E_ALL
tags:
- jumps
- system-routines
- kernal-api
sources:
- path: data/docs/c64ref/kernal-api/ff4a.md
  sha256: e1971cd5a77da3e333a1c3ea003e53dacb24b7948402cc0e5c90eba388a9a3b6
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-ff4a
---

# E_ALL



# $FF4A — E_ALL ($FF4A)

## Panoramica
La routine KERNAL `None` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF4A`
- **Chiamata**: `JSR None` o `SYS 65354`


## Note per Fonte

### Machine Language Routines (Todd D Heimarck)
outine closes all files currently opened to a specified de-
providing an improved version of CLALL. Enter the rou-
ith the accumulator holding the number of the device
ch files are to be closed. Lf the specified device is the
t input or output device, the input or output channel
e reset to the default device (screen or keyboard). If all
to the device were successfully closed, the status-register
bit w01 clear upon return. A set carry bit indicates that a
 error occurred.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-ff4a]]

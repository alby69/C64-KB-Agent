---
title: E_ALL
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
- clall
scraped_at: '2026-07-29'
c64ref:
  module: kernal
  source_files:
  - machine_language_routines.txt
  address: $FF4A
  sources:
  - name: Machine Language Routines
    author: Todd D Heimarck
    description: outine closes all files currently opened to a specified de-
---

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
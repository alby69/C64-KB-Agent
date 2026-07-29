---
title: ''
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
  address: $FF62
  symbol: DLCHR
  sources:
  - name: Machine Language Routines
    author: Todd D Heimarck
    description: outine copies character shape data for both standard
---

# DLCHR —  ($FF62)

## Panoramica
La routine KERNAL `DLCHR` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF62`
- **Chiamata**: `JSR DLCHR` o `SYS 65378`


## Note per Fonte

### Machine Language Routines (Todd D Heimarck)
outine copies character shape data for both standard
aracter sets into the VDC video chip's private block of
roviding character definitions for the 80-column dis-
(The VDC has no character ROM.) This routine is also
 as part of IOEMFI for the 128.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
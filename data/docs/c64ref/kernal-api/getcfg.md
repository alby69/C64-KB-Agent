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
  address: $FF6B
  symbol: GETCFG
  sources:
  - name: Machine Language Routines
    author: Todd D Heimarck
    description: outine translates a bank number (0-15) into the
---

# GETCFG —  ($FF6B)

## Panoramica
La routine KERNAL `GETCFG` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF6B`
- **Chiamata**: `JSR GETCFG` o `SYS 65387`


## Note per Fonte

### Machine Language Routines (Todd D Heimarck)
outine translates a bank number (0-15) into the
ponding MMU register setting to configure the system
at bank. Call the routine with .X holding the bank num-
pon return, the accumulator will hold the corresponding
nfiguration register value. (.Y is unaffected.) Once you
his value, you can store it into $FF00 to change banks.
put bank number is not checked for validity, and a
 outside the acceptable range will return a meaningless
value.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
---
title: PRIMM
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
- jmp
- jsr
scraped_at: '2026-07-29'
c64ref:
  module: kernal
  source_files:
  - machine_language_routines.txt
  address: $FF7D
  symbol: PRIMM
  sources:
  - name: Machine Language Routines
    author: Todd D Heimarck
    description: outine prints the string of character codes which im-
---


# PRIMM —  ($FF7D)

## Panoramica
La routine KERNAL `PRIMM` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF7D`
- **Chiamata**: `JSR PRIMM` o `SYS 65405`


## Note per Fonte

### Machine Language Routines (Todd D Heimarck)
outine prints the string of character codes which im-
ely follows the JSR to this routine. (You must always
his routine with JSR, never with JMP. Only JSR places the
ed address information on the stack.) The routine contin-
inting bytes as character codes until a byte containing
s encountered. When the ending marker is found, the
e returns to the address immediately following the zero
All registers (.A, .X, and .Y) are preserved during this
e.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
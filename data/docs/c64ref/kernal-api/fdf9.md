---
title: lename Location and Number of Characters FDF9/FE49-FDFF/FE4F
source_url: https://github.com/mist64/c64ref/blob/main/src/kernal/compute!'s_tool_kit:_kernal.txt
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
- ece7-load
- f34a-open
- f5ed-save
- jmp
- setnam
scraped_at: '2026-07-29'
c64ref:
  module: kernal
  source_files:
  - compute!'s_tool_kit:_kernal.txt
  address: $FDF9
  sources:
  - name: 'COMPUTE!''s Tool Kit: Kernal'
    author: Dan Heeb
    description: 'ed by**: JMP from Kernal SETNAM vector at FFBD.'
---

# $FDF9 — lename Location and Number of Characters FDF9/FE49-FDFF/FE4F ($FDF9)

## Panoramica
La routine KERNAL `None` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FDF9`
- **Chiamata**: `JSR None` o `SYS 65017`


## Note per Fonte

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: JMP from Kernal SETNAM vector at FFBD.

cation of the filename is placed in a pointer at (BB),
e number of characters in the filename is placed in B7.

outine sets filename information for later use of the
 routines OPEN, SAVE, and LOAD. If no filename is
 for these routines, load the accumulator with zero
 calling this routine. Flowever, loading or saving to a se-
evice requires that a filename be present.

ation**:

 B7, the number of characters in the filename.
 BB, the low byte of the address of the filename.
 BC, the high byte of the address of the filename.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
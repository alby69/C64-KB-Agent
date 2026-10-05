---
id: fdf9
type: entity
title: lename Location and Number of Characters FDF9/FE49-FDFF/FE4F
aliases:
- lename Location and Number of Characters FDF9/FE49-FDFF/FE4F
tags:
- jumps
- system-routines
- kernal-api
sources:
- path: data/docs/c64ref/kernal-api/fdf9.md
  sha256: 090d50d1ee7073f96b1aad5e54cfa506f4ccfc5bd3506bfd23112a05f763c800
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-fdf9
---

# lename Location and Number of Characters FDF9/FE49-FDFF/FE4F



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

## References
- Source: [[src-fdf9]]

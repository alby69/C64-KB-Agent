---
id: f6dd
type: entity
title: SETTIM Execution F6DD/F760-F6EC/F76F
aliases:
- SETTIM Execution F6DD/F760-F6EC/F76F
tags:
- jumps
- system-routines
- kernal-api
sources:
- path: data/docs/c64ref/kernal-api/f6dd.md
  sha256: 74ff54698588261cdec90e7cf73920b4b5d480f6fa2aa8d5d6eab2b37469b426
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-f6dd
---

# SETTIM Execution F6DD/F760-F6EC/F76F



# $F6DD — SETTIM Execution F6DD/F760-F6EC/F76F ($F6DD)

## Panoramica
La routine KERNAL `None` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$F6DD`
- **Chiamata**: `JSR None` o `SYS 63197`


## Note per Fonte

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: JMP from Kernal RDTIM vector at FFDE; alternate entry at
767 by JMP from Kernal SETTIM vector at FFDB.

he RDTIM entry point, this routine reads the jiffy
at A2-A0 into the accumulator, X register, and Y reg-
 and then falls through to the following routine at
767.

ering at the SETTIM entry point at F6E4/F767, set
ffy clock at A2, A1, and A0 from the accumulator, X reg-
 and Y register.

ation**:

D/F760: SEI to disable interrupts.
 from A2, LDX from A1, and LDY from A0.
4/F767: SEI to disable interrupts (which has no effect if
errupts were already disabled in step 1).
 at A2, STX at A1, and STY at A0.
 to enable interrupts, then RTS.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-f6dd]]

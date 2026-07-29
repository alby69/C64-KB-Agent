---
title: ine Device for SAVE F5ED/F685-F5F9/F691
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
- f5ed-save
- jmp
scraped_at: '2026-07-29'
c64ref:
  module: kernal
  source_files:
  - compute!'s_tool_kit:_kernal.txt
  address: $F5ED
  symbol: Determ
  sources:
  - name: 'COMPUTE!''s Tool Kit: Kernal'
    author: Dan Heeb
    description: 'ed by**: Indirect JMP through (0322) at F5EA/F682 in Jump to SAVE'
---

# Determ — ine Device for SAVE F5ED/F685-F5F9/F691 ($F5ED)

## Panoramica
La routine KERNAL `Determ` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$F5ED`
- **Chiamata**: `JSR Determ` o `SYS 62957`


## Note per Fonte

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: Indirect JMP through (0322) at F5EA/F682 in Jump to SAVE
.

 current device is the keyboard or the screen, load
cumulator with 9 and set the carry bit to display the IL-
DEVICE NUMBER message, then exit.

 current device is either tape (1) or RS-232 (2),
 to Control Routine for Tape Save (which treats RS-232
illegal device).

 current device is a serial device, fall through to the
o Serial Device routine.
ation**:
the current device is the keyboard or the screen, JMP
3/F796 to display the ILLEGAL DEVICE NUMBER er-
 message, set accumulator to 9, set carry, and exit. The
board or the screen is not a valid device for saves.
the current device is RS-232 or tape, branch to
9/F6F1, a routine that determines whether the save is to
232 or tape. If RS-232 is specified, the ILLEGAL DE-
E NUMBER message is displayed. If the device is a tape
ice, the tape save routines are executed.
the device is none of the above, its device number must
>= 4; thus, it's a serial device. Fall through to Save to
ial Device routine at F5FA/F692.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
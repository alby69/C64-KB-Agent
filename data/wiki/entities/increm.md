---
id: increm
type: entity
title: ent realtime clock
aliases:
- ent realtime clock
tags:
- jumps
- system-routines
- kernal-api
sources:
- path: data/docs/c64ref/kernal-api/increm.md
  sha256: 622e1a26f1f33347d7eea9a80cd4f00fcdb733a40118d805a35c66c6436d9dad
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-increm
---

# ent realtime clock



# Increm — ent realtime clock ($FFEA)

## Panoramica
La routine KERNAL `Increm` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FFEA`
- **Chiamata**: `JSR Increm` o `SYS 65514`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: None
aratory routines: None
r returns: None
k requirements: 2
sters affected: A, X

scription**: This routine updates the system clock. Normally this
e is called by the normal KERNAL interrupt routine every 1/60th of
nd. If the user program processes its own interrupts this routine
e called to update the time. In addition, the <STOP> key routine
e called, if the <STOP> key is to remain functional.

 to Use:

l this routine.

MPLE:

### Standard KERNAL Functions (Joe Forster / STA)
–
: –
egisters: A, X.
ddress: $F69B.

### Commented ROM Disassembly (Lee Davison)
outine updates the system clock. Normally this routine is called by the
 KERNAL interrupt routine every 1/60th of a second. If the user program
ses its own interrupts this routine must be called to update the time. Also,
OP key routine must be called if the stop key is to remain functional.

### Cracking The Kernal (Peter Marcotty)
If you are using your own interrupt system, you can update the system clock by calling UDTIM.

pdate the system clock.
   JSR UDTIM
   RTS
t is useful to call UDTIM before calling STOP.

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: JSR at EA31/EABF in IRQ Interrupt Handler.

9B/F734 to update the jiffy clock at A2-A0 and
a value from the keyboard row for column number
three (which contains the STOP key) in 91 if a key in
ow is detected.

ly, this routine is called by the IRQ interrupt han-
64 and VIC) or by the NMI interrupt handler (VIC only).
r, if you run a program with IRQ interrupts disabled,
ould call this routine if you want the jiffy clock in-
ted and the STOP key column value saved in 91.

### C64 KERNAL jump table (Frank Kontros)
- - -  - - -  A X -

### Kernal 64 / 128 (Craig Taylor)
egisters In  : None.
egisters Out : .A,.X destroyed.
emory Changed: Relevant system time locations changed.

### Das neue Commodore-64-intern-Buch (Baloui et al.)
die laufende Zeit um eine gstel Sekunde

### Mapping the Commodore 64 (Sheldon Leemon)
outine is normally called by the IRQ interrupt handler once every sixtieth
econd.  It adds one to the value in the three-byte software
clock at 160-162 ($A0-$A2), and sets the clock back to zero when
ches the 24 hour point.  In addition, it scans the keyboard row
ch the STOP key is located, and stores the current value of that
 location 145 ($91).  This variable is used by the STOP routine
checks for the STOP key.

### Machine Language Routines (Todd D Heimarck)
outine increments the software jiffy dock and scans the
rd column containing the RUN/STOP key. (The 128
n of the routine also decrements a countdown timer.)
outine is normally called every 1 /60 second as part of
andard IRQ service routine.

### Commodore 128 intern (Jörg Schieb et al.)
Routine wird vornehmlich von der IRQ-
e aufgerufen. Es wird die Drei-Byte-24-Stunden-Uhr um
inheit hochgezählt.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-increm]]

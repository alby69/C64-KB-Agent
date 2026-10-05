---
id: ffde
type: entity
title: ealtime clock
aliases:
- ealtime clock
tags:
- jumps
- system-routines
- kernal-api
sources:
- path: data/docs/c64ref/kernal-api/ffde.md
  sha256: 92cfab67909222ac7ea69159601c046ca218c6e337fd4ea1824b6eaca0a2853b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-ffde
---

# ealtime clock



# $FFDE — ealtime clock ($FFDE)

## Panoramica
La routine KERNAL `None` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FFDE`
- **Chiamata**: `JSR None` o `SYS 65502`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: A, X, Y
aratory routines: None
r returns: None
k requirements: 2
sters affected: A, X, Y

scription**: This routine is used to read the system clock. The clock's
tion is a 60th of a second. Three bytes are returned by the
e. The accumulator contains the most significant byte, the X index
er contains the next most significant byte, and the Y index
er contains the least significant byte.

MPLE:

   JSR RDTIM
   STY TIME
   STX TIME+1
   STA TIME+2
   ...
ME *=*+3

### Standard KERNAL Functions (Joe Forster / STA)
–
: A/X/Y = Current TOD value.
egisters: A, X, Y.
ddress: $F6DD.

### Commented ROM Disassembly (Lee Davison)
outine returns the time, in jiffies, in AXY. The accumulator contains the
ignificant byte.

### Cracking The Kernal (Peter Marcotty)
Locations 160-162 are transferred, in order, to the Y and X registers and the accumulator.

tore system clock to screen.
   JSR RDTIM
   STA 1026
   STX 1025
   STY 1024
he system clock can be translated as hours/minutes/ seconds.

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: JSR at AF84/CF84 in BASIC's TI and TI$.

DD/F760.

outine reads the jiffy clock (A2-A0) into the accu-
r, X register, and Y register.

updated every 1/60 second. When the jiffy clock
s a value equal to 24 hours, it is reset to 0.

 conditions**: Accumulator holds high byte of jiffy clock. X register holds
 byte of jiffy clock. Y register holds low byte of jiffy
clock.

### C64 KERNAL jump table (Frank Kontros)
t:A=MSB, X=middle, Y=LSB             - - -  A X Y  A X Y

### Kernal 64 / 128 (Craig Taylor)
egisters In  : None.
egisters Out : .AXY - Clock value in jiffies (1/60 secs).
emory Changed: None.

### Das neue Commodore-64-intern-Buch (Baloui et al.)
ie laufende Zeit

### Mapping the Commodore 64 (Sheldon Leemon)
ds the software clock (which counts sixtieths of a second) into
ternal registers.  The .Y register contains the most significant
from location 160 ($A0)), the .X register contains the middle
from location 161 ($A1)), and the Accumulator contains the least
icant byte (from location 162 ($A2)).

### Machine Language Routines (Todd D Heimarck)
outine returns the current value of the jiffy dock. The
alue corresponds to the number of jiffies (1 /60-second
als) that have elapsed since the system was turned on or
 or the number of jiffies since midnight if the dock value
en set. The low byte of the clock value (location $A2) is
ed in .A, the middle byte (location $A1) in .X, and the
yte location $A0) in .Y.

### Commodore 128 intern (Jörg Schieb et al.)
Routine liest die 24-Stunden-Uhr aus und
bt die drei Bytes den Registern Y (höchstwertig), X und
 (niederwertig).

abeparameter**: .A, .X, .Y

piel**:

      ;Auslesen der 24-Stunden-Uhr
      JSR $FFDE ;RDTIM aufrufen
      STY $FC   ;MSB merken
      STX $FD   ;mittleres Byte merken
      STA $FE   ;LSB merken

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-ffde]]

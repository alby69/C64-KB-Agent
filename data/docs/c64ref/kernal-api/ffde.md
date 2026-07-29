---
title: ealtime clock
source_url: https://github.com/mist64/c64ref/blob/main/src/kernal/commodore_128_intern.txt
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
- jsr
- rdtim
- sta
- stx
- sty
scraped_at: '2026-07-29'
c64ref:
  module: kernal
  source_files:
  - commodore_128_intern.txt
  - cracking_the_kernal.txt
  - mapping_the_commodore_64.txt
  - kernal_64_/_128.txt
  - machine_language_routines.txt
  - c64_kernal_jump_table.txt
  - c64_programmer's_reference_guide.txt
  - commented_rom_disassembly.txt
  - das_neue_commodore-64-intern-buch.txt
  - standard_kernal_functions.txt
  - compute!'s_tool_kit:_kernal.txt
  address: $FFDE
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'unication registers: A, X, Y'
  - name: Standard KERNAL Functions
    author: Joe Forster / STA
    description: –
  - name: Commented ROM Disassembly
    author: Lee Davison
    description: outine returns the time, in jiffies, in AXY. The accumulator contains
      the
  - name: Cracking The Kernal
    author: Peter Marcotty
    description: Locations 160-162 are transferred, in order, to the Y and X registers
      and the...
  - name: 'COMPUTE!''s Tool Kit: Kernal'
    author: Dan Heeb
    description: 'ed by**: JSR at AF84/CF84 in BASIC''s TI and TI$.'
  - name: C64 KERNAL jump table
    author: Frank Kontros
    description: t:A=MSB, X=middle, Y=LSB             - - -  A X Y  A X Y
  - name: Kernal 64 / 128
    author: Craig Taylor
    description: 'egisters In  : None.'
  - name: Das neue Commodore-64-intern-Buch
    author: Baloui et al.
    description: ie laufende Zeit
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: ds the software clock (which counts sixtieths of a second) into
  - name: Machine Language Routines
    author: Todd D Heimarck
    description: outine returns the current value of the jiffy dock. The
  - name: Commodore 128 intern
    author: Jörg Schieb et al.
    description: Routine liest die 24-Stunden-Uhr aus und
---

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
---
title: me-out on serial bus
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
- lda
- settmo
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
  address: $FFA2
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'unication registers: A'
  - name: Standard KERNAL Functions
    author: Joe Forster / STA
    description: A = Timeout value.
  - name: Commented ROM Disassembly
    author: Lee Davison
    description: outine sets the timeout flag for the serial bus. When the timeout
      flag is
  - name: Cracking The Kernal
    author: Peter Marcotty
    description: is used only with an IEEE add-on card to access the serial bus.
  - name: 'COMPUTE!''s Tool Kit: Kernal'
    author: Dan Heeb
    description: 'ed by**: None.'
  - name: C64 KERNAL jump table
    author: Frank Kontros
    description: ': A bit7=1 disable, bit7=0 enable    A - -  A - -  - - -'
  - name: Kernal 64 / 128
    author: Craig Taylor
    description: his is a routine who's code never made it into any versions
  - name: Das neue Commodore-64-intern-Buch
    author: Baloui et al.
    description: das Time-out-Flag für den IEC-Bus
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: outine sets the time-out flag for the IEEE bus.  When timeouts
  - name: Machine Language Routines
    author: Todd D Heimarck
    description: TTMO routine stores the contents of the accumulator in
  - name: Commodore 128 intern
    author: Jörg Schieb et al.
    description: utine speichert den im <Akku> überge-
---

# $FFA2 — me-out on serial bus ($FFA2)

## Panoramica
La routine KERNAL `None` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FFA2`
- **Chiamata**: `JSR None` o `SYS 65442`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: A
aratory routines: None
r returns: None
k requirements: 2
sters affected: None

: This routine is used ONLY with an IEEE add-on card! |
|

scription**: This routine sets the timeout flag for the IEEE bus. When
meout flag is set, the Commodore 64 will wait for a device on the
ort for 64 milliseconds. If the device does not respond to the
ore 64's Data Address Valid (DAV) signal within that time the
ore 64 will recognize an error condition and leave the handshake
ce. When this routine is called when the accumulator contains a 0
 7, timeouts are enabled. A 1 in bit 7 will disable the timeouts.

: The Commodore 64 uses the timeout feature to communicate that a disk file is not found on an attempt to OPEN a file only with an IEEE card. |
|

 to Use:

 THE TIMEOUT FLAG

 bit 7 of the accumulator to 0.
l this routine.

ET THE TIMEOUT FLAG

 bit 7 of the accumulator to 1.
l this routine.

MPLE:

ISABLE TIMEOUT
   LDA #0
   JSR SETTMO

### Standard KERNAL Functions (Joe Forster / STA)
A = Timeout value.
: –
egisters: –
ddress: $FE21.

### Commented ROM Disassembly (Lee Davison)
outine sets the timeout flag for the serial bus. When the timeout flag is
he computer will wait for a device on the serial port for 64 milliseconds.
 device does not respond to the computer's DAV signal within that time the
er will recognize an error condition and leave the handshake sequence. When
outine is called and the accumulator contains a 0 in bit 7, timeouts are
d. A 1 in bit 7 will disable the timeouts.

The the timeout feature is used to communicate that a disk file is not found
attempt to OPEN a file.

### Cracking The Kernal (Peter Marcotty)
is used only with an IEEE add-on card to access the serial bus.

isable time-outs on serial bus.
   LDA #0
   JSR SETTMO
o enable time-outs, set the accumulator to a 128 and call SETTMO.

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: None.

21/FE6F to store accumulator in 0285. The VIC-20
mmer's Reference Guide refers to this routine as setting a
 timeout flag and the Commodore 64 Programmer's Ref-
 Guide refers to it as setting a flag for IEEE timeout.
r, neither BASIC nor the Kernal refers to this vector.
0285 is not a register for an I/O chip and it is never re-
 to, it's hard to see how it can be used to enable or dis-
imeouts.

### C64 KERNAL jump table (Frank Kontros)
: A bit7=1 disable, bit7=0 enable    A - -  A - -  - - -

### Kernal 64 / 128 (Craig Taylor)
his is a routine who's code never made it into any versions
f the KERNAL on the C64, Vic-20 and C128.  Thus it is of no
ractical use.

### Das neue Commodore-64-intern-Buch (Baloui et al.)
das Time-out-Flag für den IEC-Bus

### Mapping the Commodore 64 (Sheldon Leemon)
outine sets the time-out flag for the IEEE bus.  When timeouts
abled, the Commodore will wait for a device for 64 milliseconds,
 it does not receive a response to its signal it will issue a
ut error.  Loading the Accumulator with a value less than 128
lling this routine will enable time-outs, while using a value
28 will disable time-outs.

outine is for use only with the Commodore IEEE add-on card,
at the time of this writing was not yet available.

### Machine Language Routines (Todd D Heimarck)
TTMO routine stores the contents of the accumulator in
EE timeout flag. (.X and .Y are unaffected.) This routine
erfluous, since the flag isn't used by any 64 or 128 ROM
e. It is present merely to maintain consistency with pre-
versions of the Kernal. For the 64, the flag location is
 for the 128, it's at $0A0E.

### Commodore 128 intern (Jörg Schieb et al.)
utine speichert den im <Akku> überge-
Wert als Timeout-Flag für die IEEE-Routinen an Adresse
 Um den Timeout in den IEEE-Routinen zu
ichen, muß das Bit 7 des <Akkus> gesetzt sein.

abeparameter**: .A

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
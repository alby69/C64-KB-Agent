---
title: input and output channels
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
- clrchn
- jsr
- rts
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
  address: $FFCC
  symbol: Close
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'unication registers: None'
  - name: Standard KERNAL Functions
    author: Joe Forster / STA
    description: –
  - name: Commented ROM Disassembly
    author: Lee Davison
    description: outine is called to clear all open channels and restore the I/O channels
      to
  - name: Cracking The Kernal
    author: Peter Marcotty
    description: resets all channels and I/O registers - the input to keyboard and
      the output ...
  - name: 'COMPUTE!''s Tool Kit: Kernal'
    author: Dan Heeb
    description: 'ed by**: JSR at A447/C447 in BASIC''s Error Message Handler, JSR
      at'
  - name: C64 KERNAL jump table
    author: Frank Kontros
    description: '- - -  - - -  A X -'
  - name: Kernal 64 / 128
    author: Craig Taylor
    description: 'egisters In  : None.'
  - name: Das neue Commodore-64-intern-Buch
    author: Baloui et al.
    description: setzt die Ein- und Ausgabe wieder andard (Tastatur/Bildschirm)
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: utine jumps through a RAM vector at 802 ($322).  It sets the
  - name: Machine Language Routines
    author: Todd D Heimarck
    description: outine restores the default I/O sources for the operating
  - name: Commodore 128 intern
    author: Jörg Schieb et al.
    description: Routine löscht evtl, mit CHKIN und/oder
---

# Close — input and output channels ($FFCC)

## Panoramica
La routine KERNAL `Close` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FFCC`
- **Chiamata**: `JSR Close` o `SYS 65484`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: None
aratory routines: None
r returns:
k requirements: 9
sters affected: A, X

scription**: This routine is called to clear all open channels and re-
the I/O channels to their original default values. It is usually
 after opening other I/O channels (like a tape or disk drive) and
them for input/output operations. The default input device is 0
ard). The default output device is 3 (the Commodore 64 screen).

ne of the channels to be closed is to the serial port, an UNTALK
 is sent first to clear the input channel or an UNLISTEN is sent to
the output channel. By not calling this routine (and leaving lis-
s) active on the serial bus) several devices can receive the same
rom the Commodore 64 at the same time. One way to take advantage
s would be to command the printer to TALK and the disk to LISTEN.
ould allow direct printing of a disk file.

 routine is automatically called when the KERNAL CLALL routine is
ed.

 to Use:
l this routine using the JSR instruction.

MPLE:
R CLRCHN

### Standard KERNAL Functions (Joe Forster / STA)
–
: –
egisters: A, X.
ddress: ($0322), $F333.

### Commented ROM Disassembly (Lee Davison)
outine is called to clear all open channels and restore the I/O channels to
original default values. It is usually called after opening other I/O
ls and using them for input/output operations. The default input device is
 keyboard. The default output device is 3, the screen.

 of the channels to be closed is to the serial port, an UNTALK signal is sent
to clear the input channel or an UNLISTEN is sent to clear the output channel.
 calling this routine and leaving listener(s) active on the serial bus,
l devices can receive the same data from the VIC at the same time. One way to
dvantage of this would be to command the printer to TALK and the disk to
. This would allow direct printing of a disk file.

### Cracking The Kernal (Peter Marcotty)
resets all channels and I/O registers - the input to keyboard and the output to screen.

estore default values to I/O devices.
   JSR CLRCHN
   RTS
he accumulator and the X register are altered.

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: JSR at A447/C447 in BASIC's Error Message Handler, JSR at
BB7 in BASIC's INPUT#, JSR at E37B/E467 in BA-
Warm Start, JSR at F6F4/F777 in Test for STOP Key, JSR
6/F799 in Error Message Handler.

22) with a default of F333/F3F3.

 current output device is a serial device, send an
EN command on the serial bus. If the current input
 is a serial device, send an UNTALK command on the
 bus.

, the current input device, to be the keyboard.

, the current output device, to be the screen.

### C64 KERNAL jump table (Frank Kontros)
- - -  - - -  A X -

### Kernal 64 / 128 (Craig Taylor)
egisters In  : None.
egisters Out : .A, .X used.
emory Changed: None.

### Das neue Commodore-64-intern-Buch (Baloui et al.)
setzt die Ein- und Ausgabe wieder andard (Tastatur/Bildschirm)

### Mapping the Commodore 64 (Sheldon Leemon)
utine jumps through a RAM vector at 802 ($322).  It sets the
t input device to the keyboard, and the current output device to
reen.  Also, if the current input device was formerly a serial
, the routine sends it an UNTALK command on the serial bus, and
erial device was formerly the current output device, the routine
it an UNLISTEN command.

### Machine Language Routines (Todd D Heimarck)
outine restores the default I/O sources for the operating
. The output channel (location $9A) is reset to device 3,
deo display. (If the previous output channel was a serial
, it is sent an UNLISTEN command.) The input channel
ion $99) is reset to device 0, the keyboard, (if the pre-
input channel was a serial device, it is sent an UNTALK
d.) The contents of .X and .A are changed, but .Y is
cted.

P to the CLRCHN execution routine is by way of
LRCH indirect vector at $0322-$0323. You can modify
tions of the routine by changing the vector to point to a
e of your own.

### Commodore 128 intern (Jörg Schieb et al.)
Routine löscht evtl, mit CHKIN und/oder
definierte Ein- und Ausgabedateien. Es wird an das
egerät ein UNTALK und an das Ausgabegerät ein
EN gesendet. Der Bildschirm ist wieder Ausgabe - und
statur Eingabegerät. Die Dateien werden nicht geschlossen,
olgt also kein CLOSE. Es werden weder Ein- noch
eparameter übergeben.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
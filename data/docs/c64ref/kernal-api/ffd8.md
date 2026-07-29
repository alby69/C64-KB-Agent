---
title: AM to device
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
related: []
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
  address: $FFD8
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'unication registers: A, X, Y'
  - name: Standard KERNAL Functions
    author: Joe Forster / STA
    description: A = Address of zero page register holding start address of memory
      area to sav...
  - name: Commented ROM Disassembly
    author: Lee Davison
    description: outine saves a section of memory. Memory is saved from an indirect
      address
  - name: Cracking The Kernal
    author: Peter Marcotty
    description: AM to device
  - name: 'COMPUTE!''s Tool Kit: Kernal'
    author: Dan Heeb
    description: 'ed by**: JSR at E15F/E15C in BASIC''s SAVE.'
  - name: C64 KERNAL jump table
    author: Frank Kontros
    description: ': A=zero page pointer to start.addr  A X Y  - - -  A X Y'
  - name: Kernal 64 / 128
    author: Craig Taylor
    description: 'egisters In  : .A = Z-page ptr to start address'
  - name: Das neue Commodore-64-intern-Buch
    author: Baloui et al.
    description: speichert Programm ab
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: utine jumps through a RAM vector at 818 ($332).  SAVE is used to
  - name: Machine Language Routines
    author: Todd D Heimarck
    description: outine saves the contents of a block of memory to disk
  - name: Commodore 128 intern
    author: Jörg Schieb et al.
    description: Routine speichert einen Speicherbereich auf
---

# $FFD8 — AM to device ($FFD8)

## Panoramica
La routine KERNAL `None` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FFD8`
- **Chiamata**: `JSR None` o `SYS 65496`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: A, X, Y
aratory routines: SETLFS, SETNAM
r returns: 5,8,9, READST
k requirements: None
sters affected: A, X, Y


scription**: This routine saves a section of memory. Memory is saved
n indirect address on page 0 specified by the accumulator to the
s stored in the X and Y registers. It is then sent to a logical
n an input/output device. The SETLFS and SETNAM routines must be
efore calling this routine. However, a file name is not required to
o device 1 (the Datassette™ recorder). Any attempt to save to
devices without using a file name results in an error.

: Device 0 (the keyboard), device 2 (RS-232), and device 3 (the screen) cannot be SAVEd to. If the attempt is made, an error occurs, and the SAVE is stopped. |
|

 to Use:

 the SETLFS routine and the SETNAM routine (unless a SAVE with no
e name is desired on "a save to the tape recorder"),
d two consecutive locations on page 0 with a pointer to the start
your save (in standard 6502 low byte first, high byte next
mat).
d the accumulator with the single byte page zero offset to the
nter.
d the X and Y registers with the low byte and high byte re-
ctively of the location of the end of the save.
l this routine.

MPLE:

   LDA #1              ;DEVICE = 1:CASSETTE
   JSR SETLFS
   LDA #0              ;NO FILE NAME
   JSR SETNAM
   LDA PROG            ;LOAD START ADDRESS OF SAVE
   STA TXTTAB          ;(LOW BYTE)
   LDA PROG+1
   STA TXTTA B+1       ;(HIGH BYTE)
   LDX VARTAB          ;LOAD X WITH LOW BYTE OF END OF SAVE
   LDY VARTAB+1        ;LOAD Y WITH HIGH BYTE
   LDA #<TXTTAB        ;LOAD ACCUMULATOR WITH PAGE 0 OFFSET
   JSR SAVE

### Standard KERNAL Functions (Joe Forster / STA)
A = Address of zero page register holding start address of memory area to save; X/Y = End address of memory area plus 1.
: Carry: 0 = No errors, 1 = Error; A = KERNAL error code (if Carry = 1).
egisters: A, X, Y.
ddress: $F5DD.

### Commented ROM Disassembly (Lee Davison)
outine saves a section of memory. Memory is saved from an indirect address
e 0 specified by A, to the address stored in XY, to a logical file. The
, $FFBA, and SETNAM, $FFBD, routines must be used before calling this
e. However, a file name is not required to SAVE to device 1, the cassette.
tempt to save to other devices without using a file name results in an error.

device 0, the keyboard, and device 3, the screen, cannot be SAVEd to. If
tempt is made, an error will occur, and the SAVE stopped.

### Cracking The Kernal (Peter Marcotty)
AM to device

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: JSR at E15F/E15C in BASIC's SAVE.

p routines**: SETLFS, SETNAM (not required for saving to tape)

y requirements**:
cumulator should contain the offset within zero page to
-byte pointer to the start of the area to be saved. The X
er should hold the low byte of the address of the end of
ea to be saved + 1. Y register should hold the high byte
 address of the end of the area to be saved + 1.

DD/F675 to save memory to a serial device or to
Saves to the screen, keyboard, or RS-232 are not permitted.

ing to tape from the VIC, only the contents of mem-
cations 0-7FFF may be saved. This restriction does not
when saving to tape from the 64.

name is required (through SETNAM) when saving
ial devices; a filename is optional when saving to tape.

D/F675 , the routine loads the pointer to the end
 save area + 1, (AE), from the X and Y registers. (End +
tes the fact that you must load X and Y to point to the
on just past the end of the save area, since the save
es consider the save complete when the pointer to the
rea equals the value of the pointer (AE).) It also sets
the pointer to the start of the save area, from the zero
ointer indexed by the accumulator, and then performs
irect JMP through the vector at (0332), which defaults to
675.

serial save, the routine commands the current serial
 to listen with attention, then sends a secondary address
 to indicate a SAVE operation. If the device is present,
lename and the starting address are sent to the serial de-
Next, the routine sends all the bytes from the save area
he serial bus. When the save is complete, it sends a
ary address of $E1 to indicate the CLOSE command
mmands the serial device to unlisten.

pe save, it is important that you specify the second-
dress correctly. For an even secondary address, the
 for the saved program will have a identifier byte of 1,
ting a relocatable program. An odd secondary address
es a header identifier byte of 3, indicating a non-
table program. Also, if you have bit 1 on in the second-
dress ($02 or $03 would set bit 1), then an end-of-tape
 with a identifier byte of 5 is written following the
program.

pe save operation first writes a header to tape. This
eader contains the identifier byte, the starting address
ding address + 1 of the save area, and the filename (if
name is used). Then data from the save area is written to
If bit 1 of the secondary address is 1, an end-of-tape
 is also written following the data from the save area.
entical copies of the tape header(s) and the program are
n to tape to allow for error checking and correction dur-
pe loading.

### C64 KERNAL jump table (Frank Kontros)
: A=zero page pointer to start.addr  A X Y  - - -  A X Y
  Y/X=ending address

### Kernal 64 / 128 (Craig Taylor)
egisters In  : .A = Z-page ptr to start address
               .XY = end address
egisters Out : .A = error code, .C = 1 if error.
               .XY = used.
emory Changed: None.

### Das neue Commodore-64-intern-Buch (Baloui et al.)
speichert Programm ab

### Mapping the Commodore 64 (Sheldon Leemon)
utine jumps through a RAM vector at 818 ($332).  SAVE is used to
er data directly from RAM to an I/O device.  Since the SAVE
e performs an OPEN, it must be preceded by a call to the SETLFS
e to specify the logical file number, device number, and
ary address, and a call to the SETNAM routine to specify the
me (although a SAVE to the cassette can be performed without
 a filename).  A Page 0 pointer to the starting address of the
o be saved should be set up, with the low byte of the address
  The accumulator should be loaded with the Page 0 offset of
ointer, then the .X and .Y registers should be set with the
 address for the save, and the SAVE routine called.

### Machine Language Routines (Todd D Heimarck)
outine saves the contents of a block of memory to disk
e. It could be a BASIC or ML program, but it doesn't
o be. A number of preparatory routines must be called
 SETLFS, SETNAM, and (for the 128 only) SETBNK. See
scussions of those routines for details.

 establishes the device number and secondary ad-
for the operation. (The logical file number isn't signifi-
or saving.) The secondary address is irrelevant for saves
ial devices, but for tape it specifies the header type. If bit
he secondary address value is %1 (if the value is 1, for
e), the data will be stored in a nonrelocatable file—one
ill always load to the same memory address from which
 saved. Otherwise, the data will be stored in a file that
 loaded to another location. If bit 1 of the secondary ad-
is %1 (if the value is 2 or 3, for example), the file will be
ed by an end-of-tape marker.

 calling SAVE, you must also set up a two-byte
age pointer containing the starting address of the block
ory to be saved and then store the address of the zero-
ointer in the accumulator. The ending address (plus
or the save should be stored in .X (low byte) and .Y
byte). To save the entire contents of the desired area, it's
ant to remember that .X and .Y must hold an address
s one location beyond the desired ending address.

he save is complete, the carry will be clear if the
as successfully saved, or set if an error occurred (or if the
OP key was pressed to abort the save). When carry is
on return, the accumulator will hold the Kernal error
ndicating the problem. Possible error-code values in-
5 (serial device was not present), 8 (no name was speci-
or a serial save), and 9 (an illegal device number was
ied). The success of the operation will also be indicated
 value in the tape/serial status flag. (See READST for
s.)

### Commodore 128 intern (Jörg Schieb et al.)
Routine speichert einen Speicherbereich auf
atei (Diskette, Kassette) ab. Dazu muß man, wie bei der
-Routine, zunächst Geräteadresse, Sekundäradresse,
nk, Filename etc. durch die Routinen SETBNK,
 und SETNAM definieren. Im Akku wird die Zeropage-
e angegeben, an der die Anfangsadresse des abzu-
ernden Bereiches steht. Im X- (Lo) und Y-Register (Hi)
ntsprechend die Endadresse des abzuspeichernden
hes angegeben.

abeparameter**: .A, .X, .Y, Zeropage

piel**:

      ;Abspeichern des Bereiches $1000 bis $1100
      JSR PREP  ;SETLFS, SETNAM, SETBNK etc. aufrufen
      LDA #$00  ;Lo-Byte von $1000
      STA $FC   ;in Zeropage speichern
      LDA #$10  ;Hi-Byte von $1000
      STA $FD   ;in Zeropage speichern
      LDA #$FC  ;der Pointer befindet sich an $FC
      LDX #$00  ;Lo-Byte der Endadresse $1100
      LDY #$11  ;Hi-Byte der Endadresse $1100
      JSR $FFD8 ;SAVESP - Speichern des Bereiches $1000-$1100

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
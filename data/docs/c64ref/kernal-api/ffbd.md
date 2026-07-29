---
title: lename
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
- ece7-load
- f34a-open
- f5ed-save
- jsr
- lda
- ldx
- ldy
- setnam
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
  address: $FFBD
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'unication registers: A, X, Y'
  - name: Standard KERNAL Functions
    author: Joe Forster / STA
    description: A = File name length; X/Y = Pointer to file name.
  - name: Commented ROM Disassembly
    author: Lee Davison
    description: outine is used to set up the file name for the OPEN, SAVE, or LOAD
      routines.
  - name: Cracking The Kernal
    author: Peter Marcotty
    description: . In order to access the OPEN, LOAD, or SAVE routines, SETNAM must
      be called ...
  - name: 'COMPUTE!''s Tool Kit: Kernal'
    author: Dan Heeb
    description: 'ed by**: JSR at E1D6/E1D3 in BASIC''s Set LOAD /VERIFY /SAVE'
  - name: C64 KERNAL jump table
    author: Frank Kontros
    description: ': A=length of filename               A X Y  A X Y  - - -'
  - name: Kernal 64 / 128
    author: Craig Taylor
    description: 'egisters In  : .A = string length, .XY = string address.'
  - name: Das neue Commodore-64-intern-Buch
    author: Baloui et al.
    description: Parameter des Filenamens, Akku muß des Namens enthalten, X und Y
      enthalten re...
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: outine puts the value in the Accumulator into the location which
      stores
  - name: Machine Language Routines
    author: Todd D Heimarck
    description: outine assigns the length (location $B7) and address
  - name: Commodore 128 intern
    author: Jörg Schieb et al.
    description: Routine werden die Informationen für den
---

# $FFBD — lename ($FFBD)

## Panoramica
La routine KERNAL `None` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FFBD`
- **Chiamata**: `JSR None` o `SYS 65469`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: A, X, Y
aratory routines:
k requirements: 2
sters affected:

scription**: This routine is used to set up the file name for the OPEN,
or LOAD routines. The accumulator must be loaded with the length of
le name. The X and Y registers must be loaded with the address of
le name, in standard 6502 low-byte/high-byte format. The address
 any valid memory address in the system where a string of
ters for the file name is stored. If no file name is desired, the
lator must be set to 0, representing a zero file length. The X and
sters can be set to any memory address in that case.

 to Use:

d the accumulator with the length of the file name.
d the X index register with the low order address of the file
e.
d the Y index register with the high order address.
l this routine.

MPLE:

   LDA #NAME2-NAME     ;LOAD LENGTH OF FILE NAME
   LDX #<NAME          ;LOAD ADDRESS OF FILE NAME
   LDY #>NAME
   JSR SETNAM

### Standard KERNAL Functions (Joe Forster / STA)
A = File name length; X/Y = Pointer to file name.
: –
egisters: –
ddress: $FDF9.

### Commented ROM Disassembly (Lee Davison)
outine is used to set up the file name for the OPEN, SAVE, or LOAD routines.
cumulator must be loaded with the length of the file and XY with the pointer
e name, X being th low byte. The address can be any valid memory address in
stem where a string of characters for the file name is stored. If no file
esired the accumulator must be set to 0, representing a zero file length,
t case  XY may be set to any memory address.

### Cracking The Kernal (Peter Marcotty)
. In order to access the OPEN, LOAD, or SAVE routines, SETNAM must be called first.

ETNAM will prepare the disk drive for'FILE#1'.
   LDA #6
   LDX #L,NAME
   LDY #H,NAME
   JSR SETNAM
ME .BY 'FILE#1'
ccumulator is file length, X is low byte, and Y is high byte.

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: JSR at E1D6/E1D3 in BASIC's Set LOAD /VERIFY /SAVE
ters, JSRs at E21B/E218 and E261/E25E in BASIC's
 Parameters for OPEN and CLOSE.

y requirements**:
lator should contain the length of the filename. The X
er should hold the low byte of the starting address of the
me. The Y register should hold the high byte of the file-
ddress. The filename may be stored at any addressable
 location.

F9/FE49 to prepare a filename for subsequent
LOAD/VERIFY, or SAVE processing. The accumulator
 the length of the filename, is stored in B7. The pointer
 filename from the X and Y registers is stored in (BB).

gh you could create a filename that is 255 (deci-
haracters long (the accumulator can hold a maximum
of $FF or decimal 255), not all of this maximum file-
ize can be used.

pe, the filename is stored in the tape buffer, which
 bytes long. Flowever, 5 bytes are taken for the identifier
e starting and ending addresses, which leaves 187 bytes
an be used for the filename.

irk with the serial devices is that if the secondary
s you specify in SETLFS is larger than 128, the filename
 sent for OPEN, LOAD, or SAVE.

### C64 KERNAL jump table (Frank Kontros)
: A=length of filename               A X Y  A X Y  - - -
  Y/X=pointer to name addr

### Kernal 64 / 128 (Craig Taylor)
egisters In  : .A = string length, .XY = string address.
egisters Out : None.
emory Changed: None.
ote          : To specify _no_ filename specify a length of 0.

### Das neue Commodore-64-intern-Buch (Baloui et al.)
Parameter des Filenamens, Akku muß des Namens enthalten, X und Y enthalten resse des Filenamens (Low- und High-Byte)

### Mapping the Commodore 64 (Sheldon Leemon)
outine puts the value in the Accumulator into the location which stores
mber of characters in the filename, and sets the pointer to the
s of the ASCII text of the filename from the .X and .Y
ers.  This sets up the filename for the OPEN, LOAD, or SAVE
e.

### Machine Language Routines (Todd D Heimarck)
outine assigns the length (location $B7) and address
ons $BB-$BC) of the filename for the current I/O opera-
Call the routine with the length of the filename in .A and
dress of the first character of the name in .X (low byte)
 (high byte). If no name is used for the current opera-
load the accumulator with 0; the values in .X and .Y are
rrelevant, All register values are preserved during this
e.

### Commodore 128 intern (Jörg Schieb et al.)
Routine werden die Informationen für den
men in der Zeropage gespeichert. Diese Angaben sind alle
m Öffnen eines Kanales zu machen. Im <Akku> wird die
des Filenamens übergeben, im X-Register das Lo-Byte
resse und im Y-Register das Hi-Byte der Adresse, an der
lename gespeichert ist. Ferner müssen Sie mit der
-Routine die Konfigurationsindizes für den Filenamen
n zu bearbeitenden Speicherbereich übergeben.

abeparameter**: .A, .X, .Y

piel**:

      ;Eröffnen eines des Directory-Files auf Diskette
      LDA #$0C  ;Bereich im RAM-Bank 0
      TAX       ;Filename auch in RAM-Bank 0
      JSR $FF68 ;SETBNK aufrufen
      LDA #$01  ;Logische Filenummer
      LDX #$08  ;Geräteadresse
      LDY #$00  ;Sekundäradresse für Lesen
      JSR $FFBA ;SETLFS
      LDA #$01  ;Länge des Filenamens
      LDX #$00  ;Lo-Byte der Adresse, an der der
      LDY #$10  ;Filename gespeichert ist ($1000)
      JSR $FFBD ;SETNAM
      JSR $FFC0 ;OPEN - Öffnen des Kanals

 Adresse $1000:

000 24 ....

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
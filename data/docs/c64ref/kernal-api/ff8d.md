---
title: et vectored I/O
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
- 00f3-user
- clc
- jsr
- lda
- ldx
- ldy
- rts
- sec
- sta
- vector
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
  address: $FF8D
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'unication registers: X, Y'
  - name: Standard KERNAL Functions
    author: Joe Forster / STA
    description: 'Carry: 0 = Copy user table into vector table, 1 = Copy vector table
      into user...'
  - name: Commented ROM Disassembly
    author: Lee Davison
    description: outine manages all system vector jump addresses stored in RAM. Calling
      this
  - name: Cracking The Kernal
    author: Peter Marcotty
    description: . If the carry bit of the accumulator is set, the start of a list
      of the curr...
  - name: 'COMPUTE!''s Tool Kit: Kernal'
    author: Dan Heeb
    description: 'ed by**: None.'
  - name: C64 KERNAL jump table
    author: Frank Kontros
    description: ': C=0 moves from Y/X to vectors      - X Y  - X -  A - Y'
  - name: Kernal 64 / 128
    author: Craig Taylor
    description: 'egisters In  : .C = 0 (Set KERNAL Vectors) | .C = 1 (Duplicate KERNAL
      vectors)'
  - name: Das neue Commodore-64-intern-Buch
    author: Baloui et al.
    description: ktoren initialisieren
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: outine is used to read or change the values for the 16 RAM vectors
      to the
  - name: Machine Language Routines
    author: Todd D Heimarck
    description: outine can be used either to store the current values of
  - name: Commodore 128 intern
    author: Jörg Schieb et al.
    description: Routine kopiert die 16 Vektoren ab $0314
---

# $FF8D — et vectored I/O ($FF8D)

## Panoramica
La routine KERNAL `None` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF8D`
- **Chiamata**: `JSR None` o `SYS 65421`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: X, Y
aratory routines: None
r returns: None
k requirements: 2
sters affected: A, X, Y


scription**: This routine manages all system vector jump addresses
 in RAM. Calling this routine with the the accumulator carry bit
ores the current contents of the RAM vectors in a list pointed to
 X and Y registers. When this routine is called with the carry
 the user list pointed to by the X and Y registers is transferred
 system RAM vectors. The RAM vectors are listed in the memory map.

: This routine requires caution in its use. The best way to use it is to first read the entire vector contents into the user area, alter the desired vectors, and then copy the contents back to the system vectors. |
|

 to Use:

HE SYSTEM RAM VECTORS

 the carry.
 the X and y registers to the address to put the vectors.
l this routine.

HE SYSTEM RAM VECTORS

ar the carry bit.
 the X and Y registers to the address of the vector list in RAM
t must be loaded.
l this routine.

MPLE:

HANGE THE INPUT ROUTINES TO NEW SYSTEM
   LDX #<USER
   LDY #>USER
   SEC
   JSR VECTOR      ;READ OLD VECTORS
   LDA #<MYINP     ;CHANGE INPUT
   STA USER+10
   LDA #>MYINP
   STA USER+11
   LDX #<USER
   LDY #>USER
   CLC
   JSR VECTOR      ;ALTER SYSTEM
   ...
ER *=*+26

### Standard KERNAL Functions (Joe Forster / STA)
Carry: 0 = Copy user table into vector table, 1 = Copy vector table into user table; X/Y = Pointer to user table.
: –
egisters: A, Y.
ddress: $FD1A.

### Commented ROM Disassembly (Lee Davison)
outine manages all system vector jump addresses stored in RAM. Calling this
e with the carry bit set will store the current contents of the RAM vectors
ist pointed to by the X and Y registers. When this routine is called with
rry bit clear, the user list pointed to by the X and Y registers is copied
 system RAM vectors.

This routine requires caution in its use. The best way to use it is to first
he entire vector contents into the user area, alter the desired vectors and
opy the contents back to the system vectors.

### Cracking The Kernal (Peter Marcotty)
. If the carry bit of the accumulator is set, the start of a list of the current contents of the RAM vectors is returned in the X and Y registers. If the carry bit is clear, there the user list pointed to by the X and Y registers is transferred to the system RAM vectors.

hange the input routines to new system.
   SEC
   JSR VECTOR
   LDA #L,MYINP
   STA USER+10
   LDA #H,MYINP
   STA USER+11
   LDX #L,USER
   LDY #H,USER
   CLC
   JSR VECTOR
   RTS
ER .DE 26
he new input list can start anywhere. USER is the location for temporary strings, and 35-36 is the utility pointer area.

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: None.

y requirements**:
should be set or clear, depending on the function
d:

e carry bit to store the RAM vectors at
-(0332) at the location pointed to by the X and Y
ers.

the carry bit to load the RAM vectors at
-(0332) from the location pointed to by X and Y.

1A/FD57 (see chapter 2).

X and Y at (C3), the base address of where the vec-
ble will be read from or stored to.

 carry is set, store the RAM vectors at (0314)-(0332)
 location pointed to by the X and Y registers.

 carry is clear, load the RAM vectors at
-(0332) from the location pointed to by X and Y.

### C64 KERNAL jump table (Frank Kontros)
: C=0 moves from Y/X to vectors      - X Y  - X -  A - Y
  C=1 moves vectors to Y/X           - X Y  - X -  A - Y

### Kernal 64 / 128 (Craig Taylor)
egisters In  : .C = 0 (Set KERNAL Vectors) | .C = 1 (Duplicate KERNAL vectors)
               .XY = address of vectors    | .XY = address of user vectors
egisters Out : .A, .Y destroyed            | .A, .Y destroyed.
emory Changed: KERNAL Vectors changed      | Vectors written to .XY
ote          : This routine is rarely used, usually the vectors are directly
               changed themselves. The vectors, in order, are :

               C128: IRQ,BRK,NMI,OPEN,CLOSE,CHKIN,CHKOUT,CLRCH,BASIN,BSOUT
                     STOP,GETIN,CLALL,EXMON (monitor),LOAD,SAVE
               C64 : IRQ,BRK,NMI,OPEN,CLOSE,CHKIN,CHKOUT,CLRCH,BASIN,BSOUT
                     STOP,GETIN,CLALL,USRCMD (not used),LOAD,SAVE

### Das neue Commodore-64-intern-Buch (Baloui et al.)
ktoren initialisieren

### Mapping the Commodore 64 (Sheldon Leemon)
outine is used to read or change the values for the 16 RAM vectors to the
upt and important Kernal I/O routines in the table that starts
 ($314).  If the Carry flag is set when the routine is called,
rrent value of the 16 vectors will be stored at a table whose
s is pointed to by the values in the .X and .Y registers.  If
rry flag is cleared, the RAM vectors will be loaded from the
whose address is pointed to by the .X and .Y registers.  Since
outine can change the vectors for the IRQ and NMI interrupts,
ght expect that the Interrupt disable flag would be set at its
ing.  Such is not the case, however, and therefore it would be
o execute an SEI before calling it and a CLI afterwards (as the
on RESET routine does) just to be safe.

### Machine Language Routines (Todd D Heimarck)
outine can be used either to store the current values of
 indirect vectors at $0314-$0333 or to write new values
 vectors. When calling this routine, .X and .Y should be
 with the address of a 32-byte table (low byte in .X,
yte in .Y). If the status-register carry bit is clear when
utine is called, the vectors will be loaded with the values
he table. If carry is set, the 16 two-byte address values
tly in the vectors will be copied to the table.

### Commodore 128 intern (Jörg Schieb et al.)
Routine kopiert die 16 Vektoren ab $0314
 durch das X- (Low) und Y-Register (High) definierten
er, sofern das CARRY-Flag gesetzt ist. Bei gelöschtem
Flag werden die Vektoren ab $0314 mit dem durch das
 Y-Register angegebenen Bereich geladen.

abeparameter**: .X, .Y, CARRY

piel**:

      LDX #$00  ;Lo-Byte von $1000
      LDY #$10  ;Hi-Byte von $1000
      CLC       ;Lösche Carry zum Kopieren ($1000)->($0314)
      JSR $FF80 ;Belege Vektoren neu

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
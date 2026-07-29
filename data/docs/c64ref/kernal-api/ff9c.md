---
title: et bottom of memory
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
- clc
- iny
- jsr
- membot
- rts
- sec
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
  address: $FF9C
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'unication registers: X, Y'
  - name: Standard KERNAL Functions
    author: Joe Forster / STA
    description: 'Carry: 0 = Restore from input, 1 = Save to output; X/Y = Address
      (if Carry = 0).'
  - name: Commented ROM Disassembly
    author: Lee Davison
    description: outine is used to read and set the bottom of RAM. When this routine
      is
  - name: Cracking The Kernal
    author: Peter Marcotty
    description: . If the carry bit is set, then the low byte and the high byte of
      RAM are ret...
  - name: 'COMPUTE!''s Tool Kit: Kernal'
    author: Dan Heeb
    description: 'ed by**: JSR at E403/E3E5 in BASIC''s Cold Start.'
  - name: C64 KERNAL jump table
    author: Frank Kontros
    description: ': C=0; Y/X address                   - X Y  - X Y  - - -'
  - name: Kernal 64 / 128
    author: Craig Taylor
    description: 'egisters In  : .C = 1 (Read MemBot)     | .C = 0 (Set MemBot)'
  - name: Das neue Commodore-64-intern-Buch
    author: Baloui et al.
    description: be Funktion wie $FF99, jedoch für den fang
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: outine can be used to either read or set the bottom of RAM pointer.  If
  - name: Machine Language Routines
    author: Todd D Heimarck
    description: MTOP.
  - name: Commodore 128 intern
    author: Jörg Schieb et al.
    description: o wie bei der Routine MEMTOP wird bei
---

# $FF9C — et bottom of memory ($FF9C)

## Panoramica
La routine KERNAL `None` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF9C`
- **Chiamata**: `JSR None` o `SYS 65436`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: X, Y
aratory routines: None
r returns: None
k requirements: None
sters affected: X, Y

scription**: This routine is used to set the bottom of the memory. If
cumulator carry bit is set when this routine is called, a pointer
 lowest byte of RAM is returned in the X and Y registers. On the
nded Commodore 64 the initial value of this pointer is $0800
in decimal). If the accumulator carry bit is clear (-O) when this
e is called, the values of the X and Y registers are transferred to
w and high bytes, respectively, of the pointer to the beginning of
RAM.

 to Use:

D THE BOTTOM OF RAM

 the carry.
l this routine.

 THE BOTTOM OF MEMORY

ar the carry.
l this routine.

MPLE:

OVE BOTTOM OF MEMORY UP 1 PAGE
   SEC         ;READ MEMORY BOTTOM
   JSR MEMBOT
   INY
   CLC         ;SET MEMORY BOTTOM TO NEW VALUE
   JSR MEMBOT

### Standard KERNAL Functions (Joe Forster / STA)
Carry: 0 = Restore from input, 1 = Save to output; X/Y = Address (if Carry = 0).
: X/Y = Address (if Carry = 1).
egisters: X, Y.
ddress: $FE34.

### Commented ROM Disassembly (Lee Davison)
outine is used to read and set the bottom of RAM. When this routine is
 with the carry bit set the pointer to the bottom of RAM will be loaded
Y. When this routine is called with the carry bit clear XY will be saved as
ttom of memory pointer changing the bottom of memory.

### Cracking The Kernal (Peter Marcotty)
. If the carry bit is set, then the low byte and the high byte of RAM are returned in the X and Y registers. If the carry bit is clear, the bottom of RAM is set to the X and Y registers.

ove bottom of memory up one page.
   SEC
   JSR MEMBOT
   INY
   CLC
   JSR MEMBOT
   RTS
he accumulator is left alone.

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: JSR at E403/E3E5 in BASIC's Cold Start.

y requirements**:
should be set or clear, depending on function desired:

rry to read bottom of memory.

carry to set bottom of memory. The X register is the
te of the address of the bottom of memory, and the Y
er is the high byte of the address of the bottom of
.

34/FE82.

 carry is clear at entry, set the pointer to bottom of
 (0281) from X and Y registers.

 carry is set at entry, load X and Y registers from
, the pointer to the bottom of memory.

itial values of (0281) are 1000 for an unexpanded
400 for a VIC with 3K expansion, 1200 for a VIC with
more expanded, and 0800 for the 64.

### C64 KERNAL jump table (Frank Kontros)
: C=0; Y/X address                   - X Y  - X Y  - - -
t:C=1; Y/X address                   - - -  - X Y  - X Y

### Kernal 64 / 128 (Craig Taylor)
egisters In  : .C = 1 (Read MemBot)     | .C = 0 (Set MemBot)
                                        | .XY = bottom of memory.
egisters Out : .XY = bottom of memory   | None.
emory Changed: None.                    | Bottom of Memory changed.
ote          : On the C=128, this routine refers to the bottom of BANK 0 RAM,
               not, BANK 1 RAM.

### Das neue Commodore-64-intern-Buch (Baloui et al.)
be Funktion wie $FF99, jedoch für den fang

### Mapping the Commodore 64 (Sheldon Leemon)
outine can be used to either read or set the bottom of RAM pointer.  If
 with the Carry flag set, the address in the pointer will be
 into the .X and .Y registers.  If called with the Carry flag
d, the pointer will be changed to the address found in the .X
 registers.

### Machine Language Routines (Todd D Heimarck)
MTOP.

### Commodore 128 intern (Jörg Schieb et al.)
o wie bei der Routine MEMTOP wird bei
htem CARRY-Flag die Untergrenze des verfügbaren
ers mit den beiden Registern X ^Lo) und Y (Hi) belegt.
s CARRY-Flag gesetzt, so wird die Speicheruntergrenze
esen und in den beiden Registern übergeben.

abeparameter**: .X, .Y (bei gelöschtem CARRY), CARRY

abeparameter**: .X, .Y (bei gesetztem CARRY)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
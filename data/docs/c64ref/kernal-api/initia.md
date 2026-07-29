---
title: lize RAM, reset tape buffer
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
- '0000'
- 0200-buf
- jsr
- ramtas
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
  address: $FF87
  symbol: Initia
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'unication registers: A, X, Y'
  - name: Standard KERNAL Functions
    author: Joe Forster / STA
    description: –
  - name: Commented ROM Disassembly
    author: Lee Davison
    description: st and find RAM end
  - name: Cracking The Kernal
    author: Peter Marcotty
    description: is used to test RAM, reset the top and bottom of memory pointers,
      clear $0000...
  - name: 'COMPUTE!''s Tool Kit: Kernal'
    author: Dan Heeb
    description: 'ed by**: None.'
  - name: C64 KERNAL jump table
    author: Frank Kontros
    description: '- - -  - - -  A X Y'
  - name: Kernal 64 / 128
    author: Craig Taylor
    description: 'egisters In  : None.'
  - name: Das neue Commodore-64-intern-Buch
    author: Baloui et al.
    description: schen/testen
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: outine performs a number of initialization tasks.
  - name: Machine Language Routines
    author: Todd D Heimarck
    description: outine clears zero-page RAM (locations $02-$FF) and
  - name: Commodore 128 intern
    author: Jörg Schieb et al.
    description: Routine initialisiert die Zeropage, setzt die
---

# Initia — lize RAM, reset tape buffer ($FF87)

## Panoramica
La routine KERNAL `Initia` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF87`
- **Chiamata**: `JSR Initia` o `SYS 65415`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: A, X, Y
aratory routines: None
r returns: None
k requirements: 2
sters affected: A, X, Y

scription**: This routine is used to test RAM and set the top and
 of memory pointers accordingly. It also clears locations $0000 to
and $0200 to $03FF. It also allocates the cassette buffer, and sets
reen base to $0400. Normally, this routine is called as part of the
lization process of a Commodore 64 program cartridge.

MPLE:
   JSR RAMTAS

### Standard KERNAL Functions (Joe Forster / STA)
–
: –
egisters: A, X, Y.
ddress: $FD50.

### Commented ROM Disassembly (Lee Davison)
st and find RAM end

### Cracking The Kernal (Peter Marcotty)
is used to test RAM, reset the top and bottom of memory pointers, clear $0000 to $0101 and $0200 to $03FF, and set the screen memory to $0400.

o RAM test.
   JSR RAMTAS
   RTS
ll registers are altered.

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: None.

50 to the Initialize Memory Pointers routine on
.

0 the routine stores $00 in locations 02-0101 and
3FF; sets the pointer to the tape buffer, (B2), to 033C;
he pointer to the end of RAM + 1 in (0283), sets the
r to the start of RAM in (0281), sets the screen memory
o $04.

gh the VIC does not have a RAMTAS Kernal vec-
he corresponding operation on the VIC is done by JMP
At FD8D the routine stores $00 in 00-FF and 0200-
sets pointer to tape buffer, (B2), to 033C; sets the pointer
 end of RAM + 1 in (0283); sets the pointer to the start
 in (0281); sets the screen memory page to $1E or $10
ing on where RAM ends.

MTAS routine would mainly be used by an auto-
cartridge since the RAMTAS functions are normally exe-
during system reset.

### C64 KERNAL jump table (Frank Kontros)
- - -  - - -  A X Y

### Kernal 64 / 128 (Craig Taylor)
egisters In  : None.
egisters Out : .A, .X, .Y destroyed.
emory Changed: Z-Page, Rs-232 buffers, top/bot Ram ptrs

### Das neue Commodore-64-intern-Buch (Baloui et al.)
schen/testen

### Mapping the Commodore 64 (Sheldon Leemon)
outine performs a number of initialization tasks.

 it clears Pages 0, 2, and 3 of memory to zeros.  Next, it sets
pe buffer pointer to address 828 ($33C), and performs a
tructive test of RAM from 1024 ($400) up.  When it reaches a
M address (presumably the BASIC ROM at 40960 ($A000)), that
s is placed in the top of memory pointer at 643-4 ($283-4).  The
 of memory pointer at 641-2 ($281-2) is set to point to address
$800), which is the beginning of BASIC program text.  Finally,
inter to screen memory at 648 ($288) is set to 4, which lets the
ing System know that screen memory starts at 1024 ($400).

### Machine Language Routines (Todd D Heimarck)
outine clears zero-page RAM (locations $02-$FF) and
lizes Kernal memory pointers in zero page. For the 64
the routine also clears pages 2 and 3 (locations
$03FF), tests all RAM locations from $0400 upwards
ROM is encountered, and sets the top-of-memory
r. For the 128, the routine sets the BASIC restart vector
) to point to BASIC's cold-start entry address, $4000.

### Commodore 128 intern (Jörg Schieb et al.)
Routine initialisiert die Zeropage, setzt die
 für SYSTOP und SYSBOT (also die Speicherunter- und -
enze), setzt die Zeiger für die RS-232-Ein/Ausgabebuffer
n Kassettenbuffer zurück.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
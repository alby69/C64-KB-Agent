---
title: e I/O default vectors
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
  - machine_language_routines.txt
  - c64_kernal_jump_table.txt
  - c64_programmer's_reference_guide.txt
  - commented_rom_disassembly.txt
  - das_neue_commodore-64-intern-buch.txt
  - standard_kernal_functions.txt
  - compute!'s_tool_kit:_kernal.txt
  address: $FF8A
  symbol: Restor
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'aratory routines: None'
  - name: Standard KERNAL Functions
    author: Joe Forster / STA
    description: –
  - name: Commented ROM Disassembly
    author: Lee Davison
    description: outine restores the default values of all system vectors used in
      KERNAL and
  - name: Cracking The Kernal
    author: Peter Marcotty
    description: e I/O default vectors
  - name: 'COMPUTE!''s Tool Kit: Kernal'
    author: Dan Heeb
    description: 'ed by**: None.'
  - name: C64 KERNAL jump table
    author: Frank Kontros
    description: '- - -  - - -  A - Y'
  - name: Das neue Commodore-64-intern-Buch
    author: Baloui et al.
    description: itialisieren
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: outine sets the values for the 16 RAM vectors to the interrupt and
  - name: Machine Language Routines
    author: Todd D Heimarck
    description: outine resets the Kernal indirect vectors ($0314-$0333)
  - name: Commodore 128 intern
    author: Jörg Schieb et al.
    description: den die Systemvektoren ab Adresse $0314
---

# Restor — e I/O default vectors ($FF8A)

## Panoramica
La routine KERNAL `Restor` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF8A`
- **Chiamata**: `JSR Restor` o `SYS 65418`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
aratory routines: None
r returns: None
k requirements: 2
sters affected: A, X, Y

scription**: This routine restores the default values of all system
s used in KERNAL and BASIC routines and interrupts. (See the Memory
r the default vector contents). The KERNAL VECTOR routine is used
d and alter individual system vectors.

 to Use:

l this routine.

MPLE:
   JSR RESTOR

### Standard KERNAL Functions (Joe Forster / STA)
–
: –
egisters: –
ddress: $FD15.

### Commented ROM Disassembly (Lee Davison)
outine restores the default values of all system vectors used in KERNAL and
routines and interrupts.

### Cracking The Kernal (Peter Marcotty)
e I/O default vectors

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: None.

15/FD52 to execute the routine to initialize the
 RAM vectors. This RAM vector initialization is also
uring system reset.

g this routine restores the vectors at (0314)-(0332)
ir default values from the table at FD30/FD6D.

### C64 KERNAL jump table (Frank Kontros)
- - -  - - -  A - Y

### Das neue Commodore-64-intern-Buch (Baloui et al.)
itialisieren

### Mapping the Commodore 64 (Sheldon Leemon)
outine sets the values for the 16 RAM vectors to the interrupt and
ant Kernal I/O routines in the table that starts at 788 ($314)
 standard values held in the ROM table at 64816 ($FD30).

### Machine Language Routines (Todd D Heimarck)
outine resets the Kernal indirect vectors ($0314-$0333)
ir default values. All processor registers are affected.

### Commodore 128 intern (Jörg Schieb et al.)
den die Systemvektoren ab Adresse $0314
332 (inkl.) auf Normalwert gesetzt. Diese Routine sollte
ufen werden, wenn Sie zu viele Vektoren verbogen und
ersicht verloren haben oder wenn Sie beispielsweise ein
erungspaket ausschalten wollen. Diese Routine ruft die
de VECTOR-Routine mit gelöschtem CARRY auf.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
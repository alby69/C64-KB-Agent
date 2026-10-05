---
id: restor
type: entity
title: e I/O default vectors
aliases:
- e I/O default vectors
tags:
- jumps
- system-routines
- kernal-api
sources:
- path: data/docs/c64ref/kernal-api/restor.md
  sha256: 60b4d87c36e0337f41509535d4ce524700ec18c83b7644a14342bca8a787473a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-restor
---

# e I/O default vectors



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

## References
- Source: [[src-restor]]

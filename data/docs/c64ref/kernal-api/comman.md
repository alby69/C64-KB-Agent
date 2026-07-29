---
title: d serial bus to UNTALK
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
- rts
- talk
- untalk
- untlk
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
  address: $FFAB
  symbol: Comman
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'unication registers: None'
  - name: Standard KERNAL Functions
    author: Joe Forster / STA
    description: –
  - name: Commented ROM Disassembly
    author: Lee Davison
    description: outine will transmit an UNTALK command on the serial bus. All devices
  - name: Cracking The Kernal
    author: Peter Marcotty
    description: All devices previously set to TALK will stop sending data.
  - name: 'COMPUTE!''s Tool Kit: Kernal'
    author: Dan Heeb
    description: 'ed by**: None.'
  - name: C64 KERNAL jump table
    author: Frank Kontros
    description: '- - -  - - -  A - -'
  - name: Kernal 64 / 128
    author: Craig Taylor
    description: 'egisters In  : None.'
  - name: Das neue Commodore-64-intern-Buch
    author: Baloui et al.
    description: UNTALK-Befehl auf den IEC-Bus
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: alled, this routine sends the UNTALK code (95, $5F) on the
  - name: Machine Language Routines
    author: Todd D Heimarck
    description: ow-level 1/0 routine sends an UNTALK command to all
  - name: Commodore 128 intern
    author: Jörg Schieb et al.
    description: Routine wird beim Schließen bzw. Umlegen
---

# Comman — d serial bus to UNTALK ($FFAB)

## Panoramica
La routine KERNAL `Comman` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FFAB`
- **Chiamata**: `JSR Comman` o `SYS 65451`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: None
aratory routines: None
r returns: See READST
k requirements: 8
sters affected: A

scription**: This routine transmits an UNTALK command on the serial
ll devices previously set to TALK will stop sending data when this
d is received.

 to Use:

l this routine.

MPLE:
   JSR UNTALK

### Standard KERNAL Functions (Joe Forster / STA)
–
: –
egisters: A.
ddress: $EDEF.

### Commented ROM Disassembly (Lee Davison)
outine will transmit an UNTALK command on the serial bus. All devices
usly set to TALK will stop sending data when this command is received.

### Cracking The Kernal (Peter Marcotty)
All devices previously set to TALK will stop sending data.

ommand serial bus to stop sending data.
   JSR UNTLK
   RTS
ending UNTLK commands all talking devices to get off the serial bus.

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: None.

EF/EEF6 to send $5F, the command for UNTALK,
he serial bus. Serial devices that are talking should quit
g and terminate their connection to the serial bus.

### C64 KERNAL jump table (Frank Kontros)
- - -  - - -  A - -

### Kernal 64 / 128 (Craig Taylor)
egisters In  : None.
egisters Out : .A used.
emory Changed: None.
ote          : Low level serial I/O - recommended use OPEN,CLOSE,CHROUT etc..

### Das neue Commodore-64-intern-Buch (Baloui et al.)
UNTALK-Befehl auf den IEC-Bus

### Mapping the Commodore 64 (Sheldon Leemon)
alled, this routine sends the UNTALK code (95, $5F) on the
 bus.  This commands any TALKer on the bus to stop sending data.

### Machine Language Routines (Todd D Heimarck)
ow-level 1/0 routine sends an UNTALK command to all
s on the serial bus. Any devices which are currently
s will cease sending data.

### Commodore 128 intern (Jörg Schieb et al.)
Routine wird beim Schließen bzw. Umlegen
Eingabekanals aufgerufen. Sie bringt das zum Reden
 gebrachte Gerät zum Schweigen.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
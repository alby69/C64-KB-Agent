---
id: comman
type: entity
title: d serial bus to UNTALK
aliases:
- d serial bus to UNTALK
tags:
- jumps
- system-routines
- kernal-api
sources:
- path: data/docs/c64ref/kernal-api/comman.md
  sha256: 0fd860c6868ae78c07169368c4af523e13a34a5d43dcf70212a154b42f113cdb
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-comman
---

# d serial bus to UNTALK



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

## References
- Source: [[src-comman]]

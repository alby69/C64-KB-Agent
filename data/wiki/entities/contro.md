---
id: contro
type: entity
title: l Kernal messages
aliases:
- l Kernal messages
tags:
- jumps
- system-routines
- kernal-api
sources:
- path: data/docs/c64ref/kernal-api/contro.md
  sha256: 873b6972c9c221af3c278eccc47f4c0022c258a8f711b6a1f222aa0523839625
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-contro
---

# l Kernal messages



# Contro — l Kernal messages ($FF90)

## Panoramica
La routine KERNAL `Contro` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF90`
- **Chiamata**: `JSR Contro` o `SYS 65424`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: A
aratory routines: None
r returns: None
k requirements: 2
sters affected: A

scription**: This routine controls the printing of error and control
es by the KERNAL. Either print error messages or print control mes-
can be selected by setting the accumulator when the routine is
. FILE NOT FOUND is an example of an error message. PRESS PLAY ON
TE is an example of a control message.

 6 and 7 of this value determine where the message will come from.
 7 is 1, one of the error messages from the KERNAL is printed. If
is set, control messages are printed.

 to Use:

 accumulator to desired value.
l this routine.

MPLE:

   LDA #$40
   JSR SETMSG          ;TURN ON CONTROL MESSAGES
   LDA #$80
   JSR SETMSG          ;TURN ON ERROR MESSAGES
   LDA #0
   JSR SETMSG          ;TURN OFF ALL KERNAL MESSAGES

### Standard KERNAL Functions (Joe Forster / STA)
A = Switch value.
: –
egisters: –
ddress: $FE18.

### Commented ROM Disassembly (Lee Davison)
outine controls the printing of error and control messages by the KERNAL.
 print error messages or print control messages can be selected by setting
cumulator when the routine is called.

OT FOUND is an example of an error message. PRESS PLAY ON CASSETTE is an
e of a control message.

 and 7 of this value determine where the message will come from. If bit 7
 one of the error messages from the KERNAL will be printed. If bit 6 is set
rol message will be printed.

### Cracking The Kernal (Peter Marcotty)
. Depending on the accumulator, either error messages, control messages, or neither is printed.

urn on control messages.
   LDA #$40
   JSR SETMSG
   RTS
 128 is for error messages; a zero, for turning both off.

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: JSR at A47D/C47D in BASIC's Enable Kernal Control Mes-
 JSR at A874/C874 in BASIC'S Disable Kernal Control
es.

y requirements**:
lator should contain the value used to set message
l: $80 allows Kernal control messages; $40 allows Kernal
messages; $C0 allows both Kernal control and error mes-
 $00 disallows all Kernal messages.

18/FE66. This routine is called to determine which
es will be displayed in response to control or error con-
s. The accumulator value at entry determines the setting
 message control status.

 to Russ Davies for pointing out that bits 6 and 7
versed in describing how to set message control in the
 VIC Programmer's Reference Guides.

### C64 KERNAL jump table (Frank Kontros)
: A bit7=1 error msgs on             A - -  - - -  A - -
    bit6=1 control msgs on

### Kernal 64 / 128 (Craig Taylor)
egisters In  : .A bit 7 = KERNAL Control Messages (1 = on)
                  bit 6 = KERNAL Error   Messages (1 = on)
egisters Out : None.
ote          : KERNAL Control messages are those defined as Loading, Found etc
               ... KERNAL Error messages are I/O ERROR # messages which are
               listed as follows:

### Das neue Commodore-64-intern-Buch (Baloui et al.)
Flag für Ausgabe von Systemmeldung

### Mapping the Commodore 64 (Sheldon Leemon)
outine controls the printing of error messages and control
es by the Kernal.  It Bit 6 is set to 1 (bit value of 64),
 control messages can be printed.  These messages include
ING FOR, LOADING, and the like.  If Bit 6 is cleared to 0, these
es will not be printed (BASIC will clear this bit when a program
ning so that the messages do not appear when I/O is performed
 program).  Setting Bit 6 will not suppress the PRESS PLAY ON
r PRESS PLAY & RECORD messages, however.

 7 is set to 1 (bit value of 128), Kernal error messages can be
d.  If Bit 7 is set to 0, those error messages (for example, I/O
#nn) will be suppressed.  Note that BASIC has its own set of
messages (such as FILE NOT FOUND ERROR) which it uses in
ence to the Kernal's message.

### Machine Language Routines (Todd D Heimarck)
sets the value of the Kernal message flag (location
Call the routine with the accumulator holding the de-
flag value (.X and .Y are unaffected,) Valid flag values
(no Kernal messages are displayed), 64 (only error mes-
are displayed), 128 (only control messages—PRESS
N TAPE, for example—are displayed), and 192 (both
and control messages are displayed).

### Commodore 128 intern (Jörg Schieb et al.)
utine speichert den Wert des <Akku> in
ropage-Adresse $9D. Sollen Systemmeldungen ausgegeben
, so ist das Bit 7 des <Akkus> zu setzen. Ist $9D positiv,
den Systemmeldungen verhindert.

abeparameter**: .A

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-contro]]

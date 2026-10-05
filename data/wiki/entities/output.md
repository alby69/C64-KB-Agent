---
id: output
type: entity
title: byte to serial port
aliases:
- byte to serial port
tags:
- jumps
- system-routines
- kernal-api
sources:
- path: data/docs/c64ref/kernal-api/output.md
  sha256: 4912f47fed25eb4c5e4a2029ca858e49d1b0bf5139d5f5ed26f6781965586db8
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-output
---

# byte to serial port



# Output — byte to serial port ($FFA8)

## Panoramica
La routine KERNAL `Output` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FFA8`
- **Chiamata**: `JSR Output` o `SYS 65448`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: A
aratory routines: LISTEN, [SECOND]
r returns: See READST
k requirements: 5
sters affected: None

scription**: This routine is used to send information to devices on the
 bus. A call to this routine will put a data byte onto the serial
ing full serial handshaking. Before this routine is called, the
 KERNAL routine must be used to command a device on the serial bus
 ready to receive data. (If a device needs a secondary address, it
lso be sent by using the SECOND KERNAL routine.) The accumulator is
 with a byte to handshake as data on the serial bus. A device must
tening or the status word will return a timeout. This routine
 buffers one character. (The routine holds the previous character
sent back.) So when a call to the KERNAL UNLSN routine is made to
e data transmission, the buffered character is sent with an End Or
fy (EOI) set. Then the UNLSN command is sent to the device.

 to Use:

 the LISTEN KERNAL routine (and the SECOND routine if needed).
d the accumulator with a byte of data.
l this routine to send the data byte.

MPLE:


   LDA #'X       ;SEND AN X TO THE SERIAL BUS
   JSR CIOUT

### Standard KERNAL Functions (Joe Forster / STA)
A = Byte to write.
: –
egisters: –
ddress: $EDDD.

### Commented ROM Disassembly (Lee Davison)
outine is used to send information to devices on the serial bus. A call to
outine will put a data byte onto the serial bus using full handshaking.
 this routine is called the LISTEN routine, $FFB1, must be used to
d a device on the serial bus to get ready to receive data.

cumulator is loaded with a byte to output as data on the serial bus. A
 must be listening or the status word will return a timeout. This routine
 buffers one character. So when a call to the UNLISTEN routine, $FFAE,
e to end the data transmission, the buffered character is sent with EOI
hen the UNLISTEN command is sent to the device.

### Cracking The Kernal (Peter Marcotty)
will send data to the serial bus. LISTEN and SECOND must be called first. Call UNLSN to finish up neatly.

end the letter X to the serial bus.
   LDA #'X
   JSR CIOUT
   RTS
he accumulator is used to transfer the data.

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: None.

p routines**: LISTEN, SECOND (if serial device requires a secondary
s)

y requirements**: Accumulator should contain character to output. JMP EDDD/
o execute the Send Serial Byte Deferred routine.

ending a character to a serial device, the routine
ins a one byte buffer at 95. If this buffer is empty, the
ter to be output is simply stored in the buffer. If the
 already contains a character, the character from the
 is sent onto the serial bus and the character to be out-
 stored in the buffer. When the serial file is closed or the
 device commanded to unlisten, the final byte in the
 is sent. The character is sent to all open devices on the
 bus.

### C64 KERNAL jump table (Frank Kontros)
: A=byte, C=1 and ST=3 if timeout    A - -  A - -  - - -

### Kernal 64 / 128 (Craig Taylor)
egisters In  : .A = byte.
egisters Out : .A used.
emory Changed: None.
ote          : Low level serial I/O - recommended use OPEN,CLOSE,CHROUT etc..

### Das neue Commodore-64-intern-Buch (Baloui et al.)
in Byte aus dem Akku an den IEC-Bus aus

### Mapping the Commodore 64 (Sheldon Leemon)
outine's purpose is to send a byte of data over
rial bus.  In order for the data to be received, the serial
 must have first been commanded to LISTEN and been given a
ary address if necessary.  This routine always buffers the
t character, and defers sending it until the next byte is
ed.  When the UNLISTEN command is sent, the last byte will be
ith an End or Identify (EOI).

### Machine Language Routines (Todd D Heimarck)
ow-level I/O routine sends a byte to a serial device. The
lator should hold the byte to be sent. All register val-
e preserved. The success of the operation will be in-
d by the value in the serial status flag. (See READST for
s.)

e routine to function properly, the target serial de-
ust currently he a listener on the serial bus, which re-
 a number of setup steps. However, if you have already
med all the preparatory steps necessary for CHROUT to
al device, then you can freely substitute CIOUT for
, since, for a serial device, CHROUT simply jumps to
OUT routine.

### Commodore 128 intern (Jörg Schieb et al.)
Routine ist das Gegenstück zu ACPTR. Das
ku> übergebene Zeichen wird auf dem lEC-Bus ausge-
 Auch hier wird das Statusbyte ST an $90 entsprechend
tion geändert.

abeparameter**: .A

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-output]]

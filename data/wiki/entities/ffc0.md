---
id: ffc0
type: entity
title: logical file
aliases:
- logical file
tags:
- jumps
- system-routines
- kernal-api
sources:
- path: data/docs/c64ref/kernal-api/ffc0.md
  sha256: 6208d3e220ce5520added0fa72605b27626acf1f93e6cada587290585d7a0315
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-ffc0
---

# logical file



# $FFC0 — logical file ($FFC0)

## Panoramica
La routine KERNAL `None` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FFC0`
- **Chiamata**: `JSR None` o `SYS 65472`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: None
aratory routines: SETLFS, SETNAM
r returns: 1,2,4,5,6,240, READST
k requirements: None
sters affected: A, X, Y

scription**: This routine is used to OPEN a logical file. Once the
l file is set up, it can be used for input/output operations. Most
 I/O KERNAL routines call on this routine to create the logical
to operate on. No arguments need to be set up to use this routine,
th the SETLFS and SETNAM KERNAL routines must be called before
this routine.


 to Use:

 the SETLFS routine.
 the SETNAM routine.
l this routine.

MPLE:

s an implementation of the BASIC statement: OPEN 15,8,15,"I/O"

   LDA #NAME2-NAME    ;LENGTH OF FILE NAME FOR SETLFS
   LDY #>NAME         ;ADDRESS OF FILE NAME
   LDX #<NAME
   JSR SETNAM
   LDA #15
   LDX #8
   LDY #15
   JSR SETLFS
   JSR OPEN
ME .BYT 'I/O'
ME2

### Standard KERNAL Functions (Joe Forster / STA)
–
: –
egisters: A, X, Y.
ddress: ($031A), $F34A.

### Commented ROM Disassembly (Lee Davison)
outine is used to open a logical file. Once the logical file is set up it
 used for input/output operations. Most of the I/O KERNAL routines call on
outine to create the logical files to operate on. No arguments need to be
 to use this routine, but both the SETLFS, $FFBA, and SETNAM, $FFBD,
 routines must be called before using this routine.

### Cracking The Kernal (Peter Marcotty)
After SETLFS and SETNAM have been called, you can OPEN a logical file.

uplicate the command OPEN 15,8,15,'I/O'
   LDA #3
   LDX #L,NAME
   LDY #H,NAME
   JSR SETNAM
   LDA #15
   LDX #8
   LDY #15
   JSR SETLFS
   JSR OPEN
   RTS
ME .BY 'I/O'
PEN opens the current name file with the current LFS.

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: JSR at E1C1/E1BE in BASIC's OPEN.

p routines**: SETLFS, SETNAM

1A) with a default of F34A/F40A.

hecks whether another logical file can be opened.
r logical file can be opened if the logical file number is
and if fewer than ten logical files are already open.
xits if trying to open to the screen or keyboard, as
devices do not use files.

serial device, OPEN commands the serial device to
 and then sends a secondary address for OPEN to this
 device.

pe, OPEN checks for a tape header of a sequential
f reading, or writes a tape header for a sequential file if
g.

-232 OPEN initializes various RS-232 lines and
s two 256-byte buffers at the top of memory. RS-232
andles the x-line handshaking opening sequence in-
tly on the VIC.

### C64 KERNAL jump table (Frank Kontros)
t:A=error# if C=1                    - - -  - - -  A X Y

### Kernal 64 / 128 (Craig Taylor)
egisters In  : None.
egisters Out : .A = error code, .X,.Y destroyed.
               .C = 1 if error.
emory Changed: None.

### Das neue Commodore-64-intern-Buch (Baloui et al.)
efehl, öffnet logische Datei

### Mapping the Commodore 64 (Sheldon Leemon)
utine jumps through a RAM vector at 794 ($31A).  This routine
s a logical file to a device, so that it can be used for
Output operations.  In order to specify the logical file number,
vice number, and the secondary address if any, the SETLFS
e must first be called.  Likewise, in order to designate the
me, the SETNAM routine must be used first.  After these two
es are called, OPEN is then called.

### Machine Language Routines (Todd D Heimarck)
outine opens a logical file to a specified device in
ation for input or output. At least one preparatory step
uired before the standard OPEN routine is called:
 must be called to establish the logical file number, de-
umber, and secondary address, For tape (device 1), RS-
evice 2), or serial (device 4 or higher), SETNAM is also
ed to specify the length and address of the associated
me. Tor the 128, SETBNK must be called to establish the
umber where the filename can he found.

not necessary to load any registers before calling
and all processor register values may be changed dur-
e routine. The carry will be clear if the file was success-
opened, or it will be set if it could not be opened. When
is set upon return, the accumulator will hold an error
ndicating the problem. Possible error-code values in-
1 (ten files—the maximum allowed—are already open),
urrently open file already uses the specified logical file
), and 5 (specified device did not respond). The RS-232
pe/serial status flags will also reflect the success of the
ion for those devices, (See READST for details.)

 128, there is an exception to the carry-bit rule. Be-
of a bug in the 128's RS-232 OPEN routine, carry will
 if the RS-232 device is present when x-line handshaking
d (if the DSR line is high), or clear if the device is ab-
he opposite of the proper setting.

P to the OPEN execution routine is by way of the
indirect vector $031A-$031B. You can modify the ac-
of the routine by changing the vector to point to a rou-
f your own,

### Commodore 128 intern (Jörg Schieb et al.)
d die durch die Routinen SETNAM,
 und SETBNK definierte Datei in die Liste der
hen Filenummern aufgenommen. Erst ab diesem Augen-
können die logischen Filenummern bei den Routinen
und CHKIN angegeben werden. Beachten Sie, daß Sie
l neun Files auf einmal öffnen können.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-ffc0]]

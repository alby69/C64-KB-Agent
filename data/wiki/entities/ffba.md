---
id: ffba
type: entity
title: gical, first, and second address
aliases:
- gical, first, and second address
tags:
- jumps
- system-routines
- kernal-api
sources:
- path: data/docs/c64ref/kernal-api/ffba.md
  sha256: 914f426b0b02e68228df7bc8c8a91da218896ef6149be9ef7e8db92f9650778c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-ffba
---

# gical, first, and second address



# $FFBA — gical, first, and second address ($FFBA)

## Panoramica
La routine KERNAL `None` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FFBA`
- **Chiamata**: `JSR None` o `SYS 65466`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: A, X, Y
aratory routines: None
r returns: None
k requirements: 2
sters affected: None


scription**: This routine sets the logical file number, device address,
condary address (command number) for other KERNAL routines.

logical file number is used by the system as a key to the file
created by the OPEN file routine. Device addresses can range from 0
 The following codes are used by the Commodore 64 to stand for the
vices listed below:


ESS    |     DEVICE                   |
-------|------------------------------|
       |    Keyboard                  |
       |    Datassette™               |
       |    RS-232C device            |
       |    CRT display               |
       |    Serial bus printer        |
       |    CBM serial bus disk drive |


ce numbers 4 or greater automatically refer to devices on the
 bus.

mmand to the device is sent as a secondary address on the serial
ter the device number is sent during the serial attention
aking sequence. If no secondary address is to be sent, the Y index
er should be set to 255.

 to Use:

d the accumulator with the logical file number.
d the X index register with the device number.
d the Y index register with the command.

MPLE:

OR LOGICAL FILE 32, DEVICE #4, AND NO COMMAND:
   LDA #32
   LDX #4
   LDY #255
   JSR SETLFS

### Standard KERNAL Functions (Joe Forster / STA)
A = Logical number; X = Device number; Y = Secondary address.
: –
egisters: –
ddress: $FE00.

### Commented ROM Disassembly (Lee Davison)
outine will set the logical file number, device address, and secondary
s, command number, for other KERNAL routines.

gical file number is used by the system as a key to the file table created
 OPEN file routine. Device addresses can range from 0 to 30. The following
are used by the computer to stand for the following CBM devices:

ESS | DEVICE                    |
----|---------------------------|
    | Keyboard                  |
    | Cassette #1               |
    | RS-232C device            |
    | CRT display               |
    | Serial bus printer        |
    | CBM Serial bus disk drive |

 numbers of four or greater automatically refer to devices on the serial
bus.

and to the device is sent as a secondary address on the serial bus after
vice number is sent during the serial attention handshaking sequence. If
ondary address is to be sent Y should be set to $FF.

### Cracking The Kernal (Peter Marcotty)
stands for SET Logical address, File address, and Secondary address. After SETLFS is called, OPEN may be called.

et logical file #1, device #8, secondary address of 15.
   LDA #1
   LDX #8
   LDY #15
   JSR SETLFS
f OPEN is called, the command will be OPEN 1,8,15.

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: JSRs at E1DD/E1DA, E1F0/E1ED, and E1FD/E1FA in BA-
Set LOAD/VERIFY/SAVE Parameters; JSRs at
228, E23F/E23C, and E24E/E24B in BASIC's Handle
ters for OPEN and CLOSE.

y requirements**:
cumulator should hold the logical file number, the X
er should hold the device number, and the Y register
 hold the secondary address.

00/FE50 to set the logical file number, device
, and secondary address for a subsequent open, load,
e.

gical file number can be 1-255.

vice numbers can be 0-31. Assigned device num-
nclude 0 for the keyboard, 1 for tape, 2 for RS-232, 3 for
reen, and 4-31 for serial bus devices. By convention, se-
evice numbers 4 and 5 are usually used for printers and
or disk drives.

e comments in the paragraphs on SAVE and LOAD
es about secondary addresses. An even secondary ad-
gives a identifier byte of 1 for a relocatable program tape
. An odd secondary address gives a tape identifier of 3
nonrelocatable program tape header. A secondary ad-
that has bit 1 on (e.g., $02 or $03) produces an end-of-
eader with an identifier byte of 5.

ary addresses >= 128 (decimal) will not be sent
 serial bus. For reading from serial, use an even second-
dress. For writing to serial, use an odd secondary ad-
 Valid secondary addresses for serial devices are 0-31
al). If you specify a higher value, you may be sending a
d other than what you intended, since secondary ad-
s greater than 31 are used to represent commands to se-
evices.

### C64 KERNAL jump table (Frank Kontros)
: A=logical file number              A X Y  A X Y  - - -
  X=device number
  Y=secondary addr

### Kernal 64 / 128 (Craig Taylor)
egisters In  : .A = logical file #, .X = device #, .Y = secondary #
egisters Out : None.
emory Changed: None.

### Das neue Commodore-64-intern-Buch (Baloui et al.)
die Fileparameter, Akku muß logische mmer enthalten, X = Gerätenummer und kundäradresse

### Mapping the Commodore 64 (Sheldon Leemon)
outine stores the value in the Accumulator in the location which holds the
t logical file number, the value in the .X register is put in
cation that holds the current device number, and the value in
 register is stored in the location that holds the current
ary address.  If no secondary address is used, the .Y register
 be set to 255 ($FF).  It is necessary to set the values of the
t file number, device number, and secondary address before you
 file, or LOAD or SAVE.

### Machine Language Routines (Todd D Heimarck)
outine assigns the logical file number (location $B8), de-
umber (location $BA), and secondary address location
or the current I/O operation. Call the routine with the
lator holding the logical file number, .X holding the
 number, and .Y holding the secondary address. All reg-
values are preserved during the routine. Refer to the
nd SAVE routines for the special significance of the
ary address in those cases. When OPENing files to se-
evices, it's vital that each logical file have a unique
ary address, In the 128 Kernal, the LKUPLA and
 routines can be used to find unused logical file num-
nd secondary addresses.

### Commodore 128 intern (Jörg Schieb et al.)
Routine wird überall dort benötigt, wo man
öffnen muß. Man übergibt die logische File-nummer im
, die Geräteadresse im X-Register und die Sekun-
esse im Y-Register. Die Routine speichert diese Werte an
ropage-Adressen $B8 bis $BA ab.

abeparameter**: .A, .X, .Y

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-ffba]]

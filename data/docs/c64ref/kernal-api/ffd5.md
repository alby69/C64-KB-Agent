---
title: AM from a device
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
- ece7-load
- jsr
- lda
- ldx
- ldy
- rts
- setlfs
- setnam
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
  address: $FFD5
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'unication registers: A, X, Y'
  - name: Standard KERNAL Functions
    author: Joe Forster / STA
    description: 'A: 0 = Load, 1-255 = Verify; X/Y = Load address (if secondary address
      = 0).'
  - name: Commented ROM Disassembly
    author: Lee Davison
    description: outine will load data bytes from any input device directly into the
      memory
  - name: Cracking The Kernal
    author: Peter Marcotty
    description: The computer will perform either the LOAD or the VERIFY command.
      If the accum...
  - name: 'COMPUTE!''s Tool Kit: Kernal'
    author: Dan Heeb
    description: 'ed by**: JSR at E175/E172 in BASIC''s LOAD /VERIFY.'
  - name: C64 KERNAL jump table
    author: Frank Kontros
    description: ': A=0 load, a=1 verify               A X Y  A X Y  A X Y'
  - name: Kernal 64 / 128
    author: Craig Taylor
    description: 'egisters In  : .A = 0 - Load, Non-0 = Verify'
  - name: Das neue Commodore-64-intern-Buch
    author: Baloui et al.
    description: lädt Programm in den Speicher
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: utine jumps through a RAM vector at 816 ($330).  LOAD is used to
  - name: Machine Language Routines
    author: Todd D Heimarck
    description: outine loads a program file from tape or disk into a
  - name: Commodore 128 intern
    author: Jörg Schieb et al.
    description: mit LOADSP eine Datei geladen werden
---

# $FFD5 — AM from a device ($FFD5)

## Panoramica
La routine KERNAL `None` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FFD5`
- **Chiamata**: `JSR None` o `SYS 65493`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: A, X, Y
aratory routines: SETLFS, SETNAM
r returns: 0,4,5,8,9, READST
k requirements: None
sters affected: A, X, Y

scription**: This routine LOADs data bytes from any input device di-
 into the memory of the Commodore 64. It can also be used for a
 operation, comparing data from a device with the data already in
, while leaving the data stored in RAM unchanged.

accumulator (.A) must be set to 0 for a LOAD operation, or 1 for a
, If the input device is OPENed with a secondary address (SA) of 0
ader information from the device is ignored. In this case, the X
registers must contain the starting address for the load. If the
 is addressed with a secondary address of 1, then the data is
 into memory starting at the location specified by the header. This
e returns the address of the highest RAM location loaded.

re this routine can be called, the KERNAL SETLFS, and SETNAM
es must be called.

: You can NOT LOAD from the keyboard (0), RS-232 (2), or the screen (3). |
|


 to Use:

l the SETLFS, and SETNAM routines. If a relocated load is de-
ed, use the SETLFS routine to send a secondary address of 0.
 the A register to 0 for load, 1 for verify.
a relocated load is desired, the X and Y registers must be set
the start address for the load.
l the routine using the JSR instruction.

MPLE:

OAD A FILE FROM TAPE

   LDA #FILENO      ;SET LOGICAL FILE NUMBER
   LDX #DEVICE1     ;SET DEVICE NUMBER
   LDY CMD1         ;SET SECONDARY ADDRESS
   JSR SETLFS
   LDA #NAME1-NAME  ;LOAD A WITH NUMBER OF
                    ;CHARACTERS IN FILE NAME
   LDX #<NAME       ;LOAD X AND Y WITH ADDRESS OF
   LDY #>NAME       ;FILE NAME
   JSR SETNAM
   LDA #0           ;SET FLAG FOR A LOAD
   LDX #$FF         ;ALTERNATE START
   LDY #$FF
   JSR LOAD
   STX VARTAB       ;END OF LOAD
   STY VARTA B+1
   JMP START
ME .BYT 'FILE NAME'
ME1                 ;

### Standard KERNAL Functions (Joe Forster / STA)
A: 0 = Load, 1-255 = Verify; X/Y = Load address (if secondary address = 0).
: Carry: 0 = No errors, 1 = Error; A = KERNAL error code (if Carry = 1); X/Y = Address of last byte loaded/verified (if Carry = 0).
egisters: A, X, Y.
ddress: $F49E.

### Commented ROM Disassembly (Lee Davison)
outine will load data bytes from any input device directly into the memory
 computer. It can also be used for a verify operation comparing data from a
 with the data already in memory, leaving the data stored in RAM unchanged.

cumulator must be set to 0 for a load operation or 1 for a verify. If the
device was OPENed with a secondary address of 0 the header information from
 will be ignored. In this case XY must contain the starting address for the
If the device was addressed with a secondary address of 1 or 2 the data will
nto memory starting at the location specified by the header. This routine
s the address of the highest RAM location which was loaded.

 this routine can be called, the SETLFS, $FFBA, and SETNAM, $FFBD,
es must be called.

### Cracking The Kernal (Peter Marcotty)
The computer will perform either the LOAD or the VERIFY command. If the accumulator is a 1, then LOAD; if 0, then verify.

oad a program into memory.
   LDA #$08
   LDX #$02
   LDY #$00
   JSR SETLFS
   LDA #$04
   LDX #L,NAME
   LDY #H,NAME
   JSR SETNAM
   LDA #$00
   LDY #$20
   JSR LOAD
   RTS
ME .BY 'FILE'
rogram 'FILE' will be loaded into memory starting at 8192 decimal, X being the low byte and Y being the high byte for the load.

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: JSR at E175/E172 in BASIC's LOAD /VERIFY.

p routines**: SETLFS, SETNAM

y requirements**:
lator should be set to 0 for LOAD; accumulator set to
VERIFY.

ocatable load desired: Set X register to the low byte
d starting address, and Y register to the high byte of load
ng address.

9E/F542 to store the X register and Y register in
the starting address of the load, and then JMP(0330)
 default of F4A5/F549.

5/F549, determine the device. The keyboard,
, and RS-232 are illegal devices.

serial device you must specify a filename. If you
 the MISSING FILE NAME error message is displayed.
 valid filename, the computer commands the current se-
evice to listen and sends the secondary address of $60,
ting a load, followed by the filename. Then it tells the
 to unlisten. Next, it tells the current serial device to
sends the current secondary address of $60, and receives
 from the serial bus. If the I/O status word indicates the
as not returned fast enough, a read time-out has oc-
 and the FILE NOT FOUND error message is displayed.
rst two bytes received from the serial device are used as
ter to the start of the load area (AE). However, if a
ary address of 0 is specified at entry to load, the X and
sters stored in (C3) at entry are used as the starting ad-
of the load—thus providing for a relocatable load. Then
eives bytes from the serial bus and stores or verifies them
the EOI status is received. Once the EOI status is re-
, the serial device is commanded to untalk, and the se-
evice sends the last buffered character. The serial device
s sent a CLOSE and told to untalk.

pe LOAD/VERIFY, the LOAD routine first checks if
pe buffer is located in memory >= 0200. If so, it loads
pe buffer with a header retrieved from the tape. If a file-
as been specified, a specific header with this filename
ded; if there is no filename, it loads the next header on
pe. Only tape headers with tape identifiers of 1 or 3 are
able for LOAD/VERIFY. A tape identifier of 5 indicates
-of-tape header, and in this case the routine will exit
arry set and accumulator set to 5. Tape identifiers of 2 or
for sequential files.

 identifier of 3 causes a nonrelocatable load even if
ve specified values in the X and Y registers at entry and
ndary address of 0. That is, you can't override a tape
fier of 3—it forces a nonrelocatable load.

 identifier of 1 allows a relocatable load. If the tape
fier is 1 and the secondary address is 0, the X and Y reg-
values at entry are used to determine the starting address
e load.

nonrelocatable load, the starting address for the load
en from the tape header. The ending address for the load
th relocatable and nonrelocatable loads) is determined
ing the length of the program to the starting address.
determining whether to do a relocatable or non-
table load, it loads RAM from the next two program
 on tape (two blocks are used for error correcting pur-
 they should be identical copies of each other).

### C64 KERNAL jump table (Frank Kontros)
: A=0 load, a=1 verify               A X Y  A X Y  A X Y
  Y/X = dest.addr if sec.addr=0

### Kernal 64 / 128 (Craig Taylor)
egisters In  : .A = 0 - Load, Non-0 = Verify
               .XY = load address (if secondary address = 0)
egisters Out : .A = error code .C = 1 if error.
               .XY = ending address
emory Changed: As per registers / data file.

### Das neue Commodore-64-intern-Buch (Baloui et al.)
lädt Programm in den Speicher

### Mapping the Commodore 64 (Sheldon Leemon)
utine jumps through a RAM vector at 816 ($330).  LOAD is used to
er data from a device directly to RAM.  It can also be used to
 RAM, comparing its contents to those of a disk or tape file.
ose between these operations you must set the Accumulator with a
LOAD, or a 1 for VERIFY.

the LOAD routine performs an OPEN, it must be preceded by a call
 SETLFS routine to specify the logical file number, device
, and secondary address, and a call to the SETNAM routine to
y the filename (a LOAD from tape can be performed without a
me being specified).  Then the .X and .Y registers should be set
he starting address for the load, and the LOAD routine called.
 secondary address specified was a 1, this starting address will
ored, and the header information will be used to supply the load
s.  If the secondary address was a 0, the address supplied by
ll will be used.  In either case, upon return from the
tine, the .X and .Y registers will contain the address of the
t RAM location that was loaded.

### Machine Language Routines (Todd D Heimarck)
outine loads a program file from tape or disk into a
ied area of memory, or verifies a program file against the
ts of a specified area of memory. A number of prepara-
outines must be called before LOAD: SETLFS, SETNAM,
or the 128 only) SETBNK. See the discussions of those
es for details.

 establishes the device number and secondary ad-
for the operation. The logical file number isn't significant
ading or verifying.) The secondary-address value deter-
whether the load/verify will be absolute or relocating.
 0 of the secondary address is %0 (if the value is 0 or any
umber, for example), a relocating load will be performed:
le will be loaded starting at the address specified in .X
. If the bit is %1 (if the value is 1 or any odd number,
ample), an absolute load will be performed: The data
e loaded starting at the address specified in the file itself.
pe files, the secondary-address specification can be over-
 by the file's internal type specification. Nonrelocatable
rogram files always load at their absolute address,
less of the secondary address.

alling the LOAD routine, the accumulator should
he operation type value (0 for a load, or any nonzero
for a verify). If the secondary address specifies a relocat-
ad, the starting address at which data is to be loaded
 be stored in .X (low byte) and .Y (high byte). The val-
 .X and .Y are irrelevant for an absolute load.

atus-register carry bit will be clear upon return if
le was successfully loaded, or set if an error occurred or if
N/STOP key was pressed to abort the load. When
is set upon return, the accumulator will hold a Kernal er-
de value indicating the problem. Possible error codes in-
4 (file was not found), 5 (device was not present), 8 (no
as specified for a serial load), 9 (an illegal device num-
s specified).

 128 only, the load will be aborted if it extends be-
ddress $FEFF. This prevents corruption of the MMU
uration register at $FFQ0. Ln this case, an error code of
l be returned. The success of the operation will also be
ted by the value in the tape/serial status flag. (See
 for details.)

### Commodore 128 intern (Jörg Schieb et al.)
mit LOADSP eine Datei geladen werden
muß das Gerät, die Sekundäradresse, der Filename etc.
die Routinen SETLFS, SETNAM und SETBNK definiert
 sein. Im X- (Lo) und Y-Register (Hi) wird die Adresse
ben, ab der die zu ladende Datei abgelegt werden soll.

abeparameter**: .X, .Y

piel**:

      ;Laden eines Overlay o.ä.
      JSR PREP  ;SETLFS, SETBNK, SETNAM etc.
      LDX #$00  ;Lo-Byte von $1000
      LDY #$10  ;Hi-Byte von $1000 (Ladeadresse)
      JSR $FFD5 ;Lade Datei ab $1000

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
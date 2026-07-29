---
title: hannel for output
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
- chkin
- chkout
- f34a-open
- jsr
- ldx
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
  address: $FFC9
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'unication registers: X'
  - name: Standard KERNAL Functions
    author: Joe Forster / STA
    description: X = Logical number.
  - name: Commented ROM Disassembly
    author: Lee Davison
    description: gical file that has already been opened by the OPEN routine, $FFC0,
      can be
  - name: Cracking The Kernal
    author: Peter Marcotty
    description: . Just like CHKIN, but it defines the file for output. OPEN must
      be called fi...
  - name: 'COMPUTE!''s Tool Kit: Kernal'
    author: Dan Heeb
    description: 'ed by**: JSR at E4AE/E115 in BASIC''s Set Output Device.'
  - name: C64 KERNAL jump table
    author: Frank Kontros
    description: ': X=logical file number              - X -  - - -  A X -'
  - name: Kernal 64 / 128
    author: Craig Taylor
    description: 'egisters In  : .X = logical file #.'
  - name: Das neue Commodore-64-intern-Buch
    author: Baloui et al.
    description: setzt folgende Ausgabe auf logische die in X übergeben wird. gische
      Datei muß...
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: utine jumps through a RAM vector at 800 ($320).  If you wish to
  - name: Machine Language Routines
    author: Todd D Heimarck
    description: outine (some Commodore references call it CKOUT)
  - name: Commodore 128 intern
    author: Jörg Schieb et al.
    description: echend zu CHKIN definiert diese Routine
---

# $FFC9 — hannel for output ($FFC9)

## Panoramica
La routine KERNAL `None` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FFC9`
- **Chiamata**: `JSR None` o `SYS 65481`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: X
aratory routines: (OPEN)
r returns: 0,3,5,7 (See READST)
k requirements: 4+
sters affected: A, X

scription**: Any logical file number that has been created by the
 routine OPEN can be defined as an output channel. Of course, the
 you intend opening a channel to must be an output device.
ise an error will occur, and the routine will be aborted.

 routine must be called before any data is sent to any output
 unless you want to use the Commodore 64 screen as your output
. If screen output is desired, and there are no other output chan-
lready defined, then calls to this routine, and to the OPEN routine
t needed.

 used to open a channel to a device on the serial bus, this routine
utomatically send the LISTEN address specified by the OPEN routine
 secondary address if there was one).

 to Use:

MBER: this routine is NOT NEEDED to send data to the screen. |
|

 the KERNAL OPEN routine to specify a logical file number, a
TEN address, and a secondary address (if needed).
d the X register with the logical file number used in the open
tement.
l this routine (by using the JSR instruction).

MPLE:

   LDX #3        ;DEFINE LOGICAL FILE 3 AS AN OUTPUT CHANNEL
   JSR CHKOUT

### Standard KERNAL Functions (Joe Forster / STA)
X = Logical number.
: –
egisters: A, X.
ddress: ($0320), $F250.

### Commented ROM Disassembly (Lee Davison)
gical file that has already been opened by the OPEN routine, $FFC0, can be
d as an output channel by this routine the device on the channel must be an
 device or an error will occur and the routine will abort.

 are sending data to anywhere other than the screen this routine must be
 before using the CHROUT routine, $FFD2. if you are sending data to the
 and no other output channels are open then the calls to this routine and to
EN routine, $FFC0, are not needed.

sed with a device on the serial bus this routine will automatically send the
 address specified by the OPEN routine, $FFC0, and any secondary address.

le errors are:

file not open
device not present
file is not an output file

### Cracking The Kernal (Peter Marcotty)
. Just like CHKIN, but it defines the file for output. OPEN must be called first.

efine logical file #4 as an output file.
   LDX #4
   JSR CHKOUT
nce again the X register defines the file #.

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: JSR at E4AE/E115 in BASIC's Set Output Device.

y requirements**: Set X register to logical file number.

320) with default of F250/F309. If the logical file is
 logical file number table, obtain the device number and
ary address for this logical file from the corresponding
s in the device number and secondary address tables. If
gical file is not in the logical file number table, display
LE NOT OPEN message, and return with carry set and
lator set to 3.

 current device is the keyboard, display the NOT
 FILE message, and return with carry set and accu-
r set to 7.

 current device is the screen, just set 9A, the current
 device, to 3, and exit. You do not have to call OPEN
ROUT to display on the screen.

 current device is tape, also check the secondary ad-
 If the secondary address is not $61, display the NOT
 FILE message, and return with carry set and accu-
r set to 7. If the current secondary address is $61, set
1 for tape. Note: OPEN does an ORA $60 of the
ary address.

 current device is a serial device, open the output
l for a serial device. Do this by commanding the cur-
evice to listen. Then for secondary addresses < 128, set
rial attention output line high. If the serial device does
ndshake as expected, display DEVICE NOT PRESENT,
turn with carry set and accumulator set to 5. Otherwise,
 to the serial device number.

 current device is RS-232, then open an RS-232 out-
annel. This routine sets 9A to 2, and then it handles the
 or x-line handshaking sequence.

### C64 KERNAL jump table (Frank Kontros)
: X=logical file number              - X -  - - -  A X -

### Kernal 64 / 128 (Craig Taylor)
egisters In  : .X = logical file #.
egisters Out : .A = error code, .X,.Y destroyed.
               .C = 1 if error
emory Changed: None.

### Das neue Commodore-64-intern-Buch (Baloui et al.)
setzt folgende Ausgabe auf logische die in X übergeben wird. gische Datei muß vorher mit der outine geöffnet werden

### Mapping the Commodore 64 (Sheldon Leemon)
utine jumps through a RAM vector at 800 ($320).  If you wish to
 data to any device other than the screen, this routine must be
 after OPENing the device, and before you output a data byte
he CHROUT routine.  When called, the routine will designate the
l file whose file number is in the .X register as the current
its device as the current device, and its secondary address as
rrent secondary address.  If the device on the channel uses the
 bus, and therefore requires a LISTEN command and possibly a
ary address, this information will be sent on the bus.

### Machine Language Routines (Todd D Heimarck)
outine (some Commodore references call it CKOUT)
ies a logical file as the recipient of output in preparation
ing the CHROUT routine. The logical file should be
 before this routine is called. (See the OPEN routine.)
sired logical file number should be in .X when this rou-
s called. The contents of .Y are unaffected, but the accu-
r will be changed.

utine sets the output channel (location $9A) to the
 number for the specified file. If the device is RS-232
e number 2), the routine also enables the CLA #2 inter-
for RS-232 transmission. If a serial device (device num-
or greater) is specified, the device is also made a listener
 serial bus.

 file is successfully set for output, the status-register
bit will be clear upon return. If the carry is set, the op-
n was unsuccessful, and the accumulator will contain a
 error-code value indicating which error occurred. Pos-
error codes include 3 (file was not open), 5 (device did
spond), and 7 (file was not opened for output). The RS-
d serial status-flag locations also reflect the success of
ions for those devices. (See READST for details.)

P to the CHKOUT execution routine is by way of
KOUT indirect vector at $0320-$0321. You can modify
tions of the routine by changing the vector to point to a
e of your own.

### Commodore 128 intern (Jörg Schieb et al.)
echend zu CHKIN definiert diese Routine
 X-Register zu übergebene Datei als Ausgabedatei. Die
muß ordnungsgemäß geöffnet worden sein, beispielsweise
eine Datei, die mit OPEN 1,8,0,"$" geöffnet wurde und
OUT als Ausgabedatei definiert werden soll, einen
 hervorrufen, weil diese Datei zum Lesen und nicht zum
ben geöffnet wurde. Nach Definition einer Ausgabedatei
cht mehr der Bildschirm, sondern die definierte Datei
egerät. Alle über BSOUT auzugebenen Zeichen werden
ses Gerät gesandt. Das CARRY-Flag dient als Fehlermel-
st es gelöscht, war die Aktion erfolgreich.

abeparameter**: .X

abeparameter**: CARRY

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
---
title: hannel for input
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
  address: $FFC6
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
    description: is used to define any OPENed file as an input file. OPEN must be
      called first.
  - name: 'COMPUTE!''s Tool Kit: Kernal'
    author: Dan Heeb
    description: 'ed by**: JSR at E11E/E11B in BASIC''s Set Input Device.'
  - name: C64 KERNAL jump table
    author: Frank Kontros
    description: ': X=logical file number              - X -  - - -  A X -'
  - name: Kernal 64 / 128
    author: Craig Taylor
    description: 'egisters In  : .X = logical file #.'
  - name: Das neue Commodore-64-intern-Buch
    author: Baloui et al.
    description: setzt folgende Eingabe auf logische die in X übergeben wird. gische
      Datei muß...
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: utine jumps through a RAM vector at 798 ($31E).  If you wish to
  - name: Machine Language Routines
    author: Todd D Heimarck
    description: outine specifies a logical file as the source of input in
  - name: Commodore 128 intern
    author: Jörg Schieb et al.
    description: egister wird die logische Dateinummer
---

# $FFC6 — hannel for input ($FFC6)

## Panoramica
La routine KERNAL `None` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FFC6`
- **Chiamata**: `JSR None` o `SYS 65478`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: X
aratory routines: (OPEN)
r returns: 0,3,5,6 (See READST)
k requirements: None
sters affected: A, X, Y


scription**: Any logical file that has already been opened by the
 OPEN routine can be defined as an input channel by this routine.
lly, the device on the channel must be an input device. Otherwise
or will occur, and the routine will abort.

ou are getting data from anywhere other than the keyboard, this
e must be called before using either the CHRIN or the GETIN KERNAL
es for data input. If you want to use the input from the keyboard,
 other input channels are opened, then the calls to this routine,
 the OPEN routine are not needed.

 this routine is used with a device on the serial bus, it auto-
lly sends the talk address (and the secondary address if one was
ied by the OPEN routine) over the bus.

 to Use:

N the logical file (if necessary; see description above).
d the X register with number of the logical file to be used.
l this routine (using a JSR command).


MPLE:

   ;PREPARE FOR INPUT FROM LOGICAL FILE 2
   LDX #2
   JSR CHKIN

### Standard KERNAL Functions (Joe Forster / STA)
X = Logical number.
: –
egisters: A, X.
ddress: ($031E), $F20E.

### Commented ROM Disassembly (Lee Davison)
gical file that has already been opened by the OPEN routine, $FFC0, can be
d as an input channel by this routine. the device on the channel must be an
device or an error will occur and the routine will abort.

 are getting data from anywhere other than the keyboard, this routine must be
 before using either the CHRIN routine, $FFCF, or the GETIN routine,
 if you are getting data from the keyboard and no other input channels are
hen the calls to this routine and to the OPEN routine, $FFC0, are not needed.

sed with a device on the serial bus this routine will automatically send the
 address specified by the OPEN routine, $FFC0, and any secondary address.

le errors are:

file not open
device not present
file is not an input file

### Cracking The Kernal (Peter Marcotty)
is used to define any OPENed file as an input file. OPEN must be called first.

efine logical file #2 as an input channel.
   LDX #2
   JSR CHKIN
he X register designates which file #.

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: JSR at E11E/E11B in BASIC's Set Input Device.

p routines**: OPEN

y requirements**: The X register should contain the logical file number.

31E) with a default of F20E/F2C7. If the logical file
the logical file number table, the routine obtains the de-
umber and secondary address for this logical file from
rresponding entries in the device number and secondary
s tables. If the logical file is not in the logical file num-
ble, it displays FILE NOT OPEN, and returns with carry
d accumulator set to 3.

 current device is the screen or the keyboard, the
e stores 0 for the keyboard or 3 for the screen in 99, the
on holding the device number of the current input de-
You don't have to use OPEN and CHRIN to input from
yboard.

 current device is the tape, the routine also checks
condary address. If the current secondary address is not
he routine displays the NOT INPUT FILE message, and
s with carry set and accumulator set to 6. If the current
ary address is $60, then location 99 is set to 1 to make
he current input device. OPEN does an ORA $60 of the
ary address.

 current device is a serial device, it opens the input
l by sending a TALK command to the device, and send-
e secondary address if the value for secondary address
n B9 is < 128 (decimal). If the serial device does not re-
 it displays the DEVICE NOT PRESENT error message
turns with carry set and accumulator set to 5. Other-
it stores the serial device number in 99.

 current device is RS-232, the routine opens an RS-
put channel. This RS-232 routine sets the current input
, location 99, to 2 for RS-232, then handles either the 3-
andshaking or the x-line handshaking opening sequence.

### C64 KERNAL jump table (Frank Kontros)
: X=logical file number              - X -  - - -  A X -

### Kernal 64 / 128 (Craig Taylor)
egisters In  : .X = logical file #.
egisters Out : .A = error code, .X,.Y destroyed.
               .C = 1 if error
emory Changed: None.

### Das neue Commodore-64-intern-Buch (Baloui et al.)
setzt folgende Eingabe auf logische die in X übergeben wird. gische Datei muß vorher mit der outine geöffnet werden

### Mapping the Commodore 64 (Sheldon Leemon)
utine jumps through a RAM vector at 798 ($31E).  If you wish to
ta from any device other than the keyboard, this routine must be
 after OPENing the device, before you can get a data byte with
RIN or GETIN routine.  When called, the routine will designate
gical file whose file number is in the .X register as the
t file, its device as the current device, and its secondary
s as the current secondary address.  If the device on the
l is a serial device, which requires a TALK command and
mes a secondary address, this routine will send them over the
 bus.

### Machine Language Routines (Todd D Heimarck)
outine specifies a logical file as the source of input in
ation for using the CHRIN or GETIN routines. The logi-
le should be opened before this routine is called. (See the
outine.) The desired logical file number should be in
n this routine is called. The contents of .Y are un-
ed, but the accumulator value will be changed.

utine sets the input channel (location $99) to the
 number for the specified file. If the device is RS-232
e number 2), the CIA #2 interrupts for RS-232 reception
abled. Ef a serial device (device number 4 or greater) was
ied, the device is made a talker on the serial bus,

 file is successfully set for input, the status-register
bit will be clear upon return. If carry is set, the operation
successful and the accumulator will contain a Kernal
code value indicating which error occurred. Possible er-
des include 3 (file was not open), 5 (device did not re-
, and 6 (file was not opened for input). The RS-232 and
 status-flag locations also reflect the success of operations
ose devices. (See READST for details.)

P to the CEDGN execution routine is by way of the
 indirect vector at 798-799 ($031E-$031F). You can
 the actions of CHfQN by changing the vector to point
outine of your own.

### Commodore 128 intern (Jörg Schieb et al.)
egister wird die logische Dateinummer
ben, die als Eingabekanal benutzt werden soll. Die ange-
 logische Dateinummer muß natürlich bereits mit dem
ommando geöffnet worden sein. Wird nach dem Aufruf
KIN-Kommandos die BASIN-Routine aufgerufen, so
t die Eingabe nicht von Tastatur, sondern von dem
eten Gerät; dies kann beispielsweise die Floppy sein. Zu
en ist, daß zum Einlesen von Tastatur kein CHKIN not-
 ist, da die Tastatur Standard-Eingabegerät ist. Nach
CLOSE oder CLRCH ist die Tastatur automatisch wieder
ngabegerät. Auch bei dieser Routine wird das CARRY als
g benutzt.

abeparameter**: .X

abeparameter**: CARRY

piel**:

      ;Einlesen der Directory
      JSR DIROP ;OPEN 1,8,0,"$" (selbstdefinierte Routine)
      LDX #$01  ;LFN der eröffneten Datei
      JSR $FFC6 ;CHKIN ausführen
      JSR $FFCF ;BASIN - Zeichen holen

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
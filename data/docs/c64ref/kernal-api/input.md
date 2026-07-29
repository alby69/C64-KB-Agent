---
title: character from channel
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
- bne
- chkin
- cmp
- f34a-open
- input
- iny
- jsr
- ldy
- rts
- sta
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
  address: $FFCF
  symbol: Input
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'unication registers: A'
  - name: Standard KERNAL Functions
    author: Joe Forster / STA
    description: –
  - name: Commented ROM Disassembly
    author: Lee Davison
    description: outine will get a byte of data from the channel already set up as
      the input
  - name: Cracking The Kernal
    author: Peter Marcotty
    description: will get a character from the current input device. Calling OPEN
      and CHKIN ca...
  - name: 'COMPUTE!''s Tool Kit: Kernal'
    author: Dan Heeb
    description: 'ed by**: JSR at E112/E10F in BASIC''s Input a Character.'
  - name: C64 KERNAL jump table
    author: Frank Kontros
    description: t:A=character, C=1 and ST=error      - - -  A - -  A - -
  - name: Kernal 64 / 128
    author: Craig Taylor
    description: assette - Returned one character a time from cassette buffer.
  - name: Das neue Commodore-64-intern-Buch
    author: Baloui et al.
    description: Eingabe, holt ein Zeichen in den Akku
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: utine jumps through a RAM vector at 804 ($324).  Its function is
  - name: Machine Language Routines
    author: Todd D Heimarck
    description: igh-level I/O routine (some Commodore references may
  - name: Commodore 128 intern
    author: Jörg Schieb et al.
    description: öffnete und mit CHKIN als Eingabedatei
---

# Input — character from channel ($FFCF)

## Panoramica
La routine KERNAL `Input` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FFCF`
- **Chiamata**: `JSR Input` o `SYS 65487`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: A
aratory routines: (OPEN, CHKIN)
r returns: 0 (See READST)
k requirements: 7+
sters affected: A, X

scription**: This routine gets a byte of data from a channel already
 as the input channel by the KERNAL routine CHKIN. If the CHKIN has
en used to define another input channel, then all your data is
ed from the keyboard. The data byte is returned in the accumulator.
annel remains open after the call.

t from the keyboard is handled in a special way. First, the cursor
ned on, and blinks until a carriage return is typed on the
rd. All characters on the line can be retrieved one at a time
ling this routine once for each character. When the carriage return
rieved, the entire line has been processed. The next time this
e is called, the whole process begins again, i.e., by flashing the
.

 to Use:

OM THE KEYBOARD

rieve a byte of data by calling this routine.
re the data byte.
ck if it is the last data byte (is it a CR?)
not, go to step 1.

MPLE:

   LDY $#00      ;PREPARE THE Y REGISTER TO STORE THE DATA
   JSR CHRIN
   STA DATA,Y    ;STORE THE YTH DATA BYTE IN THE YTH
                 ;LOCATION IN THE DATA AREA.
   INY
   CMP #CR       ;IS IT A CARRIAGE RETURN?
   BNE RD        ;NO, GET ANOTHER DATA BYTE

MPLE:

   JSR CHRIN
   STA DATA

OM OTHER DEVICES

 the KERNAL OPEN and CHKIN routines.
l this routine (using a JSR instruction).
re the data.

MPLE:

   JSR CHRIN
   STA DATA

### Standard KERNAL Functions (Joe Forster / STA)
–
: A = Byte read.
egisters: A, Y.
ddress: ($0324), $F157.

### Commented ROM Disassembly (Lee Davison)
outine will get a byte of data from the channel already set up as the input
l by the CHKIN routine, $FFC6.

IN, $FFC6, has not been used to define another input channel the data is
ed to be from the keyboard. the data byte is returned in the accumulator. the
l remains open after the call.

from the keyboard is handled in a special way. first, the cursor is turned on
 will blink until a carriage return is typed on the keyboard. all characters
 logical line, up to 80 characters, will be stored in the BASIC input buffer.
he characters can be returned one at a time by calling this routine once for
haracter. when the carriage return is returned the entire line has been
sed. the next time this routine is called the whole process begins again.

### Cracking The Kernal (Peter Marcotty)
will get a character from the current input device. Calling OPEN and CHKIN can change the input device.

tore a typed string to the screen.
   LDY #$00
OP JSR CHKIN
   STA $0800,Y
   INY
   CMP #$0D
   BNE LOOP
   RTS
his example is like an INPUT statement. Try running it.

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: JSR at E112/E10F in BASIC's Input a Character.

p routines**: OPEN, CHKIN (not required in retrieving from keyboard).

324) with default of F157/F20E.

 current input device, 99, is tape, then return the
yte from the tape buffer. Also, read one byte ahead to
 the next byte is zero, indicating end of file, and if true,
d-of-file status in 90.

 current input device, 99, is a serial device, the accu-
r returns the byte received over the serial bus. How-
if there are any I/O status errors, return with
lator set to $0D

 current input device, 99, is RS-232, return with the
haracter from the RS-232 receive buffer. However, if the
e buffer is empty, the RS-232 routine on the VIC just
until the receive buffer contains a character. The VIC
ng in an infinite loop if the RS-232 receive buffer never
nother character. If the receive buffer is empty on the 64,
utine returns with $0D in the accumulator.

 current input device is the keyboard, each character
(except for control characters such as the cursor keys) is
yed on the screen until the unshifted RETURN is en-
 Once an unshifted RETURN is typed, reset the input
e to retrieve a character from this screen line. After each
ter is retrieved from the screen line, increment the
r to the character being retrieved in this logical line. The
 POKE code is converted to the equivalent ASCII code,
is returned in the accumulator. If the end of the screen
as been reached, then return $0D, the ASCII code for a
ge return. The screen editor routines limit the size of a
l line to 80/88 characters. The way this CHRIN from the
rd is typically used is to fill a buffer as BASIC does.
calls the CHRIN routine to fill the BASIC input buffer
0. The BASIC routine keeps putting characters in the
 until CHRIN retrieves a carriage return (ASCII $0D).

 current input device, 99, is the screen, then return
CII code for the screen character in the current logical
ointed to by D3, the column the cursor is on. D3 is then
ented to point to the next character in the line. If D3
ached the end of the line, return $0D signifying carriage
, and set D0 to 0 to force the next CHRIN to come from
yboard.

oing CHRIN from the keyboard, the keyboard
e uses this CHRIN from the screen once the carriage re-
as been entered. After processing the screen characters,
reen CHRIN then resets a flag at D0 to 0 to force input
he keyboard for the next CHRIN.

 conditions**: Accumulator holds byte returned from channel.

### C64 KERNAL jump table (Frank Kontros)
t:A=character, C=1 and ST=error      - - -  A - -  A - -

### Kernal 64 / 128 (Craig Taylor)
assette - Returned one character a time from cassette buffer.
s-232   - Return one character at a time, waiting until
          character is ready.
erial   - Returned one character at time, waiting if needed.
creen   - Read from current cursor position.
eyboard - Read characters as a string, then return them
          individually upon each call until all characters
          have been passed ($0d is the EOL).

egisters In  : None.
egisters Out : .A = character or error code, .C = 1 if error.
emory Changed: None.

### Das neue Commodore-64-intern-Buch (Baloui et al.)
Eingabe, holt ein Zeichen in den Akku

### Mapping the Commodore 64 (Sheldon Leemon)
utine jumps through a RAM vector at 804 ($324).  Its function is
 a character from the current input device (whose device number
red at 153 ($99)).  This device must first have been OPENed and
esignated as the input channel by the CHKIN routine.

his routine is called, the next byte of data available from this
 is returned in the Accumulator.  The only exception is the
e for the keyboard device (which is the default input device).
 keyboard is the current input device, this routine blinks the
, fetches characters from the keyboard buffer, and echoes them
 screen until a carriage return is encountered.  When a carriage
 is round, the routine sets a flag to indicate the length of the
ogical line before the return character, and reads the first
ter of this logical line from the screen.

uent calls to this routine will cause the next character in the
o be read from the screen and returned in the Accumulator, until
rriage return character is returned to indicate the end of the
 Any call after this character is received will start the whole
s over again.

hat only the last logical line before the carriage return is
 Any time you type in more than 80 characters, a new logical
s started.  This routine will ignore any characters on the old
l line, and process only the most recent 80-character group.

### Machine Language Routines (Todd D Heimarck)
igh-level I/O routine (some Commodore references may
t BASIN) receives a byte from the logical file currently
ied for input (to change the default input device, see
above). Except to use the routine to retrieve input
he keyboard when the system is set for default I/O, you
pen a logical file to the desired device and specify the
s the input source before calling this routine. (See the
nd CHKIN routines.)

yboard input (device 0), the routine accepts
sses until RETURN is pressed, and then returns charac-
rom the input string one at a time on each subsequent
The character code for RETURN, 13, is returned when the
 an input string is reached. (The Kernal GETIN routine
ter for retrieving individual keypresses.)

pe (device 1), the routine retrieves the next character
he cassette buffer. If all characters have been read from
ffer, the next data block is read from tape into the
.

-232 (device 2), the routine returns the next avail-
haracter from the RS-232 input buffer. If the buffer is
 the routine waits until a character is received—unless
-232 status flag indicates that the DSR signal from the
al device is missing, in which case a RETURN character
13, is returned.

from the screen (device 3) retrieves characters one
ime from the current screen line, ending with a RETURN
ter code when the last nonspace character on the logical
s reached. (Note that CHRIN from the screen does not
roperly in the original version of the 128 Kernal.) For
 devices (device numbers 4 and higher), the routine re-
the next available character from the serial bus, unless
rial status flag contains a nonzero value. In that case, the
 character code is returned.

l input devices, the received byte will be in the
lator upon return. The contents of .X and .Y are pre-
 during input from the keyboard, screen, or RS-232. For
from tape, only .X is preserved. For input from serial de-
 only .Y is preserved. For input from the screen, key-
 or serial devices, the status-register carry bit will always
ar upon return. For tape input, the carry bit will be clear
 the operation was aborted by pressing the RUN/STOP
or tape, serial, or RS-232 input, the success of the opera-
ill be indicated by the value in the status-flag location.
he entry for READST.) The RS-232 portion of the orig-
28 version of CHRRsJ has a bug: The carry bit will be set
yte was successfully received, and will be clear only if
R signal is missing—the opposite of the settings for the
's better to judge the success of an RS-232 operation by
lue in the status-flag location rather than by the carry-
tting. (See the READST routine.)

 to the CHREN execution routine is by way of the
 indirect vector at $0324-$0325. You can modify the
s of the routine by changing the vector to point to a rou-
f your own.

### Commodore 128 intern (Jörg Schieb et al.)
öffnete und mit CHKIN als Eingabedatei
erte Datei (sonst Tastatur) übergibt ein Zeichen im
.

abeparameter**: .A

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
---
title: aracter from keyboard buffer
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
- beq
- chkin
- cmp
- f13e-getin
- f34a-open
- jsr
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
  address: $FFE4
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'unication registers: A'
  - name: Standard KERNAL Functions
    author: Joe Forster / STA
    description: –
  - name: Commented ROM Disassembly
    author: Lee Davison
    description: ctice this routine operates identically to the CHRIN routine, $FFCF,
  - name: Cracking The Kernal
    author: Peter Marcotty
    description: will get one piece of data from the input device. OPEN and CHKIN
      can be used ...
  - name: 'COMPUTE!''s Tool Kit: Kernal'
    author: Dan Heeb
    description: 'ed by**: JSR at E121 in BASIC''s Get a Character.'
  - name: C64 KERNAL jump table
    author: Frank Kontros
    description: t:keyboard:A=0 if puffer empty       - - -  A - -  A X Y
  - name: Kernal 64 / 128
    author: Craig Taylor
    description: Keyboard - Read from keyboard buffer, else return null ($00).
  - name: Das neue Commodore-64-intern-Buch
    author: Baloui et al.
    description: olt ein Zeichen in den Akku
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: utine jumps through a RAM vector at 810 ($32A).
  - name: Machine Language Routines
    author: Todd D Heimarck
    description: outine retrieves a single character from the current input
  - name: Commodore 128 intern
    author: Jörg Schieb et al.
    description: on der definierten Eingabedatei ein
---

# $FFE4 — aracter from keyboard buffer ($FFE4)

## Panoramica
La routine KERNAL `None` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FFE4`
- **Chiamata**: `JSR None` o `SYS 65508`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: A
aratory routines: CHKIN, OPEN
r returns: See READST
k requirements: 7+
sters affected: A (X, Y)

scription**: If the channel is the keyboard, this subroutine removes
aracter from the keyboard queue and returns it as an ASCII value in
cumulator. If the queue is empty, the value returned in the
lator will be zero. Characters are put into the queue automatically
interrupt driven keyboard scan routine which calls the SCNKEY
e. The keyboard buffer can hold up to ten characters. After the
 is filled, additional characters are ignored until at least one
ter has been removed from the queue. If the channel is RS-232, then
he A register is used and a single character is returned. See
 to check validity. If the channel is serial, cassette, or screen,
ASIN routine.


 to Use:

l this routine using a JSR instruction.
ck for a zero in the accumulator (empty buffer).
cess the data.


MPLE:

   ;WAIT FOR A CHARACTER
IT JSR GETIN
   CMP #0
   BEQ WAIT

### Standard KERNAL Functions (Joe Forster / STA)
–
: A = Byte read.
egisters: A, X, Y.
ddress: ($032A), $F13E.

### Commented ROM Disassembly (Lee Davison)
ctice this routine operates identically to the CHRIN routine, $FFCF,
l devices except for the keyboard. If the keyboard is the current input
 this routine will get one character from the keyboard buffer. It depends
 IRQ routine to read the keyboard and put characters into the buffer.

 keyboard buffer is empty the value returned in the accumulator will be zero.

### Cracking The Kernal (Peter Marcotty)
will get one piece of data from the input device. OPEN and CHKIN can be used to change the input device.

ait for a key to be pressed.
IT JSR GETIN
   CMP #0
   BEQ WAIT
f the serial bus is used, then all registers are altered.

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: JSR at E121 in BASIC's Get a Character.

p routines**: OPEN, CHKIN

2A) with a default of F13E/F1F5.

etrieving characters from the keyboard, if any
ters are in the keyboard buffer, the first character (an
value) in the buffer is returned in the accumulator, and
st of the characters are moved up one position in the
. If no characters are in the keyboard buffer, return with
lator cleared to 0.

uld use GETIN to retrieve the first character in the
rd buffer. Contrast this to CHRIN, which does not re-
 anything until RETURN is entered, then returns a
ter from the logical screen line.

rieving from device 2, RS-232, see if the RS-232 re-
buffer contains any characters. If it is empty, return with
lator set to 0. If it contains characters, return with
lator containing next character in the receive buffer and
ent the pointer into the receive buffer.

rieving from channel 3 (the screen), channels >= 4
l devices), or channel 1 (tape), do the same routines for
that CHRIN does for these devices.

reen GETIN, return the ASCII code for the screen
ter in the current logical line pointed to by D3, the col-
e cursor is on. D3 is then incremented to point to the
haracter in the line. If D3 is on the end of the line, re-
he ASCII code $0D for return.

rial GETIN, the accumulator returns the byte re-
 over the serial bus. However, if any I/O status errors
 return with accumulator containing $0D.

pe GETIN, return the next byte from the tape buffer.
read one byte ahead to see if the next byte is zero, in-
ng end of file, and if true, set end-of-file status in 90.

### C64 KERNAL jump table (Frank Kontros)
t:keyboard:A=0 if puffer empty       - - -  A - -  A X Y
  RS232:status byte                  - - -  A - -  A - -
  serial:status byte                 - - -  A - -  A - -
  tape:status byte                   - - -  A - -  A - Y

### Kernal 64 / 128 (Craig Taylor)
Keyboard - Read from keyboard buffer, else return null ($00).
               Rs-232   - Read from Rs-232 buffer, else null is returned.
               Serial   - See BASIN
               Cassette - See BASIN
               Screen   - See BASIN
egisters In  : None.
egisters Out : .A = character, .C = 1 if error.
               .XY = used.
emory Changed: None.

### Das neue Commodore-64-intern-Buch (Baloui et al.)
olt ein Zeichen in den Akku

### Mapping the Commodore 64 (Sheldon Leemon)
utine jumps through a RAM vector at 810 ($32A).
nction is to get a character from the current input device
 device number is stored at 153 ($99)).  In practice, it
es identically to the CHRIN routine below for all devices except
e keyboard.  If the keyboard is the current input device, this
e gets one character from the keyboard buffer at 631 ($277).  It
s on the IRQ interrupt routine to rad the keyboard and put
ters into the buffer.

### Machine Language Routines (Todd D Heimarck)
outine retrieves a single character from the current input
. The routine first checks to see whether the input de-
umber is 0 (keyboard) or 2 (RS-232). If it's not either of
 the Kernal CHRIN routine is called instead. For key-
or RS-232, the retrieved character will be in the accu-
r upon return, and the status-register carry bit wall be
 If no character is available, the accumulator will contain
REM, by contrast, will wait for a character.) The contents
are unaffected, but .X will be changed. For RS-232, bit 3
 status flag will also be set if no characters are available.
EADST for details.)

MP to the GETIN execution routine is by way of the
 indirect vector at $032A-$032B. You can modify the
s of the routine by changing the vector to point to a rou-
f your own.

### Commodore 128 intern (Jörg Schieb et al.)
on der definierten Eingabedatei ein
n. Ist kein Zeichen bereit gestellt, so wird der <Akku>
ll übergeben.

abeparameter**: .A

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
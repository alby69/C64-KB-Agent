---
title: for STOP key
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
- jsr
- rts
- stop
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
  address: $FFE1
  symbol: Check
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'unication registers: A'
  - name: Standard KERNAL Functions
    author: Joe Forster / STA
    description: –
  - name: Commented ROM Disassembly
    author: Lee Davison
    description: STOP key on the keyboard is pressed when this routine is called the
      Z flag
  - name: Cracking The Kernal
    author: Peter Marcotty
    description: ill set the Z flag of the accumulator if the STOP key was pressed.
  - name: 'COMPUTE!''s Tool Kit: Kernal'
    author: Dan Heeb
    description: 'ed by**: JSR at A82C/C82C in BASIC''s Test for STOP Key, JSR at'
  - name: C64 KERNAL jump table
    author: Frank Kontros
    description: t:Z=0 if STOP not used; X unchanged  - - -  A - -  A - -
  - name: Kernal 64 / 128
    author: Craig Taylor
    description: 'egisters In  : None.'
  - name: Das neue Commodore-64-intern-Buch
    author: Baloui et al.
    description: die STOP-Taste ab
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: outine is vectored through RAM at 808 ($328).  The routine checks
      to see
  - name: Machine Language Routines
    author: Todd D Heimarck
    description: outine checks whether the RUN/STOP key is currently
  - name: Commodore 128 intern
    author: Jörg Schieb et al.
    description: is zum letzten IRQ-Aufruf die Stop-Taste
---

# Check — for STOP key ($FFE1)

## Panoramica
La routine KERNAL `Check` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FFE1`
- **Chiamata**: `JSR Check` o `SYS 65505`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: A
aratory routines: None
r returns: None
k requirements: None
sters affected: A, X

scription**: If the <STOP> key on the keyboard was pressed during a
call, this call returns the Z flag set. In addition, the channels
e reset to default values. All other flags remain unchanged. If the
 key is not pressed then the accumulator will contain a byte
enting the lost row of the keyboard scan. The user can also check
rtain other keys this way.

 to Use:
IM should be called before this routine.
l this routine.
t for the zero flag.

MPLE:

   JSR UDTIM   ;SCAN FOR STOP
   JSR STOP
   BNE *+5     ;KEY NOT DOWN
   JMP READY   ;=... STOP

### Standard KERNAL Functions (Joe Forster / STA)
–
: Zero: 0 = Not pressed, 1 = Pressed; Carry: 1 = Pressed.
egisters: A, X.
ddress: ($0328), $F6ED.

### Commented ROM Disassembly (Lee Davison)
STOP key on the keyboard is pressed when this routine is called the Z flag
e set. All other flags remain unchanged. If the STOP key is not pressed then
cumulator will contain a byte representing the last row of the keyboard scan.

er can also check for certain other keys this way.

### Cracking The Kernal (Peter Marcotty)
ill set the Z flag of the accumulator if the STOP key was pressed.

heck for STOP key being pressed.
IT JSR STOP
   BNE WAIT
   RTS
TOP must be called if the STOP key is to remain functional.

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: JSR at A82C/C82C in BASIC's Test for STOP Key, JSR at
590 in Load/Verify from Serial Device, JSR at
6C6 in Save to Serial Device; JSR at F8D0/F94B Test
OP Key During Tape I/O; JSR at FE61/FECD in NMI
upt Handler (to find STOP and RESTORE).

328) with a default of F6ED/F770. At F6ED/F770,
1 for the value $7F/$FE. Location 91 contains the key
 value of the STOP key column (column seven/three) of
yboard scan. If $7E/$FE is found, set the Z flag of the
 register to 1, call FFCC to reset I/O channels, and set
e number of characters in the keyboard buffer, to 0.

/$FE is not found, the Z flag will be 0 on exit (BNE
ion). In this case, the accumulator can still be tested for
ys shown below using the value shown following it.

P Routine Return Values

odore 64 Key | Accumulator | VIC-20 Key  | Accumulator |
-------------|-------------|-------------|-------------|
             | $FE         | Cursor down | $7F         |
 arrow       | $FD         | /           | $BF         |
             | $FB         | ,           | $DF         |
             | $F7         | N           | $EF         |
e            | $EF         | V           | $F7         |
odore        | $DF         | X           | $FB         |
             | $BF         | Left SHIFT  | $FD         |

key is down in the STOP column, the routine returns $FF
 accumulator (64 and VIC).

### C64 KERNAL jump table (Frank Kontros)
t:Z=0 if STOP not used; X unchanged  - - -  A - -  A - -
  Z=1 if STOP used; X changed        - - -  A - -  A X -
  A=last line of keyboard matrix

### Kernal 64 / 128 (Craig Taylor)
egisters In  : None.
egisters Out : .A = last keyboard row, .X = destroyed (if stop key)
emory Changed: None.
ote          : The last keyboard row is as follows:
               .A -> | 7   | 6   | 5   | 4   | 3   | 2   | 1  | 0
                KEY: |STOP |Q    |C=   |SPACE|2    |CTRL |<-  |1

### Das neue Commodore-64-intern-Buch (Baloui et al.)
die STOP-Taste ab

### Mapping the Commodore 64 (Sheldon Leemon)
outine is vectored through RAM at 808 ($328).  The routine checks to see
 STOP key was pressed during the last UDTIM call.  If it was,
ro flag is set to 1, the CLRCHN routine is called to set the
and output devices back to the keyboard and screen, and the
rd queue is emptied.

### Machine Language Routines (Todd D Heimarck)
outine checks whether the RUN/STOP key is currently
d. It returns with the status-register Z bit clear if the key
 pressed, or with the bit set if it is pressed. Additionally,
/STOP is pressed the CLRCH routine is called to re-
default I/O channels, and the count of keys in the key-
buffer is reset to zero.
P to the STOP execution routine is by way of the
indirect vector at $0328-$0329. You can modify the ac-
of the routine by changing the vector to point to a rou-
f your own.

### Commodore 128 intern (Jörg Schieb et al.)
is zum letzten IRQ-Aufruf die Stop-Taste
gt worden ist, so wird das ZERO-Flag gesetzt und es wird
RCH ausgeführt. Wurde die Stop-Taste nicht betätigt, so
as ZERO-Flag gelöscht.

abeparameter**: ZERO-Flag

piel**:

      ;Auf STOP prüfen
      JSR $FFE1  ;STOP-Taste gedrückt?
      BEQ Jawoll ;Ist gedrückt

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
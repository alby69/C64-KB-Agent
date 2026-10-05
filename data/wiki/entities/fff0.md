---
id: fff0
type: entity
title: et X,Y cursor position
aliases:
- et X,Y cursor position
tags:
- jumps
- system-routines
- kernal-api
sources:
- path: data/docs/c64ref/kernal-api/fff0.md
  sha256: bb52b0e10754840a8f9ca7229e54940e413f972707bee27d2b7aa5f535a3fe57
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-fff0
---

# et X,Y cursor position



# $FFF0 — et X,Y cursor position ($FFF0)

## Panoramica
La routine KERNAL `None` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FFF0`
- **Chiamata**: `JSR None` o `SYS 65520`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: A, X, Y
aratory routines: None
r returns: None
k requirements: 2
sters affected: A, X, Y

scription**: A call to this routine with the accumulator carry flag
ads the current position of the cursor on the screen (in X,Y
nates) into the Y and X registers. Y is the column number of the
 location (0-39), and X is the row number of the location of the
 (0-24). A call with the carry bit clear moves the cursor to X,Y
ermined by the Y and X registers.

 to Use:


G CURSOR LOCATION

 the carry flag.
l this routine.
 the X and Y position from the Y and X registers, respectively.


G CURSOR LOCATION

ar carry flag.
 the Y and X registers to the desired cursor location.
l this routine.


MPLE:

OVE THE CURSOR TO ROW 10, COLUMN 5 (5,10)
   LDX #10
   LDY #5
   CLC
   JSR PLOT

### Standard KERNAL Functions (Joe Forster / STA)
Carry: 0 = Restore from input, 1 = Save to output; X = Cursor column (if Carry = 0); Y = Cursor row (if Carry = 0).
: X = Cursor column (if Carry = 1); Y = Cursor row (if Carry = 1).
egisters: X, Y.
ddress: $E50A.

### Commented ROM Disassembly (Lee Davison)
outine, when called with the carry flag set, loads the current position of
rsor on the screen into the X and Y registers. X is the column number of
rsor location and Y is the row number of the cursor. A call with the carry
ear moves the cursor to the position determined by the X and Y registers.

### Cracking The Kernal (Peter Marcotty)
If the carry bit of the accumulator is set, then the cursor X,Y is returned in the Y and X registers. If the carry bit is clear, then the cursor is moved to X,Y as determined by the Y and X registers.

ove cursor to row 12, column 20 (12,20).
   LDX #12
   LDY #20
   CLC
   JSR PLOT
he cursor is now in the middle of the screen.

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: JSR at AAE9/CAE9 in BASIC's Tab to Column for PRINT, JSR
A/CAFA in BASIC'S TAB and SPC, JSR at B39F/D39F
IC'S POS.

y requirements**:
bit should be set or clear, depending on function desired:
rry to read cursor location (X register = row, and Y
er = column).

carry to set cursor location (X register = row, and Y
er = column).

0A (see screen routines in chapter 7).

 carry bit is clear at entry, move the cursor to the
ied location. The contents of the the X register determine
w cursor row and the contents of the Y register deter-
he new cursor column.

 carry bit is set at entry, read the cursor location and
the row value for the current cursor location into the X
er and column value for the current cursor location into
register.

w number indicates the physical line, while the col-
mber indicates the column within a logical line. Valid
al line numbers in decimal are 0-24 (64) and 0-22
 Valid logical column numbers in decimal are 0-79 (64)
87 (VIC).

### C64 KERNAL jump table (Frank Kontros)
: C=0, X=row, Y=column               - X Y  - X Y  - - -
t:C=1, X=row, Y=column               - - -  - X Y  - X Y

### Kernal 64 / 128 (Craig Taylor)
egisters In  : .C = 1 (Read)        |      .C = 0 (Set)
                 None.              |        .X = Col
                                    |        .Y = Row
egisters Out : .C = 1 (Read)        |      .C = 0 (Set)
                 .X = Current Col   |         None.
                 .Y = Current Row   |
emory Changed:  None                |      Screen Editor Locations.

### Das neue Commodore-64-intern-Buch (Baloui et al.)
löschtem Carry-Flag wird der Cursor e Position X/Y gesetzt, bei gesetztem Flag wird die Cursorposition nach X/Y (X-Reg = Zeile, Y-Reg = Spalte)

### Mapping the Commodore 64 (Sheldon Leemon)
utine allows the user to read or set the position of the cursor.
 carry flag is set with the SEC instruction before calling this
tine, cursor column (X position) will be returned in the .X
er, and the cursor row (Y position) will be returned in the .Y
er.  If the carry flag is cleared with a CLC instruction before
ng this routine, and the .Y and .X registers are loaded with the
d row and column positions respectively, this routine will set
rsor position accordingly.

rrent read routine loads .X and .Y from locations 214 ($D6) and
D3) respectively.  The cursor set routine stores .X and .Y in
locations, and calls the routine that sets the screen pointers
32 ($E56C).

er can access this routine from BASIC by loading the .X, .Y, and
ister values desired to the save area starting at 780 ($30C).

### Machine Language Routines (Todd D Heimarck)
outine reads or sets the cursor position on the active dis-
if it is called with the status-register carry bit clear, the
in .X specifies the new cursor row (vertical position),
e value in .Y specifies the column (horizontal position).
rry bit will be set upon return if the specified column or
lues are beyond the right or bottom margins of the cur-
utput window, or it will be clear if the cursor was
sfully positioned.

 routine is called with the carry bit set, the row num-
r the current cursor position is returned in .X and the
t column number is returned in .Y. For the Commodore
he cursor position will be relative to the home position
 current output window rather than to the upper left cor-
 the screen. Of course, in the case of a full-screen output
—the default condition—the upper left comer of the
 is the home position of the window,

### Commodore 128 intern (Jörg Schieb et al.)
h Zustand des CARRY-Flags wird entweder
rsorposition geholt oder gesetzt. X- und Y-Register sind
den Fall die Kommunikationsregister. Das Y-Register
ert die Zeile (Erste Zeile im Fenster ist null) und das X-
er die Spalte des Cursors. Ist das CARRY-Flag gesetzt, so
ie aktuelle Cursorpostion im Fenster in X- und Y-
er zurückgegeben.

abeparameter**: .X, .Y, CARRY

piel**:

      ;Einen Stern (*) in die Fenstermitte setzen
      JSR $FFED ;SCRORG aufrufen
      TXA       ;Spaltenzahl nach <Akku>
      LSR A     ;Divisiondurch zwei (Mitte)
      TAX       ;und als Spalte wieder nach X
      TYA       ;Zeilenzahl nach <Akku>
      LSR A     ;Divisiondurch zwei (Mitte)
      TAY       ;und wieder als Zeile nach Y
      CLC       ;Gelöschtes Carry=Setzen Cursorposition
      JSR $FFF0 ;Setze Cursorposition
      LDA #"*"  ;<Akku> mit Stern laden
      JSR $FFD2 ;und ausgeben.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-fff0]]

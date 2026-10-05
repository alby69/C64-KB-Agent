---
id: return
type: entity
title: X,Y organization of screen
aliases:
- X,Y organization of screen
tags:
- jumps
- system-routines
- kernal-api
sources:
- path: data/docs/c64ref/kernal-api/return.md
  sha256: e97c8da4f46b65ffef202f562cdee9fa023ede65560c491c8da7b41e655cbf80
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-return
---

# X,Y organization of screen



# Return — X,Y organization of screen ($FFED)

## Panoramica
La routine KERNAL `Return` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FFED`
- **Chiamata**: `JSR Return` o `SYS 65517`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: X, Y
aratory routines: None
k requirements: 2
sters affected: X, Y

scription**: This routine returns the format of the screen, e.g., 40
s in X and 25 lines in Y. The routine can be used to determine what
e a program is running on. This function has been implemented on
mmodore 64 to help upward compatibility of your programs.

 to Use:

l this routine.

MPLE:

   JSR SCREEN
   STX MAXCOL
   STY MAXROW

### Standard KERNAL Functions (Joe Forster / STA)
–
: X = Number of columns (40); Y = Number of rows (25).
egisters: X, Y.
ddress: $E505.

### Commented ROM Disassembly (Lee Davison)
outine returns the x,y organisation of the screen in X,Y

### Cracking The Kernal (Peter Marcotty)
returns the number of columns and rows the screen has in the X and Y registers.

etermine the screen size.
   JSR SCREEN
   STX MAXCOL
   STY MAXROW
   RTS
CREEN allows further compatibility between the 64, the VIC-20, and future versions of the 64.

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: None.

05 to return the number of columns on the stan-
isplay screen in the X register and the number of rows
 Y register. On the 64, the routine returns 40 in X and 25
The VIC routine returns 22 in X and 23 in Y.

nitive way to let a program know whether it's run-
n the VIC or the 64 is to JSR to SCREEN and test the
 returned.

### C64 KERNAL jump table (Frank Kontros)
t:X=columns, Y=rows                  - - -  - X Y  - X Y

### Kernal 64 / 128 (Craig Taylor)
egisters In  : None.
egisters Out : .X - Window Row Max
               .Y - Window Col Max
               .A - Screen Col Max (128 only, 64 unchanged)
emory Changed: None

### Das neue Commodore-64-intern-Buch (Baloui et al.)
holt die Anzahl der Zeilen und n des Bildschirms

### Mapping the Commodore 64 (Sheldon Leemon)
alled, this subroutine returns the number of screen columns in
 register, and the number of screen rows in .Y.  Thus, a program
tect the screen format of the machine on which it is running,
ke sure that text output is formatted accordingly.

esent version of this routine loads the .X register with 40
and the .Y register with 25 ($19).

### Machine Language Routines (Todd D Heimarck)
outine (Commodore 128 literature calls it SCRORG) re-
information on the size of the screen display. For the 64,
utine always returns the same values—the screen width
umns (40) in .X and the screen height in rows (25) in .Y.
cumulator is unaffected. For the 128, the values returned
t the size of the current output window. The X register
ontain in the current window the number of columns mi-
e, and .Y will contain the number of rows minus one.
cumulator will hold the maximum column number for
splay currently active (39 for the 40-column screen or 79
e 80-column screen).

### Commodore 128 intern (Jörg Schieb et al.)
utine SCRORG holt die aktuellen
rwerte in die Register. Der <Akku> enthält nach dem
 die maximale Spaltenzahl, im Y-Register befindet sich
zahl der Zeilen im Fenster und im X-Register die Anzahl
alten des Fensters.

abeparameter**: .A, .X, .Y

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-return]]

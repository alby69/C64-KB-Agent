---
id: 0049-forpnt
type: entity
title: Variable pointer for FOR/NEXT
aliases:
- Variable pointer for FOR/NEXT
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0049-forpnt.md
  sha256: 877fd0849056471127e8e341fdcd24c003f4ed2d7bfb16eab52c56cb871fcfa0
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0049-forpnt
---

# Variable pointer for FOR/NEXT



# FORPNT — Variable pointer for FOR/NEXT ($0049)

## Panoramica
Il registro o area di memoria FORPNT è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0049` (`73` decimale)
- **Range**: `$0049`-`$004A`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
A variable's pointer for "FOR" loops and "LET" statements

### Original Source Comments (Microsoft/Commodore)
Pntr to list string

### Original Source Comments (Microsoft/Commodore)
The mask used by WAIT for ANDing

### Commodore-64-intern-Buch (Commodore)
Die Adresse einer Schleifenvariable
wird zunächst hier gespeichert,
bevor sie in den Stack gebracht wird.

### C64 Programmer's Reference Guide (Commodore)
Pointer: Index Variable for FOR/NEXT

### Memory Map (Jim Butterfield)
Variable pointer for FOR/NEXT

### Mapping the Commodore 64 (Sheldon Leemon)
The address of the BASIC variable which is the subject of a FOR/NEXT
loop is first stored here, but is then pushed onto the stack.  That
leaves this location free to be used as a work area by such statements
as INPUT, GET, READ, LIST, WAIT, CLOSE, LOAD, SAVE, RETURN, and GOSUB.

For a description of the stack entries made by FOR, see location 256
($0100).

### Reference (Joe Forster / STA)
Pointer to value of current variable during LET

### Reference (Joe Forster / STA)
Value of second parameter during WAIT. Logical number during CLOSE and CLOSE Device number of LOAD, SAVE and VERIFY

### 64'er Magazin (64'er)
Die Adresse einer Schleifenvariablen wird zuerst hier gespeichert, bevor sie
auf den Stapelspeicher ab Speicherzelle 256 ($0100) gebracht wird. Die Funktion
und Arbeitsweise des Stapelspeichers werden wir bei diesen Adressen behandeln.
Etliche Basic-Befehle, wie LIST, WAIT, GET, INPUT, OPEN, CLOSE und andere,
verwenden die Speicherzellen 73 und 74 für Zwischenspeicherungen. Diese
Adressen sind für den Basic-Programmierer daher nicht verwendbar.

### 64map (—)
Pointer: Index Variable for FOR/NEXT loop

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-0049-forpnt]]

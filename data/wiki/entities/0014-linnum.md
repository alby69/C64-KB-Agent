---
id: 0014-linnum
type: entity
title: Integer value
aliases:
- Integer value
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0014-linnum.md
  sha256: e3770d3f83c23752e1febf1e6a073d650a3ede0b81d6471c806aabe4bb50ee1f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0014-linnum
---

# Integer value



# LINNUM — Integer value ($0014)

## Panoramica
Il registro o area di memoria LINNUM è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0014` (`20` decimale)
- **Range**: `$0014`-`$0015`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
A comma (preload or from ROM)
used by input statement since the
data pointer always starts on a
comma or terminator.

### Original Source Comments (Microsoft/Commodore)
Temporary for input and read code

### Commodore-64-intern-Buch (Commodore)
In dieser Speicherzelle werden die
Zeilennummern von den Befehlen wie
ON..GOTO, GOTO, GOSUB, ON..GOSUB
und der Zeilenausgabe beim
LIST-Befehl gespeichert.

### C64 Programmer's Reference Guide (Commodore)
Temp: Integer Value

### Memory Map (Jim Butterfield)
Integer value

### Mapping the Commodore 64 (Sheldon Leemon)
The target line number for GOTO, LIST, ON, and GOSUB is stored here in
low- byte, high-byte integer format, as is the number of a BASIC line
that is to be added or replaced.

LIST saves the highest line number to list (or 65535 ($FFFF) if
program is to be listed to the end) at this location.

GOTO tests the target line number to see if it is greater than the
line number currently being executed.  If it is greater, GOTO starts
its search for the target line at the current line number.  If it is
not greater, GOTO must search for the target line from the first line
of the program.  It is interesting to note that the test is of the
most significant byte only.  Therefore, INT(TARGETLINE/256) must be
greater than INT(CURRENTLINE/256) in order for the search to start
with the current line, instead of at the beginning of the program.

PEEK, POKE, WAIT, and SYS use this location as a pointer to the
address which is the subject of the command.

### Reference (Joe Forster / STA)
Line number during GOSUB, GOTO and RUN. Second line number during LIST

### Reference (Joe Forster / STA)
Memory address during PEEK, POKE, SYS and WAIT

### 64'er Magazin (64'er)
In diesen Speicherzellen wird die Zeilennummer der Sprungbefehle GOTO, ON..GOTO
und GOSUB sowie die Zeilenangabe beim LIST-Befehl gespeichert. Da die Werte bis
maximal 65535 gehen können, braucht der Computer 2 Byte zur High-/Low-Byte-
Darstellung.

Die GOTO-Routine (im VC 20 ab 51360 = $C8A0, im C 64 ab 43168 = $A8A0)
vergleicht die Zahl in 20 und 21 mit der laufenden Zeilenzahl. Wenn sie kleiner
ist, wird ab der ersten Zeile des Programms gesucht. Ist sie aber größer, dann
beginnt die Suche ab der laufenden Zeilenzahl. Die Suche geht solange, bis die
in 20 und 21 angegebene Zeilenzahl gefunden ist. Dann fährt das Programm mit
dieser Zeile fort.

LIST speichert in 20 und 21 die höchste auszulistende Zeilennummer ab, falls
keine Angabe beim LISTen gegeben worden ist, den Wert 65535 ($FFFF).

Die Befehle PEEK, POKE, SYS und WAIT verwenden diese Speicherzellen zur Angabe
der Adressen, die dem Befehl immer folgen müssen.

Leider können wir die Speicherzellen 20 und 21 mit Basic-Programmen nicht
bearbeiten; ihr Inhalt wird immer gleich auf 20 zurückgesetzt.

### 64map (—)
Temporary: Integer value

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-0014-linnum]]

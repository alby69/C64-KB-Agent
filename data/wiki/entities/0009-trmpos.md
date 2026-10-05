---
id: 0009-trmpos
type: entity
title: TAB column save
aliases:
- TAB column save
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0009-trmpos.md
  sha256: a1bd26cf5309666592b9393da06168311b21a2982c836cbcd203b4c157db994a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0009-trmpos
---

# TAB column save



# TRMPOS — TAB column save ($0009)

## Panoramica
Il registro o area di memoria TRMPOS è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0009` (`9` decimale)
- **Range**: `$0009`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Position of terminal carriage

### Commodore-64-intern-Buch (Commodore)
Nach der Ausführung von TAB oder SPC
wird die Cursorposition in der
Speicherzelle 9 zwischengespeichert.

### C64 Programmer's Reference Guide (Commodore)
Screen Column From Last TAB

### Memory Map (Jim Butterfield)
TAB column save

### Mapping the Commodore 64 (Sheldon Leemon)
TRMPOS is used by TAB and SPC.  The cursor column position prior to
the TAB or SPC is moved here from 211 ($00D3), and is used to calculate
where the cursor ends up after one of these functions is invoked.
Note that the value contained here shows the position of the cursor on
a logical line.  Since one logical line can be up to two physical
lines long, the value stored here can range from 0 to 79.

### Reference (Joe Forster / STA)
Current column number during SPC() and TAB()

### 64'er Magazin (64'er)
Speicherzelle 9 wird von den Basic-Befehlen TAB und SPC verwendet. Vor ihrer
Ausführung wird die Nummer der Spalte, in der sich der Cursor befindet, aus der
Speicherzelle 211 ($00D3) nach 9 gebracht, von wo sie geholt wird, um die Position
des Cursors nach der Ausführung von TAB und SPC auszurechnen.

Diese komplizierte Erklärung können wir durch Ausprobieren deutlicher machen.
Dazu PRINTen wir 16mal den Buchstaben X hintereinander (Semikolon!), allerdings
mit SPC (2) jeweils um 2 Spalten versetzt.

    10 FOR I=0 TO 15
    20 PRINT SPC (2) "X";
    30 PRINT PEEK (9);
    40 NEXT I

Nach jedem X wird durch Zeile 30 die »alte« Cursor-Spaltenposition ausgedruckt
und zwar in derselben Zeile, ausgelöst durch das Semikolon. Dadurch erhöht sich
laufend die in Speicherzelle 9 stehende Positionsangabe des Cursors. Wir
erhalten folgenden Ausdruck:

    ..X.0...X.6...X.12...X.19...X.26...X.33...X.40...X.47.
    ..X.54...X.61...X.68...X.75...X.82...X.1...X.7...X.13

Sie können die Positionsnummer nachrechnen. Berücksichtigen Sie aber dabei, daß
bei PRINT vor und nach jeder Zahl eine Stelle frei bleibt, die erste für das
Vorzeichen, die zweite wegen des Abstandes.

Wichtig ist außerdem, daß die maximal mögliche Spaltenzahl nicht die
Bildschirmspaltenzahl, sondern die »logische« Spaltenzahl ist, also 88 beim VC
20 und 80 beim C 64.

Wir können die Cursorposition in Adresse 9 auch abfragen und ein Programm damit
steuern. Fügen Sie einfach in das obige Programm die folgende Zeile 35 ein:

    35 IF PEEK (9)=33 THEN PRINT "END": END

Sobald Position 33 erreicht ist, bleibt das Programm stehen.

### 64map (—)
Screen Column for last TAB

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-0009-trmpos]]

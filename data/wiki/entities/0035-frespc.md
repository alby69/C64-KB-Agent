---
id: 0035-frespc
type: entity
title: Utility string pointer
aliases:
- Utility string pointer
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0035-frespc.md
  sha256: 1d8e308a72ad1d96ef1ea99679e9f62d27bb60a42cf99f6fba91a7d1684c4e77
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0035-frespc
---

# Utility string pointer



# FRESPC — Utility string pointer ($0035)

## Panoramica
Il registro o area di memoria FRESPC è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0035` (`53` decimale)
- **Range**: `$0035`-`$0036`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Pointer to new string

### Commodore-64-intern-Buch (Commodore)
In diesen Zellen wird die Adresse der
Zeichenkette verzeichnet, die als
letzte von Routinen zur
Stringmanipulation abgespeichert
worden ist.

### C64 Programmer's Reference Guide (Commodore)
Utility String Pointer

### Memory Map (Jim Butterfield)
Utility string pointer

### Mapping the Commodore 64 (Sheldon Leemon)
This is used as a temporary pointer to the most current string added
by the routines which build strings or move them in memory.

### Reference (Joe Forster / STA)
Pointer to memory allocated for current string variable

### 64'er Magazin (64'er)
In diesen Speicherplätzen steht die Adresse (im vierten Block, siehe Bild 5)
der Zeichenkette, die als letzte von Routinen (Programme, Direkteingabe) zur
String-Manipulation abgespeichert worden ist. Mit dem folgenden kleinen
Programm können Sie das genau sehen:

    10 PRINT PEEK(53)+256*PEEK(54),
    20 PRINT PEEK(51)+256*PEEK(52)
    30 INPUT A$
    40 GOTO 10

Zeile 10 druckt uns zuerst (links) den Zeiger auf die zuletzt eingegebene
Zeichenkette aus, Zeile 20 rechts daneben den Zeiger auf die untere
Speichergrenze der Zeichenketten. Zeile 30 fordert zur Eingabe einer
Zeichenkette auf.

Wenn Sie bei frisch eingeschaltetem Computer das Programm starten, sehen Sie
eine 0 (=vorher noch kein String eingeben) und daneben die Adresse dezimal
40960 (C 64) beziehungsweise dezimal 7680 (VC 20 ohne Erweiterung). Wenn Sie
auf das Fragezeichen des INPUT hin zum Beispiel ein A eintippen, erhalten Sie
links den vorigen Wert von rechts und rechts jetzt eine um 1 kleinere Zahl.
Eine weitere Eingabe von zum Beispiel XXXXX schiebt die alte rechte Zahl nach
links und die neue wird um die Anzahl der Zeichen, also 5, verringert.

### 64map (—)
Utility String Pointer

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-0035-frespc]]

---
title: Utility string pointer
source_url: https://github.com/mist64/c64ref/blob/main/src/c64mem/reference.txt
category: reference
topics:
- memory-map
- zero-page
- rom-layout
- zero-page
difficulty: beginner
language: assembly
hardware:
- C64
related: []
scraped_at: '2026-07-29'
c64ref:
  module: c64mem
  source_files:
  - reference.txt
  - original_source_comments.txt
  - commodore-64-intern-buch.txt
  - 64'er_magazin.txt
  - mapping_the_commodore_64.txt
  - memory_map.txt
  - c64_programmer's_reference_guide.txt
  - 64map.txt
  address: $0035
  address_end: $0036
  symbol: FRESPC
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Pointer to new string
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: In diesen Zellen wird die Adresse der
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Utility String Pointer
  - name: Memory Map
    author: Jim Butterfield
    description: Utility string pointer
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This is used as a temporary pointer to the most current string added
  - name: Reference
    author: Joe Forster / STA
    description: Pointer to memory allocated for current string variable
  - name: 64'er Magazin
    author: 64'er
    description: In diesen Speicherplätzen steht die Adresse (im vierten Block, siehe
      Bild 5)
  - name: 64map
    author: —
    description: Utility String Pointer
---

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
---
title: Current Basic line number
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
  address: $0039
  address_end: $003A
  symbol: CURLIN
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Set to 0,255 for direct statements.
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: In diesen Speicherzellen wird die
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Current BASIC Line Number
  - name: Memory Map
    author: Jim Butterfield
    description: Current Basic line number
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This location contains the line number of the BASIC statement which
      is
  - name: Reference
    author: Joe Forster / STA
    description: 'Values:'
  - name: 64'er Magazin
    author: 64'er
    description: Diese Speicherzellen enthalten die Zeilennummer in Low-/High-Byte-Darstellung
  - name: 64map
    author: —
    description: Current BASIC Line number
---

# CURLIN — Current Basic line number ($0039)

## Panoramica
Il registro o area di memoria CURLIN è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0039` (`57` decimale)
- **Range**: `$0039`-`$003A`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Set to 0,255 for direct statements.

### Commodore-64-intern-Buch (Commodore)
In diesen Speicherzellen wird die
Zeilennummer verzeichnet, welche
gerade ausgeführt wird.

### C64 Programmer's Reference Guide (Commodore)
Current BASIC Line Number

### Memory Map (Jim Butterfield)
Current Basic line number

### Mapping the Commodore 64 (Sheldon Leemon)
This location contains the line number of the BASIC statement which is
currently being executed, in LSB/MSB format.  A value of 255 ($FF) in
location 58 ($003A), which translates to a line number of 65280 or above
(well over the 63999 limit for a program line), means that BASIC is
currently in immediate mode, rather than RUN mode.

BASIC keywords that are illegal in direct mode check 58 ($003A) to
determine whether or not this is the current mode.

When in RUN mode, this location is updated as each new BASIC line is
fetched for execution.  Therefore, a TRACE function could be added by
diverting the vector at 776 ($0308), which points to the routine that
executes the next token, to a user-written routine which prints the
line number indicated by this location before jumping to the token
execution routine.  (LISTing the line itself would be somewhat harder,
because LIST uses many Page 0 locations that would have to be
preserved and restored afterwards.)

This line number is used by BREAK and error messages to show where
program execution stopped.  The value here is copied to 59 ($003B) by
STOP, END, and the stop-key BREAK, and copied back by CONT.

### Reference (Joe Forster / STA)
Values:

* $0000-$F9FF, 0-63999: Line number.
* $FF00-$FFFF: Direct mode, no BASIC program is being executed.

### 64'er Magazin (64'er)
Diese Speicherzellen enthalten die Zeilennummer in Low-/High-Byte-Darstellung
derjenigen Basic-Anweisung, welche gerade ausgeführt wird.

Ein kurzes Programm macht das deutlich:

    10 PRINT "ZEILE 10", PEEK(57)+256*PEEK(58)
    20 A=3:PRINT A,PEEK(57)+256*PEEK(58)
    30 B=5:PRINT B,PEEK(57)+256*PEEK(58)
    40 PRINT A*B,PEEK(57)+256*PEEK(58)

In jeder Zeile wird zuerst etwas gePRINTet, nämlich Text, Variable und ein
Rechenresultat. Durch das Komma getrennt wird in der 2. Bildschirmhälfte (VC
20) beziehungsweise Bildschirmviertel (C 64) der Inhalt der Speicherzellen 57
und 58 ausgedruckt. Das Resultat zeigt in der Tat die jeweilige Zeilennummer
an.

Die Basic-Befehle GOTO, GOSUB-RETURN, FOR-NEXT, END, STOP, CONT und die
Betätigung der STOP-Taste während eines Programmlaufes verwenden alle den
Inhalt dieser Speicherzellen, um entweder zu der laufenden Zeile zurückzufinden
oder um die Unterbrechung mit BREAK IN... anzuzeigen. Auch die meisten
Fehlermeldungen verwenden diese Zellen.

In vielen Basic-Erweiterungen und Programmierhilfen wird ein Befehl TRACE oder
STEP angeboten, welcher ein schrittweises Abarbeiten eines Programms bei
gleichzeitiger Anzeige der gerade aktiven Zeilennummer erlaubt. Dieses TRACE
verwendet natürlich auch den Inhalt der Zellen 57 und 58.

Schließlich sei noch erwähnt, daß im direkten Modus, also bei direkt
eingetippten Aktionen des Computers ohne Programmzeilen, in der Zelle 58 immer
die Zahl 255 steht. Diejenigen Basic-Befehle, welche im direkten Modus nicht
erlaubt sind (INPUT, GET, DEF), prüfen in Zelle 58, ob sie im direkten Modus
oder während eines Programmlaufes aufgetreten sind.

### 64map (—)
Current BASIC Line number

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
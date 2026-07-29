---
title: 0 = INPUT; $40 = GET; $98 = READ
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
related:
- input
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
  address: $0011
  symbol: INPFLG
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Flags whether we are doing "INPUT" or "READ"
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Diese Speicherzelle gibt an, in welche
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Flag: $00 = INPUT, $40 = GET, $98 = READ'
  - name: Memory Map
    author: Jim Butterfield
    description: 0 = INPUT; $40 = GET; $98 = READ
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: Since the keywords GET, INPUT, and READ perform similar functions,
  - name: Reference
    author: Joe Forster / STA
    description: 'Values:'
  - name: 64'er Magazin
    author: 64'er
    description: Die Basic-Routinen für INPUT, GET und READ sind zum großen Teil identisch.
      Um
  - name: 64map
    author: —
    description: 'Input Flag: $00 = INPUT, $40 = GET, $98 = READ'
---

# INPFLG — 0 = INPUT; $40 = GET; $98 = READ ($0011)

## Panoramica
Il registro o area di memoria INPFLG è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0011` (`17` decimale)
- **Range**: `$0011`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Flags whether we are doing "INPUT" or "READ"

### Commodore-64-intern-Buch (Commodore)
Diese Speicherzelle gibt an, in welche
Routine der BASIC-Interpreter
verzweigen soll.

### C64 Programmer's Reference Guide (Commodore)
Flag: $00 = INPUT, $40 = GET, $98 = READ

### Memory Map (Jim Butterfield)
0 = INPUT; $40 = GET; $98 = READ

### Mapping the Commodore 64 (Sheldon Leemon)
Since the keywords GET, INPUT, and READ perform similar functions,
BASIC executes some of the same instructions for all three.  There are
also many areas of difference, however, and this flag indicates which
of the three keywords is currently being executed, so that BASIC will
know whether or not to execute the instructions which relate to the
areas in which the commands differ (152 ($98)=READ, 64 ($40)=GET,
0=INPUT).

As a result, INPUT will show the ? prompt, will echo characters back
to the screen, and will wait for a whole line of text ended by a
carriage return.  GET gives no prompt and accepts one character
without waiting.  The colon character and the comma are valid data for
GET, but are treated as delimiters between data by INPUT and READ.

As each command has its own error messages, this flag is used to
determine the appropriate message to issue in case of an error.

### Reference (Joe Forster / STA)
Values:

* $00: INPUT.
* $40: GET.
* $98: READ.

### 64'er Magazin (64'er)
Die Basic-Routinen für INPUT, GET und READ sind zum großen Teil identisch. Um
Speicherplatz zu sparen, verwendet der Basic-Übersetzer die identischen Teile
nur einmal. Um in die nichtidentischen Teile verzweigen zu können, wird in
Zelle 17 angezeigt, um welchen der drei Befehle es sich gerade handelt. Die
Flagge steht auf 0 für INPUT, auf 64 ($40) für GET und auf 152 ($98) für READ.

Mit dem folgenden kleinen Programm können wir das leicht nachprüfen.

    10 DATA 3
    20 READ A
    30 PRINT PEEK (17)
    40 INPUT B
    50 PRINT PEEK (17)
    60 GET C$:IF C$= " "THEN 60
    70 PRINT PEEK (17)

Zeile 10 und 20, 40 sowie 60 sind Anwendungen der drei zur Debatte stehenden
Basic-Befehle. Nach der Durchführung jedes Befehls wird in den Zeilen 30, 50
und 70 die jeweilige Flagge ausgelesen.

Nach RUN erhalten wir als Resultat der Zeile 20 die Zahl 152, als Resultat von
Zeile 30 die INPUT-Aufforderung mit Fragezeichen. Geben Sie irgendeine Zahl und
RETURN ein. Wir erhalten so die 0. Die GET-Schleife in Zeile 40 wartet auf
einen Tastendruck, dann erhalten wir 64.

### 64map (—)
Input Flag: $00 = INPUT, $40 = GET, $98 = READ

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
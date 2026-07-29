---
title: Variable pointer for FOR/NEXT
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
  address: $0049
  address_end: $004A
  symbol: FORPNT
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: A variable's pointer for "FOR" loops and "LET" statements
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Pntr to list string
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: The mask used by WAIT for ANDing
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Die Adresse einer Schleifenvariable
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Pointer: Index Variable for FOR/NEXT'
  - name: Memory Map
    author: Jim Butterfield
    description: Variable pointer for FOR/NEXT
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: The address of the BASIC variable which is the subject of a FOR/NEXT
  - name: Reference
    author: Joe Forster / STA
    description: Pointer to value of current variable during LET
  - name: Reference
    author: Joe Forster / STA
    description: Value of second parameter during WAIT. Logical number during CLOSE
      and CLOSE ...
  - name: 64'er Magazin
    author: 64'er
    description: Die Adresse einer Schleifenvariablen wird zuerst hier gespeichert,
      bevor sie
  - name: 64map
    author: —
    description: 'Pointer: Index Variable for FOR/NEXT loop'
---

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
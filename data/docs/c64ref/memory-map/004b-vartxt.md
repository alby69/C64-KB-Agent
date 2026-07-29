---
title: Y-save; op-save; Basic pointer save
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
  address: $004B
  address_end: $004C
  symbol: VARTXT
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Pointer to current op's entry in "OPTAB"
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Pointer into list of variables
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Diese Speicherzellen dienen als
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Temp Pointer / Data Area
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Temporary storage for TXTPTR during READ, INPUT and GET
  - name: Memory Map
    author: Jim Butterfield
    description: Y-save; op-save; Basic pointer save
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This location is used during the evaluation of mathematical
  - name: Reference
    author: Joe Forster / STA
    description: Temporary area for saving original pointer to current BASIC instruction
      durin...
  - name: 64'er Magazin
    author: 64'er
    description: Während der Auswertung eines mathematischen Ausdrucks durch die Routine
      FRMEVL
  - name: 64map
    author: —
    description: Temporary storage for TXTPTR during READ, INPUT and GET
---

# VARTXT — Y-save; op-save; Basic pointer save ($004B)

## Panoramica
Il registro o area di memoria VARTXT è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$004B` (`75` decimale)
- **Range**: `$004B`-`$004C`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Pointer to current op's entry in "OPTAB"

### Original Source Comments (Microsoft/Commodore)
Pointer into list of variables

### Commodore-64-intern-Buch (Commodore)
Diese Speicherzellen dienen als
Zwischenspeicher für mathematische
Operationen. Außerdem werden die
Speicherzellen auch noch vom
READ-Befehl als Zwischenspeicher
verwendet.

### C64 Programmer's Reference Guide (Commodore)
Temp Pointer / Data Area

### C64 Programmer's Reference Guide (Commodore)
Temporary storage for TXTPTR during READ, INPUT and GET

### Memory Map (Jim Butterfield)
Y-save; op-save; Basic pointer save

### Mapping the Commodore 64 (Sheldon Leemon)
This location is used during the evaluation of mathematical
expressions to hold the displacement of the current math operator in
an operator table.  It is also used as a save area for the pointer to
the address of program text which is currently being read.

### Reference (Joe Forster / STA)
Temporary area for saving original pointer to current BASIC instruction during GET, INPUT and READ

### 64'er Magazin (64'er)
Während der Auswertung eines mathematischen Ausdrucks durch die Routine FRMEVL
des Basic-Übersetzers, wird der Platz des betroffenen mathematischen Operators
in einer Tabelle, hier in 75 und 76, zwischengespeichert. Dieser Platz wird
dabei als Abstand zum Beginn der Tabelle dargestellt. Außerdem verwendet der
READ-Befehl diese Adressen als Zwischenspeicher für einen Programmzeiger. Die
Speicherzeilen 75 und 76 sind in Basic nicht verwendbar.

### 64map (—)
Temporary storage for TXTPTR during READ, INPUT and GET

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
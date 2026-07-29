---
title: Default DIM flag
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
  address: $000C
  symbol: DIMFLG
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: In getting a pointer to a variable
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Diese Speicherzelle wird benutzt, um
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Flag: Default Array Dimension'
  - name: Memory Map
    author: Jim Butterfield
    description: Default DIM flag
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This location is used as a flag by the routines that build an array
      or
  - name: Reference
    author: Joe Forster / STA
    description: 'Values:'
  - name: 64'er Magazin
    author: 64'er
    description: Diese Speicherzelle wird von den Basic-Routinen als Zwischenspeicher
      benutzt,
  - name: 64map
    author: —
    description: 'Flag: Default Array dimension'
---

# DIMFLG — Default DIM flag ($000C)

## Panoramica
Il registro o area di memoria DIMFLG è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$000C` (`12` decimale)
- **Range**: `$000C`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
In getting a pointer to a variable
it is important to remember whether it
is being done for "dim" or not.

DIMFLG and VALTYP must be
consecutive locations.

### Commodore-64-intern-Buch (Commodore)
Diese Speicherzelle wird benutzt, um
festzustellen, ob die Variable ein
Array oder schon eine dimensionierte
Variable ist.

### C64 Programmer's Reference Guide (Commodore)
Flag: Default Array Dimension

### Memory Map (Jim Butterfield)
Default DIM flag

### Mapping the Commodore 64 (Sheldon Leemon)
This location is used as a flag by the routines that build an array or
reference an existing array.  It is used to determine whether a
variable is in an array, whether the array has already been
DIMensioned, and whether a new array should assume the default
dimensions.

### Reference (Joe Forster / STA)
Values:

* $00: Operation was not called by DIM.
* $40-$7F: Operation was called by DIM.

### 64'er Magazin (64'er)
Diese Speicherzelle wird von den Basic-Routinen als Zwischenspeicher benutzt,
die feststellen, ob eine Variable ein Feld (Array) ist, ob das Feld bereits
DIMensioniert worden ist, oder ob ein neues Feld die unDIMensionierte Zahl von
11 Elementen hat.

### 64map (—)
Flag: Default Array dimension

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
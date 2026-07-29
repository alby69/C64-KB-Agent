---
title: Cassette buff len/Series pointer
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
  address: $0071
  address_end: $0072
  symbol: FBUFPT
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Pointer into FBUFFR used by FOUT
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Pointer to buf used by "CRUNCH"
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Pointer to string or desc
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Pointer into polynomial coefficients
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Absolute linear index is formed here
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Hier ist in LOW- und HIGH-Byte
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Pointer: Cassette Buffer'
  - name: Memory Map
    author: Jim Butterfield
    description: Cassette buff len/Series pointer
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This location points to the address of a temporary table of values
  - name: Reference
    author: Joe Forster / STA
    description: Temporary area for saving original pointer to current BASIC instruction
      durin...
  - name: Reference
    author: Joe Forster / STA
    description: Pointer to current item of polynomial table during polynomial evaluation
  - name: Reference
    author: Joe Forster / STA
    description: Auxiliary pointer during array operations
  - name: 64'er Magazin
    author: 64'er
    description: Diese Speicherzellen werden von sehr vielen Routinen des Übersetzers
      und des
  - name: 64map
    author: —
    description: 'Pointer: Used during CRUNCH/ASCII conversion'
---

# FBUFPT — Cassette buff len/Series pointer ($0071)

## Panoramica
Il registro o area di memoria FBUFPT è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0071` (`113` decimale)
- **Range**: `$0071`-`$0072`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Pointer into FBUFFR used by FOUT

### Original Source Comments (Microsoft/Commodore)
Pointer to buf used by "CRUNCH"

### Original Source Comments (Microsoft/Commodore)
Pointer to string or desc

### Original Source Comments (Microsoft/Commodore)
Pointer into polynomial coefficients

### Original Source Comments (Microsoft/Commodore)
Absolute linear index is formed here

### Commodore-64-intern-Buch (Commodore)
Hier ist in LOW- und HIGH-Byte
angegeben, was ausgewertet werden
sol 1.

### C64 Programmer's Reference Guide (Commodore)
Pointer: Cassette Buffer

### Memory Map (Jim Butterfield)
Cassette buff len/Series pointer

### Mapping the Commodore 64 (Sheldon Leemon)
This location points to the address of a temporary table of values
built in the free RAM area for the evaluation of formulas.  It is also
used for such various purposes as a TI$ work area, string setup
pointer, and work space for the evaluation of the size of an array.

Although this is labeled a pointer to the tape buffer in the
Programmer's Reference Guide, disassembly of the BASIC ROM reveals no
reference to this location for that purpose (see 178 ($00B2) for pointer
to tape buffer).

### Reference (Joe Forster / STA)
Temporary area for saving original pointer to current BASIC instruction during VAL()

### Reference (Joe Forster / STA)
Pointer to current item of polynomial table during polynomial evaluation

### Reference (Joe Forster / STA)
Auxiliary pointer during array operations

### 64'er Magazin (64'er)
Diese Speicherzellen werden von sehr vielen Routinen des Übersetzers und des
Betriebssystems, wie zum Beispiel Zeichenkettenverarbeitung, interne Uhr (TI$),
Bestimmung der Größe von Feldern (Arrays) und etlichen anderen verwendet.

### 64map (—)
Pointer: Used during CRUNCH/ASCII conversion

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
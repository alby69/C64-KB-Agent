---
id: 000c-dimflg
type: entity
title: Default DIM flag
aliases:
- Default DIM flag
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/000c-dimflg.md
  sha256: ce58ca6267ba34163e975dedf855a267629db99f225161ca9b3ffb1339dd954e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-000c-dimflg
---

# Default DIM flag



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

## References
- Source: [[src-000c-dimflg]]

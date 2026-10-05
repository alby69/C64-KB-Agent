---
id: 0071-fbufpt
type: entity
title: Cassette buff len/Series pointer
aliases:
- Cassette buff len/Series pointer
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0071-fbufpt.md
  sha256: 573e744818af219be3419e2c7a640edd8e00f0a3b48f14ed8325e23084cc070d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0071-fbufpt
---

# Cassette buff len/Series pointer



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

## References
- Source: [[src-0071-fbufpt]]

---
title: Screen color pointer
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
  address: $00F3
  address_end: $00F4
  symbol: USER
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Screen editor color IP
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Diese Speicherzellen zeigen auf die
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Pointer: Current Screen Color RAM loc'
  - name: Memory Map
    author: Jim Butterfield
    description: Screen color pointer
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This pointer is synchronized with the pointer to the address of the
  - name: Reference
    author: Joe Forster / STA
    description: Pointer to current line in Color RAM
  - name: 64'er Magazin
    author: 64'er
    description: Jedem Platz im Bildschirmspeicher, in dem der Codewert für ein Zeichen
      steht,
  - name: 64map
    author: —
    description: 'Pointer: Current Colour RAM Location'
---

# USER — Screen color pointer ($00F3)

## Panoramica
Il registro o area di memoria USER è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00F3` (`243` decimale)
- **Range**: `$00F3`-`$00F4`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Screen editor color IP

### Commodore-64-intern-Buch (Commodore)
Diese Speicherzellen zeigen auf die
Stelle im Farb-RAM, an der der Cursor
auf der Zeile steht.

### C64 Programmer's Reference Guide (Commodore)
Pointer: Current Screen Color RAM loc

### Memory Map (Jim Butterfield)
Screen color pointer

### Mapping the Commodore 64 (Sheldon Leemon)
This pointer is synchronized with the pointer to the address of the
first byte of screen RAM for the current line kept in location 209
($00D1).  It holds the address of the first byte of color RAM for the
corresponding screen line.

### Reference (Joe Forster / STA)
Pointer to current line in Color RAM

### 64'er Magazin (64'er)
Jedem Platz im Bildschirmspeicher, in dem der Codewert für ein Zeichen steht,
entspricht ein Platz im Farbspeicher, in dem der Codewert für die Farbe dieses
Zeichens steht.

Das heißt, daß den Bildschirm-Werten der Speicherzellen 209 bis 210 die
Farbspeicher-Werte der Zellen 243 bis 244 entsprechen. Dieser Zeiger bestimmt
also in der Low-/High-Byte-Darstellung die Adresse im Farbspeicher, ab der die
echte Zeile beginnt, auf welcher der Cursor gerade steht.

### 64map (—)
Pointer: Current Colour RAM Location

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
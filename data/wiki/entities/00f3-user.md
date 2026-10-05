---
id: 00f3-user
type: entity
title: Screen color pointer
aliases:
- Screen color pointer
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/00f3-user.md
  sha256: 1eba15a05ddaf79a8c3dd1cab0e5bf9beab322ae5d4b72d2e8eb486bb6f6604b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-00f3-user
---

# Screen color pointer



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

## References
- Source: [[src-00f3-user]]

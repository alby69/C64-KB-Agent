---
title: Screen row marker
source_url: https://github.com/mist64/c64ref/blob/main/src/c64mem/reference.txt
category: reference
topics:
- memory-map
- zero-page
- rom-layout
difficulty: intermediate
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
  address: $02A5
  symbol: LINTMP
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Temporary for line index
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Bildschirmzeile
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Temp For Line Index
  - name: Memory Map
    author: Jim Butterfield
    description: Screen row marker
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: Temporary Index to the Next 40-Column Line for Screen Scrolling
  - name: Reference
    author: Joe Forster / STA
    description: Number of line currently being scrolled during scrolling the screen
  - name: 64'er Magazin
    author: 64'er
    description: Das Betriebssystem enthält eine Routine, welche den Bildschirminhalt
  - name: 64map
    author: —
    description: Temporary for Line Index
---

# LINTMP — Screen row marker ($02A5)

## Panoramica
Il registro o area di memoria LINTMP è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$02A5` (`677` decimale)
- **Range**: `$02A5`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Temporary for line index

### Commodore-64-intern-Buch (Commodore)
Bildschirmzeile

### C64 Programmer's Reference Guide (Commodore)
Temp For Line Index

### Memory Map (Jim Butterfield)
Screen row marker

### Mapping the Commodore 64 (Sheldon Leemon)
Temporary Index to the Next 40-Column Line for Screen Scrolling

### Reference (Joe Forster / STA)
Number of line currently being scrolled during scrolling the screen

### 64'er Magazin (64'er)
Das Betriebssystem enthält eine Routine, welche den Bildschirminhalt
hochschiebt (scrollt), sobald eine leere Zeile eingeschoben wird. Das bedeutet,
daß jedesmal die Angaben in den Link-Tabellen der Speicherzellen 217 bis 241
geändert werden müssen. In der Speicherzelle 677 wird nun das Link-Byte
zwischengespeichert, während der obere Teil des Bildschirms hochgeschoben wird.
Beim VC 20 gibt es diese Funktion übrigens auch. Sie wird durch die
Speicherzelle 242 ausgefüllt.

### 64map (—)
Temporary for Line Index

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
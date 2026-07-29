---
title: Color under cursor
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
  address: $0287
  symbol: GDCOL
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Original color before cursor
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: In dieser Speicherzelle merkt sich das
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Background Color Under Cursor
  - name: Memory Map
    author: Jim Butterfield
    description: Color under cursor
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This location is used to keep track of the original color code of
      the
  - name: Reference
    author: Joe Forster / STA
    description: 'Values: $00-$0F, 0-15.'
  - name: 64'er Magazin
    author: 64'er
    description: Das Blinken des Cursors wird dadurch erzeugt, daß das Zeichen auf
      der Stelle
  - name: 64map
    author: —
    description: Background Colour under Cursor
---

# GDCOL — Color under cursor ($0287)

## Panoramica
Il registro o area di memoria GDCOL è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0287` (`647` decimale)
- **Range**: `$0287`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Original color before cursor

### Commodore-64-intern-Buch (Commodore)
In dieser Speicherzelle merkt sich das
Betriebssystem, welche Farbe gerade
unter dem Cursor steht.

### C64 Programmer's Reference Guide (Commodore)
Background Color Under Cursor

### Memory Map (Jim Butterfield)
Color under cursor

### Mapping the Commodore 64 (Sheldon Leemon)
This location is used to keep track of the original color code of the
character stored at the present cursor location.  Since the blinking
cursor uses the current foreground color at 646 ($0286), the original
value must be stored here so that if the cursor moves on without
changing that character, its color code can be restored to its
original value.

### Reference (Joe Forster / STA)
Values: $00-$0F, 0-15.

### 64'er Magazin (64'er)
Das Blinken des Cursors wird dadurch erzeugt, daß das Zeichen auf der Stelle
des Bildschirms, auf der er gerade steht (meistens ist es eine Leerstelle),
dauernd von »normal« auf »revers« (oder »invertiert«) und zurück geschaltet
wird. Die reverse Darstellung benutzt dabei die Farbe des Zeichens.

Genauso, wie sich der Computer in der Speicherzelle 206 das Zeichen merkt, mit
dem er gerade blinkt, um beim Weiterwandern dieses Zeichen in seiner »normalen«
Form auf dem Bildschirm zurückzulassen, merkt er sich die Farbe dieses Zeichens
in der Speicherzelle 647.

### 64map (—)
Background Colour under Cursor

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
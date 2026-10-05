---
id: 0287-gdcol
type: entity
title: Color under cursor
aliases:
- Color under cursor
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0287-gdcol.md
  sha256: 3f6be4c16a89ea514f2324dc77e2283fc317db4d5efcd804bf2a74294a34cc90
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0287-gdcol
---

# Color under cursor



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

## References
- Source: [[src-0287-gdcol]]

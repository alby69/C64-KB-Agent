---
id: 02a5-lintmp
type: entity
title: Screen row marker
aliases:
- Screen row marker
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/02a5-lintmp.md
  sha256: e08b2b5188265acfa15e4013089a330c4ec9e1f0b5053fd7d54b959b78fa35ad
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-02a5-lintmp
---

# Screen row marker



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

## References
- Source: [[src-02a5-lintmp]]

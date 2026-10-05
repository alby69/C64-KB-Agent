---
id: 0033-fretop
type: entity
title: 'Pointer : String-storage(moving down)'
aliases:
- 'Pointer : String-storage(moving down)'
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0033-fretop.md
  sha256: be449c0fd78d4e7ea54c8342722330a13b2237704779c5ac7dcd4f464ab6ba57
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0033-fretop
---

# Pointer : String-storage(moving down)



# FRETOP — Pointer : String-storage(moving down) ($0033)

## Panoramica
Il registro o area di memoria FRETOP è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0033` (`51` decimale)
- **Range**: `$0033`-`$0034`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Top of string free space

### Commodore-64-intern-Buch (Commodore)
Der Inhalt dieser Speicherzellen
zeigt auf das Ende des Textspeichers,
der aber noch zugleich das obere Ende
des frei verfügbaren RAM-Bereichs
anzeigt.

### C64 Programmer's Reference Guide (Commodore)
Pointer: Bottom of String Storage

### Memory Map (Jim Butterfield)
Pointer : String-storage(moving down)

### Mapping the Commodore 64 (Sheldon Leemon)
This pointer marks the current end of the string text area, and the
top of free RAM (strings are built from the top of memory downward).
Additional string texts are added, to the area below the address
pointed to here.  After they are added, this pointer is lowered to
point below the newly added string text.  The garbage collection
routine (which is also called by FRE) readjusts this pointer upward.

While the power-on/reset routines set this pointer to the top of RAM,
the CLR command sets this pointer to the end of BASIC memory, as
indicated in location 55 ($0037).  This allows the user to set aside an
area of BASIC memory that will not be disturbed by the program, as
detailed at location 55 ($0037).

### Reference (Joe Forster / STA)
(Grows downwards from end of BASIC area.)

### 64'er Magazin (64'er)
Der Inhalt dieser Speicherzellen zeigt in Low-/High-Byte-Darstellung auf das
jeweilige untere Ende (siehe Bild 5) des Textspeichers von Zeichenketten. Er
bezeichnet aber zugleich auch das obere Ende des frei verfügbaren RAM-Bereichs.
Das entsteht dadurch, daß der Text der Zeichenketten vom Ende des RAM-Bereichs
nach unten gespeichert wird. In Bild 5 ist das durch den Pfeil dargestellt.

Beim Einschalten des Computers und nach einem RESET wird dieser Zeiger auf das
oberste Ende des RAM-Bereichs gesetzt. Beim C 64 ist das 40960 ($A000). Beim VC
20 hängt es von den eingesetzten Speichererweiterungen ab, ohne Erweiterung ist
die Adresse 7680 ($1E00).

Der Befehl CLR setzt den Zeiger auf die Adresse, welche durch den Zeiger in den
Speicherzellen 55 und 56 als das Ende des Basic-Speichers angegeben wird. Wozu
das dient, erkläre ich Ihnen bei der Beschreibung dieses Zeigers weiter unten.

### 64map (—)
Pointer: Bottom of String space

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-0033-fretop]]

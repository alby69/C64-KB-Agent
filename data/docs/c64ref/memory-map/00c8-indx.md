---
title: End-of-line for input pointer
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
  address: $00C8
  symbol: INDX
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: ''
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Dieses Register enthält die Position
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Pointer: End of Logical Line for INPUT'
  - name: Memory Map
    author: Jim Butterfield
    description: End-of-line for input pointer
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This pointer indicates the column number of the last nonblank
  - name: Reference
    author: Joe Forster / STA
    description: 'Length of line minus 1 during screen input. Values: $27, 39; $4F,
      79'
  - name: 64'er Magazin
    author: 64'er
    description: Eine echte Zeile faßt beim C 64 maximal 40 Zeichen, beim VC 20 nur
      22.
  - name: 64map
    author: —
    description: 'Pointer: End of Line for Input (Used to suppress trailing spaces)'
---

# INDX — End-of-line for input pointer ($00C8)

## Panoramica
Il registro o area di memoria INDX è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00C8` (`200` decimale)
- **Range**: `$00C8`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)


### Commodore-64-intern-Buch (Commodore)
Dieses Register enthält die Position
des letzen Zeichens in einer Zeile.

### C64 Programmer's Reference Guide (Commodore)
Pointer: End of Logical Line for INPUT

### Memory Map (Jim Butterfield)
End-of-line for input pointer

### Mapping the Commodore 64 (Sheldon Leemon)
This pointer indicates the column number of the last nonblank
character on the logical line that is to be input.  Since a logical
line can be up to 80 characters long, this number can range from 0-79.

### Reference (Joe Forster / STA)
Length of line minus 1 during screen input. Values: $27, 39; $4F, 79

### 64'er Magazin (64'er)
Eine echte Zeile faßt beim C 64 maximal 40 Zeichen, beim VC 20 nur 22.

Eine Zeile mit Anweisungen darf beim C 64 insgesamt 80 Zeichen, beim VC 20
sogar 88 Zeichen enthalten. Diese »verlängerte« Programmzeile nennt man
»logische Zeile«.

Der Zeiger in Speicherzelle 200 gibt dem Betriebssystem an, auf welcher
Position das letzte Zeichen einer eingegebenen logischen Zeile sitzt. Löschen
Sie den Bildschirm und geben Sie direkt irgendwo auf dem Bildschirm den Befehl
ein:

    PRINT PEEK(200)

Sie erhalten die Zahl der Spalte des letzten Zeichens dieses Direkt-Befehls.

### 64map (—)
Pointer: End of Line for Input (Used to suppress trailing spaces)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
---
title: Current screen line length
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
  address: $00D5
  symbol: LNMX
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: 40/80 max position
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Der Inhalt dieser Speicherzelle
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Physical Screen Line Length
  - name: Memory Map
    author: Jim Butterfield
    description: Current screen line length
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: The line editor uses this location when the end of a line has been
  - name: Reference
    author: Joe Forster / STA
    description: 'Length of current screen line minus 1. Values: $27, 39; $4F, 79'
  - name: 64'er Magazin
    author: 64'er
    description: Im Texteinschub 23 »Logische und echte Zeilen« ist der Unterschied
      zwischen den
  - name: 64map
    author: —
    description: 'Current logical Line length: 39 or 79'
---

# LNMX — Current screen line length ($00D5)

## Panoramica
Il registro o area di memoria LNMX è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00D5` (`213` decimale)
- **Range**: `$00D5`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
40/80 max position

### Commodore-64-intern-Buch (Commodore)
Der Inhalt dieser Speicherzelle
entscheidet, ob eine neue Zeile
angefangen werden muß oder nicht.

### C64 Programmer's Reference Guide (Commodore)
Physical Screen Line Length

### Memory Map (Jim Butterfield)
Current screen line length

### Mapping the Commodore 64 (Sheldon Leemon)
The line editor uses this location when the end of a line has been
reached to determine whether another physical line can be added to the
current logical line, or if a new logical line must be started.

### Reference (Joe Forster / STA)
Length of current screen line minus 1. Values: $27, 39; $4F, 79

### 64'er Magazin (64'er)
Im Texteinschub 23 »Logische und echte Zeilen« ist der Unterschied zwischen den
beiden Zeilentypen beschrieben.

Der Inhalt dieser Speicherzelle entscheidet, wann eine neue logische Zeile
begonnen werden muß oder ob die laufende logische Zeile um eine weitere echte
Zeile erweitert werden kann. Der Bildschirm-Editor verwendet diese
Speicherzelle, um komplette logische Zeilen nach oben zu verschieben. Einige
andere Routinen benutzen den Wert der Zelle bei der Rückwärtsüberprüfung einer
Zeile, bei der die Endposition der Zeile bekannt sein muß. Schließlich bezieht
noch die bereits behandelte Speicherzelle 200 Ihren Wert von der Zelle 213.

### 64map (—)
Current logical Line length: 39 or 79

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
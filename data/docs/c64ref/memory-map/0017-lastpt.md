---
title: Last temp string vector
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
  address: $0017
  address_end: $0018
  symbol: LASTPT
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Pointer to last-used string temporary
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Der Inhalt dieser beiden Bytes zeigt
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Last Temp String Address
  - name: Memory Map
    author: Jim Butterfield
    description: Last temp string vector
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This pointer indicates the last slot used in the temporary string
  - name: Reference
    author: Joe Forster / STA
    description: Pointer to previous expression in string stack
  - name: 64'er Magazin
    author: 64'er
    description: Der Inhalt dieser 2 Byte zeigt auf den zuletzt benutzten Speicherplatz
  - name: 64map
    author: —
    description: Last temporary String Address
---

# LASTPT — Last temp string vector ($0017)

## Panoramica
Il registro o area di memoria LASTPT è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0017` (`23` decimale)
- **Range**: `$0017`-`$0018`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Pointer to last-used string temporary

### Commodore-64-intern-Buch (Commodore)
Der Inhalt dieser beiden Bytes zeigt
auf den zuletzt verwendeten
Speicherplatz.

### C64 Programmer's Reference Guide (Commodore)
Last Temp String Address

### Memory Map (Jim Butterfield)
Last temp string vector

### Mapping the Commodore 64 (Sheldon Leemon)
This pointer indicates the last slot used in the temporary string
descriptor stack.  Therefore, the value stored at 23 ($0017) should be 3
less than that stored at 22 ($0016), while 24 ($0018) will contain a 0.

### Reference (Joe Forster / STA)
Pointer to previous expression in string stack

### 64'er Magazin (64'er)
Der Inhalt dieser 2 Byte zeigt auf den zuletzt benutzten Speicherplatz
Innerhalb der Adresse 22 bis 33. Das heißt, daß der Wert in 23 ($0017) immer um 3
kleiner ist als der in 22 ($0016), während der Wert in 24 ($0018) eine Null ist.

### 64map (—)
Last temporary String Address

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
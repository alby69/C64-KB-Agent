---
title: Utility pointer area
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
  address: $0022
  address_end: $0025
  symbol: INDEX
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Indexes
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: ''
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Diese Speicherzellen benutzt der
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Utility Pointer Area
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: First Utility Pointer
  - name: Memory Map
    author: Jim Butterfield
    description: Utility pointer area
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This area is used by many BASIC routines to hold temporary pointers
  - name: Reference
    author: Joe Forster / STA
    description: Temporary area for various operations (4 bytes)
  - name: 64'er Magazin
    author: 64'er
    description: Diese vier Speicherzellen werden vom Basic-Übersetzer (Interpreter)
      für
  - name: 64map
    author: —
    description: Utility Pointer Area
  - name: 64map
    author: —
    description: First Utility Pointer
---

# INDEX — Utility pointer area ($0022)

## Panoramica
Il registro o area di memoria INDEX è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0022` (`34` decimale)
- **Range**: `$0022`-`$0025`
- **Dimensione**: `4 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Indexes

### Original Source Comments (Microsoft/Commodore)


### Commodore-64-intern-Buch (Commodore)
Diese Speicherzellen benutzt der
Interpreter, um verschiedene
Zwischenergebnisse zu speichern.

### C64 Programmer's Reference Guide (Commodore)
Utility Pointer Area

### C64 Programmer's Reference Guide (Commodore)
First Utility Pointer

### Memory Map (Jim Butterfield)
Utility pointer area

### Mapping the Commodore 64 (Sheldon Leemon)
This area is used by many BASIC routines to hold temporary pointers
and calculation results.

### Reference (Joe Forster / STA)
Temporary area for various operations (4 bytes)

### 64'er Magazin (64'er)
Diese vier Speicherzellen werden vom Basic-Übersetzer (Interpreter) für
verschiedene Zwischenergebnisse und Flaggen benutzt, die aber dem Programmierer
nichts nutzen.

### 64map (—)
Utility Pointer Area

### 64map (—)
First Utility Pointer

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
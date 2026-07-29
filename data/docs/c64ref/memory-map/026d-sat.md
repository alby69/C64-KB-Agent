---
title: Sec Adds table
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
  - mapping_the_commodore_64.txt
  - memory_map.txt
  - c64_programmer's_reference_guide.txt
  - 64map.txt
  address: $026D
  address_end: $0276
  symbol: SAT
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Secondary addresses
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Diese Tabelle entspricht $0259-$0262,
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'KERNAL Table: Second Address Each File'
  - name: Memory Map
    author: Jim Butterfield
    description: Sec Adds table
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: Kernal Table of Secondary Addresses for Each Logical File
  - name: Reference
    author: Joe Forster / STA
    description: Secondary addresses assigned to files (10 bytes, 10 entries)
  - name: 64map
    author: —
    description: 'Kernal Table: Active File Secondary Addresses'
---

# SAT — Sec Adds table ($026D)

## Panoramica
Il registro o area di memoria SAT è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$026D` (`621` decimale)
- **Range**: `$026D`-`$0276`
- **Dimensione**: `10 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Secondary addresses

### Commodore-64-intern-Buch (Commodore)
Diese Tabelle entspricht $0259-$0262,
nur mit dem Unterschied, daß hier die
Sekundäradressen vermerkt werden.

### C64 Programmer's Reference Guide (Commodore)
KERNAL Table: Second Address Each File

### Memory Map (Jim Butterfield)
Sec Adds table

### Mapping the Commodore 64 (Sheldon Leemon)
Kernal Table of Secondary Addresses for Each Logical File

### Reference (Joe Forster / STA)
Secondary addresses assigned to files (10 bytes, 10 entries)

### 64map (—)
Kernal Table: Active File Secondary Addresses

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
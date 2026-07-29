---
title: 'Accum#l : Sign'
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
  - mapping_the_commodore_64.txt
  - memory_map.txt
  - c64_programmer's_reference_guide.txt
  - 64map.txt
  address: $0066
  symbol: FACSGN
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Sign of FAC (0 or -1) when unpacked
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Der Zeiger gibt an, ob der Wert, der
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Floating Accum. #1: Sign'
  - name: Memory Map
    author: Jim Butterfield
    description: 'Accum#l : Sign'
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: A value of 0 here indicates a positive number, while a value of 255
  - name: Reference
    author: Joe Forster / STA
    description: 'Bits:'
  - name: 64map
    author: —
    description: FAC Sign
---

# FACSGN — Accum#l : Sign ($0066)

## Panoramica
Il registro o area di memoria FACSGN è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0066` (`102` decimale)
- **Range**: `$0066`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Sign of FAC (0 or -1) when unpacked

### Commodore-64-intern-Buch (Commodore)
Der Zeiger gibt an, ob der Wert, der
im FAC steht, positiv oder negativ
ist.

### C64 Programmer's Reference Guide (Commodore)
Floating Accum. #1: Sign

### Memory Map (Jim Butterfield)
Accum#l : Sign

### Mapping the Commodore 64 (Sheldon Leemon)
A value of 0 here indicates a positive number, while a value of 255
($FF) indicates a negative number.

### Reference (Joe Forster / STA)
Bits:

* Bit #7: 0 = Positive; 1 = Negative.

### 64map (—)
FAC Sign

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
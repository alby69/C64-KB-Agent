---
title: Vorzeichen von ARG
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
related:
- 0069-arg
scraped_at: '2026-07-29'
c64ref:
  module: c64mem
  source_files:
  - reference.txt
  - original_source_comments.txt
  - commodore-64-intern-buch.txt
  - mapping_the_commodore_64.txt
  - c64_programmer's_reference_guide.txt
  - 64map.txt
  address: $006E
  symbol: ARGSGN
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: ''
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Hier wird angegeben, ob der Wert, der
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Floating Accum. #2: Sign'
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: 'Floating Point Accumulator #2: Sign'
  - name: Reference
    author: Joe Forster / STA
    description: 'Bits:'
  - name: 64map
    author: —
    description: AFAC Sign
---

# ARGSGN — Vorzeichen von ARG ($006E)

## Panoramica
Il registro o area di memoria ARGSGN è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$006E` (`110` decimale)
- **Range**: `$006E`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)


### Commodore-64-intern-Buch (Commodore)
Hier wird angegeben, ob der Wert, der
im ARG steht, positiv oder negativ ist.

### C64 Programmer's Reference Guide (Commodore)
Floating Accum. #2: Sign

### Mapping the Commodore 64 (Sheldon Leemon)
Floating Point Accumulator #2: Sign

### Reference (Joe Forster / STA)
Bits:

* Bit #7: 0 = Positive; 1 = Negative.

### 64map (—)
AFAC Sign

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
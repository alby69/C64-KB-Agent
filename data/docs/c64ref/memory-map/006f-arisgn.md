---
title: 'Sign comparison, Acc#l vs #2'
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
  address: $006F
  symbol: ARISGN
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: A sign reflecting the result
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Pointer to a string or descriptor
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Diese Speicherzelle gibt dem
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Sign Comparison Result: Accum. # 1 vs #2'
  - name: Memory Map
    author: Jim Butterfield
    description: 'Sign comparison, Acc#l vs #2'
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: Used to indicate whether the two Floating Point Accumulators have
      like
  - name: Reference
    author: Joe Forster / STA
    description: Pointer to first string expression during string comparison
  - name: 64'er Magazin
    author: 64'er
    description: Wenn die Zahl in beiden Akkumulatoren gleiche Vorzeichen hat, steht
      in
  - name: 64map
    author: —
    description: Sign of result of Arithmetic Evaluation
---

# ARISGN — Sign comparison, Acc#l vs #2 ($006F)

## Panoramica
Il registro o area di memoria ARISGN è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$006F` (`111` decimale)
- **Range**: `$006F`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
A sign reflecting the result

### Original Source Comments (Microsoft/Commodore)
Pointer to a string or descriptor

### Commodore-64-intern-Buch (Commodore)
Diese Speicherzelle gibt dem
Interpreter an, ob die Vorzeichen der
beiden Akkus übereinstimmen.

### C64 Programmer's Reference Guide (Commodore)
Sign Comparison Result: Accum. # 1 vs #2

### Memory Map (Jim Butterfield)
Sign comparison, Acc#l vs #2

### Mapping the Commodore 64 (Sheldon Leemon)
Used to indicate whether the two Floating Point Accumulators have like
or unlike signs.  A 0 indicates like signs, a 255 ($FF) indicates
unlike signs.

### Reference (Joe Forster / STA)
Pointer to first string expression during string comparison

### 64'er Magazin (64'er)
Wenn die Zahl in beiden Akkumulatoren gleiche Vorzeichen hat, steht in
Speicherzelle 111 eine 0, bei verschiedenen Vorzeichen eine 255.

### 64map (—)
Sign of result of Arithmetic Evaluation

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
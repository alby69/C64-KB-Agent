---
title: 'Accum#l : Mantissa'
source_url: https://github.com/mist64/c64ref/blob/main/src/c64mem/original_source_comments.txt
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
  - original_source_comments.txt
  - mapping_the_commodore_64.txt
  - memory_map.txt
  - c64_programmer's_reference_guide.txt
  - 64map.txt
  address: $0062
  address_end: $0065
  symbol: FACHO
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Most significant byte of mantissa
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Floating Accum. #1: Mantissa'
  - name: Memory Map
    author: Jim Butterfield
    description: 'Accum#l : Mantissa'
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: The most significant digit can be assumed to be a 1 (remember that
      the
  - name: 64map
    author: —
    description: FAC Mantissa
---

# FACHO — Accum#l : Mantissa ($0062)

## Panoramica
Il registro o area di memoria FACHO è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0062` (`98` decimale)
- **Range**: `$0062`-`$0065`
- **Dimensione**: `4 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Most significant byte of mantissa

### C64 Programmer's Reference Guide (Commodore)
Floating Accum. #1: Mantissa

### Memory Map (Jim Butterfield)
Accum#l : Mantissa

### Mapping the Commodore 64 (Sheldon Leemon)
The most significant digit can be assumed to be a 1 (remember that the
range of the mantissa is from 1 to 1.99999...) when a floating point
number is stored to a variable.  The first bit is used for the sign of
the number, and the other 31 bits of the four-byte mantissa hold the
other significant digits.

The first two bytes (98-99, $0062-$0063) of this location will hold the
signed integer result of a floating point to integer conversion, in
high-byte, low- byte order.

### 64map (—)
FAC Mantissa

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
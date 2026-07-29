---
title: Accum#l lo-order (rounding)
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
  - commodore-64-intern-buch.txt
  - 64'er_magazin.txt
  - mapping_the_commodore_64.txt
  - memory_map.txt
  - c64_programmer's_reference_guide.txt
  - 64map.txt
  address: $0070
  symbol: FACOV
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Overflow byte of the FAC
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: FAC-Rundungsbyte
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Floating Accum. #1. Low-Order (Rounding)'
  - name: Memory Map
    author: Jim Butterfield
    description: Accum#l lo-order (rounding)
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: If the mantissa of the floating point number has more significant
  - name: 64'er Magazin
    author: 64'er
    description: Es kann vorkommen, daß die Mantisse einer Gleitkommazahl mehr Stellen
      hat, als
  - name: 64map
    author: —
    description: FAC low-order rounding
---

# FACOV — Accum#l lo-order (rounding) ($0070)

## Panoramica
Il registro o area di memoria FACOV è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0070` (`112` decimale)
- **Range**: `$0070`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Overflow byte of the FAC

### Commodore-64-intern-Buch (Commodore)
FAC-Rundungsbyte

### C64 Programmer's Reference Guide (Commodore)
Floating Accum. #1. Low-Order (Rounding)

### Memory Map (Jim Butterfield)
Accum#l lo-order (rounding)

### Mapping the Commodore 64 (Sheldon Leemon)
If the mantissa of the floating point number has more significant
figures than can be held in four bytes, the least significant figures
are placed here.  They are used to extend the accuracy of intermediate
mathematical operations and to round to the final figure.

### 64'er Magazin (64'er)
Es kann vorkommen, daß die Mantisse einer Gleitkommazahl mehr Stellen hat, als
mit den vier Mantissen-Bytes des Akkumulators Nr. 1 (Zelle 97 bis 102)
dargestellt werden können. In diesem Fall werden die hintersten, das heißt die
unwichtigsten Stellen hinter dem Komma in der Zelle 112 abgelegt. Von dort
werden sie geholt, um die Genauigkeit von mathematischen Operationen zu erhöhen
und auch um Endresultate abrunden zu können.

### 64map (—)
FAC low-order rounding

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
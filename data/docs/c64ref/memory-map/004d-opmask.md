---
title: Comparison symbol accumulator
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
  address: $004D
  symbol: OPMASK
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Mask created by current operator
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Dieser Zeiger wird von mathematischen
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Mask used during FRMEVL
  - name: Memory Map
    author: Jim Butterfield
    description: Comparison symbol accumulator
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: The expression evaluation routine creates a mask here which lets
      it
  - name: Reference
    author: Joe Forster / STA
    description: 'Bits:'
  - name: 64'er Magazin
    author: 64'er
    description: Die bei 75 und 76 schon erwähnte Auswertungs-Routine FRMEVL erzeugt
      in der
  - name: 64map
    author: —
    description: Mask used during FRMEVL
---

# OPMASK — Comparison symbol accumulator ($004D)

## Panoramica
Il registro o area di memoria OPMASK è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$004D` (`77` decimale)
- **Range**: `$004D`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Mask created by current operator

### Commodore-64-intern-Buch (Commodore)
Dieser Zeiger wird von mathematischen
Routinen als Vergleichsoperator
verwendet, daß heißt um festzustellen,
ob ein Wert kleiner, gleich oder
größer ist.

### C64 Programmer's Reference Guide (Commodore)
Mask used during FRMEVL

### Memory Map (Jim Butterfield)
Comparison symbol accumulator

### Mapping the Commodore 64 (Sheldon Leemon)
The expression evaluation routine creates a mask here which lets it
know whether the current comparison operation is a less-than (1),
equals (2), or greater-than (4) comparison.

### Reference (Joe Forster / STA)
Bits:

* Bit #1: 1 = ">" (greater than) is present in expression.
* Bit #2: 1 = "=" (equal to) is present in expression.
* Bit #3: 1 = "<" (less than) is present in expression.

### 64'er Magazin (64'er)
Die bei 75 und 76 schon erwähnte Auswertungs-Routine FRMEVL erzeugt in der
Speicherzelle 77 einen Wert, der angibt, ob es sich bei einer
Vergleichsoperation um den Fall »kleiner als« (<), »gleich wie« (=) oder
»größer als« (>) handelt. Diese Speicherzelle ist nur im Maschinencode
erreichbar.

### 64map (—)
Mask used during FRMEVL

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
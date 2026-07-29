---
title: Output vector ($F1CA)
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
related:
- f1ca-zeichens
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
  address: $0326
  address_end: $0327
  symbol: IBSOUT
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: ''
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: $F1CA OUTPUT-Vektor
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: KERNAL CHROUT Routine
  - name: Memory Map
    author: Jim Butterfield
    description: Output vector ($F1CA)
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: Vector to Kernal CHROUT Routine (Currently at 61898 ($F1CA))
  - name: Reference
    author: Joe Forster / STA
    description: 'Default: $F1CA.'
  - name: 64'er Magazin
    author: 64'er
    description: Die CHROUT-Routine entspricht der CHRIN-Routine in der anderen Richtung.
      Sie
  - name: 64map
    author: —
    description: 'Vector: Indirect entry to Kernal CHROUT Routine ($F1CA)'
---

# IBSOUT — Output vector ($F1CA) ($0326)

## Panoramica
Il registro o area di memoria IBSOUT è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0326` (`806` decimale)
- **Range**: `$0326`-`$0327`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)


### Commodore-64-intern-Buch (Commodore)
$F1CA OUTPUT-Vektor

### C64 Programmer's Reference Guide (Commodore)
KERNAL CHROUT Routine

### Memory Map (Jim Butterfield)
Output vector ($F1CA)

### Mapping the Commodore 64 (Sheldon Leemon)
Vector to Kernal CHROUT Routine (Currently at 61898 ($F1CA))

### Reference (Joe Forster / STA)
Default: $F1CA.

### 64'er Magazin (64'er)
Die CHROUT-Routine entspricht der CHRIN-Routine in der anderen Richtung. Sie
bedeutet »Character Output« und transferiert ein Byte, das im Akkumulator
steht, in den Puffer des angewählten Ausgabegerätes. Sie beginnt ab Adresse
62898 ($F1CA), - beim VC 20 ab 62074 ($F27A).

### 64map (—)
Vector: Indirect entry to Kernal CHROUT Routine ($F1CA)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
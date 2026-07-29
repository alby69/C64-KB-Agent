---
title: Abort I/o vector ($F32F)
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
- f32f-clall-schliet-alle
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
  address: $032C
  address_end: $032D
  symbol: ICLALL
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: ''
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: $F32F CLALL-Vektor
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: KERNAL CLALL Routine Vector
  - name: Memory Map
    author: Jim Butterfield
    description: Abort I/o vector ($F32F)
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: Vector to Kernal CLALL Routine (Currently at 62255 ($F32F))
  - name: Reference
    author: Joe Forster / STA
    description: 'Default: $F32F.'
  - name: 64'er Magazin
    author: 64'er
    description: CLALL ist die Abkürzung für Close ALL (Channels and Files). Diese
      Routine, die
  - name: 64map
    author: —
    description: 'Vector: Indirect entry to Kernal CLALL Routine ($F32F)'
---

# ICLALL — Abort I/o vector ($F32F) ($032C)

## Panoramica
Il registro o area di memoria ICLALL è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$032C` (`812` decimale)
- **Range**: `$032C`-`$032D`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)


### Commodore-64-intern-Buch (Commodore)
$F32F CLALL-Vektor

### C64 Programmer's Reference Guide (Commodore)
KERNAL CLALL Routine Vector

### Memory Map (Jim Butterfield)
Abort I/o vector ($F32F)

### Mapping the Commodore 64 (Sheldon Leemon)
Vector to Kernal CLALL Routine (Currently at 62255 ($F32F))

### Reference (Joe Forster / STA)
Default: $F32F.

### 64'er Magazin (64'er)
CLALL ist die Abkürzung für Close ALL (Channels and Files). Diese Routine, die
ab Adresse 62255 ($F32F) - beim VC 20 ab 62447 ($F3EF) - beginnt, setzt die
Speicherzelle 152 auf 0 und schließt so zwangsläufig alle Dateien und Kanäle.

### 64map (—)
Vector: Indirect entry to Kernal CLALL Routine ($F32F)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
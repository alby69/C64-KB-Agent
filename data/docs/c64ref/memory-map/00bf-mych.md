---
title: Serial word buffer
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
  address: $00BF
  symbol: MYCH
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: 'Cassette: holds input byte being built'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Beim Laden eines Programms von Band
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Serial Word Buffer
  - name: Memory Map
    author: Jim Butterfield
    description: Serial word buffer
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This is used by the tape routines as a work area in which incoming
  - name: Reference
    author: Joe Forster / STA
    description: Unknown
  - name: 64'er Magazin
    author: 64'er
    description: Diese Speicherzelle wird beim Laden eines Programms vom Band dazu
      benutzt, um
  - name: 64map
    author: —
    description: Serial Word Buffer
---

# MYCH — Serial word buffer ($00BF)

## Panoramica
Il registro o area di memoria MYCH è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00BF` (`191` decimale)
- **Range**: `$00BF`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Cassette: holds input byte being built

### Commodore-64-intern-Buch (Commodore)
Beim Laden eines Programms von Band
wird diese Speicherzelle dazu benutzt,
um die einzelnen Bits zu einem Byte
zusammenzusetzen.

### C64 Programmer's Reference Guide (Commodore)
Serial Word Buffer

### Memory Map (Jim Butterfield)
Serial word buffer

### Mapping the Commodore 64 (Sheldon Leemon)
This is used by the tape routines as a work area in which incoming
characters area assembled.

### Reference (Joe Forster / STA)
Unknown

### 64'er Magazin (64'er)
Diese Speicherzelle wird beim Laden eines Programms vom Band dazu benutzt, um
Zeichen aus einzelnen Bits zusammenzusetzen.

### 64map (—)
Serial Word Buffer

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
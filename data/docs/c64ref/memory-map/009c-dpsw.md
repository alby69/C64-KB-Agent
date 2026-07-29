---
title: Byte-received flag
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
  address: $009C
  symbol: DPSW
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: 'Cassette: if NZ then expecting LL/L combination that ends a byte'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Hier wird festgelegt, ob das gelesene
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Flag: Tape Byte-Received'
  - name: Memory Map
    author: Jim Butterfield
    description: Byte-received flag
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This location is used as a flag to indicate whether a complete byte
      of
  - name: Reference
    author: Joe Forster / STA
    description: Unknown. (Byte ready indicator during datasette input/output.)
  - name: 64'er Magazin
    author: 64'er
    description: In dieser Speicherzelle wird zwischengespeichert, ob das vom Band
      gelesene Byte
  - name: 64map
    author: —
    description: 'Flag: Byte received from Tape'
---

# DPSW — Byte-received flag ($009C)

## Panoramica
Il registro o area di memoria DPSW è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$009C` (`156` decimale)
- **Range**: `$009C`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Cassette: if NZ then expecting LL/L combination that ends a byte

### Commodore-64-intern-Buch (Commodore)
Hier wird festgelegt, ob das gelesene
Byte die Quersumme richtig gebildet
hat oder nicht.

### C64 Programmer's Reference Guide (Commodore)
Flag: Tape Byte-Received

### Memory Map (Jim Butterfield)
Byte-received flag

### Mapping the Commodore 64 (Sheldon Leemon)
This location is used as a flag to indicate whether a complete byte of
tape data has been received, or whether it has only been partially
received.

### Reference (Joe Forster / STA)
Unknown. (Byte ready indicator during datasette input/output.)

### 64'er Magazin (64'er)
In dieser Speicherzelle wird zwischengespeichert, ob das vom Band gelesene Byte
die Prüfungen bestanden hat, also richtig ist oder nicht.

### 64map (—)
Flag: Byte received from Tape

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
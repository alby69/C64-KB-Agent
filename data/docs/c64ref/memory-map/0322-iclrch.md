---
title: Restore I/0 vector ($F333)
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
- f333-io-kanal
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
  address: $0322
  address_end: $0323
  symbol: ICLRCH
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: ''
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: $F333 CLRCH-Vektor
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: KERNAL CLRCHN Routine Vector
  - name: Memory Map
    author: Jim Butterfield
    description: Restore I/0 vector ($F333)
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: Vector to Kernal CLRCHN Routine (Currently at 62259 ($F333))
  - name: Reference
    author: Joe Forster / STA
    description: 'Default: $F333.'
  - name: 64'er Magazin
    author: 64'er
    description: Der Name dieser Routine ist die Abkürzung für »clear channel«. Diese
      Routine,
  - name: 64map
    author: —
    description: 'Vector: Indirect entry to Kernal CLRCHN Routine ($F333)'
---

# ICLRCH — Restore I/0 vector ($F333) ($0322)

## Panoramica
Il registro o area di memoria ICLRCH è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0322` (`802` decimale)
- **Range**: `$0322`-`$0323`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)


### Commodore-64-intern-Buch (Commodore)
$F333 CLRCH-Vektor

### C64 Programmer's Reference Guide (Commodore)
KERNAL CLRCHN Routine Vector

### Memory Map (Jim Butterfield)
Restore I/0 vector ($F333)

### Mapping the Commodore 64 (Sheldon Leemon)
Vector to Kernal CLRCHN Routine (Currently at 62259 ($F333))

### Reference (Joe Forster / STA)
Default: $F333.

### 64'er Magazin (64'er)
Der Name dieser Routine ist die Abkürzung für »clear channel«. Diese Routine,
die ab Adresse 62259 ($F333) - beim VC 20 ab 62461 ($F3F3) - beginnt, setzt
alle Kanäle in den Einschaltzustand zurück. Das heißt, das Eingabegerät ist die
Tastatur, das Ausgabegerät ist der Bildschirm.

### 64map (—)
Vector: Indirect entry to Kernal CLRCHN Routine ($F333)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
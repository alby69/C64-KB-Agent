---
title: LOAD link ($F4A5)
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
- ece7-load
- f4a5-standard-load-ram-entry
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
  address: $0330
  address_end: $0331
  symbol: ILOAD
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: ''
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: $F4A5 LOAD-Vektor
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: KERNAL LOAD Routine
  - name: Memory Map
    author: Jim Butterfield
    description: LOAD link ($F4A5)
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: Vector to Kernal LOAD Routine (Currently at 62622 ($F49E))
  - name: Reference
    author: Joe Forster / STA
    description: 'Default: $F4A5.'
  - name: 64'er Magazin
    author: 64'er
    description: Dieser Vektor zeigt auf die Adresse 62622 ($F49E) - beim VC 20 auf
      62793
  - name: 64map
    author: —
    description: 'Vector: Indirect entry to Kernal LOAD Routine ($F4A5)'
---

# ILOAD — LOAD link ($F4A5) ($0330)

## Panoramica
Il registro o area di memoria ILOAD è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0330` (`816` decimale)
- **Range**: `$0330`-`$0331`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)


### Commodore-64-intern-Buch (Commodore)
$F4A5 LOAD-Vektor

### C64 Programmer's Reference Guide (Commodore)
KERNAL LOAD Routine

### Memory Map (Jim Butterfield)
LOAD link ($F4A5)

### Mapping the Commodore 64 (Sheldon Leemon)
Vector to Kernal LOAD Routine (Currently at 62622 ($F49E))

### Reference (Joe Forster / STA)
Default: $F4A5.

### 64'er Magazin (64'er)
Dieser Vektor zeigt auf die Adresse 62622 ($F49E) - beim VC 20 auf 62793
($F549). Die dort beginnende Routine transferiert Daten von einem Eingabegerät
direkt in den RAM-Speicher. Sie kann auch zum VERIFYen durch Vergleich der
geladen mit den gespeicherten Daten verwendet werden.

### 64map (—)
Vector: Indirect entry to Kernal LOAD Routine ($F4A5)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
---
title: GET vector ($F13E)
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
- f13e-getin
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
  address: $032A
  address_end: $032B
  symbol: IGETIN
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: ''
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: $F13E GET-Vektor
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: KERNAL GETIN Routine
  - name: Memory Map
    author: Jim Butterfield
    description: GET vector ($F13E)
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: Vector to Kernal GETIN Routine (Currently at 61758 ($F13E))
  - name: Reference
    author: Joe Forster / STA
    description: 'Default: $F13E.'
  - name: 64'er Magazin
    author: 64'er
    description: Diese Routine ist fast identisch mit der CHRiN-Routine (siehe Speicherzellen
  - name: 64map
    author: —
    description: 'Vector: Indirect entry to Kernal GETIN Routine ($F13E)'
---

# IGETIN — GET vector ($F13E) ($032A)

## Panoramica
Il registro o area di memoria IGETIN è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$032A` (`810` decimale)
- **Range**: `$032A`-`$032B`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)


### Commodore-64-intern-Buch (Commodore)
$F13E GET-Vektor

### C64 Programmer's Reference Guide (Commodore)
KERNAL GETIN Routine

### Memory Map (Jim Butterfield)
GET vector ($F13E)

### Mapping the Commodore 64 (Sheldon Leemon)
Vector to Kernal GETIN Routine (Currently at 61758 ($F13E))

### Reference (Joe Forster / STA)
Default: $F13E.

### 64'er Magazin (64'er)
Diese Routine ist fast identisch mit der CHRiN-Routine (siehe Speicherzellen
804 bis 805). Sie holt genauso Zeichen von angewählten Geräten in die
Eingabepuffer. Der einzige und damit wichtigste Unterschied liegt in der
Behandlung der Tastatur-Eingabe. Im Gegensatz zu CHRIN holt sie ein Byte aus
dem Tastaturpuffer sofort in den Akkumulator. Der Vektor zeigt auf den Anfang
der Routine ab Speicherzelle 61785 ($F13E) - beim VC 20 ab 61941 ($F1F5).

### 64map (—)
Vector: Indirect entry to Kernal GETIN Routine ($F13E)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
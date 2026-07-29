---
title: Floating to ASCII work area
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
  address: $00FF
  address_end: $010A
  symbol: BASZPT
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Location ($00FF) used by BASIC
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Diese Register werden für die
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Floating to String Work Area
  - name: Memory Map
    author: Jim Butterfield
    description: Floating to ASCII work area
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This location is used for temporary storage in the process of
  - name: Reference
    author: Joe Forster / STA
    description: Buffer for conversion from floating point to string (12 bytes.)
  - name: 64'er Magazin
    author: 64'er
    description: Diese 12 Byte werden von einer Routine des Betriebssystems verwendet,
      um Werte
  - name: 64map
    author: —
    description: Assembly Area for Floating point to ASCII conversion
---

# BASZPT — Floating to ASCII work area ($00FF)

## Panoramica
Il registro o area di memoria BASZPT è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00FF` (`255` decimale)
- **Range**: `$00FF`-`$010A`
- **Dimensione**: `12 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Location ($00FF) used by BASIC

### Commodore-64-intern-Buch (Commodore)
Diese Register werden für die
Zwischenspeicherung von Fließkommazahlen
benutzt.

### C64 Programmer's Reference Guide (Commodore)
Floating to String Work Area

### Memory Map (Jim Butterfield)
Floating to ASCII work area

### Mapping the Commodore 64 (Sheldon Leemon)
This location is used for temporary storage in the process of
converting floating point numbers to ASCII characters.

### Reference (Joe Forster / STA)
Buffer for conversion from floating point to string (12 bytes.)

### 64'er Magazin (64'er)
Diese 12 Byte werden von einer Routine des Betriebssystems verwendet, um Werte
zwischenzuspeichern, die bei der Umwandlung von Gleitkomma-Zahlen in ASCII-
Werte oder in Werte der Funktion TI$ anfallen. Eine andere Routine verwendet
den Bereich, um Zeichenketten (Strings) zu untersuchen.

### 64map (—)
Assembly Area for Floating point to ASCII conversion

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
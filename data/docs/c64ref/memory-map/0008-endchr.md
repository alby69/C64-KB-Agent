---
title: Scan-quotes flag
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
  address: $0008
  symbol: ENDCHR
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: The other delimiting character
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Während der Umwandlung von
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Flag: Scan for Quote at End of String'
  - name: Memory Map
    author: Jim Butterfield
    description: Scan-quotes flag
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: Like location 7, this location is used as a work byte during the
  - name: Reference
    author: Joe Forster / STA
    description: Byte being search for during various operations. Current byte of
      BASIC line d...
  - name: 64'er Magazin
    author: 64'er
    description: Wie Speicherzelle 7 dient auch die Zelle 8 als Zwischenspeicher für
      Basic-
  - name: 64map
    author: —
    description: 'Flag: Scan for Quote at end of String'
---

# ENDCHR — Scan-quotes flag ($0008)

## Panoramica
Il registro o area di memoria ENDCHR è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0008` (`8` decimale)
- **Range**: `$0008`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
The other delimiting character

### Commodore-64-intern-Buch (Commodore)
Während der Umwandlung von
BASIC-Befehlen in Tokens wird die
Speicherzelle $0008 als Zwischenspeicher
für BASIC-Texteingaben verwendet.

### C64 Programmer's Reference Guide (Commodore)
Flag: Scan for Quote at End of String

### Memory Map (Jim Butterfield)
Scan-quotes flag

### Mapping the Commodore 64 (Sheldon Leemon)
Like location 7, this location is used as a work byte during the
tokenization of a BASIC statement.  Most of the time, its value is 0
or 34.

### Reference (Joe Forster / STA)
Byte being search for during various operations. Current byte of BASIC line during tokenization. High byte of first integer operand during AND and OR

### 64'er Magazin (64'er)
Wie Speicherzelle 7 dient auch die Zelle 8 als Zwischenspeicher für Basic-
Texteingabe und zwar während der Umwandlung von Basic-Befehlen in den vom
Computer verwendeten Befehlscode (Tokens). Die Speicherzelle 8 ist in Basic
nicht verwertbar.

### 64map (—)
Flag: Scan for Quote at end of String

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
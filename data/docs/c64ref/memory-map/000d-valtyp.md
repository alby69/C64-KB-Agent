---
title: 'Type : FF = string, 00 = numeric'
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
  address: $000D
  symbol: VALTYP
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: 0=numeric 1=string.
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Das Flag zeigt dem BASIC-Interpreter
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Data Type: $FF = String, $00 = Numeric'
  - name: Memory Map
    author: Jim Butterfield
    description: 'Type : FF = string, 00 = numeric'
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This flag is used internally to indicate whether data being operated
  - name: Reference
    author: Joe Forster / STA
    description: 'Values:'
  - name: 64'er Magazin
    author: 64'er
    description: Diese Flagge zeigt den Routinen des Basic-Übersetzers an, ob es sich
      bei den
  - name: 64map
    author: —
    description: 'Data type Flag: $00 = Numeric, $FF = String'
---

# VALTYP — Type : FF = string, 00 = numeric ($000D)

## Panoramica
Il registro o area di memoria VALTYP è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$000D` (`13` decimale)
- **Range**: `$000D`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
0=numeric 1=string.

### Commodore-64-intern-Buch (Commodore)
Das Flag zeigt dem BASIC-Interpreter
an, ob es sich um Zahlenwerte oder um
einen String handelt.

### C64 Programmer's Reference Guide (Commodore)
Data Type: $FF = String, $00 = Numeric

### Memory Map (Jim Butterfield)
Type : FF = string, 00 = numeric

### Mapping the Commodore 64 (Sheldon Leemon)
This flag is used internally to indicate whether data being operated
upon is string or numeric.  A value of 255 ($FF) in this location
indicates string data, while a 0 indicates numeric data.  This
determination is made every time a variable is located or created.

### Reference (Joe Forster / STA)
Values:

* $00: Numerical.
* $FF: String.

### 64'er Magazin (64'er)
Diese Flagge zeigt den Routinen des Basic-Übersetzers an, ob es sich bei den
zur Verarbeitung anstehenden Daten um einen String oder um Zahlenwerte handelt.
Zeigt die Flagge 255 ($FF), ist es ein String. Bei 0 handelt es sich um Zahlen.
Diese Bestimmung erfolgt jedesmal, wenn eine Variable definiert oder gesucht
wird. Diese Flagge kann leider nicht durch ein Basic-Programm abgefragt werden.

### 64map (—)
Data type Flag: $00 = Numeric, $FF = String

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
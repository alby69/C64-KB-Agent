---
title: Current variable name
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
  address: $0045
  address_end: $0046
  symbol: VARNAM
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Variable's name is stored here
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Falls während des Ablaufs eines
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Current BASIC Variable Name
  - name: Memory Map
    author: Jim Butterfield
    description: Current variable name
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: The current variable name being searched for is stored here, in the
  - name: Reference
    author: Joe Forster / STA
    description: 'Bits:'
  - name: 64'er Magazin
    author: 64'er
    description: Wenn beim Ablauf eines Programms eine Variable auftaucht, muß ihr
      derzeitiger
  - name: 64map
    author: —
    description: Name of Variable being sought in Variable Table
---

# VARNAM — Current variable name ($0045)

## Panoramica
Il registro o area di memoria VARNAM è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0045` (`69` decimale)
- **Range**: `$0045`-`$0046`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Variable's name is stored here

### Commodore-64-intern-Buch (Commodore)
Falls während des Ablaufs eines
Programms eine Variable auftaucht,
wird deren Name hier zwischengespeichert.

### C64 Programmer's Reference Guide (Commodore)
Current BASIC Variable Name

### Memory Map (Jim Butterfield)
Current variable name

### Mapping the Commodore 64 (Sheldon Leemon)
The current variable name being searched for is stored here, in the
same two- byte format as in the variable value storage area located at
the address pointed to by 45 ($002D).  See that location for an
explanation of the format.

### Reference (Joe Forster / STA)
Bits:

* $0045 bits #0-#6: First character of variable name.
* $0046 bits #0-#6: Second character of variable name; $00 = Variable name consists of only one character.
* $0045 bit #7 and $0046 bit #7:
    * %00: Floating-point variable.
    * %01: String variable.
    * %10: FN function, created with DEF FN.
    * %11: Integer variable.

### 64'er Magazin (64'er)
Wenn beim Ablauf eines Programms eine Variable auftaucht, muß ihr derzeitiger
Wert im Variablen-Speicher gesucht werden. Während dieses Suchvorgangs wird der
Name der Variablen in 69 und 70 zwischengespeichert. Die Form der
Zwischenspeicherung ist dieselbe 2-Byte-Darstellung wie im Variablenspeicher,
beschrieben bei der Behandlung der Speicherzellen 45 und 46.

### 64map (—)
Name of Variable being sought in Variable Table

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
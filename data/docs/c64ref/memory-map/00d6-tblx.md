---
title: Row where cursor lives
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
  address: $00D6
  symbol: TBLX
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: ''
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Hier wird die Zeilenposition des
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Current Cursor Physical Line Number
  - name: Memory Map
    author: Jim Butterfield
    description: Row where cursor lives
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This location contains the current physical screen line position
      of
  - name: Reference
    author: Joe Forster / STA
    description: 'Current cursor row. Values: $00-$18, 0-24'
  - name: 64'er Magazin
    author: 64'er
    description: Diese Speicherzelle ist zusammen mit der Speicherzelle 211 beschrieben.
  - name: 64map
    author: —
    description: Current Screen Line number of Cursor
---

# TBLX — Row where cursor lives ($00D6)

## Panoramica
Il registro o area di memoria TBLX è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00D6` (`214` decimale)
- **Range**: `$00D6`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)


### Commodore-64-intern-Buch (Commodore)
Hier wird die Zeilenposition des
Cursors festgehalten.

### C64 Programmer's Reference Guide (Commodore)
Current Cursor Physical Line Number

### Memory Map (Jim Butterfield)
Row where cursor lives

### Mapping the Commodore 64 (Sheldon Leemon)
This location contains the current physical screen line position of
the cursor (0-24).  It can be used in a fashion to move the cursor
vertically, by POKEing the target screen line (1-25) minus 1 here,
followed by a PRINT command.  For example,

    POKE 214,9:PRINT:PRINT "WE'RE ON LINE ELEVEN"

prints the message on line 11.  The first PRINT statement allows the
system to update the other screen editor variables so that they will
also show the new line.  The cursor can also be set or read using the
Kernal PLOT routine (58634, $E50A) as explained in the entry from
locations 780-783 ($030C-$030F).

### Reference (Joe Forster / STA)
Current cursor row. Values: $00-$18, 0-24

### 64'er Magazin (64'er)
Diese Speicherzelle ist zusammen mit der Speicherzelle 211 beschrieben.

### 64map (—)
Current Screen Line number of Cursor

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
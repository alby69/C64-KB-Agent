---
title: Last inkey/checksum/buffer
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
  address: $00D7
  symbol: DATA
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: 'Cassette: holds most recent dipole bit value'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Bevor ein Zeichen in den
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Temp Data Area
  - name: Memory Map
    author: Jim Butterfield
    description: Last inkey/checksum/buffer
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: The ASCII value of the last character printed to the screen is held
  - name: Reference
    author: Joe Forster / STA
    description: PETSCII code of character during screen input/output. Bit buffer
      during datas...
  - name: 64'er Magazin
    author: 64'er
    description: Bei der Tastaturabfrage werden die Tastencodes (siehe Speicherzelle
      203) in
  - name: 64map
    author: —
    description: Screen value of current Input Character/Last Character Output
---

# DATA — Last inkey/checksum/buffer ($00D7)

## Panoramica
Il registro o area di memoria DATA è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00D7` (`215` decimale)
- **Range**: `$00D7`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Cassette: holds most recent dipole bit value

### Commodore-64-intern-Buch (Commodore)
Bevor ein Zeichen in den
Tastaturpuffer gebracht wird, wird es
vorher hier zwischengespeichert.

### C64 Programmer's Reference Guide (Commodore)
Temp Data Area

### Memory Map (Jim Butterfield)
Last inkey/checksum/buffer

### Mapping the Commodore 64 (Sheldon Leemon)
The ASCII value of the last character printed to the screen is held
here temporarily.

### Reference (Joe Forster / STA)
PETSCII code of character during screen input/output. Bit buffer during datasette input. Block checksum during datasette output

### 64'er Magazin (64'er)
Bei der Tastaturabfrage werden die Tastencodes (siehe Speicherzelle 203) in
ASCII-Codewerte umgewandelt und in den Tastaturpuffer gebracht. Die
Speicherzelle 215 dient dabei als Zwischenspeicher. Kassettenoperationen
speichern hier auch Prüfsummen ab.

### 64map (—)
Screen value of current Input Character/Last Character Output

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
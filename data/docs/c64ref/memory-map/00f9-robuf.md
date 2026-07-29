---
title: RS-232 Tx pntr
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
  address: $00F9
  address_end: $00FA
  symbol: ROBUF
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: RS-232 output buffer pointer
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Diese Register zeigen auf die
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: RS-232 Output Buffer  Pointer
  - name: Memory Map
    author: Jim Butterfield
    description: RS-232 Tx pntr
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This location points to the address of the 256-byte output buffer
  - name: Reference
    author: Joe Forster / STA
    description: 'Values:'
  - name: 64'er Magazin
    author: 64'er
    description: Dieser Zeiger ist der Zwilling zu dem in den Zellen 247/248 stehenden
      Zeiger,
  - name: 64map
    author: —
    description: RS232 Output Buffer Pointer
---

# ROBUF — RS-232 Tx pntr ($00F9)

## Panoramica
Il registro o area di memoria ROBUF è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00F9` (`249` decimale)
- **Range**: `$00F9`-`$00FA`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
RS-232 output buffer pointer

### Commodore-64-intern-Buch (Commodore)
Diese Register zeigen auf die
Anfangsadresse des Ausgabepuffers.

### C64 Programmer's Reference Guide (Commodore)
RS-232 Output Buffer  Pointer

### Memory Map (Jim Butterfield)
RS-232 Tx pntr

### Mapping the Commodore 64 (Sheldon Leemon)
This location points to the address of the 256-byte output buffer
which is used for transmitting data to RS-232 devices (device number
2)l

### Reference (Joe Forster / STA)
Values:

* $0000-$00FF: No buffer defined, a new buffer must be allocated upon RS232 output.
* $0100-$FFFF: Buffer pointer.

### 64'er Magazin (64'er)
Dieser Zeiger ist der Zwilling zu dem in den Zellen 247/248 stehenden Zeiger,
diesmal aber für den Ausgabe-Puffer.

### 64map (—)
RS232 Output Buffer Pointer

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
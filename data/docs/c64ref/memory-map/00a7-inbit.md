---
title: Tp Wrt ldr count/Rd pass/inbit
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
  address: $00A7
  symbol: INBIT
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: RS-232 rcvr input bit storage
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: 'Cassette: holds FSBLK, used to direct routines, because of exit
      case'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Diese Register werden häufig von
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: RS-232 Input Bits / Cassette Temp
  - name: Memory Map
    author: Jim Butterfield
    description: Tp Wrt ldr count/Rd pass/inbit
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This location is used to temporarily store each bit of serial data
  - name: Reference
    author: Joe Forster / STA
    description: Bit buffer during RS232 input
  - name: 64'er Magazin
    author: 64'er
    description: Diese Speicherzelle wird verwendet, um jedes Bit, welches von einem
      RS232-Kanal
  - name: 64map
    author: —
    description: RS232 temporary for received Bit/Tape temporary
---

# INBIT — Tp Wrt ldr count/Rd pass/inbit ($00A7)

## Panoramica
Il registro o area di memoria INBIT è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00A7` (`167` decimale)
- **Range**: `$00A7`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
RS-232 rcvr input bit storage

### Original Source Comments (Microsoft/Commodore)
Cassette: holds FSBLK, used to direct routines, because of exit case

### Commodore-64-intern-Buch (Commodore)
Diese Register werden häufig von
Kassettenoperationen und der RS-232
Schnittstelle als Zwischenspeicher
benutzt.

### C64 Programmer's Reference Guide (Commodore)
RS-232 Input Bits / Cassette Temp

### Memory Map (Jim Butterfield)
Tp Wrt ldr count/Rd pass/inbit

### Mapping the Commodore 64 (Sheldon Leemon)
This location is used to temporarily store each bit of serial data
that is received, as well as for miscellaneous tasks by tape I/O.

### Reference (Joe Forster / STA)
Bit buffer during RS232 input

### 64'er Magazin (64'er)
Diese Speicherzelle wird verwendet, um jedes Bit, welches von einem RS232-Kanal
über den User-Port eingelesen wird, zwischenzuspeichern.

Außerdem verwenden mehrere Kassetten-Routinen diese Adresse als
Zwischenspeicher.

### 64map (—)
RS232 temporary for received Bit/Tape temporary

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
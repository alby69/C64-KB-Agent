---
title: '# bits to send'
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
  address: $0298
  symbol: BITNUM
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Number of bits to send (fast response)
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Diese Speicherzelle wird verwendet,
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: RS-232 Number of Bits Left to Send
  - name: Memory Map
    author: Jim Butterfield
    description: '# bits to send'
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This location is used to determine how many zero bits must be added
      to
  - name: Reference
    author: Joe Forster / STA
    description: RS232 byte size, number of data bits per data byte, default value
      for bit cou...
  - name: 64'er Magazin
    author: 64'er
    description: Diese Speicherzelle wird verwendet, um festzustellen, mit wievielen
      Nullen das
  - name: 64map
    author: —
    description: RS232 Number of Bits left to send
---

# BITNUM — # bits to send ($0298)

## Panoramica
Il registro o area di memoria BITNUM è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0298` (`664` decimale)
- **Range**: `$0298`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Number of bits to send (fast response)

### Commodore-64-intern-Buch (Commodore)
Diese Speicherzelle wird verwendet,
um die Wortlänge festzustellen.

### C64 Programmer's Reference Guide (Commodore)
RS-232 Number of Bits Left to Send

### Memory Map (Jim Butterfield)
# bits to send

### Mapping the Commodore 64 (Sheldon Leemon)
This location is used to determine how many zero bits must be added to
the data character to pad its length out to the word length specified
in 659 ($0293).

### Reference (Joe Forster / STA)
RS232 byte size, number of data bits per data byte, default value for bit counters

### 64'er Magazin (64'er)
Diese Speicherzelle wird verwendet, um festzustellen, mit wievielen Nullen das
zu übertragende Zeichen aufgefüllt werden muß, um die in Speicherzelle 659 (Bit
5 und 6) ausgewählte Wortlänge herzustellen (s. Speicherzellen 168 und 180).

### 64map (—)
RS232 Number of Bits left to send

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
---
title: Wrt start bit/Rd bit err/stbit
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
  - 64'er_magazin.txt
  - mapping_the_commodore_64.txt
  - memory_map.txt
  - c64_programmer's_reference_guide.txt
  - 64map.txt
  address: $00A9
  symbol: RINONE
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: RS-232 rcvr flag for start bit check
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: 'Cassette: counts zeros (if Z then correct # of dipoles)'
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'RS-232 Flag: Check for Start Bit'
  - name: Memory Map
    author: Jim Butterfield
    description: Wrt start bit/Rd bit err/stbit
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This flag is used when checking for a start bit.  A 144 ($90) here
  - name: Reference
    author: Joe Forster / STA
    description: 'Values:'
  - name: 64'er Magazin
    author: 64'er
    description: Ein RS232-Datentransfer prüft, ob ein Start-Bit empfangen worden
      ist. Im
  - name: 64map
    author: —
    description: 'RS232 Flag: Start Bit check/Tape temporary'
---

# RINONE — Wrt start bit/Rd bit err/stbit ($00A9)

## Panoramica
Il registro o area di memoria RINONE è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00A9` (`169` decimale)
- **Range**: `$00A9`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
RS-232 rcvr flag for start bit check

### Original Source Comments (Microsoft/Commodore)
Cassette: counts zeros (if Z then correct # of dipoles)

### C64 Programmer's Reference Guide (Commodore)
RS-232 Flag: Check for Start Bit

### Memory Map (Jim Butterfield)
Wrt start bit/Rd bit err/stbit

### Mapping the Commodore 64 (Sheldon Leemon)
This flag is used when checking for a start bit.  A 144 ($90) here
indicates that no start bit was received, while a 0 means that a start
bit was received.

### Reference (Joe Forster / STA)
Values:

* $00: Data bit.
* $01-$FF: Stop bit.

### 64'er Magazin (64'er)
Ein RS232-Datentransfer prüft, ob ein Start-Bit empfangen worden ist. Im
positiven Fall steht in Zelle 169 die Zahl 144, im negativen Fall eine 0.

### 64map (—)
RS232 Flag: Start Bit check/Tape temporary

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
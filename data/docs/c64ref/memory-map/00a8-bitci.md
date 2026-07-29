---
title: Tp Wrt new byte/Rd error/inbit cnt
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
  address: $00A8
  symbol: BITCI
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: RS-232 rcvr bit count in
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: 'Cassette: flags errors (if Z then no error)'
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: RS-232 Input Bit Count / Cassette Temp
  - name: Memory Map
    author: Jim Butterfield
    description: Tp Wrt new byte/Rd error/inbit cnt
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This location is used to count the number of bits of serial data
      that
  - name: Reference
    author: Joe Forster / STA
    description: Bit counter during RS232 input
  - name: 64'er Magazin
    author: 64'er
    description: Die Speicherzelle 168 wird als Zähler verwendet, der dies mal nicht
      die Bytes,
  - name: 64map
    author: —
    description: RS232 Input Bit count/Tape temporary
---

# BITCI — Tp Wrt new byte/Rd error/inbit cnt ($00A8)

## Panoramica
Il registro o area di memoria BITCI è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00A8` (`168` decimale)
- **Range**: `$00A8`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
RS-232 rcvr bit count in

### Original Source Comments (Microsoft/Commodore)
Cassette: flags errors (if Z then no error)

### C64 Programmer's Reference Guide (Commodore)
RS-232 Input Bit Count / Cassette Temp

### Memory Map (Jim Butterfield)
Tp Wrt new byte/Rd error/inbit cnt

### Mapping the Commodore 64 (Sheldon Leemon)
This location is used to count the number of bits of serial data that
has been received.  This is necessary so that the serial routines will
know when a full word has been received.  It is also used as an error
flag during tape loads.

### Reference (Joe Forster / STA)
Bit counter during RS232 input

### 64'er Magazin (64'er)
Die Speicherzelle 168 wird als Zähler verwendet, der dies mal nicht die Bytes,
sondern die Anzahl der Bits zählt, die sowohl über den User-Port als auch über
den Kassetten-Port geleitet werden. Das dient dem Betriebssystem dazu, zu
wissen, wann ein volles Wort abgearbeitet worden ist.

### 64map (—)
RS232 Input Bit count/Tape temporary

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
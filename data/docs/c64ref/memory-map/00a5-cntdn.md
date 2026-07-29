---
title: Countdown, tape write/bit count
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
  address: $00A5
  symbol: CNTDN
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Temp used by serial routine
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Cassette sync countdown
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Diese Speicherzelle wird als Zähler
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Cassette Sync Countdown
  - name: Memory Map
    author: Jim Butterfield
    description: Countdown, tape write/bit count
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: Used to count down the number of synchronization characters that
      are
  - name: Reference
    author: Joe Forster / STA
    description: Bit counter during serial bus input/output. Counter for sync mark
      during data...
  - name: 64'er Magazin
    author: 64'er
    description: Beim Abspeichern eines Programms auf ein Band werden vor den eigentlichen
      Daten
  - name: 64map
    author: —
    description: Tape Synchronising count down
---

# CNTDN — Countdown, tape write/bit count ($00A5)

## Panoramica
Il registro o area di memoria CNTDN è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00A5` (`165` decimale)
- **Range**: `$00A5`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Temp used by serial routine

### Original Source Comments (Microsoft/Commodore)
Cassette sync countdown

### Commodore-64-intern-Buch (Commodore)
Diese Speicherzelle wird als Zähler
des Synchron-Bits verwendet.

### C64 Programmer's Reference Guide (Commodore)
Cassette Sync Countdown

### Memory Map (Jim Butterfield)
Countdown, tape write/bit count

### Mapping the Commodore 64 (Sheldon Leemon)
Used to count down the number of synchronization characters that are
sent before the actual data in a tape block.

### Reference (Joe Forster / STA)
Bit counter during serial bus input/output. Counter for sync mark during datasette output

### 64'er Magazin (64'er)
Beim Abspeichern eines Programms auf ein Band werden vor den eigentlichen Daten
mehrere Bits zusätzlich gespeichert, die beim Einlesen dieses Bandes zur
Synchronisierung dienen, das heißt zum Übereinstimmen der Geschwindigkeit der
Datenübertragung.

Die Speicherzelle 165 wird als Zähler dieses Synchron-Bits verwendet.

### 64map (—)
Tape Synchronising count down

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
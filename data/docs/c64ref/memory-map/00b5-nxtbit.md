---
title: Tp EOT/RS232 next bit to send
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
  address: $00B5
  symbol: NXTBIT
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: RS-232 trns next bit to be sent
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: 'Cassette: used to preserve SYNO (outside of bit routines)'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Diese Speicherzelle enthält immer das
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: RS-232 Next Bit to Send/ Tape EOT Flag
  - name: Memory Map
    author: Jim Butterfield
    description: Tp EOT/RS232 next bit to send
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This location is used by the RS-232 routines to hold the next bit
      to
  - name: Reference
    author: Joe Forster / STA
    description: 'Bit buffer (in bit #2) during RS232 output'
  - name: 64'er Magazin
    author: 64'er
    description: Bei RS232-Operationen enthält die Zelle 181 das jeweils nächste Bit,
      welches
  - name: 64map
    author: —
    description: RS232 Next Bit to send/Tape Read - End of Tape
---

# NXTBIT — Tp EOT/RS232 next bit to send ($00B5)

## Panoramica
Il registro o area di memoria NXTBIT è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00B5` (`181` decimale)
- **Range**: `$00B5`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
RS-232 trns next bit to be sent

### Original Source Comments (Microsoft/Commodore)
Cassette: used to preserve SYNO (outside of bit routines)

### Commodore-64-intern-Buch (Commodore)
Diese Speicherzelle enthält immer das
nächste Bit, das bei RS-232 Operationen
übertragen werden soll.

### C64 Programmer's Reference Guide (Commodore)
RS-232 Next Bit to Send/ Tape EOT Flag

### Memory Map (Jim Butterfield)
Tp EOT/RS232 next bit to send

### Mapping the Commodore 64 (Sheldon Leemon)
This location is used by the RS-232 routines to hold the next bit to
be sent, and by the tape routines to indicate what part of a block the
read routine is currently reading.

### Reference (Joe Forster / STA)
Bit buffer (in bit #2) during RS232 output

### 64'er Magazin (64'er)
Bei RS232-Operationen enthält die Zelle 181 das jeweils nächste Bit, welches
übertragen werden soll. Bandoperationen entnehmen dieser Speicherzelle, welcher
Block gerade gelesen wird.

### 64map (—)
RS232 Next Bit to send/Tape Read - End of Tape

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
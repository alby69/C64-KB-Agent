---
title: Cycle count
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
  - memory_map.txt
  - 64map.txt
  address: $00A4
  symbol: FIRT
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Temp used by serial routine
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: 'Cassette: used to indicate which half of dipole we''re in'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: siehe oben
  - name: Memory Map
    author: Jim Butterfield
    description: Cycle count
  - name: Reference
    author: Joe Forster / STA
    description: Byte buffer during serial bus input. Parity during datasette input/output
  - name: 64map
    author: —
    description: Pulse Counter Tape Read or Write/Serial Bus shift Counter
---

# FIRT — Cycle count ($00A4)

## Panoramica
Il registro o area di memoria FIRT è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00A4` (`164` decimale)
- **Range**: `$00A4`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Temp used by serial routine

### Original Source Comments (Microsoft/Commodore)
Cassette: used to indicate which half of dipole we're in

### Commodore-64-intern-Buch (Commodore)
siehe oben

### Memory Map (Jim Butterfield)
Cycle count

### Reference (Joe Forster / STA)
Byte buffer during serial bus input. Parity during datasette input/output

### 64map (—)
Pulse Counter Tape Read or Write/Serial Bus shift Counter

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
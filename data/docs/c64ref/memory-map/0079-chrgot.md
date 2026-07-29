---
title: CHRGOT. Read current byte from BASIC program or direct command
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
related:
- 0079-chrgot
scraped_at: '2026-07-29'
c64ref:
  module: c64mem
  source_files:
  - reference.txt
  - 64map.txt
  - c64_programmer's_reference_guide.txt
  address: $0079
  symbol: CHRGOT
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Entry to Get Same Byte of Text Again
  - name: Reference
    author: Joe Forster / STA
    description: Pointer to current byte in BASIC program or direct command.
  - name: 64map
    author: —
    description: Entry to Get same Byte again
---

# CHRGOT — CHRGOT. Read current byte from BASIC program or direct command ($0079)

## Panoramica
Il registro o area di memoria CHRGOT è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0079` (`121` decimale)
- **Range**: `$0079`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
Entry to Get Same Byte of Text Again

### Reference (Joe Forster / STA)
Pointer to current byte in BASIC program or direct command.

### 64map (—)
Entry to Get same Byte again

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
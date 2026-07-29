---
title: Time of Day Clock Minutes
source_url: https://github.com/mist64/c64ref/blob/main/src/c64io/mapping_the_commodore_64.txt
category: reference
topics:
- io-map
- cia-registers
difficulty: intermediate
language: assembly
hardware:
- CIA
related: []
scraped_at: '2026-07-29'
c64ref:
  module: c64io
  source_files:
  - mapping_the_commodore_64.txt
  - c64_programmer's_reference_guide.txt
  address: $DC0A
  symbol: TODMIN
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Time-of-Day Clock: Minutes'
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: 0-3  Second digit of Time of Day minutes (BCD)
---

# TODMIN — Time of Day Clock Minutes ($DC0A)

## Panoramica
Il registro o area di memoria TODMIN è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$DC0A` (`56330` decimale)
- **Range**: `$DC0A`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
Time-of-Day Clock: Minutes

### Mapping the Commodore 64 (Sheldon Leemon)
0-3  Second digit of Time of Day minutes (BCD)
4-6  First digit of Time of Day minutes (BCD)
7    Unused

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
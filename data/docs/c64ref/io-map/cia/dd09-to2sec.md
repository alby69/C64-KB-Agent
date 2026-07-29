---
title: Time of Day Clock Seconds
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
  address: $DD09
  symbol: TO2SEC
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Time-of-Day Clock: Seconds'
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: 0-3  Second digit of Time of Day seconds (BCD)
---

# TO2SEC — Time of Day Clock Seconds ($DD09)

## Panoramica
Il registro o area di memoria TO2SEC è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$DD09` (`56585` decimale)
- **Range**: `$DD09`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
Time-of-Day Clock: Seconds

### Mapping the Commodore 64 (Sheldon Leemon)
0-3  Second digit of Time of Day seconds (BCD)
4-6  First digit of Time of Day seconds (BCD)
     Bit 7:  Unused

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
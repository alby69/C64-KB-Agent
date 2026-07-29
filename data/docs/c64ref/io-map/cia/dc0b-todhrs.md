---
title: Time of Day Clock Hours
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
  address: $DC0B
  symbol: TODHRS
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Time-of-Day Clock: Hours + AM/PM Flag (Bit 7)'
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: 0-3  Second digit of Time of Day hours (BCD)
---

# TODHRS — Time of Day Clock Hours ($DC0B)

## Panoramica
Il registro o area di memoria TODHRS è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$DC0B` (`56331` decimale)
- **Range**: `$DC0B`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
Time-of-Day Clock: Hours + AM/PM Flag (Bit 7)

### Mapping the Commodore 64 (Sheldon Leemon)
0-3  Second digit of Time of Day hours (BCD)
4    First digit of Time of Day hours (BCD)
5-6  Unused
7    AM/PM Flag (1=PM, 0=AM)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
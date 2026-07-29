---
title: Serial Data Port
source_url: https://github.com/mist64/c64ref/blob/main/src/c64io/mapping_the_commodore_64.txt
category: reference
topics:
- io-map
- cia-registers
difficulty: intermediate
language: assembly
hardware:
- CIA
related:
- dc0c
scraped_at: '2026-07-29'
c64ref:
  module: c64io
  source_files:
  - mapping_the_commodore_64.txt
  - c64_programmer's_reference_guide.txt
  address: $DD0C
  symbol: CI2SDR
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Synchronous Serial I/O Data Buffer
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: The CIA chip has an on-chip serial port, which allows you to send
      or
---

# CI2SDR — Serial Data Port ($DD0C)

## Panoramica
Il registro o area di memoria CI2SDR è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$DD0C` (`56588` decimale)
- **Range**: `$DD0C`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
Synchronous Serial I/O Data Buffer

### Mapping the Commodore 64 (Sheldon Leemon)
The CIA chip has an on-chip serial port, which allows you to send or
     receive a byte of data one bit at a time, with the most significant
     bit (Bit 7) being transferred first.  For more information about its
     use, see the entry for location 56332 ($DC0C).  The 64's Operating
     System does not use this facility.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
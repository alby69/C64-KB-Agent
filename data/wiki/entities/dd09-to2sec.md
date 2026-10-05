---
id: dd09-to2sec
type: entity
title: Time of Day Clock Seconds
aliases:
- Time of Day Clock Seconds
tags:
- cia-registers
- io-map
sources:
- path: data/docs/c64ref/io-map/cia/dd09-to2sec.md
  sha256: f991ad2c720a72f5e55e5cf06734e15236d0fefba8d2ca1b863f1ae0105d48ca
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-dd09-to2sec
---

# Time of Day Clock Seconds



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

## References
- Source: [[src-dd09-to2sec]]

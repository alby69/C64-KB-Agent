---
id: dc0b-todhrs
type: entity
title: Time of Day Clock Hours
aliases:
- Time of Day Clock Hours
tags:
- cia-registers
- io-map
sources:
- path: data/docs/c64ref/io-map/cia/dc0b-todhrs.md
  sha256: 9d9eed14f4648cce56b3c427a74facbb36b09735657a05ac47aa855a472b4c32
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-dc0b-todhrs
---

# Time of Day Clock Hours



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

## References
- Source: [[src-dc0b-todhrs]]

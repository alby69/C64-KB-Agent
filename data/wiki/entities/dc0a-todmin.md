---
id: dc0a-todmin
type: entity
title: Time of Day Clock Minutes
aliases:
- Time of Day Clock Minutes
tags:
- cia-registers
- io-map
sources:
- path: data/docs/c64ref/io-map/cia/dc0a-todmin.md
  sha256: 54222ebcfc8060f22b88de6f552605872ed115120858da4e8d5ebfcff665fe71
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-dc0a-todmin
---

# Time of Day Clock Minutes



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

## References
- Source: [[src-dc0a-todmin]]

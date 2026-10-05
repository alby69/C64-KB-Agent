---
id: src-dc0a-todmin
type: source
title: 'Source Summary: Time of Day Clock Minutes'
aliases:
- Time of Day Clock Minutes
- dc0a-todmin.md
tags:
- io-map
- cia-registers
sources:
- path: data/docs/c64ref/io-map/cia/dc0a-todmin.md
  sha256: 54222ebcfc8060f22b88de6f552605872ed115120858da4e8d5ebfcff665fe71
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Time of Day Clock Minutes

**Raw Source File**: `data/docs/c64ref/io-map/cia/dc0a-todmin.md`
**SHA256**: `54222ebcfc8060f22b88de6f552605872ed115120858da4e8d5ebfcff665fe71`

## Summary



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
4-6  First digit of Time of Day ...

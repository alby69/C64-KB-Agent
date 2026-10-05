---
id: src-dd0a-to2min
type: source
title: 'Source Summary: Time of Day Clock Minutes'
aliases:
- Time of Day Clock Minutes
- dd0a-to2min.md
tags:
- io-map
- cia-registers
sources:
- path: data/docs/c64ref/io-map/cia/dd0a-to2min.md
  sha256: ba9adf7b061382136f5b68c22014c98720f18c71abbffa1baff2c589fe327707
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Time of Day Clock Minutes

**Raw Source File**: `data/docs/c64ref/io-map/cia/dd0a-to2min.md`
**SHA256**: `ba9adf7b061382136f5b68c22014c98720f18c71abbffa1baff2c589fe327707`

## Summary



# TO2MIN — Time of Day Clock Minutes ($DD0A)

## Panoramica
Il registro o area di memoria TO2MIN è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$DD0A` (`56586` decimale)
- **Range**: `$DD0A`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
Time-of-Day Clock: Minutes

### Mapping the Commodore 64 (Sheldon Leemon)
0-3  Second digit of Time of Day minutes (BCD)
4-6  First digit of Time of Day ...

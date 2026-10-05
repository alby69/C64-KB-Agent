---
id: src-dc09-todsec
type: source
title: 'Source Summary: Time of Day Clock Seconds'
aliases:
- Time of Day Clock Seconds
- dc09-todsec.md
tags:
- io-map
- cia-registers
sources:
- path: data/docs/c64ref/io-map/cia/dc09-todsec.md
  sha256: 4a5c36be15884b1af6e5302afa2f408bcbd313f9a79b3c2d4e1372e5cdae0d0c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Time of Day Clock Seconds

**Raw Source File**: `data/docs/c64ref/io-map/cia/dc09-todsec.md`
**SHA256**: `4a5c36be15884b1af6e5302afa2f408bcbd313f9a79b3c2d4e1372e5cdae0d0c`

## Summary



# TODSEC — Time of Day Clock Seconds ($DC09)

## Panoramica
Il registro o area di memoria TODSEC è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$DC09` (`56329` decimale)
- **Range**: `$DC09`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
Time-of-Day Clock: Seconds

### Mapping the Commodore 64 (Sheldon Leemon)
0-3  Second digit of Time of Day seconds (BCD)
4-6  First digit of Time of Day ...

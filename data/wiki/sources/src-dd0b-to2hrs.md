---
id: src-dd0b-to2hrs
type: source
title: 'Source Summary: Time of Day Clock Hours'
aliases:
- Time of Day Clock Hours
- dd0b-to2hrs.md
tags:
- io-map
- cia-registers
sources:
- path: data/docs/c64ref/io-map/cia/dd0b-to2hrs.md
  sha256: 6fcb9db41713c185e7921315c97a487ed44efe42ede2215e637a6e42aaee958c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Time of Day Clock Hours

**Raw Source File**: `data/docs/c64ref/io-map/cia/dd0b-to2hrs.md`
**SHA256**: `6fcb9db41713c185e7921315c97a487ed44efe42ede2215e637a6e42aaee958c`

## Summary



# TO2HRS — Time of Day Clock Hours ($DD0B)

## Panoramica
Il registro o area di memoria TO2HRS è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$DD0B` (`56587` decimale)
- **Range**: `$DD0B`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
Time-of-Day Clock: Hours + AM/PM Flag (Bit 7)

### Mapping the Commodore 64 (Sheldon Leemon)
0-3  Second digit of Time of Day hours (BCD)
     Bit 4:  Firs...

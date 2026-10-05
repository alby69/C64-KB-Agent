---
id: src-dc0e-ciacra
type: source
title: 'Source Summary: Control Register A'
aliases:
- Control Register A
- dc0e-ciacra.md
tags:
- io-map
- cia-registers
sources:
- path: data/docs/c64ref/io-map/cia/dc0e-ciacra.md
  sha256: 45dcd3e98bba157a37d74719d3151a105057343aae7d884f326f3de5c3bbfa42
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Control Register A

**Raw Source File**: `data/docs/c64ref/io-map/cia/dc0e-ciacra.md`
**SHA256**: `45dcd3e98bba157a37d74719d3151a105057343aae7d884f326f3de5c3bbfa42`

## Summary



# CIACRA — Control Register A ($DC0E)

## Panoramica
Il registro o area di memoria CIACRA è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$DC0E` (`56334` decimale)
- **Range**: `$DC0E`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
7    Time-of-Day Clock Frequency: 1 = 50 Hz,
       0 = 60 Hz
6    Serial Port I/O Mode Output, 0 = Input
5    Timer A Counts: 1 = CNT Signals,
       0 = Syste...

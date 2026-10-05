---
id: src-dd0c-ci2sdr
type: source
title: 'Source Summary: Serial Data Port'
aliases:
- Serial Data Port
- dd0c-ci2sdr.md
tags:
- io-map
- cia-registers
sources:
- path: data/docs/c64ref/io-map/cia/dd0c-ci2sdr.md
  sha256: 5d57c7bda5a254cdb3e0cea317795430addf51b9cd7601a9e77367958079313b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Serial Data Port

**Raw Source File**: `data/docs/c64ref/io-map/cia/dd0c-ci2sdr.md`
**SHA256**: `5d57c7bda5a254cdb3e0cea317795430addf51b9cd7601a9e77367958079313b`

## Summary



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
     receiv...

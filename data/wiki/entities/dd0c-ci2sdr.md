---
id: dd0c-ci2sdr
type: entity
title: Serial Data Port
aliases:
- Serial Data Port
tags:
- cia-registers
- io-map
sources:
- path: data/docs/c64ref/io-map/cia/dd0c-ci2sdr.md
  sha256: 5d57c7bda5a254cdb3e0cea317795430addf51b9cd7601a9e77367958079313b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-dd0c-ci2sdr
---

# Serial Data Port



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

## References
- Source: [[src-dd0c-ci2sdr]]

---
id: src-dd0f-ci2crb
type: source
title: 'Source Summary: Control Register B'
aliases:
- Control Register B
- dd0f-ci2crb.md
tags:
- io-map
- cia-registers
sources:
- path: data/docs/c64ref/io-map/cia/dd0f-ci2crb.md
  sha256: 8a2d2f27076538a58a95e1aa952bf3d6e85f95579ef605ef5750c527cce4b9bc
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Control Register B

**Raw Source File**: `data/docs/c64ref/io-map/cia/dd0f-ci2crb.md`
**SHA256**: `8a2d2f27076538a58a95e1aa952bf3d6e85f95579ef605ef5750c527cce4b9bc`

## Summary



# CI2CRB — Control Register B ($DD0F)

## Panoramica
Il registro o area di memoria CI2CRB è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$DD0F` (`56591` decimale)
- **Range**: `$DD0F`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
7    Set Alarm/TOD-Clock: 1=Alarm, 0=Clock
6-5  Timer B Mode Select:
       00 = Count System 02 Clock Pulses
       01 = Count Positive CNT Transitions
       ...

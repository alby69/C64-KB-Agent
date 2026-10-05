---
id: src-dd0d-ci2icr
type: source
title: 'Source Summary: Interrupt Control Register'
aliases:
- Interrupt Control Register
- dd0d-ci2icr.md
tags:
- io-map
- cia-registers
sources:
- path: data/docs/c64ref/io-map/cia/dd0d-ci2icr.md
  sha256: cc42b90fcc175eabc5ff759490d1159db9bc878f8ef3b25a22422e4797e00eee
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Interrupt Control Register

**Raw Source File**: `data/docs/c64ref/io-map/cia/dd0d-ci2icr.md`
**SHA256**: `cc42b90fcc175eabc5ff759490d1159db9bc878f8ef3b25a22422e4797e00eee`

## Summary



# CI2ICR — Interrupt Control Register ($DD0D)

## Panoramica
Il registro o area di memoria CI2ICR è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$DD0D` (`56589` decimale)
- **Range**: `$DD0D`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
7    NMI Flag (1 = NMI Occurred) / Set-
       Clear Flag
4    FLAG1 NMI (User/RS-232 Received Data
       Input)
3    Serial Port Interrupt
1    Timer ...

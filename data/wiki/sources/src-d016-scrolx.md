---
id: src-d016-scrolx
type: source
title: 'Source Summary: Horizontal Fine Scrolling and Control Register'
aliases:
- Horizontal Fine Scrolling and Control Register
- d016-scrolx.md
tags:
- io-map
- vic-ii-registers
sources:
- path: data/docs/c64ref/io-map/vic-ii/d016-scrolx.md
  sha256: 189a5eddae66b660c4f3a9938b150b92baae089d4387e462736ccd81d7edff99
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Horizontal Fine Scrolling and Control Register

**Raw Source File**: `data/docs/c64ref/io-map/vic-ii/d016-scrolx.md`
**SHA256**: `189a5eddae66b660c4f3a9938b150b92baae089d4387e462736ccd81d7edff99`

## Summary



# SCROLX — Horizontal Fine Scrolling and Control Register ($D016)

## Panoramica
Il registro o area di memoria SCROLX è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$D016` (`53270` decimale)
- **Range**: `$D016`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
7-6  Unused
5    ALWAYS SET THIS BIT TO 0 !
4    Multi-Color Mode: 1 = Enable (Text or
       Bit-Map)
3    Select 38/40 Column Text...

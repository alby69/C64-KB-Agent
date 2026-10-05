---
id: src-dc0d-ciaicr
type: source
title: 'Source Summary: Interrupt Control Register'
aliases:
- Interrupt Control Register
- dc0d-ciaicr.md
tags:
- io-map
- cia-registers
sources:
- path: data/docs/c64ref/io-map/cia/dc0d-ciaicr.md
  sha256: a965b76609153c5c76308d1e2f4ec919930c539c0410d9d547d8ab573275adec
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Interrupt Control Register

**Raw Source File**: `data/docs/c64ref/io-map/cia/dc0d-ciaicr.md`
**SHA256**: `a965b76609153c5c76308d1e2f4ec919930c539c0410d9d547d8ab573275adec`

## Summary



# CIAICR — Interrupt Control Register ($DC0D)

## Panoramica
Il registro o area di memoria CIAICR è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$DC0D` (`56333` decimale)
- **Range**: `$DC0D`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
7    IRQ Flag (1 = IRQ Occurred) / Set-
       Clear Flag
4    FLAG1 IRQ (Cassette Read / Serial Bus
       SRQ Input)
3    Serial Port Interrupt
2    T...

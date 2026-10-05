---
id: src-d01a-irqmask
type: source
title: 'Source Summary: IRQ Mask Register'
aliases:
- IRQ Mask Register
- d01a-irqmask.md
tags:
- io-map
- vic-ii-registers
sources:
- path: data/docs/c64ref/io-map/vic-ii/d01a-irqmask.md
  sha256: b3488dfee99fdb32a5d04baa52bade146c9c675d6016e13399d64bd7ff38c9c3
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: IRQ Mask Register

**Raw Source File**: `data/docs/c64ref/io-map/vic-ii/d01a-irqmask.md`
**SHA256**: `b3488dfee99fdb32a5d04baa52bade146c9c675d6016e13399d64bd7ff38c9c3`

## Summary



# IRQMASK — IRQ Mask Register ($D01A)

## Panoramica
Il registro o area di memoria IRQMASK è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$D01A` (`53274` decimale)
- **Range**: `$D01A`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
IRQ Mask Register: 1 = Interrupt Enabled

### Mapping the Commodore 64 (Sheldon Leemon)
0    Enable Raster Compare IRQ (1=interrupt enabled)
1    Enable IRQ to...

---
id: src-029f-irqtmp
type: source
title: 'Source Summary: IRQ save during tape I/O'
aliases:
- IRQ save during tape I/O
- 029f-irqtmp.md
tags:
- memory-map
- zero-page
- rom-layout
sources:
- path: data/docs/c64ref/memory-map/029f-irqtmp.md
  sha256: 031d9eb6201899cc7390b42f2363cd81aa504b13915c8bcd49e95db316930f3d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: IRQ save during tape I/O

**Raw Source File**: `data/docs/c64ref/memory-map/029f-irqtmp.md`
**SHA256**: `031d9eb6201899cc7390b42f2363cd81aa504b13915c8bcd49e95db316930f3d`

## Summary



# IRQTMP — IRQ save during tape I/O ($029F)

## Panoramica
Il registro o area di memoria IRQTMP è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$029F` (`671` decimale)
- **Range**: `$029F`-`$02A0`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Holds irq during tape ops

### Commodore-64-intern-Buch (Commodore)
Bei Kassettenoperationen wird hier in
LOW- und HIGH-Byte-Darstellung der
Vekto...

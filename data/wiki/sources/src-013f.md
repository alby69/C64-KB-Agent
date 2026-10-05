---
id: src-013f
type: source
title: 'Source Summary: Prozessorstack'
aliases:
- Prozessorstack
- 013f.md
tags:
- memory-map
- zero-page
- rom-layout
sources:
- path: data/docs/c64ref/memory-map/013f.md
  sha256: 5031af18f7a18cb5877300882f83b9d02472d33ec68e6e6d4da000b279a134b7
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Prozessorstack

**Raw Source File**: `data/docs/c64ref/memory-map/013f.md`
**SHA256**: `5031af18f7a18cb5877300882f83b9d02472d33ec68e6e6d4da000b279a134b7`

## Summary



# $013F — Prozessorstack ($013F)

## Panoramica
Il registro o area di memoria $013F è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$013F` (`319` decimale)
- **Range**: `$013F`-`$01FF`
- **Dimensione**: `193 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Commodore-64-intern-Buch (Commodore)
Der Stack ist generell ein
Zwischenspeicher, in dem der Programmierer
Daten ablegen kann. Außerdem
wird er vom Prozessor dazu
benutzt, bei einem Interrupt oder
einem ...

---
id: src-000a-verck
type: source
title: 'Source Summary: 0 = LOAD, 1 = VERIFY'
aliases:
- 0 = LOAD, 1 = VERIFY
- 000a-verck.md
tags:
- memory-map
- zero-page
- rom-layout
- zero-page
sources:
- path: data/docs/c64ref/memory-map/000a-verck.md
  sha256: 4637bd2b3c10c2dc53a61254793b99eb25f1f99943a853afc5ec8248a5a312de
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: 0 = LOAD, 1 = VERIFY

**Raw Source File**: `data/docs/c64ref/memory-map/000a-verck.md`
**SHA256**: `4637bd2b3c10c2dc53a61254793b99eb25f1f99943a853afc5ec8248a5a312de`

## Summary



# VERCK — 0 = LOAD, 1 = VERIFY ($000A)

## Panoramica
Il registro o area di memoria VERCK è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$000A` (`10` decimale)
- **Range**: `$000A`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Commodore-64-intern-Buch (Commodore)
Weil die Routine von LOAD und VERIFY
identisch ist, wird ein Flag benötigt,
um zu unterscheiden, ob ein LOAD oder
ein VERIFY-Vorgang ausgeführt worden
ist.

### C64 Progra...

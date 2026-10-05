---
id: src-007a-txtptr
type: source
title: 'Source Summary: Basic pointer (within subrtn)'
aliases:
- Basic pointer (within subrtn)
- 007a-txtptr.md
tags:
- memory-map
- zero-page
- rom-layout
- zero-page
sources:
- path: data/docs/c64ref/memory-map/007a-txtptr.md
  sha256: 0bcfdac18e9df92ca3b070a8e4fa98598f5f07ef28a81fcb8d29a08e95d57514
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Basic pointer (within subrtn)

**Raw Source File**: `data/docs/c64ref/memory-map/007a-txtptr.md`
**SHA256**: `0bcfdac18e9df92ca3b070a8e4fa98598f5f07ef28a81fcb8d29a08e95d57514`

## Summary



# TXTPTR — Basic pointer (within subrtn) ($007A)

## Panoramica
Il registro o area di memoria TXTPTR è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$007A` (`122` decimale)
- **Range**: `$007A`-`$007B`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Commodore-64-intern-Buch (Commodore)
In diesen Speicherzellen wird in LOW-
und HIGH-Byte die Anfangsadresse des
als nächstes auszuführenden Befehls
im BASIC-RAM angegeben.

### C64 Program...

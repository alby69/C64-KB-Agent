---
id: 007a-txtptr
type: entity
title: Basic pointer (within subrtn)
aliases:
- Basic pointer (within subrtn)
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/007a-txtptr.md
  sha256: 0bcfdac18e9df92ca3b070a8e4fa98598f5f07ef28a81fcb8d29a08e95d57514
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-007a-txtptr
---

# Basic pointer (within subrtn)



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

### C64 Programmer's Reference Guide (Commodore)
Pointer: Current Byte of BASIC Text

### Memory Map (Jim Butterfield)
Basic pointer (within subrtn)

### 64map (—)
Pointer: Current Byte of BASIC Text

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-007a-txtptr]]

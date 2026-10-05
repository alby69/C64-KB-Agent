---
id: 0079-chrgot
type: entity
title: CHRGOT. Read current byte from BASIC program or direct command
aliases:
- CHRGOT. Read current byte from BASIC program or direct command
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0079-chrgot.md
  sha256: a62ec0330ea1613783fa19b9f85ccbe8e6aff36e3609f59d468c74cbe9ffa903
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0079-chrgot
---

# CHRGOT. Read current byte from BASIC program or direct command



# CHRGOT — CHRGOT. Read current byte from BASIC program or direct command ($0079)

## Panoramica
Il registro o area di memoria CHRGOT è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0079` (`121` decimale)
- **Range**: `$0079`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
Entry to Get Same Byte of Text Again

### Reference (Joe Forster / STA)
Pointer to current byte in BASIC program or direct command.

### 64map (—)
Entry to Get same Byte again

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-0079-chrgot]]

---
id: 00a4-firt
type: entity
title: Cycle count
aliases:
- Cycle count
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/00a4-firt.md
  sha256: 4f33c1cbe69c5bf2c873c826ae6e024f72f0e2eb2bac7cda0c7a0cd0609e4624
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-00a4-firt
---

# Cycle count



# FIRT — Cycle count ($00A4)

## Panoramica
Il registro o area di memoria FIRT è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00A4` (`164` decimale)
- **Range**: `$00A4`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Temp used by serial routine

### Original Source Comments (Microsoft/Commodore)
Cassette: used to indicate which half of dipole we're in

### Commodore-64-intern-Buch (Commodore)
siehe oben

### Memory Map (Jim Butterfield)
Cycle count

### Reference (Joe Forster / STA)
Byte buffer during serial bus input. Parity during datasette input/output

### 64map (—)
Pulse Counter Tape Read or Write/Serial Bus shift Counter

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-00a4-firt]]

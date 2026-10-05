---
id: 006e-argsgn
type: entity
title: Vorzeichen von ARG
aliases:
- Vorzeichen von ARG
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/006e-argsgn.md
  sha256: 81775ae74b3a3a71339971ba24348958e972009e65379d530a502b8cd7d86c3c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-006e-argsgn
---

# Vorzeichen von ARG



# ARGSGN — Vorzeichen von ARG ($006E)

## Panoramica
Il registro o area di memoria ARGSGN è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$006E` (`110` decimale)
- **Range**: `$006E`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)


### Commodore-64-intern-Buch (Commodore)
Hier wird angegeben, ob der Wert, der
im ARG steht, positiv oder negativ ist.

### C64 Programmer's Reference Guide (Commodore)
Floating Accum. #2: Sign

### Mapping the Commodore 64 (Sheldon Leemon)
Floating Point Accumulator #2: Sign

### Reference (Joe Forster / STA)
Bits:

* Bit #7: 0 = Positive; 1 = Negative.

### 64map (—)
AFAC Sign

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-006e-argsgn]]

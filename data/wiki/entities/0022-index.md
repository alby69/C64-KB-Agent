---
id: 0022-index
type: entity
title: Utility pointer area
aliases:
- Utility pointer area
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0022-index.md
  sha256: d4add49464c1aeb823045d9cf578aec41a9d811aff2619ff920b6c9c4ee5289e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0022-index
---

# Utility pointer area



# INDEX — Utility pointer area ($0022)

## Panoramica
Il registro o area di memoria INDEX è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0022` (`34` decimale)
- **Range**: `$0022`-`$0025`
- **Dimensione**: `4 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Indexes

### Original Source Comments (Microsoft/Commodore)


### Commodore-64-intern-Buch (Commodore)
Diese Speicherzellen benutzt der
Interpreter, um verschiedene
Zwischenergebnisse zu speichern.

### C64 Programmer's Reference Guide (Commodore)
Utility Pointer Area

### C64 Programmer's Reference Guide (Commodore)
First Utility Pointer

### Memory Map (Jim Butterfield)
Utility pointer area

### Mapping the Commodore 64 (Sheldon Leemon)
This area is used by many BASIC routines to hold temporary pointers
and calculation results.

### Reference (Joe Forster / STA)
Temporary area for various operations (4 bytes)

### 64'er Magazin (64'er)
Diese vier Speicherzellen werden vom Basic-Übersetzer (Interpreter) für
verschiedene Zwischenergebnisse und Flaggen benutzt, die aber dem Programmierer
nichts nutzen.

### 64map (—)
Utility Pointer Area

### 64map (—)
First Utility Pointer

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-0022-index]]

---
title: 'Register für Arithmetik, Akku #4'
source_url: https://github.com/mist64/c64ref/blob/main/src/c64mem/reference.txt
category: reference
topics:
- memory-map
- zero-page
- rom-layout
- zero-page
difficulty: beginner
language: assembly
hardware:
- C64
related: []
scraped_at: '2026-07-29'
c64ref:
  module: c64mem
  source_files:
  - reference.txt
  - original_source_comments.txt
  - commodore-64-intern-buch.txt
  - c64_programmer's_reference_guide.txt
  - 64map.txt
  address: $005C
  address_end: $0060
  symbol: TEMPF2
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: ''
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: siehe oben
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Temporary storage for FLPT value
  - name: Reference
    author: Joe Forster / STA
    description: 'Arithmetic register #4 (5 bytes)'
  - name: 64map
    author: —
    description: Temporary storage for FLPT value
---

# TEMPF2 — Register für Arithmetik, Akku #4 ($005C)

## Panoramica
Il registro o area di memoria TEMPF2 è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$005C` (`92` decimale)
- **Range**: `$005C`-`$0060`
- **Dimensione**: `5 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)


### Commodore-64-intern-Buch (Commodore)
siehe oben

### C64 Programmer's Reference Guide (Commodore)
Temporary storage for FLPT value

### Reference (Joe Forster / STA)
Arithmetic register #4 (5 bytes)

### 64map (—)
Temporary storage for FLPT value

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
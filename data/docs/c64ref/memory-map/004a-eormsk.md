---
title: Value of third parameter during WAIT. Device number during OPEN
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
related:
- f34a-open
scraped_at: '2026-07-29'
c64ref:
  module: c64mem
  source_files:
  - reference.txt
  - original_source_comments.txt
  address: $004A
  symbol: EORMSK
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: The mask for EORing in wait
  - name: Reference
    author: Joe Forster / STA
    description: Value of third parameter during WAIT. Device number during OPEN
---

# EORMSK — Value of third parameter during WAIT. Device number during OPEN ($004A)

## Panoramica
Il registro o area di memoria EORMSK è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$004A` (`74` decimale)
- **Range**: `$004A`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
The mask for EORing in wait

### Reference (Joe Forster / STA)
Value of third parameter during WAIT. Device number during OPEN

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
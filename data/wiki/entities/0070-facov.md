---
id: 0070-facov
type: entity
title: Accum#l lo-order (rounding)
aliases:
- Accum#l lo-order (rounding)
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0070-facov.md
  sha256: 6081c7217f7bbc7c2d240357a6acc3a3a75bc8354ee0bca4f67a4769298a9976
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0070-facov
---

# Accum#l lo-order (rounding)



# FACOV — Accum#l lo-order (rounding) ($0070)

## Panoramica
Il registro o area di memoria FACOV è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0070` (`112` decimale)
- **Range**: `$0070`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Overflow byte of the FAC

### Commodore-64-intern-Buch (Commodore)
FAC-Rundungsbyte

### C64 Programmer's Reference Guide (Commodore)
Floating Accum. #1. Low-Order (Rounding)

### Memory Map (Jim Butterfield)
Accum#l lo-order (rounding)

### Mapping the Commodore 64 (Sheldon Leemon)
If the mantissa of the floating point number has more significant
figures than can be held in four bytes, the least significant figures
are placed here.  They are used to extend the accuracy of intermediate
mathematical operations and to round to the final figure.

### 64'er Magazin (64'er)
Es kann vorkommen, daß die Mantisse einer Gleitkommazahl mehr Stellen hat, als
mit den vier Mantissen-Bytes des Akkumulators Nr. 1 (Zelle 97 bis 102)
dargestellt werden können. In diesem Fall werden die hintersten, das heißt die
unwichtigsten Stellen hinter dem Komma in der Zelle 112 abgelegt. Von dort
werden sie geholt, um die Genauigkeit von mathematischen Operationen zu erhöhen
und auch um Endresultate abrunden zu können.

### 64map (—)
FAC low-order rounding

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-0070-facov]]

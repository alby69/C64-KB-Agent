---
id: 0062-facho
type: entity
title: 'Accum#l : Mantissa'
aliases:
- 'Accum#l : Mantissa'
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0062-facho.md
  sha256: a45d99ad5300d0e4b33a2d28e74120dd68666d7c3686a183cdd2b7e440604dae
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0062-facho
---

# Accum#l : Mantissa



# FACHO — Accum#l : Mantissa ($0062)

## Panoramica
Il registro o area di memoria FACHO è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0062` (`98` decimale)
- **Range**: `$0062`-`$0065`
- **Dimensione**: `4 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Most significant byte of mantissa

### C64 Programmer's Reference Guide (Commodore)
Floating Accum. #1: Mantissa

### Memory Map (Jim Butterfield)
Accum#l : Mantissa

### Mapping the Commodore 64 (Sheldon Leemon)
The most significant digit can be assumed to be a 1 (remember that the
range of the mantissa is from 1 to 1.99999...) when a floating point
number is stored to a variable.  The first bit is used for the sign of
the number, and the other 31 bits of the four-byte mantissa hold the
other significant digits.

The first two bytes (98-99, $0062-$0063) of this location will hold the
signed integer result of a floating point to integer conversion, in
high-byte, low- byte order.

### 64map (—)
FAC Mantissa

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-0062-facho]]

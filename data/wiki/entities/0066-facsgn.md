---
id: 0066-facsgn
type: entity
title: 'Accum#l : Sign'
aliases:
- 'Accum#l : Sign'
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0066-facsgn.md
  sha256: fe62a664e2cac877d36f2addb245e86e98e0ee1c4498438c86b4603bb8a26cc2
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0066-facsgn
---

# Accum#l : Sign



# FACSGN — Accum#l : Sign ($0066)

## Panoramica
Il registro o area di memoria FACSGN è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0066` (`102` decimale)
- **Range**: `$0066`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Sign of FAC (0 or -1) when unpacked

### Commodore-64-intern-Buch (Commodore)
Der Zeiger gibt an, ob der Wert, der
im FAC steht, positiv oder negativ
ist.

### C64 Programmer's Reference Guide (Commodore)
Floating Accum. #1: Sign

### Memory Map (Jim Butterfield)
Accum#l : Sign

### Mapping the Commodore 64 (Sheldon Leemon)
A value of 0 here indicates a positive number, while a value of 255
($FF) indicates a negative number.

### Reference (Joe Forster / STA)
Bits:

* Bit #7: 0 = Positive; 1 = Negative.

### 64map (—)
FAC Sign

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-0066-facsgn]]

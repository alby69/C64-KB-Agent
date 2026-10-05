---
id: 004d-opmask
type: entity
title: Comparison symbol accumulator
aliases:
- Comparison symbol accumulator
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/004d-opmask.md
  sha256: 3640ce6bb4ccb2ed4ad479229b425875635ec368938d3dc8ab390adda4b058eb
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-004d-opmask
---

# Comparison symbol accumulator



# OPMASK — Comparison symbol accumulator ($004D)

## Panoramica
Il registro o area di memoria OPMASK è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$004D` (`77` decimale)
- **Range**: `$004D`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Mask created by current operator

### Commodore-64-intern-Buch (Commodore)
Dieser Zeiger wird von mathematischen
Routinen als Vergleichsoperator
verwendet, daß heißt um festzustellen,
ob ein Wert kleiner, gleich oder
größer ist.

### C64 Programmer's Reference Guide (Commodore)
Mask used during FRMEVL

### Memory Map (Jim Butterfield)
Comparison symbol accumulator

### Mapping the Commodore 64 (Sheldon Leemon)
The expression evaluation routine creates a mask here which lets it
know whether the current comparison operation is a less-than (1),
equals (2), or greater-than (4) comparison.

### Reference (Joe Forster / STA)
Bits:

* Bit #1: 1 = ">" (greater than) is present in expression.
* Bit #2: 1 = "=" (equal to) is present in expression.
* Bit #3: 1 = "<" (less than) is present in expression.

### 64'er Magazin (64'er)
Die bei 75 und 76 schon erwähnte Auswertungs-Routine FRMEVL erzeugt in der
Speicherzelle 77 einen Wert, der angibt, ob es sich bei einer
Vergleichsoperation um den Fall »kleiner als« (<), »gleich wie« (=) oder
»größer als« (>) handelt. Diese Speicherzelle ist nur im Maschinencode
erreichbar.

### 64map (—)
Mask used during FRMEVL

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-004d-opmask]]

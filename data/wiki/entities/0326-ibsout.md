---
id: 0326-ibsout
type: entity
title: Output vector ($F1CA)
aliases:
- Output vector ($F1CA)
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0326-ibsout.md
  sha256: 6b265b91dde483ab6a469d1fffe2ed22920144789fd9b3d1c825187d91fcb24f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0326-ibsout
---

# Output vector ($F1CA)



# IBSOUT — Output vector ($F1CA) ($0326)

## Panoramica
Il registro o area di memoria IBSOUT è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0326` (`806` decimale)
- **Range**: `$0326`-`$0327`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)


### Commodore-64-intern-Buch (Commodore)
$F1CA OUTPUT-Vektor

### C64 Programmer's Reference Guide (Commodore)
KERNAL CHROUT Routine

### Memory Map (Jim Butterfield)
Output vector ($F1CA)

### Mapping the Commodore 64 (Sheldon Leemon)
Vector to Kernal CHROUT Routine (Currently at 61898 ($F1CA))

### Reference (Joe Forster / STA)
Default: $F1CA.

### 64'er Magazin (64'er)
Die CHROUT-Routine entspricht der CHRIN-Routine in der anderen Richtung. Sie
bedeutet »Character Output« und transferiert ein Byte, das im Akkumulator
steht, in den Puffer des angewählten Ausgabegerätes. Sie beginnt ab Adresse
62898 ($F1CA), - beim VC 20 ab 62074 ($F27A).

### 64map (—)
Vector: Indirect entry to Kernal CHROUT Routine ($F1CA)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-0326-ibsout]]

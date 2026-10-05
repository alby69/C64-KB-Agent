---
id: 0332-isave
type: entity
title: SAVE link ($F5ED)
aliases:
- SAVE link ($F5ED)
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0332-isave.md
  sha256: 4edf0a972a303c3b1aab02c6a2c3d573f58d952dc7e4df3ad8ebfd36c9e5d863
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0332-isave
---

# SAVE link ($F5ED)



# ISAVE — SAVE link ($F5ED) ($0332)

## Panoramica
Il registro o area di memoria ISAVE è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0332` (`818` decimale)
- **Range**: `$0332`-`$0333`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
savesp

### Commodore-64-intern-Buch (Commodore)
$F5ED SAVE-Vektor

### C64 Programmer's Reference Guide (Commodore)
KERNAL SAVE Routine Vector

### Memory Map (Jim Butterfield)
SAVE link ($F5ED)

### Mapping the Commodore 64 (Sheldon Leemon)
Vector: Kernal SAVE Routine (Currently at 62941 ($F5DD))

### Reference (Joe Forster / STA)
Default: $F5ED.

### 64'er Magazin (64'er)
Diese Routine ist das Gegenstück zur LOAD-Routine. Sie beginnt ab Adresse 62941
($F5DD) - beim VC 20 ab 63103 ($F685).

### 64map (—)
Vector: Indirect entry to Kernal SAVE Routine ($F5ED)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-0332-isave]]

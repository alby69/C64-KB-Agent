---
id: 006f-arisgn
type: entity
title: 'Sign comparison, Acc#l vs #2'
aliases:
- 'Sign comparison, Acc#l vs #2'
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/006f-arisgn.md
  sha256: 326733ab4805c42a4e3e37739a46712317807bf6ac234be111c73b80b562782b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-006f-arisgn
---

# Sign comparison, Acc#l vs #2



# ARISGN — Sign comparison, Acc#l vs #2 ($006F)

## Panoramica
Il registro o area di memoria ARISGN è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$006F` (`111` decimale)
- **Range**: `$006F`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
A sign reflecting the result

### Original Source Comments (Microsoft/Commodore)
Pointer to a string or descriptor

### Commodore-64-intern-Buch (Commodore)
Diese Speicherzelle gibt dem
Interpreter an, ob die Vorzeichen der
beiden Akkus übereinstimmen.

### C64 Programmer's Reference Guide (Commodore)
Sign Comparison Result: Accum. # 1 vs #2

### Memory Map (Jim Butterfield)
Sign comparison, Acc#l vs #2

### Mapping the Commodore 64 (Sheldon Leemon)
Used to indicate whether the two Floating Point Accumulators have like
or unlike signs.  A 0 indicates like signs, a 255 ($FF) indicates
unlike signs.

### Reference (Joe Forster / STA)
Pointer to first string expression during string comparison

### 64'er Magazin (64'er)
Wenn die Zahl in beiden Akkumulatoren gleiche Vorzeichen hat, steht in
Speicherzelle 111 eine 0, bei verschiedenen Vorzeichen eine 255.

### 64map (—)
Sign of result of Arithmetic Evaluation

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-006f-arisgn]]

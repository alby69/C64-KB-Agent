---
id: 0067-sgnflg
type: entity
title: Series evaluation constant pointer
aliases:
- Series evaluation constant pointer
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0067-sgnflg.md
  sha256: b9f0b806a1a3d4c2b5a4458d8ab8ef1f01e8c468c552d96c3c76400dd74c768d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0067-sgnflg
---

# Series evaluation constant pointer



# SGNFLG — Series evaluation constant pointer ($0067)

## Panoramica
Il registro o area di memoria SGNFLG è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0067` (`103` decimale)
- **Range**: `$0067`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Sign of FAC is preserved here by "FIN"

### Original Source Comments (Microsoft/Commodore)
A count used by polynomials

### Commodore-64-intern-Buch (Commodore)
Diese Speicherzelle dient als Zähler
für die Polynomauswertung.

### C64 Programmer's Reference Guide (Commodore)
Pointer: Series Evaluation Constant

### Memory Map (Jim Butterfield)
Series evaluation constant pointer

### Mapping the Commodore 64 (Sheldon Leemon)
This location is used by mathematical formula evaluation routines.  It
indicates the number of separate evaluations that must be done to
resolve a complex expression down to a single term.

### Reference (Joe Forster / STA)
Number of degrees during polynomial evaluation

### 64'er Magazin (64'er)
Diese Adresse wird von zwei Routinen verwendet. Der Basic-Übersetzer benutzt
sie als Vorzeichenspeicher bei der Umwandlung von Zahlen aus dem ASCII-Format
in Gleitkommazahlen. Das Betriebssystem verwendet diese Adresse als Zähler der
Abarbeitungsschritte bei der Berechnung eines Polynoms der Form
y=a0+a1*x+a2*x^2+a3*x^3+...

### 64map (—)
Pointer: Series Evaluation Constant

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-0067-sgnflg]]

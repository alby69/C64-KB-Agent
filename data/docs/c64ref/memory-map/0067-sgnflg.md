---
title: Series evaluation constant pointer
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
  - 64'er_magazin.txt
  - mapping_the_commodore_64.txt
  - memory_map.txt
  - c64_programmer's_reference_guide.txt
  - 64map.txt
  address: $0067
  symbol: SGNFLG
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Sign of FAC is preserved here by "FIN"
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: A count used by polynomials
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Diese Speicherzelle dient als Zähler
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Pointer: Series Evaluation Constant'
  - name: Memory Map
    author: Jim Butterfield
    description: Series evaluation constant pointer
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This location is used by mathematical formula evaluation routines.  It
  - name: Reference
    author: Joe Forster / STA
    description: Number of degrees during polynomial evaluation
  - name: 64'er Magazin
    author: 64'er
    description: Diese Adresse wird von zwei Routinen verwendet. Der Basic-Übersetzer
      benutzt
  - name: 64map
    author: —
    description: 'Pointer: Series Evaluation Constant'
---

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
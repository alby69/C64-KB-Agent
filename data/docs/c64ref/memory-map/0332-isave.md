---
title: SAVE link ($F5ED)
source_url: https://github.com/mist64/c64ref/blob/main/src/c64mem/reference.txt
category: reference
topics:
- memory-map
- zero-page
- rom-layout
difficulty: intermediate
language: assembly
hardware:
- C64
related:
- f5ed-save
- f5ed-standard-save-ram-entry
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
  address: $0332
  address_end: $0333
  symbol: ISAVE
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: savesp
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: $F5ED SAVE-Vektor
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: KERNAL SAVE Routine Vector
  - name: Memory Map
    author: Jim Butterfield
    description: SAVE link ($F5ED)
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: 'Vector: Kernal SAVE Routine (Currently at 62941 ($F5DD))'
  - name: Reference
    author: Joe Forster / STA
    description: 'Default: $F5ED.'
  - name: 64'er Magazin
    author: 64'er
    description: Diese Routine ist das Gegenstück zur LOAD-Routine. Sie beginnt ab
      Adresse 62941
  - name: 64map
    author: —
    description: 'Vector: Indirect entry to Kernal SAVE Routine ($F5ED)'
---

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
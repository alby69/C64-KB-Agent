---
title: Get arithmetic element link
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
  address: $030A
  address_end: $030B
  symbol: IEVAL
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: indirect EVAL (symbol evaluation)
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: $AE86 Vektor für Ausdruck auswerten
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Vector: BASIC Token Evaluation'
  - name: Memory Map
    author: Jim Butterfield
    description: Get arithmetic element link
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This vector points to the address of the EVAL routine at 44678 ($AE86)
  - name: Reference
    author: Joe Forster / STA
    description: 'Default: $AE86.'
  - name: 64'er Magazin
    author: 64'er
    description: Dieser Vektor zeigt auf 44675 ($AE83), beim VC 20 auf 52867 ($CE83).
      Hier
  - name: 64map
    author: —
    description: 'Vector: Indirect entry to BASIC Token evaluation ($AE86)'
---

# IEVAL — Get arithmetic element link ($030A)

## Panoramica
Il registro o area di memoria IEVAL è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$030A` (`778` decimale)
- **Range**: `$030A`-`$030B`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
indirect EVAL (symbol evaluation)

### Commodore-64-intern-Buch (Commodore)
$AE86 Vektor für Ausdruck auswerten

### C64 Programmer's Reference Guide (Commodore)
Vector: BASIC Token Evaluation

### Memory Map (Jim Butterfield)
Get arithmetic element link

### Mapping the Commodore 64 (Sheldon Leemon)
This vector points to the address of the EVAL routine at 44678 ($AE86)
which, among other things, is used to evaluate BASIC functions such as
INT and ABS.

### Reference (Joe Forster / STA)
Default: $AE86.

### 64'er Magazin (64'er)
Dieser Vektor zeigt auf 44675 ($AE83), beim VC 20 auf 52867 ($CE83). Hier
beginnt eine Routine, die einen einzelnen numerischen Wert, wenn er Teil eines
Ausdrucks ist, von seinem ASCII-Wert in eine Gleitkomma-Zahl umwandelt.

Ist der Ausdruck eine Konstante, wird diese Umwandlung durchgeführt.

Ist der Ausdruck eine Variable, wird ihr Zahlenwert aus dem Variablenspeicher geholt.

Ist der Ausdruck die Zahl »pi«, wird der Zahlenwert für »pi« in den Gleitkomma-Akkumulator gebracht.

### 64map (—)
Vector: Indirect entry to BASIC Token evaluation ($AE86)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
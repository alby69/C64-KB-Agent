---
title: Subscript/FNx flag
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
  address: $0010
  symbol: SUBFLG
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: '"FOR" and user-defined function'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Hier wird angezeigt, ob es sich um eine
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Flag: Subscript Ref / User Function Call'
  - name: Memory Map
    author: Jim Butterfield
    description: Subscript/FNx flag
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This flag is used by the PTRGET routine which finds or creates a
  - name: Reference
    author: Joe Forster / STA
    description: 'Values:'
  - name: 64'er Magazin
    author: 64'er
    description: Im Basic-Übersetzer gibt es eine Routine, die den Speicher absucht,
      ob es eine
  - name: 64map
    author: —
    description: 'Flag: Subscript reference/User Function call'
---

# SUBFLG — Subscript/FNx flag ($0010)

## Panoramica
Il registro o area di memoria SUBFLG è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0010` (`16` decimale)
- **Range**: `$0010`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
"FOR" and user-defined function
pointer fetching turn
this on before calling "PTRGET"
so arrays won't be detected.
"STKINI" and "PTRGET" clear it.
Also disallows integers there.

### Commodore-64-intern-Buch (Commodore)
Hier wird angezeigt, ob es sich um eine
Array-Variable oder um eine mit DEF FN
definierte Variable handelt.

### C64 Programmer's Reference Guide (Commodore)
Flag: Subscript Ref / User Function Call

### Memory Map (Jim Butterfield)
Subscript/FNx flag

### Mapping the Commodore 64 (Sheldon Leemon)
This flag is used by the PTRGET routine which finds or creates a
variable, at the time it checks whether the name of a variable is
valid.  If an opening parenthesis is found, this flag is set to
indicate that the variable in question is either an array variable or
a user-defined function.

You should note that it is perfectly legal for a user-defined function
(FN) to have the same name as a floating point variable.  Moreover, it
is also legal to redefine a function.  Using a FN name in an already
defined function results in the new definition of the function.

### Reference (Joe Forster / STA)
Values:

* $00: Integer variables are accepted.
* $01-$FF: Integer variables are not accepted.

### 64'er Magazin (64'er)
Im Basic-Übersetzer gibt es eine Routine, die den Speicher absucht, ob es eine
Variable mit bestimmten Namen bereits gibt. Wenn diese mit einer Klammer
beginnt, wird die Flagge in Zelle 16 gesetzt, um anzuzeigen, daß es sich um
eine Array-Variable oder um eine mit DEF FN selbstdefinierte Funktion handelt.

### 64map (—)
Flag: Subscript reference/User Function call

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
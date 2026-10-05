---
id: 0010-subflg
type: entity
title: Subscript/FNx flag
aliases:
- Subscript/FNx flag
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0010-subflg.md
  sha256: 6ebb7a66f8e1ced936ab39f4e4890fff4c4d0b0afc71cef7917f9c917f97389b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0010-subflg
---

# Subscript/FNx flag



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

## References
- Source: [[src-0010-subflg]]

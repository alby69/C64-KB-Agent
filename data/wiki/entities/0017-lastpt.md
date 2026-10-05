---
id: 0017-lastpt
type: entity
title: Last temp string vector
aliases:
- Last temp string vector
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0017-lastpt.md
  sha256: 72344582f4e189b904a4d51dcf0a3762c02d07dfc53b89e017558e6a274e72b4
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0017-lastpt
---

# Last temp string vector



# LASTPT — Last temp string vector ($0017)

## Panoramica
Il registro o area di memoria LASTPT è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0017` (`23` decimale)
- **Range**: `$0017`-`$0018`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Pointer to last-used string temporary

### Commodore-64-intern-Buch (Commodore)
Der Inhalt dieser beiden Bytes zeigt
auf den zuletzt verwendeten
Speicherplatz.

### C64 Programmer's Reference Guide (Commodore)
Last Temp String Address

### Memory Map (Jim Butterfield)
Last temp string vector

### Mapping the Commodore 64 (Sheldon Leemon)
This pointer indicates the last slot used in the temporary string
descriptor stack.  Therefore, the value stored at 23 ($0017) should be 3
less than that stored at 22 ($0016), while 24 ($0018) will contain a 0.

### Reference (Joe Forster / STA)
Pointer to previous expression in string stack

### 64'er Magazin (64'er)
Der Inhalt dieser 2 Byte zeigt auf den zuletzt benutzten Speicherplatz
Innerhalb der Adresse 22 bis 33. Das heißt, daß der Wert in 23 ($0017) immer um 3
kleiner ist als der in 22 ($0016), während der Wert in 24 ($0018) eine Null ist.

### 64map (—)
Last temporary String Address

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-0017-lastpt]]

---
id: 0008-endchr
type: entity
title: Scan-quotes flag
aliases:
- Scan-quotes flag
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0008-endchr.md
  sha256: d5550222d8df438045986caaae443ab60ae1db10813a46db6421ab1a91cb2701
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0008-endchr
---

# Scan-quotes flag



# ENDCHR — Scan-quotes flag ($0008)

## Panoramica
Il registro o area di memoria ENDCHR è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0008` (`8` decimale)
- **Range**: `$0008`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
The other delimiting character

### Commodore-64-intern-Buch (Commodore)
Während der Umwandlung von
BASIC-Befehlen in Tokens wird die
Speicherzelle $0008 als Zwischenspeicher
für BASIC-Texteingaben verwendet.

### C64 Programmer's Reference Guide (Commodore)
Flag: Scan for Quote at End of String

### Memory Map (Jim Butterfield)
Scan-quotes flag

### Mapping the Commodore 64 (Sheldon Leemon)
Like location 7, this location is used as a work byte during the
tokenization of a BASIC statement.  Most of the time, its value is 0
or 34.

### Reference (Joe Forster / STA)
Byte being search for during various operations. Current byte of BASIC line during tokenization. High byte of first integer operand during AND and OR

### 64'er Magazin (64'er)
Wie Speicherzelle 7 dient auch die Zelle 8 als Zwischenspeicher für Basic-
Texteingabe und zwar während der Umwandlung von Basic-Befehlen in den vom
Computer verwendeten Befehlscode (Tokens). Die Speicherzelle 8 ist in Basic
nicht verwertbar.

### 64map (—)
Flag: Scan for Quote at end of String

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-0008-endchr]]

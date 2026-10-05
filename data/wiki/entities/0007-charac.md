---
id: 0007-charac
type: entity
title: Search character
aliases:
- Search character
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0007-charac.md
  sha256: 212854b43c808b9a9b6eaf0b151653adc1f457da3d070f7b038b057188daddc6
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0007-charac
---

# Search character



# CHARAC — Search character ($0007)

## Panoramica
Il registro o area di memoria CHARAC è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0007` (`7` decimale)
- **Range**: `$0007`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
A delimiting character

### Original Source Comments (Microsoft/Commodore)
A one-byte integer from "QINT"

### Commodore-64-intern-Buch (Commodore)
Die Speicherzelle $0007 wird oft von
BASIC-Programmen als Suchzeiger für
Texteingaben verwendet.

### C64 Programmer's Reference Guide (Commodore)
Search Character

### Memory Map (Jim Butterfield)
Search character

### Mapping the Commodore 64 (Sheldon Leemon)
This location and the next are used heavily by the BASIC routines that
scan the text that comes into the buffer at 512 ($0200), in order to
detect significant characters such as quotes, comma, the colon which
separates BASIC statements, and end-of-line.  The ASCII values of such
special characters are usually stored here.

This location is also used as a work area by other BASIC routines that
do not involve scanning text.

### Reference (Joe Forster / STA)
Byte being searched for during various operations. Current digit of number being input

### Reference (Joe Forster / STA)
Low byte of first integer operand during AND and OR. Low byte of integer-format FAC during INT()

### 64'er Magazin (64'er)
Diese Speicherzelle wird viel von denjenigen Basic-Routinen als
Zwischenspeicher benutzt, die den direkt eingegebenen Text absuchen, um
Steuerzeichen (Gänsefüße, Kommata, Doppelpunkte und die Zeilenbeendigung durch
die RETURN-Taste) rechtzeitig zu erkennen. Normalerweise wird in der Zelle 7
der ASCII-Wert dieser Zeichen abgelegt. Die Speicherzelle 7 wird aber auch von
anderen Basic-Routinen benutzt. Sie ist daher für den Programmierer praktisch
nicht zu verwerten.

### 64map (—)
Temporary Integer during OR/AND

### 64map (—)
Search Character/Temporary Integer during INT

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-0007-charac]]

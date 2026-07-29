---
title: Search character
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
  address: $0007
  symbol: CHARAC
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: A delimiting character
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: A one-byte integer from "QINT"
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Die Speicherzelle $0007 wird oft von
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Search Character
  - name: Memory Map
    author: Jim Butterfield
    description: Search character
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This location and the next are used heavily by the BASIC routines
      that
  - name: Reference
    author: Joe Forster / STA
    description: Byte being searched for during various operations. Current digit
      of number be...
  - name: Reference
    author: Joe Forster / STA
    description: Low byte of first integer operand during AND and OR. Low byte of
      integer-form...
  - name: 64'er Magazin
    author: 64'er
    description: Diese Speicherzelle wird viel von denjenigen Basic-Routinen als
  - name: 64map
    author: —
    description: Temporary Integer during OR/AND
  - name: 64map
    author: —
    description: Search Character/Temporary Integer during INT
---

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
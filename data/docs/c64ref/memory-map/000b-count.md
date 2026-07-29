---
title: Input buffer pointer/# subscrpt
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
  address: $000B
  symbol: COUNT
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: A general counter
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Die Speicherzelle $000B wird dazu
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Input Buffer Pointer / No. of Subscripts
  - name: Memory Map
    author: Jim Butterfield
    description: Input buffer pointer/# subscrpt
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: The routines that convert the text in the input buffer at 512 ($0200)
  - name: Reference
    author: Joe Forster / STA
    description: Current token during tokenization. Length of BASIC line during insertion
      of l...
  - name: 64'er Magazin
    author: 64'er
    description: Alle Buchstaben und Zeichen, die mit der Tastatur direkt eingetippt
      werden,
  - name: 64map
    author: —
    description: Input Buffer Pointer/Number of Subscripts
---

# COUNT — Input buffer pointer/# subscrpt ($000B)

## Panoramica
Il registro o area di memoria COUNT è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$000B` (`11` decimale)
- **Range**: `$000B`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
A general counter

### Commodore-64-intern-Buch (Commodore)
Die Speicherzelle $000B wird dazu
verwendet, die Anzahl der Dimensionen
zu berechnen. Außerdem wird noch die
Länge der Tokenzeile hier angegeben.

### C64 Programmer's Reference Guide (Commodore)
Input Buffer Pointer / No. of Subscripts

### Memory Map (Jim Butterfield)
Input buffer pointer/# subscrpt

### Mapping the Commodore 64 (Sheldon Leemon)
The routines that convert the text in the input buffer at 512 ($0200)
into lines of executable program tokes, and the routines that link
these program lines together, use this location as an index into the
input buffer area.  When the job of converting text to tokens is
finished, the value in this location is equal to the length of the
tokenized line.

The routines which build an array or locate an element in an array use
this location to calculate the number of DIMensions called for and the
amount of storage required for a newly created array, or the number of
subscripts specified when referencing an array element.

### Reference (Joe Forster / STA)
Current token during tokenization. Length of BASIC line during insertion of line. AND/OR switch; $00 = AND; $FF = OR. Number of dimensions during array operations

### 64'er Magazin (64'er)
Alle Buchstaben und Zeichen, die mit der Tastatur direkt eingetippt werden,
kommen in einen Eingabe-Pufferspeicher.

Er beginnt ab Speicherzelle 512 ($0200). Sobald die RETURN-Taste gedrückt wird,
wandelt eine Routine des Basic-Übersetzers den Text in Codezahlen (Tokens) um.
Diese Routine und eine andere, welche die Zeilen eines Programms
aneinanderhängt, verwenden die Zelle 11 als Zwischenspeicher.

Sobald die Textumwandlung beendet ist, steht in Zelle 11 eine Zahl, die die
Länge der Token-Zeile angibt.

Die Zelle 11 wird außerdem noch von den Basic-Routinen benutzt, die ein Feld
(Array) aufbauen oder ein bestimmtes Element in einem Array suchen. Was ein
Feld oder Array ist, finden Sie in den Commodore-Handbüchern gut beschrieben.
Außerdem gehe ich bei der Behandlung der Speicherzellen 47 bis 50 näher darauf
ein.

Diese Routinen also verwenden die Speicherzelle 11, um die Anzahl der
verlangten DIMensionen und den für ein neu aufgebautes Feld nötigen
Speicherbedarf zu berechnen.

### 64map (—)
Input Buffer Pointer/Number of Subscripts

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
---
id: 000b-count
type: entity
title: Input buffer pointer/# subscrpt
aliases:
- Input buffer pointer/# subscrpt
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/000b-count.md
  sha256: 13f6285f6718661ed0c7fe223d391fa39d6c4b481b5334abf5ad5bf073bab9c6
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-000b-count
---

# Input buffer pointer/# subscrpt



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

## References
- Source: [[src-000b-count]]

---
title: Wr shift word/Rd input char
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
  address: $00BD
  symbol: ROPRTY
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: RS-232 trns parity buffer
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: ''
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Hier wird von den RS-232-Routinen ein
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: RS-232 Out Parity / Cassette Temp
  - name: Memory Map
    author: Jim Butterfield
    description: Wr shift word/Rd input char
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This location is used by the RS-232 routines as an output parity
      work
  - name: Reference
    author: Joe Forster / STA
    description: Parity during RS232 output. Byte buffer during datasette input/output
  - name: 64'er Magazin
    author: 64'er
    description: Die RS232-Routinen benutzen diese Speicherzellen als Zwischenspeicher
      für ein
  - name: 64map
    author: —
    description: RS232 Output Parity/Tape Byte to be Input or Output
---

# ROPRTY — Wr shift word/Rd input char ($00BD)

## Panoramica
Il registro o area di memoria ROPRTY è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00BD` (`189` decimale)
- **Range**: `$00BD`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
RS-232 trns parity buffer

### Original Source Comments (Microsoft/Commodore)


### Commodore-64-intern-Buch (Commodore)
Hier wird von den RS-232-Routinen ein
Prüfbyte abgelegt (Parity-Prüfung).

### C64 Programmer's Reference Guide (Commodore)
RS-232 Out Parity / Cassette Temp

### Memory Map (Jim Butterfield)
Wr shift word/Rd input char

### Mapping the Commodore 64 (Sheldon Leemon)
This location is used by the RS-232 routines as an output parity work
byte, and by the tape as temporary storage for the current character
being read or sent.

### Reference (Joe Forster / STA)
Parity during RS232 output. Byte buffer during datasette input/output

### 64'er Magazin (64'er)
Die RS232-Routinen benutzen diese Speicherzellen als Zwischenspeicher für ein
Prüf-Byte (Parity-Prüfung) bei der Ausgabe. Die Parity-Prüfung habe ich kurz im
Texteinschub Nr. 18 erklärt.

Auch die Kassetten-Routinen bedienen sich dieser Speicherzelle. Sie verwenden
sie als Zwischenspeicher für das gerade gesendete oder empfangene Zeichen.

### 64map (—)
RS232 Output Parity/Tape Byte to be Input or Output

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
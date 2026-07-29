---
title: Tape buffer pointer
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
  address: $00A6
  symbol: BUFPT
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Cassette buffer pointer
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Dieses Register wird als Zähler
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Pointer: Tape I/O Buffer'
  - name: Memory Map
    author: Jim Butterfield
    description: Tape buffer pointer
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This location is used to count the number of bytes that have been
      read
  - name: Reference
    author: Joe Forster / STA
    description: Offset of current byte in datasette buffer
  - name: 64'er Magazin
    author: 64'er
    description: Diese Speicherzelle wird als Zähler benutzt, welcher angibt, wieviele
      Bytes
  - name: 64map
    author: —
    description: 'Pointer: Tape I/O buffer'
---

# BUFPT — Tape buffer pointer ($00A6)

## Panoramica
Il registro o area di memoria BUFPT è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00A6` (`166` decimale)
- **Range**: `$00A6`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Cassette buffer pointer

### Commodore-64-intern-Buch (Commodore)
Dieses Register wird als Zähler
benutzt, welcher angibt, wie viele
Bytes aus dem Bandpuffer gelesen
oder in den Bandpuffer geschrieben
worden sind.

### C64 Programmer's Reference Guide (Commodore)
Pointer: Tape I/O Buffer

### Memory Map (Jim Butterfield)
Tape buffer pointer

### Mapping the Commodore 64 (Sheldon Leemon)
This location is used to count the number of bytes that have been read
in or written to the tape buffer.  Since on a tape write, no data is
sent until the 192 byte buffer is full, you can force output of the
buffer with the statement POKE 166,191.

### Reference (Joe Forster / STA)
Offset of current byte in datasette buffer

### 64'er Magazin (64'er)
Diese Speicherzelle wird als Zähler benutzt, welcher angibt, wieviele Bytes
gerade in den Kassetten-Puffer eingeschrieben oder aus ihm ausgelesen worden
sind. Der Kassetten-Puffer besteht aus den Speicherzellen 828 bis 1 019 und
kann somit 191 Byte aufnehmen, was zugleich die höchste Zahl ist, welche
sinnvollerweise in der Zelle 166 stehen kann.

Nähere Erklärungen und ein paar Experimente mit Zelle 166 finden Sie in dem
Texteinschub 17 »Experimente mit dem Kassetten-Puffer«.

Die meisten der nächsten 20 Speicherzellen werden bei Operationen mit der
RS232-Schnittstelle, die über den User-Port den Computer mit anderen Geräten
verbindet, eingesetzt. Da die Programmierung der RS232-Schnittstelle noch
andere Speicherzellen benötigt, die später an der Reihe sind, gehe ich auf die
RS232-Schnittstelle erst bei der Behandlung der Speicherzelle 659 bis 673 näher
ein.

### 64map (—)
Pointer: Tape I/O buffer

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
---
title: '# blocks remaining to Wr/Rd'
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
  address: $00BE
  symbol: FSBLK
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: 'Cassette: indicate which block we''re looking at (0 to exit)'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: In dieser Speicherzelle ist angegeben,
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Cassette Read / Write Block Count
  - name: Memory Map
    author: Jim Butterfield
    description: '# blocks remaining to Wr/Rd'
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: Used by the tape routines to count the number of copies of a data
  - name: Reference
    author: Joe Forster / STA
    description: Block counter during datasette input/output
  - name: 64'er Magazin
    author: 64'er
    description: Das Betriebssystem des Computers schreibt bei SAVE ein Programm zweimal
      auf das
  - name: 64map
    author: —
    description: Tape Input/Output Block count
---

# FSBLK — # blocks remaining to Wr/Rd ($00BE)

## Panoramica
Il registro o area di memoria FSBLK è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00BE` (`190` decimale)
- **Range**: `$00BE`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Cassette: indicate which block we're looking at (0 to exit)

### Commodore-64-intern-Buch (Commodore)
In dieser Speicherzelle ist angegeben,
wie viele Blockteile von Band gelesen
oder auf Band geschrieben werden
sollen.

### C64 Programmer's Reference Guide (Commodore)
Cassette Read / Write Block Count

### Memory Map (Jim Butterfield)
# blocks remaining to Wr/Rd

### Mapping the Commodore 64 (Sheldon Leemon)
Used by the tape routines to count the number of copies of a data
block remaining to be read or written.

### Reference (Joe Forster / STA)
Block counter during datasette input/output

### 64'er Magazin (64'er)
Das Betriebssystem des Computers schreibt bei SAVE ein Programm zweimal auf das
Band der Datasette. Beim LOAD-Befehl wird der erste Block in den
Arbeitsspeicher des Computers geladen; der zweite - identische - Block wird
dann mit dem ersten Block Byte für Byte verglichen, um Datenfehler auf dem
nicht immer ganz zuverlässigen Bandmaterial zu erkennen.

In derSpeicherzelle 190 wird dem Betriebssystem angezeigt, wie viele Blockteile
bei diesem Prozeß noch gelesen oder gespeichert werden müssen. Vom Basic-
Programm aus ist diese Speicherzelle nicht zugänglich.

### 64map (—)
Tape Input/Output Block count

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
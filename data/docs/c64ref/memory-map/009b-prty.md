---
title: Tape character parity
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
  address: $009B
  symbol: PRTY
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: 'Cassette: holds current calculated parity bit'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Über diese Speicherzelle findet eine
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Tape Character Parity
  - name: Memory Map
    author: Jim Butterfield
    description: Tape character parity
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This location is used to help detect when bits of information have
  - name: Reference
    author: Joe Forster / STA
    description: Unknown. (Parity bit during datasette input/output.)
  - name: 64'er Magazin
    author: 64'er
    description: Die Commodore-Datasette ist deswegen so zuverlässig, weil sie mehrere
      Methoden
  - name: 64map
    author: —
    description: Parity of Byte Output to Tape
---

# PRTY — Tape character parity ($009B)

## Panoramica
Il registro o area di memoria PRTY è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$009B` (`155` decimale)
- **Range**: `$009B`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Cassette: holds current calculated parity bit

### Commodore-64-intern-Buch (Commodore)
Über diese Speicherzelle findet eine
Parity-Prüfung (Quersummenbildung)
statt. Dies dient dazu, um Lese- und
Schreibfehler zu vermeiden.

### C64 Programmer's Reference Guide (Commodore)
Tape Character Parity

### Memory Map (Jim Butterfield)
Tape character parity

### Mapping the Commodore 64 (Sheldon Leemon)
This location is used to help detect when bits of information have
been lost during transmission of tape data.

### Reference (Joe Forster / STA)
Unknown. (Parity bit during datasette input/output.)

### 64'er Magazin (64'er)
Die Commodore-Datasette ist deswegen so zuverlässig, weil sie mehrere Methoden
zur Fehlererkennung beziehungsweise Korrektur von Lese- und Schreibfehlern verwendet.

Eine der Methoden ist die sogenannte Parity-Prüfung. Sie ist nichts anderes als
eine Quersummenbildung der einzelnen Stellen jedes Bytes, deren Resultat überprüft wird.

Die Speicherzelle 155 wird bei dieser Parity-Prüfung eingesetzt.

### 64map (—)
Parity of Byte Output to Tape

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
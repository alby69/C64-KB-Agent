---
title: Kernel setup pointer
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
  - memory_map.txt
  - c64_programmer's_reference_guide.txt
  - 64map.txt
  address: $00C3
  address_end: $00C4
  symbol: MEMUSS
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Cassette load temps (2 bytes)
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: ''
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Hier steht in LOU- und HIGH-Byte der
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Tape Load Temps
  - name: Memory Map
    author: Jim Butterfield
    description: Kernel setup pointer
  - name: Reference
    author: Joe Forster / STA
    description: Start address for a secondary address of 0 for LOAD and VERIFY from
      serial bu...
  - name: 64'er Magazin
    author: 64'er
    description: Bei jedem LOAD- und SAVE-Befehl für Kassetten wird der Vorspann (Tape
      Header),
  - name: 64map
    author: —
    description: 'Pointer: Type 3 Tape LOAD and general use'
---

# MEMUSS — Kernel setup pointer ($00C3)

## Panoramica
Il registro o area di memoria MEMUSS è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00C3` (`195` decimale)
- **Range**: `$00C3`-`$00C4`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Cassette load temps (2 bytes)

### Original Source Comments (Microsoft/Commodore)


### Commodore-64-intern-Buch (Commodore)
Hier steht in LOU- und HIGH-Byte der
Zeiger auf den Tape-Header im
Bandpuffer.

### C64 Programmer's Reference Guide (Commodore)
Tape Load Temps

### Memory Map (Jim Butterfield)
Kernel setup pointer

### Reference (Joe Forster / STA)
Start address for a secondary address of 0 for LOAD and VERIFY from serial bus or datasette. Pointer to ROM table of default vectors during initialization of I/O vectors

### 64'er Magazin (64'er)
Bei jedem LOAD- und SAVE-Befehl für Kassetten wird der Vorspann (Tape Header),
in dem Programmtyp, Anfangs- und Endadresse aufgezeichnet sind, im
Kassettenpuffer ab Adresse 828 gespeichert. Der eigentliche Teil des Programms
steht dann im Programmspeicher.

In den Speicherzellen 195 und 196 steht in der Low-/High-Byte-Darstellung diese
Adresse, ab der das Programm beginnt. Ich habe für alle diejenigen, die mit der
Datasette arbeiten, im Texteinschub Nr. 20 »Tape-Header« die Zusammenhänge mit
einem Beispiel dargestellt.

### 64map (—)
Pointer: Type 3 Tape LOAD and general use

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
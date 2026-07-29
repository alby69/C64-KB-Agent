---
title: 'Pntr : start of tape buffer'
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
  address: $00B2
  address_end: $00B3
  symbol: TAPE1
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: 'Address of tape buffer #1y'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Diese beiden Speicherzellen zeigen auf
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Pointer: Start of Tape Buffer'
  - name: Memory Map
    author: Jim Butterfield
    description: 'Pntr : start of tape buffer'
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: On power-on, this pointer is set to the address of the cassette buffer
  - name: Reference
    author: Joe Forster / STA
    description: 'Default: $033C, 828.'
  - name: 64'er Magazin
    author: 64'er
    description: Beim Einschalten des Computers werden diese Speicherzellen in Low-/High-Byte-
  - name: 64map
    author: —
    description: 'Pointer: Start Address of Tape Buffer ($033C)'
---

# TAPE1 — Pntr : start of tape buffer ($00B2)

## Panoramica
Il registro o area di memoria TAPE1 è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00B2` (`178` decimale)
- **Range**: `$00B2`-`$00B3`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Address of tape buffer #1y

### Commodore-64-intern-Buch (Commodore)
Diese beiden Speicherzellen zeigen auf
den Bandpuffer ($033C)

### C64 Programmer's Reference Guide (Commodore)
Pointer: Start of Tape Buffer

### Memory Map (Jim Butterfield)
Pntr : start of tape buffer

### Mapping the Commodore 64 (Sheldon Leemon)
On power-on, this pointer is set to the address of the cassette buffer
(828, $033C).  This pointer must contain an address greater than or
equal to 512 ($0200), or an ILLEGAL DEVICE NUMBER error will be sent
when tape I/O is tried.

### Reference (Joe Forster / STA)
Default: $033C, 828.

### 64'er Magazin (64'er)
Beim Einschalten des Computers werden diese Speicherzellen in Low-/High-Byte-
Darstellung auf die Anfangsadresse des Kassetten-Puffers gesetzt. Beim VC 20
und C 64 ist dies die Adresse 828 ($033C).

Durch Verbiegen dieses Zeigers kann der Kassettenpuffer auf beliebige Plätze
des Speichers, aber nicht unterhalb der Adresse 512 verschoben werden. Das kann
durchaus sinnvoll sein, um im Kassettenpuffer abgelegte Maschinenprogramme vor
Überschreiben durch Kassettenoperationen zu schützen.

### 64map (—)
Pointer: Start Address of Tape Buffer ($033C)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
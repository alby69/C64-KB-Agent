---
title: Wr lead length/Rd checksum/parity
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
  - 64'er_magazin.txt
  - mapping_the_commodore_64.txt
  - memory_map.txt
  - c64_programmer's_reference_guide.txt
  - 64map.txt
  address: $00AB
  symbol: RIPRTY
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: RS-232 rcvr parity storage
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: 'Cassette: short cnt; left over from debugging'
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: RS-232 Input Parity / Cassette Short Cnt
  - name: Memory Map
    author: Jim Butterfield
    description: Wr lead length/Rd checksum/parity
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This location is used to help detect if data was lost during RS-232
  - name: Reference
    author: Joe Forster / STA
    description: Parity during RS232 input. Computed block checksum during datasette
      input
  - name: 64'er Magazin
    author: 64'er
    description: Diese Speicherzelle wird vom Betriebssystem benutzt, um festzustellen,
      ob
  - name: 64map
    author: —
    description: RS232 Input parity/Tape temporary
---

# RIPRTY — Wr lead length/Rd checksum/parity ($00AB)

## Panoramica
Il registro o area di memoria RIPRTY è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00AB` (`171` decimale)
- **Range**: `$00AB`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
RS-232 rcvr parity storage

### Original Source Comments (Microsoft/Commodore)
Cassette: short cnt; left over from debugging

### C64 Programmer's Reference Guide (Commodore)
RS-232 Input Parity / Cassette Short Cnt

### Memory Map (Jim Butterfield)
Wr lead length/Rd checksum/parity

### Mapping the Commodore 64 (Sheldon Leemon)
This location is used to help detect if data was lost during RS-232
transmission, or if a tape leader is completed.

### Reference (Joe Forster / STA)
Parity during RS232 input. Computed block checksum during datasette input

### 64'er Magazin (64'er)
Diese Speicherzelle wird vom Betriebssystem benutzt, um festzustellen, ob
während einer RS232-Datenübertragung Bits verloren gingen. Da derartige
Prüfungen mit Parity-Bits (Quersummenprüfung) des öfteren erwähnt werden, gebe
ich eine kurze Beschreibung des Prüfprinzips im Texteinschub 18
»Fehlererkennung mit Parity-Bits«.

Zusätzlich wird in 171 die Länge des Band-Vorspanns bei seiner Erzeugung
gezählt.

### 64map (—)
RS232 Input parity/Tape temporary

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
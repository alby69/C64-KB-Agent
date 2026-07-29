---
title: CIA 1 Timer A control log
source_url: https://github.com/mist64/c64ref/blob/main/src/c64mem/reference.txt
category: reference
topics:
- memory-map
- zero-page
- rom-layout
difficulty: intermediate
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
  address: $02A2
  symbol: CASTON
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: TOD sense during cassettes
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Bei Bandroutinen wird hier das
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: TOD Sense During Cassette I/O
  - name: Memory Map
    author: Jim Butterfield
    description: CIA 1 Timer A control log
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: 'Indicator of CIA #1 Control Register B Activity During Cassette
      I/O'
  - name: Reference
    author: Joe Forster / STA
    description: 'Temporary area for saving original value of CIA#1 timer #1 control
      register, ...'
  - name: 64'er Magazin
    author: 64'er
    description: Mit CIA werden die beiden »Complex Interface Adapter« des C 64 bezeichnet.
      Das
  - name: 64map
    author: —
    description: TOD sense during Tape I/O
---

# CASTON — CIA 1 Timer A control log ($02A2)

## Panoramica
Il registro o area di memoria CASTON è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$02A2` (`674` decimale)
- **Range**: `$02A2`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
TOD sense during cassettes

### Commodore-64-intern-Buch (Commodore)
Bei Bandroutinen wird hier das
HIGH-Byte von Timer A zwischengespeichert.

### C64 Programmer's Reference Guide (Commodore)
TOD Sense During Cassette I/O

### Memory Map (Jim Butterfield)
CIA 1 Timer A control log

### Mapping the Commodore 64 (Sheldon Leemon)
Indicator of CIA #1 Control Register B Activity During Cassette I/O

### Reference (Joe Forster / STA)
Temporary area for saving original value of CIA#1 timer #1 control register, at memory address $DC0E, during datasette input/output

### 64'er Magazin (64'er)
Mit CIA werden die beiden »Complex Interface Adapter« des C 64 bezeichnet. Das
sind integrierte Schaltkreise, die Ein- und Ausgabeoperationen steuern. Jeder
der beiden CIAs hat mehrere Register. Das Steuerregister A (Adresse 56334
beziehungsweise $DC0E) beeinflußt die Zählregister des CIA, die ihrerseits die
Ein- und Ausgabe von Daten auf beziehungsweise von Kassetten steuern. Das
Betriebssystem speichert zu diesem Zweck geeignete Bitmuster in der
Speicherzelle 674 ab, die von da in das Steuerregister transferiert werden.

### 64map (—)
TOD sense during Tape I/O

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
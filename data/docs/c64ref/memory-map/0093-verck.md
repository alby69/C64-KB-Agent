---
title: Load = 0, Verify = l
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
  address: $0093
  symbol: VERCK
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: 'Cassette: verify or load flag (Z - loading)'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Dieses Flag dient dem Betriebssystem
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Flag: 0 = Load, 1 = Verify'
  - name: Memory Map
    author: Jim Butterfield
    description: Load = 0, Verify = l
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: The same Kernal routine can perform either a LOAD or VERIFY, depending
  - name: Reference
    author: Joe Forster / STA
    description: 'Values:'
  - name: 64'er Magazin
    author: 64'er
    description: Diese Flagge dient dem Betriebssystem, um zu unterscheiden, ob eine
      LOAD-
  - name: 64map
    author: —
    description: 'Flag: 0 = Load, 1 = Verify'
---

# VERCK — Load = 0, Verify = l ($0093)

## Panoramica
Il registro o area di memoria VERCK è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0093` (`147` decimale)
- **Range**: `$0093`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Cassette: verify or load flag (Z - loading)

### Commodore-64-intern-Buch (Commodore)
Dieses Flag dient dem Betriebssystem
dazu, um zu unterscheiden, ob eine
LOAD oder eine VERIFY Operation
erfolgt.

### C64 Programmer's Reference Guide (Commodore)
Flag: 0 = Load, 1 = Verify

### Memory Map (Jim Butterfield)
Load = 0, Verify = l

### Mapping the Commodore 64 (Sheldon Leemon)
The same Kernal routine can perform either a LOAD or VERIFY, depending
on the value stored in the Accumulator (.A) on entry to the routine.
This location is used to determine which operation to perform.

### Reference (Joe Forster / STA)
Values:

* $00: LOAD.
* $01-$FF: VERIFY.

### 64'er Magazin (64'er)
Diese Flagge dient dem Betriebssystem, um zu unterscheiden, ob eine LOAD-
Operation nur LOADen oder aber VERIFYen soll.

Sie ist identisch mit der Flagge des Basic-Übersetzers in Speicherzelle 10.
Genauere Hinweise bitte ich der Beschreibung von Zelle 10 zu entnehmen.

### 64map (—)
Flag: 0 = Load, 1 = Verify

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
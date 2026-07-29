---
title: Last shift pattern
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
  address: $028E
  symbol: LSTSHF
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Last SHIFT pattern
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Hier steht die zuletzt gedrückte
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Last Keyboard Shift Pattern
  - name: Memory Map
    author: Jim Butterfield
    description: Last shift pattern
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This location is used in combination with the one above to debounce
  - name: Reference
    author: Joe Forster / STA
    description: 'Bits:'
  - name: 64'er Magazin
    author: 64'er
    description: Diese Speicherzelle wird zusammen mit der Zelle 653 verwendet, um
      zu
  - name: 64map
    author: —
    description: Last Shift Key used for debouncing
---

# LSTSHF — Last shift pattern ($028E)

## Panoramica
Il registro o area di memoria LSTSHF è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$028E` (`654` decimale)
- **Range**: `$028E`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Last SHIFT pattern

### Commodore-64-intern-Buch (Commodore)
Hier steht die zuletzt gedrückte
Steuertaste.

### C64 Programmer's Reference Guide (Commodore)
Last Keyboard Shift Pattern

### Memory Map (Jim Butterfield)
Last shift pattern

### Mapping the Commodore 64 (Sheldon Leemon)
This location is used in combination with the one above to debounce
the special SHIFT keys.  This will keep the SHIFT/logo combination
from changing character sets back and forth during a single pressing
of both keys.

### Reference (Joe Forster / STA)
Bits:

* Bit #0: 1 = One or more of left Shift, right Shift or Shift Lock was pressed or locked at the time of previous check.
* Bit #1: 1 = Commodore was pressed at the time of previous check.
* Bit #2: 1 = Control was pressed at the time of previous check.

### 64'er Magazin (64'er)
Diese Speicherzelle wird zusammen mit der Zelle 653 verwendet, um zu
verhindern, daß ein schlechter Tastendruck als mehrfaches Drücken derselben
Taste gedeutet wird. Im Fachdeutsch nennt man das »Entprellen« einer Taste oder
eines Kontaktes. Die Funktion ist vergleichbar mit der der Zelle 197 gegenüber
der Zelle 203 für alle anderen Tasten.

### 64map (—)
Last Shift Key used for debouncing

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
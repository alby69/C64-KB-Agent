---
id: 028e-lstshf
type: entity
title: Last shift pattern
aliases:
- Last shift pattern
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/028e-lstshf.md
  sha256: 01433191455d1f6ddcd20b926bd0e195b9bc1cfad47bdaff6753304409831068
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-028e-lstshf
---

# Last shift pattern



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

## References
- Source: [[src-028e-lstshf]]

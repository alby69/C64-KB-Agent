---
id: 00d5-lnmx
type: entity
title: Current screen line length
aliases:
- Current screen line length
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/00d5-lnmx.md
  sha256: 61691a9247d3e7d8d1812e238035500437a7a694b5fab496bc9cfec3e6c257ac
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-00d5-lnmx
---

# Current screen line length



# LNMX — Current screen line length ($00D5)

## Panoramica
Il registro o area di memoria LNMX è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00D5` (`213` decimale)
- **Range**: `$00D5`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
40/80 max position

### Commodore-64-intern-Buch (Commodore)
Der Inhalt dieser Speicherzelle
entscheidet, ob eine neue Zeile
angefangen werden muß oder nicht.

### C64 Programmer's Reference Guide (Commodore)
Physical Screen Line Length

### Memory Map (Jim Butterfield)
Current screen line length

### Mapping the Commodore 64 (Sheldon Leemon)
The line editor uses this location when the end of a line has been
reached to determine whether another physical line can be added to the
current logical line, or if a new logical line must be started.

### Reference (Joe Forster / STA)
Length of current screen line minus 1. Values: $27, 39; $4F, 79

### 64'er Magazin (64'er)
Im Texteinschub 23 »Logische und echte Zeilen« ist der Unterschied zwischen den
beiden Zeilentypen beschrieben.

Der Inhalt dieser Speicherzelle entscheidet, wann eine neue logische Zeile
begonnen werden muß oder ob die laufende logische Zeile um eine weitere echte
Zeile erweitert werden kann. Der Bildschirm-Editor verwendet diese
Speicherzelle, um komplette logische Zeilen nach oben zu verschieben. Einige
andere Routinen benutzen den Wert der Zelle bei der Rückwärtsüberprüfung einer
Zeile, bei der die Endposition der Zeile bekannt sein muß. Schließlich bezieht
noch die bereits behandelte Speicherzelle 200 Ihren Wert von der Zelle 213.

### 64map (—)
Current logical Line length: 39 or 79

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-00d5-lnmx]]

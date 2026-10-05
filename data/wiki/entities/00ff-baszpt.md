---
id: 00ff-baszpt
type: entity
title: Floating to ASCII work area
aliases:
- Floating to ASCII work area
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/00ff-baszpt.md
  sha256: 78b77208547d7389411856c800d48c03c1dd53cb595a4d2b9fec571f4168ed73
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-00ff-baszpt
---

# Floating to ASCII work area



# BASZPT — Floating to ASCII work area ($00FF)

## Panoramica
Il registro o area di memoria BASZPT è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00FF` (`255` decimale)
- **Range**: `$00FF`-`$010A`
- **Dimensione**: `12 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Location ($00FF) used by BASIC

### Commodore-64-intern-Buch (Commodore)
Diese Register werden für die
Zwischenspeicherung von Fließkommazahlen
benutzt.

### C64 Programmer's Reference Guide (Commodore)
Floating to String Work Area

### Memory Map (Jim Butterfield)
Floating to ASCII work area

### Mapping the Commodore 64 (Sheldon Leemon)
This location is used for temporary storage in the process of
converting floating point numbers to ASCII characters.

### Reference (Joe Forster / STA)
Buffer for conversion from floating point to string (12 bytes.)

### 64'er Magazin (64'er)
Diese 12 Byte werden von einer Routine des Betriebssystems verwendet, um Werte
zwischenzuspeichern, die bei der Umwandlung von Gleitkomma-Zahlen in ASCII-
Werte oder in Werte der Funktion TI$ anfallen. Eine andere Routine verwendet
den Bereich, um Zeichenketten (Strings) zu untersuchen.

### 64map (—)
Assembly Area for Floating point to ASCII conversion

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-00ff-baszpt]]

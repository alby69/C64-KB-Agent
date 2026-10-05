---
id: 000d-valtyp
type: entity
title: 'Type : FF = string, 00 = numeric'
aliases:
- 'Type : FF = string, 00 = numeric'
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/000d-valtyp.md
  sha256: c7b8d96df35cf3d97186ec20102ad67c31d951e2821d52b0cdf07923923a9c2a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-000d-valtyp
---

# Type : FF = string, 00 = numeric



# VALTYP — Type : FF = string, 00 = numeric ($000D)

## Panoramica
Il registro o area di memoria VALTYP è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$000D` (`13` decimale)
- **Range**: `$000D`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
0=numeric 1=string.

### Commodore-64-intern-Buch (Commodore)
Das Flag zeigt dem BASIC-Interpreter
an, ob es sich um Zahlenwerte oder um
einen String handelt.

### C64 Programmer's Reference Guide (Commodore)
Data Type: $FF = String, $00 = Numeric

### Memory Map (Jim Butterfield)
Type : FF = string, 00 = numeric

### Mapping the Commodore 64 (Sheldon Leemon)
This flag is used internally to indicate whether data being operated
upon is string or numeric.  A value of 255 ($FF) in this location
indicates string data, while a 0 indicates numeric data.  This
determination is made every time a variable is located or created.

### Reference (Joe Forster / STA)
Values:

* $00: Numerical.
* $FF: String.

### 64'er Magazin (64'er)
Diese Flagge zeigt den Routinen des Basic-Übersetzers an, ob es sich bei den
zur Verarbeitung anstehenden Daten um einen String oder um Zahlenwerte handelt.
Zeigt die Flagge 255 ($FF), ist es ein String. Bei 0 handelt es sich um Zahlen.
Diese Bestimmung erfolgt jedesmal, wenn eine Variable definiert oder gesucht
wird. Diese Flagge kann leider nicht durch ein Basic-Programm abgefragt werden.

### 64map (—)
Data type Flag: $00 = Numeric, $FF = String

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-000d-valtyp]]

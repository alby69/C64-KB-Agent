---
id: 00f9-robuf
type: entity
title: RS-232 Tx pntr
aliases:
- RS-232 Tx pntr
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/00f9-robuf.md
  sha256: 24805292579b2810003f8c20395b0bd2e9499fc2f516ded3d1591afe0a5b28d4
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-00f9-robuf
---

# RS-232 Tx pntr



# ROBUF — RS-232 Tx pntr ($00F9)

## Panoramica
Il registro o area di memoria ROBUF è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00F9` (`249` decimale)
- **Range**: `$00F9`-`$00FA`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
RS-232 output buffer pointer

### Commodore-64-intern-Buch (Commodore)
Diese Register zeigen auf die
Anfangsadresse des Ausgabepuffers.

### C64 Programmer's Reference Guide (Commodore)
RS-232 Output Buffer  Pointer

### Memory Map (Jim Butterfield)
RS-232 Tx pntr

### Mapping the Commodore 64 (Sheldon Leemon)
This location points to the address of the 256-byte output buffer
which is used for transmitting data to RS-232 devices (device number
2)l

### Reference (Joe Forster / STA)
Values:

* $0000-$00FF: No buffer defined, a new buffer must be allocated upon RS232 output.
* $0100-$FFFF: Buffer pointer.

### 64'er Magazin (64'er)
Dieser Zeiger ist der Zwilling zu dem in den Zellen 247/248 stehenden Zeiger,
diesmal aber für den Ausgabe-Puffer.

### 64map (—)
RS232 Output Buffer Pointer

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-00f9-robuf]]

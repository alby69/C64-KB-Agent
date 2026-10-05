---
id: 029d-rodbs
type: entity
title: RS232 transmit pointer
aliases:
- RS232 transmit pointer
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/029d-rodbs.md
  sha256: 44880ba5ed73a96375ac028379aabea28c38a79d0207b8ceff127a1a6f639da0
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-029d-rodbs
---

# RS232 transmit pointer



# RODBS — RS232 transmit pointer ($029D)

## Panoramica
Il registro o area di memoria RODBS è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$029D` (`669` decimale)
- **Range**: `$029D`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Output buffer index to start

### Commodore-64-intern-Buch (Commodore)
Wenn man den Inhalt der Speicherzelle
mit dem Wert in $00F9-$00FA addiert,
erhält man die Adresse des ersten im
Ausgabepuffer eingegebenen Bytes.

### C64 Programmer's Reference Guide (Commodore)
RS-232 Start of Output Buffer (Page)

### Memory Map (Jim Butterfield)
RS232 transmit pointer

### Mapping the Commodore 64 (Sheldon Leemon)
This index points to the starting byte within the 256-byte RS-232
transmit buffer, and is used to remove data from that buffer.

### Reference (Joe Forster / STA)
Offset of byte to send in RS232 output buffer

### 64'er Magazin (64'er)
Dieser Index wird verwendet, um Daten aus dem Ausgabepufferspeicher auszulesen.
Wenn man ihn nämlich zum Inhalt der Speicherzelle 249 und 250 addiert, erhält
man die Adresse des ersten in den Ausgabepufferspeicher eingegebenen Bytes.

### 64map (—)
RS232 Pointer: High Byte of Address of Output Buffer

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-029d-rodbs]]

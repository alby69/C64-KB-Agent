---
id: 029c-ridbs
type: entity
title: RS232 input pointer
aliases:
- RS232 input pointer
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/029c-ridbs.md
  sha256: 13a7f33fd5c3c77ef3ecc2ec364801b43fcfd5fa163f2f2acc654077e24fdb17
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-029c-ridbs
---

# RS232 input pointer



# RIDBS — RS232 input pointer ($029C)

## Panoramica
Il registro o area di memoria RIDBS è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$029C` (`668` decimale)
- **Range**: `$029C`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Input buffer pointer to start

### Commodore-64-intern-Buch (Commodore)
Wenn man den Inhalt der Speicherzelle
mit dem Wert in $00F7-$00F8 addiert,
erhält man die Adresse des ersten im
Eingabepuffer eingegebenen Bytes.

### C64 Programmer's Reference Guide (Commodore)
RS-232 Start of Input Buffer (Page)

### Memory Map (Jim Butterfield)
RS232 input pointer

### Mapping the Commodore 64 (Sheldon Leemon)
This index points to the starting byte within the 256-byte RS-232
receive buffer, and is used to remove data from that buffer.

### Reference (Joe Forster / STA)
Offset of current byte in RS232 input buffer

### 64'er Magazin (64'er)
Dieser Index wird verwendet, um Daten aus dem Eingabepufferspeicher auszulesen.
Wenn man ihn nämlich zum Inhalt der Speicherzelle 247 und 248 addiert, erhält
man die Adresse des ersten in den Eingabepufferspeicher eingegebenen Bytes.

### 64map (—)
RS232 Pointer: High Byte of Address of Input Buffer

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-029c-ridbs]]

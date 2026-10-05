---
id: 029e-rodbe
type: entity
title: RS232 output pointer
aliases:
- RS232 output pointer
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/029e-rodbe.md
  sha256: 5cdaae795dc1f7d6a0e11f460b721e88874fbcc7da7ee0f4e3c6b472c14e58b0
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-029e-rodbe
---

# RS232 output pointer



# RODBE — RS232 output pointer ($029E)

## Panoramica
Il registro o area di memoria RODBE è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$029E` (`670` decimale)
- **Range**: `$029E`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Output buffer index to end

### Commodore-64-intern-Buch (Commodore)
Wenn man den Inhalt der Speicherzelle
mit dem Wert in $00F9-$00FA addiert,
erhält man die Adresse des zuletzt im
Ausgabepuffer eingegebenen Bytes.

### C64 Programmer's Reference Guide (Commodore)
RS-232 Index to End of Output Buffer

### Memory Map (Jim Butterfield)
RS232 output pointer

### Mapping the Commodore 64 (Sheldon Leemon)
This index points to the ending byte within the 256-byte RS-232
transmit buffer, and is used to add data to that buffer.

### Reference (Joe Forster / STA)
Offset of current byte in RS232 output buffer

### 64'er Magazin (64'er)
Dieser Index wird verwendet, um Daten in den Ausgabepufferspeicher zu
schreiben. Wenn man ihn nämlich zum Inhalt der Speicherzelle 249 und 250
addiert, erhält man die Adresse des zuletzt in den Ausgabepufferspeicher
eingegebenen Bytes.

### 64map (—)
RS232 Index to End of Output Buffer

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-029e-rodbe]]

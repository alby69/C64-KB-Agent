---
id: 029b-ridbe
type: entity
title: RS232 receive pointer
aliases:
- RS232 receive pointer
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/029b-ridbe.md
  sha256: ebdbcb72518c02eccd04d0e182ff89c0d66ba28a5813360f50937e803da1b375
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-029b-ridbe
---

# RS232 receive pointer



# RIDBE — RS232 receive pointer ($029B)

## Panoramica
Il registro o area di memoria RIDBE è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$029B` (`667` decimale)
- **Range**: `$029B`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Input buffer index to end

### Commodore-64-intern-Buch (Commodore)
Wenn man den Inhalt der Speicherzelle
mit dem Wert in $00F7-$00F8 addiert,
erhält man die Adresse des zuletzt im
Eingabepuffer eingegebenen Bytes.

### C64 Programmer's Reference Guide (Commodore)
RS-232 Index to End of Input Buffer

### Memory Map (Jim Butterfield)
RS232 receive pointer

### Mapping the Commodore 64 (Sheldon Leemon)
The two 256-byte First In, First Out (FIFO) buffers for RS-232 data
reception and transmission are dynamic wraparound buffers.  This means
that the starting point and the ending point of the buffer can change
over time, and either point can be anywhere withing the buffer.  If,
for example, the starting point is at byte 100, the buffer will fill
towards byte 255, at which point it will wrap around to byte 0 again.
To maintain this system, the following four locations are used as
indices to the starting and the ending point of each buffer.

### Mapping the Commodore 64 (Sheldon Leemon)
This index points to the ending byte within the 256-byte RS-232
receive buffer, and is used to add data to that buffer.

### Reference (Joe Forster / STA)
Offset of byte received in RS232 input buffer

### 64'er Magazin (64'er)
Dieser Index wird verwendet, um Daten in den Eingabepufferspeicher zu
schreiben. Wenn man ihn nämlich zum Inhalt der Speicherzelle 247/248 addiert,
erhält man die Adresse des zuletzt in den Eingabepufferspeicher eingegebenen
Bytes.

### 64map (—)
RS232 Index to End of Input Buffer

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-029b-ridbe]]

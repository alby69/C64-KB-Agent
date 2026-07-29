---
title: RS232 receive pointer
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
  address: $029B
  symbol: RIDBE
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Input buffer index to end
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Wenn man den Inhalt der Speicherzelle
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: RS-232 Index to End of Input Buffer
  - name: Memory Map
    author: Jim Butterfield
    description: RS232 receive pointer
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: The two 256-byte First In, First Out (FIFO) buffers for RS-232 data
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This index points to the ending byte within the 256-byte RS-232
  - name: Reference
    author: Joe Forster / STA
    description: Offset of byte received in RS232 input buffer
  - name: 64'er Magazin
    author: 64'er
    description: Dieser Index wird verwendet, um Daten in den Eingabepufferspeicher
      zu
  - name: 64map
    author: —
    description: RS232 Index to End of Input Buffer
---

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
---
title: RS232 output pointer
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
  address: $029E
  symbol: RODBE
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Output buffer index to end
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Wenn man den Inhalt der Speicherzelle
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: RS-232 Index to End of Output Buffer
  - name: Memory Map
    author: Jim Butterfield
    description: RS232 output pointer
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This index points to the ending byte within the 256-byte RS-232
  - name: Reference
    author: Joe Forster / STA
    description: Offset of current byte in RS232 output buffer
  - name: 64'er Magazin
    author: 64'er
    description: Dieser Index wird verwendet, um Daten in den Ausgabepufferspeicher
      zu
  - name: 64map
    author: —
    description: RS232 Index to End of Output Buffer
---

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
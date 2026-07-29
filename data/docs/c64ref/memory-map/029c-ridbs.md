---
title: RS232 input pointer
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
  address: $029C
  symbol: RIDBS
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Input buffer pointer to start
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Wenn man den Inhalt der Speicherzelle
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: RS-232 Start of Input Buffer (Page)
  - name: Memory Map
    author: Jim Butterfield
    description: RS232 input pointer
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This index points to the starting byte within the 256-byte RS-232
  - name: Reference
    author: Joe Forster / STA
    description: Offset of current byte in RS232 input buffer
  - name: 64'er Magazin
    author: 64'er
    description: Dieser Index wird verwendet, um Daten aus dem Eingabepufferspeicher
      auszulesen.
  - name: 64map
    author: —
    description: 'RS232 Pointer: High Byte of Address of Input Buffer'
---

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
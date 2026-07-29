---
title: RS232 transmit pointer
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
  address: $029D
  symbol: RODBS
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Output buffer index to start
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Wenn man den Inhalt der Speicherzelle
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: RS-232 Start of Output Buffer (Page)
  - name: Memory Map
    author: Jim Butterfield
    description: RS232 transmit pointer
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This index points to the starting byte within the 256-byte RS-232
  - name: Reference
    author: Joe Forster / STA
    description: Offset of byte to send in RS232 output buffer
  - name: 64'er Magazin
    author: 64'er
    description: Dieser Index wird verwendet, um Daten aus dem Ausgabepufferspeicher
      auszulesen.
  - name: 64map
    author: —
    description: 'RS232 Pointer: High Byte of Address of Output Buffer'
---

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
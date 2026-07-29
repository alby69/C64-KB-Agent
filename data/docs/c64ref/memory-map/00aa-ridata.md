---
title: Tp Scan; Cnt; Ld; End/byte assy
source_url: https://github.com/mist64/c64ref/blob/main/src/c64mem/reference.txt
category: reference
topics:
- memory-map
- zero-page
- rom-layout
- zero-page
difficulty: beginner
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
  - 64'er_magazin.txt
  - mapping_the_commodore_64.txt
  - memory_map.txt
  - c64_programmer's_reference_guide.txt
  - 64map.txt
  address: $00AA
  symbol: RIDATA
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: RS-232 rcvr byte buffer
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: MI - waiting for block SYNC
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: RS-232 Input Byte Buffer/Cassette Temp
  - name: Memory Map
    author: Jim Butterfield
    description: Tp Scan; Cnt; Ld; End/byte assy
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: Serial routines use this area to reassemble the bits received into
      a
  - name: Reference
    author: Joe Forster / STA
    description: Byte buffer during RS232 input
  - name: 64'er Magazin
    author: 64'er
    description: Bei der Speicherzelle 165 haben wir gesehen, daß ein Band Synchronisationsbits
  - name: 64map
    author: —
    description: RS232 Input Byte Buffer/Tape temporary
---

# RIDATA — Tp Scan; Cnt; Ld; End/byte assy ($00AA)

## Panoramica
Il registro o area di memoria RIDATA è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00AA` (`170` decimale)
- **Range**: `$00AA`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
RS-232 rcvr byte buffer

### Original Source Comments (Microsoft/Commodore)
MI - waiting for block SYNC
VS - in data block reading data
NE - waiting for byte SYNC

### C64 Programmer's Reference Guide (Commodore)
RS-232 Input Byte Buffer/Cassette Temp

### Memory Map (Jim Butterfield)
Tp Scan; Cnt; Ld; End/byte assy

### Mapping the Commodore 64 (Sheldon Leemon)
Serial routines use this area to reassemble the bits received into a
byte that will be stored in the receiving buffer pointed to by 247
($00F7).  Tape routines use this as a flag to help determine whether a
received character should be treated as data or as a synchronization
character.

### Reference (Joe Forster / STA)
Byte buffer during RS232 input

### 64'er Magazin (64'er)
Bei der Speicherzelle 165 haben wir gesehen, daß ein Band Synchronisationsbits
enthält. Die Speicherzelle 170 wird dabei als Flagge benutzt, die angibt, ob
ein gelesenes Zeichen Synchronisierungs-Bits oder ein Datenwort darstellt.

Die RS232-Routinen verwenden Zelle 17 0 dagegen als Speicher, in welchem die
eingelesenen Bits zu einem Byte zusammengefaßt werden, bevor sie im
Eingabepuffer am oberen Ende des Programmspeichers abgelegt werden (siehe auch
Speicherzellen 55/56).

### 64map (—)
RS232 Input Byte Buffer/Tape temporary

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
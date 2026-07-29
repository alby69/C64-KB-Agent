---
title: RS-232 Rev pntr
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
  - commodore-64-intern-buch.txt
  - 64'er_magazin.txt
  - mapping_the_commodore_64.txt
  - memory_map.txt
  - c64_programmer's_reference_guide.txt
  - 64map.txt
  address: $00F7
  address_end: $00F8
  symbol: RIBUF
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: RS-232 input buffer pointer
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Diese Register zeigen auf die
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: RS-232 Input Buffer Pointer
  - name: Memory Map
    author: Jim Butterfield
    description: RS-232 Rev pntr
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: When device number 2 (the RS-232 channel) is opened, two buffers
      of
  - name: Reference
    author: Joe Forster / STA
    description: 'Values:'
  - name: 64'er Magazin
    author: 64'er
    description: Immer wenn ein Kanal mit der Geräte-Nummer 2 (User-Port) eröffnet
      wird, werden
  - name: 64map
    author: —
    description: RS232 Input Buffer Pointer
---

# RIBUF — RS-232 Rev pntr ($00F7)

## Panoramica
Il registro o area di memoria RIBUF è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00F7` (`247` decimale)
- **Range**: `$00F7`-`$00F8`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
RS-232 input buffer pointer

### Commodore-64-intern-Buch (Commodore)
Diese Register zeigen auf die
Anfangsadresse des Eingabepuffers.

### C64 Programmer's Reference Guide (Commodore)
RS-232 Input Buffer Pointer

### Memory Map (Jim Butterfield)
RS-232 Rev pntr

### Mapping the Commodore 64 (Sheldon Leemon)
When device number 2 (the RS-232 channel) is opened, two buffers of
256 bytes each are created at the top of memory.  This location points
to the address of the one which is used to store characters as they
are received.  A BASIC program should always OPEN device 2 before
assigning any variables to avoid the consequences of overwriting
variables which were previously located at the top of memory, as BASIC
executes a CLR after opening this device.

### Reference (Joe Forster / STA)
Values:

* $0000-$00FF: No buffer defined, a new buffer must be allocated upon RS232 input.
* $0100-$FFFF: Buffer pointer.

### 64'er Magazin (64'er)
Immer wenn ein Kanal mit der Geräte-Nummer 2 (User-Port) eröffnet wird, werden
am oberen Ende des Arbeitsspeichers zwei Pufferspeicher mit je 256 Byte
reserviert (siehe auch die Beschreibung der Speicherzellen 55 bis 56).

Der Zeiger, der in Low-/High-Byte-Darstellung in 247 und 248 steht, zeigt auf
die Anfangsadresse desjenigen Pufferspeichers, der die ankommenden Zeichen
aufnimmt.

Ein Programm, das den User-Port benutzen will, sollte übrigens immer zuerst die
Gerätenummer 2 eröffnen, bevor irgendwelche Variable definiert werden. Dadurch
wird vermieden, daß die Puffer-Reservierung eventuelle Variablenwerte
überschreibt, die bereits in diesen 512 Byte angesiedelt worden sind.

### 64map (—)
RS232 Input Buffer Pointer

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
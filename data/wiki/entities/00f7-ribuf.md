---
id: 00f7-ribuf
type: entity
title: RS-232 Rev pntr
aliases:
- RS-232 Rev pntr
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/00f7-ribuf.md
  sha256: e6c2a5aaa3584416946239258f2e006256dfe8d9b405492e7f83fbea29e23e26
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-00f7-ribuf
---

# RS-232 Rev pntr



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

## References
- Source: [[src-00f7-ribuf]]

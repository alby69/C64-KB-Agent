---
id: 00d7-data
type: entity
title: Last inkey/checksum/buffer
aliases:
- Last inkey/checksum/buffer
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/00d7-data.md
  sha256: 0d4ce27e973bbee83d4870f983c12347d0b7162c208fa526e3b4b8960ad392ba
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-00d7-data
---

# Last inkey/checksum/buffer



# DATA — Last inkey/checksum/buffer ($00D7)

## Panoramica
Il registro o area di memoria DATA è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00D7` (`215` decimale)
- **Range**: `$00D7`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Cassette: holds most recent dipole bit value

### Commodore-64-intern-Buch (Commodore)
Bevor ein Zeichen in den
Tastaturpuffer gebracht wird, wird es
vorher hier zwischengespeichert.

### C64 Programmer's Reference Guide (Commodore)
Temp Data Area

### Memory Map (Jim Butterfield)
Last inkey/checksum/buffer

### Mapping the Commodore 64 (Sheldon Leemon)
The ASCII value of the last character printed to the screen is held
here temporarily.

### Reference (Joe Forster / STA)
PETSCII code of character during screen input/output. Bit buffer during datasette input. Block checksum during datasette output

### 64'er Magazin (64'er)
Bei der Tastaturabfrage werden die Tastencodes (siehe Speicherzelle 203) in
ASCII-Codewerte umgewandelt und in den Tastaturpuffer gebracht. Die
Speicherzelle 215 dient dabei als Zwischenspeicher. Kassettenoperationen
speichern hier auch Prüfsummen ab.

### 64map (—)
Screen value of current Input Character/Last Character Output

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-00d7-data]]

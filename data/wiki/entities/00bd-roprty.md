---
id: 00bd-roprty
type: entity
title: Wr shift word/Rd input char
aliases:
- Wr shift word/Rd input char
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/00bd-roprty.md
  sha256: 7620f0b957a6d8ce50d55734607f929ae508264c069a9dcfd06599c5c45447f4
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-00bd-roprty
---

# Wr shift word/Rd input char



# ROPRTY — Wr shift word/Rd input char ($00BD)

## Panoramica
Il registro o area di memoria ROPRTY è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00BD` (`189` decimale)
- **Range**: `$00BD`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
RS-232 trns parity buffer

### Original Source Comments (Microsoft/Commodore)


### Commodore-64-intern-Buch (Commodore)
Hier wird von den RS-232-Routinen ein
Prüfbyte abgelegt (Parity-Prüfung).

### C64 Programmer's Reference Guide (Commodore)
RS-232 Out Parity / Cassette Temp

### Memory Map (Jim Butterfield)
Wr shift word/Rd input char

### Mapping the Commodore 64 (Sheldon Leemon)
This location is used by the RS-232 routines as an output parity work
byte, and by the tape as temporary storage for the current character
being read or sent.

### Reference (Joe Forster / STA)
Parity during RS232 output. Byte buffer during datasette input/output

### 64'er Magazin (64'er)
Die RS232-Routinen benutzen diese Speicherzellen als Zwischenspeicher für ein
Prüf-Byte (Parity-Prüfung) bei der Ausgabe. Die Parity-Prüfung habe ich kurz im
Texteinschub Nr. 18 erklärt.

Auch die Kassetten-Routinen bedienen sich dieser Speicherzelle. Sie verwenden
sie als Zwischenspeicher für das gerade gesendete oder empfangene Zeichen.

### 64map (—)
RS232 Output Parity/Tape Byte to be Input or Output

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-00bd-roprty]]

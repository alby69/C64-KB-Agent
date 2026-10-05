---
id: 00a6-bufpt
type: entity
title: Tape buffer pointer
aliases:
- Tape buffer pointer
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/00a6-bufpt.md
  sha256: d68dbd2486f62d77f367bc7c0c9217d1956b617ab14399667adc60b4463ffc1a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-00a6-bufpt
---

# Tape buffer pointer



# BUFPT — Tape buffer pointer ($00A6)

## Panoramica
Il registro o area di memoria BUFPT è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00A6` (`166` decimale)
- **Range**: `$00A6`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Cassette buffer pointer

### Commodore-64-intern-Buch (Commodore)
Dieses Register wird als Zähler
benutzt, welcher angibt, wie viele
Bytes aus dem Bandpuffer gelesen
oder in den Bandpuffer geschrieben
worden sind.

### C64 Programmer's Reference Guide (Commodore)
Pointer: Tape I/O Buffer

### Memory Map (Jim Butterfield)
Tape buffer pointer

### Mapping the Commodore 64 (Sheldon Leemon)
This location is used to count the number of bytes that have been read
in or written to the tape buffer.  Since on a tape write, no data is
sent until the 192 byte buffer is full, you can force output of the
buffer with the statement POKE 166,191.

### Reference (Joe Forster / STA)
Offset of current byte in datasette buffer

### 64'er Magazin (64'er)
Diese Speicherzelle wird als Zähler benutzt, welcher angibt, wieviele Bytes
gerade in den Kassetten-Puffer eingeschrieben oder aus ihm ausgelesen worden
sind. Der Kassetten-Puffer besteht aus den Speicherzellen 828 bis 1 019 und
kann somit 191 Byte aufnehmen, was zugleich die höchste Zahl ist, welche
sinnvollerweise in der Zelle 166 stehen kann.

Nähere Erklärungen und ein paar Experimente mit Zelle 166 finden Sie in dem
Texteinschub 17 »Experimente mit dem Kassetten-Puffer«.

Die meisten der nächsten 20 Speicherzellen werden bei Operationen mit der
RS232-Schnittstelle, die über den User-Port den Computer mit anderen Geräten
verbindet, eingesetzt. Da die Programmierung der RS232-Schnittstelle noch
andere Speicherzellen benötigt, die später an der Reihe sind, gehe ich auf die
RS232-Schnittstelle erst bei der Behandlung der Speicherzelle 659 bis 673 näher
ein.

### 64map (—)
Pointer: Tape I/O buffer

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-00a6-bufpt]]

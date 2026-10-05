---
id: 00be-fsblk
type: entity
title: '# blocks remaining to Wr/Rd'
aliases:
- '# blocks remaining to Wr/Rd'
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/00be-fsblk.md
  sha256: ca04dc6fa17b4701128f40d05a78121a4b82e2aff519828305561243f8bbedd1
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-00be-fsblk
---

# # blocks remaining to Wr/Rd



# FSBLK — # blocks remaining to Wr/Rd ($00BE)

## Panoramica
Il registro o area di memoria FSBLK è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00BE` (`190` decimale)
- **Range**: `$00BE`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Cassette: indicate which block we're looking at (0 to exit)

### Commodore-64-intern-Buch (Commodore)
In dieser Speicherzelle ist angegeben,
wie viele Blockteile von Band gelesen
oder auf Band geschrieben werden
sollen.

### C64 Programmer's Reference Guide (Commodore)
Cassette Read / Write Block Count

### Memory Map (Jim Butterfield)
# blocks remaining to Wr/Rd

### Mapping the Commodore 64 (Sheldon Leemon)
Used by the tape routines to count the number of copies of a data
block remaining to be read or written.

### Reference (Joe Forster / STA)
Block counter during datasette input/output

### 64'er Magazin (64'er)
Das Betriebssystem des Computers schreibt bei SAVE ein Programm zweimal auf das
Band der Datasette. Beim LOAD-Befehl wird der erste Block in den
Arbeitsspeicher des Computers geladen; der zweite - identische - Block wird
dann mit dem ersten Block Byte für Byte verglichen, um Datenfehler auf dem
nicht immer ganz zuverlässigen Bandmaterial zu erkennen.

In derSpeicherzelle 190 wird dem Betriebssystem angezeigt, wie viele Blockteile
bei diesem Prozeß noch gelesen oder gespeichert werden müssen. Vom Basic-
Programm aus ist diese Speicherzelle nicht zugänglich.

### 64map (—)
Tape Input/Output Block count

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-00be-fsblk]]

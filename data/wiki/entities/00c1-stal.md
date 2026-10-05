---
id: 00c1-stal
type: entity
title: I/O start address
aliases:
- I/O start address
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/00c1-stal.md
  sha256: 223911b941494d88dee0258dad5aa88175797781fd3f2c18f73a2056b5916f1f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-00c1-stal
---

# I/O start address



# STAL — I/O start address ($00C1)

## Panoramica
Il registro o area di memoria STAL è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00C1` (`193` decimale)
- **Range**: `$00C1`-`$00C2`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)


### Original Source Comments (Microsoft/Commodore)


### Commodore-64-intern-Buch (Commodore)
In diesen Registern ist in LOW- und
HIGH-Byte-Darstellung angegeben, ab
welcher Adresse ein Programm geladen
oder gespeichert wird.

### C64 Programmer's Reference Guide (Commodore)
I/O Start Address

### Memory Map (Jim Butterfield)
I/O start address

### Mapping the Commodore 64 (Sheldon Leemon)
This location points to the beginning address of the area in RAM which
is currently being LOADed or SAVEd.  For tape I/O, it will point to
the cassette buffer, and the rest of the data is LOADed or SAVEd
directly to or from RAM.  This location points to the beginning
address of the area of RAM to be used for the blocks of data that come
after the initial header.

### Reference (Joe Forster / STA)
Start address during SAVE to serial bus, LOAD and VERIFY from datasette and SAVE to datasette. Pointer to current byte during memory test

### 64'er Magazin (64'er)
In diesen Speicherzellen steht in Low-/High-Byte-Darstellung die Adresse, ab
der ein Programm gerade geladen oder gespeichert wird. Diese Adresse wird
übrigens von hier auch in die Speicherzellen 172 und 173gebracht, die wir schon
früher besprochen haben.

Bei LOAD und SAVE auf Band steht hier die Anfangsadresse des Bandpuffers (828).
Im Bandpuffer steht allerdings nur der sogenannte Bandvorspann (auf englisch
»Tape Header«), während der Hauptteil des Programms im Programmspeicher ab
einer Adresse steht, auf die der Zeiger in den Speicherzellen 195 und 196
hinweist.

### 64map (—)
Start Address for LOAD and Cassette Write

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-00c1-stal]]

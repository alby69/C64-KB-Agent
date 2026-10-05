---
id: 009c-dpsw
type: entity
title: Byte-received flag
aliases:
- Byte-received flag
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/009c-dpsw.md
  sha256: 4548e9c1100bdb2b37b7a6b82797f92d3efb854f0d26f4849e64f4a4b8cfb94e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-009c-dpsw
---

# Byte-received flag



# DPSW — Byte-received flag ($009C)

## Panoramica
Il registro o area di memoria DPSW è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$009C` (`156` decimale)
- **Range**: `$009C`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Cassette: if NZ then expecting LL/L combination that ends a byte

### Commodore-64-intern-Buch (Commodore)
Hier wird festgelegt, ob das gelesene
Byte die Quersumme richtig gebildet
hat oder nicht.

### C64 Programmer's Reference Guide (Commodore)
Flag: Tape Byte-Received

### Memory Map (Jim Butterfield)
Byte-received flag

### Mapping the Commodore 64 (Sheldon Leemon)
This location is used as a flag to indicate whether a complete byte of
tape data has been received, or whether it has only been partially
received.

### Reference (Joe Forster / STA)
Unknown. (Byte ready indicator during datasette input/output.)

### 64'er Magazin (64'er)
In dieser Speicherzelle wird zwischengespeichert, ob das vom Band gelesene Byte
die Prüfungen bestanden hat, also richtig ist oder nicht.

### 64map (—)
Flag: Byte received from Tape

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-009c-dpsw]]

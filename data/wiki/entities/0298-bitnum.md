---
id: 0298-bitnum
type: entity
title: '# bits to send'
aliases:
- '# bits to send'
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0298-bitnum.md
  sha256: 2c6b5eed89eb67f0c49fa6acf5fb71913544d9691011efc0e27f6534491cb3da
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0298-bitnum
---

# # bits to send



# BITNUM — # bits to send ($0298)

## Panoramica
Il registro o area di memoria BITNUM è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0298` (`664` decimale)
- **Range**: `$0298`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Number of bits to send (fast response)

### Commodore-64-intern-Buch (Commodore)
Diese Speicherzelle wird verwendet,
um die Wortlänge festzustellen.

### C64 Programmer's Reference Guide (Commodore)
RS-232 Number of Bits Left to Send

### Memory Map (Jim Butterfield)
# bits to send

### Mapping the Commodore 64 (Sheldon Leemon)
This location is used to determine how many zero bits must be added to
the data character to pad its length out to the word length specified
in 659 ($0293).

### Reference (Joe Forster / STA)
RS232 byte size, number of data bits per data byte, default value for bit counters

### 64'er Magazin (64'er)
Diese Speicherzelle wird verwendet, um festzustellen, mit wievielen Nullen das
zu übertragende Zeichen aufgefüllt werden muß, um die in Speicherzelle 659 (Bit
5 und 6) ausgewählte Wortlänge herzustellen (s. Speicherzellen 168 und 180).

### 64map (—)
RS232 Number of Bits left to send

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-0298-bitnum]]

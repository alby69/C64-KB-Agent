---
id: 00b2-tape1
type: entity
title: 'Pntr : start of tape buffer'
aliases:
- 'Pntr : start of tape buffer'
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/00b2-tape1.md
  sha256: 2105ce9b2e1577d182baee8797b1b5998dfdb0d4085898b82721b016ce1b98ba
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-00b2-tape1
---

# Pntr : start of tape buffer



# TAPE1 — Pntr : start of tape buffer ($00B2)

## Panoramica
Il registro o area di memoria TAPE1 è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00B2` (`178` decimale)
- **Range**: `$00B2`-`$00B3`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Address of tape buffer #1y

### Commodore-64-intern-Buch (Commodore)
Diese beiden Speicherzellen zeigen auf
den Bandpuffer ($033C)

### C64 Programmer's Reference Guide (Commodore)
Pointer: Start of Tape Buffer

### Memory Map (Jim Butterfield)
Pntr : start of tape buffer

### Mapping the Commodore 64 (Sheldon Leemon)
On power-on, this pointer is set to the address of the cassette buffer
(828, $033C).  This pointer must contain an address greater than or
equal to 512 ($0200), or an ILLEGAL DEVICE NUMBER error will be sent
when tape I/O is tried.

### Reference (Joe Forster / STA)
Default: $033C, 828.

### 64'er Magazin (64'er)
Beim Einschalten des Computers werden diese Speicherzellen in Low-/High-Byte-
Darstellung auf die Anfangsadresse des Kassetten-Puffers gesetzt. Beim VC 20
und C 64 ist dies die Adresse 828 ($033C).

Durch Verbiegen dieses Zeigers kann der Kassettenpuffer auf beliebige Plätze
des Speichers, aber nicht unterhalb der Adresse 512 verschoben werden. Das kann
durchaus sinnvoll sein, um im Kassettenpuffer abgelegte Maschinenprogramme vor
Überschreiben durch Kassettenoperationen zu schützen.

### 64map (—)
Pointer: Start Address of Tape Buffer ($033C)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-00b2-tape1]]

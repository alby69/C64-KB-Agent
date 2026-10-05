---
id: 00c3-memuss
type: entity
title: Kernel setup pointer
aliases:
- Kernel setup pointer
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/00c3-memuss.md
  sha256: 04f6046c88a3d956e18ce05ab642f9a668b9bf570b2c37248bed3d85cc9d9938
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-00c3-memuss
---

# Kernel setup pointer



# MEMUSS — Kernel setup pointer ($00C3)

## Panoramica
Il registro o area di memoria MEMUSS è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00C3` (`195` decimale)
- **Range**: `$00C3`-`$00C4`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Cassette load temps (2 bytes)

### Original Source Comments (Microsoft/Commodore)


### Commodore-64-intern-Buch (Commodore)
Hier steht in LOU- und HIGH-Byte der
Zeiger auf den Tape-Header im
Bandpuffer.

### C64 Programmer's Reference Guide (Commodore)
Tape Load Temps

### Memory Map (Jim Butterfield)
Kernel setup pointer

### Reference (Joe Forster / STA)
Start address for a secondary address of 0 for LOAD and VERIFY from serial bus or datasette. Pointer to ROM table of default vectors during initialization of I/O vectors

### 64'er Magazin (64'er)
Bei jedem LOAD- und SAVE-Befehl für Kassetten wird der Vorspann (Tape Header),
in dem Programmtyp, Anfangs- und Endadresse aufgezeichnet sind, im
Kassettenpuffer ab Adresse 828 gespeichert. Der eigentliche Teil des Programms
steht dann im Programmspeicher.

In den Speicherzellen 195 und 196 steht in der Low-/High-Byte-Darstellung diese
Adresse, ab der das Programm beginnt. Ich habe für alle diejenigen, die mit der
Datasette arbeiten, im Texteinschub Nr. 20 »Tape-Header« die Zusammenhänge mit
einem Beispiel dargestellt.

### 64map (—)
Pointer: Type 3 Tape LOAD and general use

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-00c3-memuss]]

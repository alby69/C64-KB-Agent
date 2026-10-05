---
id: 00a7-inbit
type: entity
title: Tp Wrt ldr count/Rd pass/inbit
aliases:
- Tp Wrt ldr count/Rd pass/inbit
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/00a7-inbit.md
  sha256: 00133dcb7ccf463af34c7a980fdda8298eda4c176240b1dd0bfd723730e08461
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-00a7-inbit
---

# Tp Wrt ldr count/Rd pass/inbit



# INBIT — Tp Wrt ldr count/Rd pass/inbit ($00A7)

## Panoramica
Il registro o area di memoria INBIT è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00A7` (`167` decimale)
- **Range**: `$00A7`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
RS-232 rcvr input bit storage

### Original Source Comments (Microsoft/Commodore)
Cassette: holds FSBLK, used to direct routines, because of exit case

### Commodore-64-intern-Buch (Commodore)
Diese Register werden häufig von
Kassettenoperationen und der RS-232
Schnittstelle als Zwischenspeicher
benutzt.

### C64 Programmer's Reference Guide (Commodore)
RS-232 Input Bits / Cassette Temp

### Memory Map (Jim Butterfield)
Tp Wrt ldr count/Rd pass/inbit

### Mapping the Commodore 64 (Sheldon Leemon)
This location is used to temporarily store each bit of serial data
that is received, as well as for miscellaneous tasks by tape I/O.

### Reference (Joe Forster / STA)
Bit buffer during RS232 input

### 64'er Magazin (64'er)
Diese Speicherzelle wird verwendet, um jedes Bit, welches von einem RS232-Kanal
über den User-Port eingelesen wird, zwischenzuspeichern.

Außerdem verwenden mehrere Kassetten-Routinen diese Adresse als
Zwischenspeicher.

### 64map (—)
RS232 temporary for received Bit/Tape temporary

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-00a7-inbit]]

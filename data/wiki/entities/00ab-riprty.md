---
id: 00ab-riprty
type: entity
title: Wr lead length/Rd checksum/parity
aliases:
- Wr lead length/Rd checksum/parity
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/00ab-riprty.md
  sha256: 35a17137d37a02c85f0ea110ea0b82a5760ce17e377b0543d0f041c3ff6593c2
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-00ab-riprty
---

# Wr lead length/Rd checksum/parity



# RIPRTY — Wr lead length/Rd checksum/parity ($00AB)

## Panoramica
Il registro o area di memoria RIPRTY è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00AB` (`171` decimale)
- **Range**: `$00AB`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
RS-232 rcvr parity storage

### Original Source Comments (Microsoft/Commodore)
Cassette: short cnt; left over from debugging

### C64 Programmer's Reference Guide (Commodore)
RS-232 Input Parity / Cassette Short Cnt

### Memory Map (Jim Butterfield)
Wr lead length/Rd checksum/parity

### Mapping the Commodore 64 (Sheldon Leemon)
This location is used to help detect if data was lost during RS-232
transmission, or if a tape leader is completed.

### Reference (Joe Forster / STA)
Parity during RS232 input. Computed block checksum during datasette input

### 64'er Magazin (64'er)
Diese Speicherzelle wird vom Betriebssystem benutzt, um festzustellen, ob
während einer RS232-Datenübertragung Bits verloren gingen. Da derartige
Prüfungen mit Parity-Bits (Quersummenprüfung) des öfteren erwähnt werden, gebe
ich eine kurze Beschreibung des Prüfprinzips im Texteinschub 18
»Fehlererkennung mit Parity-Bits«.

Zusätzlich wird in 171 die Länge des Band-Vorspanns bei seiner Erzeugung
gezählt.

### 64map (—)
RS232 Input parity/Tape temporary

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-00ab-riprty]]

---
id: 009b-prty
type: entity
title: Tape character parity
aliases:
- Tape character parity
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/009b-prty.md
  sha256: 1fb8ba66e267880d43041d6d1a9691c89e018fc81897737a84c57cdbfffc6cc9
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-009b-prty
---

# Tape character parity



# PRTY — Tape character parity ($009B)

## Panoramica
Il registro o area di memoria PRTY è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$009B` (`155` decimale)
- **Range**: `$009B`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Cassette: holds current calculated parity bit

### Commodore-64-intern-Buch (Commodore)
Über diese Speicherzelle findet eine
Parity-Prüfung (Quersummenbildung)
statt. Dies dient dazu, um Lese- und
Schreibfehler zu vermeiden.

### C64 Programmer's Reference Guide (Commodore)
Tape Character Parity

### Memory Map (Jim Butterfield)
Tape character parity

### Mapping the Commodore 64 (Sheldon Leemon)
This location is used to help detect when bits of information have
been lost during transmission of tape data.

### Reference (Joe Forster / STA)
Unknown. (Parity bit during datasette input/output.)

### 64'er Magazin (64'er)
Die Commodore-Datasette ist deswegen so zuverlässig, weil sie mehrere Methoden
zur Fehlererkennung beziehungsweise Korrektur von Lese- und Schreibfehlern verwendet.

Eine der Methoden ist die sogenannte Parity-Prüfung. Sie ist nichts anderes als
eine Quersummenbildung der einzelnen Stellen jedes Bytes, deren Resultat überprüft wird.

Die Speicherzelle 155 wird bei dieser Parity-Prüfung eingesetzt.

### 64map (—)
Parity of Byte Output to Tape

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-009b-prty]]

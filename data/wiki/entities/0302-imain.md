---
id: 0302-imain
type: entity
title: Basic warm start link
aliases:
- Basic warm start link
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0302-imain.md
  sha256: a86742720ef3a46034321ed45c57add4e4451b1d98e8170d35004a44dd5085ab
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0302-imain
---

# Basic warm start link



# IMAIN — Basic warm start link ($0302)

## Panoramica
Il registro o area di memoria IMAIN è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0302` (`770` decimale)
- **Range**: `$0302`-`$0303`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
indirect MAIN (system direct loop)

### Commodore-64-intern-Buch (Commodore)
$A483 Vektor für Eingabe einer Zeile

### C64 Programmer's Reference Guide (Commodore)
Vector: BASIC Warm Start

### Memory Map (Jim Butterfield)
Basic warm start link

### Mapping the Commodore 64 (Sheldon Leemon)
This vector points to the address of the main BASIC program loop at
42115 ($A483).  This is the routine that is operating when you are in
the direct mode (READY).  It executes statements, or stores them as
program lines.

### Reference (Joe Forster / STA)
Default: $A483.

### 64'er Magazin (64'er)
Dieser Vektor zeigt auf die Adresse 42115 ($A483), beim VC 20 auf 50307
($C483). Die dort beginnende Routine steuert den Direkt-Modus, indem sie
entweder direkt eingegebene Befehle ausführt oder mit Zeilennummer eingegebene
Anweisungen speichert.

### 64map (—)
Vector: Indirect entry to BASIC Input Line and Decode ($A483)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-0302-imain]]

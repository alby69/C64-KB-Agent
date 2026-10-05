---
id: 0322-iclrch
type: entity
title: Restore I/0 vector ($F333)
aliases:
- Restore I/0 vector ($F333)
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0322-iclrch.md
  sha256: 666c8d19531d2e2136e13b3fe961f7315c4533f769cc9d8cb3662f2e7523e021
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0322-iclrch
---

# Restore I/0 vector ($F333)



# ICLRCH — Restore I/0 vector ($F333) ($0322)

## Panoramica
Il registro o area di memoria ICLRCH è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0322` (`802` decimale)
- **Range**: `$0322`-`$0323`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)


### Commodore-64-intern-Buch (Commodore)
$F333 CLRCH-Vektor

### C64 Programmer's Reference Guide (Commodore)
KERNAL CLRCHN Routine Vector

### Memory Map (Jim Butterfield)
Restore I/0 vector ($F333)

### Mapping the Commodore 64 (Sheldon Leemon)
Vector to Kernal CLRCHN Routine (Currently at 62259 ($F333))

### Reference (Joe Forster / STA)
Default: $F333.

### 64'er Magazin (64'er)
Der Name dieser Routine ist die Abkürzung für »clear channel«. Diese Routine,
die ab Adresse 62259 ($F333) - beim VC 20 ab 62461 ($F3F3) - beginnt, setzt
alle Kanäle in den Einschaltzustand zurück. Das heißt, das Eingabegerät ist die
Tastatur, das Ausgabegerät ist der Bildschirm.

### 64map (—)
Vector: Indirect entry to Kernal CLRCHN Routine ($F333)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-0322-iclrch]]

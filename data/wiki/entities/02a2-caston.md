---
id: 02a2-caston
type: entity
title: CIA 1 Timer A control log
aliases:
- CIA 1 Timer A control log
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/02a2-caston.md
  sha256: e30e9432676e161ce58ccce49732a4d5684dc11e195e2f7b37174861c9d4b02c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-02a2-caston
---

# CIA 1 Timer A control log



# CASTON — CIA 1 Timer A control log ($02A2)

## Panoramica
Il registro o area di memoria CASTON è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$02A2` (`674` decimale)
- **Range**: `$02A2`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
TOD sense during cassettes

### Commodore-64-intern-Buch (Commodore)
Bei Bandroutinen wird hier das
HIGH-Byte von Timer A zwischengespeichert.

### C64 Programmer's Reference Guide (Commodore)
TOD Sense During Cassette I/O

### Memory Map (Jim Butterfield)
CIA 1 Timer A control log

### Mapping the Commodore 64 (Sheldon Leemon)
Indicator of CIA #1 Control Register B Activity During Cassette I/O

### Reference (Joe Forster / STA)
Temporary area for saving original value of CIA#1 timer #1 control register, at memory address $DC0E, during datasette input/output

### 64'er Magazin (64'er)
Mit CIA werden die beiden »Complex Interface Adapter« des C 64 bezeichnet. Das
sind integrierte Schaltkreise, die Ein- und Ausgabeoperationen steuern. Jeder
der beiden CIAs hat mehrere Register. Das Steuerregister A (Adresse 56334
beziehungsweise $DC0E) beeinflußt die Zählregister des CIA, die ihrerseits die
Ein- und Ausgabe von Daten auf beziehungsweise von Kassetten steuern. Das
Betriebssystem speichert zu diesem Zweck geeignete Bitmuster in der
Speicherzelle 674 ab, die von da in das Steuerregister transferiert werden.

### 64map (—)
TOD sense during Tape I/O

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-02a2-caston]]

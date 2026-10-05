---
id: 00a5-cntdn
type: entity
title: Countdown, tape write/bit count
aliases:
- Countdown, tape write/bit count
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/00a5-cntdn.md
  sha256: 02e18442303e661cae9584b4d7389cfa2f058bfcef86d916f72b8642b27fcf9a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-00a5-cntdn
---

# Countdown, tape write/bit count



# CNTDN — Countdown, tape write/bit count ($00A5)

## Panoramica
Il registro o area di memoria CNTDN è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00A5` (`165` decimale)
- **Range**: `$00A5`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Temp used by serial routine

### Original Source Comments (Microsoft/Commodore)
Cassette sync countdown

### Commodore-64-intern-Buch (Commodore)
Diese Speicherzelle wird als Zähler
des Synchron-Bits verwendet.

### C64 Programmer's Reference Guide (Commodore)
Cassette Sync Countdown

### Memory Map (Jim Butterfield)
Countdown, tape write/bit count

### Mapping the Commodore 64 (Sheldon Leemon)
Used to count down the number of synchronization characters that are
sent before the actual data in a tape block.

### Reference (Joe Forster / STA)
Bit counter during serial bus input/output. Counter for sync mark during datasette output

### 64'er Magazin (64'er)
Beim Abspeichern eines Programms auf ein Band werden vor den eigentlichen Daten
mehrere Bits zusätzlich gespeichert, die beim Einlesen dieses Bandes zur
Synchronisierung dienen, das heißt zum Übereinstimmen der Geschwindigkeit der
Datenübertragung.

Die Speicherzelle 165 wird als Zähler dieses Synchron-Bits verwendet.

### 64map (—)
Tape Synchronising count down

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-00a5-cntdn]]

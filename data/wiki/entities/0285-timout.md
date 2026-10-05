---
id: 0285-timout
type: entity
title: Serial bus timeout flag
aliases:
- Serial bus timeout flag
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0285-timout.md
  sha256: 6e0040759ddff18722d8856c31159b69b4ff59a1488aa1d30bac49eeb4187d49
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0285-timout
---

# Serial bus timeout flag



# TIMOUT — Serial bus timeout flag ($0285)

## Panoramica
Il registro o area di memoria TIMOUT è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0285` (`645` decimale)
- **Range**: `$0285`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
IEEE timeout flag

### Commodore-64-intern-Buch (Commodore)
Alle Zähler in dieser Speicherzelle,
die größer als 128 sind, bedeuten, daß
ein Gerät angeschlossen ist. Die
kleineren Werte bedeuten das
Gegenteil.

### C64 Programmer's Reference Guide (Commodore)
Flag: Kernal Variable for IEEE Timeout

### Memory Map (Jim Butterfield)
Serial bus timeout flag

### Mapping the Commodore 64 (Sheldon Leemon)
This location is used only with the external IEEE interface card
(which was not yet available from Commodore at the time of writing).
For more information, see the entry for the Kernal SETTMO routine at
65057 ($FE21).

### Reference (Joe Forster / STA)
Unused. (Serial bus timeout.)

### 64'er Magazin (64'er)
Diese Speicherzelle ist etwas mysteriös. Sie kommt im ganzen Betriebssystem nur
ein einziges Mal zum Einsatz, und zwar als Flagge beim Betrieb der sogenannten
IEEE-488-Interface-Karte. Wenn diese Flagge gesetzt ist, wartet der Computer 64
Millisekunden lang, ob er von einem angeschlossenen Gerät angesprochen wird.
Wenn kein Signal kommt, gibt er ein Fehlersignal aus.

Zahlen in der Zelle 645, die kleiner als 128 sind, bedeuten Flagge gesetzt,
größer als 128 löschen sie die Flagge.

### 64map (—)
Serial IEEE Bus timeout defeat Flag

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-0285-timout]]

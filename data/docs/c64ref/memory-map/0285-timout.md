---
title: Serial bus timeout flag
source_url: https://github.com/mist64/c64ref/blob/main/src/c64mem/reference.txt
category: reference
topics:
- memory-map
- zero-page
- rom-layout
difficulty: intermediate
language: assembly
hardware:
- C64
related: []
scraped_at: '2026-07-29'
c64ref:
  module: c64mem
  source_files:
  - reference.txt
  - original_source_comments.txt
  - commodore-64-intern-buch.txt
  - 64'er_magazin.txt
  - mapping_the_commodore_64.txt
  - memory_map.txt
  - c64_programmer's_reference_guide.txt
  - 64map.txt
  address: $0285
  symbol: TIMOUT
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: IEEE timeout flag
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Alle Zähler in dieser Speicherzelle,
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Flag: Kernal Variable for IEEE Timeout'
  - name: Memory Map
    author: Jim Butterfield
    description: Serial bus timeout flag
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This location is used only with the external IEEE interface card
  - name: Reference
    author: Joe Forster / STA
    description: Unused. (Serial bus timeout.)
  - name: 64'er Magazin
    author: 64'er
    description: Diese Speicherzelle ist etwas mysteriös. Sie kommt im ganzen Betriebssystem
      nur
  - name: 64map
    author: —
    description: Serial IEEE Bus timeout defeat Flag
---

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
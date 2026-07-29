---
title: Basic warm start link
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
  address: $0302
  address_end: $0303
  symbol: IMAIN
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: indirect MAIN (system direct loop)
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: $A483 Vektor für Eingabe einer Zeile
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Vector: BASIC Warm Start'
  - name: Memory Map
    author: Jim Butterfield
    description: Basic warm start link
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This vector points to the address of the main BASIC program loop
      at
  - name: Reference
    author: Joe Forster / STA
    description: 'Default: $A483.'
  - name: 64'er Magazin
    author: 64'er
    description: Dieser Vektor zeigt auf die Adresse 42115 ($A483), beim VC 20 auf
      50307
  - name: 64map
    author: —
    description: 'Vector: Indirect entry to BASIC Input Line and Decode ($A483)'
---

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
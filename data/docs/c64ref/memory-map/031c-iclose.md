---
title: CLOSE vector ($F291)
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
related:
- close
- f291-im-akku
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
  address: $031C
  address_end: $031D
  symbol: ICLOSE
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: ''
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: $F291 CLOSE-Vektor
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: KERNAL CLOSE Routine Vector
  - name: Memory Map
    author: Jim Butterfield
    description: CLOSE vector ($F291)
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: Vector to Kernal CLOSE Routine (Currently at 62097 ($F291))
  - name: Reference
    author: Joe Forster / STA
    description: 'Default: $F291.'
  - name: 64'er Magazin
    author: 64'er
    description: Dieser Vektor zeigt auf die Adresse 62097 ($F291) - beim VC 20 auf
      62282
  - name: 64map
    author: —
    description: 'Vector: Indirect entry to Kernal CLOSE Routine ($F291)'
---

# ICLOSE — CLOSE vector ($F291) ($031C)

## Panoramica
Il registro o area di memoria ICLOSE è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$031C` (`796` decimale)
- **Range**: `$031C`-`$031D`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)


### Commodore-64-intern-Buch (Commodore)
$F291 CLOSE-Vektor

### C64 Programmer's Reference Guide (Commodore)
KERNAL CLOSE Routine Vector

### Memory Map (Jim Butterfield)
CLOSE vector ($F291)

### Mapping the Commodore 64 (Sheldon Leemon)
Vector to Kernal CLOSE Routine (Currently at 62097 ($F291))

### Reference (Joe Forster / STA)
Default: $F291.

### 64'er Magazin (64'er)
Dieser Vektor zeigt auf die Adresse 62097 ($F291) - beim VC 20 auf 62282
($F34A). Ab hier beginnt eine Routine, die beim CLOSE-Befehl zuerst prüft, ob
die Datei-Nummer in der Tabelle der eröffneten Datei enthalten ist. Dann holt
sie die dazugehörige Geräte-Nummer und Sekundär-Adresse und schließt den Kanal
und die Datei.

### 64map (—)
Vector: Indirect entry to Kernal CLOSE Routine ($F291)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
---
title: Set - input vector ($F20E)
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
- f20e-chkin-eingabegert-setzen
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
  address: $031E
  address_end: $031F
  symbol: ICHKIN
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: ''
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: $F20E CHKIN-Vektor
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: KERNAL CHKIN Routine
  - name: Memory Map
    author: Jim Butterfield
    description: Set - input vector ($F20E)
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: Vector to Kernal CHKIN Routine (Currently at 61966 ($F20E))
  - name: Reference
    author: Joe Forster / STA
    description: 'Default: $F20E.'
  - name: 64'er Magazin
    author: 64'er
    description: Diese Routine beginnt ab Adresse 61966 ($F20E) - beim VC 20 ab 62161
      ($F2C7).
  - name: 64map
    author: —
    description: 'Vector: Indirect entry to Kernal CHKIN Routine ($F20E)'
---

# ICHKIN — Set - input vector ($F20E) ($031E)

## Panoramica
Il registro o area di memoria ICHKIN è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$031E` (`798` decimale)
- **Range**: `$031E`-`$031F`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)


### Commodore-64-intern-Buch (Commodore)
$F20E CHKIN-Vektor

### C64 Programmer's Reference Guide (Commodore)
KERNAL CHKIN Routine

### Memory Map (Jim Butterfield)
Set - input vector ($F20E)

### Mapping the Commodore 64 (Sheldon Leemon)
Vector to Kernal CHKIN Routine (Currently at 61966 ($F20E))

### Reference (Joe Forster / STA)
Default: $F20E.

### 64'er Magazin (64'er)
Diese Routine beginnt ab Adresse 61966 ($F20E) - beim VC 20 ab 62161 ($F2C7).
Sie eröffnet einen Datenkanal zur Übernahme von Daten von dem Gerät, das durch
den OPEN-Befehl angegeben worden ist.

### 64map (—)
Vector: Indirect entry to Kernal CHKIN Routine ($F20E)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
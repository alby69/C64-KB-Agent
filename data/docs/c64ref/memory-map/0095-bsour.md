---
title: Serial deferred character
source_url: https://github.com/mist64/c64ref/blob/main/src/c64mem/reference.txt
category: reference
topics:
- memory-map
- zero-page
- rom-layout
- zero-page
difficulty: beginner
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
  address: $0095
  symbol: BSOUR
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Char buffer for IEEE
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Hier wird das Zeichen abgelegt,
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Buffered Character for Serial Bus
  - name: Memory Map
    author: Jim Butterfield
    description: Serial deferred character
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This is the character waiting to be sent.  A 255 ($FF) indicates
      that
  - name: Reference
    author: Joe Forster / STA
    description: Serial bus output cache, previous byte to be sent to serial bus
  - name: 64'er Magazin
    author: 64'er
    description: In dieser Speicherzelle wird das Zeichen abgelegt, welches als nächstes
      über
  - name: 64map
    author: —
    description: Buffered Character for Serial Bus
---

# BSOUR — Serial deferred character ($0095)

## Panoramica
Il registro o area di memoria BSOUR è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0095` (`149` decimale)
- **Range**: `$0095`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Char buffer for IEEE

### Commodore-64-intern-Buch (Commodore)
Hier wird das Zeichen abgelegt,
welches über den seriellen Port zur
Floppy oder zum Drucker geschickt
werden soll, sobald die Adresse $0094
Bereitschaft zeigt.

### C64 Programmer's Reference Guide (Commodore)
Buffered Character for Serial Bus

### Memory Map (Jim Butterfield)
Serial deferred character

### Mapping the Commodore 64 (Sheldon Leemon)
This is the character waiting to be sent.  A 255 ($FF) indicates that
no character is waiting for serial output.

### Reference (Joe Forster / STA)
Serial bus output cache, previous byte to be sent to serial bus

### 64'er Magazin (64'er)
In dieser Speicherzelle wird das Zeichen abgelegt, welches als nächstes über
den Serial-Port zum Floppy-Gerät oder zum Drucker transportiert wird, sobald
die Flagge in 148 die Bereitschaft anzeigt.

### 64map (—)
Buffered Character for Serial Bus

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
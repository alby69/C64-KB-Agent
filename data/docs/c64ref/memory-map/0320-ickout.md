---
title: Set - output vector ($F250)
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
- f250-ckout-ausgabegert-setzen
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
  address: $0320
  address_end: $0321
  symbol: ICKOUT
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: ''
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: $F250 CKOUT-Vektor
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: KERNAL CHKOUT Routine
  - name: Memory Map
    author: Jim Butterfield
    description: Set - output vector ($F250)
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: Vector to Kernal CKOUT Routine (Currently at 62032 ($F250))
  - name: Reference
    author: Joe Forster / STA
    description: 'Default: $F250.'
  - name: 64'er Magazin
    author: 64'er
    description: Dieser Vektor zeigt auf die Adresse 62032 ($F250) - beim VC 20 auf
      62217
  - name: 64map
    author: —
    description: 'Vector: Indirect entry to Kernal CHKOUT Routine ($F250)'
---

# ICKOUT — Set - output vector ($F250) ($0320)

## Panoramica
Il registro o area di memoria ICKOUT è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0320` (`800` decimale)
- **Range**: `$0320`-`$0321`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)


### Commodore-64-intern-Buch (Commodore)
$F250 CKOUT-Vektor

### C64 Programmer's Reference Guide (Commodore)
KERNAL CHKOUT Routine

### Memory Map (Jim Butterfield)
Set - output vector ($F250)

### Mapping the Commodore 64 (Sheldon Leemon)
Vector to Kernal CKOUT Routine (Currently at 62032 ($F250))

### Reference (Joe Forster / STA)
Default: $F250.

### 64'er Magazin (64'er)
Dieser Vektor zeigt auf die Adresse 62032 ($F250) - beim VC 20 auf 62217
($F309). Dort beginnt die Routine, welche einen Datenkanal zur Abgabe von Daten
an das im OPEN-Befehl angegebene Gerät aufmacht.

### 64map (—)
Vector: Indirect entry to Kernal CHKOUT Routine ($F250)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
---
title: CIA 1 Timer A enabled flag
source_url: https://github.com/mist64/c64ref/blob/main/src/c64mem/original_source_comments.txt
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
  - original_source_comments.txt
  - commodore-64-intern-buch.txt
  - 64'er_magazin.txt
  - mapping_the_commodore_64.txt
  - memory_map.txt
  - c64_programmer's_reference_guide.txt
  - 64map.txt
  address: $02A4
  symbol: STUPID
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: 'Cassette: hold indicator (NZ - no T1IRQ yet) for T1IRQ'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Hier wird bei Bandroutinen angegeben,
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Temp D1 IRQ Indicator For Cassette Read
  - name: Memory Map
    author: Jim Butterfield
    description: CIA 1 Timer A enabled flag
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: 'Save Area for CIA #1 Control Register A During Cassette Read'
  - name: 64'er Magazin
    author: 64'er
    description: Derselbe Wert, der bei der Vorbereitung des Lesevorganges von der
      Kassette in
  - name: 64map
    author: —
    description: Temporary D1IRQ Indicator during Tape READ
---

# STUPID — CIA 1 Timer A enabled flag ($02A4)

## Panoramica
Il registro o area di memoria STUPID è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$02A4` (`676` decimale)
- **Range**: `$02A4`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Cassette: hold indicator (NZ - no T1IRQ yet) for T1IRQ

### Commodore-64-intern-Buch (Commodore)
Hier wird bei Bandroutinen angegeben,
ob Timer A läuft oder nicht. Wenn hier
eine $00 steht, ist der Timer
freigegeben, andernfalls ist er
gesperrt.

### C64 Programmer's Reference Guide (Commodore)
Temp D1 IRQ Indicator For Cassette Read

### Memory Map (Jim Butterfield)
CIA 1 Timer A enabled flag

### Mapping the Commodore 64 (Sheldon Leemon)
Save Area for CIA #1 Control Register A During Cassette Read

### 64'er Magazin (64'er)
Derselbe Wert, der bei der Vorbereitung des Lesevorganges von der Kassette in
die Speicherzelle 674 kommt, gelangt auch nach 676, von wo er zu einem späteren
Zeitpunkt beim Lesen zu Vergleichszwecken herangezogen wird.

### 64map (—)
Temporary D1IRQ Indicator during Tape READ

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
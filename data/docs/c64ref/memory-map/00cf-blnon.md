---
title: Cursor in blink phase
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
  address: $00CF
  symbol: BLNON
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: On/off blink flag
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: In diesem Register wird festgehalten,
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Flag: Last Cursor Blink On/Off'
  - name: Memory Map
    author: Jim Butterfield
    description: Cursor in blink phase
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This location keeps track of whether, during the current cursor blink,
  - name: Reference
    author: Joe Forster / STA
    description: 'Values:'
  - name: 64'er Magazin
    author: 64'er
    description: In dieser Speicherzelle wird festgehalten, in welcher der beiden
      Blink-Phasen -
  - name: 64map
    author: —
    description: 'Flag: Cursor Status; $00 = Off, $01 = On'
---

# BLNON — Cursor in blink phase ($00CF)

## Panoramica
Il registro o area di memoria BLNON è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00CF` (`207` decimale)
- **Range**: `$00CF`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
On/off blink flag

### Commodore-64-intern-Buch (Commodore)
In diesem Register wird festgehalten,
in welcher Blink-Phase sich der Cursor
gerade befindet.

### C64 Programmer's Reference Guide (Commodore)
Flag: Last Cursor Blink On/Off

### Memory Map (Jim Butterfield)
Cursor in blink phase

### Mapping the Commodore 64 (Sheldon Leemon)
This location keeps track of whether, during the current cursor blink,
the character under the cursor was reversed, or was restored to
normal.  This location will contain a 0 if the character is reversed,
and a 1 if the character is restored to its nonreversed status.

### Reference (Joe Forster / STA)
Values:

* $00: Cursor off phase, original character visible.
* $01: Cursor on phase, reverse character visible.

### 64'er Magazin (64'er)
In dieser Speicherzelle wird festgehalten, in welcher der beiden Blink-Phasen -
normal oder revers - der Cursor sich gerade befindet. Eine 0 bedeutet reverses
Zeichen, eine 1 bedeutet ein normales Zeichen.

Die Abfrage innerhalb eines Basic-Programms funktioniert nicht. Denn die
Interrupt-Routine steuert den Phasenwechsel.

### 64map (—)
Flag: Cursor Status; $00 = Off, $01 = On

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
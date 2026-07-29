---
title: Read character error/outbyte buf
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
  address: $00B6
  symbol: RODATA
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: RS-232 trns byte buffer
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: 'Cassette: has combined error values from bit routines'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Dieses Register wird als Ausgabezwischenspeicher
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: RS-232 Out Byte Buffer
  - name: Memory Map
    author: Jim Butterfield
    description: Read character error/outbyte buf
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: RS-232 routines use this area to disassemble each byte to be sent
      from
  - name: Reference
    author: Joe Forster / STA
    description: Byte buffer during RS232 output
  - name: 64'er Magazin
    author: 64'er
    description: Bei Ausgabe von Daten über die RS232-Schnittstelle wird jedes Byte
      in seine
  - name: 64map
    author: —
    description: RS232 Output Byte Buffer/Tape Read Error Flag
---

# RODATA — Read character error/outbyte buf ($00B6)

## Panoramica
Il registro o area di memoria RODATA è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00B6` (`182` decimale)
- **Range**: `$00B6`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
RS-232 trns byte buffer

### Original Source Comments (Microsoft/Commodore)
Cassette: has combined error values from bit routines

### Commodore-64-intern-Buch (Commodore)
Dieses Register wird als Ausgabezwischenspeicher
benutzt.

### C64 Programmer's Reference Guide (Commodore)
RS-232 Out Byte Buffer

### Memory Map (Jim Butterfield)
Read character error/outbyte buf

### Mapping the Commodore 64 (Sheldon Leemon)
RS-232 routines use this area to disassemble each byte to be sent from
the transmission buffer pointed to by 249 ($00F9).

### Reference (Joe Forster / STA)
Byte buffer during RS232 output

### 64'er Magazin (64'er)
Bei Ausgabe von Daten über die RS232-Schnittstelle wird jedes Byte in seine
Einzelteile zerlegt, bevor es über den Ausgabepuffer seriell übertragen wird.
DerAusgabepufferwird im obersten Teil des Programmspeichers angelegt (siehe
auch Speicherzellen 55 und 56); die genaue Anfangsadresse steht in
Speicherzelle 248. Auch die Ausgabe von Daten auf die Kassette verwendet Zelle
182 als Ausgabe-Zwischenspeicher.

### 64map (—)
RS232 Output Byte Buffer/Tape Read Error Flag

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
---
title: l = Tp timer enabled; bit count
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
  address: $00B4
  symbol: BITTS
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: RS-232 trns bit count
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: 'Cassette: flags if we have byte SYNC (a longlong)'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Hier wird die Anzahl der übertragenden
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: RS-232 Out Bit Count / Cassette Temp
  - name: Memory Map
    author: Jim Butterfield
    description: l = Tp timer enabled; bit count
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: RS-232 routines use this to count the number of bits transmitted,
      and
  - name: Reference
    author: Joe Forster / STA
    description: 'Bits:'
  - name: 64'er Magazin
    author: 64'er
    description: Die RS232-Routinen verwenden die Speicherzelle 180, um die Zahl der
  - name: 64map
    author: —
    description: RS232 Write bit count/Tape Read timing Flag
---

# BITTS — l = Tp timer enabled; bit count ($00B4)

## Panoramica
Il registro o area di memoria BITTS è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00B4` (`180` decimale)
- **Range**: `$00B4`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
RS-232 trns bit count

### Original Source Comments (Microsoft/Commodore)
Cassette: flags if we have byte SYNC (a longlong)

### Commodore-64-intern-Buch (Commodore)
Hier wird die Anzahl der übertragenden
Bits gezählt.

### C64 Programmer's Reference Guide (Commodore)
RS-232 Out Bit Count / Cassette Temp

### Memory Map (Jim Butterfield)
l = Tp timer enabled; bit count

### Mapping the Commodore 64 (Sheldon Leemon)
RS-232 routines use this to count the number of bits transmitted, and
for parity and stop bit manipulation.  Tape load routines use this
location to flag when they are ready to receive data bytes.

### Reference (Joe Forster / STA)
Bits:

* Bits #0-#6: Bit count.
* Bit #7: 0 = Data bit; 1 = Stop bit.

Bit counter during datasette input/output.

### 64'er Magazin (64'er)
Die RS232-Routinen verwenden die Speicherzelle 180, um die Zahl der
übertragenen Bits zu zählen, außerdem für Parity-Berechnung (siehe Texteinschub
18) und Stop-Bit-Bearbeitung.

Die Lade-Routinen für Kassettenbetrieb benutzen diese Zelle als Flagge, die
angibt, ob der Computer bereit ist, Daten zu übernehmen.

### 64map (—)
RS232 Write bit count/Tape Read timing Flag

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
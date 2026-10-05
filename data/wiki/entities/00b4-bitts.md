---
id: 00b4-bitts
type: entity
title: l = Tp timer enabled; bit count
aliases:
- l = Tp timer enabled; bit count
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/00b4-bitts.md
  sha256: e220a51753f7451d6e5479d4f9fdd237b1054aeff2fb96841d8ba266db17fa19
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-00b4-bitts
---

# l = Tp timer enabled; bit count



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

## References
- Source: [[src-00b4-bitts]]

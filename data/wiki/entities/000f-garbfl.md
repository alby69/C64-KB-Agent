---
id: 000f-garbfl
type: entity
title: DATA scan/LIST quote/memry flag
aliases:
- DATA scan/LIST quote/memry flag
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/000f-garbfl.md
  sha256: b5e831bd4c4135b30bce24cb580af78f294dd8dc182e294ee8a8cdfdb6ff0b37
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-000f-garbfl
---

# DATA scan/LIST quote/memry flag



# GARBFL — DATA scan/LIST quote/memry flag ($000F)

## Panoramica
Il registro o area di memoria GARBFL è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$000F` (`15` decimale)
- **Range**: `$000F`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Whether to do garbage collection

### Original Source Comments (Microsoft/Commodore)
Turned on when "data"
being scanned by crunch so unquoted
strings won't be crunched.

### Commodore-64-intern-Buch (Commodore)
Durch diese Speicherzelle wird beim
LIST-Befehl durch ein Hochkomma
erkannt, ob eine Textkette folgt.
Zusätzlich wird in dieser
Speicherzelle markiert, ob eine
Garbage Collection durchgeführt
werden muß oder nicht.

### C64 Programmer's Reference Guide (Commodore)
Flag: DATA scan/LIST quote/Garbage Coll

### Memory Map (Jim Butterfield)
DATA scan/LIST quote/memry flag

### Mapping the Commodore 64 (Sheldon Leemon)
The LIST routine uses this byte as a flag to let it know when it has
come to a character string in quotes.  It will then print the string,
rather than search it for BASIC keyword tokens.

The garbage collection routine uses this location as a flag to
indicate that garbage collection has already been tried before adding
a new string.  If there is still not enough memory, an OUT OF MEMORY
message will result.

This location is also used as a work byte for the process of
converting a line of text in the BASIC input buffer (512, $0200) into a
linked program line of BASIC keyword tokens.

### Reference (Joe Forster / STA)
Garbage collection indicator during memory allocation for string variable; $00-$7F = There was no garbage collection yet; $80 = Garbage collection already took place

### Reference (Joe Forster / STA)
Quotation mode switch during tokenization; Bit #6: 0 = Normal mode; 1 = Quotation mode. Quotation mode switch during LIST; $01 = Normal mode; $FE = Quotation mode

### 64'er Magazin (64'er)
Die Routine des LIST-Befehls muß unterscheiden zwischen Basic-Befehlen und
normalem Text. Wenn eine Zeichenkette durch ein »Gänsefüßchen« identifiziert
worden ist, wird die Flagge gesetzt, und der Text wird ausgedruckt.

Unter »Garbage Collection« (Müllabfuhr) wird die Routine des Betriebssystems
verstanden, welche zu bestimmten Anlässen im Variablenspeicher alle nicht mehr
benötigten Strings entfernt, um Platz zu schaffen. Dabei wird eine Flagge in
Zelle 15 gesetzt, die anzeigt, daß eine Müllabfuhr bereits stattgefunden hat.
Wenn bei der Speicherung eines neuen Strings zu wenig Speicherplatz vorhanden
ist, wird bei der Flagge nachgesehen, ob gerade vorher schon durch die
Müllabfuhr (Garbage Collection) der Speicher entrümpelt worden ist. Falls das
der Fall ist, wird OUT OF MEMORY angezeigt, falls nicht, wird eine Müllabfuhr
durchgeführt.

Schließlich wird Zelle 15 auch bei der Umwandlung von Basic-Befehlen in
internen Codezahlen (Tokens) eingesetzt.

### 64map (—)
Flag: DATA scan/List Quote/Garbage collection

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-000f-garbfl]]

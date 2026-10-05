---
id: 009a-dflto
type: entity
title: Output CMD device, normally 3
aliases:
- Output CMD device, normally 3
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/009a-dflto.md
  sha256: 7cf79a29f4067fd702363c75c5b9795879e39a35e9c783b3ecefe0ba083aeb21
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-009a-dflto
---

# Output CMD device, normally 3



# DFLTO — Output CMD device, normally 3 ($009A)

## Panoramica
Il registro o area di memoria DFLTO è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$009A` (`154` decimale)
- **Range**: `$009A`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Default output device #

### Commodore-64-intern-Buch (Commodore)
Diese Speicherzelle ist mit der
vorherigen zu vergleichen, nur steht
hier die Nummer des Geräts, über das
die Ausgabe erfolgt.

### C64 Programmer's Reference Guide (Commodore)
Default Output (CMD) Device (3)

### Memory Map (Jim Butterfield)
Output CMD device, normally 3

### Mapping the Commodore 64 (Sheldon Leemon)
The default value of this location is 3, which designates the screen
as the current output device.  That value can be changed by the Kernal
routine CHKOUT (62032, $F250), which uses this location to store the
device number of the device whose file it defines as an output
channel.

BASIC calls CHKOUT whenever the command PRINT# or CMD is executed, but
clears the channel after the PRINT# operation has been completed.

### Reference (Joe Forster / STA)
Default: $03, screen.

### 64'er Magazin (64'er)
Diese Speicherzelle entspricht der Zelle 153, nur steht hier die Nummer des
Gerätes, über das die Ausgabe läuft.

Nach dem Einschalten und nach Ausgabeoperationen wird der Wert immer auf 3
gesetzt. Das ist entsprechend der oben genannten Zuordnung der Bildschirm.

Für Maschinenprogrammierer sei erwähnt, daß Basic bei den Befehlen PRINT# oder
CMD die Routine CHKOUT einsetzt, welche die Adresse 154 belegt. Sie steht im C
64 ab Adresse 62032 ($F250), im VC 20 ab 62217 ($F309).

### 64map (—)
Default Output Device (3)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-009a-dflto]]

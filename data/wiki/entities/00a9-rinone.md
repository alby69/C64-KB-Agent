---
id: 00a9-rinone
type: entity
title: Wrt start bit/Rd bit err/stbit
aliases:
- Wrt start bit/Rd bit err/stbit
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/00a9-rinone.md
  sha256: f64abf2a18cddb8606b1cfe549e9915e6a5f258bed8f0f421d3b466683843439
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-00a9-rinone
---

# Wrt start bit/Rd bit err/stbit



# RINONE — Wrt start bit/Rd bit err/stbit ($00A9)

## Panoramica
Il registro o area di memoria RINONE è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00A9` (`169` decimale)
- **Range**: `$00A9`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
RS-232 rcvr flag for start bit check

### Original Source Comments (Microsoft/Commodore)
Cassette: counts zeros (if Z then correct # of dipoles)

### C64 Programmer's Reference Guide (Commodore)
RS-232 Flag: Check for Start Bit

### Memory Map (Jim Butterfield)
Wrt start bit/Rd bit err/stbit

### Mapping the Commodore 64 (Sheldon Leemon)
This flag is used when checking for a start bit.  A 144 ($90) here
indicates that no start bit was received, while a 0 means that a start
bit was received.

### Reference (Joe Forster / STA)
Values:

* $00: Data bit.
* $01-$FF: Stop bit.

### 64'er Magazin (64'er)
Ein RS232-Datentransfer prüft, ob ein Start-Bit empfangen worden ist. Im
positiven Fall steht in Zelle 169 die Zahl 144, im negativen Fall eine 0.

### 64map (—)
RS232 Flag: Start Bit check/Tape temporary

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-00a9-rinone]]

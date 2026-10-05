---
id: 00b5-nxtbit
type: entity
title: Tp EOT/RS232 next bit to send
aliases:
- Tp EOT/RS232 next bit to send
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/00b5-nxtbit.md
  sha256: 9474593d5300dc66c98ef0fc028e8006c6a37fd807f8f60ab25ab8fd81ef77e1
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-00b5-nxtbit
---

# Tp EOT/RS232 next bit to send



# NXTBIT — Tp EOT/RS232 next bit to send ($00B5)

## Panoramica
Il registro o area di memoria NXTBIT è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00B5` (`181` decimale)
- **Range**: `$00B5`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
RS-232 trns next bit to be sent

### Original Source Comments (Microsoft/Commodore)
Cassette: used to preserve SYNO (outside of bit routines)

### Commodore-64-intern-Buch (Commodore)
Diese Speicherzelle enthält immer das
nächste Bit, das bei RS-232 Operationen
übertragen werden soll.

### C64 Programmer's Reference Guide (Commodore)
RS-232 Next Bit to Send/ Tape EOT Flag

### Memory Map (Jim Butterfield)
Tp EOT/RS232 next bit to send

### Mapping the Commodore 64 (Sheldon Leemon)
This location is used by the RS-232 routines to hold the next bit to
be sent, and by the tape routines to indicate what part of a block the
read routine is currently reading.

### Reference (Joe Forster / STA)
Bit buffer (in bit #2) during RS232 output

### 64'er Magazin (64'er)
Bei RS232-Operationen enthält die Zelle 181 das jeweils nächste Bit, welches
übertragen werden soll. Bandoperationen entnehmen dieser Speicherzelle, welcher
Block gerade gelesen wird.

### 64map (—)
RS232 Next Bit to send/Tape Read - End of Tape

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-00b5-nxtbit]]

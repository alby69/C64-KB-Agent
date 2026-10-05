---
id: d40d-surel2
type: entity
title: Voice 2 Sustain/Release Control Register
aliases:
- Voice 2 Sustain/Release Control Register
tags:
- io-map
- sid-registers
sources:
- path: data/docs/c64ref/io-map/sid/d40d-surel2.md
  sha256: 0af08cfdff6a96c050f57c29d7d09bce2a109f00508f05d309661df25227620f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-d40d-surel2
---

# Voice 2 Sustain/Release Control Register



# SUREL2 — Voice 2 Sustain/Release Control Register ($D40D)

## Panoramica
Il registro o area di memoria SUREL2 è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$D40D` (`54285` decimale)
- **Range**: `$D40D`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
7-4  Select Sustain Cycle Duration: 0-15
3-0  Select Release Cycle Duration: 0-15

### Mapping the Commodore 64 (Sheldon Leemon)
0-3  Select release cycle duration (0-15)
4-7  Select sustain volume level (0-15)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-d40d-surel2]]

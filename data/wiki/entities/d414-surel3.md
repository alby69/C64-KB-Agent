---
id: d414-surel3
type: entity
title: Voice 3 Sustain/Release Control Register
aliases:
- Voice 3 Sustain/Release Control Register
tags:
- io-map
- sid-registers
sources:
- path: data/docs/c64ref/io-map/sid/d414-surel3.md
  sha256: 150bf79b17dbf8a4e5080fee53653877678ceab786641de050c70d293483292e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-d414-surel3
---

# Voice 3 Sustain/Release Control Register



# SUREL3 — Voice 3 Sustain/Release Control Register ($D414)

## Panoramica
Il registro o area di memoria SUREL3 è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$D414` (`54292` decimale)
- **Range**: `$D414`
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
- Source: [[src-d414-surel3]]

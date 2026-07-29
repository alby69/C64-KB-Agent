---
title: Voice 3 Sustain/Release Control Register
source_url: https://github.com/mist64/c64ref/blob/main/src/c64io/mapping_the_commodore_64.txt
category: reference
topics:
- io-map
- sid-registers
difficulty: intermediate
language: assembly
hardware:
- SID
related: []
scraped_at: '2026-07-29'
c64ref:
  module: c64io
  source_files:
  - mapping_the_commodore_64.txt
  - c64_programmer's_reference_guide.txt
  address: $D414
  symbol: SUREL3
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: '7-4  Select Sustain Cycle Duration: 0-15'
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: 0-3  Select release cycle duration (0-15)
---

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
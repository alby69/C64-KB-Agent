---
title: Envelope Generator 3 Output
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
  address: $D41C
  symbol: ENV3
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Envelope Generator 3 Output
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This register allows you to read the output of the voice 3 Envelope
---

# ENV3 — Envelope Generator 3 Output ($D41C)

## Panoramica
Il registro o area di memoria ENV3 è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$D41C` (`54300` decimale)
- **Range**: `$D41C`
- **Dimensione**: `1 byte`
- **Permessi**: `R`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
Envelope Generator 3 Output

### Mapping the Commodore 64 (Sheldon Leemon)
This register allows you to read the output of the voice 3 Envelope
     generator, in much the same way that the preceding register lets you
     read the output of Oscillator 3.  This output can also be added to
     another oscillator's Frequency Control Registers, Pulse Width
     Registers, or the Filter Frequency Control Register.  In order to
     produce any output from this register, however, the gate bit in
     Control Register 3 must be set to 1.  Just as in the production of
     sound, setting the gate bit to 1 starts the attack/decay/sustain
     cycle, and setting it back to 0 starts the release cycle.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
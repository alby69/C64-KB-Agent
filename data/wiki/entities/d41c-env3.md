---
id: d41c-env3
type: entity
title: Envelope Generator 3 Output
aliases:
- Envelope Generator 3 Output
tags:
- io-map
- sid-registers
sources:
- path: data/docs/c64ref/io-map/sid/d41c-env3.md
  sha256: 7ada4c0809da8311ecea63f3591cc34dfcc06fe43a7f1d77861007406238a191
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-d41c-env3
---

# Envelope Generator 3 Output



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

## References
- Source: [[src-d41c-env3]]

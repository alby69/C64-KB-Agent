---
id: d40b-vcreg2
type: entity
title: Voice 2 Control Register
aliases:
- Voice 2 Control Register
tags:
- io-map
- sid-registers
sources:
- path: data/docs/c64ref/io-map/sid/d40b-vcreg2.md
  sha256: 3b55091274514411a0843ed89625666845fa6ee7dc6f5683b1e1a1c3bd9a5b65
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-d40b-vcreg2
---

# Voice 2 Control Register



# VCREG2 — Voice 2 Control Register ($D40B)

## Panoramica
Il registro o area di memoria VCREG2 è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$D40B` (`54283` decimale)
- **Range**: `$D40B`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
7    Select Random Noise Waveform, 1 = On
6    Select Pulse Waveform, 1 = On
5    Select Sawtooth Waveform, 1 = On
4    Select Triangle Waveform, 1 = On
3    Test Bit: 1 = Disable Oscillator 1
2    Ring Modulate Osc. 2 with Osc. 1 Output,
       1 = On
1    Synchronize Osc.2 with Osc. 1 Frequency,
       1 = On
0    Gate Bit: 1 = Start Att/Dec/Sus,
               0 = Start Release

### Mapping the Commodore 64 (Sheldon Leemon)
0    Gate Bit:  1=Start attack/decay/sustain, 0=Start release
1    Sync Bit:  1=Synchronize oscillator with Oscillator 1 frequency
2    Ring Modulation:  1=Ring modulate Oscillators 2 and 1
3    Test Bit:  1=Disable Oscillator 2
4    Select triangle waveform
5    Select sawtooth waveform
6    Select pulse waveform
7    Select noise waveform

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-d40b-vcreg2]]

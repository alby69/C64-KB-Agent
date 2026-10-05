---
id: d412-vcreg3
type: entity
title: Voice 3 Control Register
aliases:
- Voice 3 Control Register
tags:
- io-map
- sid-registers
sources:
- path: data/docs/c64ref/io-map/sid/d412-vcreg3.md
  sha256: d7886c0757113bd4df616c693f643dbd1f27df6897e8414ecc6fa8f9b6d8381f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-d412-vcreg3
---

# Voice 3 Control Register



# VCREG3 — Voice 3 Control Register ($D412)

## Panoramica
Il registro o area di memoria VCREG3 è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$D412` (`54290` decimale)
- **Range**: `$D412`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
7    Select Random Noise Waveform, 1 = On
6    Select Pulse Waveform, 1 = On
5    Select Sawtooth Waveform, 1 = On
4    Select Triangle Waveform, 1 = On
3    Test Bit: 1 = Disable Oscillator 1
2    Ring Modulate Osc. 3 with Osc. 2 Output,
       1 = On
1    Synchronize Osc. 3 with Osc.2 Frequency,
       1 = On
0    Gate Bit: 1 = Start Att/Dec/Sus,
               0 = Start Release

### Mapping the Commodore 64 (Sheldon Leemon)
0    Gate Bit:  1=Start attack/decay/sustain, 0=Start release
1    Sync Bit:  1=Synchronize oscillator with Oscillator 2 frequency
2    Ring Modulation:  1=Ring modulate Oscillators 3 and 2
3    Test Bit:  1=Disable Oscillator 3
4    Select triangle waveform
5    Select sawtooth waveform
6    Select pulse waveform
7    Select noise waveform

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-d412-vcreg3]]

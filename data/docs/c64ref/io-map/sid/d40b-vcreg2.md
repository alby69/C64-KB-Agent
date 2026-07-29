---
title: Voice 2 Control Register
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
  address: $D40B
  symbol: VCREG2
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 7    Select Random Noise Waveform, 1 = On
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: '0    Gate Bit:  1=Start attack/decay/sustain, 0=Start release'
---

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
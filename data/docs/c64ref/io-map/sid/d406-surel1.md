---
title: Voice 1 Sustain/Release Control Register
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
  address: $D406
  symbol: SUREL1
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: '7-4  Select Sustain Cycle Duration: 0-15'
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: 0-3  Select release cycle duration (0-15)
---

# SUREL1 — Voice 1 Sustain/Release Control Register ($D406)

## Panoramica
Il registro o area di memoria SUREL1 è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$D406` (`54278` decimale)
- **Range**: `$D406`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
7-4  Select Sustain Cycle Duration: 0-15
3-0  Select Release Cycle Duration: 0-15

### Mapping the Commodore 64 (Sheldon Leemon)
0-3  Select release cycle duration (0-15)
4-7  Select sustain volume level (0-15)

     Bits 4-7 select the volume level at which the note is sustained.
     Following the decay cycle, the volume of the output of voice 1 will
     remain at the selected sustain level as long as the gate bit of the
     Control Register is set to 1.  The sustain values range from 0, which
     chooses no volume, to 15, which sets the output of voice 1 equal to
     the peak volume achieved during the attack cycle.

     Bits 0-3 determine the length of the release cycle.  This phase, in
     which the volume fades from the sustain level to near zero volume,
     begins when the gate bit of the Control Register is set to 0 (while
     leaving the waveform setting that was previously chosen).  The
     duration of this decline in volume corresponds to the number (0-15)
     selected in the same way as for the decay value:

     |    |                  |
     |----|------------------|
     |  0 | 6 milliseconds   |
     |  1 | 24 milliseconds  |
     |  2 | 48 milliseconds  |
     |  3 | 72 milliseconds  |
     |  4 | 114 milliseconds |
     |  5 | 168 milliseconds |
     |  6 | 204 milliseconds |
     |  7 | 240 milliseconds |
     |  8 | 300 milliseconds |
     |  9 | 750 milliseconds |
     | 10 | 1.5 seconds      |
     | 11 | 2.4 seconds      |
     | 12 | 3 seconds        |
     | 13 | 9 seconds        |
     | 14 | 15 seconds       |
     | 15 | 24 seconds       |

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
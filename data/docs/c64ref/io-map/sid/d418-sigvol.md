---
title: Volume and Filter Select Register
source_url: https://github.com/mist64/c64ref/blob/main/src/c64io/mapping_the_commodore_64.txt
category: reference
topics:
- io-map
- sid-registers
difficulty: intermediate
language: assembly
hardware:
- SID
related:
- d417
scraped_at: '2026-07-29'
c64ref:
  module: c64io
  source_files:
  - mapping_the_commodore_64.txt
  - c64_programmer's_reference_guide.txt
  address: $D418
  symbol: SIGVOL
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: '7    Cut-Off Voice 3 Output: 1 = Off, 0 = On'
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: 0-3  Select output volume (0-15)
---

# SIGVOL — Volume and Filter Select Register ($D418)

## Panoramica
Il registro o area di memoria SIGVOL è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$D418` (`54296` decimale)
- **Range**: `$D418`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
7    Cut-Off Voice 3 Output: 1 = Off, 0 = On
6    Select Filter High-Pass Mode: 1 = On
5    Select Filter Band-Pass Mode: 1 = On
4    Select Filter Low-Pass Mode: 1 = On
3-0  Select Output Volume: 0-15

### Mapping the Commodore 64 (Sheldon Leemon)
0-3  Select output volume (0-15)
4    Select low-pass filter, 1=low-pass on
5    Select band-pass filter, 1=band-pass on
6    Select high-pass filter, 1=high-pass on
7    Disconnect output of voice 4, 1=voice 3 off

     Bits 0-3 control the volume of all outputs.  The possible volume
     levels range from 0 (no volume) to 15 (maximum volume).  Some level of
     volume must be set here before any sound can be heard.

     Bits 4-6 control the selection of the low-pass, band-pass, or
     high-pass filter.  A 1 in any of these bits turns the corresponding
     filter on.  These filters can be combined, although only one cutoff
     frequency can be chosen.  In order for the filter to have any effect,
     at least one of the voices must be routed through it using the Filter
     Resonance Control Register at 54295 ($D417).

     When Bit 7 is set to 1,  it disconnects the output of voice 3.  This
     allows you to use the output of the oscillator for modulating the
     frequency of the other voices, or for generating random number,
     without any undesired audio output.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
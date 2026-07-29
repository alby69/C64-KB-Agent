---
title: See locations 56334 and 56334 for details
source_url: https://github.com/mist64/c64ref/blob/main/src/c64io/mapping_the_commodore_64.txt
category: reference
topics:
- io-map
- cia-registers
difficulty: intermediate
language: assembly
hardware:
- CIA
related: []
scraped_at: '2026-07-29'
c64ref:
  module: c64io
  source_files:
  - mapping_the_commodore_64.txt
  - c64_programmer's_reference_guide.txt
  address: $DD0E
  address_end: $DD0F
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: '7    Time-of-Day Clock Frequency: 1 = 50 Hz,'
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: See locations 56334 and 56334 for details
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: 0    Start Timer A (1=start, 0=stop)
---

# $DD0E — See locations 56334 and 56334 for details ($DD0E)

## Panoramica
Il registro o area di memoria $DD0E è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$DD0E` (`56590` decimale)
- **Range**: `$DD0E`-`$DD0F`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
7    Time-of-Day Clock Frequency: 1 = 50 Hz,
       0 = 60 Hz
6    Serial Port I/O Mode Output, 0 = Input
5    Timer A Counts: 1 = CNT Signals,
       0 = System 02 Clock
4    Force Load Timer A: 1 = Yes
3    Timer A Run Mode: 1 = One-Shot,
       0 = Continuous
2    Timer A Output Mode to PB6: 1 = Toggle,
       0 = Pulse
1    Timer A Output on PB6: 1 = Yes, 0 = No
0    Start/Stop Timer A: 1 = Start, 0 = Stop

### Mapping the Commodore 64 (Sheldon Leemon)
See locations 56334 and 56334 for details

### Mapping the Commodore 64 (Sheldon Leemon)
0    Start Timer A (1=start, 0=stop)
1    Select Timer A output on Port B (1=Timer A output appears on
       Bit 6 of Port B)
2    Port B output mode (1=toggle Bit 6, 0=pulse Bit 6 for one
       cycle)
3    Timer A run mode (1=one-shot, 0=continuous)
4    Force latched value to be loaded to Timer A counter (1=force
       load strobe)
5    Timer A input mode (1=count microprocessor cycles, 0=count
       signals on CNT line at pin 4 of User Port)
6    Serial Port (56588, $DD0C) mode (1=output, 0=input)
7    Time of Day Clock frequency (1=50 Hz required on TOD pin,
       0=60 Hz)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
---
title: Control Register B
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
  address: $DD0F
  symbol: CI2CRB
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: '7    Set Alarm/TOD-Clock: 1=Alarm, 0=Clock'
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: 0    Start Timer B (1=start, 0=stop)
---

# CI2CRB — Control Register B ($DD0F)

## Panoramica
Il registro o area di memoria CI2CRB è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$DD0F` (`56591` decimale)
- **Range**: `$DD0F`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
7    Set Alarm/TOD-Clock: 1=Alarm, 0=Clock
6-5  Timer B Mode Select:
       00 = Count System 02 Clock Pulses
       01 = Count Positive CNT Transitions
       10 = Count Timer A Underflow Pulses
       11 = Count Timer A Underflows While
         CNT Positive
4-0  Same as CIA Control Reg. A - for Timer B

### Mapping the Commodore 64 (Sheldon Leemon)
0    Start Timer B (1=start, 0=stop)
1    Select Timer B output on Port B (1=Timer B output appears on
     Bit 7 of Port B)
2    Port B output mode (1=toggle Bit 7, 0=pulse Bit 7 for one
       cycle)
3    Timer B run mode (1=one shot, 0=continuous)
4    Force latched value to be loaded to Timer B counter (1=force
       load strobe)
5-6  Timer B input mode
         00 = Timer B counts microprocessor cycles
         01 = Count signals on CNT line at pin 4 of User Port
         10 = Count each time that Timer A counts down to 0
         11 = Count Timer A 0's when CNT pulses are also present
7    Select Time of Day write (0=writing to TOD registers sets
       alarm, 1=writing to ROD registers sets clock)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
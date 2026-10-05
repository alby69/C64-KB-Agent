---
id: dd0f-ci2crb
type: entity
title: Control Register B
aliases:
- Control Register B
tags:
- cia-registers
- io-map
sources:
- path: data/docs/c64ref/io-map/cia/dd0f-ci2crb.md
  sha256: 8a2d2f27076538a58a95e1aa952bf3d6e85f95579ef605ef5750c527cce4b9bc
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-dd0f-ci2crb
---

# Control Register B



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

## References
- Source: [[src-dd0f-ci2crb]]

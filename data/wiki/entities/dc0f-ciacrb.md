---
id: dc0f-ciacrb
type: entity
title: Control Register B
aliases:
- Control Register B
tags:
- cia-registers
- io-map
sources:
- path: data/docs/c64ref/io-map/cia/dc0f-ciacrb.md
  sha256: d7f99ab18d0982b4f70406cfc964bd72298893591dd697ebf280024d56d19fcc
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-dc0f-ciacrb
---

# Control Register B



# CIACRB — Control Register B ($DC0F)

## Panoramica
Il registro o area di memoria CIACRB è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$DC0F` (`56335` decimale)
- **Range**: `$DC0F`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
7    Set Alarm/TOD-Clock: 1 = Alarm,
       0 = Clock
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
3    Timer B run mode (1=one-shot, 0=continuous)
4    Force latched value to be loaded to Timer B counter (1=force
       load strobe)
5-6  Timer B input mode
         00 = Timer B counts microprocessor cycles
         01 = Count signals on CNT line at pin 4 of User Port
         10 = Count each time that Timer A counts down to 0
         11 = Count Timer A 0's when CNT pulses are also present
7    Select Time of Day write (0=writing to TOD registers sets
     alarm, 1=writing to TOD registers sets clock)

     Bits 0-3.  This nybble performs the same functions for Timer B that
     Bits 0-3 of Control Register A perform for Timer A, except that Timer
     B output on Data Port B appears at Bit 7, and not Bit 6.

     Bits 5 and 6.  These two bits are used to select what Timer B counts.
     If both bits are set to 0, Timer B counts the microprocessor machine
     cycles (which occur at the rate of 1,022,730 cycles per second).  If
     Bit 6 is set to 0 and Bit 5 is set to 1, Timer B counts pulses on the
     CNT line, which is connected to pin 4 of the User Port.  If Bit 6 is
     set to 1 and Bit 5 is set to 0, Timer B counts Timer A underflow
     pulses, which is to say that it counts the number of times that Timer
     A counts down to 0.  This is used to link the two numbers into one
     32-bit timer that can count up to 70 minutes with accuracy to within
     1/15 second.  Finally, if both bits are set to 1, Timer B counts the
     number of times that Timer A counts down to 0 and there is a signal on
     the CNT line (pin 4 of the User Port).

     Bit 7.  Bit 7 controls what happens when you write to the Time of Day
     registers.  If this bit is set to 1, writing to the TOD registers sets
     the ALARM time.  If this bit is cleared to 0, writing to the TOD
     registers sets the TOD clock.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-dc0f-ciacrb]]

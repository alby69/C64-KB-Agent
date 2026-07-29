---
title: Control Register A
source_url: https://github.com/mist64/c64ref/blob/main/src/c64io/mapping_the_commodore_64.txt
category: reference
topics:
- io-map
- cia-registers
difficulty: intermediate
language: assembly
hardware:
- CIA
related:
- dc0c
scraped_at: '2026-07-29'
c64ref:
  module: c64io
  source_files:
  - mapping_the_commodore_64.txt
  - c64_programmer's_reference_guide.txt
  address: $DC0E
  symbol: CIACRA
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: '7    Time-of-Day Clock Frequency: 1 = 50 Hz,'
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: 0    Start Timer A (1=start, 0=stop)
---

# CIACRA — Control Register A ($DC0E)

## Panoramica
Il registro o area di memoria CIACRA è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$DC0E` (`56334` decimale)
- **Range**: `$DC0E`
- **Dimensione**: `1 byte`
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
0    Start Timer A (1=start, 0=stop)
1    Select Timer A output on Port B (1=Timer A output appears on Bit 6 of
       Port B)
2    Port B output mode (1=toggle Bit 6, 0=pulse Bit 6 for one cycle)
3    Timer A run mode (1=one-shot, 0=continuous)
4    Force latched value to be loaded to Timer A counter (1=force load
       strobe)
5    Timer A input mode (1=count microprocessor cycles, 0=count signals on
       CNT line at pin 4 of User Port)
6    Serial Port (56332, $DC0C) mode (1=output, 0=input)
7    Time of Day Clock frequency (1=50 Hz required on TOD pin, 0=60 Hz)

     Bits 0-3.  This nybble controls Timer A.  Bit 0 is set to 1 to start
     the timer counting down, and set to 0 to stop it.  Bit 3 sets the
     timer for one-shot or continuous mode.

     In one-shot mode, the timer counts down to 0, sets the counter value
     back to the latch value, and then sets Bit 0 back to 0 to stop the
     timer.  In continuous mode, it reloads the latch value and starts all
     over again.

     Bits 1 and 2 allow you to send a signal on Bit 6 of Data Port B when
     the timer counts.  Setting Bit 1 to 1 forces this output (which
     overrides the Data Direction Register B Bit 6, and the normal Data
     Port B value).  Bit 2 allows you to choose the form this output to Bit
     6 of Data Port B will take.  Setting Bit 2 to a value of 1 will cause
     Bit 6 to toggle to the opposite value when the timer runs down (a
     value of 1 will change to 0, and a value of 0 will change to 1).
     Setting Bit 2 to a value of 0 will cause a single pulse of a one
     machine-cycle duration (about a millionth of a second) to occur.

     Bit 4.  This bit is used to load the Timer A counter with the value
     that was previously written to the Timer Low and High Byte Registers.
     Writing a 1 to this bit will force the load (although there is no data
     stored here, and the bit has no significance on a read).

     Bit 5.  Bit 5 is used to control just what it is Timer A is counting.
     If this bit is set to 1, it counts the microprocessor machine cycles
     (which occur at the rate of 1,022,730 cycles per second).  If the bit
     is set to 0, the timer counts pulses on the CNT line, which is
     connected to pin 4 of the User Port.  This allows you to use the CIA
     as a frequency counter or an event counter, or to measure pulse width
     or delay times of external signals.

     Bit 6.  Whether the Serial Port Register is currently inputting or
     outputting data (see the entry for that register at 56332 ($DC0C) for
     more information) is controlled by this bit.

     Bit 7.  This bit allows you to select from software whether the Time
     of Day Clock will use a 50 Hz or 60 Hz signal on the TOD pin in order
     to keep accurate time (the 64 uses a 60 Hz signal on that pin).

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
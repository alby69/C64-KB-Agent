---
title: Interrupt Control Register
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
  address: $DC0D
  symbol: CIAICR
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 7    IRQ Flag (1 = IRQ Occurred) / Set-
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: 0    Read / did Timer A count down to 0?  (1=yes).
---

# CIAICR — Interrupt Control Register ($DC0D)

## Panoramica
Il registro o area di memoria CIAICR è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$DC0D` (`56333` decimale)
- **Range**: `$DC0D`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
7    IRQ Flag (1 = IRQ Occurred) / Set-
       Clear Flag
4    FLAG1 IRQ (Cassette Read / Serial Bus
       SRQ Input)
3    Serial Port Interrupt
2    Time-of-Day Clock Alarm Interrupt
1    Timer B Interrupt
0    Timer A Interrupt

### Mapping the Commodore 64 (Sheldon Leemon)
0    Read / did Timer A count down to 0?  (1=yes).
     Write/ enable or disable Timer A interrupt (1=enable, 0=disable)
1    Read / did Timer B count down to 0?  (1=yes).
     Write/ enable or disable Timer B interrupt (1=enable, 0=disable)
2    Read / did Time of Day Clock reach the alarm time?  (1=yes).
     Write/ enable or disable TOD clock alarm interrupt (1=enable,
     0=disable)
3    Read / did the serial shift register finish a byte? (1=yes).
     Write/ enable or disable serial shift register interrupt (1=enable,
     0=disable)
4    Read / was a signal sent on the flag line?  (1=yes).
     Write/ enable or disable FLAG line interrupt (1=enable, 0=disable)
5    Not used
6    Not used
7    Read / did any CIA #1 source cause an interrupt?  (1=yes).
     Write/ set or clear bits of this register (1=bits written with 1 will
     be set, 0=bits written with 1 will be cleared)

     This register is used to control the five interrupt sources on the
     6526 CIA chip.  These sources are Timer A, Timer B, the Time of Day
     Clock, the Serial Register, and the FLAG line.  Timers A and B cause
     an interrupt when they count down to 0.  The Time of Day Clock
     generates an interrupt when it reaches the ALARM time.  The Serial
     Shift Register interrupts when it compiles eight bits of input or
     output.  An external signal pulling the CIA hardware line called FLAG
     low will also cause an interrupt (on CIA #1, this FLAG line is
     connected to the Cassette Read line of the Cassette Port).

     Even if the condition for a particular interrupt is satisfied, the
     interrupt must still be enabled for an IRQ actually to occur.  This is
     done by writing to the Interrupt Control Register.  What happens when
     you write to this register depends on the way that you set Bit 7.  If
     you set it to 0, any other bit that was written to with a 1 will be
     cleared, and the corresponding interrupt will be disabled.  If you set
     Bit 7 to 1, any bit written to with a 1 will be set, and the
     corresponding interrupt will be enabled.  In either case, the
     interrupt enable flags for those bits written to with a 0 will not be
     affected.

     For example, in order to disable all interrupts from BASIC, you could
     POKE 56333, 127.  This sets Bit 7 to 0, which clears all of the other
     bits, since they are all written with 1's.  Don't try this from BASIC
     immediate mode, as it will turn off Timer A which causes the IRQ for
     reading the keyboard, so that it will in effect turn off the keyboard.

     To turn on the Timer A interrupt, a program could POKE 56333,129.  Bit
     7 is set to 1 and so is Bit 0, so the interrupt which corresponds to
     Bit 0 (Timer A) is enabled.

     When you read this register, you can tell if any of the conditions for
     a CIA Interrupt were satisfied because the corresponding bit will be
     set to a 1.  For example, if Timer A counts down to 0, Bit 0 of this
     register will be set to 1.  If, in addition, the mask bit that
     corresponds to that interrupt source is set to 1, and an interrupt
     occurs, Bit 7 will also be set.  This allows a multi-interrupt system
     to read one bit and see if the source of a particular interrupt was
     CIA #1.  You should note, however, that reading this register clears
     it, so you should preserve its contents in RAM if you want to test
     more than one bit.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
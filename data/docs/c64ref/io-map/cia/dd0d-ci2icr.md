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
related:
- dc0d
scraped_at: '2026-07-29'
c64ref:
  module: c64io
  source_files:
  - mapping_the_commodore_64.txt
  - c64_programmer's_reference_guide.txt
  address: $DD0D
  symbol: CI2ICR
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 7    NMI Flag (1 = NMI Occurred) / Set-
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: 0    Read / did Timer A count down to 0?  (1=yes).
---

# CI2ICR — Interrupt Control Register ($DD0D)

## Panoramica
Il registro o area di memoria CI2ICR è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$DD0D` (`56589` decimale)
- **Range**: `$DD0D`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
7    NMI Flag (1 = NMI Occurred) / Set-
       Clear Flag
4    FLAG1 NMI (User/RS-232 Received Data
       Input)
3    Serial Port Interrupt
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
3    Read / did the serial shift register finish a byte?  (1=yes).
     Write/ enable or disable serial shift register interrupt (1=enable,
     0=disable)
4    Read / was a signal sent on the FLAG line?  (1=yes).
     Write/ enable or disable FLAG line interrupt (1=enable, 0=disable)
5    Not used
6    Not used
7    Read / did any CIA #2 source cause an interrupt?  (1=yes).
     Write/ set or clear bits of this register (1=bits written with 1 will
     be set, 0=bits written with 1 will be cleared)

     This register is used to control the five interrupt sources on the
     6526 CIA chip.  For details on its operation, see the entry for 56333
     ($DC0D).  The main difference between these two chips pertaining to
     this register is that on CIA #2, the FLAG line is connected to Pin B
     of the User Port, and thus is available to the user who wishes to take
     advantage of its ability to cause interrupts for handshaking purposes.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
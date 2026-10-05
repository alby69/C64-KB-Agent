---
id: dd0d-ci2icr
type: entity
title: Interrupt Control Register
aliases:
- Interrupt Control Register
tags:
- cia-registers
- io-map
sources:
- path: data/docs/c64ref/io-map/cia/dd0d-ci2icr.md
  sha256: cc42b90fcc175eabc5ff759490d1159db9bc878f8ef3b25a22422e4797e00eee
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-dd0d-ci2icr
---

# Interrupt Control Register



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

## References
- Source: [[src-dd0d-ci2icr]]

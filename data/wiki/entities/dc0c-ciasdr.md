---
id: dc0c-ciasdr
type: entity
title: Serial Data Port
aliases:
- Serial Data Port
tags:
- cia-registers
- io-map
sources:
- path: data/docs/c64ref/io-map/cia/dc0c-ciasdr.md
  sha256: cc9c16cb090275445e3f62f5a56337dc91d73e68e499dfb50dd27820a15fbdb7
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-dc0c-ciasdr
---

# Serial Data Port



# CIASDR — Serial Data Port ($DC0C)

## Panoramica
Il registro o area di memoria CIASDR è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$DC0C` (`56332` decimale)
- **Range**: `$DC0C`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
Synchronous Serial I/O Data Buffer

### Mapping the Commodore 64 (Sheldon Leemon)
The CIA chip has an on-chip serial port, which allows you to send or
     receive a byte of data one bit at a time, with the most significant
     bit (Bit 7) being transferred first.  Control Register A at 56334
     ($DC0E) allows you to choose input or output modes.  In input mode, a
     bit of data is read from the SP line (pin 5 of the User Port) whenever
     a signal on the CNT line (pin 4) appears to let you know that it is
     time for a read.  After eight bits are received this way, the data is
     placed in the Serial Port Register, and an interrupt is generated to
     let you know that the register should be read.

     In output mode, you write data to the Serial Port Register, and it is
     sent out over the SP line (pin 5 of the User Port), using Timer A for
     the baud rate generator.  Whenever a byte of data is written to this
     register, transmission will start as long as Timer A is running and in
     continuous mode.  Data is sent at half the Timer A rage, and an output
     will appear on the CNT line (pin 4 of the User Port) whenever a bit is
     sent.  After all eight bits have been sent, an interrupt is generated
     to indicate that it is time to load the next byte to send into the
     Serial Register.

     The Serial Data Register is not used by the 64, which does all of its
     serial I/O through the regular data ports.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-dc0c-ciasdr]]

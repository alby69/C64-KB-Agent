---
title: Serial Data Port
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
- dc0e
scraped_at: '2026-07-29'
c64ref:
  module: c64io
  source_files:
  - mapping_the_commodore_64.txt
  - c64_programmer's_reference_guide.txt
  address: $DC0C
  symbol: CIASDR
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Synchronous Serial I/O Data Buffer
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: The CIA chip has an on-chip serial port, which allows you to send
      or
---

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
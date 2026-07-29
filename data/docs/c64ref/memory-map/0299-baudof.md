---
title: RS-232 speed/code
source_url: https://github.com/mist64/c64ref/blob/main/src/c64mem/reference.txt
category: reference
topics:
- memory-map
- zero-page
- rom-layout
difficulty: intermediate
language: assembly
hardware:
- C64
related: []
scraped_at: '2026-07-29'
c64ref:
  module: c64mem
  source_files:
  - reference.txt
  - original_source_comments.txt
  - commodore-64-intern-buch.txt
  - 64'er_magazin.txt
  - mapping_the_commodore_64.txt
  - memory_map.txt
  - c64_programmer's_reference_guide.txt
  - 64map.txt
  address: $0299
  address_end: $029A
  symbol: BAUDOF
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Baud rate full bit time (created by open)
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Die Übertragungsrate errechnet sich
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'RS-232 Baud Rate: Full Bit Time (us)'
  - name: Memory Map
    author: Jim Butterfield
    description: RS-232 speed/code
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: 'This location holds the prescaler value used by CIA #2 timers A
      and B.'
  - name: Reference
    author: Joe Forster / STA
    description: (Calculated automatically from default value of RS232 output timer,
      at memory...
  - name: 64'er Magazin
    author: 64'er
    description: Sobald ein RS232-Kanal eröffnet worden ist, berechnet das Betriebssystem
      einen
  - name: 64map
    author: —
    description: RS232 Baud Rate; Full Bit time microseconds
---

# BAUDOF — RS-232 speed/code ($0299)

## Panoramica
Il registro o area di memoria BAUDOF è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0299` (`665` decimale)
- **Range**: `$0299`-`$029A`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Baud rate full bit time (created by open)

### Commodore-64-intern-Buch (Commodore)
Die Übertragungsrate errechnet sich
aus der Systemfrequenz (985.25) KHz
dividiert duch die Baudrate.
Dieser Wert steht in LOW- und
HIGH-Byte-Darstellung in den beiden
Speicherzellen. Er wird vom Betriebssystem
abgerufen.

### C64 Programmer's Reference Guide (Commodore)
RS-232 Baud Rate: Full Bit Time (us)

### Memory Map (Jim Butterfield)
RS-232 speed/code

### Mapping the Commodore 64 (Sheldon Leemon)
This location holds the prescaler value used by CIA #2 timers A and B.

These timers cause an NMI interrupt to drive the RS-232 receive and
transmit routines CLOCK/PRESCALER times per second each, where CLOCK
is the system 02 frequency of 1,022,730 Hz (985,250 if you are using
the European PAL television standard rather than the American NTSC
standard), and PRESCALER is the value stored at 56580-1 ($DD04-5) and
56582-3 ($DD06-7), in low-byte, high-byte order.  You can use the
following formula to figure the correct prescaler value for a
particular RS-232 baud rate:

PRESCALER=((CLOCK/BAUDRATE)/2)-100

The American (NTSC standard) prescaler values for the standard RS-232
baud rates which the control register at 659 ($0293) makes available
are stored in a table at 65218 ($FEC2), starting with the two-byte
value used for 50 baud.  The European (PAL standard) version of that
table is located at 58604 ($E4EC).

### Reference (Joe Forster / STA)
(Calculated automatically from default value of RS232 output timer, at memory address $0295-$0296.)

### 64'er Magazin (64'er)
Sobald ein RS232-Kanal eröffnet worden ist, berechnet das Betriebssystem einen
Wert, der die Zeitdauer eines Bits festlegt. Da die Übertragungsrate in
Speicherzelle 659 einstellbar ist, hängt diese Bit-Dauer von der gewählten
Übertragungsgeschwindigkeit ab. Die Bit-Dauer errechnet sich aus der
Systemfrequenz (985,25 kHz) geteilt durch die Übertragungsgeschwindigkeit.
Dieser Wert steht in Low-/High-Byte-Darstellung in diesen beiden
Speicherzellen, von wo aus er vom Betriebssystem abgerufen wird.

### 64map (—)
RS232 Baud Rate; Full Bit time microseconds

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
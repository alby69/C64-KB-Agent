---
title: Data Port B
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
- rts
scraped_at: '2026-07-29'
c64ref:
  module: c64io
  source_files:
  - mapping_the_commodore_64.txt
  - c64_programmer's_reference_guide.txt
  address: $DD01
  symbol: CI2PRB
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 7    User / RS-232 Data Set Ready
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: 0    RS-232 data input (SIN)/ Pin C of User Port
---

# CI2PRB — Data Port B ($DD01)

## Panoramica
Il registro o area di memoria CI2PRB è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$DD01` (`56577` decimale)
- **Range**: `$DD01`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
7    User / RS-232 Data Set Ready
6    User / RS-232 Clear to Send
5    User
4    User / RS-232 Carrier Detect
3    User / RS-232 Ring Indicator
2    User / RS-232 Data Terminal Ready
1    User / RS-232 Request to Send
0    User / RS-232 Received Data

### Mapping the Commodore 64 (Sheldon Leemon)
0    RS-232 data input (SIN)/ Pin C of User Port
1    RS-232 request to send (RTS)/ Pin D of User Port
2    RS-232 data terminal ready (DTR)/ Pin E of User Port
3    RS-232 ring indicator (RI)/ Pin F of User Port
4    RS-232 carrier detect (DCD)/ Pin H of User Port
5    Pin J of User Port
6    RS-232 clear to send (CTS)/ Pin K of User Port
     Toggle or pulse data output for Timer A
7    RS-232 data set ready (DSR)/ Pin L of User Port
     Toggle or pulse data output for Timer B

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
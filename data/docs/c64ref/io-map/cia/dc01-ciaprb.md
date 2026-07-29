---
title: Data Port Register B
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
  address: $DC01
  symbol: CIAPRB
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 7-0  Read Keyboard Row Values for Keyboard
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: 0    Read keyboard row 0.
---

# CIAPRB — Data Port Register B ($DC01)

## Panoramica
Il registro o area di memoria CIAPRB è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$DC01` (`56321` decimale)
- **Range**: `$DC01`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
7-0  Read Keyboard Row Values for Keyboard
       Scan
7    Timer B Toggle/Pulse Output
6    Timer A: Toggle/Pulse Output
4    Joystick 1 Fire Button: 1 = Fire
3-2  Paddle Fire Buttons
3-0  Joystick 1 Direction

### Mapping the Commodore 64 (Sheldon Leemon)
0    Read keyboard row 0.
     Read joystick 1 up direction
1    Read keyboard row 1.
     Read joystick 1 down direction
2    Read keyboard row 2.
     Read joystick 1 left direction.
     Read paddle 1 fire button
3    Read keyboard row 3.
     Read joystick 1 right direction.
     Read paddle 2 fire button
4    Read keyboard row 4.
     Read joystick 1 fire button
5    Read keyboard row 5
6    Read keyboard row 6.
     Toggle or pulse data output for Timer A
7    Read keyboard row 7.
     Toggle or pulse data output for Timer B

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
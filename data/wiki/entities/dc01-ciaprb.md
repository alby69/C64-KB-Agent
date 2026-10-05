---
id: dc01-ciaprb
type: entity
title: Data Port Register B
aliases:
- Data Port Register B
tags:
- cia-registers
- io-map
sources:
- path: data/docs/c64ref/io-map/cia/dc01-ciaprb.md
  sha256: 2835183af9ea1499f8dfead73a3c475e41129395502a5a8a285712dce9cf92cc
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-dc01-ciaprb
---

# Data Port Register B



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

## References
- Source: [[src-dc01-ciaprb]]

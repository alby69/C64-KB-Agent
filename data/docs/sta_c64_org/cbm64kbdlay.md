---
title: Commodore 64 keyboard matrix layout
source_url: https://sta.c64.org/cbm64kbdlay.html
category: reference
topics:
- input handling
difficulty: intermediate
language: none
hardware:
- CIA
related:
- cia-registers
- keyboard-handling
- joystick-reading
scraped_at: '2026-07-20'
last_modified: Fri, 13 Feb 2015 23:00:00 GMT
---


# Commodore 64 keyboard matrix layout

| Bit#0 $01,$FE | Bit#1 $02,$FD | Bit#2 $04,$FB | Bit#3 $08,$F7 | Bit#4 $10,$EF | Bit#5 $20,$DF | Bit#6 $40,$BF | Bit#7 $80,$7F | |
|---|---|---|---|---|---|---|---|---|
| Bit#0$01,$FE | Insert/Delete | Return | cursor left/right | F7 | F1 | F3 | F5 | cursor up/down | 
| Bit#1$02,$FD | 3 | W | A | 4 | Z | S | E | left Shift | 
| Bit#2$04,$FB | 5 | R | D | 6 | C | F | T | X | 
| Bit#3$08,$F7 | 7 | Y | G | 8 | B | H | U | V | 
| Bit#4$10,$EF | 9 | I | J | 0 | M | K | O | N | 
| Bit#5$20,$DF | + (plus) | P | L | – (minus) | . (period) | : (colon) | @ (at) | , (comma) | 
| Bit#6$40,$BF | £ (pound) | * (asterisk) | ; (semicolon) | Clear/Home | right Shift (Shift Lock) | = (equal) | ↑ (up arrow) | / (slash) | 
| Bit#7$80,$7F | 1 | ← (left arrow) | Control | 2 | Space | Commodore | Q | Run/Stop | 

Notes:

- Rows refer to values for memory address $DC00, columns to values for $DC01.

---
*Fonte originale: [https://sta.c64.org/cbm64kbdlay.html](https://sta.c64.org/cbm64kbdlay.html)*


### Collegamenti e Riferimenti Hardware
- **$DC00 (CIA 1 Port A (Joystick 2, Keyboard))**: Associato al chip CIA. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#dc00).
- **$DC01 (CIA 1 Port B (Joystick 1, Keyboard))**: Associato al chip CIA. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#dc01).

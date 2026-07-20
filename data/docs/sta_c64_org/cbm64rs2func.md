---
title: Commodore 64 RS232 functions
source_url: https://sta.c64.org/cbm64rs2func.html
category: reference
topics: []
difficulty: advanced
language: none
hardware:
- KERNAL
- CPU
- CIA
related:
- cia-registers
- joystick-reading
- memory-map
- keyboard-handling
- kernal-routines
scraped_at: '2026-07-20'
last_modified: Fri, 13 Feb 2015 23:00:00 GMT
---

# Commodore 64 RS232 functions

| Address | Function | 
|---|---|
| $EF4A | Compute number of
  data bits, according to memory address $0293. | 
| $EFE1 | Define RS232 as default output. | 
| $F017 | Write byte, from RS232 output cache at
  memory address $009E, to RS232. | 
| $F04D | Define RS232 as default input. | 
| $F086 | Read byte from RS232. | 
| $F0A4 | Wait for the end of RS232 transfer and
  disable RS232 interrupts. (So that the common chip registers can be used by
  serial bus or datasette input/output.) | 
| $F14E | Read byte from RS232. | 
| $F1B8 | Read byte from RS232; retry on $00
  byte. | 
| $F1DD | Write byte to RS232. | 
| $F2AF | Close file on RS232; free RS232 input and
  output buffers, if exist. | 
| $F409 | Open file on RS232; allocate RS232 input
  and output buffers, if do not exist. | 
| $F483 | Initialize CIA #2 for opening/closing
  RS232. |

---
*Fonte originale: [https://sta.c64.org/cbm64rs2func.html](https://sta.c64.org/cbm64rs2func.html)*

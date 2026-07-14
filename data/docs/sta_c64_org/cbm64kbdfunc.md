---
title: Commodore 64 keyboard functions
source_url: https://sta.c64.org/cbm64kbdfunc.html
category: reference
topics:
- assembly
- sprite programming
difficulty: intermediate
language: assembly
hardware:
- CIA
- KERNAL
related:
- vic-ii-registers
- keyboard-handling
- sprite-programming
- raster-interrupts
- memory-map
- joystick-reading
- kernal-routines
- cia-registers
scraped_at: '2026-07-14'
last_modified: Fri, 13 Feb 2015 23:00:00 GMT
---

# Commodore 64 keyboard functions

| Address | Function | 
|---|---|
| $E5B4 | Read byte from
  keyboard buffer; shift keyboard buffer; decrease buffer pointer. | 
| $EA87 | Query keyboard; put current matrix code
  into memory address $00CB, current status of shift keys into memory address
  $028D and PETSCII code into keyboard buffer; handle Commodore-Shift; repeat
  keys. | 
| $F142 | Read byte from keyboard buffer; shift
  keyboard buffer; decrease buffer pointer. | 
| $F6BC | Update Stop key indicator, at memory
  address $0091. | 
| $F6ED | Query Stop key indicator, at memory
  address $0091; if pressed, call CLRCHN and clear keyboard buffer. | 
| Standard KERNAL functions | |
| $FF9F | SCNKEY. Query keyboard; put current matrix
  code into memory address $00CB, current status of shift keys into memory
  address $028D and PETSCII code into keyboard buffer; handle Commodore-Shift;
  repeat keys. | 
| $FFE1 | STOP. Query Stop key indicator, at memory
  address $0091; if pressed, call CLRCHN and clear keyboard buffer. |

---
*Fonte originale: [https://sta.c64.org/cbm64kbdfunc.html](https://sta.c64.org/cbm64kbdfunc.html)*

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
- CPU
- KERNAL
- CIA
related:
- vic-ii-registers
- kernal-routines
- raster-interrupts
- sprite-programming
- cia-registers
- keyboard-handling
- memory-map
- joystick-reading
scraped_at: '2026-08-03'
last_modified: Fri, 13 Feb 2015 23:00:00 GMT
---

# Commodore 64 keyboard functions

| **Address** | Function | 
|---|---|
| $E5B4 | Read byte from   keyboard buffer; shift keyboard buffer; decrease buffer pointer. Input: – Output: A = Byte read. Used registers: A, X, Y. | 
| $EA87 | Query keyboard; put current matrix code   into memory address $00CB, current status of shift keys into memory address   $028D and PETSCII code into keyboard buffer; handle Commodore-Shift; repeat   keys. Input: – Output: – Used registers: A, X, Y. | 
| $F142 | Read byte from keyboard buffer; shift   keyboard buffer; decrease buffer pointer. Input: – Output: A = Byte read; 0 = No key press available. Used registers: A, X, Y. | 
| $F6BC | Update Stop key indicator, at memory   address $0091. Input: – Output: – Used registers: A, X. | 
| $F6ED | Query Stop key indicator, at memory   address $0091; if pressed, call CLRCHN and clear keyboard buffer. Input: – Output: Zero: 0 = Not pressed, 1 = Pressed; Carry: 1 = Pressed. Used registers: A, X. | 
| **Standard KERNAL functions** |  | 
| $FF9F | SCNKEY. Query keyboard; put current matrix   code into memory address $00CB, current status of shift keys into memory   address $028D and PETSCII code into keyboard buffer; handle Commodore-Shift;   repeat keys. Input: – Output: – Used registers: A, X, Y. Real address: $EA87. | 
| $FFE1 | STOP. Query Stop key indicator, at memory   address $0091; if pressed, call CLRCHN and clear keyboard buffer. Input: – Output: Zero: 0 = Not pressed, 1 = Pressed; Carry: 1 = Pressed. Used registers: A, X. Real address: ($0328), $F6ED. |

---
*Fonte originale: [https://sta.c64.org/cbm64kbdfunc.html](https://sta.c64.org/cbm64kbdfunc.html)*

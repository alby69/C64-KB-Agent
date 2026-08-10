---
title: Commodore 64 RS232 functions
source_url: https://sta.c64.org/cbm64rs2func.html
category: reference
topics: []
difficulty: advanced
language: none
hardware:
- CIA
- CPU
- KERNAL
related:
- kernal-routines
- memory-map
- keyboard-handling
- cia-registers
- joystick-reading
scraped_at: '2026-08-10'
last_modified: Fri, 13 Feb 2015 23:00:00 GMT
---

# Commodore 64 RS232 functions

| **Address** | Function | 
|---|---|
| $EF4A | Compute number of   data bits, according to memory address $0293. Input: – Output: X = Number of data bits. Used registers: A, X. | 
| $EFE1 | Define RS232 as default output. Input: A = 2. Output: – Used registers: A. | 
| $F017 | Write byte, from RS232 output cache at   memory address $009E, to RS232. Input: – Output: – Used registers: A, Y. | 
| $F04D | Define RS232 as default input. Input: A = 2. Output: – Used registers: A. | 
| $F086 | Read byte from RS232. Input: – Output: A = Byte read. Used registers: – | 
| $F0A4 | Wait for the end of RS232 transfer and   disable RS232 interrupts. (So that the common chip registers can be used by   serial bus or datasette input/output.) Input: – Output: – Used registers: – | 
| $F14E | Read byte from RS232. Input: – Output: A = Byte read. Used registers: A. | 
| $F1B8 | Read byte from RS232; retry on $00   byte. Input: – Output: A = Byte read. Used registers: A. | 
| $F1DD | Write byte to RS232. Input: Carry = 0; A = Byte to write. Output: – Used registers: – | 
| $F2AF | Close file on RS232; free RS232 input and   output buffers, if exist. Input: – Output: – Used registers: A, X, Y. | 
| $F409 | Open file on RS232; allocate RS232 input   and output buffers, if do not exist. Input: – Output: – Used registers: A, X, Y. | 
| $F483 | Initialize CIA #2 for opening/closing   RS232. Input: – Output: – Used registers: A, Y. |

---
*Fonte originale: [https://sta.c64.org/cbm64rs2func.html](https://sta.c64.org/cbm64rs2func.html)*

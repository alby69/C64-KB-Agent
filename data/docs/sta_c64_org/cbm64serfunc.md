---
title: Commodore 64 serial bus functions
source_url: https://sta.c64.org/cbm64serfunc.html
category: reference
topics:
- assembly
difficulty: intermediate
language: assembly
hardware:
- CPU
- KERNAL
related:
- kernal-routines
- memory-map
scraped_at: '2026-08-17'
last_modified: Fri, 13 Feb 2015 23:00:00 GMT
---

# Commodore 64 serial bus functions

| **Address** | Function | 
|---|---|
| $ED09 | Send TALK command   to serial bus. Input: A = Device number. Output: – Used registers: A. | 
| $ED0C | Send LISTEN command to serial bus. Input: A = Device number. Output: – Used registers: A. | 
| $ED40 | Flush serial bus output cache, at memory   address $0095, to serial bus. Input: – Output: – Used registers: A. | 
| $EDB9 | Send LISTEN secondary address to serial   bus. Input: A = Secondary address. Output: – Used registers: A. | 
| $EDC7 | Send TALK secondary address to serial   bus. Input: A = Secondary address. Output: – Used registers: A. | 
| $EDDD | Write byte to serial bus. Input: A = Byte to write. Output: – Used registers: – | 
| $EDEF | Send UNTALK command to serial bus. Input: – Output: – Used registers: A. | 
| $EDFE | Send UNLISTEN command to serial bus. Input: – Output: – Used registers: A. | 
| $EE13 | Read byte from serial bus. Input: – Output: A = Byte read. Used registers: A. | 
| $EE85 | Set CLOCK OUT to high. Input: – Output: – Used registers: A. | 
| $EE8E | Set CLOCK OUT to low. Input: – Output: – Used registers: A. | 
| $EE97 | Set DATA OUT to high. Input: – Output: – Used registers: A. | 
| $EEA0 | Set DATA OUT to low. Input: – Output: – Used registers: A. | 
| $EEA9 | Read CLOCK IN and DATA IN. Input: – Output: Carry = DATA IN; Negative = CLOCK IN; A = CLOCK IN (in bit #7). Used registers: A. | 
| $F1AD | Read byte from serial bus; read $0D,   Return, if device status != 0. Input: – Output: A = Byte read. Used registers: A. | 
| $F237 | Define serial bus as standard input; do   not send TALK secondary address if secondary address bit #7 = 1. Input: A = Device number. Output: – Used registers: A, X. | 
| $F279 | Define serial bus as standard output; do   not send LISTEN secondary address if secondary address bit #7 = 1. Input: A = Device number. Output: – Used registers: A, X. | 
| $F3D5 | Open file on serial bus; do not send file   name if secondary address bit #7 = 1 or file name length = 0. Input: – Output: – Used registers: A, Y. | 
| $F528 | Send UNTALK and CLOSE command to serial   bus. Input: – Output: – Used registers: A. | 
| $F63F | Send UNLISTEN and CLOSE command to serial   bus. Input: – Output: – Used registers: A. | 
| $F642 | Close file on serial bus; do not send   CLOSE secondary address if secondary address bit #7 = 1. Input: – Output: – Used registers: – | 
| $FE21 | Unknown. (Set serial bus timeout.) Input: A = Timeout value. Output: – Used registers: – | 
| **Standard KERNAL functions** |  | 
| $FF93 | LSTNSA. Send LISTEN secondary address to   serial bus. (Must call LISTEN beforehands.) Input: A = Secondary address. Output: – Used registers: A. Real address: $EDB9. | 
| $FF96 | TALKSA. Send TALK secondary address to   serial bus. (Must call TALK beforehands.) Input: A = Secondary address. Output: – Used registers: A. Real address: $EDC7. | 
| $FFA2 | SETTMO. Unknown. (Set serial bus   timeout.) Input: A = Timeout value. Output: – Used registers: – Real address: $FE21. | 
| $FFA5 | IECIN. Read byte from serial bus. (  Must call TALK and TALKSA beforehands.) Input: – Output: A = Byte read. Used registers: A. Real address: $EE13. | 
| $FFA8 | IECOUT. Write byte to serial bus. (Must   call LISTEN and LSTNSA beforehands.) Input: A = Byte to write. Output: – Used registers: – Real address: $EDDD. | 
| $FFAB | UNTALK. Send UNTALK command to serial   bus. Input: – Output: – Used registers: A. Real address: $EDEF. | 
| $FFAE | UNLSTN. Send UNLISTEN command to serial   bus. Input: – Output: – Used registers: A. Real address: $EDFE. | 
| $FFB1 | LISTEN. Send LISTEN command to serial   bus. Input: A = Device number. Output: – Used registers: A. Real address: $ED0C. | 
| $FFB1 | TALK. Send TALK command to serial bus. Input: A = Device number. Output: – Used registers: A. Real address: $ED09. |

---
*Fonte originale: [https://sta.c64.org/cbm64serfunc.html](https://sta.c64.org/cbm64serfunc.html)*

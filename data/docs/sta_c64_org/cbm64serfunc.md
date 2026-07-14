---
title: Commodore 64 serial bus functions
source_url: https://sta.c64.org/cbm64serfunc.html
category: reference
topics:
- assembly
difficulty: intermediate
language: assembly
hardware:
- KERNAL
related:
- memory-map
- kernal-routines
scraped_at: '2026-07-14'
last_modified: Fri, 13 Feb 2015 23:00:00 GMT
---

# Commodore 64 serial bus functions

| Address | Function | 
|---|---|
| $ED09 | Send TALK command
  to serial bus. | 
| $ED0C | Send LISTEN command to serial bus. | 
| $ED40 | Flush serial bus output cache, at memory
  address $0095, to serial bus. | 
| $EDB9 | Send LISTEN secondary address to serial
  bus. | 
| $EDC7 | Send TALK secondary address to serial
  bus. | 
| $EDDD | Write byte to serial bus. | 
| $EDEF | Send UNTALK command to serial bus. | 
| $EDFE | Send UNLISTEN command to serial bus. | 
| $EE13 | Read byte from serial bus. | 
| $EE85 | Set CLOCK OUT to high. | 
| $EE8E | Set CLOCK OUT to low. | 
| $EE97 | Set DATA OUT to high. | 
| $EEA0 | Set DATA OUT to low. | 
| $EEA9 | Read CLOCK IN and DATA IN. | 
| $F1AD | Read byte from serial bus; read $0D,
  Return, if device status != 0. | 
| $F237 | Define serial bus as standard input; do
  not send TALK secondary address if secondary address bit #7 = 1. | 
| $F279 | Define serial bus as standard output; do
  not send LISTEN secondary address if secondary address bit #7 = 1. | 
| $F3D5 | Open file on serial bus; do not send file
  name if secondary address bit #7 = 1 or file name length = 0. | 
| $F528 | Send UNTALK and CLOSE command to serial
  bus. | 
| $F63F | Send UNLISTEN and CLOSE command to serial
  bus. | 
| $F642 | Close file on serial bus; do not send
  CLOSE secondary address if secondary address bit #7 = 1. | 
| $FE21 | Unknown. (Set serial bus timeout.) | 
| Standard KERNAL functions | |
| $FF93 | LSTNSA. Send LISTEN secondary address to
  serial bus. (Must call LISTEN beforehands.) | 
| $FF96 | TALKSA. Send TALK secondary address to
  serial bus. (Must call TALK beforehands.) | 
| $FFA2 | SETTMO. Unknown. (Set serial bus
  timeout.) | 
| $FFA5 | IECIN. Read byte from serial bus. (
 Must call TALK and TALKSA beforehands.) | 
| $FFA8 | IECOUT. Write byte to serial bus. (Must
  call LISTEN and LSTNSA beforehands.) | 
| $FFAB | UNTALK. Send UNTALK command to serial
  bus. | 
| $FFAE | UNLSTN. Send UNLISTEN command to serial
  bus. | 
| $FFB1 | LISTEN. Send LISTEN command to serial
  bus. | 
| $FFB1 | TALK. Send TALK command to serial bus. |

---
*Fonte originale: [https://sta.c64.org/cbm64serfunc.html](https://sta.c64.org/cbm64serfunc.html)*

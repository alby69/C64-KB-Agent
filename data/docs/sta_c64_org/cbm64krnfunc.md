---
title: Commodore 64 standard KERNAL functions
source_url: https://sta.c64.org/cbm64krnfunc.html
category: reference
topics:
- basic
- memory management
- graphics
- assembly
difficulty: advanced
language: mixed
hardware:
- SID
- CIA
- KERNAL
related:
- keyboard-handling
- sid-registers
- sound-programming
- music-player
- kernal-routines
- memory-map
- joystick-reading
- cia-registers
scraped_at: '2026-07-14'
last_modified: Wed, 13 Nov 2024 00:00:00 GMT
---


# Commodore 64 standard KERNAL functions

| Address | Function | 
|---|---|
| $FF81 | SCINIT. Initialize
  VIC; restore default input/output to keyboard/screen; clear screen; set
  PAL/NTSC switch and interrupt timer. | 
| $FF84 | IOINIT. Initialize CIA's, SID volume;
  setup memory configuration; set and start interrupt timer. | 
| $FF87 | RAMTAS. Clear memory addresses $0002-$0101
  and $0200-$03FF; run memory test and set start and end address of BASIC work
  area accordingly; set screen memory to $0400 and datasette buffer to
  $033C. | 
| $FF8A | RESTOR. Fill vector table at memory
  addresses $0314-$0333 with default values. | 
| $FF8D | VECTOR. Copy vector table at memory
  addresses $0314-$0333 from or into user table. | 
| $FF90 | SETMSG. Set system error display switch at
  memory address $009D. | 
| $FF93 | LSTNSA. Send LISTEN secondary address to
  serial bus. (Must call LISTEN beforehands.) | 
| $FF96 | TALKSA. Send TALK secondary address to
  serial bus. (Must call TALK beforehands.) | 
| $FF99 | MEMTOP. Save or restore end address of
  BASIC work area. | 
| $FF9C | MEMBOT. Save or restore start address of
  BASIC work area. | 
| $FF9F | SCNKEY. Query keyboard; put current matrix
  code into memory address $00CB, current status of shift keys into memory
  address $028D and PETSCII code into keyboard buffer. | 
| $FFA2 | SETTMO. Unknown. (Set serial bus
  timeout.) | 
| $FFA5 | IECIN. Read byte from serial bus. (Must
  call TALK and TALKSA beforehands.) | 
| $FFA8 | IECOUT. Write byte to serial bus. (Must
  call LISTEN and LSTNSA beforehands.) | 
| $FFAB | UNTALK. Send UNTALK command to serial
  bus. | 
| $FFAE | UNLSTN. Send UNLISTEN command to serial
  bus. | 
| $FFB1 | LISTEN. Send LISTEN command to serial
  bus. | 
| $FFB4 | TALK. Send TALK command to serial bus. | 
| $FFB7 | READST. Fetch status of current
  input/output device, value of ST variable. (For RS232, status is
  cleared.) | 
| $FFBA | SETLFS. Set file parameters. | 
| $FFBD | SETNAM. Set file name parameters. | 
| $FFC0 | OPEN. Open file. (Must call SETLFS and
  SETNAM beforehands.) | 
| $FFC3 | CLOSE. Close file. | 
| $FFC6 | CHKIN. Define file as default input. (Must
  call OPEN beforehands.) | 
| $FFC9 | CHKOUT. Define file as default output.
  (Must call OPEN beforehands.) | 
| $FFCC | CLRCHN. Close default input/output files
  (for serial bus, send UNTALK and/or UNLISTEN); restore default input/output
  to keyboard/screen. | 
| $FFCF | CHRIN. Read byte from default input (for
  keyboard, read a line from the screen). (If not keyboard, must call OPEN and
  CHKIN beforehands.) | 
| $FFD2 | CHROUT. Write byte to default output. (If
  not screen, must call OPEN and CHKOUT beforehands.) | 
| $FFD5 | LOAD. Load or verify file. (Must call
  SETLFS and SETNAM beforehands.) | 
| $FFD8 | SAVE. Save file. (Must call SETLFS and
  SETNAM beforehands.) | 
| $FFDB | SETTIM. Set Time of Day, at memory address
  $00A0-$00A2. | 
| $FFDE | RDTIM. read Time of Day, at memory address
  $00A0-$00A2. | 
| $FFE1 | STOP. Query Stop key indicator, at memory
  address $0091; if pressed, call CLRCHN and clear keyboard buffer. | 
| $FFE4 | GETIN. Read byte from default input. (If
  not keyboard, must call OPEN and CHKIN beforehands.) | 
| $FFE7 | CLALL. Clear file table; call CLRCHN. | 
| $FFEA | UDTIM. Update Time of Day, at memory
  address $00A0-$00A2, and Stop key indicator, at memory address $0091. | 
| $FFED | SCREEN. Fetch number of screen rows and
  columns. | 
| $FFF0 | PLOT. Save or restore cursor position. | 
| $FFF3 | IOBASE. Fetch CIA #1 base address. |

---
*Fonte originale: [https://sta.c64.org/cbm64krnfunc.html](https://sta.c64.org/cbm64krnfunc.html)*


### Collegamenti e Riferimenti Hardware
- **$FFD2 (CHROUT (Output Character))**: Associato al chip KERNAL. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#ffd2).
- **$FFE4 (GETIN (Get Character))**: Associato al chip KERNAL. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#ffe4).
- **$0314 (IRQ Vector)**: Associato al chip KERNAL. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#0314).

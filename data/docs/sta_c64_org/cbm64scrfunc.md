---
title: Commodore 64 screen functions
source_url: https://sta.c64.org/cbm64scrfunc.html
category: reference
topics:
- sprite programming
- graphics
- assembly
difficulty: intermediate
language: assembly
hardware:
- KERNAL
- CIA
related:
- vic-ii-registers
- cia-registers
- joystick-reading
- memory-map
- raster-interrupts
- keyboard-handling
- sprite-programming
- kernal-routines
scraped_at: '2026-07-20'
last_modified: Thu, 16 Jun 2016 22:00:00 GMT
---

# Commodore 64 screen functions

| Address | Function | 
|---|---|
| $E4DA | Put current color,
  at memory address $0286, into color RAM, pointed at by memory addresses
  $00F3-$00F4. | 
| $E505 | Fetch number of screen rows and
  columns. | 
| $E50A | Save or restore cursor position. | 
| $E518 | Initialize VIC; restore default
  input/output to keyboard/screen; clear screen. | 
| $E544 | Clear screen. | 
| $E566 | Move cursor home, to upper left corner of
  screen. | 
| $E56C | Set pointer at memory addresses
  $00D1-$00D2 to current line in screen memory and pointer at memory addresses
  $00F3-$00F4 to current line in Color RAM, according to current cursor row,
  at memory address $00D6, and column, at memory address $00D3. | 
| $E59A | Initialize VIC; restore default
  input/output to keyboard/screen; move cursor home. | 
| $E5A0 | Initialize VIC; restore default
  input/output to keyboard/screen. | 
| $E5A8 | Initialize VIC. | 
| $E632 | Read byte from screen; if input line is
  empty, the cursor appears and a line of data is input. | 
| $E684 | Check PETSCII code; if $22, quotation
  mark, then toggle quotation mode switch, at memory address $00D4. | 
| $E6B6 | Recompute the high bytes of pointers to
  lines in screen memory, at memory addresses $00D9-$00F1. | 
| $E716 | Write byte to screen. | 
| $E8CB | Check PETSCII code; if belongs to a color,
  set current color, at memory address $0286. | 
| $E8EA | Scroll complete screen upwards. | 
| $E965 | Insert line before current line and scroll
  lower part of screen downwards. | 
| $E9F0 | Set pointer at memory addresses
  $00D1-$00D2 to current line in screen memory, fetching high byte from table
  at memory addresses $00D9-$00F1. | 
| $E9FF | Clear screen line. | 
| $EA13 | Write character and color onto screen; 
 set cursor phase delay to 2. | 
| $EA24 | Set pointer at memory addresses
  $00F3-$00F4 to current line in Color RAM, according to pointer at memory
  addresses $00D1-$00D2 to current line in screen memory. | 
| Standard KERNAL functions | |
| $FFED | SCREEN. Fetch number of screen rows and
  columns. | 
| $FFF0 | PLOT. Save or restore cursor position. |

---
*Fonte originale: [https://sta.c64.org/cbm64scrfunc.html](https://sta.c64.org/cbm64scrfunc.html)*

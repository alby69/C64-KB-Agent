---
title: Commodore 64 screen functions
source_url: https://sta.c64.org/cbm64scrfunc.html
category: reference
topics:
- assembly
- graphics
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
last_modified: Thu, 16 Jun 2016 22:00:00 GMT
---

# Commodore 64 screen functions

| **Address** | Function | 
|---|---|
| $E4DA | Put current color,   at memory address $0286, into color RAM, pointed at by memory addresses   $00F3-$00F4. Input: Y = Column number. Output: – Used registers: A. | 
| $E505 | Fetch number of screen rows and   columns. Input: – Output: X = Number of columns (40); Y = Number of rows (25). Used registers: X, Y. | 
| $E50A | Save or restore cursor position. Input: Carry: 0 = Restore from input, 1 = Save to output; X = Cursor row   (if Carry = 0); Y = Cursor column (if Carry = 0). Output: X = Cursor row (if Carry = 1); Y = Cursor column (if Carry = 1). Used registers: X, Y. | 
| $E518 | Initialize VIC; restore default   input/output to keyboard/screen; clear screen. Input: – Output: – Used registers: A, X, Y. | 
| $E544 | Clear screen. Input: – Output: – Used registers: A, X, Y. | 
| $E566 | Move cursor home, to upper left corner of   screen. Input: – Output: – Used registers: A, X, Y. | 
| $E56C | Set pointer at memory addresses   $00D1-$00D2 to current line in screen memory and pointer at memory addresses   $00F3-$00F4 to current line in Color RAM, according to current cursor row,   at memory address $00D6, and column, at memory address $00D3. Input: – Output: – Used registers: A, X, Y. | 
| $E59A | Initialize VIC; restore default   input/output to keyboard/screen; move cursor home. Input: – Output: – Used registers: A, X, Y. | 
| $E5A0 | Initialize VIC; restore default   input/output to keyboard/screen. Input: – Output: – Used registers: A, X. | 
| $E5A8 | Initialize VIC. Input: – Output: – Used registers: A, X. | 
| $E632 | Read byte from screen; if input line is   empty, the cursor appears and a line of data is input. Input: – Output: A = Byte read. Used registers: A. | 
| $E684 | Check PETSCII code; if $22, quotation   mark, then toggle quotation mode switch, at memory address $00D4. Input: – Output: – Used registers: – | 
| $E6B6 | Recompute the high bytes of pointers to   lines in screen memory, at memory addresses $00D9-$00F1. Input: – Output: – Used registers: A, X, Y. | 
| $E716 | Write byte to screen. Input: A = Byte to write. Output: – Used registers: – | 
| $E8CB | Check PETSCII code; if belongs to a color,   set current color, at memory address $0286. Input: – Output: – Used registers: A, X. | 
| $E8EA | Scroll complete screen upwards. Input: – Output: – Used registers: A, X, Y. | 
| $E965 | Insert line before current line and scroll   lower part of screen downwards. Input: – Output: – Used registers: A, X, Y. | 
| $E9F0 | Set pointer at memory addresses   $00D1-$00D2 to current line in screen memory, fetching high byte from table   at memory addresses $00D9-$00F1. Input: X = Row number. Output: – Used registers: A. | 
| $E9FF | Clear screen line. Input: X = Row number. Output: – Used registers: A, Y. | 
| $EA13 | Write character and color onto screen;   set cursor phase delay to 2. Input: A = Character to write; X = Color to write. Output: – Used registers: A, Y. | 
| $EA24 | Set pointer at memory addresses   $00F3-$00F4 to current line in Color RAM, according to pointer at memory   addresses $00D1-$00D2 to current line in screen memory. Input: – Output: – Used registers: – | 
| **Standard KERNAL functions** |  | 
| $FFED | SCREEN. Fetch number of screen rows and   columns. Input: – Output: X = Number of columns (40); Y = Number of rows (25). Used registers: X, Y. Real address: $E505. | 
| $FFF0 | PLOT. Save or restore cursor position. Input: Carry: 0 = Restore from input, 1 = Save to output; X = Cursor column   (if Carry = 0); Y = Cursor row (if Carry = 0). Output: X = Cursor column (if Carry = 1); Y = Cursor row (if Carry = 1). Used registers: X, Y. Real address: $E50A. |

---
*Fonte originale: [https://sta.c64.org/cbm64scrfunc.html](https://sta.c64.org/cbm64scrfunc.html)*

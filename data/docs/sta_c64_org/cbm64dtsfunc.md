---
title: Commodore 64 datasette functions
source_url: https://sta.c64.org/cbm64dtsfunc.html
category: reference
topics:
- sprite programming
- assembly
difficulty: advanced
language: assembly
hardware:
- KERNAL
- CPU
related:
- vic-ii-registers
- memory-map
- raster-interrupts
- kernal-routines
- sprite-programming
scraped_at: '2026-07-20'
last_modified: Fri, 13 Feb 2015 23:00:00 GMT
---

# Commodore 64 datasette functions

| **Address** | Function | 
|---|
| $F179 | Read byte from
  datasette (data files only).Input: –
 Output: A = Byte read.
 Used registers: A, Y.
 | 
| $F1DD | Write byte to datasette.Input: Carry = 1; A = Byte to write; 0 = End of file.
 Output: –
 Used registers: –
 | 
| $F22A | Define datasette as default input.Input: A = 1.
 Output: –
 Used registers: A, X.
 | 
| $F26F | Define datasette as default output.Input: A = 1.
 Output: –
 Used registers: A, X.
 | 
| $F2C8 | Close file on datasette (data file only);
  write $00, end of file first. (Must push logical number into stack
  beforehands.)Input: –
 Output: –
 Used registers: A, X, Y.
 | 
| $F38B | Open file on datasette (data file only);
  display "ILLEGAL DEVICE NUMBER" error code if datasette buffer pointer, at
  memory addresses $00B2-$00B3, is below $0200.Input: –
 Output: –
 Used registers: A, X, Y.
 | 
| $F72C | Read header from datasette.Input: –
 Output: X = Header type; Carry = 1 and Zero = 1: Interrupted by Stop key
  having been pressed; Carry = 1 and Zero = 0: Interrupted by having reached
  end of tape.
 Used registers: A, X, Y.
 | 
| $F76A | Generate and write header to
  datasette.Input: A = Header type.
 Output: Carry = 1 and Zero = 1: Interrupted by Stop key having been
  pressed.
 Used registers: A, X, Y.
 | 
| $F7D0 | Fetch pointer to datasette buffer.Input: –
 Output: Carry = 0: Pointer below $0200; X/Y = Pointer.
 Used registers: X, Y.
 | 
| $F7EA | Find file on datasette. (Must call SETLFS
  and SETNAM beforehands.)Input: –
 Output: X = Header type; Carry = 1 and Zero = 1: Interrupted by Stop key
  having been pressed; Carry = 1 and Zero = 0: Interrupted by having reached
  end of tape
 Used registers: A, X, Y.
 | 
| $F80D | Increase datasette buffer pointer.Input: –
 Output: Zero = 1: Buffer is full; Carry = 1 and Zero = 0: Buffer overflow
  occurred.
 Used registers: X, Y.
 | 
| $F817 | Wait for the PLAY button to be pressed on
  datasette.Input: –
 Output: Carry = 1: Interrupted by Stop key having been pressed.
 Used registers: A, Y.
 | 
| $F82E | Detect button presses on datasette.Input: –
 Output: Zero: 0 = No button is pressed, 1 = One or more of PLAY, RECORD,
    F.FWD or REW pressed.
 Used registers: –
 | 
| $F838 | Wait for the RECORD button to be pressed
  on datasette.Input: –
 Output: Carry = 1: Interrupted by Stop key having been pressed.
 Used registers: A, Y.
 | 
| $F841 | Read block from datasette.Input: –
 Output: Carry = 1 and Zero = 1: Interrupted by Stop key having been
  pressed.
 Used registers: A, X, Y.
 | 
| $F84A | Read program file from datasette.Input: –
 Output: Carry = 1 and Zero = 1: Interrupted by Stop key having been
  pressed.
 Used registers: A, X, Y.
 | 
| $F864 | Write block to datasette.Input: –
 Output: Carry = 1 and Zero = 1: Interrupted by Stop key having been
  pressed.
 Used registers: A, X, Y.
 | 
| $F86B | Write program file to datasette.Input: –
 Output: Carry = 1 and Zero = 1: Interrupted by Stop key having been
  pressed.
 Used registers: A, X, Y.
 | 
| $FC93 | Switch off datasette motor; switch screen
  back; restore execution address of interrupt service routine from memory
  addresses $029F-$02A0.Input: –
 Output: –
 Used registers: A.
 | 
| $FCCA | Switch off datasette motor.Input: –
 Output: –
 Used registers: A.
 |

---
*Fonte originale: [https://sta.c64.org/cbm64dtsfunc.html](https://sta.c64.org/cbm64dtsfunc.html)*

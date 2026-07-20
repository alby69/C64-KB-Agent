---
title: Datasette
source_url: https://codebase.c64.org/doku.php?id=base%3Adatasette
category: reference
topics:
- basic
difficulty: intermediate
language: none
hardware:
- KERNAL
- CIA
related:
- keyboard-handling
- memory-map
- joystick-reading
- kernal-routines
- cia-registers
scraped_at: '2026-07-20'
---

# Datasette

base:datasette

                # Datasette

The datasette is accessed via $01 (right, it's directly connected to CPU)

You have 3 lines = 3 bits in $01:


bit 5  is Cassette Motor Control (NOTE! It's low-active: 0 = on; 1 = off)

bit 4  is Cassette Switch Sense: 1 = Switch Closed

bit 3  is Cassette Data Output Line


Make sure you don't mess up $00!

Since bit 4 is input and bit 3 obviously output.

Default for $00 on C64 is %00101111 ($2f)


And in case you wondered: you READ from tape via the FLAG-line in CIA1:

bit 4 in $dc0d.


In BASIC $c0 (dec.192) is a tape motor control too…


/enthusi

base/datasette.txt · Last modified:  by 127.0.0.1

---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Adatasette](https://codebase.c64.org/doku.php?id=base%3Adatasette)*

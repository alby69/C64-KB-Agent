---
title: CIA (6526) Programming
source_url: https://codebase.c64.org/doku.php?id=base%3Acia
category: reference
topics:
- input handling
- raster interrupts
- memory management
difficulty: advanced
language: none
hardware:
- VIC-II
- CIA
related:
- sprite-programming
- keyboard-handling
- cia-registers
- raster-interrupts
- vic-ii-registers
- joystick-reading
scraped_at: '2026-07-14'
---

# CIA (6526) Programming

base:cia

                ### Table of Contents

# CIA (6526) Programming

A lot of stuff is controlled by the CIA chips, such as keyboard/joystick reading, serial IO, timer interrupts, VIC bank switching and… You name it!

## Interrupts

There are many kinds of interrupts on the C64. The CIA generates Timer interrupts, which can be set to be trigged at specific timed intervals. Other kinds of interrupts, such as raster interrupts are trigged by the VIC chip. Information on interrupts in general is collected in one place:

## Keyboard/joystick and serial IO

See the IO page for this.

## Time-of-Day Clock aka TOD

- [Initialize TOD Clock on all platforms](https://codebase.c64.org/doku.php?id=cia:initialize_tod_clock_on_all_platforms)- by Devia
- [Efficient TOD initialisation](https://codebase.c64.org/doku.php?id=cia:efficient_tod_initialisation)- by Silver Dream !/W.F.M.H.
- [TOD calibration](https://codebase.c64.org/doku.php?id=cia:tod_calibration)- by Soci / Singular

base/cia.txt · Last modified:  by 127.0.0.1

---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Acia](https://codebase.c64.org/doku.php?id=base%3Acia)*

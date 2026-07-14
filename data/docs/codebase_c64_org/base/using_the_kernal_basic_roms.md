---
title: KERNAL and BASIC ROMs
source_url: https://codebase.c64.org/doku.php?id=base%3Ausing_the_kernal_basic_roms
category: reference
topics:
- memory management
- basic
difficulty: intermediate
language: basic
hardware:
- SID
- KERNAL
- CIA
- BASIC ROM
related:
- keyboard-handling
- sound-programming
- cia-registers
- memory-map
- sid-registers
- music-player
- kernal-routines
- joystick-reading
scraped_at: '2026-07-14'
---

# KERNAL and BASIC ROMs

base:using_the_kernal_basic_roms

                ### Table of Contents

# KERNAL and BASIC ROMs

About using the “system” of the C64. This system is located in the Kernal ROM and the Basic ROM.

## Memory configuration

The KERNAL and BASIC ROMs (and the IO area, used to access the VIC and the SID) can be switched in and out, depending on whether you want to access the ROM chips, or the RAM “behind” the ROM chips. To see how to do this switching, consult the memory configuration section.

## Reference material

- [Kernal Reference](https://codebase.c64.org/doku.php?id=base:kernalreference)- created by unknown
- [Asm include file for BASIC routines](https://codebase.c64.org/doku.php?id=base:asm_include_file_for_basic_routines)- briefly documents each call - by White Flame

## File IO with the KERNAL

More information on diskdrive/tape etc programming is available in the [IO programming section](https://codebase.c64.org/doku.php?id=cia:io_programming) of this site.

- [DOS examples](https://codebase.c64.org/doku.php?id=base:dos_examples)- a few sourcecodes on how to use DOS/KERNAL calls, by Graham

## KERNAL/BASIC tweaking

- [Sample wedge - Adding four new BASIC commands](https://codebase.c64.org/doku.php?id=base:basicwedge)- Scott Julian
- [Modify keyboard decoding](https://codebase.c64.org/doku.php?id=base:modify_keyboard_decoding)- Wil

## KERNAL/BASIC initialisation

base/using_the_kernal_basic_roms.txt · Last modified:  by 127.0.0.1

---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Ausing_the_kernal_basic_roms](https://codebase.c64.org/doku.php?id=base%3Ausing_the_kernal_basic_roms)*

---
id: using-the-kernal-basic-roms
type: entity
title: KERNAL and BASIC ROMs
aliases:
- KERNAL and BASIC ROMs
tags:
- memory management
- basic
sources:
- path: data/docs/codebase_c64_org/base/using_the_kernal_basic_roms.md
  sha256: b4710666fa1220df3ea4fc4d7b8d1edd4dd463f59e45c370fc02399112794d0d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-using-the-kernal-basic-roms
---

# KERNAL and BASIC ROMs



# KERNAL and BASIC ROMs

base:using_the_kernal_basic_roms

                ### Table of Contents

# KERNAL and BASIC ROMs

About using the “system” of the C64. This system is located in the Kernal ROM and the Basic ROM.

## Memory configuration

The KERNAL and BASIC ROMs (and the IO area, used to access the VIC and the SID) can be switched in and out, depending on whether you want to access the ROM chips, or the RAM “behind” the ROM chips. To see how to do this switching, consult the memory configuration section.

## Reference material

- [Kernal Reference](https://codebase.c64.org/doku.php?id=base:kernalreference) - created by unknown
- [Asm include file for BASIC routines](https://codebase.c64.org/doku.php?id=base:asm_include_file_for_basic_routines) - briefly documents each call - by White Flame

## File IO with the KERNAL

More information on diskdrive/tape etc programming is available in the [IO programming section](https://codebase.c64.org/doku.php?id=cia:io_programming) of this site.

- [DOS examples](https://codebase.c64.org/doku.php?id=base:dos_examples) - a few sourcecodes on how to use DOS/KERNAL calls, by Graham

## KERNAL/BASIC tweaking

- [Sample wedge - Adding four new BASIC commands](https://codebase.c64.org/doku.php?id=base:basicwedge) - Scott Julian
- [Modify keyboard decoding](https://codebase.c64.org/doku.php?id=base:modify_keyboard_decoding) - Wil

## KERNAL/BASIC initialisation

base/using_the_kernal_basic_roms.txt · Last modified:  by cz

---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Ausing_the_kernal_basic_roms](https://codebase.c64.org/doku.php?id=base%3Ausing_the_kernal_basic_roms)*


## References
- Source: [[src-using-the-kernal-basic-roms]]

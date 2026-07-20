---
title: High level KERNAL examples
source_url: https://codebase.c64.org/doku.php?id=base%3Ados_examples
category: reference
topics:
- basic
difficulty: advanced
language: none
hardware:
- BASIC ROM
- KERNAL
related:
- memory-map
- kernal-routines
scraped_at: '2026-07-20'
---

# High level KERNAL examples

base:dos_examples

                # High level KERNAL examples

Be aware that some of these KERNAL routines call SEI and CLI, so if you have interrupts running in your program, be sure to disable your interrupts properly (i.e. do not only do SEI) before calling these routines in case you don't want the interrupts to be re-enabled by the KERNAL code. Also note that BASIC ROM can be disabled when doing disk IO (except for the DIR routine here, which calls one of the BASIC routines, but that is not for the disk IO itself, but just for printing the output to the screen).

base/dos_examples.txt · Last modified:  by 127.0.0.1

---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Ados_examples](https://codebase.c64.org/doku.php?id=base%3Ados_examples)*

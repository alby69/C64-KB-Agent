---
title: Preparation F13E/F1F5-F14D/F204
source_url: https://github.com/mist64/c64ref/blob/main/src/kernal/compute!'s_tool_kit:_kernal.txt
category: reference
topics:
- kernal-api
- system-routines
- jumps
difficulty: intermediate
language: assembly
hardware:
- C64
related:
- chrin
- clc
- f13e-getin
- jmp
scraped_at: '2026-07-29'
c64ref:
  module: kernal
  source_files:
  - compute!'s_tool_kit:_kernal.txt
  address: $F13E
  symbol: GETIN
  sources:
  - name: 'COMPUTE!''s Tool Kit: Kernal'
    author: Dan Heeb
    description: 'ed by**: Indirect JMP through (032A) from Kernal GETIN vector at'
---

# GETIN — Preparation F13E/F1F5-F14D/F204 ($F13E)

## Panoramica
La routine KERNAL `GETIN` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$F13E`
- **Chiamata**: `JSR GETIN` o `SYS 61758`


## Note per Fonte

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: Indirect JMP through (032A) from Kernal GETIN vector at
FFE4.

outine first determines if the current input device is
yboard. If not, GETIN falls through to F14E/F205 for an
 device or branches to F166/F21D for other devices
the same routines as are used by CHRIN.

 current input device is the keyboard and if the key-
buffer contains characters, JMP E5B4/E5CF to retrieve
rst character from the keyboard buffer.

ation**:

99, the current input device, is not 0 (the keyboard),
nch to step 5.
99 is 0 for the keyboard, see if any characters are in the
board buffer as indicated by C6, the number of charac-
s in the keyboard buffer.
no characters are in the keyboard buffer, just CLC and
, thus returning with the accumulator set to 0.
characters do exist in the keyboard buffer, disable IRQ
errupts and JMP E5B4/E5CF to retrieve the first character
m the keyboard buffer and exit.
the current input device, 99, is 2 for RS-232, fall through
F14E/F205 for the routine to get characters from RS-232.
the current input device is neither 0 nor 2, branch to
6/F21D to get a character from other devices. F166/F21D
located in the Determine Input Device routine used by
IN; thus, other devices (tape, screen, serial) perform
 same routines for both GETIN and CHRIN.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
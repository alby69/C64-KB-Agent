---
title: Execution FE25/FE73-FE33/FE81
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
- jmp
- jsr
- memtop
scraped_at: '2026-07-29'
c64ref:
  module: kernal
  source_files:
  - compute!'s_tool_kit:_kernal.txt
  address: $FE25
  symbol: MEMTOP
  sources:
  - name: 'COMPUTE!''s Tool Kit: Kernal'
    author: Dan Heeb
    description: 'ed by**: JMP from Kernal MEMTOP vector at FF99; alternate entry
      at'
---

# MEMTOP — Execution FE25/FE73-FE33/FE81 ($FE25)

## Panoramica
La routine KERNAL `MEMTOP` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FE25`
- **Chiamata**: `JSR MEMTOP` o `SYS 65061`


## Note per Fonte

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: JMP from Kernal MEMTOP vector at FF99; alternate entry at
E75 by JSR at F2B2/F377 in Close Logical File for RS-
SR at F468/F527 in Open RS-232 Device; alternate entry
D/FE7B by JMP at F480/F53F in Open RS-232 Device,
 FDCF in Initialize Memory Pointers (VIC only).

ering at FE25/FE73, the carry flag determines
r the top of memory is being set or read. If the carry
 clear, or if the routine is entered at FE2D/FE7B, the top
ory pointer (0283) is set from the X and Y register val-
f the carry is set, or if the routine is entered at
E75, the X and Y registers are set from the top of
 pointer (0283).

ation**:

5/FE73: If carry is set, branch to step 3.
7/FE75: Load X and Y registers from pointer to top of
ory (0283), and fall through to step 3.
D/FE7B: Set (0283) from values in X and Y registers.
.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
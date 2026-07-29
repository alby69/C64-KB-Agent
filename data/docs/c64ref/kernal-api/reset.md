---
title: to No Open Files F32F/F3EF-F332/F3F2
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
- clall
- jmp
scraped_at: '2026-07-29'
c64ref:
  module: kernal
  source_files:
  - compute!'s_tool_kit:_kernal.txt
  address: $F32F
  symbol: Reset
  sources:
  - name: 'COMPUTE!''s Tool Kit: Kernal'
    author: Dan Heeb
    description: 'ed by**: Indirect JMP through (032C) from Kernal CLALL vector at'
---

# Reset — to No Open Files F32F/F3EF-F332/F3F2 ($F32F)

## Panoramica
La routine KERNAL `Reset` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$F32F`
- **Chiamata**: `JSR Reset` o `SYS 62255`


## Note per Fonte

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: Indirect JMP through (032C) from Kernal CLALL vector at
FFE7.

location 98, the number of open files, to zero and
hrough to F333/F3F3 to reset any open serial channels
set the default device numbers.

ation**:

 98, the number of open files, to 0.
l through to F333/F3F3, Clear Serial Channels and Reset
ault Devices routine.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
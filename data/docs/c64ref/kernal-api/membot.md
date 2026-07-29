---
title: Execution FE34/FE82-FE42/FE90
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
- membot
scraped_at: '2026-07-29'
c64ref:
  module: kernal
  source_files:
  - compute!'s_tool_kit:_kernal.txt
  address: $FE34
  symbol: MEMBOT
  sources:
  - name: 'COMPUTE!''s Tool Kit: Kernal'
    author: Dan Heeb
    description: 'ed by**: JMP from Kernal MEMBOT vector at FF9C.'
---

# MEMBOT — Execution FE34/FE82-FE42/FE90 ($FE34)

## Panoramica
La routine KERNAL `MEMBOT` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FE34`
- **Chiamata**: `JSR MEMBOT` o `SYS 65076`


## Note per Fonte

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: JMP from Kernal MEMBOT vector at FF9C.

 carry is clear at entry, set (0281), the pointer to the
 of memory, from the X and Y registers. If carry is set at
 load X and Y registers from (0281).

ation**:

 carry is clear, branch to step 3.
ad X and Y registers from pointer to bottom of memory
281), and fall through to step 3.
t (0281) from values in X and Y registers.
S.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*
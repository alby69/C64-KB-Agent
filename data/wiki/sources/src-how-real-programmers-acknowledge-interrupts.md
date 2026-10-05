---
id: src-how-real-programmers-acknowledge-interrupts
type: source
title: 'Source Summary: How Real Programmers Acknowledge Interrupts'
aliases:
- How Real Programmers Acknowledge Interrupts
- how_real_programmers_acknowledge_interrupts.md
tags:
- raster interrupts
- sound generation
- assembly
sources:
- path: data/docs/codebase_c64_org/base/how_real_programmers_acknowledge_interrupts.md
  sha256: ecd599f816c48dd30995c943b11f6a128c82b0e62024f2b65fb5ab89eb39a4d2
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: How Real Programmers Acknowledge Interrupts

**Raw Source File**: `data/docs/codebase_c64_org/base/how_real_programmers_acknowledge_interrupts.md`
**SHA256**: `ecd599f816c48dd30995c943b11f6a128c82b0e62024f2b65fb5ab89eb39a4d2`

## Summary




# How Real Programmers Acknowledge Interrupts

base:how_real_programmers_acknowledge_interrupts

                ### Table of Contents

# How Real Programmers Acknowledge Interrupts









## With RMW instructions

```
        ; beginning of combined raster/timer interrupt routine
        LSR $D019       ; clear VIC interrupts, read raster interrupt flag to C
        BCS raster      ; jump if VIC caused an interrupt
        ...             ; timer interrupt routine
        Operational diagr...

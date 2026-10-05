---
id: src-delay
type: source
title: 'Source Summary: Delay'
aliases:
- Delay
- delay.md
tags:
- raster interrupts
- assembly
sources:
- path: data/docs/codebase_c64_org/base/delay.md
  sha256: 10021fcf225f92e55c567555715e67b6dc27e28fd2e6d88ac68101183de34a05
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Delay

**Raw Source File**: `data/docs/codebase_c64_org/base/delay.md`
**SHA256**: `10021fcf225f92e55c567555715e67b6dc27e28fd2e6d88ac68101183de34a05`

## Summary



# Delay

base:delay

                # Delay

by Zed Yago

When stabilizing a IRQ, you often need a subroutine or macro which can delay a given amount of cycles.

```
delay:            ;delay 84-accu cycles, 0<=accu<=65
  lsr             ;2 cycles akku=akku/2 carry=1 if accu was odd, 0 otherwise
  bcc waste1cycle ;2/3 cycles, depending on lowest bit, same operation for both
waste1cycle:
  sta smod+1      ;4 cycles selfmodifies the argument of branch
  clc             ;2 cycles 
;now we have bu...

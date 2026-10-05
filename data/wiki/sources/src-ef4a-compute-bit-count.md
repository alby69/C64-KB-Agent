---
id: src-ef4a-compute-bit-count
type: source
title: 'Source Summary: compute bit count'
aliases:
- compute bit count
- ef4a-compute-bit-count.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ef4a-compute-bit-count.md
  sha256: e6d1cdc3571bb0c788b4c821e722cfb26f658a7c5271bb4cdacb5d0c8964c8e5
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: compute bit count

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/ef4a-compute-bit-count.md`
**SHA256**: `e6d1cdc3571bb0c788b4c821e722cfb26f658a7c5271bb4cdacb5d0c8964c8e5`

## Summary



# $EF4A — compute bit count

## Disassemblatura
```assembly
.EF4A  A2 09    LDX #$09   ; set bit count to 9, 8 data + 1 stop bit
.EF4C  A9 20    LDA #$20   ; mask for 8/7 data bits
.EF4E  2C 93 02 BIT $0293   ; test pseudo 6551 control register
.EF51  F0 01    BEQ $EF54   ; branch if 8 bits
.EF53  CA       DEX   ; else decrement count for 7 data bits
.EF54  50 02    BVC $EF58   ; branch if 7 bits
.EF56  CA       DEX   ; else decrement count ..
.EF57  CA       DEX   ; .. for 5 data bits
.EF58  ...

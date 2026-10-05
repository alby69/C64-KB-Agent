---
id: src-b82d-perform-wait
type: source
title: 'Source Summary: perform WAIT'
aliases:
- perform WAIT
- b82d-perform-wait.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b82d-perform-wait.md
  sha256: 9a310ac28e6734b8766705712c515664504642f2febff27c8fdd7c28150b072b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform WAIT

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b82d-perform-wait.md`
**SHA256**: `9a310ac28e6734b8766705712c515664504642f2febff27c8fdd7c28150b072b`

## Summary



# $B82D — perform WAIT

## Disassemblatura
```assembly
.B82D  20 EB B7 JSR $B7EB   ; get parameters for POKE/WAIT
.B830  86 49    STX $49   ; save byte
.B832  A2 00    LDX #$00   ; clear mask
.B834  20 79 00 JSR $0079   ; scan memory
.B837  F0 03    BEQ $B83C   ; skip if no third argument
.B839  20 F1 B7 JSR $B7F1   ; scan for "," and get byte, else syntax error then warm start
.B83C  86 4A    STX $4A   ; save EOR argument
.B83E  A0 00    LDY #$00   ; clear index
.B840  B1 14    LDA ($14),Y   ...

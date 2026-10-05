---
id: src-e37b-basic-warm-start-entry-point
type: source
title: 'Source Summary: BASIC warm start entry point'
aliases:
- BASIC warm start entry point
- e37b-basic-warm-start-entry-point.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e37b-basic-warm-start-entry-point.md
  sha256: a1fec528175c4564242f4b2846e4e42f31ca098c7977ee2562e4040d6f3003d4
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: BASIC warm start entry point

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e37b-basic-warm-start-entry-point.md`
**SHA256**: `a1fec528175c4564242f4b2846e4e42f31ca098c7977ee2562e4040d6f3003d4`

## Summary



# $E37B — BASIC warm start entry point

## Disassemblatura
```assembly
.E37B  20 CC FF JSR $FFCC   ; close input and output channels
.E37E  A9 00    LDA #$00   ; clear A
.E380  85 13    STA $13   ; set current I/O channel, flag default
.E382  20 7A A6 JSR $A67A   ; flush BASIC stack and clear continue pointer
.E385  58       CLI   ; enable the interrupts
.E386  A2 80    LDX #$80   ; set -ve error, just do warm start
.E388  6C 00 03 JMP ($0300)   ; go handle error message, normally $E38B
.E38B ...

---
id: src-a928-perform-if
type: source
title: 'Source Summary: perform IF'
aliases:
- perform IF
- a928-perform-if.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a928-perform-if.md
  sha256: 3c7ebde8c47999f30f7203f257c0c7c7d389ae5555f36947c19c1699ce8f3940
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform IF

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a928-perform-if.md`
**SHA256**: `3c7ebde8c47999f30f7203f257c0c7c7d389ae5555f36947c19c1699ce8f3940`

## Summary



# $A928 — perform IF

## Disassemblatura
```assembly
.A928  20 9E AD JSR $AD9E   ; evaluate expression
.A92B  20 79 00 JSR $0079   ; scan memory
.A92E  C9 89    CMP #$89   ; compare with "GOTO" token
.A930  F0 05    BEQ $A937   ; if it was  the token for GOTO go do IF ... GOTO wasn't IF ... GOTO so must be IF ... THEN
.A932  A9 A7    LDA #$A7   ; set "THEN" token
.A934  20 FF AE JSR $AEFF   ; scan for CHR$(A), else do syntax error then warm start
.A937  A5 61    LDA $61   ; get FAC1 exponent
....

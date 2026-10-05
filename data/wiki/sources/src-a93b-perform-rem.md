---
id: src-a93b-perform-rem
type: source
title: 'Source Summary: perform REM'
aliases:
- perform REM
- a93b-perform-rem.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a93b-perform-rem.md
  sha256: 755dbacc3caa92e5890d1139a0b0ba75923ef3fc74866e0d065de126371c8e7f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform REM

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a93b-perform-rem.md`
**SHA256**: `755dbacc3caa92e5890d1139a0b0ba75923ef3fc74866e0d065de126371c8e7f`

## Summary



# $A93B — perform REM

## Disassemblatura
```assembly
.A93B  20 09 A9 JSR $A909   ; scan for next BASIC line
.A93E  F0 BB    BEQ $A8FB   ; add Y to the BASIC execute pointer and return, branch always result was non zero so do rest of line
.A940  20 79 00 JSR $0079   ; scan memory
.A943  B0 03    BCS $A948   ; branch if not numeric character, is variable or keyword
.A945  4C A0 A8 JMP $A8A0   ; else perform GOTO n is variable or keyword
.A948  4C ED A7 JMP $A7ED   ; interpret BASIC code from BA...

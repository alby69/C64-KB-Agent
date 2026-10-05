---
id: src-a871-perform-run
type: source
title: 'Source Summary: perform RUN'
aliases:
- perform RUN
- a871-perform-run.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a871-perform-run.md
  sha256: 3041925889c77e3d6f3d3efc9ba8c4a86fa0e39d6e7598031c7b0cdbf808487d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform RUN

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a871-perform-run.md`
**SHA256**: `3041925889c77e3d6f3d3efc9ba8c4a86fa0e39d6e7598031c7b0cdbf808487d`

## Summary



# $A871 — perform RUN

## Disassemblatura
```assembly
.A871  08       PHP   ; save status
.A872  A9 00    LDA #$00   ; no control or kernal messages
.A874  20 90 FF JSR $FF90   ; control kernal messages
.A877  28       PLP   ; restore status
.A878  D0 03    BNE $A87D   ; branch if RUN n
.A87A  4C 59 A6 JMP $A659   ; reset execution to start, clear variables, flush stack and return
.A87D  20 60 A6 JSR $A660   ; go do "CLEAR"
.A880  4C 97 A8 JMP $A897   ; get n and do GOTO n
```


## Commenti

#...

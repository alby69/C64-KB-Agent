---
id: src-f5d2-display-loading-or-verifying
type: source
title: 'Source Summary: display "LOADING" or "VERIFYING"'
aliases:
- display "LOADING" or "VERIFYING"
- f5d2-display-loading-or-verifying.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f5d2-display-loading-or-verifying.md
  sha256: a3c28e1837cea0e16dd0070c3834a614684a1fe78fd64d0ef4c78b584362e7ed
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: display "LOADING" or "VERIFYING"

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f5d2-display-loading-or-verifying.md`
**SHA256**: `a3c28e1837cea0e16dd0070c3834a614684a1fe78fd64d0ef4c78b584362e7ed`

## Summary



# $F5D2 — display "LOADING" or "VERIFYING"

## Disassemblatura
```assembly
.F5D2  A0 49    LDY #$49   ; point to "LOADING"
.F5D4  A5 93    LDA $93   ; get load/verify flag
.F5D6  F0 02    BEQ $F5DA   ; branch if load
.F5D8  A0 59    LDY #$59   ; point to "VERIFYING"
.F5DA  4C 2B F1 JMP $F12B   ; display kernel I/O message if in direct mode and return
```


## Commenti

### Original Disassembly (—)
- **$F5D2**: point to "LOADING"
- **$F5D4**: get load/verify flag
- **$F5D6**: branch if load
- *...

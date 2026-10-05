---
id: src-e0f9-handle-basic-io-error
type: source
title: 'Source Summary: handle BASIC I/O error'
aliases:
- handle BASIC I/O error
- e0f9-handle-basic-io-error.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e0f9-handle-basic-io-error.md
  sha256: d5acb56d174ead969a244992e9b8ca8b93f1242d99e5a3d4527d0ef7583b8a8e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: handle BASIC I/O error

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e0f9-handle-basic-io-error.md`
**SHA256**: `d5acb56d174ead969a244992e9b8ca8b93f1242d99e5a3d4527d0ef7583b8a8e`

## Summary



# $E0F9 — handle BASIC I/O error

## Disassemblatura
```assembly
.E0F9  C9 F0    CMP #$F0   ; compare error with $F0
.E0FB  D0 07    BNE $E104   ; branch if not $F0
.E0FD  84 38    STY $38   ; set end of memory high byte
.E0FF  86 37    STX $37   ; set end of memory low byte
.E101  4C 63 A6 JMP $A663   ; clear from start to end and return error was not $F0
.E104  AA       TAX   ; copy error #
.E105  D0 02    BNE $E109   ; branch if not $00
.E107  A2 1E    LDX #$1E   ; else error $1E, break err...

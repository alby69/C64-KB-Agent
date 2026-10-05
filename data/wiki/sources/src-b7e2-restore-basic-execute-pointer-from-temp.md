---
id: src-b7e2-restore-basic-execute-pointer-from-temp
type: source
title: 'Source Summary: restore BASIC execute pointer from temp'
aliases:
- restore BASIC execute pointer from temp
- b7e2-restore-basic-execute-pointer-from-temp.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b7e2-restore-basic-execute-pointer-from-temp.md
  sha256: e7b43bdfe66b41db9eb46148b23cd0d3cb3c7542ba8c3c6158e8c595f38d13e9
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: restore BASIC execute pointer from temp

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b7e2-restore-basic-execute-pointer-from-temp.md`
**SHA256**: `e7b43bdfe66b41db9eb46148b23cd0d3cb3c7542ba8c3c6158e8c595f38d13e9`

## Summary



# $B7E2 — restore BASIC execute pointer from temp

## Disassemblatura
```assembly
.B7E2  A6 71    LDX $71   ; get BASIC execute pointer low byte back
.B7E4  A4 72    LDY $72   ; get BASIC execute pointer high byte back
.B7E6  86 7A    STX $7A   ; save BASIC execute pointer low byte
.B7E8  84 7B    STY $7B   ; save BASIC execute pointer high byte
.B7EA  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$B7E2**: get BASIC execute pointer low byte back
- **$B7E4**: get BASIC execut...

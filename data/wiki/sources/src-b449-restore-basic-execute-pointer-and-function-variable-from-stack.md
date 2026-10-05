---
id: src-b449-restore-basic-execute-pointer-and-function-variable-from-stack
type: source
title: 'Source Summary: restore BASIC execute pointer and function variable from stack'
aliases:
- restore BASIC execute pointer and function variable from stack
- b449-restore-basic-execute-pointer-and-function-variable-from-stack.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b449-restore-basic-execute-pointer-and-function-variable-from-stack.md
  sha256: a034b6625984c6f079f27116c9d281fa62807c09d0db3383854ecf279a2dcceb
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: restore BASIC execute pointer and function variable from stack

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b449-restore-basic-execute-pointer-and-function-variable-from-stack.md`
**SHA256**: `a034b6625984c6f079f27116c9d281fa62807c09d0db3383854ecf279a2dcceb`

## Summary



# $B449 — restore BASIC execute pointer and function variable from stack

## Disassemblatura
```assembly
.B449  68       PLA   ; pull BASIC execute pointer low byte
.B44A  85 7A    STA $7A   ; save BASIC execute pointer low byte
.B44C  68       PLA   ; pull BASIC execute pointer high byte
.B44D  85 7B    STA $7B   ; save BASIC execute pointer high byte put execute pointer and variable pointer into function
.B44F  A0 00    LDY #$00   ; clear index
.B451  68       PLA   ; pull BASIC execute poin...

---
id: src-fe66-user-function-default-vector
type: source
title: 'Source Summary: user function default vector'
aliases:
- user function default vector
- fe66-user-function-default-vector.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fe66-user-function-default-vector.md
  sha256: 7e55025a74c6ee426bb84bdbc7b8bee6c444a0914cafa128853084a69c9612f6
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: user function default vector

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/fe66-user-function-default-vector.md`
**SHA256**: `7e55025a74c6ee426bb84bdbc7b8bee6c444a0914cafa128853084a69c9612f6`

## Summary



# $FE66 — user function default vector

## Disassemblatura
```assembly
.FE66  20 15 FD JSR $FD15   ; restore default I/O vectors
.FE69  20 A3 FD JSR $FDA3   ; initialise SID, CIA and IRQ
.FE6C  20 18 E5 JSR $E518   ; initialise the screen and keyboard
.FE6F  6C 02 A0 JMP ($A002)   ; do BASIC break entry
```


## Commenti

### Original Disassembly (—)
- **$FE66**: restore default I/O vectors
- **$FE69**: initialise SID, CIA and IRQ
- **$FE6C**: initialise the screen and keyboard
- **$FE6F**: do...

---
id: src-b761-pull-string-data-and-byte-parameter-from-stack
type: source
title: 'Source Summary: pull string data and byte parameter from stack'
aliases:
- pull string data and byte parameter from stack
- b761-pull-string-data-and-byte-parameter-from-stack.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b761-pull-string-data-and-byte-parameter-from-stack.md
  sha256: 128869faa4008fa5f00662a0c16407dcb22b958b8f8e7c2a0cb48371eb1f5d0d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: pull string data and byte parameter from stack

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b761-pull-string-data-and-byte-parameter-from-stack.md`
**SHA256**: `128869faa4008fa5f00662a0c16407dcb22b958b8f8e7c2a0cb48371eb1f5d0d`

## Summary



# $B761 — pull string data and byte parameter from stack

## Disassemblatura
```assembly
.B761  20 F7 AE JSR $AEF7   ; scan for ")", else do syntax error then warm start
.B764  68       PLA   ; pull return address low byte
.B765  A8       TAY   ; save return address low byte
.B766  68       PLA   ; pull return address high byte
.B767  85 55    STA $55   ; save return address high byte
.B769  68       PLA   ; dump call to function vector low byte
.B76A  68       PLA   ; dump call to function ve...

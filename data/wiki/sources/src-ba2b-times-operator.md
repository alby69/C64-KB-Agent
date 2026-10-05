---
id: src-ba2b-times-operator
type: source
title: 'Source Summary: times operator'
aliases:
- times operator
- ba2b-times-operator.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/ba2b-times-operator.md
  sha256: 4066060d93a0a4c424259c026af8dba9d9d5fb23f36dc00a3b454d8945827bce
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: times operator

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/ba2b-times-operator.md`
**SHA256**: `4066060d93a0a4c424259c026af8dba9d9d5fb23f36dc00a3b454d8945827bce`

## Summary



# $BA2B — times operator

## Disassemblatura
```assembly
.BA2B  D0 03    BNE $BA30
.BA2D  4C 8B BA JMP $BA8B
.BA30  20 B7 BA JSR $BAB7
.BA33  A9 00    LDA #$00
.BA35  85 26    STA $26
.BA37  85 27    STA $27
.BA39  85 28    STA $28
.BA3B  85 29    STA $29
.BA3D  A5 70    LDA $70
.BA3F  20 59 BA JSR $BA59
.BA42  A5 65    LDA $65
.BA44  20 59 BA JSR $BA59
.BA47  A5 64    LDA $64
.BA49  20 59 BA JSR $BA59
.BA4C  A5 63    LDA $63
.BA4E  20 59 BA JSR $BA59
.BA51  A5 62    LDA $62
.BA53  20 5E BA JS...

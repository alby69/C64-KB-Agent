---
id: src-b6a3-evaluate-string
type: source
title: 'Source Summary: evaluate string'
aliases:
- evaluate string
- b6a3-evaluate-string.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b6a3-evaluate-string.md
  sha256: bca28b4d01910fc60b174db12e4680a42f4a70e0d721e54a8aa1f8efac63b0d9
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: evaluate string

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b6a3-evaluate-string.md`
**SHA256**: `bca28b4d01910fc60b174db12e4680a42f4a70e0d721e54a8aa1f8efac63b0d9`

## Summary



# $B6A3 — evaluate string

## Disassemblatura
```assembly
.B6A3  20 8F AD JSR $AD8F   ; check if source is string, else do type mismatch pop string off descriptor stack, or from top of string space returns with A = length, X = pointer low byte, Y = pointer high byte
.B6A6  A5 64    LDA $64   ; get descriptor pointer low byte
.B6A8  A4 65    LDY $65   ; get descriptor pointer high byte pop (YA) descriptor off stack or from top of string space returns with A = length, X = pointer low byte, Y = p...

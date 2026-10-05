---
id: src-ad8a-evaluate-expression-and-check-type-mismatch
type: source
title: 'Source Summary: evaluate expression and check type mismatch'
aliases:
- evaluate expression and check type mismatch
- ad8a-evaluate-expression-and-check-type-mismatch.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/ad8a-evaluate-expression-and-check-type-mismatch.md
  sha256: a0d8cb1c576de242dc9af87e90d34ff05a81263e77244d95ed76f2b9e7ed82f3
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: evaluate expression and check type mismatch

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/ad8a-evaluate-expression-and-check-type-mismatch.md`
**SHA256**: `a0d8cb1c576de242dc9af87e90d34ff05a81263e77244d95ed76f2b9e7ed82f3`

## Summary



# $AD8A — evaluate expression and check type mismatch

## Disassemblatura
```assembly
.AD8A  20 9E AD JSR $AD9E   ; evaluate expression check if source and destination are numeric
.AD8D  18       CLC
.AD8E  24       .BYTE $24   ; makes next line BIT $38 check if source and destination are string
.AD8F  38       SEC   ; destination is string type match check, set C for string, clear C for numeric
.AD90  24 0D    BIT $0D   ; test data type flag, $FF = string, $00 = numeric
.AD92  30 03    BMI $A...

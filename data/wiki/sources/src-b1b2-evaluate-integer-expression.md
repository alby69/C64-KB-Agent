---
id: src-b1b2-evaluate-integer-expression
type: source
title: 'Source Summary: evaluate integer expression'
aliases:
- evaluate integer expression
- b1b2-evaluate-integer-expression.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b1b2-evaluate-integer-expression.md
  sha256: 00d07214ec7d6d61ea9b7962dd7656465c5b8fffb87dc3c9f5ff7d1495f12bb1
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: evaluate integer expression

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b1b2-evaluate-integer-expression.md`
**SHA256**: `00d07214ec7d6d61ea9b7962dd7656465c5b8fffb87dc3c9f5ff7d1495f12bb1`

## Summary



# $B1B2 — evaluate integer expression

## Disassemblatura
```assembly
.B1B2  20 73 00 JSR $0073   ; increment and scan memory
.B1B5  20 9E AD JSR $AD9E   ; evaluate expression evaluate integer expression, sign check
.B1B8  20 8D AD JSR $AD8D   ; check if source is numeric, else do type mismatch
.B1BB  A5 66    LDA $66   ; get FAC1 sign (b7)
.B1BD  30 0D    BMI $B1CC   ; do illegal quantity error if -ve evaluate integer expression, no sign check
.B1BF  A5 61    LDA $61   ; get FAC1 exponent
.B1...

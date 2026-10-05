---
id: src-ae20-get-vector-execute-function-then-continue-evaluation
type: source
title: 'Source Summary: get vector, execute function then continue evaluation'
aliases:
- get vector, execute function then continue evaluation
- ae20-get-vector-execute-function-then-continue-evaluation.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/ae20-get-vector-execute-function-then-continue-evaluation.md
  sha256: 08b0b2fa81b58c3ed38803914d770e6e49937fcc4ac53f559466ef323a331e1b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: get vector, execute function then continue evaluation

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/ae20-get-vector-execute-function-then-continue-evaluation.md`
**SHA256**: `08b0b2fa81b58c3ed38803914d770e6e49937fcc4ac53f559466ef323a331e1b`

## Summary



# $AE20 — get vector, execute function then continue evaluation

## Disassemblatura
```assembly
.AE20  B9 82 A0 LDA $A082,Y   ; get function vector high byte
.AE23  48       PHA   ; onto stack
.AE24  B9 81 A0 LDA $A081,Y   ; get function vector low byte
.AE27  48       PHA   ; onto stack now push sign, round FAC1 and put on stack
.AE28  20 33 AE JSR $AE33   ; function will return here, then the next RTS will call the function
.AE2B  A5 4D    LDA $4D   ; get comparison evaluation flag
.AE2D  4C...

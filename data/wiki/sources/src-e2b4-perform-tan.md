---
id: src-e2b4-perform-tan
type: source
title: 'Source Summary: perform TAN()'
aliases:
- perform TAN()
- e2b4-perform-tan.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e2b4-perform-tan.md
  sha256: 2f2a43dd7c9547d6f30c4eb0a101dd4f32cf4f302c2a006628b7f931b8898414
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform TAN()

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e2b4-perform-tan.md`
**SHA256**: `2f2a43dd7c9547d6f30c4eb0a101dd4f32cf4f302c2a006628b7f931b8898414`

## Summary



# $E2B4 — perform TAN()

## Disassemblatura
```assembly
.E2B4  20 CA BB JSR $BBCA   ; pack FAC1 into $57
.E2B7  A9 00    LDA #$00   ; clear A
.E2B9  85 12    STA $12   ; clear the comparison evaluation flag
.E2BB  20 6B E2 JSR $E26B   ; perform SIN()
.E2BE  A2 4E    LDX #$4E   ; set sin(n) pointer low byte
.E2C0  A0 00    LDY #$00   ; set sin(n) pointer high byte
.E2C2  20 F6 E0 JSR $E0F6   ; pack FAC1 into (XY)
.E2C5  A9 57    LDA #$57   ; set n pointer low byte
.E2C7  A0 00    LDY #$00   ; s...

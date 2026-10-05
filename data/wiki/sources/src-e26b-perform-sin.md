---
id: src-e26b-perform-sin
type: source
title: 'Source Summary: perform SIN()'
aliases:
- perform SIN()
- e26b-perform-sin.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e26b-perform-sin.md
  sha256: f098472728b2100be7699be8ba6c200e1ecaa69531a55194d026c38f5fafb853
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform SIN()

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e26b-perform-sin.md`
**SHA256**: `f098472728b2100be7699be8ba6c200e1ecaa69531a55194d026c38f5fafb853`

## Summary



# $E26B — perform SIN()

## Disassemblatura
```assembly
.E26B  20 0C BC JSR $BC0C   ; round and copy FAC1 to FAC2
.E26E  A9 E5    LDA #$E5   ; set 2*pi pointer low byte
.E270  A0 E2    LDY #$E2   ; set 2*pi pointer high byte
.E272  A6 6E    LDX $6E   ; get FAC2 sign (b7)
.E274  20 07 BB JSR $BB07   ; divide by (AY) (X=sign)
.E277  20 0C BC JSR $BC0C   ; round and copy FAC1 to FAC2
.E27A  20 CC BC JSR $BCCC   ; perform INT()
.E27D  A9 00    LDA #$00   ; clear byte
.E27F  85 6F    STA $6F   ; cl...
